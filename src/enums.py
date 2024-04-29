from enum import StrEnum, auto

from aiogram.filters.state import State, StatesGroup


class States(StatesGroup):
    INPUT_NAME = State()
    INPUT_AGE = State()
    INPUT_PROBLEM = State()
    INPUT_THERAPIST = State()
    INPUT_PERFORMATIVE = State()
    INPUT_INDIVIDUAL = State()
    INPUT_PRICE = State()
    INPUT_ON_PLACE = State()
    INPUT_EXPERIENCE = State()
    INPUT_MORE = State()
    INPUT_TELEGRAM = State()
    INPUT_RECOMMENDED = State()


class Stage(StrEnum):
    DEV = auto()
    PROD = auto()


class Action(StrEnum):
    CONFIRM = auto()
    CHANGE = auto()
