from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.records = {}  # Використовуємо як контейнер для зберігання контактів

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

        for record in self.records.values():  # Виправлено з self.data на self.records
            if record.birthday:
                # Якщо значення дня народження — рядок, конвертуємо його
                if isinstance(record.birthday.value, str):
                    record.birthday.value = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year.date() <= next_week:
                    results.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })

        return results


