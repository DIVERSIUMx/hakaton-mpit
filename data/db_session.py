import sqlalchemy as sa
import sqlalchemy.orm as orm
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()


async def global_init(db_file):

    if not db_file or not db_file.strip():
        raise Exception("Укажи файл базы, дурень")

    conn_str = f'sqlite+aiosqlite:///{db_file.strip()}'
    print(f"Подключаемся к базе ({conn_str})")

    engine = create_async_engine(
        conn_str, echo=False)

    from . import __all_models

    async with engine.begin() as conn:
        await conn.run_sync(SqlAlchemyBase.metadata.create_all)

    __factory = async_sessionmaker(
        bind=engine, expire_on_commit=False)
    return __factory


class DbMiddleware(BaseMiddleware):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    async def __call__(self, handler, event, data):
        async with self.engine() as session:
            data["db"] = session
            return await handler(event, data)
