from collections import UserDict
from datetime import datetime, timedelta
from modul8.record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def get(self, name):
        return self.data.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.now()
        next_week = today + timedelta(days=7)
        results = []

        for record in self.data.values():
            if record.birthday:
                birthday_str = record.birthday.value
                birthday_dt = datetime.strptime(birthday_str, "%d.%m.%Y")
                birthday_this_year = birthday_dt.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if birthday_this_year.weekday() == 5:  # Saturday
                    birthday_this_year += timedelta(days=2)
                elif birthday_this_year.weekday() == 6:  # Sunday
                    birthday_this_year += timedelta(days=1)

                if today <= birthday_this_year <= next_week:
                    results.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })

        return results
