#This script is used for testing purposes. It will download the gui.py script to ~/pafp-test every 30 seconds so I can run gui.py while editing with the VSCode Web IDE.
import os
import time

os.system("mkdir $HOME/pafp-test")
os.system("cd $HOME/pafp-test")
while True:
  os.system("wget https://raw.githubusercontent.com/Captain-Toad/pi-apps-python/main/gui.py")
  time.sleep(30)