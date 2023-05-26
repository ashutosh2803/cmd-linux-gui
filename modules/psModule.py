import subprocess

def ps():
    result = subprocess.run(["ps", "aux"], shell=True, capture_output=True, text=True)
    print(result.stdout)
