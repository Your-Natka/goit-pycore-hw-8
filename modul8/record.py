from modul8.fields import Name, Phone, Birthday

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        for idx, ph in enumerate(self.phones):
            if ph.value == old_phone.value:
                self.phones[idx] = new_phone
                return
        raise ValueError("Old phone number not found.")

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

