'''8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать 
Update, Delete
Информация о человеке: Фамилия, Имя, Телефон, Описание
Корректность и уникальность данных не обязательны.
Функционал программы
1) телефонный справочник хранится в памяти в процессе выполнения кода.
Выберите наиболее удобную структуру данных для хранения справочника.
2) CRUD: Create, Read, Update, Delete
Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
Delete: Удаление записи из справочника. Выбор - как в Read.
3) экспорт данных в текстовый файл формата csv
4) импорт данных из текстового файла формата csv
Используйте функции для реализации значимых действий в программе
(*) Усложнение.
Сделать тесты для функций
Разделить на model-view-controller
'''

# user = ["ferstname","secondname","phone","discription"]
# phone_dir = {1:["ferstname","secondname","phone","discription"],2:["ferstname","secondname","phone","discription"]}
# key_count
def input_user()->list:
    user = []
    user.append(input("Input ferst name"))
    user.append(input("Input second name"))
    user.append(input("Input phone"))
    user.append(input("Input discription"))

    return user
print(input_user())

key_count=0
phone_dir=dict()

def create( phone_dir_local: list, idc: int, user:list, )-> dict:
    idc +=1
    phone_dir_local[idc] = user
    return phone_dir_local, idc

# user1 = ["ferstname1","secondname1","phone1","discription1"]
# user2 = ["ferstname","secondname","phone","discription"]

# 0
# print(phone_dir)

def menu():
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
            change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

menu()       

