from os import getenv

from dotenv import load_dotenv

load_dotenv()

TOKEN_ERROR = 'Отсутствует необходимый токен {}'


def get_token(token_name):
    token = getenv(token_name)
    if token is None:
        raise EnvironmentError(TOKEN_ERROR.format(token_name))
    return token
