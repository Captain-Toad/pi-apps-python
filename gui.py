import guizero
import sys
import time
import os

def start():
	if os.name != ("posix"):
		os.system('cls')
		while True:
			os.system('clear')
			print("Error: Pi Apps for Python is not supported on Windows. Please install the program on a *nix machine. Press CTRL+C to exit.")
			time.sleep(1)
			os.system('clear')
			print("       Pi Apps for Python is not supported on Windows. Please install the program on a *nix machine. Press CTRL+C to exit.")
			time.sleep(1)
		quit()
	else:
		os.system('clear')
		print('\033[32m' + "Operating System detected as: " + os.name + ". Continuing..." + '\033[0m')
		print('\033[30m' + "Current working directory: " + os.getcwd() + '\033[0m')
		cwd = os.getcwd()
		if cwd != ("$HOME/pi-apps"):
			print('\033[31m' + "Error: Pi Apps for Python is not installed in the correct directory. Please install the program in the directory: $HOME/pi-apps. Please run ./install.sh." + '\033[0m')
			quit()

def gui():
    app = guizero.App(title="Pi Apps for Python", width=600, height=300, layout="grid")
    logo = guizero.Picture(app, image="icons/logo-simple.png", width=100, height=100, grid=[1, 1])
    logo_text = guizero.Picture(app, image="icons/logo-text.png", width=218, height=80, grid=[2, 1])
    logo_ext_text = guizero.Text(app, text="for Python", size=30, grid=[5,1])
    app.display()
start()
gui()
