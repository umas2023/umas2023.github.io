---
layout: post
title: 'js: 异步优先级'
info: 'setTimeout(0); Promise; 宏任务与微任务'
date: 2023-11-27 14:03:54  +0800
categories: ['js']
toc: True
---


- JavaScript中的异步操作具有不同的优先级，这取决于异步操作的类型和调用方式。下面列出了常见的异步操作及其优先级：
  1. 宏任务（Macrotasks）：宏任务包括整体代码块（script），setTimeout、setInterval、setImmediate（Node.js环境中），I/O 操作等。宏任务具有较低的优先级，当执行栈为空时才会执行。
  2. 微任务（Microtasks）：微任务包括Promise、MutationObserver、process.nextTick（Node.js环境中）等。微任务拥有较高的优先级，会在当前宏任务执行结束后、下一个宏任务开始之前执行。
- 综合来说，JavaScript的异步操作按照以下顺序执行：
	1. 执行当前的同步代码，直到遇到第一个宏任务。
	2. 执行所有微任务队列中的任务，直到微任务队列为空。


{% raw %}
```js
console.log('1');
setTimeout(function() {
  console.log('2');
}, 0);
Promise.resolve().then(function() {
  console.log('3');
});
console.log('4');

// 结果1432
```
{% endraw %}


在这个例子中，首先会执行同步代码，并按顺序打印出1和4。然后，setTimeout函数会被调度为一个宏任务，但由于延时为0，所以会被放入宏任务队列中等待执行。接下来，Promise.resolve().then会被调度为一个微任务，并立即执行，打印出3。最后，当所有的同步代码执行完毕后，事件循环会开始执行下一个宏任务，此时会打印出2。


<!--![引入图片]({{site.url}}/image/js/2023-11-27-async_priority/image_1.jpg) -->