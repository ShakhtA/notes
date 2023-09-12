from datetime import date, datetime
import model
import text
import view

def start():

    while True:
        if model.open_file():
            if model.notes_book:
                view.print_message(text.load_successful)
            else:
                view.print_message(text.empty_notes)
            break
        else:
            view.print_message(text.load_unsuccessful)

def show_notes(notes_book):
    view.print_message(text.notes_book)
    view.show_notes(notes_book, text.empty_notes)
    return model.notes_book

def add_note():
    new_note = view.create_note()
    model.create_note(new_note)
    view.print_message(text.create_successful(new_note["Heading"]))

#   Поиск по всем категориям
def search() -> dict[int:dict[str, str]]:
    select_search = view.search_note()
    match select_search:
        case "1":
            print("Поиск по заголовкам")
            return search_note_head()
            # return result
            # word = view.search_word(text.search_word)
            # result = model.search_head(word)
            # if result:
            #     view.print_message(text.number_of_notes(len(result), word))
            #     view.show_notes(result, text.empty_search(word))
            # else:
            #     view.show_notes(result, text.empty_search(word))
        case "2":
            print("Поиск по тексту")
            return search_note_text()
            # return result
        #     word = view.search_word(text.search_word)
        #     result = model.search_text(word)
        #     if result:
        #         view.print_message(text.number_of_notes(len(result), word))
        #         view.show_notes(result, text.empty_search(word))
        #     else:
        #         view.show_notes(result, text.empty_search(word))
        #
        # case "3":
        #     print("Поиск по дате")
        #     word = view.search_word(text.search_date)
        #     result = model.search_date(word)
        #     if result:
        #         view.print_message(text.number_of_notes(len(result), word))
        #         view.show_notes(result, text.empty_search(word))
        #     else:
        #         view.show_notes(result, text.empty_search(word))
        case "3":
            print("Поиск по дате")
            return search_note_date()
            # return result
        case "4":
            print("Поиск по всем полям")
            return search_note()

        case "5":
            return show_notes(model.notes_book)
            # return result

def is_id_correct(id, notes_book):
    if id in notes_book.keys():
        return id
    else:
        if id:
            view.print_message(text.error_input_id)
        return False

def edit_note(id):
    view.print_message(text.prompt_edit)
    new = view.edit_note()
    if model.edit_note(id, new):
        view.print_message(text.changed_note_successful)
    else:
        view.print_message(text.note_not_changed)

def remove_note(id):
    print(text.confirm_del(model.notes_book[id]["Heading"]))
    if input().upper() in ("Y", "Н"):
        dlt_note = model.remove_note(str(id))
        view.print_message(text.del_successful(dlt_note))
    else:
        view.print_message(text.del_unsuccessful(model.notes_book[id]["Heading"]))

def show_note(id):
    view.show_note(id)

def note_menu(id):
    operation = view.input_id(text.choice_operation)
    match operation:
        case "1":
            edit_note(id)

        case "2":
            remove_note(id)

        case "3":
            show_note(id)

def search_note_head() -> dict[int:dict[str, str]]:
    word = view.search_word(text.search_word)
    result = model.search_head(word)
    if result:
        view.print_message(text.number_of_notes(len(result), word))
        view.show_notes(result, text.empty_search(word))
    else:
        view.show_notes(result, text.empty_search(word))
    return result

def search_note_text() -> dict[int:dict[str, str]]:
    word = view.search_word(text.search_word)
    result = model.search_text(word)
    if result:
        view.print_message(text.number_of_notes(len(result), word))
        view.show_notes(result, text.empty_search(word))
    else:
        view.show_notes(result, text.empty_search(word))
    return result

def search_note_date() -> dict[int:dict[str, str]]:
    word = view.search_word(text.search_date)
    result = model.search_date(word)
    if result:
        view.print_message(text.number_of_notes(len(result), word))
        view.show_notes(result, text.empty_search(word))
    else:
        view.show_notes(result, text.empty_search(word))
    return result

def search_note() -> dict[int:dict[str, str]]:
    word = view.search_word(text.search_word)
    result = model.search(word)
    if result:
        view.print_message(text.number_of_notes(len(result), word))
        view.show_notes(result, text.empty_search(word))
    else:
        view.show_notes(result, text.empty_search(word))
    return result