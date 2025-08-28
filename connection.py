import sqlite3
from dotenv import load_dotenv
import os

import User

load_dotenv()

db = str(os.getenv('DATABASE'))
user_table_name = str(os.getenv('USERS'))
check_table_name = str(os.getenv('CHECKTABLE'))
rooms_table_name = str(os.getenv('ROOMS'))
password_checker = str(os.getenv("ADMIN_PASSWORD"))

# DB start
def init_db():
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command1 = f"""CREATE TABLE IF NOT EXISTS {user_table_name} ( user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL unique,tg_id TEXT NOT NULL unique, status text not null, role text not null)"""
        command2 = f"create table if not exists {check_table_name}(duty_id integer primary key autoincrement, date text, duty_status integer)"
        command3 = f"""CREATE TABLE IF NOT EXISTS {rooms_table_name} ( room_id INTEGER PRIMARY KEY AUTOINCREMENT, room TEXT NOT NULL unique, status text not null)"""
        cursor.execute(command1)
        cursor.execute(command2)
        cursor.execute(command3)
        conn.commit()

# User
def add_new_user(user):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"insert into {user_table_name} (name, tg_id, status, role) values (?,?,?,?)"
        cursor.execute(command, (user.name, user.tg_id, user.status, user.role))
        conn.commit()

def first_admin_adding(tg_id, password):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command0 = f"SELECT * FROM {user_table_name} WHERE role = 'admin'"
        if cursor.execute(command0).fetchone() is None and password == password_checker:
            command = f"UPDATE {user_table_name} SET role = 'admin' WHERE tg_id = ?"
            cursor.execute(command, (tg_id,))
            conn.commit()
            return True
        else:
            return False    

def get_user_by_id(id):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"select * from {user_table_name} where user_id = ?"
        a = cursor.execute(command, (id,))
        conn.commit()
        return a

def get_user_by_tg_id(id):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"select * from {user_table_name} where tg_id = ?"
        a = cursor.execute(command, (id,)).fetchone()
        return a

def update_user_status(tg_id, status):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"update {user_table_name} set status = ? where tg_id = ?"
        cursor.execute(command, (status,tg_id,))
        conn.commit()
        return "Status updated"

def hard_user_delete(tg_id):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"delete from {user_table_name} where tg_id = ?"
        a = cursor.execute(command, (tg_id,))
        conn.commit()
        return "You was deleted from database"

def get_users_from_db_as_list():
    users=[]
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"select * from {user_table_name} where status = ?"
        a = cursor.execute(command,("active",)).fetchall()
        for i in a:
            users.append(User.User_DTO(i[1]))
        print(users)

# Rooms
def add_new_room(room):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"insert into {rooms_table_name} (room, status) values (?,?)"
        cursor.execute(command, (room.room, room.status))
        conn.commit()
        return "room "+room.room+" was added"

def update_room_status(room,status):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"update {rooms_table_name} set status = ? where room = ?"
        cursor.execute(command, (room,status))
        conn.commit()
        return "Room status updated"