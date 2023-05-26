import subprocess


def sys():
    result = subprocess.run(["hostnamectl"], shell=True, capture_output=True, text=True)
    print(result.stdout)
    res = subprocess.run(["lscpu"], shell=True, capture_output=True, text=True)
    print(res.stdout)
    a = subprocess.run(["ifconfig"], shell=True, capture_output=True, text=True)
    print(a.stdout)
    b = subprocess.run(["lspci"], shell=True, capture_output=True, text=True)
    print(b.stdout)
