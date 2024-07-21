from aiogram import Router, types, F, Bot
from aiogram.enums import ChatMemberStatus
from aiogram.exceptions import TelegramForbiddenError
from aiogram_i18n import I18nContext

from data.repository.ChannelRepository import ChannelRepository

router = Router()


@router.message(F.forward_from_chat.type == 'channel')
async def forward_message_handler(message: types.Message, bot: Bot, i18n: I18nContext):
    id_channel = message.forward_from_chat.id
    title_channel = message.forward_from_chat.title

    try:
        status_bot = await bot.get_chat_member(chat_id=id_channel, user_id=bot.id)
        if status_bot.status != ChatMemberStatus.ADMINISTRATOR:
            raise TelegramForbiddenError
    except TelegramForbiddenError as _:
        await message.answer(i18n.BOT_IS_NO_ADMIN_THAT_CHANNEL())
        return

    if ChannelRepository().get_channel(id_channel):
        await message.answer(i18n.CHANNEL_ALREADY_ADDED_TO_YOU())
        return

    if not ChannelRepository().add_channel(id_channel, title_channel, message.from_user.id):
        await message.answer(i18n.CHANNEL_ERROR_ADD())
        return

    await message.answer(i18n.CHANNEL_JUST_ADDED())
