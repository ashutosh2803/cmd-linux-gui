import subprocess


def help1():
    print("It will Provide you Information about the commands eg:ls , ps etc...")
    a = input("ENTER THE COMMAND:")
    result = subprocess.run(["man", a])
    print(result.stdout)


def helpWin():
    print("It will Provide you Information about the commands eg:DISKPART,DIR,COLOR etc...")
    print(subprocess.run(["help"]))
    a = input("ENTER THE COMMAND:")
    result = subprocess.run(["help", a])
    print(result.stdout)


