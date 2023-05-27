import subprocess


def ps():
    result = subprocess.run(["ps", "aux"])
    print(result.stdout)


def Winps():
    print(subprocess.run(["tasklist"]))


def Macps():
    print(subprocess.run(["top"]))
