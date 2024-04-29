import logging

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.controllers import get_form_field_type_text, get_state_by_text
from src.bot.internal.keyboards import ActionCallbackFactory, get_action_keyboard
from src.bot.internal.texts import replies
from src.config import settings
from src.database.models import Form, User
from src.enums import States

router = Router()
logger = logging.getLogger()


@router.callback_query(F.data == 'form')
async def start_registration(call: types.CallbackQuery, state: FSMContext) -> None:
    await call.answer()
    await call.message.answer(text=replies['input_name'])
    await state.set_state(States.INPUT_NAME)


@router.message(States.INPUT_NAME)
@router.message(States.INPUT_AGE)
@router.message(States.INPUT_PROBLEM)
@router.message(States.INPUT_THERAPIST)
@router.message(States.INPUT_PERFORMATIVE)
@router.message(States.INPUT_INDIVIDUAL)
@router.message(States.INPUT_PRICE)
@router.message(States.INPUT_ON_PLACE)
@router.message(States.INPUT_EXPERIENCE)
@router.message(States.INPUT_MORE)
@router.message(States.INPUT_TELEGRAM)
@router.message(States.INPUT_RECOMMENDED)
async def input_entity(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    await message.answer(
        text=replies['input_confirmation'].format(get_form_field_type_text(current_state), message.text),
        reply_markup=get_action_keyboard(current_state, str(message.text)),
    )


@router.callback_query(ActionCallbackFactory.filter())
async def action_button_processing(
    callback: types.CallbackQuery,
    callback_data: ActionCallbackFactory,
    state: FSMContext,
    user: User,
    db_session: AsyncSession,
) -> None:
    await callback.answer()
    await callback.message.delete()
    action = callback_data.action
    attr = callback_data.state
    text = callback_data.text
    current_state = await state.get_state()
    match action:
        case action.CONFIRM:
            match current_state:
                case States.INPUT_NAME:
                    await state.update_data(name=text)
                    await callback.message.answer(text=replies['input_age'])
                    await state.set_state(States.INPUT_AGE)
                case States.INPUT_AGE:
                    await state.update_data(age=text)
                    await callback.message.answer(text=replies['input_problem'])
                    await state.set_state(States.INPUT_PROBLEM)
                case States.INPUT_PROBLEM:
                    await state.update_data(problem=text)
                    await callback.message.answer(text=replies['input_therapist'])
                    await state.set_state(States.INPUT_THERAPIST)
                case States.INPUT_THERAPIST:
                    await state.update_data(therapist=text)
                    await callback.message.answer(text=replies['input_performative'])
                    await state.set_state(States.INPUT_PERFORMATIVE)
                case States.INPUT_PERFORMATIVE:
                    await state.update_data(performative=text)
                    await callback.message.answer(text=replies['input_individual'])
                    await state.set_state(States.INPUT_INDIVIDUAL)
                case States.INPUT_INDIVIDUAL:
                    await state.update_data(individual=text)
                    await callback.message.answer(text=replies['input_price'])
                    await state.set_state(States.INPUT_PRICE)
                case States.INPUT_PRICE:
                    await state.update_data(price=text)
                    await callback.message.answer(text=replies['input_on_place'])
                    await state.set_state(States.INPUT_ON_PLACE)
                case States.INPUT_ON_PLACE:
                    await state.update_data(on_place=text)
                    await callback.message.answer(text=replies['input_experience'])
                    await state.set_state(States.INPUT_EXPERIENCE)
                case States.INPUT_EXPERIENCE:
                    await state.update_data(experience=text)
                    await callback.message.answer(text=replies['input_more'])
                    await state.set_state(States.INPUT_MORE)
                case States.INPUT_MORE:
                    await state.update_data(more=text)
                    await callback.message.answer(text=replies['input_telegram'])
                    await state.set_state(States.INPUT_TELEGRAM)
                case States.INPUT_TELEGRAM:
                    await state.update_data(telegram=text)
                    await callback.message.answer(text=replies['input_recommended'])
                    await state.set_state(States.INPUT_RECOMMENDED)
                case States.INPUT_RECOMMENDED:
                    await state.update_data(recommended=text)
                    await state.update_data(user_id=user.id)
                    new_form = Form(**await state.get_data())
                    db_session.add(new_form)
                    await db_session.commit()
                    await state.clear()
                    logger.info(f'Form {new_form.id} created')
                    await callback.message.answer(text=replies['form_сomplete'])

                    await callback.bot.send_message(
                        chat_id=settings.ADMIN,
                        text=replies['new_form_message'].format(
                            new_form.id,
                            new_form.name,
                            new_form.age,
                            new_form.problem,
                            new_form.therapist,
                            new_form.performative,
                            new_form.individual,
                            new_form.price,
                            new_form.on_place,
                            new_form.experience,
                            new_form.more,
                            new_form.telegram,
                            new_form.recommended,
                        ),
                    )
        case action.CHANGE:
            await callback.message.answer(text=replies[attr.lower()])
            await state.set_state(get_state_by_text(attr.lower()))
