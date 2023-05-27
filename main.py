#! /usr/bin/python3
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
                [10, "Run Command of Your choice", "NISHANT VIDHU"],
                [11,"Exit/Quit"]]

    print(tabulate(head1, tablefmt='grid'))
    print(tabulate(head2, tablefmt='grid'))
    print(tabulate(head, tablefmt='fancy_grid'))
    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))

    a = input("SELECT YOUR CHOICE:")

    if a == '1':
        calModule.calmodule()

    elif a == '2':
        dateModule.dateModule()

    elif a == '3':
        initModule.initFunction()

    # install module code
    elif a == '4':
        if opsys == "Linux":
            installModule.main()
        elif opsys == "Windows":
            pkgInstall.winPkg()
        elif opsys == "Darwin":
            pkgInstall.MacPkg()

    # process module code
    elif a == '5':

        if opsys == "Linux":
            psModule.ps()
        elif opsys == "Windows":
            psModule.Winps()
        elif opsys == "Darwin":
            psModule.Macps()

    elif a == '6':
        mkdirModule.mkdirModule()

    # ping module code
    elif a == '7':

        if opsys == "Linux":
            pingModule.ping()
        elif opsys == "Windows":
            pingModule.pingWin()
        elif opsys == "Darwin":
            pingModule.ping()

    # command help code
    elif a == '8':

        if opsys == "Linux":
            help.help1()
        elif opsys == "Windows":
            help.helpWin()
        elif opsys == "Darwin":
            help.help1()

    # system information
    elif a == '9':

        if opsys == "Linux":
            systemModule.sys()
        elif opsys == "Windows":
            systemModule.WinSys()
        elif opsys == "Darwin":
            systemModule.sys()

    # any command run
    elif a == '10':
        anyCom.anycom()
    # Quit/Exit the program
    elif a == '11':
    	return
    else:
        print("YOU CHOOSE A WRONG CHOICE PLEASE TRY AGAIN")
    # Repeat the process if user wants...
    a = input("Do you want to continue?(y/n)")
    if a.lower() == 'y':
        main()
    return

if __name__ == "__main__":
    main()
