---
layout: post
title: 'js: 构造函数'
info: '基础扫盲，什么是构造函数？'
date: 2023-10-15 20:21:36  +0800
categories: ['js', 'knowhow']
toc: True
---


- 面向对象编程（Object Oriented Programming，缩写为 OOP）是目前主流的编程范式。它将真实世界各种复杂的关系，抽象为一个个对象，然后由对象之间的分工与合作，完成对真实世界的模拟。

- JavaScript 语言使用构造函数（constructor）作为对象的模板。所谓”构造函数”，就是专门用来生成实例对象的函数。它就是对象的模板，描述实例对象的基本结构。

- new 就是创造对象/实例化对象的过程，new 创造出来的对象叫做构造函数的 实例对象


{% raw %}
```js
function Person() {
  //构造函数体内的属性
  this.name = 'Jack'
}

// Person.prototype 原型 上的方法
Person.prototype = {
  a: function () {
    console.log('我是一个a方法')
  },
  b: function () { },
  // ...
}

var p = new Person()
console.log(p)
console.log(p.name)// Jack
p.a()// 我是一个a方法

```
{% endraw %}


{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/js/2023-10-15-constructor/image_1.jpg) -->