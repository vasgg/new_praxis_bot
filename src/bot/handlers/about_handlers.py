from aiogram import F, Router, types

from src.bot.internal.texts import replies

router = Router()


@router.callback_query(F.data == 'how_it_works')
async def how_it_works(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['how_it_works'])


@router.callback_query(F.data == 'its_free')
async def its_free(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['its_free'])


@router.callback_query(F.data == 'money')
async def money(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['money'])


@router.callback_query(F.data == 'choice')
async def choice(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['choice'])


@router.callback_query(F.data == 'difference')
async def difference(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['difference'])


@router.callback_query(F.data == 'education')
async def education(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['education'])


@router.callback_query(F.data == 'reviews')
async def reviews(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['reviews'])


@router.callback_query(F.data == 'cooperation')
async def cooperation(call: types.CallbackQuery) -> None:
    await call.answer()
    await call.message.answer(text=replies['cooperation'])


@router.message(F.text)
async def no_state(message: types.Message) -> None:
    await message.answer(text=replies['no_state'])
