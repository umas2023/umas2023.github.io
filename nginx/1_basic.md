# nginx

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