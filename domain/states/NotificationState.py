from aiogram.fsm.state import StatesGroup, State


class NotificationState(StatesGroup):
    Message = State()
    Media = State()
    ButtonText = State()
    ButtonUrl = State()
    Preview = State()
