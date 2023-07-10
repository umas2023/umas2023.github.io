---
layout: post
title: 'electron: 打包改名改图标'
info: '研究了好久'
date: 2023-07-10 10:28:43  +0800
categories: ['electron']
toc: True
---

		
## 解决左上角图标不显示：
- 网上说是生成的ico文件格式不对
- 解决方法：改用png，像素还是256
- 新问题：左上角图标显示了一半（？？？）
- 改用png之后自动生成了dist/.icon-ico/icon.ico，有帖子说用这个ico，也不行
- 放大缩小重新生成了几次ico，问题没解决
- 第二天发现下面任务栏的图标也只显示一半了（？？？）
  
- 2022.8.28图标修好了
  - 正确的配置是在background.ts里设置图标，打包之后因为路径问题没有成功加载，像python脚本那样直接拷贝出来，区分开发环境和生产环境的路径

{% raw %}
```js
icon: process.env.NODE_ENV === "development" // 图标路径在打包之后不能识别，使用extraResources单独拷贝出来
? path.join(process.cwd(), "public/static/icon/mati_ei_256.ico")
: path.join(process.cwd(), "resources/static/icon/mati_ei_256.ico"),
```
{% endraw %}

   
- 之前可能是因为asar压缩导致只显示一半？Vue.config.js里的win.icon也要配置，这个是exe文件自己的图标
		
## 打包后左上角名称

- 尝试修改打包后的左上角名称也失败
- 方法1：直接在package.json中修改name，这个方法改中文会报错，而且不被推荐
- 方法2：require('electron').app.setName(name)
  - setName是官方文档中出现的方法
  - setName不管加在哪都不行，有时候可以看到启动瞬间名字被改掉了但马上就变回来
  - 参考了官方所有打包参数：
    - https://www.electron.build/configuration/configuration
    - 没有找到定义左上角name的键


- 把package.json的name删了，再使用setName就不会变了
- 后面buid时候会报错
- 2022.8.28改好了
- setName函数无论如何都会被刷掉，正确的修改方法是找到public/index.html

{% raw %}
```html
<title>电脑的配件</title>
```
{% endraw %}


- 这里的优先级是最高的




<!-- ![引入图片]({{site.url}}/image/electron/2023-07-10-build_icon/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
