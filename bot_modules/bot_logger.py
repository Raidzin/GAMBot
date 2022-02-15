import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE_NAME = f'{str(Path.home())}/.GAM.log'
FILE_SIZE = 10 * 1024 ** 3
ENCODING = 'utf-8'
FORMAT = '%(levelname)s - %(asctime)s - %(funcName)s - %(message)s'

handler = RotatingFileHandler(
    filename=LOG_FILE_NAME,
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
