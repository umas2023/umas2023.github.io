---
layout: post
title: 'django: 用户认证'
info: '接上文mysql增删改查'
date: 2023-08-23 14:21:32  +0800
categories: ['django']
toc: True
---

## 验证用户的一个例子


```py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            response_data = {'token': "generated_token"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

```

- postman发送请求时在body里选择"x-www-form-urlencoded"并添加key
- (因为使用postman时csrf报错不知道怎么解决所以在settings的MIDDLEWARE里先禁用了)
- 前端axios数据发送时data字段使用qs.stringify而不是JSON.stringify，前者用于构造 URL 查询字符串
```js
// npm i -s qs
// import qs from 'qs';
inputData: qs.stringify({
            "username":username,
            "password":password
        })
// 结果："username=user123&password=pass456"
```



## 部分官方文档搬运

- 参考：
  - https://docs.djangoproject.com/en/4.2/topics/auth/default/


- 创建用户

```py
from django.contrib.auth.models import User
user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
user.last_name = "Lennon"
ser.save()
```

- 创建super用户

```
python manage.py createsuperuser --username=joe --email=joe@example.com
```

- 修改密码

```py
from django.contrib.auth.models import User
u = User.objects.get(username="john")
u.set_password("new password")
u.save()
```


- 身份验证

```py
from django.contrib.auth import authenticate

user = authenticate(username="john", password="secret")
if user is not None:
    # A backend authenticated the credentials
    ...
else:
    # No backend authenticated the credentials
    ...
```


- 权限和用户组
  - 略，参见官方文档


- 登录

```py
from django.contrib.auth import authenticate, login


def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
```


- 注销

```py
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

- 使用装饰器来限制仅登录用户访问

```py
from django.contrib.auth.decorators import login_required

@login_required
def xxx ...
```


- 可能会报错RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods

```
pip install cryptography
```




