#!/bin/bash

echo "installing packages"
sudo pacman -Syyu
sudo pacman -S --needed git tmux vim python-pip xf86-video-fbdev htop raspberrypi-firmware xterm base-devel

yay -S mpv-rpi # wir brauchen nur die dependencies
yay -Rdd mpv-rpi

echo "installing pip dependencies"
yes | sudo pip install python-mpv Adafruit_PN532

echo "cloning mpv-rpi repo"
cd ~
git clone https://aur.archlinux.org/mpv-rpi.git
cd mpv-rpi
git checkout 69b28392d825428abafe14c38e7749974eeb3c81
rm -rf mpv* pkg src waf* || true

echo "starting build"
makepkg -si