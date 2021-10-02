#!/bin/bash


pkg update
pkg install toilet
toilet -f term -F border --gay "Hola, soy s8m6n2o7a mucho gusto"
#Installing zsh
pkg install zsh
#Installing Oh-My-Zsh
curl sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
#Installing Dracula theme
git clone https://github.com/dracula/zsh.git
ln -s $DRACULA_THEME/dracula.zsh-theme $OH_MY_ZSH/themes/dracula.zsh-theme
toilet -f term -F border --gay "Mucho"
