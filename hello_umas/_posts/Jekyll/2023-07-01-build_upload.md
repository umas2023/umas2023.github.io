---
layout: post
title: 'jekyll: build_upload 打包上传脚本'
info: 用python写的，把build，commit，push三个命令放在一个脚本里，节省了3秒的生命
date: 2023-07-01 12:13:20  +0800
categories: ['jekyll', 'python']
toc: True
---


- 写代码用了3分钟
- 就是说这个脚本得至少跑60次才能回本

{% raw %}
```py
# 打包并上传Jekyll项目

commit_txt = "add new"

import os
import subprocess
import sys
script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)

print("\n===== jekyll build =====\n")
os.system("jekyll build --source hello_umas --destination docs")

print("\n===== push source =====\n")
subprocess.run(["git", "add", "."], cwd=".", shell=True)
subprocess.run(["git", "commit", "-m", commit_txt], cwd=".", shell=True)
subprocess.run(["git", "push"], cwd=".", shell=True)
```
{% endraw %}


- 好的，现在只需要一个脚本就可以打包上传修改了
- 至于为什么前面用os.system后面用subprocess，因为两段代码分别是从不同的脚本里拷过来的（所以只用了3分钟），两个命令在这里没什么区别