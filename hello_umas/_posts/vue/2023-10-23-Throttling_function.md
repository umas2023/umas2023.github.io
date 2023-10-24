---
layout: post
title: 'vue: 前端性能优化之节流函数'
info: '限制一个函数的执行频率（补充防抖函数）'
date: 2023-10-23 12:39:42  +0800
categories: ['vue', 'js']
toc: True
---


## 节流

- 节流函数是一种用于限制函数执行频率的技术，可以有效地控制事件触发频率，减少不必要的函数执行次数，提高前端性能和用户体验。


- 一个例子


{% raw %}
```js
function throttle(func, delay) {
  let timerId = null;
  
  return function() {
    if (!timerId) {
      const context = this;
      const args = arguments;
      
      timerId = setTimeout(function() {
        func.apply(context, args);
        timerId = null;
      }, delay);
    }
  }
}
```
{% endraw %}


- 上述节流函数接受两个参数：func 是要执行的函数，delay 是限制的时间间隔（以毫秒为单位）。函数内部使用一个定时器来控制函数的执行时间。当事件触发时，如果定时器未启动，则会启动定时器，并在指定的延迟后执行函数。如果定时器已经启动，则不会执行任何操作，从而限制了函数的执行频率。


{% raw %}
```js
const throttledFunction = throttle(myFunction, 500);
window.addEventListener('scroll', throttledFunction);
```
{% endraw %}


- （一些库中提供节流函数，比如lodash、Underscore.js）




## 防抖

- 防抖函数是一种用于控制函数执行频率的技术，类似于节流函数。不同之处在于，防抖函数会在连续触发事件后等待一段时间后执行函数，如果在等待时间内再次触发事件，则重新计时等待时间。防抖函数适用于那些连续触发的事件，但我们只关心最后一次触发的结果。


{% raw %}
```js
function debounce(func, delay) {
  let timerId = null;
  
  return function() {
    const context = this;
    const args = arguments;
    
    clearTimeout(timerId);
    timerId = setTimeout(function() {
      func.apply(context, args);
    }, delay);
  }
}

```
{% endraw %}


{% raw %}
```js
const debouncedFunction = debounce(myFunction, 500);

inputElement.addEventListener('input', debouncedFunction);

```
{% endraw %}


**防抖函数在以下情况下非常有用：**

- 频繁触发的事件：对于一些频繁触发的事件，如窗口调整大小、滚动事件或用户输入等，防抖函数可以控制事件回调函数的执行频率，避免过多的触发和执行。这可以减轻浏览器的负担，并提高性能和响应速度。

- 用户输入：在实时搜索、自动完成或自动保存等场景中，当用户在输入框中连续输入时，防抖函数可以延迟执行相关操作，直到用户停止输入一段时间后再进行处理。这样可以减少不必要的请求或操作，并提供更流畅的用户体验。

- 避免重复提交：在表单提交或按钮点击等场景中，防抖函数可以防止用户多次触发重复操作。通过设置适当的等待时间，只有在最后一次触发事件后才会执行相关操作，避免了重复提交的问题。

- 函数节流：尽管防抖函数和节流函数有些细微差别，但在某些情况下，防抖函数也可以用作函数节流的方式。例如，当需要限制函数的执行频率时，防抖函数可以确保函数在一定时间间隔内只执行一次，而忽略中间的触发。



**区分**

- 执行时机：
  - 节流函数：在一定的时间间隔内，只执行一次函数，即限制函数的执行频率。无论事件触发频率是多高，节流函数都会按照固定的时间间隔执行函数。
  - 防抖函数：在连续触发事件后，等待一段时间后执行函数，如果在等待时间内再次触发事件，则重新计时等待时间。防抖函数会等待一段时间，确保事件不再触发后才执行函数。

- 执行结果：
  - 节流函数：在指定的时间间隔内，只执行一次函数，并返回最后一次函数执行的结果。
  - 防抖函数：等待一段时间后，只执行一次函数，并返回最后一次函数执行的结果。

- 应用场景：
  - 节流函数：适用于需要限制函数执行频率的场景，例如监听滚动事件、窗口调整大小事件等。常用于减少事件处理的次数，提高性能。
  - 防抖函数：适用于连续触发事件但只关心最后一次触发结果的场景，例如实时搜索、延迟加载、防止重复提交等。常用于控制事件回调的执行时机，提供更好的用户体验。







<!--![引入图片]({{site.url}}/image/vue/2023-10-23-Throttling_function/image_1.jpg) -->