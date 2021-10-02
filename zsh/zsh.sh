#!/bin/bash

pkg update
pkg install toilet
toilet -f term -F border --gay "Hola, soy s8m6n2o7a mucho gusto"
#Installing zsh
pkg install zsh
#Installing Oh-My-Zsh
rm ~/.zshrc
cp .zshrc $HOME
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
#Installing Dracula theme
git clone https://github.com/dracula/zsh.git
cd zsh && cp dracula.zsh-theme ~/.oh-my-zsh/themes/
cp -rf lib oh-my-zsh/themes
toilet -f term -F border --gay "Mucho"
