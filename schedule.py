import connection
import User

def create_new_schedule():
    a = connection.get_users_from_db_as_list()
    