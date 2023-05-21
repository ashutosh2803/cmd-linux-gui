import sys
import os
import subprocess
import datetime

def initModule():
    # Function to display the menu options
    def display_menu():
        print("Basic CMD Menu")
        print("1. System Information")
        print("2. File Operations")
        print("3. Run Command")
        print("4. Current Date and Time")
        print("5. Exit")

    # Function to get user input and execute corresponding functionality
    def process_user_choice(choice):
        if choice == '1':
            print("System Information:")
            # Call functions from sys module to get system information
            print("Operating System:", sys.platform)
            print("Python Version:", sys.version)
            print("")

        elif choice == '2':
            print("File Operations:")
            file_path = input("Enter the file path: ")

            # Call functions from os module to perform file operations
            if os.path.exists(file_path):
                print("File exists!")
                print("File Size:", os.path.getsize(file_path))
            else:
                print("File does not exist!")
            print("")

        elif choice == '3':
            print("Run Command:")
            command = input("Enter the command to run: ")

            # Call functions from subprocess module to run a command
            subprocess.run(command, shell=True)
            print("")

        elif choice == '4':
            print("Current Date and Time:")
            # Call function from datetime module to display current date and time
            current_datetime = datetime.datetime.now()
            print("Current Date:", current_datetime.strftime("%B %d, %Y"))
            print("Current Time:", current_datetime.strftime("%I:%M %p"))
            print("")

        elif choice == '5':
            print("Exiting the program...")
            sys.exit()

        else:
            print("Invalid choice! Please enter a valid option.")
            print("")

    def init_functionality():
        print("Initializing the program...")
        # Add any initialization steps here
        print("Program initialized!")
        print("")

    # Main program loop
    while True:
        display_menu()
        user_choice = input("Enter your choice (1-5): ")

        if user_choice == '0':
            init_functionality()
        else:
            process_user_choice(user_choice)

# Entry point of the module
if __name__ == "__main__":
    initModule()
