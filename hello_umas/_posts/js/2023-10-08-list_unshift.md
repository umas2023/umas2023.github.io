---
layout: post
title: 'js: 列表扩展'
info: '两个列表合并为一个，扩展运算符的用法'
date: 2023-10-08 14:39:03  +0800
categories: ['js']
toc: True
---


- unshift函数扩展列表，三点（扩展运算符）拆分列表


```js
show_list.unshift(...image_urls)
```

- 关于扩展运算符

```js
const array1 = [1, 2, 3];
const array2 = [...array1, 4, 5]; // [1, 2, 3, 4, 5]
```

```js
const obj1 = { foo: 'bar', x: 42 };
const obj2 = { ...obj1, y: 10 }; // { foo: 'bar', x: 42, y: 10 }
```



{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/js/2023-10-08-list_unshift/image_1.jpg) -->