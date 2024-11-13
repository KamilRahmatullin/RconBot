from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from rconJasCube import config
from bot.handlers import router


async def rcon_bot():
    bot = Bot(config.TOKEN_API)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.message.middleware(ChatActionMiddleware())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
