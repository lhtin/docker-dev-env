#!bash

set -ex

. ../dev/pre.sh

mkdir -p home/apps/src

if [ ! -f "qemu-8.1.3.tar.xz" ]; then
  wget https://download.qemu.org/qemu-8.1.3.tar.xz
fi
tar -xvf qemu-8.1.3.tar.xz -C home/apps/src

if [ ! -f "libslirp-v4.7.0.tar.gz" ]; then
  wget https://gitlab.com/qemu-project/libslirp/-/archive/v4.7.0/libslirp-v4.7.0.tar.gz
fi
tar -xvf libslirp-v4.7.0.tar.gz -C home/apps/src


