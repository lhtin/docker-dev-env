#!bash

set -ex

rm -rf home
mkdir -p home

unzip ../common/ohmyzsh-master.zip
mv ohmyzsh-master home/.oh-my-zsh

unzip ../common/zsh-syntax-highlighting-master.zip
mv zsh-syntax-highlighting-master home/zsh-syntax-highlighting

unzip ../common/zsh-autosuggestions-master.zip
mv zsh-autosuggestions-master home/zsh-autosuggestions
