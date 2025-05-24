from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        value = str(value)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must be a 10-digit number.")
        super().__init__(value)
    def __str__(self):
        return self.value
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value
    def __hash__(self):
        return hash(self.value)

class Birthday(Field):
    def __init__(self, value):
        self._validate_birthday(value)
        super().__init__(value)

    def _validate_birthday(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid birthday format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value
