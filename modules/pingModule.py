import subprocess


def ping():
    a = input("Enter the website(in www.xyz.com format): ")
    result = subprocess.run(['ping', a, '-c', '10'], capture_output=True, text=True)
    print(result.stdout)


def pingWin():
    a = input("Enter the website(in www.xyz.com format): ")
    result = subprocess.run(['ping', a])
    print(result.stdout)
