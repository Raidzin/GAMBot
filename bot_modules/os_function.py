from os import getenv

from dotenv import load_dotenv

TELEGRAM_TOKEN_NAME = 'TELEGRAM_TOKEN'
CAMERA_TOKEN_NAME = 'CAMERA_TOKEN'

TOKEN_ERROR = 'Отсутствует необходимый токен {}'

load_dotenv()


def get_telegram_token():
    token = getenv(TELEGRAM_TOKEN_NAME)
    if token is None:
        raise EnvironmentError(TOKEN_ERROR.format(TELEGRAM_TOKEN_NAME))
    return token


def get_camera_token():
    token = getenv(CAMERA_TOKEN_NAME)
    if token is None:
        raise EnvironmentError(TOKEN_ERROR.format(CAMERA_TOKEN_NAME))
    return token
