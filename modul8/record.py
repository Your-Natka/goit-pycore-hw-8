from modul8.fields import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return f"Phone updated: {old_phone} → {new_phone}"
        raise ValueError("Old phone number not found.")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
