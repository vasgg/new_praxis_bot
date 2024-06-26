import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.types import TelegramObject, Update


class UpdatesDumperMiddleware(BaseMiddleware):
    # TODO: переделать логгинг на дамп в отдельную таблицу
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        json_event = event.model_dump_json(exclude_unset=True)

        res = await handler(event, data)
        if res is UNHANDLED:
            logging.info(json_event)
        return res
