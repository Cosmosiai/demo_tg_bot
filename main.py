import telebot
from dotenv import load_dotenv
import os

print('hello world')

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(content_types=['text'])
def get_text_messages(messege):
    bot.send_message(messege.from_user.id, "I know what u wrote me"+str(messege.text))

bot.polling(none_stop=True, interval=0)