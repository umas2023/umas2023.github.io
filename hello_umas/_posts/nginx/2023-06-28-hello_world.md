---
layout: post
title:  "nginx: hello_world 点亮nginx服务器"
info: "nginx基本操作"
date:   2023-06-28 09:15:00 +0800
categories: nginx
toc: true
---

## 安装启动

- 安装
```
apt install nginx
```

- 配置
  - 默认配置文件 /etc/nginx/nginx.conf
    - 检查默认配置文件语法：nginx -t
  - 添加配置 /etc/nginx/conf.d/xxxx.conf
    - 此时需要在nginx.conf中http添加include，包含这个conf
    - 可以看到下面默认包含了

- 启动服务 
```
service nginx start
或：
nginx -s reload
```


## 可能出现的问题


> nginx: [error] invalid PID number "" in "/run/nginx.pid"

- 解决：

先运行
nginx -c /etc/nginx/nginx.conf

新增配置文件
nginx -c /etc/nginx/conf.d/iiir_frontend.conf 

再 nginx -s reload


> nginx: [warn] conflicting server name "iiir_test.local" on 0.0.0.0:8080, ignored

- 解决：

server_name冲突了
可能是nginx.conf里面include了两次，默认include了就不要再手动include


> nginx: [error] invalid PID number "" in "/run/nginx.pid"

- 解决：

- 先执行
nginx -c /etc/nginx/nginx.conf
- 再执行
nginx -s reload


> 网页访问403

- 解决：

可能的原因很多，用户名不匹配，修改nginx.conf中的user，改为和启动用户一致
user www-data; -> user root;