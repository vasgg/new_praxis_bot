from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Заполнить анкету', callback_data='form'),
        ],
        [
            InlineKeyboardButton(text='О проекте', callback_data='about'),
            InlineKeyboardButton(text='Поддержать проект', callback_data='donate'),
        ],
        [
            InlineKeyboardButton(text='Связаться с нами', callback_data='contacts'),
            InlineKeyboardButton(text='Дать фидбэк', callback_data='feedback'),
        ],
    ]
)


about_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Как это работает', callback_data='how_it_works'),
            InlineKeyboardButton(text='Это бесплатно?', callback_data='its_free'),
        ],
        [
            InlineKeyboardButton(text='Где деньги?', callback_data='money'),
            InlineKeyboardButton(text='Отбор терапевтов', callback_data='choice'),
        ],
        [
            InlineKeyboardButton(text='Психолог или терапевт', callback_data='difference'),
            InlineKeyboardButton(text='Образования', callback_data='education'),
        ],
        [
            InlineKeyboardButton(text='Отзывы', callback_data='reviews'),
            InlineKeyboardButton(text='Сотрудничество', callback_data='cooperation'),
        ],
    ]
)
