from os import getenv

from dotenv import load_dotenv

load_dotenv()

TOKEN_ERROR = 'Отсутствует необходимый токен {}'


class Config:
    TELEGRAM_TOKEN_NAME = 'TELEGRAM_TOKEN'
    CAMERA_TOKEN_NAME = 'CAMERA_TOKEN'
    ADMIN_ID_NAME = 'ADMIN_ID'

    _BASE_PATH = 'BASE_PATH'

    LOG_PATH = 'LOG_PATH'
    _LOG_NAME = 'LOG_NAME'
    DB_PATH = 'DB_PATH'
    _DM_NAME = 'DM_NAME'

    _PATHS = {
        LOG_PATH: (_BASE_PATH, LOG_PATH, _LOG_NAME),
        DB_PATH: (_BASE_PATH, DB_PATH, _DM_NAME),
    }

    @classmethod
    def get_token(cls, token_name):
        token = getenv(token_name)
        if token is None:
            raise EnvironmentError(TOKEN_ERROR.format(token_name))
        return token

    @classmethod
    def get_path(cls, filename):
        full_path = cls._PATHS[filename]
        return (
                cls.get_token(full_path[0]) +
                cls.get_token(full_path[1]) +
                cls.get_token(full_path[2])
        )


if __name__ == '__main__':
    print(Config.get_path(Config.LOG_PATH))
