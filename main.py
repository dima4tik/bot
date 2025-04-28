import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('7531422376:AAHUzj74xeDJNbcQ2ysmvJAY7HUto70LhQ8')
#
# markup = types.InlineKeyboardMarkup()
# btn1 = types.InlineKeyboardButton('Наша группа', url="https://t.me/+l8NE4eX3JhE3YTQ6")
# markup.row(btn1)
# markup.add(types.InlineKeyboardButton('Удалить', callback_data='delete'))
#
#
# @bot.message_handler(commands=['group'])
# def main(message):
#     webbrowser.open('https://t.me/+l8NE4eX3JhE3YTQ6')
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, "Вас приветсвует Бот дели на 2, уважаемая просьба не писать суда")
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, "ЧЁ НЕ ПОНЯТНО ТО?")
#
# @bot.message_handler(commands=['info'])
# def main(message):
#     bot.send_message(message.chat.id, f'{message.from_user.first_name}' , reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text', 'audio', 'document', 'video', ])
# def main(message):
#     bot.reply_to(message.chat.id, 'Ну и зачем?')
#
# @bot.message_handler()
# def main(message):
#     if message.text.lower == 'макар' or 'makar':
#         bot.send_message(message.chat.id, "маладец")
#     elif message.text.lower == 'jura' or 'юра':
#         bot.reply_to(message.chat.id, "тоже не плохо")
#
#
# bot.polling(none_stop=True)


# Обработчик всех текстовых сообщений
KEYWORD = 'юра'

# Функция для проверки сообщения
def check_keyword_in_message(message, keyword):
    return keyword.lower() in message.text.lower()

# Обработчик всех текстовых сообщений
@bot.message_handler(content_types=['text'])
def echo_all(message):
    try:
        # Проверяем, что сообщение из группы (чтобы не отвечать в личку)
        if message.chat.type in ['group', 'supergroup']:
            # Проверяем, содержит ли сообщение нужное слово
            if check_keyword_in_message(message, KEYWORD):
                bot.reply_to(message, "lox")
    except Exception as e:
        print(f"Error occurred: {e}")

bot.polling(non_stop=True)
