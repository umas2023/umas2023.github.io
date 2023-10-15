---
layout: post
title: 'js: 箭头函数'
info: '区分匿名函数，什么时候不适合用箭头函数'
date: 2023-10-15 19:53:21  +0800
categories: ['js', 'knowhow']
toc: True
---

{% raw %}
```js
// 表达式函数
var fn1 = function(a, b) {
    return a + b
}

var fn1 = (a, b) => {
    return a + b
}

// 声明式函数
function fn2(a, b) {
    return a + b
}

(a, b) => {
    return a + b
}
```
{% endraw %}


## 区分箭头函数和匿名函数

- 箭头函数没有自己的 this 值，它会继承上下文中的 this 值。这意味着箭头函数内部的 this 始终指向定义该函数时的对象，而不是调用时的对象。
- 箭头函数没有自己的 arguments 对象，但可以访问外部作用域中的 arguments 对象。
- 箭头函数不能用作构造函数，不能使用 new 关键字实例化。
- 箭头函数没有 prototype 属性。



{% raw %}
```js
// 箭头函数
const add = (a, b) => a + b;
console.log(add(2, 3)); // 输出: 5
```
{% endraw %}

{% raw %}
```js
// 匿名函数
const multiply = function(a, b) {
  return a * b;
};
console.log(multiply(2, 3)); // 输出: 6
```
{% endraw %}


- 下面的例子可以说明二者的区别


{% raw %}
```js
const obj = {
  name: 'Alice',
  arrowFunc: () => {
    console.log(`Hello, ${this.name}!`);
  },
  anonymousFunc: function() {
    console.log(`Hello, ${this.name}!`);
  }
};

obj.arrowFunc(); // 输出: Hello, undefined!
obj.anonymousFunc(); // 输出: Hello, Alice!
```
{% endraw %}

- 在上面的例子中，arrowFunc继承自外部上下文的 this 值，即全局上下文，并且无法被修改。在全局上下文中并没有定义 name 属性，因此输出结果为 "undefined"。



## 详解箭头函数


- 函数对象是一个支持[[Call]]、[[Construct]]内部方法的对象。每个支持[[Construct]]的对象必须支持[[Call]]，也就是说，每个构造函数必须是一个函数对象。因此，构造函数也可以被称为构造函数函数或构造函数对象。所以，想要对某个对象使用new，就得确保该对象具有[[Construct]]这个内部方法。而箭头函数没有[[Construct]]。


- 同时因为没有构造原型的需求，所以箭头函数不存在 prototype 属性

- 用call()或者apply()调用箭头函数时，无法对this进行绑定，即传入的第一个参数被忽略。


## 什么时候不使用箭头函数

- 定义对象上的方法

由上面的例子可以看到this.name输出undefined

- 动态上下文的回调函数

在客户端编程中，将事件侦听器附加到DOM元素是一项常见的任务。事件触发处理程序函数，并将this作为目标元素,这里如果使用箭头函数就不够灵活。

{% raw %}
```js
const button = document.getElementById('myButton');
button.addEventListener('click', () => {
  console.log(this === window); // => true
  this.innerHTML = 'Clicked button';
});
```
{% endraw %}

在全局上下文中 this 指向 window。 当发生单击事件时，浏览器尝试使用按钮上下文调用处理函数，但箭头函数不会更改其预定义的上下文。this.innerHTML相当于window.innerHTML，没有任何意义。


必须应用函数表达式，该表达式允许根据目标元素更改 this：

{% raw %}
```js
const button = document.getElementById('myButton');
button.addEventListener('click', function() {
  console.log(this === button); // => true
  this.innerHTML = 'Clicked button';
});
```
{% endraw %}

当用户单击按钮时，处理程序函数中的 this 指向 button。因此这个问题。innerHTML = '已单击按钮'正确地修改按钮文本以反映已单击状态。

- 调用构造函数

this 在构造调用中是新创建的对象。当执行new MyFunction()时，构造函数MyFunction的上下文是一个新对象:this instanceof MyFunction === true。

箭头函数不能用作构造函数。 JavaScript通过抛出异常隐式阻止这样做。


{% raw %}
```js
const Message = (text) => {
  this.text = text;
};
// Throws "TypeError: Message is not a constructor"
const helloMessage = new Message('Hello World!');
```
{% endraw %}




{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/js/2023-10-15-Arrow_Function/image_1.jpg) -->