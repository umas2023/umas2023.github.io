---
layout: post
title:  "python: virtualenv"
info: "python虚拟环境管理工具virtualenv"
date:   2023-06-28 09:25:00 +0800
categories: python
toc: true
---



- 在一台计算机上管理多个不同版本项目时使用虚拟环境非常有必要

- python虚拟环境管理工具常用的有virtualenv和venv, 推荐使用virtualenv，可以指定python版本

- 可以通过以下命令在操作系统上来安装和查看virtualenv (需要先安装好python3解释器) 
```
windows:
安装: pip3 install virtualenv
查看: pip3 show virtualenv 
```
```
linux:
安装: apt install python3-virtualenv
查看: apt show python3-virtualenv 
```

- 可以通过以下命令来创建虚拟环境 / 激活虚拟环境 / 退出虚拟环境 / 删除虚拟环境。 
```
linux:
创建: virtualenv -p python3.X env 
激活: source env/bin/activate 
退出: deactivate 
删除: rm -rf env/
```
```
windows:
创建: virtualenv -p python3.X env 
激活: env/bin/activate 
退出: deactivate 
删除: rm -rf env/
```

- 脚本中的os.system和subprocess函数无法指定虚拟环境, 如果想在脚本中直接调用虚拟环境的python,可以定位到
```
env/Script/python.exe
env/Script/pip.exe
```



