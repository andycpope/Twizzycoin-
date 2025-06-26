import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to $TWIZZY. Type 'ca' to get the contract address.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == "ca":
        bot.reply_to(message, "Contract Address: 8UN4HQbskKB4tLrwe6VEsqvr2HfnPDHg4fKdUYBipump")
    else:
        bot.reply_to(message, "Thanks for your message.")

bot.polling(none_stop=True)
