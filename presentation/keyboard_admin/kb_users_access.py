import math

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.constants.Basic import BACK


class AccessesCallback(CallbackData, prefix="access*manager"):
    uuid: str
    page_back: int


class AccessesPageCallback(CallbackData, prefix="page*access*callback"):
    page: int


def accesses_pagination_keyboard(current_page: int, accesses):
    total_pages = math.ceil(len(accesses) / 10)
    keyboard = InlineKeyboardBuilder()

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(accesses))

    for i in range(start_index, end_index):
        activate = accesses[i]['harddrive_id'] is not None
        keyboard.row(InlineKeyboardButton(
            text=f"{activate} | {accesses[i]['comment']}",
            callback_data=AccessesCallback(uuid=accesses[i]['uuid_key'], page_back=current_page).pack()
        ))

    nav = []
    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<<--',
            callback_data=AccessesPageCallback(page=current_page - 1).pack()
        ))
    nav.append(InlineKeyboardButton(
        text=BACK,
        callback_data="BACKCATEGORY"
    ))
    if current_page < total_pages:
        nav.append(InlineKeyboardButton(
            text='-->>',
            callback_data=AccessesPageCallback(page=current_page + 1).pack()
        ))

    keyboard.row(*nav)

    return keyboard.as_markup()


def access_detail_back(page_back):
    return InlineKeyboardBuilder(
        [[InlineKeyboardButton(text=BACK, callback_data=f"BACKACCESSES_{page_back}")]]).as_markup()
