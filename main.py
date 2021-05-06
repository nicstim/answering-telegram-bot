import telebot

token = ""
admin_id = ""

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['id'])
def get_id(message):
    bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать!")


@bot.message_handler(content_types=['text'])
def body(message):
    if message.reply_to_message:
        bot.send_message(message.reply_to_message.forward_from.id, message.text)
    else:
        bot.forward_message(admin_id,
                            message.from_user.id,
                            message.id
                            )


bot.polling()
