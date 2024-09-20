import time
from telebot.types import Message, InputMediaPhoto
from handlers.custom_handlers.operations.api_requests import hotels_request
from loader import bot
from states.hotel_info import HotelPriceState
from database import write_db


@bot.message_handler(state=HotelPriceState.info)
def get_search_results(
        message: Message,
        count_photos=0,
        stop_iter=5,
        sort_order="PRICE_LOW_TO_HIGH",
        call_chat_id=None,
        is_reverse=False) -> None:
    """
    Хендлер для вывода информации

    :param call_chat_id:
    :param is_reverse: вывод в обратном порядке при команде /highprice
    :param sort_order: режим запроса
    :param message: сообщение пользователя
    :param count_photos: кол-во фотографий для каждого отеля
    :param stop_iter: параметр для предотвращения рекурсии
    :return: None
    """

    if call_chat_id is None:
        user_id = message.from_user.id
        chat_id = message.chat.id
    else:
        user_id, chat_id = call_chat_id, call_chat_id

    if stop_iter:
        try:
            with bot.retrieve_data(user_id, chat_id) as hotels_data:
                start = time.time()
                if is_reverse:
                    data = hotels_request(user_id=user_id, chat_id=chat_id, sort_order=sort_order, is_reverse=True)
                else:
                    data = hotels_request(user_id=user_id, chat_id=chat_id, sort_order=sort_order)
                stop = time.time()
                time_out = round(stop - start)
                hotel_count = -1
                flag_distance_list = [False if int(elem['distance']) <= int(hotels_data["distance_max"])
                                      else True for elem in data.values() if 'distance_max' in hotels_data.keys()]

                if all(flag_distance_list) and flag_distance_list:
                    data = {}

                write_db.set_history(
                    hotels_data['city_id'],
                    str(hotels_data['chat_id']),
                    hotels_data['date'],
                    hotels_data['city'],
                    hotels_data['command']
                )

                for name, hotel in data.items():
                    hotel_count += 1

                    if flag_distance_list:
                        if flag_distance_list[hotel_count]:
                            bot.send_message(user_id, f'{hotel_count + 1} отель не подходит по расстоянию от центра')
                            continue

                    text = f'Название отеля: {name}\n' \
                           f'ID отеля: {hotel["hotel_id"]}\n' \
                           f'Адрес: {hotel["address"]}\n'

                    text += f'Диапазон расстояний: от 0 до ' \
                            f'{hotels_data["distance_max"]}\n' \
                        if "distance_max" in hotels_data.keys() else ''

                    metric_list = hotels_data["metric"].split()
                    metric, value = metric_list[0], metric_list[1]

                    text += f'Расстояние от центра города: ' \
                            f'{round(hotel["distance"] * float(value))} {metric}\n'

                    text += f'Диапазон цен: от ${hotels_data["price_min"]} до ${hotels_data["price_max"]}\n' \
                        if "price_min" in hotels_data.keys() else ''

                    text += f'Цена за ночь: ${int(hotel["price"]):,d} ({(hotel["price"] * 90):,d} рублей)\n' \
                        if hotel['price'] is not None else ''

                    text += f'Длительность проживания, дней: {hotel["total_days"]}\n'

                    text += f'Итоговая стоимость: ${hotel["total_price"]:,d} ({(hotel["total_price"] * 90):,d} рублей)\n' \
                        if hotel['price'] is not None else ''

                    text += f'Рейтинг: {hotel["rating"]}\n' \
                            f'Ссылка на отель: {hotel["linc"]}\n'

                    write_db.set_hotels(
                        hotels_data['city_id'],
                        hotel['hotel_id'],
                        name,
                        hotel['address'],
                        hotel['price'],
                        hotel['linc']
                    )

                    if count_photos:
                        data_ph = hotel['photos'][:count_photos]
                        photos = [InputMediaPhoto(elem) for elem in data_ph]
                        if len(photos) >= 2:
                            bot.send_media_group(user_id, photos)
                        else:
                            bot.send_photo(user_id, photo=data_ph[0])

                        for photo in data_ph:
                            write_db.set_photos(
                                hotel['hotel_id'],
                                photo
                            )

                    bot.send_message(user_id, text)
                    bot.send_message(user_id, f'{hotel_count + 1}')

                if data:
                    bot.send_message(user_id, 'Готово!')
                else:
                    bot.send_message(user_id, 'К сожалению, подходящих отелей не найдено.')
                bot.send_message(user_id, f'Время выполнения запроса: {time_out} сек.')
                bot.set_state(user_id, None, chat_id)

        except Exception as e:
            stop_iter -= 1
            get_search_results(message, count_photos=count_photos, stop_iter=stop_iter, call_chat_id=call_chat_id)
    else:
        bot.send_message(user_id,
                         'Возникла непредвиденная ошибка,\nПроверь соединение с интернетом')
        bot.set_state(user_id, None, chat_id)
