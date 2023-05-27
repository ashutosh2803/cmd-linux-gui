import subprocess
from tabulate import tabulate


def anycom():
    all_data = [["OPTION", "TYPE", "EXAMPLES"],
                ["1", "COMMAND WITHOUT ARGUMENTS", "pwd ,history"],
                ["2", "COMMAND WITH ARGUMENTS", "ps aux ,cd Desktop,mkdir NewFolder"]]
    print(tabulate(all_data, tablefmt='grid'))

    a = input("ENTER YOUR CHOICE:")

    if a == '1':
        p = input("ENTER THE COMMAND WITH NO ARGUMENTS:")
        result = subprocess.run([p])
        print(result.stdout)

    elif a == '2':
        q = input("ENTER THE FIRST PART:")
        r = input("ENTER THE ARGUMENT PART:")
        res = subprocess.run([q, r])
        print(res.stdout)

    else:
        print("You Choose an Invalid Option. Please Try again!")



