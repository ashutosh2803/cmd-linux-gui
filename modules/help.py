import subprocess


def help1():
    print("It will Provide you Information about the commands eg:ls , ps etc...")
    a = input("ENTER THE COMMAND:")
    result = subprocess.run(["man", a])
    print(result.stdout)
