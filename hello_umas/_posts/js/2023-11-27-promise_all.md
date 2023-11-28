---
layout: post
title: 'js: 记某面试手搓promise.all'
info: '什么是promise.all以及手写一个'
date: 2023-11-27 14:10:53  +0800
categories: ['js']
toc: True
---


Promise.all 是 JavaScript 中的一个方法，它接收一个 Promise 对象的可迭代数组，并返回一个新的 Promise 对象。这个新的 Promise 对象会在数组中的所有 Promise 对象都已成功解析（resolved）时才会解析，否则会在遇到第一个被拒绝（rejected）的 Promise 对象时被拒绝。


{% raw %}
```js
Promise.all(iterable);
```
{% endraw %}

其中，iterable 是一个可迭代对象（如数组或类数组对象），包含了多个 Promise 对象。


使用 Promise.all 可以同时处理多个异步操作，并等待它们全部完成后进行进一步的处理。当所有的 Promise 都成功解析时，Promise.all 返回的 Promise 对象会以一个包含了所有 Promise 解析值的数组进行解析。如果任何一个 Promise 被拒绝，Promise.all 返回的 Promise 对象会立即被拒绝，并带有被拒绝的 Promise 的原因。
下面是一个使用 Promise.all 的示例：


{% raw %}
```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 1 resolved');
  }, 1000);
});
const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 2 resolved');
  }, 2000);
});
const promise3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 3 resolved');
  }, 1500);
});
Promise.all([promise1, promise2, promise3])
  .then((results) => {
    console.log(results); // ["Promise 1 resolved", "Promise 2 resolved", "Promise 3 resolved"]
    // 所有 Promise 都已成功解析
})
  .catch((error) => {
    console.log(error); // 如果有任何一个 Promise 被拒绝
});

```
{% endraw %}


在上述示例中，Promise.all 接收一个包含了三个 Promise 对象的数组。当这三个 Promise 都成功解析后，.then 部分会被执行，并打印出包含了所有 Promise 解析值的数组。如果有任何一个 Promise 被拒绝，.catch 部分会被执行，并打印出被拒绝的 Promise 的原因。



以下是一个简单的示例，演示如何自己实现 Promise.all 方法：


{% raw %}
```js
function myPromiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let completedCount = 0;
    // 检查参数是否为可迭代对象
    if (!Symbol.iterator in promises) {
      reject(new TypeError('promises must be an iterable'));
}
    // 遍历所有 Promise 对象
    for (let i = 0; i < promises.length; i++) {
promises[i]
        .then((result) => {
results[i] = result;
          completedCount++;
          // 当所有 Promise 都已成功解析时，解析返回的 Promise
          if (completedCount === promises.length) {
resolve(results);
          }
        })
        .catch((error) => {
          // 如果有一个 Promise 被拒绝，立即拒绝返回的 Promise
reject(error);
        });
    }
  });
}
// 示例用法
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 1 resolved');
  }, 1000);
});
const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 2 resolved');
  }, 2000);
});
const promise3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 3 resolved');
  }, 1500);
});
myPromiseAll([promise1, promise2, promise3])
  .then((results) => {
    console.log(results); // ["Promise 1 resolved", "Promise 2 resolved", "Promise 3 resolved"]
    // 所有 Promise 都已成功解析
})
  .catch((error) => {
    console.log(error); // 如果有任何一个 Promise 被拒绝
});

```
{% endraw %}


<!--![引入图片]({{site.url}}/image/js/2023-11-27-promise_all/image_1.jpg) -->
