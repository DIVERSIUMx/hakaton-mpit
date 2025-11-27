import asyncio
import os

import aiogram
import dotenv
from aiogram import Bot, Dispatcher

from data.db_session import DbMiddleware, global_init
from handlers import router


async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        print("ТОКЕНА НЕТ")
        return
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.update.middleware.register(DbMiddleware(await global_init("./db/blob.db")))
    dp.include_router(router)
    print("Бот открывается!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    dotenv.load_dotenv()
    asyncio.run(main())
