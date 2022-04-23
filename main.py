import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, "Hello!")



@bot.message_handler(commands=['claim'])
def claim(message):
  bot.send_message(message.chat.id, "Please Enter a CLAIM KEY!")

  
@bot.message_handler(commands=[os.getenv('mKey')])
def link(message):
  bot.send_message(message.chat.id, os.getenv('mClaim'))

  
bot.polling()
