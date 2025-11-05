import sqlite3 as sql
import datetime as dtm
from datetime import date

class db():
    def __init__(self):
        self.table_name = "NOTES"
        self.connect = sql.connect("data.db")
        self.date = date.today()
        # self.time = dtm.datetime.now()
        self.cursor = self.connect.cursor()

        table_check = self.cursor.execute( 
   f"""SELECT name FROM sqlite_master WHERE type='table'  
   AND name='{self.table_name}'; """).fetchall() 
  
        if table_check: 
             print(f"Table {self.table_name} exists") 
        else: 
             print(f"Table {self.table_name} not found. Creating") 
             self.cursor.execute( 
                     f"""CREATE TABLE {self.table_name}(DESCRIPTION, ADDDATE, REMINDCOUNT)""") 
             print("Created")


    def add_note(self, note, description):
        desc = description
        today_date = self.date
        cur = self.cursor
        remind_count = 0

        ins_statement = f'''INSERT INTO {self.table_name}(DESCRIPTION, ADDDATE, REMINDCOUNT)
            VALUES(?, ?, ?) '''
        cur.execute(ins_statement, (desc, today_date, remind_count))
        self.connect.commit()

        print("added succesfully")
                

    def del_note_by_id(self, id):
        cur = self.cursor
        delete_query = f"DELETE FROM {self.table_name} WHERE ROWID = ?"
        
        cur.execute(delete_query, (id,))
        self.connect.commit()
        print("deleted succesfully")


    def return_notes(self):
        cur = self.cursor
        cur.execute(f"SELECT * FROM {self.table_name}")
        rows = cur.fetchall()
        self.connect.commit()

        return rows


