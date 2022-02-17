import logging
from logging.handlers import RotatingFileHandler

import datetime as dt

from bot_modules.os_function import Config

LOG_FILE = Config.get_path(Config.LOG_PATH)
FILE_SIZE = 10 * 1024 ** 3
ENCODING = 'utf-8'
FORMAT = '%(levelname)s - %(asctime)s - %(funcName)s - %(message)s'
DT_FORMAT = '%Y-%m-%d %H:%M:%S,%f'

handler = RotatingFileHandler(
    filename=LOG_FILE,
    maxBytes=FILE_SIZE,
    encoding=ENCODING,
)

handler.formatter = logging.Formatter(
    fmt=FORMAT
)

logger = logging.getLogger('GAM_logger')
logger.setLevel(logging.INFO)
logger.addHandler(
    handler,
)


class Log:
    def __init__(self, level, time, function, message):
        self.level = level
        self.time = dt.datetime.strptime(time + '000', DT_FORMAT)
        self.function = function
        self.message = message

    def __str__(self):
        return (f'LOG: {self.level=},{self.time=}, '
                f'{self.function=}, {self.message=}')


def parse_log(log: str):
    log = log.split(' - ')
    return Log(*log)
