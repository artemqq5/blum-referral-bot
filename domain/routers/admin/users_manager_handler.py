from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.Operation import ALL_USERS, USER_MODEL_INFO
from data.repository.UserRepository import UserRepository
from presentation.keyboard_admin.kb_users_manager import users_pagination_keyboard, UsersCallback, UsersPageCallback, \
    user_detail_back

router = Router()


@router.callback_query(F.data.contains("MENU*USERS*CALLBACK"))
async def users_callbacl_handler(callback: CallbackQuery, state: FSMContext):
    users = [user for user in UserRepository().users() if user['userid'] != callback.from_user.id]

    await callback.message.edit_text(ALL_USERS, reply_markup=users_pagination_keyboard(1, users))


@router.callback_query(UsersCallback.filter())
async def users_callbacl_handler(callback: CallbackQuery, state: FSMContext):
    user = UserRepository().user(callback.data.split(":")[1])

    await callback.message.edit_text(
        USER_MODEL_INFO.format(
            user['username'],
            user['userid'],
            user['referral_url'],
            user['ref_count']
        ),
        reply_markup=user_detail_back
    )


@router.callback_query(UsersPageCallback.filter())
async def page_users_listener(callback: CallbackQuery):
    page = int(callback.data.split(":")[1])
    users = [user for user in UserRepository().users() if user['userid'] != callback.from_user.id]
    await callback.message.edit_reply_markup(reply_markup=users_pagination_keyboard(page, users))


@router.callback_query(F.data.contains("BACKUSERS"))
async def back_from_user_detail(callback: CallbackQuery, state: FSMContext):
    users = [user for user in UserRepository().users() if user['userid'] != callback.from_user.id]

    await callback.message.edit_text(ALL_USERS, reply_markup=users_pagination_keyboard(1, users))
