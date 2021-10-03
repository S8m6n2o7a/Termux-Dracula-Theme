#!/bin/bash

pkg update
toilet -f term -F border --gay "Hola, soy s8m6n2o7a mucho gusto"
apt update --fix-missing
sleep 3
#Installing zsh
pkg install -y zsh
apt update --fix-missing
#Installing Oh-My-Zsh
rm ~/.zshrc
cp .zshrc $HOME
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
apt update --fix-missing
#Installing Dracula theme
git clone https://github.com/dracula/zsh.git
apt update --fix-missing
cd zsh && cp dracula.zsh-theme ~/.oh-my-zsh/themes/
apt update --fix-missing
cp -rf lib ~/.oh-my-zsh/themes
apt update --fix-missing
toilet -f term -F border --gay "Mucho"
