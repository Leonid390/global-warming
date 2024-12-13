import telebot
from bot_logic import gen_pass


bot = telebot.TeleBot("7131412717:AAGpOXPfuqxP8qfJSyp6AsH0uby-a6FmXuE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот по определению CO2. Напиши команду /hello, /bye или /co2")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")


saved_message = ''

waiting_chislo = False

@bot.message_handler(commands=['co2'])
def countedcarbon(message):
    global waiting_chislo
    waiting_chislo = True
    bot.reply_to(message, "сколько?:")

@bot.message_handler(func=lambda message: waiting_chislo)
def receive_number(message):
    global waiting_chislo
    
    try:
        int_message = int(message.text)  # Пробуем преобразовать в int
        waiting_chislo = False  # Сбрасываем состояние
        bot.reply_to(message, f"Удачи с экологией! ВЫ ВЫДЕЛЯЕТЕ, ВНИМАНИЕ, {int_message + int_message} мЭкв/л CO2")
        if int_message + int_message > 30:
            bot.reply_to(message, f"капец ты паровоз")
        elif int_message + int_message <= 30:
            bot.reply_to(message, f"МЕГАХАРОШ")
    except ValueError:
        bot.reply_to(message, "Ошибка: это не число. Пожалуйста, введите число.")


# Запускаем бота
bot.polling()