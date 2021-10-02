#!/bin/bash

pkg update
toilet -f term -F border --gay "Hola, soy s8m6n2o7a mucho gustov"
sleep 3
pkg install vim
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
cp .vimrc $HOME
mkdir ~/.vim/plug
toilet -f term -F border --gay "Mucho"
