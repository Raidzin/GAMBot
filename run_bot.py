from bot import bot
from modules.settings.default_settings import ADMIN_ID
from modules.bot_logger import logger

BOT_ERROR = 'Произошла ошибка {0} {1}'

while True:
    try:
        bot.run(interval=2)
    except Exception as error:
        error_message = BOT_ERROR.format(type(error), error)
        try:
            bot.bot.send_message(
                ADMIN_ID,
                error_message)
        finally:
            logger.error(error_message)
