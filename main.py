# main file to execute all modules in gui and cli sys
from tabulate import tabulate
from modules import calModule, dateModule, initModule, installModule, mkdirModule, psModule, anyCom, systemModule


def main():
    head = [["COMMAND LINE INTERFACE", "CREATED BY ACHIEVERS TEAM"]]
    all_data = [["FUNCTION NUMBER", "DESCRIPTION", "CONTRIBUTORS"],
                [1, "Calender", "NISHANT VIDHU"],
                [2, "Date", "ASHUTOSH KUMAR"],
                [3, "init Package", "ADITYA KUMAR"],
                [4, "Package Installation", "AMIT KOUSHIK"],
                [5, "Running Processes List", "NISHANT VIDHU"],
                [6, "Create a New Directory", "VINAYAK PANDIA"],
                [7, "System Information", "NISHANT VIDHU"],
                [8, "RUN COMMAND OF YOUR CHOICE", "NISHANT VIDHU"]]

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
        print(psModule.ps())

    elif a == '6':
        print(mkdirModule.mkdirModule())

    # elif a == '7':
    #   print(pingModule.ping())

    # elif a == '8':
    #   print(help.help1())

    elif a == '7':
        print(systemModule.sys())

    elif a == '8':
        print(anyCom.anycom())

    else:
        print("YOU CHOOSE A WRONG CHOICE PLEASE TRY AGAIN")


main()
