import asyncio

import aiogram
from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart, Filter
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from data import db_session
from data.user import User

router = Router(name="test")


@router.message(Command("start"))
async def start_r(message: Message, bot: Bot, db: AsyncSession):
    user_id = message.from_user.id

    async with ChatActionSender(bot=bot, chat_id=message.chat.id, action="typing"):
        q = await db.execute(select(User).filter(User.tg_id == user_id))
        user = q.scalar_one_or_none()

        if not user:
            user = User()
            user.tg_id = user_id
            user.mes_count = 100
            db.add(user)
            await db.commit()
            await db.refresh(user)

        await message.answer(f"id: {user.id}, cnt: {user.mes_count}")
        user.mes_count += 1

        await db.merge(user)
        await db.commit()

        await db.close()
