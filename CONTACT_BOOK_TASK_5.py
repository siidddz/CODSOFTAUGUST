contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")
            print()

def search_contact():
    search_term = input("Enter a name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term in (name, info['Phone']):
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")
            print()
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        address = input("Enter the new address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
