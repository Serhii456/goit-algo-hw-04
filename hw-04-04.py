import sys

phonebook = {}


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
        command, *args = user_input.strip().lower().split(' ')

        try:
            if command == "hello":
                print("How can I help you?")
            elif command == "add":
                username, phone = validate_add_contact_input(args)
                if username in phonebook:
                    print(f"Контакт з ім'ям '{username}' вже існує. Введіть нову інформацію або 'exit'.")
                    return
                phonebook[username] = phone
                print(f"Контакт '{username}' успішно додано.")
            elif command == "change":
                if username not in phonebook:
                    print(f"Контакт '{username}' не знайдено.")
                    return
                username, phone = validate_change_contact_input(args)
                phonebook[username] = phone
                print(f"Номер телефону для '{username}' оновлено.")
            elif command == "phone":
                if username not in phonebook:
                    print(f"Контакт '{username}' не знайдено.")
                    return
                username = validate_phone_contact_input(args)
                phone = phonebook[username]
                print(f"Номер телефону для '{username}': {phone}")
            elif command == "all":
                for username, phone in phonebook.items():
                    print(f"{username}: {phone}")
            elif command in ["close", "exit"]:
                print("Good bye!")
                sys.exit(0)
            else:
                print("Невідома команда. Спробуйте ще раз.")
        except ValueError as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
