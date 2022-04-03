import datetime
import io
from random import randint
from tempfile import gettempdir
import os

from requests import get
from moviepy.editor import VideoClip
from PIL import Image, ImageDraw
import numpy as np

from modules.exceptions import SkipCommand
from modules.settings.default_settings import (CAMERA_TOKEN,
                                               CAMERA_IMAGE_URL,
                                               CAMERA_ENABLED)

CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'
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
        fill='#F8F8FF',  # призрачно белый
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
    enabled = CAMERA_ENABLED
    frame_rate = 10
    HEADERS = {
        'Authorization': f'Basic {CAMERA_TOKEN}'
    }

    @classmethod
    def get_photo(cls):
        if not cls.enabled:
            raise SkipCommand
        try:
            return get(CAMERA_IMAGE_URL, headers=cls.HEADERS).content
        except Exception as error:
            raise ConnectionError(CAMERA_ERROR.format(error))

    @classmethod
    def get_video(cls, duration=10):
        file_name = os.path.join(
            gettempdir(),
            'GAM',
            f'video_{randint(1000, 9999)}.mp4'
        )
        try:
            video = VideoClip(
                make_frame=get_frame_from_camera,
                duration=duration
            )
            video.write_videofile(
                file_name,
                fps=Camera.frame_rate,
                audio=False
            )
            return file_name
        except Exception as error:
            os.remove(file_name)
            raise error

    @classmethod
    def switch(cls):
        cls.enabled = not cls.enabled
        return 'ВКЛЮЧЕНО' if cls.enabled else 'ВЫКЛЮЧЕНО'
