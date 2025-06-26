import telebot

BOT_TOKEN = "7625675407:AAHN2K4xZ3fNa4Ze_V47_BEjvuhDRyalJR4"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: message.text.lower() in ["x", "ca", "website"])
def handle_message(message):
    text = message.text.lower()
    if text == "x":
        bot.reply_to(message, "Follow the $TWIZZY Twitter: https://twitter.com/twizzycoin")
    elif text == "ca":
        bot.reply_to(message, "Contract Address: 8UN4HQbskKB4tLrwe6VEsqvr2HfnPDHg4fKdUYBipump")
    elif text == "website":
        bot.reply_to(message, "🌐 TWIZZY Website: https://considerate-tweak-094048.framer.app")

bot.polling(non_stop=True)
