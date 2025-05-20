from utility import input_error, save_data, load_data
from modul8.address_book import AddressBook
from modul8.record import Record

@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return f"Contact {name} with phone {phone} added."

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    record.change_phone(old_phone, new_phone)
    return f"Phone number for {name} updated from {old_phone} to {new_phone}."

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    phones = ", ".join(p.value for p in record.phones)
    return f"{name}: {phones}"

@input_error
def show_all(args, book):
    if not book.records:
        return "Address book is empty."
    result = []
    for record in book.all_records():
        phones = ", ".join(p.value for p in record.phones)
        birthday = record.birthday if record.birthday else "No birthday"
        result.append(f"{record.name.value}: {phones} | Birthday: {birthday}")
    return "\n".join(result)

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    record.add_birthday(birthday)
    return f"Birthday {birthday} added for {name}."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    return f"{name}'s birthday: {record.birthday}"

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays this week."
    result = []
    for entry in upcoming:
        result.append(f"{entry['name']} - {entry['birthday']}")
    return "\n".join(result)

def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    return command, parts[1:]

def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            save_data(book)
            print("Good bye! Your data has been saved.")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in commands:
            print(commands[command](args, book))
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()