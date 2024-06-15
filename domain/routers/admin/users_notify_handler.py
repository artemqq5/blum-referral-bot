from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data.constants.Operation import NOTIFY_MEDIA, NOTIFY_BUTTON_URL, NOTIFY_PREVIEW, \
    NOTIFY_BUTTON_URL_VALIDATION, NOTIFY_BUTTON_TEXT, NOTIFY_BUTTON_TEXT_LIMIT, SKIP, NOTIFY_DEFAULT_BUTTON_TEXT, \
    NOTIFY_SEND, NOTIFY_MESSAGE
from domain.notification.BaseNotification import BaseNotification
from domain.states.NotificationState import NotificationState
from presentation.keyboard_admin.kb_users_notification import notification_back, kb_skip_notification, \
    kb_preview_notification

router = Router()


@router.callback_query(F.data.contains("MENU*NOTIFICATION*CALLBACK"))
async def notification_callbacl_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == 886327182:
        await state.set_state(NotificationState.Message)
        await callback.message.edit_text(NOTIFY_MESSAGE, reply_markup=notification_back)
    else:
        await callback.message.edit_text("У вас немає доступа на це", reply_markup=notification_back)


@router.callback_query(StateFilter(NotificationState), F.data.contains("SKIPNOTIFICATION"))
async def skip_step_notify(callback: CallbackQuery, state: FSMContext, bot: Bot):
    current_state = await state.get_state()

    if current_state == NotificationState.Media.state:
        await state.set_state(NotificationState.ButtonUrl)
        await callback.message.edit_text(NOTIFY_BUTTON_URL, reply_markup=kb_skip_notification)

    elif current_state == NotificationState.ButtonUrl.state:
        await state.set_state(NotificationState.Preview)
        data = await state.get_data()
        await BaseNotification.generate_message_users(data, bot, callback.from_user.id)
        await callback.message.answer(NOTIFY_PREVIEW, reply_markup=kb_preview_notification)

    elif current_state == NotificationState.ButtonText.state:
        await state.update_data(button_text=NOTIFY_DEFAULT_BUTTON_TEXT)
        data = await state.get_data()
        await BaseNotification.generate_message_users(data, bot, callback.from_user.id)
        await state.set_state(NotificationState.Preview)
        await callback.message.answer(NOTIFY_PREVIEW, reply_markup=kb_preview_notification)


@router.callback_query(NotificationState.Preview, F.data.contains("PREVIEWNOTIFICATION"))
async def skip_step_notify(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    await state.clear()

    result = await BaseNotification.notify_all(bot, data)
    await callback.message.answer(result, reply_markup=notification_back)


@router.message(NotificationState.Message)
async def message_notify(message: Message, state: FSMContext):
    await state.update_data(message=message.html_text)
    await state.set_state(NotificationState.Media)
    await message.answer(NOTIFY_MEDIA, reply_markup=kb_skip_notification)


@router.message(NotificationState.Media, (F.photo | F.animation | F.video | (F.text == SKIP)))
async def media_notify(message: Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(photo=message.photo[-1].file_id)
    elif message.content_type == 'animation':
        await state.update_data(animation=message.document.file_id)
    elif message.content_type == 'video':
        await state.update_data(video=message.video.file_id)

    await state.set_state(NotificationState.ButtonUrl)
    await message.answer(NOTIFY_BUTTON_URL, reply_markup=kb_skip_notification)


@router.message(NotificationState.ButtonUrl)
async def button_notify_url(message: Message, state: FSMContext):
    if not message.text.startswith("https://"):
        await message.answer(NOTIFY_BUTTON_URL_VALIDATION, reply_markup=kb_skip_notification)
        return

    await state.update_data(button_url=message.text)
    await state.set_state(NotificationState.ButtonText)
    await message.answer(NOTIFY_BUTTON_TEXT, reply_markup=kb_skip_notification)


@router.message(NotificationState.ButtonText)
async def button_notify_text(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(button_text=message.text)

    if len(message.text) > 50:
        await message.edit_text(NOTIFY_BUTTON_TEXT_LIMIT, reply_markup=kb_skip_notification)
        return

    data = await state.get_data()
    await BaseNotification.generate_message_users(data, bot, message.from_user.id)
    await state.set_state(NotificationState.Preview)
    await message.answer(NOTIFY_PREVIEW, reply_markup=kb_preview_notification)


