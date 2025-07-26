import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get("BOTTOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот TicTac Galaxy 🪐")

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route("/")
def home():
    return "✅ TicTac Galaxy Telegram Bot работает."

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://tacgalaxy.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
