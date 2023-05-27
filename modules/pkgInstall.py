import subprocess


def winPkg():
    c = input("Enter Package Name:")
    result = subprocess.run(["winget", "search", c])
    print(result.stdout)

    print("Please put ""if Package Name has space inbetween ")
    d = input("Enter Full Package Name:")
    result1 = subprocess.run(["winget", "install", d])
    print(result1.stdout)


def MacPkg():
    w = input("YOU REQUIRED TO INSTALL BREW IF YOU HAVE BREW PRESS 0 ,IF NOT PRESS 1")
    if w == '1':
        print("Please install Brew first")

    else:
        e = input("Enter package Name You want to Install")
        pr = subprocess.run(["brew", "install", e])
        print(pr.stdout)



