from aiogram import Router, types, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import CHANNEL_ID
from data.constants.Basic import OPEN_CHANNEL, HELLO_USER
from data.repository.UserRepository import UserRepository
from domain.notification.BaseNotification import BaseNotification


router = Router()
notification = BaseNotification()


@router.chat_join_request()
async def handle_join_request(chat_join_request: types.ChatJoinRequest, bot: Bot):
    user = chat_join_request.from_user
    link = chat_join_request.invite_link.invite_link

    try:
        try:
            await chat_join_request.approve()

            if not UserRepository().user(user.id):
                link_name = f"{user.username} ({user.id})"
                link_generate = await bot.create_chat_invite_link(CHANNEL_ID, link_name, creates_join_request=True)

                if UserRepository().add(
                        user.id, user.username, user.first_name, user.last_name, user.language_code,
                        link_generate.invite_link
                ):
                    await notification.user_join_by_link(user, link, bot)

        except TelegramBadRequest as e:
            if "USER_ALREADY_PARTICIPANT" not in str(e):
                raise Exception

        kb_join = InlineKeyboardBuilder(markup=[
            [InlineKeyboardButton(text=OPEN_CHANNEL, url=link)]
        ])

        await bot.send_message(chat_id=user.id,
                               text=HELLO_USER,
                               reply_markup=kb_join.as_markup())
    except Exception as e:
        print(f"handle_join_request: {e} | @{chat_join_request.from_user.username}")
