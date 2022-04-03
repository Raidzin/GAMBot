import io
from random import randint
from tempfile import gettempdir
import os

import numpy as np
from requests import get
from moviepy.editor import VideoClip
from PIL import Image

from modules.exceptions import SkipCommand
from modules.camera.video_filters import process_frame, add_datetime
from modules.settings.default_settings import (CAMERA_TOKEN,
                                               CAMERA_IMAGE_URL,
                                               CAMERA_ENABLED)

CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'


def get_video_file_name():
    file_name = os.path.join(
        gettempdir(),
        'GAM',
        f'video_{randint(1000, 9999)}.mp4'
    )
    video_folder = os.path.dirname(file_name)
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    return file_name


class Camera:
    enabled = CAMERA_ENABLED
    frame_rate = 10
    HEADERS = {
        'Authorization': f'Basic {CAMERA_TOKEN}'
    }

    @classmethod
    def switch(cls):
        cls.enabled = not cls.enabled
        return 'ВКЛЮЧЕНО' if cls.enabled else 'ВЫКЛЮЧЕНО'

    @classmethod
    def get_video(cls, duration=10):
        file_name = get_video_file_name()
        try:
            video = VideoClip(
                make_frame=cls.get_video_frame,
                duration=duration
            )
            video.write_videofile(
                file_name,
                fps=Camera.frame_rate,
                audio=False
            )
            return file_name
        except Exception as error:
            try:
                os.remove(file_name)
            except FileNotFoundError:
                pass
            raise error

    @classmethod
    def get_photo(cls):
        if not cls.enabled:
            raise SkipCommand
        try:
            return Image.open(io.BytesIO(get(
                CAMERA_IMAGE_URL,
                headers=cls.HEADERS).content))
        except Exception as error:
            raise ConnectionError(CAMERA_ERROR.format(error))

    @classmethod
    def get_video_frame(cls, *args):
        filters = add_datetime,
        frame = process_frame(cls.get_photo(), filters)
        return np.array(frame)
