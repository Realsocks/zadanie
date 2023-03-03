import os


def Sorting(path):
    list_files = []
    with os.scandir(path) as files:
        for i in files:
            list_files.append(i.name)
    print('Выберите вид сортировки:')
    print('1. В алфавитном порядке;')
    print('2. В обратном алфавитном порядке.')
    a = int(input())
    if (a == 1):
        for file in sorted(list_files, reverse=False):
            print(file)
    elif (a == 2):
        for file in sorted(list_files, reverse=True):
            print(file)
    else:
        print('Неверный ввод.')


def CreateFile(path):
    print('Введите название файла, который нужно создать:')
    file_name = input()
    new_path = path + "/" + file_name
    if (os.path.exists(new_path)):
        print('Данный файл уже существует')
    else:
        open(new_path, "w")
        print('Файл создан')

def CheckUnique(path):
    list_files = []
    with os.scandir(path) as files:
        for i in files:
            i = path + "/" + i.name
            list_files.append(i)
    files_hash = {}
    for j in list_files:
        opened_file = open(j, 'r')
        hash_cod = hash(opened_file.read())
        if hash_cod in files_hash.values():
            print("Файл : " + j + " удалён.")
            opened_file.close()
            os.remove(j)
        elif hash_cod not in files_hash.values():
            files_hash[j] = hash_cod

def WriteFile(path):
    print('Введите название файла:')
    file_name = input()
    new_path = path + "/" + file_name #
    print('Введите, что нужно записать:')
    text = input()
    with open(new_path, "a") as file:
        file.write("\n" + text)

def CheckFile(path):
    print('Введите название файла:')
    file_name = input()
    new_path = path + "/" + file_name
    if (os.path.exists(new_path)):
        with open(new_path, "r") as file:
            line = file.readline()
            while line:
                print(line, end="")
                line = file.readline()
            print()
    else:
        print('Файла не существует')


def DeleteFile(path):
    print('Введите название файла:')
    file_name = input()
    new_path = path + "/" + file_name
    if (os.path.exists(new_path)):
        os.remove(new_path)
        print('Файл удален')
    else:
        print('Файл не существует')


print('Введите путь:')
path = input()
if (os.path.exists(path)):
        print("\nФайлы в папке:")
        with os.scandir(path) as files:
            for i in files:
                print(i.name)
            print()
        print('Выберите желаемую опцию: ')
        print('1. Проверка на уникальность;')
        print('2. Сортировка файлов;')
        print('3. Добавить новый файл;')
        print('4. Дополнить текст в файле;')
        print('5. Просмотр содержимого файла;')
        print('6. Удалить файл;')
        a = int(input())
        if (a == 1):
            CheckUnique(path)
        elif (a == 2):
            Sorting(path)
        elif (a == 3):
            CreateFile(path)
        elif (a == 4):
            WriteFile(path)
        elif (a == 5):
            CheckFile(path)
        elif (a == 6):
            DeleteFile(path)
else:
    print('Путь не найден.')