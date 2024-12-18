def parse_input(user_input):
    """Парсимо введення"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    """Додаємо новий контакт."""
    if len(args) != 2:
        return "Invalid format. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    """Змінюємо номер телефону для існуючого контакту."""
    if len(args) != 2:
        return "Invalid format. Use: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    return f"Contact {name} not found."

def show_phone(args, contacts):
    """Показуємо номер телефону за ім'ям."""
    if len(args) != 1:
        return "Invalid format. Use: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Contact {name} not found."

def show_all(contacts):
    """Виводимо всі збережені контакти."""
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
