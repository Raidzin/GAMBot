import datetime
import io
from random import randint

from requests import get
from moviepy.editor import VideoClip
from PIL import Image, ImageDraw
import numpy as np

from modules.configurator import Config
from modules.exceptions import SkipCommand

DATE_FORMAT = '%a %d-%m-%Y\n%H:%M %S'
"""
пример:
Fri 01-04-2022
17:25 24
"""


def add_date_to_image(image):
    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        (10, 10),
        f'{datetime.datetime.now().strftime(DATE_FORMAT)}',
        fill='#F0F0F0'
    )
    return image


def get_image_from_photo(photo):
    return Image.open(io.BytesIO(photo))


def get_frame_from_camera(*args):
    return np.array(
        add_date_to_image(
            get_image_from_photo(
                Camera.get_photo()
            )
        )
    )


class Camera:
    enabled = True
    frame_rate = 10
    URL = 'http://192.168.77.60/image.jpg'
    CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'
    HEADERS = {
        'Authorization': f'Basic {Config.get_token(Config.CAMERA_TOKEN_NAME)}'
    }

    @classmethod
    def get_photo(cls):
        if not cls.enabled:
            raise SkipCommand
        try:
            return get(cls.URL, headers=cls.HEADERS).content
        except Exception as error:
            raise ConnectionError(cls.CAMERA_ERROR.format(error))

    @classmethod
    def get_video(cls, duration=10):
        video = VideoClip(make_frame=get_frame_from_camera, duration=duration)
        file_name = f'video_{randint(1000, 9999)}.mp4'
        video.write_videofile(file_name, fps=Camera.frame_rate, audio=False)
        return file_name

    @classmethod
    def switch(cls):
        cls.enabled = not cls.enabled
        return 'ВКЛЮЧЕНО' if cls.enabled else 'ВЫКЛЮЧЕНО'
