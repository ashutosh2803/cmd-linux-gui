# main file to execute all modules in gui and cli sys

import platform
from tabulate import tabulate
from modules import calModule, dateModule, initModule, installModule, mkdirModule, psModule, anyCom, systemModule, \
    pingModule, help, pkgInstall


def main():
    opsys: str = platform.system()
    head1 = [["OS DETECTED --> ", opsys]]

    head = [["COMMAND LINE INTERFACE", "CREATED BY ACHIEVERS TEAM"]]
    head2 = [["(CROSS PLATFORM PYTHON SCRIPT)"]]
    all_data = [["FUNCTION NUMBER", "DESCRIPTION", "CONTRIBUTORS"],
                [1, "Calender", "NISHANT VIDHU"],
                [2, "Date", "ASHUTOSH KUMAR"],
                [3, "init Package", "ADITYA KUMAR"],
                [4, "Package Installation", "AMIT KOUSHIK"],
                [5, "Running Processes List", "NISHANT VIDHU"],
                [6, "Create a New Directory", "VINAYAK PANDIA"],
                [7, "PING any Website", "NISHANT VIDHU"],
                [8, "Info About any command ", "NISHANT VIDHU"],
                [9, "system Information", "NISHANT VIDHU"],
                [10, "Run Command of Your choice", "NISHANT VIDHU"]]

    print(tabulate(head1, tablefmt='grid'))
    print(tabulate(head2, tablefmt='grid'))
    print(tabulate(head, tablefmt='fancy_grid'))
    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))

    a = input("SELECT YOUR CHOICE:")

    if a == '1':
        print(calModule.calmodule())

    elif a == '2':
        print(dateModule.dateModule())

    elif a == '3':
        print(initModule.initFunction())

    # install module code
    elif a == '4':
        if opsys == "Linux":
            print(installModule.main())
        elif opsys == "Windows":
            print(pkgInstall.winPkg())
        elif opsys == "Darwin":
            print(pkgInstall.MacPkg())

    # process module code
    elif a == '5':

        if opsys == "Linux":
            print(psModule.ps())
        elif opsys == "Windows":
            print(psModule.Winps())
        elif opsys == "Darwin":
            print(psModule.Macps())

    elif a == '6':
        print(mkdirModule.mkdirModule())

    # ping module code
    elif a == '7':

        if opsys == "Linux":
            print(pingModule.ping())
        elif opsys == "Windows":
            print(pingModule.pingWin())
        elif opsys == "Darwin":
            print(pingModule.ping())

    # command help code
    elif a == '8':

        if opsys == "Linux":
            print(help.help1())
        elif opsys == "Windows":
            print(help.helpWin())
        elif opsys == "Darwin":
            print(help.help1())

    # system information
    elif a == '9':

        if opsys == "Linux":
            print(systemModule.sys())
        elif opsys == "Windows":
            print(systemModule.WinSys())
        elif opsys == "Darwin":
            print(systemModule.sys())

    # any command run
    elif a == '10':
        print(anyCom.anycom())


    else:
        print("YOU CHOOSE A WRONG CHOICE PLEASE TRY AGAIN")


main()
