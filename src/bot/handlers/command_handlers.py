from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from bot.internal.keyboards import about_kb, main_menu_kb
from bot.internal.texts import replies
from enums import Feedback, States

router = Router()


@router.message(CommandStart())
async def start(
    message: types.Message,
    state: FSMContext,
) -> None:
    await state.clear()
    await message.answer(text=replies['start_message'],
                         reply_markup=main_menu_kb)


@router.message(Command('form'))
async def form(message: types.Message, state: FSMContext) -> None:
    await message.answer(text=replies['input_name'])
    await state.set_state(States.INPUT_NAME)


@router.callback_query(F.data == 'form')
async def form(call: types.CallbackQuery, state: FSMContext) -> None:
    await call.answer()
    await call.message.answer(text=replies['input_name'])
    await state.set_state(States.INPUT_NAME)


@router.message(Command('about'))
async def about(message: types.Message) -> None:
    await message.answer(text=replies['about'], reply_markup=about_kb)


@router.callback_query(F.data == 'about')
async def about(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['about'], reply_markup=about_kb)


@router.message(Command('donate'))
async def donate(message: types.Message) -> None:
    await message.answer(text=replies['donate'])


@router.callback_query(F.data == 'donate')
async def donate(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['donate'])


@router.message(Command('contacts'))
async def contact(message: types.Message) -> None:
    await message.answer(text=replies['contacts'])


@router.callback_query(F.data == 'contacts')
async def contact(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['contacts'])


@router.message(Command('feedback'))
async def feedback(message: types.Message, state: FSMContext) -> None:
    await message.answer(text=replies['feedback'])
    await state.set_state(Feedback.INPUT_FEEDBACK)


@router.callback_query(F.data == 'feedback')
async def feedback(call: types.CallbackQuery, state: FSMContext) -> None:
    await call.answer()
    await call.message.answer(text=replies['feedback'])
    await state.set_state(Feedback.INPUT_FEEDBACK)
