from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.Operation import *

kb_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=ALL_USERS, callback_data="MENU*USERS*CALLBACK")],
    [InlineKeyboardButton(text=ALL_ACCESS, callback_data="MENU*ACCESS*CALLBACK")],
    [InlineKeyboardButton(text=NOTIFICATION_FOR_USER, callback_data="MENU*NOTIFICATION*CALLBACK")],
])