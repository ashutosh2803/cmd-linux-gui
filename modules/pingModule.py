import subprocess

def ping():
    a = input("Enter a website (in www.abc.com format):")
    result = subprocess.run(["ping", a], shell=True, capture_output=True, text=True)

    print(result.stdout)
