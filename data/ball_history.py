import sqlalchemy as sa
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class Ball(SqlAlchemyBase):
    __tablename__ = "ball_history"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    year = sa.Column(sa.Integer)
    ball = sa.Column(sa.Integer)

    cource_id = sa.Column(sa.Integer, sa.ForeignKey("cources.id"))
