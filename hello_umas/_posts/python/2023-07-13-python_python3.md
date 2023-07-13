---
layout: post
title: 'python: python指向python3'
info: '老版的linux会有python2和python3两个命令，但是没有python命令'
date: 2023-07-13 14:31:35  +0800
categories: ['python']
toc: True
---

- 在.bashrc中`alias python=python3`可以解决一部分问题

- 根源上解决

{% raw %}
```bash
mv /usr/bin/python /usr/bin/python.bak
 
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo ln -s /usr/bin/pip3 /usr/bin/pip
```
{% endraw %}



- 也可以试试这个

```bash
apt install python-is-python3
```


<!-- ![引入图片]({{site.url}}/image/python/2023-07-13-python_python3/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
