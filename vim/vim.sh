#!/bin/bash

pkg update
apt update --fix-missing
toilet -f term -F border --gay "Hola, soy s8m6n2o7a mucho gustov"
sleep 3
pkg install -y vim
apt update --fix-missing
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
apt update --fix-missing
cp .vimrc $HOME
mkdir ~/.vim/plug
apt update --fix-missing
toilet -f term -F border --gay "Mucho"
