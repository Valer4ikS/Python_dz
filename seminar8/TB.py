# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Открыть файл
# Сохранить файл
# Показать телефонную книгу
# Добавить контакт
# Изменить контакт
# Удалить контакт
# Выход

path = 'phonebook.txt'

def create_open_file():
    data = open(path, 'a', encoding='UTF-8')
    data.close

create_open_file()
    
def add_contact():
    with open('phonebook.txt', 'r+', encoding= 'UTF-8') as data:
        new_contact = str(input("Введи новый контакт: "))
        new_contact = new_contact + '\n'
        data.writelines(new_contact)
    return 'Контакт добавлен'

def clear_all():
    with open('phonebook.txt', 'r+', encoding= 'UTF-8') as data:
        data.write('')
            
def find_contact():
    with open('phonebook.txt', 'r+', encoding= 'UTF-8') as file1:
        data_list = []
        for line in file1:
            data_list.append(line.strip())
        print(data_list)
        for i in data_list:
            res = i.split()
            name = str(input('Найти контакт: '))
            if res[0] == name:
                print(i)
                return i

def delete(contacts):
    print("Введите контакт: ")
    name = input('> ')
    for contact in contacts:
        if contact['name'] == name:
            print("Вы хотите удалить контакт %s (yes/no)?: " % name )
            name_del = input('> ')
            if name_del == 'yes':
               contacts.remove(contact)
               print("Вы удалили контакт %s " % name)
            

def main_menu():
    print('1 - добавить контакт')
    print('2 - закрыть книгу')
    print('3 - очистить книгу')
    print('4 - найти контакт')
    # print('5 - изменить контакт')
    # print('6 - удалить контакт')
    while True:
        menu = int(input('Действие: '))
        
        if menu == 1:
            print(add_contact())
        elif menu == 2:
            break
        elif menu == 3:
            clear_all()
        elif menu == 4:
            find_contact()
        # elif menu == 5:
            
            
main_menu()

with open('phonebook.txt', 'r+', encoding= 'UTF-8') as data:
    res = data.read()
    print(res)
        
            
    



# def add_into_file():
#     data = open(path, 'a', encoding='UTF-8')
#     name = input("Введите имя: ").capitalize()
#     surname = input("Введите фамилию: ").capitalize()
#     mid_name = input("Введите отчество: ").capitalize()
#     phone = input("Введите норме телефона: ")
#     data.write(f"{name} {mid_name} {surname} {phone}")
#     data.close()
    
# def reading_file():
#     data = open(path, 'r', encoding='UTF-8')
#     print(data.read())
#     print(data.readlines())
#     data.close()
    
# def find_contact_file():
#     data = open(path, 'r', encoding='UTF-8')
#     find_contact = input('Введите искомый параметр: ')
#     in_find_text = data.readlines()
#     dict_cont = {}
#     for i, j in enumerate(in_find_text, 1):
#         j = j.strip()
#         dict_cont = {'name': in_find_text[0], 'mid_name': in_find_text[1], 'surname': in_find_text[2], 'phone': in_find_text[3]}
#     for i in in_find_text:
#         if i == find_contact:
#             print('123')