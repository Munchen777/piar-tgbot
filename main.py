import asyncio


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from config.config import config, async_engine
from config.orm import Base
from handlers.default_handlers.check_subscribe import task_router
from my_logger import my_logger
from utils.set_bot_commands import set_commands

# from handlers.default_handlers.menu import menu_router
# from handlers.default_handlers.start import start_router
# from handlers.admin_handlers.read_only_cmd import admin_router
# from log import my_logger
# from src.config import config, async_engine
# from src.orm import Base
# from utils.set_bot_commands import set_commands

bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def create_tables():
    my_logger.info('Tables have been created.')
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        # print(Base.metadata.tables)
        await conn.run_sync(Base.metadata.create_all)


async def main():
    my_logger.info('Starting bot')

    await create_tables()

    await set_commands(bot)
    
    dp.include_routers(
        task_router,
    )
    # dp.include_routers(admin_router,
    #                    start_router,
    #                    menu_router
    #                    )

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot, close_bot_session=True)
    finally:
        my_logger.info('Stop bot. The session is closing.')
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())

