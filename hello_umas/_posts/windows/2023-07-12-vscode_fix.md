---
layout: post
title: 'windows: vscode连接不上'
info: '卡在Setting up SSH Host XX:Copying VS Code Server to host with scp'
date: 2023-07-12 23:14:59  +0800
categories: ['windows']
toc: True
---

- 今天连不上寝室的树莓派了
- 终端可以用ssh登陆上
- vscode卡在Setting up SSH Host umas-rpi: Copying VS Code Server to host with scp
- 把失败的那个文件手动下载下来就好了

```bash
ls .vscode-server/bin/
# 记下返回的commit_id
660393deaaa6d1996740ff4880f1bad43768c814
```

- 删掉下载一半的东西

```bash
rm -rf .vscode-server/bin/*
```

- 手动下载这个包，wget或者scp

```
https://update.code.visualstudio.com/commit:660393deaaa6d1996740ff4880f1bad43768c814/server-linux-x64/stable 
```

- 发现wget下载不下来，然后问题找到了，之前配置clash的时候全局代理到了7890端口，没有启动clash的时候就会报错Could not connect to 127.0.0.1:7890 (127.0.0.1). - connect (111: Connection refused)
- 把/etc/environment改回来就好了



- 那就不下载vscode更新包了，如果后面再碰到这个问题再回头补充，反正百度一下就能找到

