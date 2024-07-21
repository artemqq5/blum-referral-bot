import asyncio
import logging

from aiogram import Dispatcher, Bot, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

import config
from domain.middlewares.LocaleManager import LocaleManager
from domain.middlewares.RegistrationMiddleware import RegistrationMiddleware
from domain.routers import join_handler
from domain.routers.admin import main_admin_handler
from domain.routers.user import main_user_handler

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(
    join_handler.router,
    main_user_handler.router,
    main_admin_handler.router
)


async def main():
    logging.basicConfig(level=logging.INFO)
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.BOT_TOKEN, default=default_properties)

    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path='presentation/localization'),
        default_locale='en',
        manager=LocaleManager()
    )

    i18n_middleware.setup(dp)

    dp.message.outer_middleware(RegistrationMiddleware())  # register if user not registered
    dp.callback_query.outer_middleware(RegistrationMiddleware())  # register if user not registered

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())

