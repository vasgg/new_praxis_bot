import logging

from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.internal.texts import replies
from src.config import settings
from src.database.models import Form, User
from src.enums import States

router = Router()
logger = logging.getLogger(__name__)


@router.message(StateFilter(States))
async def input_entity(message: types.Message, user: User, state: FSMContext, db_session: AsyncSession) -> None:
    current_state = await state.get_state()
    text = str(message.text)
    match current_state:
        case States.INPUT_NAME:
            await state.update_data(name=text)
            await message.answer(text=replies['input_age'])
            await state.set_state(States.INPUT_AGE)
        case States.INPUT_AGE:
            await state.update_data(age=text)
            await message.answer(text=replies['input_problem'])
            await state.set_state(States.INPUT_PROBLEM)
        case States.INPUT_PROBLEM:
            await state.update_data(problem=text)
            await message.answer(text=replies['input_therapist'])
            await state.set_state(States.INPUT_THERAPIST)
        case States.INPUT_THERAPIST:
            await state.update_data(therapist=text)
            await message.answer(text=replies['input_performative'])
            await state.set_state(States.INPUT_PERFORMATIVE)
        case States.INPUT_PERFORMATIVE:
            await state.update_data(performative=text)
            await message.answer(text=replies['input_individual'])
            await state.set_state(States.INPUT_INDIVIDUAL)
        case States.INPUT_INDIVIDUAL:
            await state.update_data(individual=text)
            await message.answer(text=replies['input_price'])
            await state.set_state(States.INPUT_PRICE)
        case States.INPUT_PRICE:
            await state.update_data(price=text)
            await message.answer(text=replies['input_on_place'])
            await state.set_state(States.INPUT_ON_PLACE)
        case States.INPUT_ON_PLACE:
            await state.update_data(on_place=text)
            await message.answer(text=replies['input_experience'])
            await state.set_state(States.INPUT_EXPERIENCE)
        case States.INPUT_EXPERIENCE:
            await state.update_data(experience=text)
            await message.answer(text=replies['input_more'])
            await state.set_state(States.INPUT_MORE)
        case States.INPUT_MORE:
            await state.update_data(more=text)
            await message.answer(text=replies['input_recommended'])
            await state.set_state(States.INPUT_RECOMMENDED)
        case States.INPUT_RECOMMENDED:
            await state.update_data(recommended=text,
                                    user_telegram_id=user.telegram_id,
                                    user_fullname=user.fullname)
            data = await state.get_data()
            new_form = Form(**data)
            db_session.add(new_form)
            await db_session.flush()
            await state.clear()
            logger.info(f'Form {new_form.id} created')
            await message.answer(text=replies['form_сomplete'])
            username = message.from_user.full_name + ' @' + message.from_user.username if message.from_user.username else message.from_user.full_name
            channel_message_text = replies['new_form_message'].format(new_form.id, username) + replies['form_message_content'].format(**data)
            await message.bot.send_message(
                chat_id=settings.CHANNEL_ID,
                text=channel_message_text,
            )
