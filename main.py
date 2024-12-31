from command_parser import parse_input
from handlers import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from address_book import AddressBook

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))   
            case "change":
                print(change_contact(args, book)) 
            case "phone":
                show_phone(args, book)
            case "all":
                show_all(book)
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                birthdays(book)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()