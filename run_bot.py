from bot import GAMbot
from bot_modules.os_function import Tokens
from bot_modules.bot_logger import logger

BOT_ERROR = 'Произошла ошибка {0} {1}'

while True:
    try:
        GAMbot.run()
    except Exception as error:
        error_message = BOT_ERROR.format(type(error), error)
        try:
            GAMbot.bot.send_message(
                Tokens.get_token(Tokens.ADMIN_ID_NAME),
                error_message)
        finally:
            logger.error(error_message)