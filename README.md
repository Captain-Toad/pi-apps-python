# Pi Apps for Python: A Front-end for Pi-Apps
Pi Apps for Python is a front end for pi-apps (which can be found at [Botspot's GitHub repo.](http://github.com/Botspot/pi-apps "Botspot's GitHub repo."))

*From here on, I may refer to Pi Apps for Python as PAFP.*

The main reason I am making this is because I love Pi Apps, but I am slightly irritated at yad's terrible draw times. It can take over 5 to 10 seconds to draw a single window. I am using a Python module named [guizero](http://lawsie.github.io/guizero "guizero"), which is essentially Tkinter but with a simpler syntax. (It is based on Tkinter.) It has relatively fast loading times.

## Installation
Installation for Pi Apps for Python is simple. I spent about an hour writing a fancy bash script to install PAFP. Clone the repo with:

`git clone https://github.com/captain-toad/pi-apps-python`.

Navigate to the new directory with:

`cd pi-apps-python`

Make install.sh executable with:

`chmod +x install.sh`

And finally, run install.sh with:

`./install.sh`.

If you want to do all of that in one command, try:

`git clone https://github.com/captain-toad/pi-apps-python && cd pi-apps-python && chmod +x install.sh && ./install.sh`.

Just let everything install, and you're good to go!
