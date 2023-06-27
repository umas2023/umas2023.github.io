# bug记录


## nginx: [error] invalid PID number "" in "/run/nginx.pid"

- 解决：

先运行
nginx -c /etc/nginx/nginx.conf

新增配置文件
nginx -c /etc/nginx/conf.d/iiir_frontend.conf 

再 nginx -s reload

## nginx: [warn] conflicting server name "iiir_test.local" on 0.0.0.0:8080, ignored

- 解决：

server_name冲突了
可能是nginx.conf里面include了两次，默认include了就不要再手动include


## nginx: [error] invalid PID number "" in "/run/nginx.pid"

- 解决：

- 先执行
nginx -c /etc/nginx/nginx.conf
- 再执行
nginx -s reload


## 网页访问403

- 解决：

可能的原因很多，用户名不匹配，修改nginx.conf中的user，改为和启动用户一致
user www-data; -> user root;