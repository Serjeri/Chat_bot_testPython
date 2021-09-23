# Написать чат пода ,который выдает погоду.

import math

import telebot
import requests,json

bot = telebot.TeleBot("")

def get_connect (Str):
     key = "8ab8dd8e10c2a1ae46c279684b638c3e"
     URL_TEMPLATE = "http://api.openweathermap.org/data/2.5/weather?q=" + Str + "&appid=" + key
     w = requests.get( URL_TEMPLATE ).json()
     Celsium = (w['main']['temp'] - 32) * 5 / 9
     return str(math.ceil(Celsium))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

       if message.text == 'Привет':
           return bot.send_message( message.from_user.id, 'Привет, чем я вам могу помочь ?' )
       if message.text == 'Погода' or message.text == 'Привет, погода':
           return bot.send_message( message.from_user.id, 'Введите страну ' )
       if message.text == message.text or message.text != 0:
           return bot.send_message( message.from_user.id, 'Темпиратура = ' + get_connect( message.text ) + ' по цельсию в ' + message.text )



bot.polling(none_stop=True, interval=0)# слушатель сообщений
