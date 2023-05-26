import subprocess

def ping():
    
    p= subprocess.Popen("ping google.com")
    p.wait()
    print(p.poll())

ping()