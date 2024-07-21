from aiogram import Router, types, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from data.repository.LinkRepository import LinkRepository
from data.repository.UserRepository import UserRepository
from domain.notification.NotificationAdmin import NotificationAdmin
from presentation.keyboard_user.kb_user import kb_menu_user

router = Router()


@router.chat_join_request()
async def handle_join_request(chat_join_request: types.ChatJoinRequest, bot: Bot, i18n: I18nContext):
    user = chat_join_request.from_user
    link = chat_join_request.invite_link.invite_link
    link_from_db = LinkRepository().get_link(link)

    if UserRepository().add(user.id, user.username, user.first_name, user.last_name, user.language_code):
        await NotificationAdmin().user_activate_bot(user.id, bot, i18n)

    try:
        try:
            await chat_join_request.approve()
        except TelegramBadRequest as e:
            if "USER_ALREADY_PARTICIPANT" not in str(e):
                raise Exception

        if not link_from_db:
            raise Exception

        LinkRepository().update_link(user_join=link_from_db['users_join'] + 1, link=link)
        await bot.send_message(chat_id=user.id, text=i18n.USER.HELLO(), reply_markup=kb_menu_user(link))
    except Exception as e:
        print(f"handle_join_request: {e} | @{chat_join_request.from_user.username}")
