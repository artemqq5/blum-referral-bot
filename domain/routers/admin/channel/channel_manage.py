from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.ChannelRepository import ChannelRepository
from data.repository.LinkRepository import LinkRepository
from domain.states.ChannelManagementState import ChannelManagementState
from presentation.keyboard_admin.kb_admin import ShowCannels
from presentation.keyboard_admin.kb_channels import channel_pagination_keyboard, ChannelCalback, ChannelPageCallback, \
    channel_detail, ChannelListBack, ChannelDetailBack

router = Router()


@router.callback_query(ShowCannels.filter())
async def show_channel_handler(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ChannelManagementState.ShowChannels)
    list_channels = ChannelRepository().get_all_channels()

    if not list_channels:
        await callback.answer(i18n.ADMIN.CHANNEL.LIST_EMPTY(), show_alert=True)
        return

    data = await state.get_data()
    page = data.get("last_page_id_channel", 1) if len(list_channels) > 5 else 1

    await callback.message.edit_text(i18n.ADMIN.CHANNELS(),
                                     reply_markup=channel_pagination_keyboard(page, list_channels))


@router.callback_query(ChannelPageCallback.filter(), ChannelManagementState.ShowChannels)
async def nav_channel(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]

    await state.update_data(last_page_id_channel=int(page))

    list_channels = ChannelRepository().get_all_channels()
    await callback.message.edit_text(i18n.ADMIN.CHANNELS(),
                                     reply_markup=channel_pagination_keyboard(int(page), list_channels))


@router.callback_query(ChannelCalback.filter(), ChannelManagementState.ShowChannels)
async def show_detail_channel(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    channel_id = callback.data.split(":")[1]

    channel = ChannelRepository().get_channel(channel_id)

    links = LinkRepository().get_all(channel['channel_id'])
    users_join = 0

    for link in links:
        users_join += link['users_join']

    await state.set_state(ChannelManagementState.DetailChannel)
    await state.update_data(channel_id=channel_id)

    await callback.message.edit_text(
        i18n.ADMIN.CHANNEL.TEMPLATE(
            channel_id=channel['channel_id'],
            channel_name=channel['title'],
            date=channel['_at'],
            link_count=len(links),
            user_count=users_join
        ),
        reply_markup=channel_detail
    )


@router.callback_query(ChannelListBack.filter(), StateFilter(ChannelManagementState))
async def list_channel_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await show_channel_handler(callback, state, i18n)


@router.callback_query(ChannelDetailBack.filter(), StateFilter(ChannelManagementState))
async def detail_channel_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    new_callback = CallbackQuery(
        id=callback.id,
        from_user=callback.from_user,
        message=callback.message,
        chat_instance=callback.chat_instance,
        data=ChannelCalback(id=data['channel_id']).pack(),
        inline_message_id=callback.inline_message_id,
        chat=callback.message.chat,
        json=callback.json
    )
    await show_detail_channel(new_callback, state, i18n)



