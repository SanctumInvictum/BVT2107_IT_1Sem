import telebot
from telebot import types

token = '2086590525:AAFnueqlFIAbcRW4U4_GPhBjd4tYhgeTywg'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/who")
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу сделать тоже самое, что и вы только меньше.')
    bot.send_message(message.chat.id, 'У меня есть команда /who, которая выдаст имя моего автора.')
    bot.send_message(message.chat.id, 'Возможно, тут есть ещё команда, о которой мне нельзя говорить...')

@bot.message_handler(commands=['who'])
def who(message):
    bot.send_message(message.chat.id, 'БВТ2107 Соколов Юрий — мой автор.')

@bot.message_handler(commands=['42'])
def fortytwo(message):
    bot.send_message(message.chat.id, 'Я не понимаю о чем вы')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Лучше послушай анекдот: В линейном пространстве вождей базисом является плесень и липовый мёд.')
    elif message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'Это печально')
    elif message.text.lower() == "42424242":
        bot.send_message(message.chat.id, '░░██╗██╗██████╗░')
        bot.send_message(message.chat.id, '░██╔╝██║╚════██╗')
        bot.send_message(message.chat.id, '██╔╝░██║░░███╔═╝')
        bot.send_message(message.chat.id, '███████║██╔══╝░░')
        bot.send_message(message.chat.id, '╚════██║███████╗')
        bot.send_message(message.chat.id, '░░░░░╚═╝╚══════╝')
    else:
        bot.send_message(message.chat.id, 'Возможно, стоит попробоавть команду /help. Рекомендую.')

bot.polling()