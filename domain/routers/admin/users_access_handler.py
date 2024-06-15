import math

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.Operation import ALL_ACCESS, ACCESS_MODEL_INFO, ALL_ACCESS_KEY
from data.repository.AccessRepository import AccessRepository
from data.repository.UserRepository import UserRepository
from presentation.keyboard_admin.kb_users_access import accesses_pagination_keyboard, AccessesCallback, \
    access_detail_back, AccessesPageCallback

router = Router()


@router.callback_query(F.data.contains("MENU*ACCESS*CALLBACK"))
async def access_callbacl_handler(callback: CallbackQuery):
    accesses = AccessRepository().accesses()

    await callback.message.edit_text(ALL_ACCESS_KEY.format(len(accesses), 1, math.ceil(len(accesses)/1)), reply_markup=accesses_pagination_keyboard(1, accesses))


@router.callback_query(AccessesCallback.filter())
async def users_callbacl_handler(callback: CallbackQuery):
    access = AccessRepository().access(callback.data.split(":")[1])
    page_back = callback.data.split(":")[2]
    user = UserRepository().user(access['userid'])

    await callback.message.edit_text(
        ACCESS_MODEL_INFO.format(
            user['username'],
            user['userid'],
            access['days'],
            access['uuid_key'],
            access['harddrive_id'],
            access['created_at'],
            access['start_time'],
            access['end_time']
        ),
        reply_markup=access_detail_back(page_back)
    )


@router.callback_query(AccessesPageCallback.filter())
async def page_users_listener(callback: CallbackQuery):
    page = int(callback.data.split(":")[1])
    accesses = AccessRepository().accesses()
    await callback.message.edit_text(ALL_ACCESS_KEY.format(len(accesses), page, math.ceil(len(accesses)/1)), reply_markup=accesses_pagination_keyboard(1, accesses))


@router.callback_query(F.data.contains("BACKACCESSES"))
async def back_from_user_detail(callback: CallbackQuery, state: FSMContext):
    accesses = AccessRepository().accesses()
    page_back = callback.data.split("_")[1]
    await callback.message.edit_text(ALL_ACCESS_KEY.format(len(accesses), page_back, math.ceil(len(accesses)/1)), reply_markup=accesses_pagination_keyboard(int(page_back), accesses))
