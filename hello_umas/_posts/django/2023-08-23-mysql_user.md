---
layout: post
title: 'django: mysql数据库用户认证'
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








