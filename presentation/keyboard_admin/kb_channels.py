import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.keyboard_admin.kb_admin import BackMainMenu


class ChannelCalback(CallbackData, prefix="ChannelCalback"):
    id: str


class ChannelPageCallback(CallbackData, prefix="ChannelPageCallback"):
    page: int


def channel_pagination_keyboard(current_page: int, channels):
    total_pages = math.ceil(len(channels) / 10)
    keyboard = []

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(channels))

    for i in range(start_index, end_index):
        identify = channels[i]['title']

        keyboard.append([InlineKeyboardButton(
            text=identify,
            callback_data=ChannelCalback(id=channels[i]['channel_id'], page_back=current_page).pack()
        )])

    if len(channels) > 5:
        nav = []
        # Navigation buttons
        if current_page > 1:
            nav.append(InlineKeyboardButton(
                text='<',
                callback_data=ChannelPageCallback(page=current_page - 1).pack()
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
                callback_data=ChannelPageCallback(page=current_page + 1).pack()
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


class ChannelListBack(CallbackData, prefix="ChannelListBack"):
    pass


class DeleteChannel(CallbackData, prefix="DeleteChannel"):
    pass


class CreateLink(CallbackData, prefix="CreateLink"):
    pass


class ManageLinks(CallbackData, prefix="ManageLinks"):
    pass


class ChannelDetailBack(CallbackData, prefix="ChannelDetailBack"):
    pass


channel_detail = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.CHANNEL.DELETE(), callback_data=DeleteChannel().pack())],
    [InlineKeyboardButton(text=L.ADMIN.CHANNEL.MANAGE_LINK(), callback_data=ManageLinks().pack())],
    [InlineKeyboardButton(text=L.ADMIN.CHANNEL.CREATE_LINK(), callback_data=CreateLink().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ChannelListBack().pack())]
])
