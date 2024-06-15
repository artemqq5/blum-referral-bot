import math

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.Operation import ALL_ACCESS, ACCESS_MODEL_INFO, ALL_ACCESS_KEY
from data.repository.AccessRepository import AccessRepository
from data.repository.UserRepository import UserRepository
from presentation.keyboard_admin.kb_generate_access import generate_access_back
from presentation.keyboard_admin.kb_users_access import accesses_pagination_keyboard, AccessesCallback, \
    access_detail_back, AccessesPageCallback, access_back

router = Router()


@router.callback_query(F.data.contains("MENU*ACCESS*CALLBACK"))
async def access_callbacl_handler(callback: CallbackQuery):
    accesses = AccessRepository().accesses()

    await callback.message.edit_text(ALL_ACCESS_KEY.format(len(accesses), 1, math.ceil(len(accesses) / 10)),
                                     reply_markup=accesses_pagination_keyboard(1, accesses))


@router.callback_query(AccessesCallback.filter())
async def access_callbacl_handler(callback: CallbackQuery):
    access = AccessRepository().access(callback.data.split(":")[1])
    page_back = callback.data.split(":")[2]

    user = UserRepository().user(access['userid'])
    if not user:
        user = {'username': 'Невизначено', 'userid': 'Невизначено'}

    await callback.message.edit_text(
        ACCESS_MODEL_INFO.format(
            user['username'],
            user['userid'],
            access['comment'],
            access['days'],
            access['uuid_key'],
            access['harddrive_id'],
            access['created_at'],
            access['start_time'],
            access['end_time']
        ),
        reply_markup=access_detail_back(page_back, access['uuid_key'])
    )


@router.callback_query(F.data.contains("DELETEACCESSCALLBACK"))
async def delete_access_callbacl_handler(callback: CallbackQuery):
    if callback.from_user.id == 886327182:
        access = AccessRepository().access(callback.data.split("_")[1])
        if not AccessRepository().delete(access['uuid_key']):
            await callback.message.edit_text(f"Не вийшло видалити доступ: {access}", reply_markup=access_back())
            return

        await callback.message.edit_text(f"Доступ успішно видалено", reply_markup=access_back())
    else:
        await callback.message.edit_text("У вас немає доступа на це", reply_markup=access_back())


@router.callback_query(AccessesPageCallback.filter())
async def page_users_listener(callback: CallbackQuery):
    page = int(callback.data.split(":")[1])
    accesses = AccessRepository().accesses()
    await callback.message.edit_text(ALL_ACCESS_KEY.format(len(accesses), page, math.ceil(len(accesses) / 10)),
                                     reply_markup=accesses_pagination_keyboard(1, accesses))


@router.callback_query(F.data.contains("BACKACCESSES"))
async def back_from_user_detail(callback: CallbackQuery, state: FSMContext):
    accesses = AccessRepository().accesses()
    page_back = callback.data.split("_")[1]
    await callback.message.edit_text(ALL_ACCESS_KEY.format(len(accesses), page_back, math.ceil(len(accesses) / 10)),
                                     reply_markup=accesses_pagination_keyboard(int(page_back), accesses))
