import os

def mkdirModule():
    
    # Taking path as input
    path_input = input("Enter the path: ")

    #checking for path location
    if '.' in path_input:
        path = os.getcwd()
    else:
        path = path_input
        # using mkdir to create directory
        os.mkdir(path)
        print("Successfully created directory " + path)
