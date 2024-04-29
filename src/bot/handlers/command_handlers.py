from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from src.bot.internal.keyboards import fill_form_keyboard
from src.bot.internal.texts import replies
from src.enums import States

router = Router()


@router.message(CommandStart())
async def start_message(
    message: types.Message,
    state: FSMContext,
) -> None:
    await state.clear()
    await message.answer(text=replies['start_message'])


@router.message(Command('form'))
async def fill_form_message(message: types.Message, state: FSMContext) -> None:
    await message.answer(text=replies['fill_form'], reply_markup=fill_form_keyboard)
    await state.set_state(States.INPUT_NAME)
