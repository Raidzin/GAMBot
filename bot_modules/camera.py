from requests import get

from bot_modules.configurator import Config


class SkipCommand(Exception):
    pass


class Camera:
    enabled = True
    URL = 'http://192.168.77.60/image.jpg'
    HEADERS = {
        'Authorization': f'Basic {Config.get_token(Config.CAMERA_TOKEN_NAME)}'
    }
    CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'

    @classmethod
    def get_photo(cls):
        if cls.enabled:
            try:
                return get(cls.URL, headers=cls.HEADERS).content
            except Exception as error:
                raise ConnectionError(cls.CAMERA_ERROR.format(error))
        raise SkipCommand

    @classmethod
    def switch(cls):
        cls.enabled = not cls.enabled
        return 'ВКЛЮЧЕНО' if cls.enabled else 'ВЫКЛЮЧЕНО'
