---
layout: post
title:  "docker: hello_world 基础操作"
info: "docker基础操作"
date:   2023-06-27 22:50:00 +0800
categories: docker
toc: true
---

## 参考
- [官方文档](https://docs.docker.com/)


## 基本命令

- 下载镜像
```
docker pull ubuntu
docker pull ubuntu:22.04
```

- 推送本地镜像
```
docker push
```

- 检查镜像信息
```
docker image ls
```

- 检查容器信息
```
docker container ls (-a)
docker ps (-a)
```

- 启动新容器并进入shell
```
docker run --name my_ubuntu -it ubuntu /bin/bash
exit退出
```

- docker run 参数
  - -i :  以交互模式运行容器，通常与 -t 同时使用
  - -t : 分配一个伪输入终端，一般与 -i 连用
  - -d : 后台运行容器，并返回容器ID
  - -p : 指定端口映射 -p 18080:80
  - -P : 随机端口映射，容器内部端口随机映射到主机的端口
  - --name="nginx-lb" : 为容器指定一个名称
  - --dns 8.8.8.8 : 指定容器使用的DNS服务器，默认和宿主一致
  - -h "mars" : 指定容器的hostname
  - -e username="ritchie" : 设置环境变量
  - --dns-search example.com : 指定容器DNS搜索域名，默认和宿主一致
  - -a stdin : 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项
  - --net="bridge": 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型
  - -m : 设置容器使用内存最大值


- 后台启动新容器
```
sudo docker run --restart always --name openwrt -itd sulinggg/openwrt /sbin/init
docker run -p 44080:4080 -p 44090:4090 --restart=always --name amtc_ubuntu -itd ubuntu:22.04 /bin/bash
```

- 启动已存在的容器
```
sudo docker start openwrt
```

- 进入后台容器（退出后容器停止）  
```
docker attach [ID] 
```

- 进入后台容器（退出后容器不停止）（常用）  
```
docker exec -it [id/name] /bin/bash
```

- 启动/重启/停止
```
docker start/restart/stop [contaierID]
```

- 删除容器
```
docker rm [id/name]
```

- 启动示例: iiir
```
docker run -p 13306:3306 --name mysql-iiir --restart=always \
-v  /home/iiir/mysql/conf.d:/etc/mysql/conf.d \
-v  /home/iiir/mysql/logs:/var/log/mysql \
-v  /home/iiir/mysql/data:/var/lib/mysql  \
-e MYSQL_ROOT_PASSWORD="iiirmysql" \
-h mysql-iiir \
--net mynet \
-d biarms/mysql:5.7.30-linux-arm64v8
```


## 增加端口映射（桌面）

- （命令行的操作后面有空再说）
- 比如有了一个amtc_ubuntu，run的时候忘记映射22端口
- 先把容器停掉
- 文件资源管理器访问：

```
\\wsl.localhost\docker-desktop-data\data\docker\containers
```

- 找到里面的hostconfig.json，里面可以配置端口映射

```json
"PortBindings": {
    "22/tcp": [
        {
            "HostIp": "",
            "HostPort": "44022"
        }
    ],
    "4080/tcp": [
        {
            "HostIp": "",
            "HostPort": "44080"
        }
    ],
    "4090/tcp": [
        {
            "HostIp": "",
            "HostPort": "44090"
        }
    ]
},
```

- 同时要修改同目录下的config.v2.json

```json
"ExposedPorts": {
    "22/tcp": {},
    "4080/tcp": {},
    "4090/tcp": {}
},
```

- 重新docker desktop

## dockerfile

- 一个例子

```dockerfile
FROM ubuntu:
MAINTAINER umas 1970313791@qq.com
LABEL version="1.0" description="umas个人测试镜像" by="umas "

RUN apt-get update \
&& apt-get install --no-install-recommends -y \
make \
build-essential \
openssh-server \
vim \
net-tools

RUN echo "root:umas1970" | chpasswd

EXPOSE 22 80 8080 8081 8082 8083 8084 8085

RUN echo "PermitRootLogin yes"        >> /etc/ssh/sshd_config \
&& echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config \
&& ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa \
&& /etc/init.d/ssh start 

CMD ["sh", "-c", "/etc/init.d/ssh start"]
```


## 可能出现的问题

- docker启动失败(2022.2.20)
- 报错：windows平台Docker Desktop failed to start…
- 原因：梯子和docker冲突
- 解决：
  - （检查wsl是否可以启动）
  - 删除文件夹C:\Users\umas2017\AppData\Roaming\Docker
  - 重新启动













