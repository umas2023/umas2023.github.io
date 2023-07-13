---
layout: post
title: 'python: 程序时间'
info: '三种时间：time.time、time.process_time、datetime.now'
date: 2023-07-13 12:47:00  +0800
categories: ['python']
toc: True
---


- time.time是程序时间
  - 返回：2.2061703205108643

```py
start = time.time()
time.sleep(2.2)
end = time.time()
print (end-start)
```

- time.process_time是cpu占用时间
  - 如time.sleep的等待时间是不会记录在内的
    - 返回：0.0

```py
import time
start = time.process_time()
time.sleep(2.2)
end = time.process_time()
print (end-start)
```


- datetime.datetime.now给出格式化时间
- 返回：0:00:02.209129

```py
import time
import datetime
start = datetime.datetime.now()
time.sleep(2.2)
end = datetime.datetime.now()
print (end-start)
```
