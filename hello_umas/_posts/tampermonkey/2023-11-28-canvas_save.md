---
layout: post
title: 'tampermonkey: docin白嫖下载'
info: '终于把canvas搞明白了'
date: 2023-11-28 19:37:21  +0800
categories: ['tampermonkey', 'js']
toc: True
---


- docin上看到ok的文章之后发现果然需要付费下载
- （你都在网页上给我看了还想限制我下载？）
- F12发现果然是放在canvas里的图片，关于canvas早就想了解一下了，正好今天比较闲，决定找gpt学一学


## canvas下载基本原理

```js
// 获取具有 class="hkswf-content2" 的 <div> 元素
const divElement = document.querySelector('.hkswf-content2');

// 在 <div> 元素内查找 <canvas> 元素
const canvasElement = divElement.querySelector('canvas');

// 将画布内容转换为数据 URL
const dataURL = canvasElement.toDataURL();
```

- 上面的脚本可以直接在console里敲，获取到的dataURL是一个以data:image/png;base64开头的非常长的数据（其实就是图片）


- 另存为test.txt，使用py脚本把它转化为图片


{% raw %}
```py
import base64
# 读取文本文件中的数据 URL
with open('./test.txt', 'r') as file:
    data_url = file.read()
# 确定数据 URL 的格式（例如："data:image/png;base64"）
format, encoded_data = data_url.split(',', 1)
# 解码 Base64 编码的数据
decoded_data = base64.b64decode(encoded_data)
# 提取文件名（可根据需要进行自定义命名）
filename = "image.png"  # 文件名为 image.png，你可以根据需要修改
# 以二进制模式写入解码后的数据到本地文件
with open(filename, 'wb') as file:
    file.write(decoded_data)
print("图像已保存为", filename)
```
{% endraw %}



- 可以看到图片已经被成功下载了，下面把这些步骤集成在一个tampermonkey脚本里


## tampermonkey基本框架和主要函数

- 首先是一个简单的框架，获取页面所有的canvas元素，设计的使用方法是直接在console里敲函数，所以把主函数getAllCanvases挂在window上，这样就可以直接在console里使用这个函数

{% raw %}
```js
// ==UserScript==
// @name         获取所有 canvas 对象
// @namespace    tampermonkey-example
// @version      1.0
// @description  获取指定目标网站上的所有 canvas 对象
// @match        https://www.docin.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 获取所有 canvas 对象的函数
    function getAllCanvases() {
        var canvases = document.getElementsByTagName('canvas');
        return Array.from(canvases);
    }

    // 将 getAllCanvases 函数绑定到 window 对象上
    window.getAllCanvases = getAllCanvases;

    console.log("加载用户脚本");
    console.log("提供函数：getAllCanvases");
})();
```
{% endraw %}



- 为了把资源保存到本地，还需要一个保存的函数


{% raw %}
```js
// 将 canvas 对象的内容保存为文本文件
function saveCanvasToTextFile(canvas, name) {
    var dataURL = canvas.toDataURL();
    var fileName = name + '.txt';
    var blob = new Blob([dataURL], { type: 'text/plain' });

    // 创建下载链接
    var downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = fileName;

    // 模拟点击下载链接
    downloadLink.click();

    // 释放资源
    URL.revokeObjectURL(downloadLink.href);
}
```
{% endraw %}


- 但实际上直接在js里把资源保存为png更加简单方便


{% raw %}
```js
function saveCanvasToImage(canvas, index) {
var dataURL = canvas.toDataURL('image/png');
var fileName = index + '.png';

// 创建下载链接
var downloadLink = document.createElement('a');
downloadLink.href = dataURL;
downloadLink.download = fileName;

// 模拟点击下载链接
downloadLink.click();
}
```
{% endraw %}


## 完整脚本


- 上面的脚本有一个问题，实际上网页中的图片是懒加载的，并且当图片移出可视区域时资源会被回收
- 所以至少要从头到尾滚动一次，在新的canvas出现时读取它并存入一个全局变量中，并且需要一个合理的去重函数
- （由于 canvas 对象是 JavaScript 中的对象类型，即使两个 canvas 对象的内容相同，它们在内存中也是不同的对象，因此无法直接使用 includes 方法进行准确的去重）
- 如果每个canvas都有独立的id的话就很简单了，直接用canvas.id即可去重，但显然没有；观察网页结构发现canvas的第5级父元素有独立的id，把它作为去重的依据
- 绑定鼠标滚动事件刷新allCanvases列表


- 以下是完整脚本


{% raw %}
```js
// ==UserScript==
// @name         获取docin所有懒加载的 canvas 对象并保存为图像文件
// @namespace    tampermonkey-example
// @version      1.0
// @description  获取指定目标网站上的所有懒加载的 canvas 对象，并将内容保存为以序号命名的图像文件（PNG格式）
// @match        https://www.docin.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    console.log("加载用户脚本");
    console.log("提供函数：saveAllCanvases");

    // 存储所有 canvas 对象的全局变量
    var allCanvases = [];
    // 存储所有 canvas 对象对应的第5级父元素的id的辅助数组
    var parentIds = [];


    // 获取所有 canvas 对象的函数
    function getAllCanvases() {
        var canvases = document.getElementsByTagName('canvas');
        return Array.from(canvases);
    }

    // 将 canvas 对象的内容保存为图像文件（PNG格式）
    function saveAllCanvases(){
        function saveCanvasToImage(canvas, index) {
            var dataURL = canvas.toDataURL('image/png');
            var fileName = index + '.png';

            // 创建下载链接
            var downloadLink = document.createElement('a');
            downloadLink.href = dataURL;
            downloadLink.download = fileName;

            // 模拟点击下载链接
            downloadLink.click();
        }
        allCanvases.forEach(function(canvas, index) {
            saveCanvasToImage(canvas, index);
        });
    }
    window.saveAllCanvases = saveAllCanvases




    // 初始化，获取当前可见的 canvas 对象并存储在全局变量中
    allCanvases = getAllCanvases();
    parentIds = allCanvases.map(function(canvas) {
        return getCanvasParentId(canvas);
    });

    // 手动滚动页面时触发的事件处理函数
    function handleScrollEvent() {
        // 延迟一段时间等待页面加载
        setTimeout(function() {
            // 获取新的 canvas 对象
            var newCanvases = getAllCanvases();

            // 合并新获取的 canvas 对象并去除重复项
            newCanvases.forEach(function(newCanvas) {
                var parentId = getCanvasParentId(newCanvas);
                var existingIndex = parentIds.indexOf(parentId);

                if (existingIndex === -1) {
                    allCanvases.push(newCanvas);
                    parentIds.push(parentId);
                }
            });

            console.log("更新全局变量中的 canvas 对象:", allCanvases);
            console.log("更新辅助数组中的父元素id:", parentIds);
        }, 300); // 可根据需要调整延迟时间
    }


    // 获取 canvas 父级元素的 id（向上5级，用于去重）
    function getCanvasParentId(canvas) {
        var parent = canvas;
        for (var i = 0; i < 5; i++) {
            parent = parent.parentNode;
        }
        return parent.id;
    }

    // 监听页面滚动事件
    window.addEventListener('scroll', handleScrollEvent);


})();
```
{% endraw %}



## 使用说明

- 添加脚本
- 进入网页后鼠标滚动页面直至所有图片都被加载一次（推荐打开F12终端查看是否成功载入）
- F12终端调用函```saveAllCanvases()```


{% raw %}
```
```
{% endraw %}

<!--![引入图片]({{site.url}}/image/tampermonkey/2023-11-28-canvas_save/image_1.jpg) -->
