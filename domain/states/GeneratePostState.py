from aiogram.fsm.state import StatesGroup, State


class GeneratePostState(StatesGroup):
    Channel = State()
    Name = State()
    Year = State()
    Temp = State()
    Desc = State()
    Media = State()
    ButtonText = State()
    ButtonUrl = State()
    ButtonRepeat = State()
    Preview = State()


