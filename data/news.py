from datetime import datetime

import sqlalchemy as sa
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = "news"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    img = sa.Column(sa.String)
    name = sa.Column(sa.String)
    body = sa.Column(sa.String)
