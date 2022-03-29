import requests

from bot_modules.configurator import Config
from bot_modules.bot_logger import get_info_logs_tail, to_telegram_logs
from bot_modules.camera import Camera
from bot_modules.base_bot import BaseBot, Message


class GAMbot(BaseBot):

    def command_start(self, message: Message):
        self.bot.send_message(message.from_user.id, ':0')

    def command_photo(self, message: Message):
        self.bot.send_photo(message.from_user.id, Camera.get_photo())

    def command_commands(self, message: Message):
        self.bot.send_message(
            message.from_user.id,
            '\n'.join(['/' + command for command in self.commands])
        )

    def command_ip(self, message: Message):
        self.bot.send_message(
            message.from_user.id,
            requests.get('https://ident.me').text
        )

    def command_logs(self, message: Message):
        self.bot.send_message(
            message.from_user.id,
            to_telegram_logs(get_info_logs_tail(5))
        )

    def command_switch(self, message: Message):
        enabled = Camera.switch()
        self.bot.send_message(
            message.from_user.id,
            enabled,
        )


bot = GAMbot(Config.get_token(Config.TELEGRAM_TOKEN_NAME))

if __name__ == '__main__':
    bot.run()
