import math

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.constants.Basic import BACK
from data.constants.Operation import SKIP, NOTIFY_SEND

notification_back = InlineKeyboardBuilder([[InlineKeyboardButton(text=BACK, callback_data="BACKCATEGORY")]]).as_markup()

kb_skip_notification = InlineKeyboardBuilder([
    [InlineKeyboardButton(text=SKIP, callback_data="SKIPNOTIFICATION")],
    [InlineKeyboardButton(text=BACK, callback_data="BACKCATEGORY")]
]).as_markup()

kb_preview_notification = InlineKeyboardBuilder([
    [InlineKeyboardButton(text=NOTIFY_SEND, callback_data="PREVIEWNOTIFICATION")],
    [InlineKeyboardButton(text=BACK, callback_data="BACKCATEGORY")]
]).as_markup()

