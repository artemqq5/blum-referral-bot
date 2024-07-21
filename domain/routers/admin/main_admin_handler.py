from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.default_constants import ADMIN
from domain.filters.IsAdminFilter import IsAdminFilter
from domain.middlewares.IsRoleMiddleware import IsRoleMiddleware
from domain.routers.admin import users_manager_handler
from domain.routers.admin.channel import add_channel_, channel_manage, delete_channel
from domain.routers.admin.channel.link import link_manage
from domain.routers.admin.messaging import messaging_main
from domain.routers.admin.post import post_generate
from presentation.keyboard_admin.kb_admin import kb_menu_admin, BackMainMenu

router = Router()
router.include_routers(
    users_manager_handler.router,
    messaging_main.router,
    add_channel_.router,
    delete_channel.router,
    channel_manage.router,
    link_manage.router,
    post_generate.router
)

router.message.middleware(IsRoleMiddleware(ADMIN))
router.callback_query.middleware(IsRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.MAIN_MENU(), reply_markup=kb_menu_admin)


@router.callback_query(BackMainMenu.filter())
async def back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await callback.message.edit_text(i18n.MAIN_MENU(), reply_markup=kb_menu_admin)
