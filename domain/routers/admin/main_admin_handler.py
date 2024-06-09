from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.constants.Basic import MENU_ADMIN
from data.constants.Operation import CANCEL, CANCEL_SUCCESS
from domain.filters.IsAdmin import IsAdminFilter
from domain.middlewares.IsAdminMiddleware import IsAdminMiddleware
from domain.routers.admin import users_notify_handler, users_manager_handler, users_access_handler
from presentation.keyboard_admin.kb_admin import kb_menu_admin

router = Router()
router.include_routers(
    users_notify_handler.router,
    users_manager_handler.router,
    users_access_handler.router
)

router.message.middleware(IsAdminMiddleware(True))
router.callback_query.middleware(IsAdminMiddleware(True))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(MENU_ADMIN, reply_markup=kb_menu_admin)


@router.message(F.text == CANCEL, IsAdminFilter(True))
async def cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(CANCEL_SUCCESS)


@router.callback_query(F.data.contains("BACKCATEGORY"))
async def back_from_users(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(MENU_ADMIN, reply_markup=kb_menu_admin)

