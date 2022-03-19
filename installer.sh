clear
echo -e "\033[36mWelcome to the Pi Apps for Python installer. This will install the Pi Apps for Python front-end on your Linux machine.\033[0m" 
echo "This installer will install or update the following:"
echo " - Python3 (if not already installed)"
echo " - guizero (through pip3, if not already installed)"
echo " - pi-apps (if not already installed)"
echo " - Pi Apps for Python (will be moved to ~/pi-apps)"
echo " - A desktop shortcut to the Pi Apps for Python front-end will be installed in /usr/share/applications"
echo "Are you sure you want to continue? (y/n)"
read answer
if [ "$answer" != "y" ]; then
    echo "The installation wil be aborted. Remove the installation files? (~/pi-apps-python) (y/n)"
    read answer1
    if [ "$answer1" != "y" ]; then
        echo "The installation has been aborted, but files have been preserved."
        exit
    fi
    echo "Removing..."
    rm -rf $HOME/pi-apps-python
    echo "Files have been removed, and the installation has been aborted."
    exit
fi
command -v apt >/dev/null || error "\033[31mYou are not running Debian or a deriatve of it. This installer is for Debian based systems.\033[0m"
echo -e "\033[32m😀 Your system is Debian based! Continuing...\033[0m"
if uname -m | grep -q 'x86' ;then
    error -e "\033[31mPi-Apps is not not supported on non-arm processor architectures. You can install pi-apps-x86, but the Pi Apps for Python front-end will not be compatible.\033[0m"
fi
echo -e "\033[32m😀 Your processor architecture is ARM, supported by Pi Apps for Python! Continuing...\033[0m"
echo -e "\033[34m⬇ Downloading or Updating Python3...\033[0m"
sudo apt install python3
echo -e "\033[32m😀 Python3 has been installed or updated! Continuing...\033[0m"
echo -e "\033[34m⬇ Downloading or Updating guizero...\033[0m"
pip3 install guizero
echo -e "\033[32m😀 guizero has been installed or updated! Continuing...\033[0m"
echo -e "\033[34m⬇ Downloading or Updating pi-apps...\033[0m"
wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
echo -e "\033[32m😀 pi-apps has been installed or updated! Continuing...\033[0m"
echo -e "\033[34m↔ Copying Pi-Apps for Python to ~/pi-apps...\033[0m"
cp gui.py $HOME/pi-apps
echo -e "\033[32m😀 Pi-Apps for Python has been moved to ~/pi-apps! Continuing...\033[0m"
echo -e "\033[34m↔ Installing desktop shortcut...\033[0m"
sudo cp pi-apps-python.desktop /usr/share/applications/
echo -e "\033[32m😀 Desktop shortcut has been installed! Installation Complete!\033[0m"
echo -e "\033[32m😀 You can now run the Pi Apps for Python front-end by selecting 'Pi Apps for Python' in the menu. (don't think it works right now though, you might have to run it with python3 ~/pi-apps/gui.py)\033[0m"
echo -e "\033[32m🙏 Thank you for installing Pi Apps for Python! Would you like to remove the installation files? (~/pi-apps-python) (y/n)\033[0m"
read answer2
if [ answer2 == "y" ]; then
    echo "Removing..."
    rm -rf $HOME/pi-apps-python
    echo "Files have been removed. Bye!"
    exit
fi
echo "Installation files will be preserved. Bye!"
exit
