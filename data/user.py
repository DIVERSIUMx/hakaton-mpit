import sqlalchemy as sa
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    tg_id = sa.Column(sa.Integer)

    mes_count = sa.Column(sa.Integer)
