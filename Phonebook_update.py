import os
import json


def сreate_new_dict(): 
    dict_temp = {}
    number = check_number()
    dict2_temp = data_input()

    dict_temp[number] = dict2_temp

    with open('Dict.json', 'w+') as file:
        file.write(json.dumps(dict_temp))


def show_dict():
    with open('Dict.json', 'r') as file:
        dict_temp = json.loads(str(file.read()))
        
    for i in dict_temp.keys():
        print('number : ',i)
        for j in dict_temp[i]:
            print(j,":",dict_temp[i][j])
        print("\n")


def update_dict():
    update = {}
    with open('Dict.json', 'r') as file:
        dict_temp = json.loads(str(file.read()))
        number = check_number()
        dict2_temp = data_input() 
        update[number] = dict2_temp
        dict_temp.update(update)

    with open('Dict.json', 'w+') as file:
        file.write(json.dumps(dict_temp))


def delete_number():
    with open('Dict.json', 'r') as file:
        dict_temp = json.loads(str(file.read()))
        number = check_number()
        del dict_temp[number]
    with open('Dict.json', 'w+') as file:
        file.write(json.dumps(dict_temp))


def check_number():
    while True:
        number = input('\nВведіть номер телефону абонента\n')
        if len(number)!=10:
            print('Введіть коректний номер телефону (напр. 0997772558)')
        else: 
            return number


def data_input():
    temp = {}
    temp['name'] = input("\nВведіть призвище ім'я по батькові\n")
    temp['street'] = input("\nВведіть назву вулиці\n") 
    temp['house'] = input("\nВведіть номер будинку\n")
    temp['apartment'] = input("\nВведіть номер квартири\n")
    return temp


def main_def(): 
    run_programm = True
    while run_programm:
        print('Выберіть варіант:\n1 Створити новий телефонний словник\n'
        '2.Додати новий контакт\n3.Видалити контакт\n4.Показати телефонний словник\n'
        '5.Вихід\n\n')
        my_choice = input()
        if my_choice == '1':
            сreate_new_dict()
        elif my_choice == '2':
            update_dict()
        elif my_choice == '3':
            delete_number()
        elif my_choice == '4':
            show_dict()
        elif my_choice == '5': 
            run_programm = False
        else:
            print('Невірний вібір')



main_def()