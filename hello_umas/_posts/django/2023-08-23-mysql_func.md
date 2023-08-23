---
layout: post
title: 'django: mysql数据库增删改查基本操作'
info: '接上文mysql连接'
date: 2023-08-23 13:21:32  +0800
categories: ['django']
toc: True
---


## 准备

- mysql安装启动(ubuntu)

```bash
# 安装
apt install mysql-server mysql-client
# 查看初始密码
sudo cat /etc/mysql/debian.cnf
# 启动
sudo service mysql start
# 登录
mysql -u[用户名] -p[密码]
```

- 修改密码(sql)

```sql
ALTER USER 'root'@'localhost' IDENTIFIED  BY '123456';
flush privileges;
quit; 
```

- 创建数据库(sql)

```sql
create database ubk default charset=utf8;
```






## 创建一个带用户认证的model


- 新增一个app

```bash
python manage.py startapp app_model
```

- settings.py中添加这个app

```py
INSTALLED_APPS = [
    ***
    'app_model'
]
```

- 在 @/app_model/models.py中添加数据模型

```py
from django.db import models

from django.contrib.auth.models import User
from django.db.models import JSONField

# 类名ModelRec对应数据库中的Tabel名是app_model_modelrec

class ModelRec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, default='date')
    amount = models.CharField(max_length=100, default='amount')
    commit = models.CharField(max_length=100, default='commit')
    tag = models.CharField(max_length=100, default='tag')
```


- 迁移数据库（django）

```bash
python manage.py makemigrations
python manage.py migrate

# 如果对model进行了大量修改导致migrate冲突，可以把数据库Tables内所有表全部删除后重新migrate
```


## 新增用户的一个示例app


```py
from django.http import HttpResponse

from app_model.models import ModelRec
from django.contrib.auth.models import User

import json

def add_user(request):
    '''basic response test'''
    data = json.loads(request.body.decode('utf-8'))
    user_name = data['user_name']
    password = data['password']
    print(data)

    if User.objects.filter(username=user_name).exists():
        return HttpResponse("User already exists.")

    user = User.objects.create(username = user_name)
    user.set_password(password)
    user.save()
    
    return HttpResponse("Success.")
```

- postman发送请求；在body中添加json

```
{
    "user_name":"admin",
    "password":"1234"
}
```

- 新增的用户可以在数据库Tabels/auth_user中看到



## 添加数据的一个示例app


```py

from django.http import HttpResponse

from app_model.models import ModelRec
from django.contrib.auth.models import User

import json


def add_data(request):
    '''basic response test'''
    data = json.loads(request.body.decode('utf-8'))
    user_name = data['user_name']
    date = data['date']
    amount = data['amount']
    commit = data['commit']
    tag = data['tag']

    print(data)

    user_id = User.objects.get(username=user_name)

    new_object = ModelRec(user=user_id, date=date, amount=amount, commit=commit, tag=tag)
    new_object.save()

    return HttpResponse("Hello world ")

```


- postman发送请求；在body中添加json

```
{
    "user_name":"admin",
    "date":"20230823",
    "amount":"7225",
    "commit":"api test",
    "tag":"test"
}
```

- 新增的用户可以在数据库Tabels/app_model_modelrec中看到


