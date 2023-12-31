---
layout: post
title: 'js: async,await异步修饰符'
info: '异步程序'
date: 2023-07-13 14:18:18  +0800
categories: ['js']
toc: True
---



    
    
- await 关键字只能放在 async 函数内部，await关键字的作用是获取Promise中返回的内容，获取的是Promise函数中resolve或者reject的值
- 如果一个 Promise 被传递给一个 await 操作符，await 将等待 Promise 正常处理完成并返回其处理结果。
- 如果await后面不是一个Promise的返回值，则会按照同步程序返回值处理,为undefined
    

{% raw %}
```js 
const bbb = function(){ return 'string'}
    
async function funAsy() {
    const a = await 1
    const b = await new Promise((resolve, reject)=>{
        setTimeout(function(){
            resolve('time')
        }, 3000)
    })
    const c = await bbb()
    console.log(a, b, c)
}
    
funAsy()

//  运行结果是 3秒钟之后 ，输出 1， time , string,
//  程序在b = await处停顿了
```
{% endraw %}


- 异常处理

```js
async function asyncFunc() {
    try {
        await new Promise(function (resolve, reject) {
            throw "Some error"; // 或者 reject("Some error")
        });
    } catch (err) {
        console.log(err);
        // 会输出 Some error
    }
}
asyncFunc();
```
    


- 返回值

```js
async function asyncFunc() {
    let value = await new Promise(
        function (resolve, reject) {
            resolve("Return value");
        }
    );
    console.log(value);
}
asyncFunc();
```


- async 函数本身并不是一个 Promise 对象。async 函数是一种特殊的函数语法，它的目的是简化基于 Promises 的异步操作。
- async 函数在执行时会返回一个 Promise 对象。这个 Promise 对象的最终结果取决于 async 函数内部的执行情况。如果 async 函数内部显式地返回一个值，那么这个 Promise 将会被解析为该值。如果 async 函数内部抛出一个异常，那么这个 Promise 将会被拒绝，并且捕获到的异常将成为拒绝的原因。


<!-- ![引入图片]({{site.url}}/image/js/2023-07-13-async_await/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
