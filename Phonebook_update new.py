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
        print(dict_temp)
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

show_dict()