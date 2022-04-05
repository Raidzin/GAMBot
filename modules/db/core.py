from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import NullPool

from modules.settings.default_settings import DB_PATH, DB_PATH_IS_ABSOLUTE

path = '////' if DB_PATH_IS_ABSOLUTE else '///'


def get_engine():
    engine = create_engine(f'sqlite:{path}{DB_PATH}?check_same_thread=False',
                           poolclass=NullPool)
    engine.connect()
    return engine


def get_session():
    return Session(bind=get_engine())


def get_or_create(model, defaults=None, **kwargs):
    session = get_session()
    session.expire_on_commit = False
    record = session.query(model).filter_by(**kwargs).one_or_none()
    if record:
        return record, False
    kwargs |= defaults or {}
    record = model(**kwargs)
    session.add(record)
    session.commit()
    session.close()
    return record, True
