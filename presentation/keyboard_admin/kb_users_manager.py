import math

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.constants.Basic import BACK


class UsersCallback(CallbackData, prefix="users*manager"):
    id: str
    page_back: int


class UsersPageCallback(CallbackData, prefix="page*users*callback"):
    page: int


def users_pagination_keyboard(current_page: int, users):
    total_pages = math.ceil(len(users) / 10)
    keyboard = InlineKeyboardBuilder()

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(users))

    for i in range(start_index, end_index):
        identify = f"{users[i]['firstname']} | {users[i]['username']}"

        keyboard.row(InlineKeyboardButton(
            text=identify,
            callback_data=UsersCallback(id=users[i]['userid'], page_back=current_page).pack()
        ))

    nav = []
    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<<--',
            callback_data=UsersPageCallback(page=current_page - 1).pack()
        ))

    nav.append(InlineKeyboardButton(
        text=BACK,
        callback_data="BACKCATEGORY"
    ))

    if current_page < total_pages:
        nav.append(InlineKeyboardButton(
            text='-->>',
            callback_data=UsersPageCallback(page=current_page + 1).pack()
        ))

    keyboard.row(*nav)

    return keyboard.as_markup()


def user_detail_back(page_back):
    return InlineKeyboardBuilder([[InlineKeyboardButton(text=BACK, callback_data=f"BACKUSERS_{page_back}")]]).as_markup()
