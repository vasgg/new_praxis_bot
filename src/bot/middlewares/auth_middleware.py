from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from bot.internal.ngrok_whistles import blink1_blue, sheet_update
from config import settings
from bot.controllers import add_user_to_db, get_user_from_db_by_tg_id
from enums import Stage


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        session = data['db_session']
        user = await get_user_from_db_by_tg_id(event.from_user.id, session)
        if not user:
            user = await add_user_to_db(event.from_user, session)
            if settings.STAGE == Stage.PROD:
                await blink1_blue()
                await sheet_update('C4', user.id)
        data['user'] = user
        return await handler(event, data)
