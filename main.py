from datetime import date, datetime

import model
import text
import view
import controller


controller.start()

while True:
    select = view.menu()
    match select:
        case 1: # показать все заметки
            controller.show_notes(model.notes_book)
            if model.notes_book:
                while True:
                    id = view.input_id(text.choice_note)
                    if controller.is_id_correct(id, model.notes_book):
                        controller.note_menu(id)
                    break

        case 2: #  Создать заметку
            controller.add_note()

        case 3: # Найти заметку
            result = controller.search()
            if result:
                id = view.input_id(text.choice_note)
                if controller.is_id_correct(id, result):
                    controller.note_menu(id)

        case 4: # Удаление заметок
            result = controller.search()
            if result:
                index_list = view.input_id_notes()
                for id in index_list:
                    if id in result.keys():
                        dlt_note = model.remove_note(id)
                        view.print_message(text.del_successful(dlt_note))
                    else:
                        view.print_message(text.del_unsuccessful(str(id)))

        case 5: # Удалить все заметки
            print(text.remove_all)
            if input().upper() in ("Y", "Н"):
                model.remove_all()
                view.print_message(text.remove_all_successful)
            else:
                view.print_message(text.remove_all_unsuccessful)

        case 6: # Сохранить изменения
                if model.save_file():
                    view.print_message(text.save_successful)

        case 7: # Отмена изменений
                model.open_file()

        case 8: # Выход
            view.print_message(text.exit_message)
            if input().upper() in ("Y","Н"):
                model.save_file()
                view.print_message(text.save_successful)
            else: view.print_message(text.changes_not_saved)
            break


#==============================================================



