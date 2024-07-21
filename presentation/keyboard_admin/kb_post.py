import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboard_admin.kb_admin import BackMainMenu


class ChannelPost(CallbackData, prefix="ChannelPost"):
    id: str


class ChannelPostPageCallback(CallbackData, prefix="ChannelPostPageCallback"):
    page: int


def channel_post_kb(current_page: int, channels):
    total_pages = math.ceil(len(channels) / 10)
    keyboard = []

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(channels))

    for i in range(start_index, end_index):
        identify = channels[i]['title']

        keyboard.append([InlineKeyboardButton(
            text=identify,
            callback_data=ChannelPost(id=channels[i]['channel_id'], page_back=current_page).pack()
        )])

    if len(channels) > 5:
        nav = []
        # Navigation buttons
        if current_page > 1:
            nav.append(InlineKeyboardButton(
                text='<',
                callback_data=ChannelPostPageCallback(page=current_page - 1).pack()
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
                callback_data=ChannelPostPageCallback(page=current_page + 1).pack()
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


kb_back_post = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMainMenu().pack())]
])


class SkipMediaPost(CallbackData, prefix="SkipMediaPost"):
    pass


kb_back_post_skip_media = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.SKIP(), callback_data=SkipMediaPost().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMainMenu().pack())]
])


class SkipButtonPost(CallbackData, prefix="SkipButtonPost"):
    skip: bool


kb_back_post_skip_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.YES(), callback_data=SkipButtonPost(skip=False).pack())],
    [InlineKeyboardButton(text=L.SKIP(), callback_data=SkipButtonPost(skip=True).pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMainMenu().pack())]
])


class RepeatButtonPost(CallbackData, prefix="RepeatButtonPost"):
    repeat: bool


kb_repeat_button_post = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.YES(), callback_data=RepeatButtonPost(repeat=True).pack())],
    [InlineKeyboardButton(text=L.NO(), callback_data=RepeatButtonPost(repeat=False).pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMainMenu().pack())]
])


class PreviewPost(CallbackData, prefix="PreviewPost"):
    pass


kb_preview_post = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.POST.SEND(), callback_data=PreviewPost().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMainMenu().pack())]
])
