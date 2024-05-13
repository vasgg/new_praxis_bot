import logging

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.internal.texts import replies
from src.config import settings
from src.database.models import FeedbackMessage, User
from src.enums import Feedback

router = Router()
logger = logging.getLogger(__name__)


@router.message(Feedback.INPUT_FEEDBACK, F.text)
async def input_feedback(message: types.Message, user: User, state: FSMContext, db_session: AsyncSession) -> None:
    text = str(message.text)
    await state.update_data(text=text,
                            user_telegram_id=user.telegram_id,
                            user_fullname=user.fullname)
    data = await state.get_data()
    new_feedback = FeedbackMessage(**data)
    db_session.add(new_feedback)
    await db_session.flush()
    username = message.from_user.full_name + ' @' + message.from_user.username if message.from_user.username else message.from_user.full_name
    channel_message_text = replies['new_feedback_message'].format(new_feedback.id, username) + text
    await message.bot.send_message(
        chat_id=settings.CHANNEL_ID,
        text=channel_message_text,
    )
    logger.info(f'New feedback message: {text} from {user.fullname}')
    await state.clear()
