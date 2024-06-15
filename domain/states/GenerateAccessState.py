from aiogram.fsm.state import StatesGroup, State


class GenerateAccessState(StatesGroup):
    comment = State()
    days = State()
    userid = State()

