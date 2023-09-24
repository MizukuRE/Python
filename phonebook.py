'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной
'''

def enter_first_name():
    return input('Введите имя абонента: ').title()

def enter_second_name():
    return input('Введите фамилию абонента: ').title()

def enter_family_name():
    return input('Введите отчество абонента: ').title()

def enter_phone_number():
    return input('Введите номер телефона абонента: ')

def enter_address():
    return input('Введите адрес абонента: ').title()

def enter_data():
    first_name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{first_name} {surname} {family}\n{number}\n{address}\n\n')

def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print(file.read())

def search_data():
    print('Выберите вариант поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес\n')
    index = int(input('Введите номер варианта: ')) - 1
    searched = input('Введите данные для поиска: ').title()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for contact in data:
            contact_split = contact.replace('\n', ' ').split()
            if searched in contact_split[index]:
                print(contact, end='\n\n')

def interface():
    cmd = 0
    while cmd != '4':
        print('Выберите действие:\n'
              '1. Добавить контакт\n'
              '2. Вывести все контакты\n'
              '3. Поиск контакта\n'
              '4. Ввход\n')
        cmd = input('Введите действие: ')
        while cmd not in ('1', '2', '3', '4'):
            print('Некорректный ввод\n')
            cmd = input('Введите действие: ')
        match cmd:
            case '1': enter_data()
            case '2': print_data()
            case '3': search_data()
            case '4': print('Всего доброго\n')

interface()
