from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from modules.settings.default_settings import DB_FILE_ABSOLUTE_PATH

engine = create_engine(f'sqlite:////{DB_FILE_ABSOLUTE_PATH}')
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
        instance = model(**kwargs)
        try:
            session.add(instance)
            session.commit()
        except Exception:
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, True
        else:
            return instance, True
