from modul8.address_book import AddressBook
from modul8.record import Record
from utility import input_error
from storage import save_data, load_data
from datetime import datetime, timedelta

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message

@input_error
def show_all(_, book: AddressBook):
    if not book.records:  # Перевіряємо, чи є контакти в книзі
        return "No contacts in the address book."
    
    result = []  # Збираємо інформацію про всі контакти
    for record in book.records.values():  # Використовуємо self.records, а не self.data
        phones = ", ".join(phone.value for phone in record.phones)
        birthday = str(record.birthday) if record.birthday else "No birthday"
        result.append(f"{record.name.value}: Phones: {phones}, Birthday: {birthday}")
    
    return "\n".join(result)

@input_error
def show_phone(args, book: AddressBook):
    if len(args) < 1:
        return "Error: You must provide a contact name."

    name = args[0]

    # Знаходимо контакт
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."

    # Отримуємо телефони
    phones = ", ".join(phone.value for phone in record.phones)
    return f"{name}: Phones: {phones}" if phones else f"{name} has no phones."

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Error: You must provide a contact name and birthday (DD.MM.YYYY)."

    name, birthday = args[0], args[1]

    # Перевіряємо, чи знайдено запис
    record = book.find(name)
    if not record:
        return f"Error: Contact {name} not found."

    # Перетворення рядка на datetime
    try:
        birthday_date = datetime.strptime(birthday, "%d.%m.%Y")
        birthday_str = birthday_date.strftime("%d.%m.%Y")  # Перетворення на рядок в потрібному форматі
        record.add_birthday(birthday_str)  # Додаємо як рядок
        return f"Birthday added for {name}."
    except ValueError:
        return "Error: Invalid birthday format. Use DD.MM.YYYY."
    
@input_error
def show_birthday(args, book: AddressBook):
    if not args:
        return "Error: No name provided."

    name = args[0]
    record = book.find(name)

    if not record or not record.birthday:
        return f"Birthday not found for {name}."

    # Показуємо лише дату народження контакту
    return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y')}."

@input_error
def birthdays(_, book: AddressBook):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    result = []

    for record in book.records.values():
        if record.birthday:
            # Отримуємо дату народження для поточного року
            birthday_this_year = record.birthday.value
            day, month, year = birthday_this_year.day, birthday_this_year.month, birthday_this_year.year

            # Переносимо на понеділок, якщо день народження випадає на вихідні
            birthday_this_year = datetime(year=today.year, month=month, day=day).date()

            if birthday_this_year.weekday() == 5:  # Субота
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя
                birthday_this_year += timedelta(days=1)

            # Перевіряємо, чи день народження в межах наступного тижня
            if today <= birthday_this_year <= next_week:
                result.append(f"{record.name.value} - {birthday_this_year.strftime('%d.%m.%Y')}")

    return "\n".join(result) if result else "No birthdays in the next week."

def parse_input(user_input):
    parts = user_input.strip().split(" ", 1)
    command = parts[0]
    args = parts[1].split(" ") if len(parts) > 1 else []
    return command, args

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args

    # Знаходимо контакт
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."

    # Шукаємо старий телефон
    for phone in record.phones:
        if phone.value == old_phone:
            phone.value = new_phone  # Змінюємо телефон
            return f"Phone number for {name} updated from {old_phone} to {new_phone}."
    
    return f"Phone number {old_phone} not found for contact {name}."

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    
    commands = {
        "add": add_contact,
        "change": change_contact,
        "all": show_all,
        "phone": show_phone,
        "add-birthday": add_birthday,  
        "show-birthday": show_birthday,
        "birthdays": birthdays,
    }
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break 
        elif command == "hello":
            print("How can I help you?")
        elif command in commands:
            print(commands[command](args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()