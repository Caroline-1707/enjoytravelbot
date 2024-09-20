import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ('start', "Старт"),
    ('help', "Доступные команды"),
    ('lowprice', 'Цена по возрастанию'),
    ('highprice', 'Цена по убыванию'),
    ('bestdeal', 'Лучшие предложения'),
    ('history', 'История поиска')
)
