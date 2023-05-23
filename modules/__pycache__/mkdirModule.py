import os

def create_directory():
    directory_name = input("Enter the directory name: ")

    # Check if the directory already exists
    if not os.path.exists(directory_name):
        # Create the directory
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

# Call the function to create the directory
create_directory()