from requests import get

from bot_modules.os_function import get_camera_token

URL = 'http://192.168.77.60/image.jpg'
HEADERS = {'Authorization': f'Basic {get_camera_token()}'}


def get_photo():
    return get(URL, headers=HEADERS).content
