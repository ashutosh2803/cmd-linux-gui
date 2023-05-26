import subprocess

def ping():
    a = input("ENTER THE COMMAND:")
    result = subprocess.run(["ping", a], shell=True, capture_output=True, text=True)

    print(result.stdout)
ping()