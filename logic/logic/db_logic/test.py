from db_interaction import db

newDB = db()
newDB.add_note("newNote", "just testing")
print(newDB.return_notes())
newDB.del_note_by_id(1)


