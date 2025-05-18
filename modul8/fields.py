from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must be a 10-digit number.")
        super().__init__(value)

class Birthday:
    def __init__(self, value):
        self.value = self._validate_birthday(value)

    def _validate_birthday(self, value):
        if isinstance(value, str):
            day, month, year = map(int, value.split("."))
            return datetime(year, month, day)  # Перетворюємо в об'єкт datetime
        raise ValueError("Invalid birthday format. Use DD.MM.YYYY")
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y") if self.value else "No birthday"