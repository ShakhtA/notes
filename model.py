from datetime import datetime
import text
import json

notes_book = {}
path = text.path_jason_file

def check_id() -> int:
    if notes_book:
        return max(map(int, notes_book.keys())) + 1
    else:
        return 1

def create_note(new):
    new["Date"] = date_to_string()
    notes_book[check_id()] = new

def date_to_string() -> str:
    now = datetime.now()
    return f'{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}'

def edit_note(id, new): #   Еще поработать!!!
    edit = False
    for key in new.keys():
        if new[key] != "":
            notes_book[id][key] = new[key]
            edit = True
    if edit:
        notes_book[id]["Date"] = date_to_string()
        notes_book[id] = notes_book.pop(id)
    return edit

def open_file():
    global  notes_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            notes_book = json.load(file)
        return True
    except:
        return False

def remove_all():
    notes_book.clear()

def remove_note(index) -> str:
    return notes_book.pop(index)["Heading"]

def save_file():
    try:
        with open(path, 'w', encoding= 'UTF-8') as file:
            json.dump(notes_book, file, ensure_ascii=False)
        return True
    except:
        return False

def search(str) -> dict[int:dict[str, str]]:
    tmp_dict = {}
    if str != "":
        for key, value in notes_book.items():
            if str.lower() in ' '.join(value.values()).lower():
                tmp_dict[key] = value
    else:
        return {}
    return tmp_dict

def search_date(str) -> dict[int:dict[str, str]]:
    tmp_dict = {}
    if str != "":
        for key, value in notes_book.items():
            if str.lower() in datetime\
                              .strptime(value["Date"], text.date_format)\
                              .strftime(text.date_format):
                tmp_dict[key] = value
    else:
        return {}
    return tmp_dict

def search_head(str) -> dict[int:dict[str, str]]:
    tmp_dict = {}
    if str != "":
        for key, value in notes_book.items():
            if str.lower() in value["Heading"]:
                tmp_dict[key] = value
    else:
        return {}
    return tmp_dict

def search_text(str) -> dict[int:dict[str, str]]:
    tmp_dict = {}
    if str != "":
        for key, value in notes_book.items():
            if str.lower() in value["Text"]:
                tmp_dict[key] = value
    else:
        return {}
    return tmp_dict

