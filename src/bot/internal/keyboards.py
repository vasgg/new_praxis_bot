from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.enums import Action


class ActionCallbackFactory(CallbackData, prefix='action'):
    action: Action
    state: str
    text: str


def get_action_keyboard(state: str, text: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='✔︎ подтвердить',
                    callback_data=ActionCallbackFactory(
                        action=Action.CONFIRM, state=state.split(':')[1], text=text
                    ).pack(),
                ),
                InlineKeyboardButton(
                    text='✏︎ изменить',
                    callback_data=ActionCallbackFactory(
                        action=Action.CHANGE, state=state.split(':')[1], text=text
                    ).pack(),
                ),
            ],
        ],
    )


fill_form_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🖊️ Заполнить форму', callback_data='form'),
        ],
    ],
)
