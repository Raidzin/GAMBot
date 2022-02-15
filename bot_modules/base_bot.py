from telebot import TeleBot
from telebot.types import Message

from bot_modules.bot_logger import logger

GET_COMMAND = 'КОМАНДА {0}, ОТ {1}'
SUCCESS = 'ФУНКЦИЯ {0} УСПЕХ '
START = 'БОТ ЗАПУЩЕН'


class BaseBot:
    def __init__(self, token):
        self.bot = TeleBot(token=token)
        self.commands = [
            command.replace('command_', '') for command in self.__dir__()
            if command.startswith('command_')
        ]

    def message_handler(self):
        @self.bot.message_handler()
        def message_handler(message):
            self.do_command(message)
            logger.info(SUCCESS.format(message.text))

    def do_command(self, message: Message):
        command = message.text[1:]
        logger.info(GET_COMMAND.format(command, message.from_user.username))
        if command not in self.commands:
            self.bot.send_message(message.from_user.id, 'нет такой команды')

        else:
            getattr(self, 'command_' + command)(message)

    def run(self, interval=0):
        self.message_handler()
        logger.info(START)
        self.bot.polling(none_stop=True, interval=interval)
