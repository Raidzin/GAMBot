import logging
from logging.handlers import RotatingFileHandler

import datetime as dt

from modules.settings.default_settings import Config

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
logger.setLevel(logging.DEBUG)
logger.addHandler(
    handler,
)


class Log:
    def __init__(self, level, time, function, message):
        self.level = level
        self.time = dt.datetime.strptime(time + '000', DT_FORMAT)
        self.function = function
        self.message = message[:len(message) - 1]

    def to_telegram(self):
        return f'{self.time}\n{self.message}\n'

    def __str__(self):
        return (f'LOG: {self.level=},{self.time=}, '
                f'{self.function=}, {self.message=}')


def get_logs():
    with open(
            Config.get_path(Config.LOG_PATH),
            mode='r',
            encoding='utf-8'
    ) as file:
        text = file.readlines()
        file.close()
    return [parse_log(log) for log in text]


def parse_log(log: str):
    log = log.split(' - ')
    return Log(*log)


def get_info_logs_tail(n):
    logs = get_logs()[::-1]
    logs_tail = []
    for log in logs:
        if len(logs_tail) == n:
            break
        if log.level == 'INFO':
            logs_tail.append(log)
    return logs_tail[::-1]


def to_telegram_logs(logs):
    logs = [log.to_telegram() for log in logs]
    return ''.join(logs)


if __name__ == '__main__':
    get_logs()
