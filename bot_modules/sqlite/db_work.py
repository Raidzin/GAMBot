import sqlite3
from bot_modules.configurator import Config


class DataBase:
    conn = sqlite3.connect(Config.get_path(Config.DB_PATH))
    cur = conn.cursor()
