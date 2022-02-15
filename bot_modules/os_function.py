from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Tokens:
    TELEGRAM_TOKEN_NAME = 'TELEGRAM_TOKEN'
    CAMERA_TOKEN_NAME = 'CAMERA_TOKEN'
    ADMIN_ID_NAME = 'ADMIN_ID'
    LOG_PATH_NAME = 'LOG_PATH'

    TOKEN_ERROR = 'Отсутствует необходимый токен {}'

    @classmethod
    def get_token(cls, token_name):
        token = getenv(token_name)
        if token is None:
            raise EnvironmentError(cls.TOKEN_ERROR.format(token_name))
        return token
