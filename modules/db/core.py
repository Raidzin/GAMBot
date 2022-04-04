from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from modules.settings.default_settings import DB_PATH, DB_PATH_IS_ABSOLUTE

if DB_PATH_IS_ABSOLUTE:
    path = '////'
else:
    path = '///'
engine = create_engine(f'sqlite:{path}{DB_PATH}?check_same_thread=False')
engine.connect()


def get_session():
    return Session(bind=engine)


def get_or_create(model, defaults=None, **kwargs):
    session = get_session()
    session.expire_on_commit = False
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        kwargs |= defaults or {}
        print(kwargs)
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance, True
