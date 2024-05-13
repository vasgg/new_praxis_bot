from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import FeedbackMessage, Form, User
from enums import States


async def add_user_to_db(user, db_session) -> User:
    new_user = User(
        telegram_id=user.id,
        fullname=user.full_name,
        username=user.username,
    )
    db_session.add(new_user)
    await db_session.flush()
    return new_user


async def get_user_from_db_by_tg_id(telegram_id: int, db_session: AsyncSession) -> User:
    query = select(User).filter(User.telegram_id == telegram_id)
    result: Result = await db_session.execute(query)
    user = result.scalar()
    return user


def get_form_field_type_text(state: str) -> str:
    form_field_to_text = {
        States.INPUT_NAME: 'Имя',
        States.INPUT_AGE: 'Возраст',
        States.INPUT_PROBLEM: 'Для чего ищете терапевта? Какие задачи хотите решить?',
        States.INPUT_THERAPIST: 'Какого терапевта вы ищете сейчас? Почему это важно?',
        States.INPUT_PERFORMATIVE: 'Лучше, чтобы терапевт был',
        States.INPUT_INDIVIDUAL: 'Индивидуально или вдвоём с партнёром/родителем/ребёнком?',
        States.INPUT_PRICE: 'Сколько вы готовы платить за час терапии?',
        States.INPUT_ON_PLACE: 'Очные встречи или онлайн?',
        States.INPUT_EXPERIENCE: 'Расскажите о своём опыте обращений к психологам, психотерапевтам или психиатрам.',
        States.INPUT_MORE: 'Что ещё важного мы не спросили?',
        States.INPUT_RECOMMENDED: 'Как вы узнали о Новой практике?',
    }
    return form_field_to_text.get(state)


def get_state_by_text(text: str) -> str:
    text_to_state = {
        'input_name': States.INPUT_NAME,
        'input_age': States.INPUT_AGE,
        'input_problem': States.INPUT_PROBLEM,
        'input_therapist': States.INPUT_THERAPIST,
        'input_performative': States.INPUT_PERFORMATIVE,
        'input_individual': States.INPUT_INDIVIDUAL,
        'input_price': States.INPUT_PRICE,
        'input_on_place': States.INPUT_ON_PLACE,
        'input_experience': States.INPUT_EXPERIENCE,
        'input_more': States.INPUT_MORE,
        'input_recommended': States.INPUT_RECOMMENDED,
    }
    return text_to_state.get(text)


async def get_user_tg_id_from_record(mode: str, record_id: int, db_session: AsyncSession) -> int:
    match mode:
        case 'FORM':
            query = select(Form.user_telegram_id).filter(Form.id == record_id)
        case 'FEEDBACK':
            query = select(FeedbackMessage.user_telegram_id).filter(FeedbackMessage.id == record_id)
        case _:
            msg = f"Unexpected data type: {mode}"
            raise AssertionError(msg)
    result: Result = await db_session.execute(query)
    return result.scalar()
