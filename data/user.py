import sqlalchemy as sa
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    name = sa.Column(sa.Integer)
    second_name = sa.Column(sa.Integer)

    hashed_passowd = sa.Column(sa.String)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
