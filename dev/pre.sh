#!/usr/bin/env bash

set -ex

rm -rf home
mkdir -p home/.config/pip

unzip ../common/ohmyzsh-master.zip
mv ohmyzsh-master home/.oh-my-zsh

unzip ../common/zsh-syntax-highlighting-master.zip
mv zsh-syntax-highlighting-master home/zsh-syntax-highlighting

unzip ../common/zsh-autosuggestions-master.zip
mv zsh-autosuggestions-master home/zsh-autosuggestions

unzip ../common/gdb-python.zip
mv gdb-python home/.gdb-python

cp ../common/config/.vimrc \
   ../common/config/.gdbinit \
   ../common/config/.gitconfig \
   home/

cp ../common/config/pip.conf home/.config/pip/
