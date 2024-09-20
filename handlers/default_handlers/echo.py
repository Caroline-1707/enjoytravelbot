from telebot.types import Message
from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния

@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(message, f"Для начала работы выбери любую команду из меню\n"
                          f"Либо нажми кнопку")
