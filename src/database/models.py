from datetime import datetime
from typing import Any

from sqlalchemy import BigInteger, ForeignKey, JSON, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}
    type_annotation_map = {dict[str, Any]: JSON}

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, server_default=func.now())


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    fullname: Mapped[str]
    username: Mapped[str | None] = mapped_column(String(32))

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, ' f'telegram_id={self.telegram_id}, fullname={self.fullname})'

    def __repr__(self):
        return str(self)


class Form(Base):
    __tablename__ = 'forms'

    user_telegram_id: Mapped[int] = mapped_column(ForeignKey('users.telegram_id'))
    user_fullname: Mapped[str] = mapped_column(ForeignKey('users.fullname'))
    name: Mapped[str]
    age: Mapped[int]
    problem: Mapped[str]
    therapist: Mapped[str]
    performative: Mapped[str]
    individual: Mapped[str]
    price: Mapped[str]
    on_place: Mapped[str]
    experience: Mapped[str]
    more: Mapped[str]
    recommended: Mapped[str]


class FeedbackMessage(Base):
    __tablename__ = 'feedbacks'

    user_telegram_id: Mapped[int] = mapped_column(ForeignKey('users.telegram_id'))
    user_fullname: Mapped[str] = mapped_column(ForeignKey('users.fullname'))
    text: Mapped[str]
