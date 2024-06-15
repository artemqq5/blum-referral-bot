from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data.constants.Basic import USER_HAS_KEY_ERROR, ADMIN_GENRETED_KEY
from data.constants.Operation import COMMENT_ACCESS, USER_ID_ACCESS, \
    DAYS_ACCESS
from data.repository.AccessRepository import AccessRepository
from domain.AccessGenerate import AccessGenerate
from domain.states.GenerateAccessState import GenerateAccessState
from presentation.keyboard_admin.kb_admin import kb_menu_admin
from presentation.keyboard_admin.kb_generate_access import *

router = Router()


@router.callback_query(F.data.contains("MENU*GENERATEACCESS*CALLBACK"))
async def geneerate_access_callbacl_handler(callback: CallbackQuery, state: FSMContext):
    print(callback.from_user.id)
    if callback.from_user.id == 886327182:
        await state.set_state(GenerateAccessState.comment)
        await callback.message.edit_text(COMMENT_ACCESS, reply_markup=generate_access_back)
    else:
        await callback.message.edit_text("У вас немає доступа на це", reply_markup=generate_access_back)


@router.message(GenerateAccessState.comment)
async def set_comment_access(message: Message, state: FSMContext):
    if len(message.text) < 50:
        await state.update_data(comment=message.text)
    else:
        await message.answer(f"Забагато тексту, зменш до 50 символів, зараз {len(message.text)}")
        return

    await state.set_state(GenerateAccessState.userid)
    await message.answer(USER_ID_ACCESS, reply_markup=kb_skip_generate)


@router.callback_query(GenerateAccessState.userid, F.data.contains("SKIPUSERID"))
async def skip_step_userid(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(GenerateAccessState.days)
    await callback.message.edit_text(DAYS_ACCESS, reply_markup=generate_access_back)


@router.message(GenerateAccessState.userid)
async def set_userid_access(message: Message, state: FSMContext):
    await state.update_data(userid=message.text)
    await state.set_state(GenerateAccessState.days)
    await message.answer(DAYS_ACCESS, reply_markup=generate_access_back)


@router.message(GenerateAccessState.days)
async def set_days_access(message: Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Це не число, введіть число:")
        return
    await state.update_data(days=message.text)
    data = await state.get_data()

    try:
        access = AccessGenerate.generate_custom_access(data.get('userid', None), data['comment'], data['days'])
        if access:
            await message.answer(text=ADMIN_GENRETED_KEY.format(AccessRepository().access(access)['days'], access), reply_markup=kb_menu_admin)
        else:
            await message.answer(text=USER_HAS_KEY_ERROR.format(data.get('userid', None)), reply_markup=kb_menu_admin)

        await state.clear()
    except Exception as e:
        print(f"data generate ({data}) | {e} ")

