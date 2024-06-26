import contextlib
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.exc import PendingRollbackError

from database.database_connector import DatabaseConnector


class DBSessionMiddleware(BaseMiddleware):
    def __init__(self, db: DatabaseConnector):
        self.db = db

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        async with self.db.session_factory() as db_session:
            data['db_session'] = db_session
            res = await handler(event, data)
            with contextlib.suppress(PendingRollbackError):
                await db_session.commit()

            return res
