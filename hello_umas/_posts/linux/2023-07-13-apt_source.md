---
layout: post
title: 'linux: apt改国内源'
info: '改源加速下载'
date: 2023-07-13 14:33:32  +0800
categories: ['linux']
toc: True
---


- 这里可以找到源：
  - 阿里源：https://developer.aliyun.com/mirror/
  - 清华源：https://mirrors.tuna.tsinghua.edu.cn/
  - 华科源：http://mirrors.ustc.edu.cn/
  - 网易源：http://mirrors.163.com/


- 查看linux版本

```bash
cat /etc/issue
# 返回
Debian GNU/Linux 11 \n \l
```

- debian换国内源，修改/etc/apt/sources.list文件

```bash
sed -i "s@http://deb.debian.org@https://mirrors.163.com@g" /etc/apt/sources.list
```


- 补充ubuntu改源


- 备份原文件

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
vim /etc/apt/sources.list
```

```
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
```

- 更新软件列表

```
apt update
```



<!-- ![引入图片]({{site.url}}/image/linux/2023-07-13-apt_source/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
