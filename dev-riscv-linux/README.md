# RISC-V Ubuntu虚拟机使用指南

> https://wiki.ubuntu.com/RISC-V/QEMU

## 使用原始的img进行初始化

1. 构建镜像：`./build.sh`
2. 启动RISC-V Ubuntu服务器：`docker run -it --publish 127.0.0.1:2223:2223/tcp -v /work/home/lding/docker:/work/home/lding/docker riscv-ubuntu-lding python3 ~/run.py --img /work/home/lding/docker/imgs/ubuntu-23.10-preinstalled-server-riscv64.img --ssh-port 2223 --cpu 64 --memory 32G`
   1. 这里的cpu核数指定了之后就不能再修改
   2. 登录（默认账号密码：ubuntu:ubuntu，第一次登录需要修改）
   3. 修改密码为1：`echo "ubuntu:1" | sudo chpasswd`
   4. 切换到清华镜像：https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu-ports
      1. 23.10版本的/etc/apt/sources.list改为如下内容（mantic是23.10的代号，这个需要跟你的发行版本匹配）                ：
         ```
         deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ mantic main restricted universe multiverse
         deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ mantic-updates main restricted universe          multiverse
         deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ mantic-backports main restricted universe          multiverse

         deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ mantic-security main restricted universe          multiverse
         ```
   5. `sudo apt-get update && sudo apt-get upgrade -y`
   6. `sudo apt install zsh gcc g++ build-essential libmpc-dev libmpfr-dev libgmp-dev`
   7. 安装Oh My Zsh
      ```
      sh -c "$(curl -fsSL https://gitlab.com/lhtin-rivai/ohmyzsh/-/raw/master/tools/install.sh)"
      git clone https://gitlab.com/lhtin-rivai/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
      git clone https://gitlab.com/lhtin-rivai/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
      sed -i -E "s/plugins=\(git\)/plugins=\(zsh-autosuggestions zsh-syntax-highlighting\)/" ~/.zshrc
      ```
   8. 启动 SSH Server：`sudo systemctl enable ssh`
3. 验证下ssh登录：`ssh ubuntu@localhost -p 2223` 密码1

## 使用初始化好的img

1. 构建镜像：`./build.sh`
2. 解压一个始化好了的镜像：`unzip -n ubuntu-23.10-preinstalled-server-riscv64.img.zip`
3. 启动RISC-V Ubuntu服务器：`docker run -d --publish 127.0.0.1:2223:2223/tcp -v /work/home/lding/docker:/work/home/lding/docker riscv-ubuntu-lding python3 ~/run.py --img /work/home/lding/docker/imgs/ubuntu-23.10-preinstalled-server-riscv64.img --ssh-port 2223 --cpu 64 --memory 32G`
   1. `-d` 表示在后台执行
   2. 也可以用在tmux里面用`-it`，这样可以看到输出
4. ssh登录：`ssh ubuntu@localhost -p 2223` 密码1
5. 如果img容量不够可以进行扩容：`qemu-img resize -f raw ubuntu-23.10-preinstalled-server-riscv64.img +10G`

