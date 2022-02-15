from requests import get

from bot_modules.os_function import Tokens

URL = 'http://192.168.77.60/image.jpg'
HEADERS = {
    'Authorization': f'Basic {Tokens.get_token(Tokens.CAMERA_TOKEN_NAME)}'
}
CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'


def get_photo():
    try:
        return get(URL, headers=HEADERS).content
    except Exception as error:
        raise ConnectionError(CAMERA_ERROR.format(error))
