from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class GetAllUsers(CallbackData, prefix="GetAllUsers"):
    pass


class NotificationForUsers(CallbackData, prefix="NotificationForUsers"):
    pass


class ShowCannels(CallbackData, prefix="ShowCannels"):
    pass


class CreatePost(CallbackData, prefix="CreatePost"):
    pass


kb_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.ALL_USERS(), callback_data=GetAllUsers().pack())],
    [InlineKeyboardButton(text=L.ADMIN.MESSAGING(), callback_data=NotificationForUsers().pack())],
    [InlineKeyboardButton(text=L.ADMIN.CHANNELS(), callback_data=ShowCannels().pack())],
    [InlineKeyboardButton(text=L.ADMIN.POST(), callback_data=CreatePost().pack())],
])


class BackMainMenu(CallbackData, prefix="BackMainMenu"):
    pass
