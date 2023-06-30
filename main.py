import telebot
from telebot import types

bot = telebot.TeleBot('5844849473:AAEDoV95mmhGduMgtahGepwS7biz5a2BHF0')

file = open('data.txt', encoding='utf-8')
for row in file:
    hello = row
    #print()

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(hello)
    btn2 = types.KeyboardButton("Чей Крым?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот-помощник".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == hello):
        bot.send_message(message.chat.id, text="Привееет, рад что ты со мной!)")
    elif (message.text == "Чей Крым?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Наш")
        btn2 = types.KeyboardButton("Не наш")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Ну-ка ответь мне на вопрос", reply_markup=markup)

    elif (message.text == "Наш"):
        bot.send_message(message.chat.id, "Правильный ответ, Вы прошли проверку")

    elif message.text == "Не наш":
        bot.send_message(message.chat.id, text="Попался! Шпион!")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(hello)
        button2 = types.KeyboardButton("Чей Крым?")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

#print(file.read())

#s = file.readlines()
#print(s)

bot.polling(none_stop=True)

