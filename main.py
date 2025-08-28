import telebot
from telebot import types
from dotenv import load_dotenv
import os

import connection
import User
import Room
import status

# Functional code
load_dotenv()
connection.init_db()
bot = telebot.TeleBot(os.getenv('TOKEN'))
user_states = {}

def create_menu_keyboard(message, options, text, next_handler):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton(option) for option in options]
    markup.add(*buttons, row_width=2)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    bot.register_next_step_handler(message, next_handler)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Thanks, for using CleanerBot. I collect your tg_id for messeging to you. With me you can sing up in schedule of the room.")
    user_check_menu(message)
    
@bot.message_handler(func=lambda message: message.text == "Register")
def adding_to_schedule(message):
    bot.send_message(message.chat.id, "You will be added into schedule, message come every friday")

@bot.message_handler(commands=['restart'])
def restart(message):
    create_menu_keyboard(message,{"/start"},"Chat restarted",start)
    
def user_check_menu(message):
    user_id = str(message.from_user.id)
    if user_check(user_id):
        main_menu1(message)
    else:
        create_menu_keyboard(message,{"yes","no"},"Do you want registrate?",registration_yesno_handler)

def user_check(tg_id):
    if (connection.get_user_by_tg_id(tg_id) is None):return False
    else: return True

def registration_yesno_handler(message):
    match message.text:
        case "yes":
            register_s1(message)
        case "no":
            unregistered_user_menu(message)
        case _: main_menu1(message)

def register_s1(message):
    bot.send_message(message.chat.id, "What is your name? Write name with your keyboard",reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message,register_s2)


def register_s2(message):
    connection.add_new_user(User.User(message.text, str(message.from_user.id)))
    bot.send_message(message.chat.id,"You are registered")
    main_menu1(message)
        
def register_blank(message):
    bot.send_message(message.chat.id, "What is your name? Write name with your keyboard",reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message,register_s2)

def set_user_status(message, status_value):
    bot.send_message(message.chat.id, connection.update_user_status(message.from_user.id, status_value))

def main_menu1(message):
    create_menu_keyboard(message, {"Schedule","Account", "Room management"},"Main menu", main_menu2)

def unregistered_user_menu(message):
    create_menu_keyboard(message,{"Registration"},"Unregistered user, goodbye",register_blank)

def main_menu2(message):
    match message.text:
        case "Schedule":
            create_menu_keyboard(message, {"Add me into schedule","Pausa for me", "What should I do this time"},"Choose option", status_handler)
        case "Account":
            create_menu_keyboard(message, {"Change status", "Delete me from database", "Become an Admin"},"Account menu", account_menu)
        case "Room management":
            bot.register_next_step_handler(message,admin_adding_new_room)
        case _: main_menu1(message)

def account_menu(message):
    match message.text:
        case "Change status":
            create_menu_keyboard(message,{"Activate me", "Deactivate me"},"Changing process", status_handler)
        case "Delete me from database":
            delete_handler(message)
        case "Become an Admin":
            admin_handler(message)
        case _: main_menu1(message)
        

def status_handler(message):
    match message.text:
        case "Activate me":
            set_user_status(message, status.user_status.active)
            user_check_menu(message)
        case "Deactivate me":
            set_user_status(message, status.user_status.deactivated)
            user_check_menu(message)
        case _: main_menu1(message)


def delete_handler(message):
    bot.send_message(message.chat.id,connection.hard_user_delete(message.from_user.id))
    restart(message)

def admin_handler(message):
    bot.send_message(message.chat.id, "Write an password please",reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, admin_adding)

def admin_adding(message):
    answer = connection.first_admin_adding(str(message.from_user.id),message.text)
    bot.send_message(message.chat.id,answer)

# def admin_adding_by_admin(message):

def admin_adding_new_room(message):
    r = Room.Room(message.text)
    a = connection.add_new_room(r)
    bot.send_message(message.chat.id, a)
    restart(message)



bot.polling(none_stop=True, interval=0)


