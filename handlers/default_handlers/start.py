from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.from_user.id, f"""
    Привет, {message.from_user.full_name}! 
    
    Я - Enjoy Travel, бот для поиска отелей. Вот что я могу:
        
        1. Показать топ отелей в выбранном городе по заданным параметрам, 
        2. Вывести основную информацию и фото выбранных отелей,
        3. Отправить ссылку на отель для бронирования,
        А еще я умею запоминать историю, и ты всегда сможешь найти понравившийся отель в истории поиска.
        
        Начнем?
        
        Нажав /help, ты увидишь список всех доступных команд."""
                     )
