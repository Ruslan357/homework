import os
import json
from unicodedata import name

class Phonebook:
    dict = None

    def __init__(self, dict = {}):
        self.dict = dict

    def сreate_new_dict(self):
        number = input('\nВведіть номер телефону абонента\n')
        dict2_temp = self.data_input()
        self.dict[number] = dict2_temp
        with open('Dict.json', 'w+') as file:
            file.write(json.dumps(self.dict))


    def show_dict(self):
        with open('Dict.json', 'r') as file:
            self.dict = json.loads(str(file.read()))
        
        for i in self.dict.keys():
            print('number : ',i)
            for j in self.dict[i]:
                print(j,":",self.dict[i][j])
            print("\n")

    def update_dict(self):
        update = {}
        with open('Dict.json', 'r') as file:
            self.dict = json.loads(str(file.read()))
            number = input('\nВведіть номер телефону абонента\n')
            dict2_temp = self.data_input() 
            update[number] = dict2_temp
            self.dict.update(update)

        with open('Dict.json', 'w+') as file:
            file.write(json.dumps(self.dict))


    def delete_number(self):
        with open('Dict.json', 'r') as file:
            self.dict = json.loads(str(file.read()))
            number = input('\nВведіть номер телефону абонента\n')
            del self.dict[number]
        with open('Dict.json', 'w+') as file:
            file.write(json.dumps(self.dict))


    def data_input(self):
        temp = {}
        temp['name'] = input("\nВведіть призвище ім'я по батькові\n")
        temp['street'] = input("\nВведіть назву вулиці\n") 
        temp['house'] = input("\nВведіть номер будинку\n")
        temp['apartment'] = input("\nВведіть номер квартири\n")
        return temp


    def main_def(self): 
        run_programm = True
        while run_programm:
            print('Выберіть варіант:\n1 Створити новий телефонний словник\n'
            '2.Додати новий контакт\n3.Видалити контакт\n4.Показати телефонний словник\n'
            '5.Вихід\n\n')
            my_choice = input()
            if my_choice == '1':
                self.сreate_new_dict()
            elif my_choice == '2':
                self.update_dict()
            elif my_choice == '3':
                self.delete_number()
            elif my_choice == '4':
                self.show_dict()
            elif my_choice == '5': 
                run_programm = False
            else:
                print('Невірний вібір')


my_phonebook = Phonebook()
my_phonebook.main_def()