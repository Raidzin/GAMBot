from bot import GAMbot
from bot_modules.configurator import Config
from bot_modules.bot_logger import logger

BOT_ERROR = 'Произошла ошибка {0} {1}'
BOT_STOP = 'БОТ ОСТАНОВЛЕН'

while True:
    try:
        bot = GAMbot(Config.get_token(Config.TELEGRAM_TOKEN_NAME))
        bot.run(interval=2)
    except Exception as error:
        error_message = BOT_ERROR.format(type(error), error)
        try:
            bot.bot.send_message(
                Config.get_token(Config.ADMIN_ID_NAME),
                error_message)
        finally:
            logger.error(error_message)
