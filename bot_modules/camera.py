import io
from random import randint

from requests import get
from moviepy.editor import VideoClip
from PIL import Image
import numpy as np

from bot_modules.configurator import Config


class SkipCommand(Exception):
    pass


class Camera:
    enabled = True
    frame_rate = 10
    URL = 'http://192.168.77.60/image.jpg'
    HEADERS = {
        'Authorization': f'Basic {Config.get_token(Config.CAMERA_TOKEN_NAME)}'
    }
    CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'

    @classmethod
    def get_photo(cls):
        if not cls.enabled:
            raise SkipCommand
        try:
            return get(cls.URL, headers=cls.HEADERS).content
        except Exception as error:
            raise ConnectionError(cls.CAMERA_ERROR.format(error))

    @classmethod
    def get_numpy_image(cls, *args):
        photo = cls.get_photo()
        return np.array(Image.open(io.BytesIO(photo)))

    @classmethod
    def get_video(cls, duration=5):
        if not cls.enabled:
            raise SkipCommand
        file_name = f'video_{randint(1000, 9999)}.mp4'
        video = VideoClip(make_frame=cls.get_numpy_image, duration=duration)
        video.write_videofile(file_name, fps=Camera.frame_rate, audio=False)
        return file_name

    @classmethod
    def switch(cls):
        cls.enabled = not cls.enabled
        return 'ВКЛЮЧЕНО' if cls.enabled else 'ВЫКЛЮЧЕНО'
