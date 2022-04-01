# GAM TELEBOT
Прототип микро фреймворка для телеграм ботов общей направленности

## Процедура запуска:

#### Скачать проект
```shell
git clone https://github.com/Raidzin/GAMBot.git
```

#### Установить необходимые зависимости

В директории проекта

```shell
pip install -r requirements.txt
```

#### Создать файл `.env` в директории проекта и вписать в него необходимые переменные
```
TELEGRAM_TOKEN=<токен от телеграма>
CAMERA_TOKEN=<токен для доступа к вебкамере>
ADMIN_ID=<теллеграм id аккаунта администратора>

BASE_PATH=<путь до папки проекта>
LOG_PATH=<путь до файла логов>
LOG_NAME=<имя файла логов>
DB_PATH=<путь до базы данных sqlite3>
DB_NAME=<имя файла базы данных sqlite3>
```

#### Запуск бота
 
В директории проекта

```shell
python run_bot.py
```

## Авторы:

- [RAIDZIN](https://github.com/Raidzin, "GitHub")