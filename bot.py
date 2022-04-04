import os

import requests

from modules.settings.default_settings import TELEGRAM_TOKEN
from modules.camera.camera import Camera
from modules.base_bot import BaseBot, Message


class GAMbot(BaseBot):

    def command_start(self, message: Message):
        self.bot.send_message(message.from_user.id, ':0')

    def command_photo(self, message: Message):
        self.check_is_known(message)
        self.bot.send_photo(message.from_user.id, Camera.get_photo())

    def command_video(self, message: Message):
        self.check_is_known(message)
        self.bot.send_message(message.from_user.id, 'подождите 10 сек')
        filename = Camera.get_video()
        with open(filename, 'rb') as video:
            self.bot.send_video(message.from_user.id, video)
        os.remove(filename)

    def command_switch(self, message: Message):
        self.check_is_admin(message)
        enabled = Camera.switch()
        self.bot.send_message(
            message.from_user.id,
            enabled,
        )

    def command_commands(self, message: Message):
        self.check_is_admin(message)
        self.bot.send_message(
            message.from_user.id,
            '\n'.join(['/' + command for command in self.commands])
        )

    def command_ip(self, message: Message):
        self.check_is_admin(message)
        self.bot.send_message(
            message.from_user.id,
            requests.get('https://ident.me').text
        )

    # def command_logs(self, message: Message):
    #     self.check_is_admin(message)
    #     self.bot.send_message(
    #         message.from_user.id,
    #         to_telegram_logs(get_info_logs_tail(5))
    #     )
    # нужно переделать


bot = GAMbot(TELEGRAM_TOKEN)

if __name__ == '__main__':
    bot.run()
