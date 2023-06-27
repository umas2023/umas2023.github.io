# docker基本操作

- [官方文档](https://docs.docker.com/)

- 下载镜像
```
docker pull ubuntu
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

- 进入容器shell
```
docker run -it ubuntu /bin/bash
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


- 进入后台容器
```
退出后容器停止:
docker attach [ID] 

退出后容器不停止:
docker exec -it [id] /bin/bash
```

- 启动/重启/停止
```
docker start/restart/stop [contaierID]
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















