import re
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
            if not value.strip():
                raise Exception("Name required field.")
            super().__init__(value.strip())
          
class Phone(Field):
    def __init__(self, phone):
        if not re.match(r'^\d{10}$', phone):
            raise Exception("The phone number must be 10 digits.")
        super().__init__(phone)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")