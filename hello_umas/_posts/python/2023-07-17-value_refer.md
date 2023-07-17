---
layout: post
title: 'python: 传值调用、传引用调用'
info: 'call by value / call by reference'
date: 2023-07-17 14:01:41  +0800
categories: ['python']
toc: True
---

- 在 Python 中，参数传递的方式分为传值调用和传引用调用两种方式。

- 对于不可变对象，如数字、字符串、元组等，Python 采用的是传值调用的方式。这意味着，在将这些对象作为参数传递给函数或方法时，其实是将对象的值复制一份传递给了函数或方法，而不是对象本身。因此，在函数或方法内部修改参数的值，不会影响到原始对象。

- 对于可变对象，如列表、字典等，则采用的是传引用调用的方式。这意味着，在将这些对象作为参数传递给函数或方法时，其实是将对象的引用（即指向对象的内存地址）传递给了函数或方法。因此，在函数或方法内部修改参数的值，将会影响到原始对象。

- 例子：

{% raw %}
```py
class AutoPlay():
    def __init__(self, url="", stop_flag=False) -> None:
        ...

    def auto_run(self) -> None:
        i=0
        while True:
            i+=1
            print(i)
            time.sleep(self.INTERVAL)
            if self.stop_flag:
                break

# 调用：
stop_flag = False
AutoPlay(url="", stop_flag=stop_flag).auto_run_th()

time.sleep(3)
stop_flag = True
```
{% endraw %}

- 以上程序不会在3秒后停下
- 要想实现外部控制程序停止，可以改成数组（call by reference）

{% raw %}
```py
stop_flag = [False]
stop_flag[0] = True
```
{% endraw %}
