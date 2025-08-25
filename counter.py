from datetime import date 
from datetime import datetime
import schedule
import sqlite3

def time_to_clean():
    print( "Time to clean appartments")

schedule.every().friday.at('09:00').do(time_to_clean())
