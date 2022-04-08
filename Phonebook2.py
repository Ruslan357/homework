def show_dict():
    import os
    file = open('dict.txt','r')
    dict_temp = {}
    for line in file:
        key, *value = line.split()
        dict_temp[key] = value
    file.close()
    print(dict_temp)


def add_to_dict(): 
    import os
    dict_temp = {}
    file = open('dict.txt', 'a+') 

    number = input('\nВведіть номер телефону абонента\n')
    name = input("\nВведіть призвище ім'я по батькові\n")
    street = input("\nВведіть назву вулиці\n") 
    house = input("\nВведіть номер будинку\n")
    apartment = input("\nВведіть номер квартири\n")
    str_temp = name +' '+ street+' '+house+' '+apartment
    
    dict_temp[number] = str_temp
    for k,v in dict_temp.items():
        file.write(str(k)+' '+str(v)+'\n')  
    file.close()


def update_dict():
    import os
    file = open('dict.txt','w+')
    dict_temp = {}
    for line in file:
        key, *value = line.split()
        dict_temp[key] = value
    file.close()
    
    number = input('\nВведіть номер телефону абонента, який потрібно редагувати\n')
    name = input("\nВведіть призвище ім'я по батькові\n")
    street = input("\nВведіть назву вулиці\n") 
    house = input("\nВведіть номер будинку\n")
    apartment = input("\nВведіть номер квартири\n")
    str_temp = name +' '+ street+' '+house+' '+apartment

    update = {}
    update[number] = str_temp
    dict_temp.update(update)
    for k,v in dict_temp.items():
        file.write(str(k)+' '+str(v)+'\n')  
    file.close()