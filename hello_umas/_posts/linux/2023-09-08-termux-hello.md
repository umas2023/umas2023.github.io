---
layout: post
title: 'termux: hello world'
info: 'termux基操'
date: 2023-09-08 10:16:49  +0800
categories: ['linux']
toc: True
---


## 基本命令

- termux-change-repo
  - 换源，空格键选中
- termux-setup-storage
  - 创建storage文件夹，直接访问手机文件
- pkg install vim
  - 有时候apt可能不好用，改为pkg
- ssh远程
  - 实测termux里面的ubuntu的ssh服务启不起来，只能先ssh进termux再进ubuntu
  - 更新：termux和ubuntu共用8022端口，不能同时开ssh，把termux的ssh关了就可以开ubuntu的ssh了
  - pkg install openssh
  - 看我是谁：whoami
  - 设置密码：passwd
  - 启动服务：sshd
  - 电脑连接端口是8022：ssh u0_a153@192.168.1.109 -p 8022
  - mate10用户名u0_a243
  - nova9用户名u0_a282
  - matepad用户名u0_a153
  - 记得把vpn都退了不然一直timeout，md查了好久居然是因为这个


- termux调用摄像头，参考：https://zhuanlan.zhihu.com/p/381044910


## 安装ubuntu

- 安装ubuntu
	- 安装工具：pkg install proot-distro
	- 记得先pkg update一下
	- 查看可安装版本：proot-distro list
	- 安装：proot-distro install ubuntu
	- 登录：proot-distro login ubuntu
	- 文件：termux启用storage之后，Ubuntu中 /sdcard 目录即为手机存储
- termux设置默认进入ubuntu：
	- 新建.profile
	- 加入登录命令
		
- 手机文件在/sdcard目录下
		
- 安装code－server
	- curl -fsSL https://code-server.dev/install.sh | sh
	- 挂梯子↑
	- code-server
	- cat .config/code-server/config.yaml
	- 把密码记住
	- fe2bee81b0fa36545baec7ad
	- 浏览器访问127.0.0.1:8080
	- 输完密码黑屏/白屏换个浏览器，安卓edge可行chrome不行
	- 密码替换：sed -i "/^passwd=*/cpasswd=666" config.yaml









{% raw %}
```
```
{% endraw %}
