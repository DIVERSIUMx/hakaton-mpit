import sqlalchemy as sa
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class Chalange(SqlAlchemyBase):
    __tablename__ = "challenges"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    desc = sa.Column(sa.String)

    course_id = sa.Column(sa.Integer, sa.ForeignKey("cources.id"))

    # cources = orm.relationship("Cource",
    #                            back_populates="challenges")
