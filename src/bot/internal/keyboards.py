from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Заполнить анкету', callback_data='form'),
            InlineKeyboardButton(text='Как это работает', callback_data='how_it_works'),
        ],
        [
            InlineKeyboardButton(text='О проекте', callback_data='about'),
            InlineKeyboardButton(text='Поддержать проект', callback_data='donate'),
        ],
        [
            InlineKeyboardButton(text='Связаться с нами', callback_data='contact'),
            InlineKeyboardButton(text='Дать фидбэк', callback_data='feedback'),
        ],
    ]
)
