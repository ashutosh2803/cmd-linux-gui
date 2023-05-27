import subprocess


def sys():
    result = subprocess.run(["hostnamectl"])
    print(result.stdout)
    res = subprocess.run(["lscpu"])
    print(res.stdout)
    a = subprocess.run(["ifconfig"])
    print(a.stdout)
    b = subprocess.run(["lspci"])
    print(b.stdout)


def macSys():
    print(subprocess.run(["system_profiler", "SPSoftwareDataType", "SPHardwareDataType"]))
    print(subprocess.run(["system_profiler", "-listDataTypes"]))
    a = input("ENTER A COMMAND FROM ABOVE:")
    print(subprocess.run([a]))


def WinSys():
    print("PRINTING SYSTEM INFO:")
    print(subprocess.run(["systeminfo"]))
    print("PRINTING MAC ADDRESS:")
    print(subprocess.run(["getmac"]))
    print("PRINTING CPU DETAILS")
    print(subprocess.run(["wmic", "cpu"]))
    print("PRINTING PARTITION DETAILS:")
    print(subprocess.run(["wmic", "partition", "get", "name,size,type"]))
    print("PRINTING WINDOWS VERSION:")
    print(subprocess.run(["winver"]))
