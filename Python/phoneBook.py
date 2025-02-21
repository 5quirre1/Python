class PhoneBook:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}"


contacts = []

def add():
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")

    new_contact = PhoneBook(name, address, phone)
    contacts.append(new_contact)
    print("\nContact added successfully!\n")

def remove():
    name = input("Enter the name of the contact to remove: ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            print(f"\n{name} has been removed.\n")
            return
    print("\nContact not found...\n")

def view():
    if not contacts:
        print("\nNo contacts available.\n")
    else:
        print("\nPhone Book:")
        for contact in contacts:
            print(contact)
        print()

def main():
    while True:
        print("Welcome to the Phone Book")
        print("\n1. Add\n2. Remove\n3. View\n4. Exit")
        choice = input("Choose: ").strip()

        match choice:
            case "1":
                add()
            case "2":
                remove()
            case "3":
                view()
            case "4":
                print("Come back soon!")
                break
            case _:
                print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
