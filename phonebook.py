# Import the json module to handle JSON file operations
import json

# Define the Phonebook class
class Phonebook:
    # Initializer method for the class
    def __init__(self, filename='phonebook.json'):
        self.filename = filename       # Set the filename for the phonebook storage
        self._load_entries()           # Load the phonebook entries from the file

    # Method to load entries from the JSON file
    def _load_entries(self):
        try:
            # Open the JSON file in read mode
            with open(self.filename, 'r') as file:
                # Load the JSON content into the 'entries' dictionary
                self.entries = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or there's an error in the JSON format, initialize an empty dictionary
            self.entries = {}

    # Method to save entries into the JSON file
    def save_to_file(self):
        # Open the JSON file in write mode
        with open(self.filename, 'w') as file:
            # Write the 'entries' dictionary as JSON into the file
            json.dump(self.entries, file)

    # Method to add a new entry to the phonebook
    def add(self, name, number):
        # Check if the name already exists in the phonebook
        if name in self.entries:
            # Ask the user if they want to overwrite the existing number
            overwrite = input(f"{name} already exists with number {self.entries[name]}. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                # If not, return without doing anything
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
        # Check if the name exists in the phonebook
        if name in self.entries:
            # Delete the entry from the dictionary
            del self.entries[name]
            # Save the updated entries to the file
            self.save_to_file()
            print(f"Entry for {name} deleted!")
        else:
            print(f"{name} not found in the phonebook.")

    # Method to display all the entries in the phonebook
    def display_all(self):
        for name, number in self.entries.items():
            print(f"{name}: {number}")

# Main function to run the phonebook application
def main():
    # Instantiate the Phonebook class
    phonebook = Phonebook()

    # Define the menu options for the application
    menu_options = {
        "1": ("Add Entry", phonebook.add),
        "2": ("Lookup Number", phonebook.lookup),
        "3": ("Delete Entry", phonebook.delete),
        "4": ("Display All Entries", phonebook.display_all),
        "5": ("Quit", None)
    }

    # Infinite loop to keep the application running until the user chooses to quit
    while True:
        print("\nPhonebook Menu:")
        # Display the menu options
        for key, value in menu_options.items():
            print(f"{key}. {value[0]}")

        # Get the user's choice
        choice = input("Choose an option (1-5): ")

        # Check if the user chose to quit
        if choice == "5":
            print("Exiting phonebook. Goodbye!")
            break

        # Get the corresponding action for the user's choice
        action = menu_options.get(choice)
        if action:
            # Check if the user chose to add an entry
            if choice == "1":
                name = input("Enter the name: ")
                number = input("Enter the phone number: ")
                action[1](name, number)
            # Check if the user chose to lookup or delete an entry
            elif choice in ["2", "3"]:
                name = input(f"Enter the name to {action[0].lower()}: ")
                print(action[1](name))
            else:
                # For displaying all entries
                action[1]()
        else:
            print("Invalid option. Please choose between 1-5.")

# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    # If so, run the main function
    main()
