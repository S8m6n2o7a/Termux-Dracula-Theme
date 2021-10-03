#!/bin/bash
pkg update
apt update --fix-missing
toilet -f term -F border --gay "Hola, soy s8m6n2o7a mucho gusto"
sleep 3
git clone https://github.com/dracula/termux/
apt update --fix-missing
cd termux
cp colors.properties ~/.termux
apt update --fix-missing
toilet -f term -F border --gay "Mucho"
