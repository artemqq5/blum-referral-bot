from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from config import CHANNEL_ID
from data.repository.UserRepository import UserRepository
from domain.notification.BaseNotification import BaseNotification


class RegistrationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user = event.from_user

        if not UserRepository().user(user.id):
            link_name = f"@{user.username} ({user.id})"
            link_generate = await event.bot.create_chat_invite_link(CHANNEL_ID, link_name, creates_join_request=True)
            if not UserRepository().add(user.id, user.username, user.first_name, user.last_name, user.language_code, link_generate.invite_link):
                await event.bot.send_message(chat_id=user.id, text="REGISTER_FAIL")
                return None

            await BaseNotification().new_user(link_name, data['bot'])

            await event.bot.send_message(chat_id=user.id, text="REGISTER_SUCCESS")

        return await handler(event, data)
