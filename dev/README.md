```
# 构建镜像
./build.py --image-name test-image-tintin --build-dir . 

# 启动镜像（以Daemon的形式运行在后台）
./run.py --image-name test-image-tintin --ssh-port 2222

# 使用SSH登录该镜像
ssh docker@localhost -p 2222
```
