import sqlite3
from dotenv import load_dotenv
import os
import User
import sqlalchemy as sa

load_dotenv()

engine = sa.create_engine(f"sqlite:///{str(os.getenv('DATABASE'))}")
connection = engine.connect()

metadata = sa.MetaData()

user_table = sa.Table(
    "users",
    metadata,
    sa.Column("user_id", sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column("name", sa.String, unique=True),
    sa.Column("tg_id", sa.String, unique=True),
    sa.Column(status, sa.String, nul)
)
# connection = sqlite3.connect(str(os.getenv('DATABASE')))
# cursor = connection.cursor()
# user_table_name = str(os.getenv('USERS'))
# check_table_name = str(os.getenv('CHECKTABLE'))
# command1 = f"""
# CREATE TABLE IF NOT EXISTS {user_table_name} ( user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL unique,tg_id TEXT NOT NULL unique, status text not null)
# """
# command2 = f"create table if not exists {check_table_name}(duty_id integer primary key autoincrement, date text, duty_status integer)"

# cursor.execute(command1)
# cursor.execute(command2)

# def add_new_user(user):
#     command = f"insert into {user_table_name} (name, tg_id, status) values (?,?,?)"
#     try:
#         cursor.execute(command, (user_table_name, user.name, user.tg_id, user.status))
#         connection.commit()
#     except sqlite3.IntegrityError:
#         print("Your name or id was not unique, add new name: ")
#         name = input("name: ")
#         tg_id = input("id: ")
#         cursor.execute(command, (name, tg_id, "active"))
#         connection.commit()

# def get_user_by_id(id):
#     command = f"select * from {user_table_name} where user_id = ?"
#     a = cursor.execute(command, (id,))

#     print(cursor.fetchone())
# # add_new_user(User.User("hello", "world"))
# get_user_by_id(1)