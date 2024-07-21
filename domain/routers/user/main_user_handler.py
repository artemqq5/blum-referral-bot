from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from data.default_constants import USER
from data.repository.UserRepository import UserRepository
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware

router = Router()


router.message.middleware(IsRoleMiddleware(USER))
router.callback_query.middleware(IsRoleMiddleware(USER))


@router.message(Command("start"), IsAdminFilter(False))
async def start(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.MAIN_MENU())

# @router.message(F.text == CANCEL, IsAdminFilter(False))
# async def cancel(message: types.Message, state: FSMContext):
#     await state.clear()
#     await message.answer(text=CANCEL_SUCCESS)
