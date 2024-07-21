import math

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repository.UserRepository import UserRepository
from presentation.keyboard_admin.kb_admin import GetAllUsers
from presentation.keyboard_admin.kb_users_manager import users_pagination_keyboard, UsersCallback, UsersPageCallback, \
    user_detail_back

router = Router()


@router.callback_query(GetAllUsers.filter())
async def users_callbacl_handler(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    users = [user for user in UserRepository().users() if user['userid'] != callback.from_user.id]

    if not users:
        await callback.answer(i18n.ADMIN.USER_LIST_EMPTY(), show_alert=True)
        return

    await callback.message.edit_text(i18n.ADMIN.ALL_USERS(), reply_markup=users_pagination_keyboard(1, users))


@router.callback_query(UsersCallback.filter())
async def users_callbacl_handler(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    user = UserRepository().user(callback.data.split(":")[1])
    page_back = callback.data.split(":")[2]

    username = f"@{user['username']}" if user['username'] else ""
    firstname = user['firstname'] if user['firstname'] else ""
    lastname = user['lastname'] if user['lastname'] else ""

    await callback.message.edit_text(
        i18n.ADMIN.USER_TEMPLATE(
            username=username,
            userid=user['userid'],
            name=firstname,
            lastname=lastname,
            lang=user['lang_code'],
            date=user['join_at']
        ),
        reply_markup=user_detail_back(page_back)
    )


@router.callback_query(UsersPageCallback.filter())
async def page_users_listener(callback: CallbackQuery, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    users = [user for user in UserRepository().users() if user['userid'] != callback.from_user.id]
    await callback.message.edit_text(i18n.ADMIN.ALL_USERS(),
                                     reply_markup=users_pagination_keyboard(page, users))


@router.callback_query(F.data.contains("BACKUSERS"))
async def back_from_user_detail(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page_back = callback.data.split("_")[1]
    users = [user for user in UserRepository().users() if user['userid'] != callback.from_user.id]

    await callback.message.edit_text(i18n.ADMIN.ALL_USERS(),
                                     reply_markup=users_pagination_keyboard(int(page_back), users))
