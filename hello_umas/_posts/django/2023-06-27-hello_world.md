---
layout: post
title:  "django: hello_world 创建一个django后端（包含websocket）"
info: "土木工程都能看懂的django hello_world"
date:   2023-06-27 22:25:00 +0800
categories: django
toc: true
---



## 一个简单app

- 创建项目
```
django-admin.exe startproject hello_world
```

- 启动项目(migrate只需要运行一次)  
```
python manage.py migrate
python ./manage.py runserver 0.0.0.0:4090
``` 
可以看到后端已经成功运行了

- 添加app
```
python manage.py startapp say_hello
```

- app添加views: say_hello/views.py
```python
from django.http import HttpResponse
def say_hello(request):
    '''basic response test'''
    print("request:")
    print(request.body)
    return HttpResponse("Hello world ")
```

- app添加urls: say_hello/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [
    path("say_hello",views.say_hello),
]
```

- 全局添加urls: hello_world/urls.py
```python
from django.conf.urls import include
urlpatterns = [
    path(r'',include("say_hello.urls"))
]
```

- 好了,现在可以用postman试着给localhost:4090/say_hello发送一个get请求,会收到"hello world"的回复


## 添加websocket应用
- 参考：[channels官方文档](https://channels.readthedocs.io/en/stable/tutorial/part_1.html)

- 安装必备库
```python
pip install channels
pip install daphne
```

- 创建app
```
python manage.py startapp hello_ws
```

- 在hello_world/settings.py添加设置,注意daphne要写在最上面,这一步配置完毕后启动服务器可以看到终端输出ASGI/Daphne版本号
```python
INSTALLED_APPS = [
    'daphne',
    'hello_ws',
    '...',
]
ASGI_APPLICATION = 'hello_world.asgi.application'
```

- app添加views: hello_ws/views.py
```python
from channels.generic.websocket import WebsocketConsumer
class WebsocketTest(WebsocketConsumer):
    '''websocket test'''
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        pass
    def receive(self, text_data):
        print(text_data)
        for i in range(10):
            self.send(str(i))
```

- app添加urls: hello_ws/urls.py
```python
from django.urls import path
from . import views
websocket_urlpatterns = [path("hello_ws",views.WebsocketTest.as_asgi())]
```

- 全局添加asgi: hello_world/asgi.py

```python
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello_world.settings")
django_asgi_app = get_asgi_application()

import hello_ws.urls

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(URLRouter(
        hello_ws.urls.websocket_urlpatterns
    ))
})
```

- 好了,现在可以用postman试着给localhost:4090/hello_ws发送一个websocket请求;postman创建websocket请求需要点击左上角My Workspace右边的new;点击connect按钮后发送任意消息,可以收到后端返回的1~9
  
- 如果返回403说明请求被跨域拦截,可以在hello_world/settings.py中直接允许所有跨域请求：
```
ALLOWED_HOSTS = ['*']
```

- 如果路径或类名写错,可能会报错Cannot import ASGI_APPLICATION module,可以启用shell调试模式debug  
```python 
manage.py shell 
from py_server.asgi import application
```




