from bot_modules.os_function import Tokens
from bot_modules.bot_logger import logger
from bot_modules.camera import get_photo
from bot_modules.base_bot import BaseBot, Message


class GAMbot(BaseBot):

    def command_start(self, message: Message):
        self.bot.send_message(message.from_user.id, ':0')

    def command_photo(self, message: Message):
        self.bot.send_photo(message.from_user.id, get_photo())

    def command_commands(self, message: Message):
        self.bot.send_message(
            message.from_user.id,
            '\n'.join(['/' + command for command in self.commands])
        )


if __name__ == '__main__':
    bot = GAMbot(Tokens.get_token(Tokens.TELEGRAM_TOKEN_NAME))
    bot.run()
