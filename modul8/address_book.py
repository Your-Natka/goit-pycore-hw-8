import pickle
from datetime import datetime, timedelta
from collections import UserDict
from modul8.record import Record
from utils.utility import input_error

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.records = {}

    def add_record(self, record):
        self.records[record.name.value] = record

    def find(self, name):
        return self.records.get(name)

    def all_records(self):
        return self.records.values()

    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        next_week = today + timedelta(days=7)
        results = []

        for record in self.records.values():
            if record.birthday:
                if isinstance(record.birthday.value, str):
                    record.birthday.value = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year.date() <= next_week:
                    results.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })

        return results

    def save_to_file(self, filename="addressbook.pkl"):
        """Зберігає адресну книгу у файл."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename="addressbook.pkl"):
        """Відновлює адресну книгу з файлу."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook()  # Повертає новий екземпляр, якщо файл не знайдено
