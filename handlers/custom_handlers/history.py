from loader import bot
from telebot.types import Message
from database import write_db


@bot.message_handler(commands=["history"])
def history(message: Message) -> None:
    history_info = write_db.get_history(chat_id=str(message.chat.id))
    if history_info:
        for record in history_info:
            uid = record.uid
            text = f"Дата и время запроса: {record.datetime}\nКоманда: {record.command}\nГород: {record.city}\n"
            hotels = write_db.get_hotels(uid=uid)
            if hotels:
                text += '\nНайденные отели:\n'
                bot.send_message(message.from_user.id, text)
                for i, hotel in enumerate(hotels):
                    text_hotel = f"\n{i + 1}.\nНазвание отеля: {hotel.name}\n"\
                                 f"Адрес: {hotel.address}"\
                                 f"\nСсылка: {hotel.link}"\
                                 f"\nЦена за сутки: {hotel.price} USD\n"
                    bot.send_message(message.from_user.id, text=text_hotel)

                bot.send_message(message.from_user.id, 'Готово!')
            else:
                bot.send_message(message.from_user.id, text)
                bot.send_message(message.from_user.id, 'Не найдено подходящих отелей.')
    else:
        bot.send_message(chat_id=message.chat.id, text='История запросов пуста.')
