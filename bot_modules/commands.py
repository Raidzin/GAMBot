from bot_modules.camera import get_photo


def commands(bot, message):
    match message.text[1:]:
        case 'photo':
            bot.send_photo(message.from_user.id, get_photo())
        case _:
            bot.send_message(message.from_user.id, 'Неизвестная команда')


def messages(bot, message):
    pass
