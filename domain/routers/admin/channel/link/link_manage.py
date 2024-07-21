from aiogram import Router, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.ChannelRepository import ChannelRepository
from data.repository.LinkRepository import LinkRepository
from domain.states.ChannelManagementState import ChannelManagementState
from presentation.keyboard_admin.kb_channels import ManageLinks, CreateLink
from presentation.keyboard_admin.kb_links import links_pagination_keyboard, kb_create_link, ListLinkBack, \
    LinkPageCallback, LinkCalback, kb_detail_link, DeleteLink

router = Router()


# MANAGE LINKS
@router.callback_query(ManageLinks.filter(), ChannelManagementState.DetailChannel)
async def managelink_handler(callback: types.CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    channel = ChannelRepository().get_channel(data['channel_id'])
    links = LinkRepository().get_all(channel['channel_id'])

    if not links:
        await callback.answer(i18n.ADMIN.LINK.LIST_EMPTY(), show_alert=True)
        return

    await state.update_data(channel_title=channel['title'])
    page = data.get("last_link_page_id", 1) if len(links) > 5 else 1

    await state.set_state(ChannelManagementState.ShowLinks)
    await callback.message.edit_text(i18n.ADMIN.LINK(channel_name=channel['title']),
                                     reply_markup=links_pagination_keyboard(page, links))


@router.callback_query(LinkPageCallback.filter(), ChannelManagementState.ShowLinks)
async def nav_channel(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = callback.data.split(":")[1]
    data = await state.get_data()
    links = LinkRepository().get_all(data['channel_id'])

    await state.update_data(last_link_page_id=int(page))
    await callback.message.edit_text(i18n.ADMIN.LINK(channel_name=data['channel_title']),
                                     reply_markup=links_pagination_keyboard(int(page), links))


@router.callback_query(LinkCalback.filter(), ChannelManagementState.ShowLinks)
async def link_detail(callback: types.CallbackQuery, state: FSMContext, i18n: I18nContext):
    link_url = "https://" + callback.data.split(":")[1]

    link = LinkRepository().get_link(link_url)
    channel = ChannelRepository().get_channel(link['channel_id'])

    await state.set_state(ChannelManagementState.DetailLink)
    await state.update_data(link_url=link_url)

    await callback.message.edit_text(
        i18n.ADMIN.LINK.TEMPLATE(
            title=link['link_title'],
            channel=channel['title'],
            channel_id=channel['channel_id'],
            link=link_url,
            count_user=link['users_join'],
            date=link['_at']
        ),
        reply_markup=kb_detail_link
    )


@router.callback_query(ListLinkBack.filter(), ChannelManagementState.DetailLink)
async def link_list_back(callback: types.CallbackQuery, state: FSMContext, i18n: I18nContext):
    await managelink_handler(callback, state, i18n)


@router.callback_query(DeleteLink.filter(), ChannelManagementState.DetailLink)
async def delete_link(callback: types.CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    if not LinkRepository().delete_link(data['link_url']):
        await callback.message.answer(i18n.ADMIN.LINK.DELETE_FAIL())
        return

    await callback.message.answer(i18n.ADMIN.LINK.DELETE_SUCCESS())
    await managelink_handler(callback, state, i18n)


# CREATE LINK
@router.callback_query(CreateLink.filter(), ChannelManagementState.DetailChannel)
async def createlink_handler(callback: types.CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ChannelManagementState.CreateLink)
    await callback.message.edit_text(i18n.ADMIN.LINK.SET_NAME(), reply_markup=kb_create_link)


@router.message(ChannelManagementState.CreateLink)
async def create_link(message: types.Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    link_generate = await bot.create_chat_invite_link(data['channel_id'], message.text, creates_join_request=True)

    if not LinkRepository().add_link(
            channel_id=data['channel_id'],
            link_title=message.text,
            link=link_generate.invite_link,
            user_id=message.from_user.id
    ):
        await message.answer(i18n.ADMIN.LINK.CREATE_FAIL(), reply_markup=kb_create_link)
        return

    await message.answer(i18n.ADMIN.LINK.CREATE_SUCCESS(), reply_markup=kb_create_link)
