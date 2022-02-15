from telebot import TeleBot

from bot_modules.os_function import Tokens
from bot_modules.commands import Commands
from bot_modules.bot_logger import logger

ADMIN_ID = 'None'


class GAMbot:
    bot = TeleBot(
        token=Tokens.get_token(
            Tokens.TELEGRAM_TOKEN_NAME
        )
    )

    @classmethod
    def message_handler(cls):
        @cls.bot.message_handler()
        def do_command(message):
            Commands.do_command(cls.bot, message)

    logger.info('bot start')

    @classmethod
    def run(cls, interval=0):
        cls.message_handler()
        cls.bot.polling(none_stop=True, interval=interval)


if __name__ == '__main__':
    GAMbot.run()
