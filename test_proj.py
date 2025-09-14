# добавлять дату (заметку)
# убирать дату (заметку)
# напоминание: проверка даты, вывод в терминал

import sqlite3 as sql
import datetime as dtm
from datetime import date

class db:
    def __init__(self):
        self.connect = sql.connect("data.db")
        self.date = date.today()
        self.time = dtm.datetime.now()
        self.cursor = self.connect.cursor()

        table_check = self.cursor.execute(
  """SELECT name FROM sqlite_master WHERE type='table' 
  AND name='NOTES'; """).fetchall()

        if table_check:
            print("Table NOTES exists")
        else:
            print("Table NOTES not found. Creating")
            self.cursor.execute(
                    """CREATE TABLE NOTES(DESCRIPT VARCHAR(255), STARTDATE VARCHAR(255), NEXTDATE VARCHAR(255), ADDTIME VARCHAR(255)), REMCOUNT int;""")
            print("Created")

    # adds description, today date, nest date (for remind), next time (also for rm), remind count, to database
    def add_note(self):
        today = self.date
        nowT = self.time
        nxt_date = today + timedelta(days = 1)
        cur = self.cursor
        remCount = 0

        descr = input("type description: ")

        ins_statement = '''INSERT INTO NOTES(DESCRIPT, FIRSTDATE, NEXTDATE, ADDTIME, REMCOUNT)
             VALUES(descr, today, nxt_date, nowT, remCount) '''
        cur.execute(ins_statement, NOTES)



    def del_note(self):
        cur = self.cursor


    def print_notes(self):
        cur = self.cursor
        results = cur.fetchall()
        print(results)


    def remind(self): # remind after 2m - 10m - 1h - 5h - 1d - 5d - 25d - 4m - 2y
        cur = self.cursor
        date = self.date
        # check matching dates in base and today
        # print note on matching date


    def start_work(self):
        pass


    def stop_work(self):
        conn = self.connect
        conn.commit()
        print("stop working")


start = db()

#print("test")

start.print_notes()

