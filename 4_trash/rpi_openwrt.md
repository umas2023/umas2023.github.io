# 树莓派 + docker + openwrt

- 参考：
  - [树莓派3B+通过Docker安装OpenWrt旁路由流程详解_软件应用_什么值得买 (smzdm.com)](https://post.smzdm.com/p/agq6r58d/)
  - [[OpenWrt Wiki] OpenWrt as Docker container host](https://openwrt.org/docs/guide-user/virtualization/docker_host)
  - [Explore Docker's Container Image Repository | Docker Hub](https://hub.docker.com/search?q=openwrt)



- 发现应该靠谱的镜像
[sulinggg/openwrt - Docker Image | Docker Hub](https://hub.docker.com/r/sulinggg/openwrt)



https://mlapp.cn/376.html


- 拉取镜像
```
sudo docker pull sulinggg/openwrt
```

- 打开网卡混杂模式
sudo ip link set eth0 promisc on
打开成功后ifconfig可以看到promisc
eth0: flags=4355<UP,BROADCAST,PROMISC,MULTICAST>  mtu 1500


- 创建虚拟网络
sudo docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 macnet

- 删除这个网络
sudo docker network rm macnet

- 查看
sudo docker network ls




- 启动容器
sudo docker run --name openwrt --network macnet -it sulinggg/openwrt /bin/bash

sudo docker run --restart always --name openwrt -d --network macnet --privileged sulinggg/openwrt /sbin/init

- 或者后台启动
--restart always  -d
sudo docker exec -it openwrt /bin/bash 

- 退出后再次连接
sudo docker start openwrt
sudo docker exec -it openwrt /bin/bash 

- 停止容器
sudo docker stop openwrt

- 删除容器
sudo docker rm openwrt
sudo docker rm 3e3c1601fc7d



- 查看网络配置信息
sudo docker inspect openwrt


- 编辑网络
vim /etc/config/network 


config interface 'loopback'
        option ifname 'lo'
        option proto 'static'
        option ipaddr '127.0.0.1'
        option netmask '255.0.0.0'

config globals 'globals'

config interface 'lan'
        option type 'bridge'
        option ifname 'eth0'
        option proto 'static'
        option netmask '255.255.255.0'
        option ip6assign '60'
        option ipaddr '192.168.1.169'
        option gateway '192.168.1.1'
        option dns '192.168.1.169'

config interface 'vpn0'
        option ifname 'tun0'
        option proto 'none'





树莓派主机重启网络运行：
/etc/init.d/network restart

报错：
sudo: /etc/init.d/network: command not found

改用这个命令
sudo systemctl restart networking
sudo /etc/init.d/networking restart 



发现容器里没有网，路由器也ping不通
始终打不开openwrt管理页面




放弃