from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from data.repository.ChannelRepository import ChannelRepository
from domain.states.ChannelManagementState import ChannelManagementState
from presentation.keyboard_admin.kb_channels import DeleteChannel

router = Router()


# DELETE CHANNEL
@router.callback_query(DeleteChannel.filter(), ChannelManagementState.DetailChannel)
async def delete_cannel_handler(callback: types.CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    if not ChannelRepository().delete_channel(data['channel_id']):
        await callback.message.answer(i18n.ADMIN.CHANNEL.DELETE_FAIL())
        return

    await callback.message.answer(i18n.ADMIN.CHANNEL.DELETE_SUCCESS())
    from domain.routers.admin.channel.channel_manage import show_channel_handler
    await show_channel_handler(callback, state, i18n)
