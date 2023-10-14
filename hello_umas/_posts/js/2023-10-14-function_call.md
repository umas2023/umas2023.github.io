---
layout: post
title: 'js: call函数'
info: '记得物面试题一道'
date: 2023-10-14 17:08:42  +0800
categories: ['js']
toc: True
---


## 首先了解什么是call


- 在 JavaScript 中，函数是对象的方法。如果一个函数不是 JavaScript 对象的方法，那么它就是全局对象的函数



{% raw %}
```js
var person = {
    firstName:"Bill",
    lastName: "Gates",
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
}
person.fullName();		// 将返回 "Bill Gates"
```
{% endraw %}

- 上面的例子中fullName 属性是一个方法。person 对象是该方法的拥有者。fullName 属性属于 person 对象的方法。



- call() 方法是预定义的 JavaScript 方法。它可以用来调用所有者对象作为参数的方法。通过 call()，您能够使用属于另一个对象的方法。下例调用 person 的 fullName 方法，并用于 person1：



{% raw %}
```js
var person = {
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
}
var person1 = {
    firstName:"Bill",
    lastName: "Gates",
}
var person2 = {
    firstName:"Steve",
    lastName: "Jobs",
}
person.fullName.call(person1);  // 将返回 "Bill Gates"
```
{% endraw %}



- call方法可以接受参数



{% raw %}
```js
var person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}
var person1 = {
  firstName:"Bill",
  lastName: "Gates"
}
person.fullName.call(person1, "Seattle", "USA");
```
{% endraw %}



## 然后自己实现一个call

- 下面是gpt写的，但我觉得hr要的应该不是这个

{% raw %}
```js
// 自定义的 call 函数实现
function myCall(fn, context, ...args) {
  // 检查 fn 是否为函数
  if (typeof fn !== 'function') {
    throw new TypeError('myCall 只能用于函数');
  }

  // 将函数作为上下文对象的一个属性
  const symbol = Symbol('temp');
  context[symbol] = fn;

  // 使用 eval 执行函数并获取结果
  const result = eval('context[symbol](...args)');

  // 删除添加的属性
  delete context[symbol];

  // 返回函数执行的结果
  return result;
}

// 示例用法
function greet() {
  console.log(`Hello, ${this.name}!`);
}

const person = { name: 'John' };

myCall(greet, person);
```
{% endraw %}



- Symbol是JavaScript中的一种原始数据类型，引入于ES6（ECMAScript 2015）标准。它是一种唯一且不可变的数据类型，用于表示一个独一无二的标识符。

- 与其他原始数据类型（如字符串、数字和布尔值）不同，Symbol值在内存中是唯一的。每个Symbol值都是独一无二的，即使它们具有相同的描述。

- 在示例代码中，我们使用Symbol('temp')创建了一个带有描述符为"temp"的Symbol值，并将其作为临时属性名添加到上下文对象中。通过这种方式，我们确保了该属性名的唯一性，不会与上下文对象中的其他属性名冲突。

- context[symbol] = fn 这行代码的意思是将一个函数 fn 赋值给对象 context 的一个属性，而该属性的名称是 symbol 所表示的 Symbol 值。

- 在 JavaScript 中，eval 函数接受一个字符串参数，并将该字符串作为 JavaScript 代码进行解析和执行。在这个特定的表达式中，我们使用 eval 函数来执行一个动态生成的函数调用。

- 在上面的示例中，greet 函数是要调用的函数，person 对象是作为上下文对象传递给 myCall 函数的参数，也就是说在myCall中context = person







- 根据对代码的理解，简化了gpt的代码如下：

```js
function myCall(fn, context) {
  if (typeof fn !== 'function') {
    throw new TypeError('myCall 只能用于函数');
  }

  // 创建一个唯一的属性名
  const propertyName = '__myCall__';

  // 将函数赋值给上下文对象的属性
  context[propertyName] = fn;

  // 使用属性名调用函数并获取结果
  const result = context[propertyName]();

  // 删除临时属性
  delete context[propertyName];

  return result;
}

// 示例用法
function greet() {
  console.log(`Hello, ${this.name}!`);
}

const person = { name: 'John' };

myCall(greet, person);
```


- 简单来说就是，person内部没有greet方法，在myCall里把greet方法加入到person中，调用完后再删掉
- 因为greet加入了person，所以可以共享this

<!--![引入图片]({{site.url}}/image/js/2023-10-14-function_call/image_1.jpg) -->


