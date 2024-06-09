from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.Basic import NEW_USER_INVITE, NEW_USER_INVITE_ADMIN, NEW_USER_JOIN, USER_HAS_KEY, \
    USER_HAS_KEY_ERROR, USER_HAS_KEY_ADMIN
from data.constants.Operation import NOTIFY_RESULT
from data.repository.UserRepository import UserRepository
from domain.AccessGenerate import AccessGenerate


class BaseNotification:

    @staticmethod
    async def user_join_by_link(user_join, link_join, bot):
        referral_user = UserRepository().user_by_link(link_join)
        UserRepository().update_ref_count(referral_user['userid'], referral_user['ref_count'] + 1)

        to_new_key = 5 - ((referral_user['ref_count'] + 1) % 5)

        admins = UserRepository().admins()

        try:
            await bot.send_message(chat_id=referral_user['userid'], text=NEW_USER_INVITE.format(to_new_key))

            for admin in admins:
                try:
                    if admin['userid'] == referral_user['userid']:
                        continue

                    await bot.send_message(
                        chat_id=admin['userid'],
                        text=NEW_USER_INVITE_ADMIN.format(
                            f"@{referral_user['username']} <b>({referral_user['userid']})</b>",
                            f"{user_join.username} <b>({user_join.id})</b>",
                            to_new_key
                        )
                    )
                except Exception as e:
                    print(f"user({admin}) | {e} ")

            if to_new_key == 5:
                await BaseNotification.__send_user_key(referral_user, bot)
                await BaseNotification.__user_get_access_for_2_week(referral_user, bot)

        except Exception as e:
            print(f"user({referral_user}) | {e} ")

    @staticmethod
    async def new_user(username, bot):
        admins = UserRepository().admins()

        for admin in admins:
            try:
                await bot.send_message(
                    chat_id=admin['userid'],
                    text=NEW_USER_JOIN.format(username)
                )
            except Exception as e:
                print(f"user({admin}) | {e} ")

    @staticmethod
    async def __user_get_access_for_2_week(user, bot):
        admins = UserRepository().admins()

        for admin in admins:
            try:
                await bot.send_message(
                    chat_id=admin['userid'],
                    text=USER_HAS_KEY_ADMIN.format(f"@{user['username']} <b>({user['userid']})</b>")
                )
            except Exception as e:
                print(f"user({admin}) | {e} ")

    @staticmethod
    async def __send_user_key(user, bot):
        try:
            access = AccessGenerate.generate_access(user)
            if access:
                await bot.send_message(chat_id=user['userid'], text=USER_HAS_KEY.format(access))
            else:
                await bot.send_message(chat_id=user['userid'], text=USER_HAS_KEY_ERROR.format(user['userid']))
        except Exception as e:
            print(f"user({user}) | {e} ")

    @staticmethod
    async def notify_all(bot, data):
        users = UserRepository().users()

        counter = 0
        block = 0
        other = 0

        for user in users:
            try:
                await BaseNotification.generate_message_users(data, bot, user['userid'])
                counter += 1
            except TelegramForbiddenError as e:
                block += 1
                print(f"user({user}) | {e} ")
                continue
            except Exception as e:
                other += 1
                print(f"user({user}) | {e} ")
                continue

        return NOTIFY_RESULT.format(str(counter), str(len(users)), str(block), str(other))

    @staticmethod
    async def generate_message_users(data, bot: Bot, user_id):
        keyboard = ReplyKeyboardRemove()
        if data.get('button_url', None):
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=data['button_text'], url=data['button_url'])]
            ])

        if data.get('photo', None):
            await bot.send_photo(chat_id=user_id, photo=data['photo'], caption=data['message'], reply_markup=keyboard)
        elif data.get('video', None):
            await bot.send_video(chat_id=user_id, video=data['video'], caption=data['message'], reply_markup=keyboard)
        elif data.get('animation', None):
            await bot.send_animation(chat_id=user_id, animation=data['animation'], caption=data['message'],
                                     reply_markup=keyboard)
        else:
            await bot.send_message(chat_id=user_id, text=data['message'], reply_markup=keyboard)

