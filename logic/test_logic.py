from remind_logic import remind_logic as rmnd
from db_logic import db_interaction as db


test_db = db.db("test_db")


def add_note():
    escape = input("you can escape. If you want to, type yes: ")
    if escape in ['Y', 'y', 'Yes', 'yes']:
        return

    note_name = input("I need note name: ")
    note_desc = input("Also description: ")
    
    test_db.add_note(note_name, note_desc)


def del_note():
    escape = input("Now i can delete notes only by id.\nEscape?: ")
    if escape in "YyYesyes":
        return
    nid = input("Type id of your note: ")
    test_db.del_note_by_id(nid)


def print_notes():
    print("printing notes...")
    print(test_db.return_notes())


app_loop = True
menu_text = '''what you want? (choose from below)\n
    Add Note | Delete Note | Print all Notes | Exit | Hide menu\n
    (1, 2, 3, 4, 5): '''


while app_loop:
    print(menu_text, end='')
    temp = int(input())
    if temp == 1:
        # add note
        add_note()

    elif temp == 2:
        #del note
        del_note()

    elif temp == 3:
        # print all notes
        print_notes()

    elif temp == 4:
        # exit
        app_loop = False
        break;

    elif temp == 5:
        if menu_text[0] == 'w':
            menu_text = "type here (1, 2, 3, 4, 5): "
        else:
            menu_text = '''what you want? (choose from below)\n
    Add Note | Delete Note | Print all Notes | Exit | Hide menu\n
    (1, 2, 3, 4, 5): '''
    else:
        print("You entered something wrong.\nIf you want to escape, type 4: ")


print("Program finished")
    
