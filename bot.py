import requests

from bot_modules.configurator import Config
from bot_modules.bot_logger import get_info_logs_tail, to_telegram_logs
from bot_modules.camera import get_photo
from bot_modules.base_bot import BaseBot, Message


class GAMbot(BaseBot):
    camera_enabled = True

    def command_start(self, message: Message):
        self.bot.send_message(message.from_user.id, ':0')

    def command_photo(self, message: Message):
        if self.camera_enabled:
            self.bot.send_photo(message.from_user.id, get_photo())

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
        self.camera_enabled = not self.camera_enabled
        if self.camera_enabled:
            self.bot.send_message(message.from_user.id, 'выключено')
        else:
            self.bot.send_message(message.from_user.id, 'включено')




bot = GAMbot(Config.get_token(Config.TELEGRAM_TOKEN_NAME))

if __name__ == '__main__':
    bot.run()
