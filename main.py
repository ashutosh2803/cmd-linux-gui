# main file to execute all modules in gui and cli sys
from tabulate import tabulate
from modules import calModule, dateModule, initModule, installModule, pwdModule, mkdirModule


def main():
    head = [["COMMAND LINE INTERFACE", "CREATED BY ACHIEVERS TEAM"]]
    all_data = [["FUNCTION NUMBER", "DESCRIPTION", "CONTRIBUTORS"],
                [1, "Calender", "NISHANT VIDHU"],
                [2, "Date", "ASHUTOSH KUMAR"],
                [3, "init package", "ADITYA KUMAR"],
                [4, "Package installation", "AMIT KOUSHIK"],
                [5, "Print Working Directory", "NISHANT VIDHU"],
                [6, "Create a New Folder", "VINAYAK PANDIA"]]
    print(tabulate(head, tablefmt='fancy_grid'))
    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))

    a = input("SELECT YOUR CHOICE:")

    if a == '1':
        print(calModule.calmodule())

    elif a == '2':
        print(dateModule.dateModule())

    elif a == '3':
        print(initModule.initFunction())

    elif a == '4':
        print(installModule.main())

    elif a == '5':
        print(pwdModule.pwd())
    
    elif a == '6':
        print(mkdirModule.mkdirModule())

    else:
        print("YOU CHOOSE A WRONG CHOICE PLEASE TRY AGAIN")


main()
