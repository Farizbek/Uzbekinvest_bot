import telebot
from telebot import types


bot = telebot.TeleBot("5569375690:AAHqq9wMtkbyjz14kptApDZMdPZkm36wMpQ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom botimizga hush kelibsiz\nBitronta shartni talang!!!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
bot.polling()