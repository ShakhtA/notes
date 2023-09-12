import model
import text

def open_file():
    global notes_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            notes_book = json.load(file)
        return True
    except:
        return False


def create_note() -> dict[str,str]:
    new_note = {}
    for key, value in text.create_note.items():
        new_note[key] = input(value)
    return new_note

def edit_note() -> dict[str, str]:
    new = {}
    for key, value in text.create_note.items():
        new[key] = input(value)
    return new;

def menu() -> int:
    print(text.text_menu[0])
    for i in range(1, len(text.text_menu)):
        print(f'\t{i:>2}. {text.text_menu[i]}')

    while True:
        select = (input(text.select_menu))
        if select.isdigit() and 0 < int(select) < len(text.text_menu):
            return int(select)
        else:
            print(text.input_error)

def input_id(message) -> str:
    return input(message)

def input_id_notes() -> list[str]:
    new_list = input(text.choice_notes).split(" ")
    return new_list

def print_message(message):
    print('\n'+ message)
    print_separator(message)

def print_separator(message):
    print("=" * len(message))

def search_note() -> str:
    return input(text.search_note)

def search_word(word) -> str:
    return input(word)

def show_note(id):
    print(f'\nid: {id:>03}\nHeading: {model.notes_book[id]["Heading"]}\nText: {model.notes_book[id]["Text"]}\nDate: {model.notes_book[id]["Date"]}\n')


def show_notes(notes, message):
    if notes:
        for key, value in notes.items():
            print(f'id: {key:>03}\nHeading: {value.get("Heading")}\nText: {value.get("Text")}\nDate: {value.get("Date")}\n')
    else:
        print_message(message)










