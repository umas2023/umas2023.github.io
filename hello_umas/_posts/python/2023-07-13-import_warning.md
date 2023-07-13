---
layout: post
title: 'python: vscode中import黄色波浪线报警'
info: '修复一个小问题'
date: 2023-07-13 14:12:11  +0800
categories: ['python', 'windows']
toc: True
---


![引入图片]({{site.url}}/image/python/2023-07-13-import_warning/image_1.png)

- 但是脚本能正常运行

- 左下角打开设置，搜索：

```
python analysis extra paths
```

![引入图片]({{site.url}}/image/python/2023-07-13-import_warning/image_2.png)

- 用pip show查找目标的path:`c:\python310\lib\site-packages`添加进去
