---
layout: post
title: 'css: 保持宽高比的简单方法'
info: '虽然使用padding+height可以实现，但有更简单的方法'
date: 2023-09-20 18:52:11  +0800
categories: ['css']
toc: True
---


- 设置height=0后用padding-bottom控制比例

{% raw %}
```html
<div class="box2-out">
    <div class="box2-in">aspect-ratio</div>
</div>
```
{% endraw %}


{% raw %}
```css
div.box2-out {
    width: 30%;
    height: 0;
    margin: 10px;
    position: relative;
    padding-bottom: 15%;
    border: solid 1px red;
}
div.box2-in{
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0; // height: 100%
    right: 0; // width: 100%
    background-color: aqua;
}
```
{% endraw %}


- 也可以直接用aspect-ratio属性控制


{% raw %}
```html
<div class="box1">aspect-ratio</div>
```
{% endraw %}


{% raw %}
```css
div.box1 {
    width: 30%;
    background-color: aqua;
    margin: 10px;
    aspect-ratio: 16/9;
}

```
{% endraw %}

<!-- ![引入图片]({{site.url}}/image/css/2023-09-20-aspect_ratio/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
