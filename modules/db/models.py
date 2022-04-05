from datetime import datetime

import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

from modules.db.core import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    pk = sql.Column(sql.Integer, primary_key=True)
    username = sql.Column(sql.String(100), nullable=True)
    first_name = sql.Column(sql.String(100), nullable=True)
    last_name = sql.Column(sql.String(100), nullable=True)
    role = sql.Column(sql.Integer, default=3)


class Log(Base):
    __tablename__ = 'logs'
    pk = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    user = sql.Column(sql.Integer, sql.ForeignKey('users.pk'), nullable=True)
    type = sql.Column(sql.String(50))
    command = sql.Column(sql.String(50), nullable=True)
    message = sql.Column(sql.String(256), nullable=True)
    datetime = sql.Column(sql.DateTime, default=datetime.now)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
