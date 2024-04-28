import sys

phonebook = {}

def add_contact(username, phone): #Додає новий контакт до телефонного довідника
    if username in phonebook:
        print(f"Контакт з ім'ям '{username}' вже існує. Введіть нову інформацію або 'exit'.")
        return
    phonebook[username] = phone
    print(f"Контакт '{username}' успішно додано.")

def change_contact(username, phone): #Змінює номер телефону для існуючого контакту
    if username not in phonebook:
        print(f"Контакт '{username}' не знайдено.")
        return
    phonebook[username] = phone
    print(f"Номер телефону для '{username}' оновлено.")

def show_phone(username): #Виводить номер телефону для контакту
    if username not in phonebook:
        print(f"Контакт '{username}' не знайдено.")
        return
    phone = phonebook[username]
    print(f"Номер телефону для '{username}': {phone}")

def show_all_contacts(): #Виводить всі контакти з номерами телефонів
    if not phonebook:
        print("Телефонний довідник порожній.")
        return
    for username, phone in phonebook.items():
        print(f"{username}: {phone}")

def parse_input(user_input): #Розбирає введений користувачем рядок на команду та її аргументи
    command, *args = user_input.strip().lower().split(' ')
    return command, *args

def validate_add_contact_input(args): #Перевіряє формат введення для команди 'add'
    if len(args) != 2:
        raise ValueError("Невірний формат команди. Спробуйте 'add username phone'.")
    username, phone = args
    if len(phone) != 10 or not phone.isdigit():
        raise ValueError("Номер телефона повинен складатися з 10 цифр.")
    return username, phone

def validate_change_contact_input(args): #Перевіряє формат введення для команди 'change'
    if len(args) != 2:
        raise ValueError("Невірний формат команди. Спробуйте 'change username phone'.")
    username, phone = args
    if len(phone) != 10 or not phone.isdigit():
        raise ValueError("Номер телефона повинен складатися з 10 цифр.")
    return username, phone

def validate_phone_contact_input(args): #Перевіряє формат введення для команди 'phone'
    if len(args) != 1:
        raise ValueError("Невірний формат команди. Спробуйте 'phone username'.")
    username = args[0]
    return username

def main():
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        try:
            if command == "hello":
                print("How can I help you?")
            elif command == "add":
                username, phone = validate_add_contact_input(args)
                add_contact(username, phone)
            elif command == "change":
                username, phone = validate_change_contact_input(args)
                change_contact(username, phone)
            elif command == "phone":
                username = validate_phone_contact_input(args)
                show_phone(username)
            elif command == "all":
                show_all_contacts()
            elif command in ["close", "exit"]:
                print("Good bye!")
                sys.exit(0)
            else:
                print("Невідома команда. Спробуйте ще раз.")
        except ValueError as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
