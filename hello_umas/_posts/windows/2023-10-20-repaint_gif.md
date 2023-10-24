---
layout: post
title: 'windows: edge浏览器查看页面repaint'
info: '为后续优化页面回流做准备（附带一个好用的桌面gif录制工具）'
date: 2023-10-20 21:04:31  +0800
categories: ['windows', 'vue', 'zip_backyard']
toc: True
---


## gif录制

- 好用的工具：https://www.screentogif.com/


## edge检查页面回流情况

- f12添加rendering，页面里绿色部分是repaint，蓝色是shift（布局位移）


![引入图片]({{site.url}}/image/windows/2023-10-20-repaint_gif/image_1.gif)


- 可以看到左侧hover时所有元素都在重绘，帧数下降到30
- 后面尝试优化（首先打算用gpu加速的css属性试试（transform））

{% raw %}
```
```
{% endraw %}