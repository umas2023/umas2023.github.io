---
layout: post
title: 'amtc: 本地前端部署'
info: 'nginx简化部署'
date: 2023-07-10 09:14:54  +0800
categories: ['amtc', 'nginx','raspberry_pi']
toc: True
---


## 网页打包

- 简化部署，树莓派上就不配置开发环境了
- 只把build完的dist文件夹放进去


## 配置nginx

- 安装

{% raw %}
```bash
apt install nginx
# 修改/etc/nginx/nginx.conf中的user
```
{% endraw %}


- 修改/etc/nginx/nginx.conf中的user为root
- 添加配置 /etc/nginx/conf.d/localfront.conf

```bash
# 一个简单的frontend.conf
server {
listen 4080;
server_name localfront; 
root /home/amtc/lf_localfront/lfdist;
index index.html;
}
```

- 启动服务

```bash
service nginx start
或：
nginx -s reload
查看状态：
service nginx status
```


## 设置开机自启

- 方法同上一页配置opcua时添加的后端

```bash
sudo vim /etc/systemd/system/start_localfront.service
```

- 写入以下内容

```bash
[Unit]
Description=Nginx HTTP Server
After=network.target

[Service]
Type=forking
ExecStart=/usr/sbin/nginx
ExecReload=/usr/sbin/nginx -s reload
ExecStop=/usr/sbin/nginx -s stop
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

- 控制
  
{% raw %}
```bash
# 启动服务
sudo systemctl enable start_localfront.service
# 查看状态
sudo systemctl status start_localfront.service
```
{% endraw %}


- 访问:192.168.1.101:4080

<!-- ![引入图片]({{site.url}}/image/amtc/2023-07-10-py_type/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
