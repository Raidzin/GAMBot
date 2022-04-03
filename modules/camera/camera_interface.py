from io import BytesIO

from requests import get
from PIL import Image

CAMERA_ERROR = 'Не удалось получить фото с камеры, {}'


def get_photo(url, headers):
    try:
        return Image.open(BytesIO(
            get(
                url,
                headers=headers
            ).content
        ))
    except Exception as error:
        raise ConnectionError(CAMERA_ERROR.format(error))
