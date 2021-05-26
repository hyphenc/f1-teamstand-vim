#!/bin/bash

echo "installing packages"
sudo pacman -Syyu
sudo pacman -S --needed git tmux vim python-pip xf86-video-fbdev htop raspberrypi-firmware xterm base-devel python-raspberry-gpio

yay -S mpv-rpi # wir brauchen nur die dependencies
yay -Rdd mpv-rpi

echo "installing pip dependencies"
yes | sudo pip install Adafruit_PN532

cd ~

echo "cloning mpv-rpi repo"
git clone https://aur.archlinux.org/mpv-rpi.git && cd mpv-rpi
git checkout 69b28392d825428abafe14c38e7749974eeb3c81
# letzter version die mit den gelinkten libs auf dem rpi 3b+ noch zu funktionieren scheint
rm -rf mpv* pkg src waf* || true
echo "starting build"
makepkg -si

echo "cloning python-mpv repo"
git clone https://aur.archlinux.org/python-mpv.git && cd python-mpv
git checkout 15ef4c3f85bb35e99dfb039a1da0c5dc90d6e95a
echo "starting build"
makepkg -si

echo "you might want to move the executables to some place that's in your PATH"
