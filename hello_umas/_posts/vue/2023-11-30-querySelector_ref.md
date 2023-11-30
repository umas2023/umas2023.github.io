---
layout: post
title: 'vue: ref替代querySelector'
info: '如果父组件中渲染了多个子组件，子组件中用querySelector只能选中第一个'
date: 2023-11-30 14:23:09  +0800
categories: ['vue', 'js']
toc: True
---


- 这样一个场景
- 子组件CollapseBlock中用querySelector选中div后修改了属性

{% raw %}
```html
<div id="header-arrow" style="margin-left: 5px;">
```
{% endraw %}

{% raw %}
```js
let arrow_element = (document.querySelector("#header-arrow") as HTMLElement)
arrow_element.style.transform = "rotate(90deg)"
...
```
{% endraw %}

- 父组件中用v-for循环了多个子组件，发现被修改的属性始终只有循环第一个元素，因为document.querySelector默认在整个dom中查找



- 可以用vue的ref替代


{% raw %}
```html
<div id="header-arrow" ref="arrow_element" style="margin-left: 5px;">
```
{% endraw %}


{% raw %}
```js
const arrow_element = ref()
arrow_element.value.style.transform = "rotate(90deg)"
```
{% endraw %}

- 此时对arrow_element的引用是独一无二的


<!--![引入图片]({{site.url}}/image/vue/2023-11-30-querySelector_ref/image_1.jpg) -->