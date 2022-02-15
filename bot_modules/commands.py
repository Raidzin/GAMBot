from telebot.types import Message
from telebot import TeleBot

from bot_modules.camera import get_photo
from bot_modules.bot_logger import logger


class Commands:

    @classmethod
    def get_all_commands(cls):
        commands = [
            command.replace('command_', '') for command in cls.__dict__
            if command.startswith('command_')
        ]
        return commands

    @classmethod
    def do_command(cls, bot: TeleBot, message: Message):
        command = message.text[1:]
        logger.info(f'command {command}, from {message.from_user.username}')
        if command not in cls.get_all_commands():
            bot.send_message(message.from_user.id, 'нет такой команды')
        else:
            getattr(cls, 'command_' + command)(bot, message)

    @classmethod
    def command_start(cls, bot: TeleBot, message: Message):
        bot.send_message(message.from_user.id, 'hello!, im on OOP')

    @classmethod
    def command_photo(cls, bot: TeleBot, message: Message):
        bot.send_photo(message.from_user.id, get_photo())


if __name__ == '__main__':
    print(Commands.__dict__)
    print(Commands.get_all_commands())
