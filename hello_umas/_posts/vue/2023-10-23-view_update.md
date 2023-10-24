---
layout: post
title: 'vue: 前端性能优化之关于视图的更新方式'
info: '回流、重绘、合成'
date: 2023-10-23 12:59:59  +0800
categories: ['vue', 'js', 'knowhow']
toc: True
---


## 回流（reflow）

- 对 DOM 结构的修改引发 DOM 几何尺寸变化的时候,会发生回流过程。


**触发回流的操作：**

  1. DOM 元素的几何属性变化，常见的几何属性有width、height、padding、margin、left、top、border 等等, 这个很好理解。
  2. 使 DOM 节点发生增减或者移动。
  3. 当需要计算元素的几何属性（如宽度、高度、位置等）时，浏览器会进行回流操作，重新计算元素的布局信息。读取或写入 offset、scroll 和 client 相关属性时，也会导致浏览器进行回流操作。（offset族、scroll族和client族）
    - offset：用于获取元素在页面中的位置和尺寸信息，包括 offsetTop、offsetLeft、offsetWidth 和 offsetHeight。
    - scroll：用于获取或设置元素的滚动信息，包括 scrollTop、scrollLeft、scrollWidth 和 scrollHeight。
    - client：用于获取或设置元素的可视区域信息，包括 clientTop、clientLeft、clientWidth 和 clientHeight。
  4. 调用 window.getComputedStyle 方法。该方法返回元素的计算样式（computed style），而计算样式需要考虑元素的布局信息。因此，浏览器在执行 getComputedStyle 方法时，会强制进行回流操作




## 重绘

- 元素样式的改变并不影响它在文档流中的位置时触发重绘

- 例如：color、background-color、visibility等

- 重绘不一定导致回流，但回流一定发生了重绘



## 合成

- 跳过布局和绘制，transform、opacity、filter这些属性就可以实现合成的效果，也就是大家常说的GPU加速
- 直接进入合成线程





{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/vue/2023-10-23-view_update/image_1.jpg) -->