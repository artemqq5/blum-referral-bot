from aiogram.fsm.state import StatesGroup, State


class ChannelManagementState(StatesGroup):
    ShowChannels = State()
    DetailChannel = State()
    ShowLinks = State()
    DetailLink = State()
    CreateLink = State()
