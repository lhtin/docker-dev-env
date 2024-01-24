```
# 准备环境（包括zsh、gdb、vim、git等配置）
./pre.sh

# 构建镜像
./build.py --image-name my-dev --build-dir . 

# 启动镜像（以Daemon的形式运行在后台）
./run.py --image-name my-dev --volume ~/.zsh_history ~/your/project --ssh-port 2222

# 使用SSH登录该镜像
ssh docker@localhost -p 2222
```
