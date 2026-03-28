import os

def add_blocker():
    """Ask the user for their daily blocker and save it persistently."""
    blocker = input("Please enter your Daily Blocker: ")
    with open("database.txt", "a") as file:
        file.write(blocker + "\n")
    print("Blocker successfully recorded.")

def fetch_blockers():
    """Retrieve and display all blockers from the database."""
    if os.path.exists("database.txt"):
        with open("database.txt", "r") as file:
            lines = file.readlines()
            if lines:
                print("\nTeam Daily Blockers:")
                for idx, line in enumerate(lines, start=1):
                    print(f"{idx}. {line.strip()}")
            else:
                print("The database is currently empty.")
    else:
        print("Error: database.txt does not exist.")

def overwrite_warning():
    """Warn the user if they attempt to overwrite the file."""
    if os.path.exists("database.txt"):
        print("Warning: Overwriting will erase all existing blockers.")
    else:
        print("No existing file found. A new one will be created.")

def main():
    option = ""
    while option != "4":
        print("\nTeam Daily Status Menu")
        print("1. Add Blocker")
        print("2. Fetch Blockers")
        print("3. Overwrite Warning")
        print("4. Exit")

        option = input("Select an option (1-4): ")

        if option == "1":
            add_blocker()
        elif option == "2":
            fetch_blockers()
        elif option == "3":
            overwrite_warning()
        elif option == "4":
            print("Exiting program.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


"""
Protocol Selection:

1. "I will notify the team on Slack so they can respond quickly and help resolve the blocker."
2. "If the issue requires structured follow-up, I will create a Jira ticket with detailed information."
3. "I will send an email to the project manager to explain the impact and share supporting evidence."

Vocabulary Integration

The program saves the daily blockers in a text file, ensuring that the information is not lost when the system is closed.
Each time a new blocker is added, append mode is used to preserve the previous data and prevent it from being deleted.
When reviewing the blockers, the program opens the file and displays the list clearly and in an organized manner.
If the user decides to delete everything, the program shows a warning beforehand to confirm the action.
During development, I communicate with my team mainly via Slack, which makes it easy to discuss issues and suggest improvements quickly.
"""
