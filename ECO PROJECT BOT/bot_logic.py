import random
import telebot
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

