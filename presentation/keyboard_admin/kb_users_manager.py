import math

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.constants.Basic import BACK


class UsersCallback(CallbackData, prefix="users*manager"):
    id: str


class UsersPageCallback(CallbackData, prefix="page*users*callback"):
    page: int


def users_pagination_keyboard(current_page: int, users):
    total_pages = math.ceil(len(users) / 10)
    keyboard = []

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(users))

    for i in range(start_index, end_index):
        keyboard.append([InlineKeyboardButton(
            text=users[i]['userid'],
            callback_data=UsersCallback(id=users[i]['userid']).pack()
        )])

    # Navigation buttons
    if current_page > 1:
        keyboard.append([InlineKeyboardButton(
            text='<<--',
            callback_data=UsersPageCallback(page=current_page - 1).pack()
        )])
    if current_page < total_pages:
        keyboard.append([InlineKeyboardButton(
            text='-->>',
            callback_data=UsersPageCallback(page=current_page + 1).pack()
        )])

    keyboard.append([InlineKeyboardButton(
        text=BACK,
        callback_data="BACKCATEGORY"
    )])

    return InlineKeyboardBuilder(markup=keyboard).as_markup()


user_detail_back = InlineKeyboardBuilder([[InlineKeyboardButton(text=BACK, callback_data="BACKUSERS")]]).as_markup()