from fields import Name, Phone, Birthday
from datetime import datetime

class Record:
    def __init__(self, name = ""):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone = ""):
        self.phones.append(Phone(phone))
        return "Added mobile phone number."

    def remove_phone(self, phone: str):
        phone = self.find_phone(phone)
        if isinstance(phone, str):
            return phone
        
        self.phones.pop(self.phones.index(phone))
        return "Mobile number has been deleted."
        

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if isinstance(phone, str):
            return phone
        
        self.phones[self.phones.index(phone)] = Phone(new_phone)
        return "Mobile number has been changed."
       
    def find_phone(self, phone):
        for number in self.phones:
            if phone == number.value:
                return number
        return "Mobile number not found."
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return "Birthday updated."

    def __str__(self):
        birthday_value = datetime.strftime(self.birthday.value, "%d.%m.%Y") if self.birthday else "No birthday"
        return f"Contact name: {self.name.value}, birthday: {birthday_value}, phones: {'; '.join(p.value for p in self.phones)}"