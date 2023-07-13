---
layout: post
title: 'python: threading多线程'
info: '并行执行'
date: 2023-07-13 13:59:46  +0800
categories: ['python']
toc: True
---


- 基本写法

```py
import threading

def test_thread:
    # xxx
    pass

thread_hi = threading.Thread(target=test_thread)
thread_hello = threading.Thread(target=test_thread, args=('hello', 1))

thread_hi.start()
thread_hello.start()
```


- 多线程不能被ctrl+c中断，设置deamon参数使得子线程随主线程一起中断
- （即设置为守护进程，当程序仅剩守护进程时退出）

```py
th_shot = threading.Thread(target=shot_main)
th_sharpen = threading.Thread(target=sharpen_main)
th_shot.daemon = True
th_sharpen.daemon = True
th_sharpen.start()
th_shot.start()
while True:
if not sharpen_running:
    break
```
- 上面的代码实测无法完全同时运行，th2运行中会等待th1
- 没能实现这个功能



![引入图片]({{site.url}}/image/python/2023-07-13-threading/image_1.jpg)

{% raw %}
```
```
{% endraw %}
