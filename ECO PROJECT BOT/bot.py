import telebot
from bot_logic import gen_pass


bot = telebot.TeleBot("")

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

numbers = []

@bot.message_handler(commands=['co2'])
def send_welcome(message):
    bot.reply_to(message, "Если хотите получить ваши результаты за год, то напишите следующими сообщениями числа, обозначающие: затреченную электроэнергию (в среднем 1090,4 млрд кВт•ч), выбросы транспорта (для этого количество поездок за год умножте на 148) и для каждых 100 грамм мяса умножте значение на 24.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Пробуем преобразовать сообщение в число
        number = float(message.text)
        numbers.append(number)

        # Проверяем, сколько чисел уже получено
        if len(numbers) == 3:
            total = sum(numbers)
            bot.reply_to(message, f"Сумма ваших чисел: {total}")
            # Очищаем список для следующего набора чисел
            numbers.clear()
        else:
            bot.reply_to(message, f"Вы отправили {len(numbers)} число(а). Отправьте еще {3 - len(numbers)}.")
    except ValueError:
        bot.reply_to(message, "Пожалуйста, отправьте число.")



# Запускаем бота
bot.polling()