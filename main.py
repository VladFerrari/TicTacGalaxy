import telebot
import os

bot = telebot.TeleBot(os.environ.get("BOTTOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот TicTac Galaxy 💫")

bot.polling()
