#!bash

set -ex

mkdir -p home/apps/src

wget https://download.qemu.org/qemu-8.1.3.tar.xz
wget https://gitlab.com/qemu-project/libslirp/-/archive/v4.7.0/libslirp-v4.7.0.tar.gz
tar -xvf qemu-8.1.3.tar.xz -C home/apps/src
tar -xvf libslirp-v4.7.0.tar.gz -C home/apps/src

wget https://github.com/ohmyzsh/ohmyzsh/archive/refs/heads/master.zip -O ohmyzsh-master.zip
unzip ohmyzsh-master.zip
mv ohmyzsh-master home/.oh-my-zsh

wget https://github.com/zsh-users/zsh-syntax-highlighting/archive/refs/heads/master.zip -O zsh-syntax-highlighting-master.zip
unzip zsh-syntax-highlighting-master.zip
mv zsh-syntax-highlighting-master home/zsh-syntax-highlighting

wget https://github.com/zsh-users/zsh-autosuggestions/archive/refs/heads/master.zip -O zsh-autosuggestions-master.zip
unzip zsh-autosuggestions-master.zip
mv zsh-autosuggestions-master home/zsh-autosuggestions
