import telebot

# Your bot token
BOT_TOKEN = '7933122221:AAGVxsByONSuECDUtdnJJbamZBKEg9RSd4s'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to $TWIZZY HQ. The future is now.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if 'x' in message.text.lower():
        bot.reply_to(message, "Follow us on Twitter: https://twitter.com/twizzycoin")
    else:
        bot.reply_to(message, "Thanks for your message. Stay tuned for $TWIZZY updates.")

bot.polling()
