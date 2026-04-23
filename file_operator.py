import datetime     # Used to get current date and time
import os           # Used for file operations like delete

print("Welcome to Personal Journal Manager!!!")

class JournalManager: 
    
    # Function to add a new journal entry
    def new_entry():
        # Open file in append mode (creates file if it doesn't exist)
        with open('journal.txt', 'a') as j: 
            # Get current timestamp
            entry_time = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            # Take user input
            user_input = input("Please enter your Journal Entry:\n\n")
            # Write timestamp and entry into file
            j.write(entry_time + "\n")
            j.write(user_input + "\n\n")
            print("\nEntry added successfully!")
    
    # Function to view all journal entries
    def view_entries():
        try: 
            with open('journal.txt', 'r')as j:
                print("Your Journal Entries:")
                print("----------------------------------")
                
                # Read and print each line
                for line in j:
                    print(line.strip())
        except FileNotFoundError:
            print("No Journal Entries found. Start by adding a new entry!")

    # Function to search for a word in entries
    def search_entry():
        word = input("please enter the word you want to search: ")

        try: 
            with open("journal.txt","r") as j:
                found = False
                
                # Search word line by line
                for line in j:
                    if word.lower() in line.lower():
                        print(line.strip())
                        found = True
                
                # If no match found
                if not found:  
                    print("Word not found in the file")  
                    
        except PermissionError:
            print("Permission denied! Unable to read the file.")
        except FileNotFoundError:
            print("No Journal Entries found. Start by adding a new entry!")

     # Function to delete all entries (delete file)        
    def delete_entry():
        ask_permission = input("are you sure you want to delete all the enteries?(yes/no)").lower()
        if ask_permission == 'yes':
            try:
                os.remove("journal.txt")    # delete file completely
                print("All the entries deleted successfully!!")
            except PermissionError:
                print("Permission denied! Unable to delete the file.")
            except FileNotFoundError: 
                print("No Journal Entries to delete")
        else:
            print("As you said No, We have not deleted any enteries!")

# Main program loop
while True:
    print("\nPlease Select an Option: \n" \
        "1. Add a New Entry \n" \
        "2. View All Entries \n" \
        "3. Search For an Entry \n" \
        "4. Delete All Entries \n" \
        "5. Exit")
    
    try: 
        choice = int(input("Please Input Your choice: "))
    except ValueError as v:
        print("Please enter a number!!",v)
        continue

    # Menu handling
    if choice == 1:
        JournalManager.new_entry()
    elif choice == 2:
        JournalManager.view_entries()
    elif choice == 3:
        JournalManager.search_entry()
    elif choice == 4:
        JournalManager.delete_entry()
    elif choice == 5: 
        print("Thank you for using Personal Journal Manager. Goodbye!!!")
        print("Exiting the Program.....")
        break   # Exit loop

    else:
        print("Invalid option. Please select a valid option from the menu!")