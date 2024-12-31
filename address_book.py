from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        if str(record.name).lower() in self.data:
            raise ValueError(f"AddressBook already have record with name {str(record.name)}")
        self.data[str(record.name).lower()] = record
    
    def find(self, name: str):
        for name_record, record in self.data.items():
            if name_record == name.lower().strip():
                return record
        return None
    
    def delete(self, name: str):
        return self.data.pop(name.lower().strip(), None)
    
    def get_upcoming_birthdays(self) -> list:
        today = datetime.today().date()
        upcoming_birthdays = []
    
        for name, record in self.data.items():
            print(record.birthday)
            birthday_this_year = record.birthday.value.date().replace(year=today.year)
            if today.month == 12 and today.day > 20:
                birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)

            if birthday_this_year > today:
                if (birthday_this_year-today).days <= 7:
                    match birthday_this_year.weekday():
                        case 5:
                            birthday_this_year += timedelta(days=2)
                        case 6:
                            birthday_this_year += timedelta(days=1)

                    upcoming_birthdays.append({"name": name, "congratulation_date": datetime.strftime(birthday_this_year, "%Y.%m.%d")})
    
        return upcoming_birthdays

# book = AddressBook()

#     # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday("04.01.1998")

# print(john_record)
# book.add_record(john_record)
# print(book)

# print(book.get_upcoming_birthdays())