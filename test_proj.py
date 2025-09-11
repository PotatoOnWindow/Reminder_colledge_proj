# добавлять дату (заметку)
# убирать дату (заметку)
# напоминание: проверка даты, вывод в терминал

import sqlite3 as sql
from datetime import date

class db:
    def __init__(self):
        self.connect = sql.connect("data.db")
        self.date = date.today()
        self.cursor = self.connect.cursor()
        table_check = self.cursor.execute(
  """SELECT name FROM sqlite_master WHERE type='table' 
  AND name='NOTES'; """).fetchall()
        if table_check:
            print("Table NOTES exists")
        else:
            print("Table NOTES not found. Creating")
            self.cursor.execute(
  """CREATE TABLE NOTES(DESCRIPT VARCHAR(255), LASTDATE int, NEXTDATE int);""")
            print("Created")


   # def _create

start = db()

print("test")

