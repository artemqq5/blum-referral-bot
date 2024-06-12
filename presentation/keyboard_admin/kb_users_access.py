import math

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.constants.Basic import BACK


class AccessesCallback(CallbackData, prefix="access*manager"):
    uuid: str


class AccessesPageCallback(CallbackData, prefix="page*access*callback"):
    page: int


def accesses_pagination_keyboard(current_page: int, accesses):
    total_pages = math.ceil(len(accesses) / 10)
    keyboard = []

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(accesses))

    for i in range(start_index, end_index):
        keyboard.append([InlineKeyboardButton(
            text=accesses[i]['userid'],
            callback_data=AccessesCallback(uuid=accesses[i]['uuid_key']).pack()
        )])

    # Navigation buttons
    if current_page > 1:
        keyboard.append([InlineKeyboardButton(
            text='<<--',
            callback_data=AccessesPageCallback(page=current_page - 1).pack()
        )])
    if current_page < total_pages:
        keyboard.append([InlineKeyboardButton(
            text='-->>',
            callback_data=AccessesPageCallback(page=current_page + 1).pack()
        )])

    keyboard.append([InlineKeyboardButton(
        text=BACK,
        callback_data="BACKCATEGORY"
    )])

    return InlineKeyboardBuilder(markup=keyboard).as_markup()


access_detail_back = InlineKeyboardBuilder([[InlineKeyboardButton(text=BACK, callback_data="BACKACCESSES")]]).as_markup()

