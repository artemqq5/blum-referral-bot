from aiogram import Bot
from aiogram_i18n import I18nContext

from data.repository.UserRepository import UserRepository


class NotificationAdmin:
    @staticmethod
    async def user_activate_bot(user_id: int, bot: Bot, i18n: I18nContext, activate=False):
        counter = 0
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)

        with i18n.use_locale(user['lang_code']):
            for admin in admins:
                try:
                    if activate:
                        await bot.send_message(
                            chat_id=admin['userid'],
                            text=i18n.NOTIFICATION.NEW_USER(
                                username=user['username'],
                                user_id=user['userid'],
                                join_at=user['join_at']
                            )
                        )
                    else:
                        await bot.send_message(
                            chat_id=admin['userid'],
                            text=i18n.NOTIFICATION.NEW_USER_BY_LINK(
                                username=user['username'],
                                user_id=user['userid'],
                                join_at=user['join_at']
                            )
                        )
                    counter += 1
                except Exception as e:
                    print(f"user_activate_bot: {e}")

        print(f"messaging user_activate_bot {counter}/{len(admins)}")
