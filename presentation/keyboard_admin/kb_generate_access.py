import math

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.constants.Basic import BACK
from data.constants.Operation import SKIP, NOTIFY_SEND

generate_access_back = InlineKeyboardBuilder([[InlineKeyboardButton(text=BACK, callback_data="BACKCATEGORY")]]).as_markup()

kb_skip_generate = InlineKeyboardBuilder([
    [InlineKeyboardButton(text=SKIP, callback_data="SKIPUSERID")],
    [InlineKeyboardButton(text=BACK, callback_data="BACKCATEGORY")]
]).as_markup()
