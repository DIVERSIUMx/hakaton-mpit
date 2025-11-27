import sqlalchemy as sa
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class Cource(SqlAlchemyBase):
    __tablename__ = "cources"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    desc = sa.Column(sa.String)
    c_ball = sa.Column(sa.Integer)

    math = sa.Column(sa.Boolean, default=True)
    russian_lang = sa.Column(sa.Boolean, default=True)
    physics = sa.Column(sa.Boolean, default=True)
    it = sa.Column(sa.Boolean, default=True)
    sosial = sa.Column(sa.Boolean, default=True)
    chemystry = sa.Column(sa.Boolean, default=True)
    liter = sa.Column(sa.Boolean, default=True)
    geography = sa.Column(sa.Boolean, default=True)
    forein_lang = sa.Column(sa.Boolean, default=True)

    # challenges = orm.relationship("Chalange", back_populates="cources")
    ball = orm.relationship("Ball", back_populates="cource")
