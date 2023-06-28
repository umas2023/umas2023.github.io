---
layout: post
title:  "python: subprocess 多线程函数"
info: "python多线程函数subprocess"
date:   2023-06-28 09:22:00 +0800
categories: python
toc: true
---

- 一个例子
```python
subprocess.run(["npm", "run", "electron:serve"], cwd="./desktop_electron", stdout=subprocess.PIPE,shell=True)
```
- 其中cwd指定程序运行的位置,  
- shell=True使用与在命令提示符中相同的shell来运行命令,否则会找不到npm命令
- stdout=subprocess.PIPE 表示子进程的标准输出将被捕获,不设置的默认情况下子进程的输出将直接发送到控制台窗口,使用result = subprocess.run(...),print(result.stdout)可以获取捕获的输出
- 上面的程序会等待subprocess运行结束之后再继续,而os.system()不会等待





