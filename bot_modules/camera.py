from requests import get

from bot_modules.os_function import Config

URL = 'http://192.168.77.60/image.jpg'
HEADERS = {
    'Authorization': f'Basic {Config.get_token(Config.CAMERA_TOKEN_NAME)}'
}
CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'


def get_photo():
    try:
        return get(URL, headers=HEADERS).content
    except Exception as error:
        raise ConnectionError(CAMERA_ERROR.format(error))
