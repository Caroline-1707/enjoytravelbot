# Enjoy Travel Bot

**Enjoy Travel Bot** — это простой и удобный Telegram-бот, который помогает пользователям находить информацию об отелях по всему миру. Бот использует Rapid API для получения данных об отелях и предоставляет пользователям актуальную информацию.

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://t.me/my_enjoytravelbot)

---

## Основные функции

- Поиск отелей по всему миру.
- Получение информации о ценах, расположении и рейтинге отелей.
- Удобный интерфейс для взаимодействия с ботом.
- Интеграция с календарем для выбора дат.

---

## Технологии

- **Python 3.11** — основной язык разработки.
- **PyTelegramBotAPI** — фреймворк для создания Telegram-ботов.
- **SQLite3** — база данных для хранения информации.
- **Requests** — библиотека для работы с HTTP-запросами.
- **Telebot-Calendar** — модуль для работы с календарем в Telegram.

---

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Caroline-1707/enjoytravelbot.git
   cd enjoytravelbot
   
2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   
3. **Настройте переменные окружения:**
   - Переименуйте файл .env.template в .env.
   - Откройте файл .env и вставьте следующие данные:
     ```plaintext
     TELEGRAM_BOT_TOKEN=ваш_токен_бота
     RAPIDAPI_KEY=ваш_api_ключ
   - Чтобы получить TELEGRAM_BOT_TOKEN, создайте бота через @BotFather.
   - Для получения RAPIDAPI_KEY зарегистрируйтесь на RapidAPI и скопируйте ключ из раздела "My Apps" => "Ваш API ключ" => "Security".
  
4. **Запустите бота:**
   ```bash
   python main.py

## Использование

1. Перейдите в Telegram и найдите бота по имени @my_enjoytravelbot.
2. Начните взаимодействие с ботом, используя команду /start.
3. Следуйте инструкциям бота для поиска отелей.

## Структура проекта

```text
enjoytravelbot/
├── .env.template          # Шаблон для файла .env
├── main.py                # Основной файл для запуска бота
├── requirements.txt       # Список зависимостей
├── README.md              # Документация (этот файл)
├── database/              # Папка для базы данных SQLite3
├── handlers/              # Модули для обработки команд и сообщений
├── keyboards/             # Клавиатуры и кнопки для бота
├── utils/                 # Вспомогательные функции и утилиты
└── config.py              # Конфигурация бота
```

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

## Автор

Caroline-1707

GitHub: [Caroline-1707](https://github.com/Caroline-1707)

Telegram: [@Caroline_17](https://t.me/Caroline_17)

