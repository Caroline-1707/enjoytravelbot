# EnjoyTravelBot
Enjoy Travel Bot https://t.me/my_enjoytravelbot
Простой телеграм бот, с помощью которого можно получать информацию об отелях по всему миру, в работе использует Rapid Api.
В работе использовано:
Python (3.11)
PyTelegramBotApi (Telegram Bot framework)
SQLite3 (database)
requests
telebot-calendar
Установка:
Необходимо скопировать содержимое репозитория в отдельный каталог.
Установить все библиотеки из requirements.txt
Файл .env.template переименовать в .env. Внести в него необходимые данные по ключам. Для этого:
Создать своего бота с помощью @BotFather, запросить токен
Зарегистрироваться на сайте rapidapi.com/apidojo/api/hotels4/, скопировать API ключ (вкладка My Apps => Ваш API ключ => Security)
Запустить файл main.py.
