#!bash

set -ex

rm -rf home
mkdir -p home/apps/src

wget https://download.qemu.org/qemu-8.1.3.tar.xz
wget https://gitlab.com/qemu-project/libslirp/-/archive/v4.7.0/libslirp-v4.7.0.tar.gz
tar -xvf qemu-8.1.3.tar.xz -C home/apps/src
tar -xvf libslirp-v4.7.0.tar.gz -C home/apps/src

unzip ../common/ohmyzsh-master.zip
mv ohmyzsh-master home/.oh-my-zsh

unzip ../common/zsh-syntax-highlighting-master.zip
mv zsh-syntax-highlighting-master home/zsh-syntax-highlighting

unzip ../common/zsh-autosuggestions-master.zip
mv zsh-autosuggestions-master home/zsh-autosuggestions
