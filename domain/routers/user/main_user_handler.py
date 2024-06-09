from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data.constants.Basic import MENU_USER
from data.constants.Operation import *
from data.repository.UserRepository import UserRepository
from domain.filters.IsAdmin import IsAdminFilter
from domain.middlewares.IsAdminMiddleware import IsAdminMiddleware

router = Router()


router.message.middleware(IsAdminMiddleware(False))
router.callback_query.middleware(IsAdminMiddleware(False))


@router.message(Command("start"), IsAdminFilter(False))
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    user = UserRepository().user(message.from_user.id)
    ref_to_key = 5 - (user['ref_count'] % 5)
    await message.answer(MENU_USER.format(user['referral_url'], user['ref_count'], ref_to_key))

# @router.message(F.text == CANCEL, IsAdminFilter(False))
# async def cancel(message: types.Message, state: FSMContext):
#     await state.clear()
#     await message.answer(text=CANCEL_SUCCESS)
