import telebot
from telebot import types
from mysql import connector

bot = telebot.TeleBot("5569375690:AAHqq9wMtkbyjz14kptApDZMdPZkm36wMpQ")

# Malumotlar bazasiga ulash
def connect_to_base():
    mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sugurta_uz"
    )
    return mydb

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    contact = types.KeyboardButton("Telefon nomer", request_contact=True)
    markup.add(contact)
    bot.send_message(message.chat.id, "Avtosug'urta botimizga xush kelibsiz!!!\nBotdan foydalanishda davom etishingiz uchun ro'yxatdan o'ting!!!", reply_markup=markup)
    bot.register_next_step_handler(message, fio)

def fio(message):
    bot.send_message(message.chat.id,"Iltimos F.I.O ni kiriting!")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
bot.polling()