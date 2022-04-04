import os

from modules.settings.tokens import get_token

TELEGRAM_TOKEN = get_token('TELEGRAM_TOKEN')
ADMIN_ID = get_token('ADMIN_ID')

BASE_PATH = os.getcwd()
LOG_FILE_ABSOLUTE_PATH = os.path.join(BASE_PATH, '.GAM.log')

DB_PATH = get_token('DB_PATH')

CAMERA_ENABLED = True
if CAMERA_ENABLED:
    CAMERA_TOKEN = get_token('CAMERA_TOKEN')
    CAMERA_IMAGE_URL = 'http://192.168.77.60/image.jpg'
