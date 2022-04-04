from sys import argv


def make_db():
    from modules.db.models import Base, engine
    Base.metadata.create_all(engine)
    print('База данных успешно записана!')


def run_bot():
    from bot import bot
    from modules.settings.default_settings import ADMIN_ID
    from modules.bot_logger import logger

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
                logger.error(error_message)


match argv[1]:
    case 'make_db':
        make_db()
    case 'run_bot':
        run_bot()
