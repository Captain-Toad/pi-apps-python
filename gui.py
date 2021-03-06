#!/usr/bin/env python3

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
			print('\033[31m' + "Error: Pi Apps for Python is not installed in the correct directory. Please install the program in the directory: $HOME/pi-apps. Run install.sh, move the files manually, or press i to ignore." + '\033[0m')
			ignoredirectoryerr = input()
			if ignoredirectoryerr != "i":
				quit()

def gui():
    app = guizero.App(title="Pi Apps for Python", width=600, height=300, layout="grid")
    logo = guizero.Picture(app, image=os.environ['HOME'] + "/pi-apps/icons/logo-simple.png", width=100, height=100, grid=[1, 1])
    logo_text = guizero.Picture(app, image=os.environ['HOME'] + "/pi-apps/icons/vector/logo-ext-text.svg", grid=[2, 1])
    app.display()
start()
gui()
