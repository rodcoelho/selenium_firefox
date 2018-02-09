#!/usr/bin/env bash

sudo apt-get install python-pip

sudo pip install selenium

wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz

tar -xvzf geckodriver-v0.18.0-linux64.tar.gz

chmod +x geckodriver

chmod 755 geckodriver

#export PATH=$PATH:/usr/bin/env/geckodriver
mv geckodriver /usr/local/bin