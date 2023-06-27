# 树莓派安装docker

sudo curl -sSL https://get.docker.com | sh

docker -v 


- 开机启动
sudo systemctl enable docker 

- 手动启动

#重启 systemctl 守护进程
sudo systemctl daemon-reload
#开启 Docker 服务
sudo systemctl start docker