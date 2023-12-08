---
layout: post
title: 'tampermonkey: 下载页面img'
info: 'img可以直接获取src，比起canvas简单多了'
date: 2023-12-08 13:32:20  +0800
categories: ['js', 'tampermonkey']
toc: True
---



- 首先获取所有img的src

{% raw %}
```js
function getImageSources() {
    const imgTags = document.querySelectorAll('img');
    const srcList = Array.from(imgTags).map(img => img.src);
    return srcList;
}
```
{% endraw %}


- 然后下载

{% raw %}
```js
function downloadImages(images) {
    images.forEach((src, index) => {
        // 创建一个虚拟的链接元素
        const link = document.createElement('a');
        link.href = src;
        link.target = '_blank';

        // 模拟点击链接以触发下载
        const fileName = `image_${index + 1}`;
        link.download = fileName;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
}
```
{% endraw %}


- 实测发现上面的简单函数有一个问题，只有10张图片被下载了，可能是网站或者浏览器存在某些限制


- 增加滚动监听确保所有图片都被加载


{% raw %}
```js
// 监听页面滚动事件，刷新图片列表
function handleScrollEvent() {
    // 延迟一段时间等待页面加载
    setTimeout(function() {
        getImageSources()
    }, 300);
}
window.addEventListener('scroll', handleScrollEvent);
```
{% endraw %}


- （实际上被测的网站没有懒加载，所有图片都被一次性载入，srcList是完整的）
- 考虑到srcList没有问题，可能是浏览器本身对下载数量进行了限制
- 用jszip把所有图片打包后一次性下载


{% raw %}
```js
// @grant        GM_download
// @grant        GM_xmlhttpRequest
// @require      https://cdn.jsdelivr.net/npm/jszip@3.7.1/dist/jszip.min.js


// 下载所有<img>
function downloadImages(images) {
    // 创建一个 JSZip 实例
    const zip = new JSZip();

    srcList.forEach((src, index) => {

        // 使用 GM_xmlhttpRequest 获取图片的二进制数据
        GM_xmlhttpRequest({
            method: 'GET',
            url: src,
            responseType: 'arraybuffer',
            onload: function(response) {
                // 将图片添加到zip文件中
                zip.file(`image_${index + 1}.png`, response.response);
            }
        });



    });

    // 生成并下载zip文件
    zip.generateAsync({ type: 'blob' }).then(function(content) {
        GM_download({
            name: 'images.zip',
            blob: content
        });
    });

}
window.downloadImages = downloadImages

```
{% endraw %}


- 上面的脚本使用 GM_xmlhttpRequest 获取图片的二进制数据，需要用grant关键字向浏览器请求权限

>在 Tampermonkey 用户脚本中，@grant 和 @require 是两个重要的元数据标签，用于配置脚本的权限和引入外部库。

>@grant 元数据标签用于指定用户脚本需要的权限。Tampermonkey 提供了一系列的权限，例如 GM_xmlhttpRequest 用于发起跨域请求，GM_download 用于下载文件等。

>@require 元数据标签用于引入外部库或脚本文件。它允许你在脚本中使用外部库的功能。

>默认情况下，Tampermonkey 将脚本的权限设置为 none，允许脚本访问普通的 JavaScript API，但不允许对浏览器执行其他高级操作，如发起跨域请求或下载文件。


- 添加grant后直接在控制台调用函数被禁止了，改用fetch获取图片的二进制数据

{% raw %}
```js
// 使用 Fetch API 获取图片的二进制数据
fetch(src)
    .then(response => response.arrayBuffer())
    .then(data => {
        // 将图片添加到 zip 文件中
        zip.file(`image_${index + 1}.png`, data);
    });
```
{% endraw %}


- 最后添加Promise.all保证所有fetch运行完毕后再下载，完整脚本如下

{% raw %}
```js
// ==UserScript==
// @name         下载页面所有img
// @namespace    tampermonkey-example
// @version      1.0
// @description  下载所有img标签的图片
// @match        （某个不知名的神奇妙妙图片网站）
// @grant        none
// @require      https://cdn.jsdelivr.net/npm/jszip@3.7.1/dist/jszip.min.js
// ==/UserScript==

(function() {
    'use strict';

    console.log("加载用户脚本");
    console.log("提供函数：downloadImages");

    // 全局，存储img列表
    var srcList = [];

    // 遍历<img>标签，获取src
    function getImageSources() {
        const imgTags = document.querySelectorAll('img');
        const newList = Array.from(imgTags).map(img => img.src);
        srcList = [...srcList,...newList];
        srcList = [...new Set(srcList)];
        console.log("srcList.length: "+srcList.length)
    }
    window.getImageSources = getImageSources


    // 监听页面滚动事件，刷新图片列表
    function handleScrollEvent() {
        // 延迟一段时间等待页面加载
        setTimeout(function() {
            getImageSources()
        }, 300);
    }
    window.addEventListener('scroll', handleScrollEvent);


    // 下载所有<img>
    function downloadImages() {
        // 创建一个 JSZip 实例
        const zip = new JSZip();

        // 用于存储所有 fetch 请求的 promise
        const fetchPromises = [];

        srcList.forEach((src, index) => {
            // 使用 Fetch API 获取图片的二进制数据
            const fetchPromise = fetch(src)
            .then(response => response.arrayBuffer())
            .then(data => {
                // 将图片添加到 zip 文件中
                zip.file(`image_${index + 1}.png`, data);
                console.log("fetch: "+index)
            });

            fetchPromises.push(fetchPromise);
        });

        // 使用 Promise.all 等待所有 fetch 请求完成
        Promise.all(fetchPromises)
            .then(() => {
            // 生成并下载 zip 文件
            return zip.generateAsync({ type: 'blob' });
        })
            .then(content => {
            const downloadLink = document.createElement('a');
            downloadLink.href = URL.createObjectURL(content);
            downloadLink.download = 'images.zip';
            downloadLink.click();
        });
    }
    window.downloadImages = downloadImages





})();
```
{% endraw %}


- （上一篇下载docin图片的脚本并没有观察到10张图片的下载限制）







{% raw %}
```
```
{% endraw %}





<!--![引入图片]({{site.url}}/image/tampermonkey/2023-12-08-img_download/image_1.jpg) -->