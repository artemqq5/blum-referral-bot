from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject
from aiogram_i18n import L

from config import CHANNEL_ID
from data.repository.UserRepository import UserRepository
from domain.notification.NotificationAdmin import NotificationAdmin


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
            if not UserRepository().add(user.id, user.username, user.first_name, user.last_name, user.language_code):
                return None

            await NotificationAdmin().user_activate_bot(user.id, event.bot, data['i18n'], activate=True)

            await event.bot.send_message(
                chat_id=user.id,
                text=L.USER.HELLO()
            )

        return await handler(event, data)
