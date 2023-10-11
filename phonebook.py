import json
# https://www.w3schools.com/python/python_json.asp




class Phonebook:
    #
    # The Default __init__ Constructor in C++ and Java. Constructors are used to initializing the object’s state.
    # https://www.geeksforgeeks.org/__init__-in-python/
    def __init__(self, filename='phonebook.json'):
        self.filename = filename
        self._load_entries()

    # Method to load entries from the JSON file
    def _load_entries(self):
        try:
            with open(self.filename, 'r') as file:
                self.entries = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = {}

    # Method to save entries into the JSON file
    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.entries, file)

    # Method to add a new entry to the phonebook
    def add(self, name, number):
        if name in self.entries:
            overwrite = input(f"{name} already exists with number {self.entries[name]}. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                return
        # Add/Update the entry in the dictionary
        self.entries[name] = number
        # Save the updated entries to the file
        self.save_to_file()
        print(f"Entry for {name} added successfully!")

    # Method to lookup an entry by name
    def lookup(self, name):
        # Return the number for the name, or "Not found" if the name doesn't exist
        return self.entries.get(name, "Not found")

    # Method to delete an entry by name
    def delete(self, name):
        if name in self.entries:
            del self.entries[name]
            # Save the updated entries to the file
            self.save_to_file()
            print(f"Entry for {name} deleted!")
        else:
            print(f"{name} not found in the phonebook.")

    # Method to display all the entries in the phonebook
    def display_all(self):
        if not self.entries:
            print("No entries in the phonebook.")
            return

        # Read more about Python String format() Method:  https://www.w3schools.com/python/ref_string_format.asp
        # displaying header for style
        print("\nPhonebook Entries:")
        print("-" * 30)
        print(f"{'Name':<15} | {'Number'}")
        print("-" * 30)

        # Display entries in a sorted, table-like format
        for name, number in sorted(self.entries.items()):
            print(f"{name:<15} | {number}")

        print("-" * 30)


def main():


    phonebook = Phonebook("Person.json")

    # The  menu options using dictionary key-value pairs for simplicity
    menu_options = {
        "1": ("Add Entry", phonebook.add), # To retrieve  menu_options["1"][1](name, number)
        "2": ("Lookup Number", phonebook.lookup),
        "3": ("Delete Entry", phonebook.delete),
        "4": ("Display All Entries", phonebook.display_all),
        "5": ("Quit", None)
    }

    # Infinite loop to keep the application running until the user chooses to quit
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
                action[1](name, number) # arguments for action
            elif choice in ["2", "3"]:
                name = input(f"Enter the name to {action[0].lower()}: ")
                print(action[1](name))
            else:
                action[1]()
        else:
            print("Invalid option. Please choose between 1-5.")




if __name__ == "__main__":
    main()
