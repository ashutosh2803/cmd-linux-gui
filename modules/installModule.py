#! /usr/bin/python
import subprocess


# Function install a package 
def install_package(package_name) : 
	if check_package_installed(package_name):#Check before installing
		print(f'{package_name} is alredy installed.')
	else:#Install the package
		try:
			subprocess.check_call(['sudo','apt-get','install',package_name,'-y'])
			print(f"Sucessfully installed {package_name}")
		except subprocess.CalledProcessError:
			print(f"Failed to install {package_name}.Please check the package name and try again")


# Function to check if a package is alredy installed or not
def check_package_installed(package_name):
	try:
		subprocess.check_output(['dpkg','-s',package_name])
		return True
	except subprocess.CalledProcessError:
		return False



def main():
	print("Welcome to package installer :")
	#Prompt the menu until user exit
	while True:
		package_name = input("Enter the package name (or quit to exit):")
		if package_name.lower()=='quit':
			break
		install_package(package_name)
if __name__ == "__main__" :
	main()	
