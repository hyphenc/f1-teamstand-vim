#!/bin/bash

echo "installing packages"
sudo apt update
sudo apt -y install mpv

echo "installing pip dependencies"
yes | sudo pip3 install python-mpv
yes | sudo pip3 install Adafruit_PN532