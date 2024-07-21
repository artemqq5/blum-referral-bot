import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.keyboard_admin.kb_admin import BackMainMenu


class UsersCallback(CallbackData, prefix="users*manager"):
    id: str
    page_back: int


class UsersPageCallback(CallbackData, prefix="page*users*callback"):
    page: int


def users_pagination_keyboard(current_page: int, users):
    total_pages = math.ceil(len(users) / 10)
    keyboard = []

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(users))

    for i in range(start_index, end_index):
        identify = f"{users[i]['firstname']} | {users[i]['username']}"

        keyboard.append([InlineKeyboardButton(
            text=identify,
            callback_data=UsersCallback(id=users[i]['userid'], page_back=current_page).pack()
        )])

    if users:
        nav = []
        # Navigation buttons
        if current_page > 1:
            nav.append(InlineKeyboardButton(
                text='<',
                callback_data=UsersPageCallback(page=current_page - 1).pack()
            ))
        else:
            nav.append(InlineKeyboardButton(
                text='<',
                callback_data="None"
            ))

        nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

        if current_page < total_pages:
            nav.append(InlineKeyboardButton(
                text='>',
                callback_data=UsersPageCallback(page=current_page + 1).pack()
            ))
        else:
            nav.append(InlineKeyboardButton(
                text='>',
                callback_data="None"
            ))

        keyboard.append(nav)
    keyboard.append([InlineKeyboardButton(
        text=L.BACK(),
        callback_data=BackMainMenu().pack()
    )])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def user_detail_back(page_back):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.BACK(), callback_data=f"BACKUSERS_{page_back}")]
    ])
