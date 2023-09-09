---
layout: post
title: 'windows: powershell基操'
info: '记录用到的基本命令，持续更新'
date: 2022-01-11 23:14:59  +0800
categories: ['windows',"powershell"]
toc: True
---


## 常用命令

- echo的换行是``` `n (左上角反撇)```


## 安装帮助

- 命令：```Update-Help```
- 之后可以用man查看命令手册
- 也可以查看示例：get-help  command -examples


## 像bashrc一样添加powershell的启动脚本

- 查看当前用户的profile：```$profile```，如果返回的路径不能打开的话需要自己手动创建
- 在路径下创建profile.ps1，比如我的路径是```C:\Users\umas\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1```
- 可能出现的错误：无法加载文件 xxx 因为在此系统上禁止运行脚本；解决方法：管理员身份运行：```set-executionpolicy remotesigned```


## 像alias一样定义别名

- 预先定义在profile里的一个例子

```powershell
echo "load user profile from C:\Users\umas2\Documents\WindowsPowerShell\profile.ps1"

function cdbox_function {cd D:\s-linux\project\box_v0.1}
Set-Alias -Name cdbox -value cdbox_function
		
echo "user alias: cdbox `n"

```

