import sqlite3 as sql
import datetime as dtm
from datetime import date

class db():
    def __init__(self):
        self.connect = sql.connect("data.db")
        self.date = date.today()
        self.time = dtm.datetime.now()
        self.cursor = self.connect.cursor()



    def add_note(self, note):
        pass


    def del_note(self, id):
        pass


    def return_notes(self):
        pass