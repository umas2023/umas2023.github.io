---
layout: post
title:  "js: hello_world JavaScript基础语法"
info: "JavaScript基础语法"
date:   2023-06-28 08:20:00 +0800
categories: js
toc: true
---


## 基本语法

- 两种for循环

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