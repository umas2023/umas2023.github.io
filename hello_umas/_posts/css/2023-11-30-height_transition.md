---
layout: post
title: 'css: height:auto的元素改变高度时适用transition'
info: '一个小技巧，用max-height'
date: 2023-11-30 13:12:22  +0800
categories: ['css']
toc: True
---


- 下面这个例子里height从auto改变到0时是不能触发transition: 0.5s的过渡动画的

{% raw %}
```css
div.block-body {
    height:auto;
    transition: 0.5s;
}

div.block-body.hide {
    height: 0;
    overflow: hidden;
}
```
{% endraw %}



- 一个小trick，用max-height替代height，设置一个很大的初值像这样：

{% raw %}
```css
div.block-body {
    transition: 0.5s;
    max-height: 1000px;
    overflow-y: auto;
}

div.block-body.hide {
    max-height: 0;
    overflow: hidden;
}
```
{% endraw %}

- 就可以有过渡动画效果了
- 但有一个小问题，实际上0.5s被分配给1000px~0px的变化过程中，但实际auto~0px会小于1000，页面上变化的视觉效果并不是0.5s，这个小技巧只适用于对动效精度要求不高的场合
- （不然就用js）



{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/css/2023-11-30-height_transition/image_1.jpg) -->