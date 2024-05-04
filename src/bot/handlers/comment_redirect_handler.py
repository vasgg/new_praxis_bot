from aiogram import Router, types

from bot.filter import ChatTypeFilter
from config import settings

router = Router()


# @router.message(ChatTypeFilter(chat_type=["group", "supergroup"]))
# async def handle_messages(message: types.Message):
#     # Проверка, что сообщение является комментарием к посту в канале
#     if message.reply_to_message:
#         await message.reply("Спасибо за ваш комментарий к посту!")
#     else:
#         await message.reply("Это обычное сообщение в чате.")
# async def handle_channel_post(message: types.Message):
#     if message.forward_from_chat:
#         print(f'its just chat message {message.text}')
#     if message.reply_to_message:
#         print(f'{message.text} zbs its reply to {message.reply_to_message.text}')

#
# @router.message()
# async def handle_chat_specific(message: types.Message):
#     await message.reply("Это сообщение только для конкретного чата!")