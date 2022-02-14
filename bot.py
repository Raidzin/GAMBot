from telebot import TeleBot

from bot_modules.os_function import get_telegram_token
from bot_modules.commands import commands, messages

if __name__ == '__main__':
    bot = TeleBot(token=get_telegram_token())


    @bot.message_handler()
    def separator(message):
        if message.text.startswith('/'):
            commands(bot, message)
        else:
            commands(bot, message)

    bot.polling(none_stop=True)

