---
layout: post
title: 'vue: 关于template'
info: '记一个得物面试代码题'
date: 2023-10-14 17:01:33  +0800
categories: ['vue', 'knowhow']
toc: True
---

## template标签

- template的作用是模板占位符，可帮助我们包裹元素，但在循环过程当中，template不会被渲染到页面上

- 一个例子：用v-for循环的div下面增加了一个span，想让这个span也加入for循环
  - 法1：span上也添加v-for（显然不利于代码的后续扩展）
  - 法2：div和span外面再包一层div，给外层div添加v-for（缺点是会引入新的层级）
  - 法3：用template标签替代法2的div，template不会渲染在页面上（推荐）

- .vue文件中最外层template标签是用来写 html 模板的，且内部必须只有一个根元素（不然IDE会报错）


{% raw %}
```html
<template>
    <div class="demo">
        .....
    </div>
</template>
```
{% endraw %}






{% raw %}
```
```
{% endraw %}



<!--![引入图片]({{site.url}}/image/leetcode/2023-10-14-category_tag/image_1.jpg) -->