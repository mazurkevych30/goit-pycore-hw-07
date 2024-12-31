from record import Record
from address_book import AddressBook
from datetime import datetime



def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return e

    return inner


@input_error
def add_contact(args: list, book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def show_all(book: AddressBook) -> None :
    print("My contacts:")
    for _ , record in book.data.items():
        print(record)


@input_error
def show_phone( args: list, book: AddressBook) -> None: 
    name = args[0]
    record = book.find(name)
    if record is None:
       print("Contact not found.")
       return
    
    for number in record.phones:
        print(number)
    

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact not found."

    return record.edit_phone(old_phone, new_phone)


@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."
    
    return record.add_birthday(birthday)

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."
    
    if record.birthday is None:
        return record.birthday
    return f"{name} birthday {datetime.strftime(record.birthday.value, "%d.%m.%Y")}"

@input_error
def birthdays(book: AddressBook):
    dates = book.book.get_upcoming_birthdays()
    if len(dates) == 0:
        print("Not upcoming birthday")
        return
    for name, day in dates.items():
        print(f"")