#!/usr/bin/env bash

mkdir logs

sudo apt-get install python-pip

sudo pip install selenium

sudo pip install pyvirtualdisplay

wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz

tar -xvzf geckodriver-v0.18.0-linux64.tar.gz

chmod +x geckodriver

chmod 755 geckodriver

#export PATH=$PATH:/usr/bin/env/geckodriver
#sudo mv geckodriver /usr/bin/
sudo mv geckodriver /usr/local/bin

sudo apt-get install dbus-x11

sudo apt-add-repository ppa:mozillateam/firefox-next

sudo apt-get install firefox xvfb

if [[ ! -f /tmp/.X10-lock ]]; then
    Xvfb :10 -ac
else
    echo "INFO: $(date) - X Server already running" 1>&2
fi
export DISPLAY=:10