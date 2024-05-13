import contextlib
import logging

from aiogram import F, Router, types
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.controllers import get_user_tg_id_from_record
from src.bot.filter import ChatTypeFilter
from src.config import settings

router = Router()
logger = logging.getLogger(__name__)


@router.message(ChatTypeFilter(chat_type=["group", "supergroup"]), F.text)
async def handle_messages(message: types.Message, db_session: AsyncSession):
    with contextlib.suppress(AttributeError, ValidationError):
        if message.reply_to_message.forward_origin.chat.id == settings.CHANNEL_ID:
            chat_id = await get_user_tg_id_from_record(str(message.reply_to_message.text.split(" ")[0]),
                                                       int(message.reply_to_message.text.split(" ")[1]),
                                                       db_session)
        await message.bot.copy_message(
            chat_id=chat_id,
            from_chat_id=message.chat.id,
            message_id=message.message_id,
        )
        logger.info(f'New comment message: {message.text} from {message.from_user.full_name}')
