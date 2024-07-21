from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_menu_user(url):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.USER.OPEN_CHANNEL(), url=url)],
    ])
