from modul8.address_book import AddressBook
from modul8.record import Record
from utils.utility import input_error
from datetime import datetime, timedelta

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Error: You must provide a name and phone number."
    name, phone = args[0], args[1]
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return f"Contact {name} added/updated."

def main():
    book = AddressBook()
    commands = {
        "add": add_contact,
        # ... інші команди
    }
    while True:
        user_input = input("Enter a command: ")
        command, args = user_input.split(" ", 1) if " " in user_input else (user_input, [])
        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command in commands:
            print(commands[command](args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
