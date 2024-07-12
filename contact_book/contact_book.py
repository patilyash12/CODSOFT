import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'], data['address'])

def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as file:
            contacts_dict = json.load(file)
            return [Contact.from_dict(contact) for contact in contacts_dict]
    except FileNotFoundError:
        return []

def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append(Contact(name, phone, email, address))
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact.name} - {contact.phone}")

def search_contacts(contacts):
    query = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if query in contact.name.lower() or query in contact.phone]
    if results:
        for contact in results:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
    else:
        print("No matching contacts found.")

def update_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            contact = contacts[idx]
            contact.name = input(f"Enter new name (current: {contact.name}): ") or contact.name
            contact.phone = input(f"Enter new phone number (current: {contact.phone}): ") or contact.phone
            contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
            contact.address = input(f"Enter new address (current: {contact.address}): ") or contact.address
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            contacts.pop(idx)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save and Exit")

def main():
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
