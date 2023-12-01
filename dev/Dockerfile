# riscv64
# FROM riscv64/ubuntu:23.04
# RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
# COPY tsinghua-ubuntu-23.04-port-sources.list /etc/apt/sources.list

# x86
FROM ubuntu:23.10
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY tsinghua-ubuntu-23.10-sources.list /etc/apt/sources.list

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y autoconf automake autotools-dev curl python3 python3-pip python-is-python3 \
                       libmpc-dev libmpfr-dev libgmp-dev gawk build-essential \
                       bison flex texinfo gperf libtool patchutils bc zlib1g-dev \
                       libexpat-dev ninja-build git cmake libglib2.0-dev libpixman-1-dev \
                       expect
RUN apt-get install -y zsh wget sudo vim openssh-server openssh-client

ARG DOCKER_USER_ID=10000
ARG DOCKER_USER_NAME=dev1
ARG DOCKER_GROUP_ID=1000
ARG DOCKER_GROUP_NAME=dev
ARG DOCKER_HOME_DIR=/home/dev1

# 23.10 will add default no-root user ubuntu which use 1000 user id, remove the default user
RUN userdel -r ubuntu || true
RUN echo "Create dev user: ${DOCKER_USER_NAME}(${DOCKER_USER_ID}) ${DOCKER_GROUP_NAME}(${DOCKER_GROUP_ID})"
RUN groupadd -f -g ${DOCKER_GROUP_ID} ${DOCKER_GROUP_NAME}
RUN useradd -s /usr/bin/zsh -d ${DOCKER_HOME_DIR} -u ${DOCKER_USER_ID} -g ${DOCKER_GROUP_ID} ${DOCKER_USER_NAME}
# add user to sudo group
RUN usermod -aG sudo ${DOCKER_USER_NAME}

# set root and user password to 1
RUN echo "root:1" | chpasswd
RUN echo "${DOCKER_USER_NAME}:1" | chpasswd

# create user home dir
RUN mkdir -p ${DOCKER_HOME_DIR}
RUN chown ${DOCKER_USER_NAME}:${DOCKER_GROUP_NAME} ${DOCKER_HOME_DIR}

USER ${DOCKER_USER_NAME}

COPY --chown=${DOCKER_USER_NAME}:${DOCKER_GROUP_NAME} home ${DOCKER_HOME_DIR}

# installing zsh
RUN cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
RUN mv ~/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
RUN mv ~/zsh-syntax-highlighting ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
RUN sed -i -E "s/plugins=\(git\)/plugins=\(git zsh-autosuggestions zsh-syntax-highlighting\)/" ~/.zshrc
RUN echo "1" | sudo -S chsh -s $(which zsh)

# modify pip3 source
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# start ssh server
RUN ssh-keygen -A
CMD echo "1" | sudo -S sshd -D -e
