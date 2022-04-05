from modules.base_bot import Message
from modules.db.core import session
from modules.db.models import Log


class Logger:

    @classmethod
    def info(cls, log_message, message: Message = None, command=None):
        cls.log(
            log_message=log_message,
            message=message,
            command=command,
            level='info'
        )

    @classmethod
    def debug(cls, log_message, message: Message = None, command=None):
        cls.log(
            log_message=log_message,
            message=message,
            command=command,
            level='debug'
        )

    @classmethod
    def error(cls, log_message, message: Message = None, command=None):
        cls.log(
            log_message=log_message,
            message=message,
            command=command,
            level='error'
        )

    @classmethod
    def log(cls, log_message, level='log',
            message: Message = None, command=None):
        user_id = message.from_user.id if message else None
        log = {
            'type': level,
            'user': user_id,
            'command': command,
            'message': log_message,
        }
        rec = Log(**log)
        session.add(rec)
        session.commit()
