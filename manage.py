from sys import argv


def migrate():
    from modules.db.models import Base, get_engine
    Base.metadata.create_all(get_engine())
    print('База данных успешно записана!')


def run_bot():
    from bot import bot
    from modules.settings.default_settings import ADMIN_ID
    from modules.logger import Logger

    BOT_ERROR = 'Произошла ошибка {0} {1}'
    print('Бот запущен')

    while True:
        try:
            bot.run(interval=2)
        except Exception as error:
            error_message = BOT_ERROR.format(type(error), error)
            try:
                bot.bot.send_message(
                    ADMIN_ID,
                    error_message)
            finally:
                Logger.error(error_message)


match argv[1]:
    case 'migrate':
        migrate()
    case 'runbot':
        run_bot()
    case _:
        print('Команда не найдена')
