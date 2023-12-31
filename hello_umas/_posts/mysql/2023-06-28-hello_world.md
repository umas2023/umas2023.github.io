---
layout: post
title:  "mysql: hello_world 基本操作"
info: "mysql基本操作"
date:   2023-06-28 09:10:00 +0800
categories: mysql
toc: true
---



## ubuntu安装
```
sudo apt install mysql-server mysql-client
mysql --version
```

## 用户密码设置
- 查看默认用户密码
```
 sudo cat /etc/mysql/debian.cnf
```

- 登入（先启动）
```
mysql -u用户名 -p密码
```

- 重置用户密码
```
（登入）
use mysql;
update mysql.user set authentication_string=password('123456') where user='root' and Host ='localhost'; 
update user set  plugin="mysql_native_password";     
flush privileges;
quit; 
（重新登入）
mysql -uroot -p123456
```
- 新版
```
ALTER USER 'root'@'localhost' IDENTIFIED  BY '123456';
flush privileges;
quit; 
```

## 启动/关闭/重启mysql
```
启动mysql：
sudo /etc/init.d/mysql start
或
sudo service mysql start
停止mysql：
sudo /etc/init.d/mysql stop
或
sudo service mysql stop
重启mysql：
sudo/etc/init.d/mysql restart
或
sudo service mysql restart
```

## 基本操作

- 创建数据库
```
create database 数据库名称 default charset=utf8; # 防止编码问题，指定为 utf8
create database iiir_fullstack default charset=utf8;
```

- 查看数据库

```
SHOW DATABASES;
```


- 新建用户(略)



- 为用户umas添加访问数据库ubk的权限

```sql
GRANT ALL PRIVILEGES ON ubk.* TO 'umas'@'localhost';
FLUSH PRIVILEGES;
```