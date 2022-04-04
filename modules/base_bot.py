from telebot import TeleBot
from telebot.types import Message

from modules.bot_logger import logger
from modules.exceptions import SkipCommand
from modules.db.core import get_or_create
from modules.db.models import User

GET_COMMAND = 'КОМАНДА {0}, ОТ {1}, {2}, {3}'
SUCCESS = 'ФУНКЦИЯ {0} УСПЕХ '
START = 'БОТ ЗАПУЩЕН'


def get_user(message: Message):
    user_info = {
        'pk': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
    }
    user, _ = get_or_create(User, defaults=user_info, pk=user_info['pk'])
    return user


class BaseBot:
    """
    Базовый класс бота.
    Вы должный унаследовать свой класс Bot(BaseBot):
    в нём пишутся команды по типу command_start(self, message)
    где start это команда на которую будет отвечать бот,
    а message это сообщения класса telebot.types Message
    """

    def __init__(self, token):
        self.bot = TeleBot(token=token)
        self.commands = [
            command.replace('command_', '') for command in self.__dir__()
            if command.startswith('command_')
        ]

    def message_handler(self):
        """
        Функция, которая создаёт необходимый handler для работы библиотеки
        pytelegrambotapi и передаёт полученные сообщения в функцию do_command
        """

        @self.bot.message_handler()
        def message_handler(message):
            self.do_command(message)
            logger.debug(SUCCESS.format(message.text))

    def do_command(self, message: Message):
        """
        Функция принимает сообщение от пользователя, проверяет наличие такой
        команды и вызывает её если она существует.
        :param message: сообщении типа telebot.types Message
        :return:
        """
        command = message.text[1:]
        logger.info(GET_COMMAND.format(
            command,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        ))
        if command not in self.commands:
            self.bot.send_message(message.from_user.id, 'нет такой команды')
        else:
            try:
                getattr(self, 'command_' + command)(message)
            except SkipCommand:
                pass

    def run(self, interval=0):
        """
        Функция запуска бота
        :param interval: интервал опроса телеги
        :return:
        """
        self.message_handler()
        logger.info(START)
        self.bot.polling(none_stop=True, interval=interval)

    def check_is_admin(self, message: Message):
        user = get_user(message)
        if user.role > 0:
            self.bot.send_message(
                message.from_user.id,
                'У вас нет доступа'
            )
            raise SkipCommand

    def check_is_known(self, message: Message):
        user = get_user(message)
        if user.role > 1:
            self.bot.send_message(
                message.from_user.id,
                'У вас нет доступа'
            )
            raise SkipCommand
