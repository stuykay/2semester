import os

PATH = 'notes/{}.txt'
MENU = '''1. Добавить заметку
2. Вывести список заметок
3. Вывести заметку
4. Удалить заметку
5. Удалить все заметки
6. Выход
'''

class NotesManager:
    def __init__(self):
        if not os.path.exists('notes/'):
            os.mkdir('notes/')

    def file_exists(self, title):
        return os.path.exists(PATH.format(title))

    def add_note(self, title, text):
        with open(PATH.format(title), 'w') as file:
            file.writelines(text)

    def list_notes(self):
        print(os.listdir('notes/'))

    def read_note(self, title):
        if self.file_exists(title):
            with open(f'{title}.txt', 'r') as file:
                print(file.readlines())

    def delete_note(self, title):
        if self.file_exists(title):
            os.remove(PATH.format(title))
        else:
            print('Файла итак нет')

    def clear_notes(self):
        for file in os.listdir('notes/'):
            if file.endswith('.txt'):
                os.remove(f'notes/{file}')
        print('Заметки удалены')

nm = NotesManager()

while True:
    print(MENU)
    inp = input('ВЫБЕРИТЕ ДЕЙСТВИЕ: ')
    if inp=='1': 
        nm.add_note(input('Введите название вашей заметки: '), input('Введите текст вашей заметки: '))
    elif inp=='2':
        nm.list_notes()
    elif inp=='3':
        nm.read_note(input('Введите название вашей заметки: '))
    elif inp=='4':
        nm.delete_note(input('Введите название вашей заметки: '))
    elif inp=='5':
        nm.clear_notes()
    elif inp=='6':
        break
    else: print('Вы ввели неправильную комманду')