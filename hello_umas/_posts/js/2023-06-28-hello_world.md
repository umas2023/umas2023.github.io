---
layout: post
title:  "js: hello_world JavaScript基础语法"
info: "JavaScript基础语法"
date:   2023-06-28 08:20:00 +0800
categories: js
toc: true
---


## 基本语法


### 数据类型

- Map 和 Set

```js
// Map: 类似Object的一种键值对，但Map的键不仅限字符串
const a = new Map()
a.set(0,"aaa")
a.get(0)
a.size

// Set: 类似数组，但没有重复的值
const set = new Set([1,1,2,3])
// > Set(4) {1,2,3}
set.add(4)
set.delete(1)
set.size
```

- 区分Map和Object：
  - 键的类型
  - Object的键值对个数需要手动计算，而Map可以.size
  - Map是iterable可迭代的


- 利用Set给数组去重

```js
function unique (arr) {
  return Array.from(new Set(arr))
}

// 注意这种方法不能去除空对象{}
// 可以用双层for循环splice删除
```

- 补充Array.from的用法：

```js
// 类数组转换为数组


// 数组每一项乘2
const someNumbers = { '0': 10, '1': 15, length: 2 };
Array.from(someNumbers, value => value * 2); // => [20, 30]

// 填充数组
const length = 3;
const init   = 0;
const result = Array.from({ length }, () => init);

// 填充数组2
const length = 3;
const init   = 0;
const result = Array(length).fill(init);
```

- 补充去重的其他方法

```js
// 新建空数组，使用indexOf或者includes判断是否已存在，不存在push进去，代码略


// 使用filter：filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素
// 接受一个函数作为输入参数，这个函数有三个参数：item, index, arr
// filter基础示例：返回数组 ages 中所有元素都大于 18 的元素
var ages = [32, 33, 16, 40];
function checkAdult(age) {return age >= 18;}
function myFunction() {    
  document.getElementById("demo").innerHTML = ages.filter(checkAdult);
}

// filter去重
function unique(arr) {
  return arr.filter(function(item, index, arr) {
    //当前元素，在原始数组中的第一个索引==当前索引值，否则返回当前元素
    return arr.indexOf(item, 0) === index;
  });
}
```



### 变量声明

- var ——ES5 变量声明方式
1. 在变量未赋值时，变量undefined（为使用声明变量时也为undefined）
2. 作用域——var的作用域为方法作用域；只要在方法内定义了，整个方法内的定义变量后的代码都
可以使用

- let——ES6变量声明方式
1. 在变量为声明前直接使用会报错
2. 作用域——let为块作用域——通常let比var 范围要小
3. let禁止重复声明变量，否则会报错；var可以重复声明

- const——ES6变量声明方式
1. const为常量声明方式；声明变量时必须初始化，在后面出现的代码中不能再修改该常量的值
2. const实际上保证的，并不是变量的值不得改动，而是变量指向的那个内存地址不得改动


### 两种for循环

{% raw %}
```js
// for...in 循环适用于遍历对象的属性，而不是用于遍历数组的元素。
// 使用 for...of 循环来遍历它的元素。

for (let item of tableData.value) {
  console.log(item);
}
```
{% endraw %}







## 常用函数

### 定时器
{% raw %}
```js
  // 时间间隔
  let time_interval = 3000
  // 设置定时器
  let set_id = setInterval(get_list_check, time_interval)
  // 定时清除
  setTimeout(() => {
      clearInterval(set_id)
  }, 10 * time_interval)
```
{% endraw %}



### 获取当前时间

- 格式为 20:05:31
{% raw %}
```js
const currentTime = new Date().toLocaleTimeString('en-US', { hour12: false });
```
{% endraw %}




{% raw %}
```js
```
{% endraw %}