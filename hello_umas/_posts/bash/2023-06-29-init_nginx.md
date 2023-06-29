---
layout: post
title:  "bash: init_nginx 一键部署nginx在ubuntu主机上"
info: "部署在ubuntu"
date:   2023-06-29 14:15:00 +0800
categories: bash
toc: true
---

- 简单介绍nginx
  - 略

- sh脚本

{% raw %}

```bash
#! /bin/bash


# ### - init_nginx [nginx静态页面服务器]
# - 脚本调用  
# ```./setup.sh```
# - 参数修改
#     - index.html文件位置：init_nginx/frontend.conf - server.root (line 12)
#     - 登录用户名：init_nginx.nginx.conf - user (line 1)
# - 注意
#     - 默认端口8080


# 切换工作目录
cd `dirname $0`

# 参数：端口
port=4080
# 参数：dist文件路径
# dist_path="/root/umasbox/frontend/dist"
dist_path="/mnt/d/s-linux/project/onebox/server_frontend/dist"

# 确认参数
echo -e "\nnginx port: $port"
echo -e "dist path: $dist_path\n\npress enter to continue..."
read -r input

# 创建.user_profile文件并写入.bashrc启动项
if [ ! -e ~/.user_profile ];then
    touch ~/.user_profile
else
    echo "user_profile already exist"
fi
if !( cat ~/.bashrc | grep "user_profile" > /dev/null );then
    echo -e "\necho 'setup command : ~/.user_profile'\n" >> ~/.bashrc
    echo -e "if [ -f ~/.user_profile ]; then\n\t. ~/.user_profile\nfi" >> ~/.bashrc
else
    echo "user_profile already loaded in bashrc"
fi

# 参数写入conf
if cat './frontend.conf' | grep "listen" > /dev/null ;then
    sed -i "/listen*/c\ \tlisten $port;" ./frontend.conf
fi
if cat './frontend.conf' | grep "root" > /dev/null ;then
    sed -i "/root*/c\ \troot $dist_path;" ./frontend.conf
fi

apt update
apt install nginx -y

cp frontend.conf /etc/nginx/conf.d/frontend.conf
cp nginx.conf /etc/nginx/nginx.conf

if !( cat '~/.user_profile' | grep "^service nginx start" > /dev/null );then
    echo "# user profile: nginx" >> ~/.user_profile
    echo "echo ' * nginx port $port starting ...'" >> ~/.user_profile
    echo "service nginx start" >> ~/.user_profile
fi

service nginx stop
nginx -c /etc/nginx/nginx.conf
nginx -s reload

echo -e "\nnginx setup finish\n"

```

{% endraw %}


- 考虑到版本区别，没有直接用脚本修改conf文件，而是用现有的conf文件直接覆盖
- nginx.conf
{% raw %}
```conf
user  root;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```
{% endraw %}


- frontend.conf
{% raw %}
```conf
# # 负载均衡（以后再研究）
# upstream test {
#     server localhost:8080;
#     server localhost:8081;
#     ip_hash; # 同一ip请求定向到同一后端
# }

# 静态网页
server {
    listen 4080;
    server_name box_server; # 这个名字不知道干啥用的
    root /mnt/d/s-linux/project/onebox/server_frontend/dist;
    index index.html;

    
    # 跨域转发
    
    # location ~ /cloudapi/ {
    #     # proxy_pass http://47.100.209.58:18080/api/; # 没加api也能访问成功？
    #     proxy_pass http://47.100.209.58:18080;
    # }

    location /cloudapi/ {
        proxy_pass http://47.100.209.58:18080/api/;
    }
    location /isesol/ {
        proxy_pass http://idis.isesol.com/;
    }
}

```
{% endraw %}






