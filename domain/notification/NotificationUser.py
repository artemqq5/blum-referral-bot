from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError

from data.repository.UserRepository import UserRepository
from domain.routers.admin.messaging.MessagingTools import MessagingTools


class NotificationUser:

    @staticmethod
    async def push_all_users(data: dict[str], bot: Bot, i18n):
        counter = 0
        block = 0
        other = 0

        users = UserRepository().users()

        for user in users:
            try:
                await MessagingTools.preview_message_send(data, bot, user['userid'])
                counter += 1
            except TelegramForbiddenError as e:
                block += 1
                print(f"user({user}) | push_all_users: {e} ")
            except Exception as e:
                other += 1
                print(f"user({user}) | push_all_users: {e} ")

        print(f"messaging: {counter}/{len(users)}\nblock:{block}\nother:{other}")
        return i18n.ADMIN.RESULT_NOTIFICATION(send=counter, users=len(users), block=block, other=other)

    @staticmethod
    async def push_individual_user(data: dict[str], bot: Bot, user_id, i18n):
        counter = 0
        block = 0
        other = 0

        user = UserRepository().user(user_id)

        try:
            await MessagingTools.preview_message_send(data, bot, user['userid'])
            counter += 1
        except TelegramForbiddenError as e:
            block += 1
            print(f"user({user}) | push_all_users: {e} ")
        except Exception as e:
            other += 1
            print(f"user({user}) | push_all_users: {e} ")

        print(f"messaging: {counter}/{1}\nblock:{block}\nother:{other}")
        return i18n.ADMIN.RESULT_NOTIFICATION(send=counter, users=1, block=block, other=other)
