import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to $TWIZZY. Type 'ca' to get the contract address or 'x' to see our X page.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    
    if text == "ca":
        bot.reply_to(message, "Contract Address: 8UN4HQbskKB4tLrwe6VEsqvr2HfnPDHg4fKdUYBipump")
    elif text == "x":
        bot.reply_to(message, "Follow us on X: https://twitter.com/TwizzyCoin")
    else:
        bot.reply_to(message, "Thanks for your message. Type 'ca' or 'x' for quick links.")

bot.polling(none_stop=True)
