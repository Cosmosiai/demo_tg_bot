import sqlite3
from dotenv import load_dotenv
import os
import User
import sqlalchemy as sa

load_dotenv()

db = str(os.getenv('DATABASE'))
user_table_name = str(os.getenv('USERS'))
check_table_name = str(os.getenv('CHECKTABLE'))


def init_db():
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command1 = f"""CREATE TABLE IF NOT EXISTS {user_table_name} ( user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL unique,tg_id TEXT NOT NULL unique, status text not null)"""
        command2 = f"create table if not exists {check_table_name}(duty_id integer primary key autoincrement, date text, duty_status integer)"
        cursor.execute(command1)
        cursor.execute(command2)
        conn.commit()

def add_new_user(user):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"insert into {user_table_name} (name, tg_id, status) values (?,?,?)"
        cursor.execute(command, (user.name, user.tg_id, user.status))
        conn.commit()

def get_user_by_id(id):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        command = f"select * from {user_table_name} where user_id = ?"
        a = cursor.execute(command, (id,))
        print(cursor.fetchone())
        conn.commit()

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
