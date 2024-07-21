import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.keyboard_admin.kb_admin import BackMainMenu
from presentation.keyboard_admin.kb_channels import ChannelListBack, ChannelDetailBack


class LinkCalback(CallbackData, prefix="LinkCalback"):
    link: str


class LinkPageCallback(CallbackData, prefix="LinkPageCallback"):
    page: int


def links_pagination_keyboard(current_page: int, links):
    total_pages = math.ceil(len(links) / 10)
    keyboard = []

    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(links))

    for i in range(start_index, end_index):
        identify = links[i]['link_title']

        keyboard.append([InlineKeyboardButton(
            text=identify,
            callback_data=LinkCalback(link=str(links[i]['link']).replace("https://", "")).pack()
        )])

    if len(links) > 5:
        nav = []
        # Navigation buttons
        if current_page > 1:
            nav.append(InlineKeyboardButton(
                text='<',
                callback_data=LinkPageCallback(page=current_page - 1).pack()
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
                callback_data=LinkPageCallback(page=current_page + 1).pack()
            ))
        else:
            nav.append(InlineKeyboardButton(
                text='>',
                callback_data="None"
            ))

        keyboard.append(nav)
    keyboard.append([InlineKeyboardButton(text=L.BACK(), callback_data=ChannelDetailBack().pack())])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


class ListLinkBack(CallbackData, prefix="ListLinkBack"):
    pass


kb_create_link = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ChannelDetailBack().pack())]
])


class DeleteLink(CallbackData, prefix="DeleteLink"):
    pass


kb_detail_link = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.LINK.DELETE(), callback_data=DeleteLink().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ListLinkBack().pack())]
])
