import os
import shutil
from pathlib import Path

menu = '''
1. Создание папки (с указанием имени);
2. Удаление папки по имени;
3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
4. Создание пустых файлов с указанием имени;
5. Запись текста в файл;
6. Просмотр содержимого текстового файла;
7. Удаление файлов по имени;
8. Копирование файлов из одной папки в другую;
9. Перемещение файлов;
10. Переименование файлов.
11. Выход из программы
'''


def create_folder(name):
    os.mkdir(name)


def delete_folder(name):
    shutil.rmtree(name, ignore_errors=True)


def move_to_folder(path, root_folder):
    while True:
        os.chdir(input("Введите имя папки, в которую хотите перейти, или путь: "))
        if root_folder in os.getcwd().split('/'):
            break
        else:
            print("Нельзя выходить из корневой папки")


def create_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write


def write_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(input("Введите текст, который хотите написать: "))


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"Файл {file_name} содержит: ")
        for line in lines:
            print(line)


def remove_file(file_name):
    os.remove(file_name)

def copy_file():
    file_name = input("Введите название файла, который хотите скопировать: ")
    dict_name = input("Укажите в какую папку хоитите скопировать или путь: ")
    shutil.copy(file_name, dict_name)



print("""
    Настройка:
    Сначала укажите папку, в которой будем работать
                """)

# /Users/kirillanpilov/PycharmProjects/file_manager/
path = input("Введите путь к папке: ")  # /Users/kirillanpilov/Downloads/
os.chdir(path)
root_folder = os.getcwd().split('/')[-1]

while True:
    print("Текущие файлы", os.listdir())
    print(menu)
    choice = int(input("Выбирите пункт в меню: "))
    if choice == 1:
        name = input("Введите имя папки: ")
        create_folder(name)
    if choice == 2:
        name = input("Введите имя папки: ")
        delete_folder(name)
    if choice == 3:
        move_to_folder(path, root_folder)

    if choice == 4:
        file_name = input("Введите название файла: ")
        create_file(file_name)

    if choice == 5:
        file_name = input("Введите название файла: ")
        write_file(file_name)

    if choice == 6:
        file_name = input("Введите название файла: ")
        read_file(file_name)

    if choice == 7:
        file_name = input("Введите название файла: ")
        remove_file(file_name)

    if choice == 8:
        copy_file()


    if choice == 9:
        pass

    if choice == 10:
        file_name = input("Введите название файла, который хотите переименовать: ")
        new_file_name = input("Введите новое название файла: ")
        os.rename(file_name, new_file_name)
    if choice == 11:
        break
