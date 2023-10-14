import json
# https://www.w3schools.com/python/python_json.asp

# https://www.geeksforgeeks.org/__init__-in-python/
#  https://www.w3schools.com/python/ref_string_format.asp

class Phonebook:

    def __init__(self, filename='phonebook.json'):
        self.filename = filename
        self._load_entries()
    def _load_entries(self):
        try:
            with open(self.filename, 'r') as file:
                self.entries = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = {}


    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.entries, file)

    def add(self, name, number):
        if name in self.entries:
            overwrite = input(f"{name} already exists with number {self.entries[name]}. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                return

        self.entries[name] = number
        self.save_to_file()
        print(f"Entry for {name} added successfully!")

    def lookup(self, name):
        return self.entries.get(name, "Not found")


    def delete(self, name):
        if name in self.entries:
            del self.entries[name]

            self.save_to_file()
            print(f"Entry for {name} deleted!")
        else:
            print(f"{name} not found in the phonebook.")
    def display_all(self):
        if not self.entries:
            print("No entries in the phonebook.")
            return
        print("\nPhonebook Entries:")
        print("-" * 30)
        print(f"{'Name':<15} | {'Number'}")
        print("-" * 30)
        for name, number in sorted(self.entries.items()):
            print(f"{name:<15} | {number}")

        print("-" * 30)


def main():


    phonebook = Phonebook("Person.json")
    menu_options = {
        "1": ("Add Entry", phonebook.add),
        "2": ("Lookup Number", phonebook.lookup),
        "3": ("Delete Entry", phonebook.delete),
        "4": ("Display All Entries", phonebook.display_all),
        "5": ("Quit", None)
    }

    while True:
        print("\nPhonebook Menu:")
        for key, value in menu_options.items():
            print(f"{key}. {value[0]}")

        choice = input("Choose an option (1-5): ")
        if choice == "5":
            print("Exiting phonebook. Goodbye!")
            break

        action = menu_options.get(choice)

        if action:
            if choice == "1":
                name = input("Enter the name: ")
                number = input("Enter the phone number: ")
                # menu_options["1"][1](name, number)
                action[1](name, number)
            elif choice in ["2", "3"]:
                name = input(f"Enter the name to {action[0].lower()}: ")
                print(action[1](name))
            else:
                action[1]()
        else:
            print("Invalid option. Please choose between 1-5.")




if __name__ == "__main__":
    main()
