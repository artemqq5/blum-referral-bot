import uuid

from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.ChannelRepository import ChannelRepository
from data.repository.PostRepository import PostRepository
from domain.notification.ChannelPost import ChannelPostMessage
from domain.routers.admin.messaging.MessagingTools import MessagingTools
from domain.states.GeneratePostState import GeneratePostState
from presentation.keyboard_admin.kb_admin import CreatePost
from presentation.keyboard_admin.kb_post import kb_back_post, kb_back_post_skip_media, SkipMediaPost, SkipButtonPost, \
    kb_back_post_skip_button, kb_preview_post, PreviewPost, kb_repeat_button_post, RepeatButtonPost, channel_post_kb, \
    ChannelPost, ChannelPostPageCallback

router = Router()


@router.callback_query(CreatePost.filter())
async def create_post_start(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.clear()

    channels = ChannelRepository().get_all_channels()

    if not channels:
        await callback.answer(i18n.ADMIN.CHANNEL.LIST_EMPTY(), show_alert=True)
        return

    await state.set_state(GeneratePostState.Channel)
    await callback.message.edit_text(i18n.ADMIN.POST.CHOICE_CHANNEL(), reply_markup=channel_post_kb(1, channels))


@router.callback_query(ChannelPostPageCallback.filter(), GeneratePostState.Channel)
async def nav_channel_post(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]

    list_channels = ChannelRepository().get_all_channels()
    await callback.message.edit_text(i18n.ADMIN.CHANNELS(), reply_markup=channel_post_kb(int(page), list_channels))


@router.callback_query(ChannelPost.filter(), GeneratePostState.Channel)
async def choice_channel_post(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    channel_id = callback.data.split(":")[1]
    await state.update_data(channel_id=channel_id)
    await state.set_state(GeneratePostState.Name)
    await callback.message.edit_text(i18n.ADMIN.POST.SET_NAME(), reply_markup=kb_back_post)


@router.message(GeneratePostState.Name)
async def set_post_name(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(name=message.text)
    await state.set_state(GeneratePostState.Year)
    await message.answer(i18n.ADMIN.POST.SET_YEAR(), reply_markup=kb_back_post)


@router.message(GeneratePostState.Year)
async def set_post_year(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(year=message.text)
    await state.set_state(GeneratePostState.Temp)
    await message.answer(i18n.ADMIN.POST.SET_TEMP(), reply_markup=kb_back_post)


@router.message(GeneratePostState.Temp)
async def set_post_temp(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(temp=message.text)
    await state.set_state(GeneratePostState.Desc)
    await message.answer(i18n.ADMIN.POST.SET_DESC(), reply_markup=kb_back_post)


@router.message(GeneratePostState.Desc)
async def set_post_desc(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 1000:
        await message.answer(i18n.ADMIN.POST.SET_DESC_ERROR(size=len(message.text)), reply_markup=kb_back_post)
        return

    await state.update_data(buttons=[])
    await state.update_data(desc=message.text)
    await state.set_state(GeneratePostState.Media)
    await message.answer(i18n.ADMIN.POST.SET_MEDIA(), reply_markup=kb_back_post_skip_media)


@router.callback_query(SkipMediaPost.filter(), GeneratePostState.Media)
async def skip_post_media(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(GeneratePostState.ButtonText)
    await callback.message.edit_text(i18n.ADMIN.POST.SET_BUTTON(), reply_markup=kb_back_post_skip_button)


@router.message(GeneratePostState.Media)
async def set_post_media(message: types.Message, state: FSMContext, i18n: I18nContext):
    if message.content_type == 'photo':
        await state.update_data(photo=message.photo[-1].file_id)
    elif message.content_type == 'animation':
        await state.update_data(animation=message.document.file_id)
    elif message.content_type == 'video':
        await state.update_data(video=message.video.file_id)
    else:
        await message.answer(i18n.ADMIN.POST.SET_MEDIA_ERROR(), reply_markup=kb_back_post_skip_media)
        return

    await state.set_state(GeneratePostState.ButtonText)
    await message.answer(i18n.ADMIN.POST.SET_BUTTON(), reply_markup=kb_back_post_skip_button)


@router.callback_query(SkipButtonPost.filter(), GeneratePostState.ButtonText)
async def skip_post_button(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    skip = callback.data.split(":")[1]
    if int(skip):
        await state.set_state(GeneratePostState.Preview)
        data = await state.get_data()
        await MessagingTools.preview_post_send(data, bot, i18n, callback.from_user.id)
        await callback.message.answer(i18n.ADMIN.POST.PREVIEW_POST(), reply_markup=kb_preview_post)
    else:
        await callback.message.edit_text(i18n.ADMIN.POST.SET_BUTTON_TEXT(), reply_markup=kb_back_post)


@router.message(GeneratePostState.ButtonText)
async def set_post_button_text(message: types.Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) > 50:
        await message.answer(i18n.ADMIN.POST.BUTTON_TEXT_ERROR(count=len(message.text)), reply_markup=kb_back_post)
        return

    await MessagingTools.add_new_button(state)
    await MessagingTools.add_text_last_button(state, message.text)
    await state.set_state(GeneratePostState.ButtonUrl)
    await message.answer(i18n.ADMIN.POST.SET_BUTTON_URL(), reply_markup=kb_back_post)


@router.message(GeneratePostState.ButtonUrl)
async def set_post_button_url(message: types.Message, state: FSMContext, i18n: I18nContext):
    if not MessagingTools.is_valid_url(message.text):
        await message.answer(i18n.ADMIN.POST.BUTTON_URL_ERROR(), reply_markup=kb_back_post)
        return

    await MessagingTools.add_url_last_button(state, message.text)
    await state.set_state(GeneratePostState.ButtonRepeat)
    await message.answer(i18n.ADMIN.POST.SET_BUTTON_NEXT(), reply_markup=kb_repeat_button_post)


@router.callback_query(RepeatButtonPost.filter(), GeneratePostState.ButtonRepeat)
async def post_repeat_button(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    repeat = callback.data.split(":")[1]
    if int(repeat):
        await state.set_state(GeneratePostState.ButtonText)
        await callback.message.edit_text(i18n.ADMIN.POST.SET_BUTTON_TEXT(), reply_markup=kb_back_post)
    else:
        await state.set_state(GeneratePostState.Preview)
        data = await state.get_data()
        await MessagingTools.preview_post_send(data, bot, i18n, callback.from_user.id)
        await callback.message.answer(i18n.ADMIN.POST.PREVIEW_POST(), reply_markup=kb_preview_post)


@router.callback_query(PreviewPost.filter(), GeneratePostState.Preview)
async def send_post_to_channel(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()

    identify = str(uuid.uuid4())
    if not PostRepository().add(data['name'], data['year'], data['temp'], data['desc'], callback.from_user.id, identify):
        await callback.answer(i18n.ADMIN.POST.SEND_ERROR_DB())
        return

    if not await ChannelPostMessage.make_post_channel(data, bot, data['channel_id'], i18n, identify):
        await callback.answer(i18n.ADMIN.POST.SEND_ERROR_TG())
        return

    await callback.message.answer(i18n.ADMIN.POST.SEND_SUCCESS())
