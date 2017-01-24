#!/usr/bin/env bash

printf "Downloading new version...\n"
git fetch --all
git reset --hard origin/master
printf "Remove old version...\n"
sudo -u pi /home/pi/oprint/bin/pip uninstall -y Octoprint-netconnectd
printf "Installing new version...\n"
sudo -u pi /home/pi/oprint/bin/python setup.py install

