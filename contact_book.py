"""Contact Book using a Dictionary: add, search, update, delete contacts."""

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print("Contact already exists. Use update instead.")
        return
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"Contact '{name}' added.")


def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        contacts[name] = input("Enter new phone number: ").strip()
        print(f"Contact '{name}' updated.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return
    print("\n--- All Contacts ---")
    for name, phone in contacts.items():
        print(f"{name:<20} {phone}")


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. View all contacts")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()