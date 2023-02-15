import file_operation
import Note
import ui

number = 6 # сколько знаков МИНИМУМ может быть в тексте заметки

def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print("Заметка добавлена")


def show():
    try:
        array = file_operation.read_file()
        for notes in array:
            print(Note.Note.map_note(notes))
            print("\n")
    except Exception:
        print('\nНет ни одной заметки...\n')


def show_date():
    date = input('Введите дату в формате dd.mm.yyyy: ')
    logic = True
    array = file_operation.read_file()
    for notes in array:
        if date in Note.Note.get_date(notes):
            print(Note.Note.map_note(notes))
            print('\n')
            logic = False
    if logic == True:
        print("Нет ни одной заметки...")


def show_id():
    try:
        array = file_operation.read_file()
        print('\n')
        for notes in array:
            print('id: ' + Note.Note.get_id(notes))
    except Exception:
        print('\nНет ни одной заметки...\n')
    id = input("Введите id необходимой заметки: ")
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            print('\n')
            print(Note.Note.map_note(notes))
            logic = False
    if logic == True:
        print("Заметки не найдено...")


def delete():
    show()
    id = input("Введите id заметки: ")
    logic = True
    array = file_operation.read_file()
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            array.remove(notes)
            print("Заметка удалена...")
            file_operation.write_file(array, 'a')
    if logic == True:
        print('Такой заметки нет. Возможно вы ввели неверный id')


def edit():
    show()
    input_from_user = input("Введите id заметки: ")
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if input_from_user == Note.Note.get_id(notes):
            note = ui.create_note(number)
            Note.Note.set_title(notes, note.get_title())
            Note.Note.set_body(notes, note.get_body())
            Note.Note.set_date(notes)
            print('Заметка изменена')
            logic = False
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')
