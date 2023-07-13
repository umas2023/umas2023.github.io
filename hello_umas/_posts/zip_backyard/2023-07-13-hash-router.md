---
layout: post
title: 'zip_backyard: hash模式路由'
info: '解决/show页刷新404'
date: 2023-07-13 10:35:05  +0800
categories: ['zip_backyard', 'vue']
toc: True
---


- 站点上传到github.io后，由于GitHub Pages 默认基于静态文件，在 /show 页面刷新时，GitHub Pages 服务器会尝试查找对应的静态文件 /show/index.html ，当然找不到，所以会报404
- 解决方法是使用hash模式路由（也称为锚点路由），在 URL 中使用 # 符号，并不会触发页面刷新，因此可以绕过 GitHub Pages 的限制。

{% raw %}
```js
import { createRouter, createWebHashHistory } from 'vue-router';

const router = createRouter({
  history: createWebHashHistory(),
  // ...其他配置项
});
```
{% endraw %}


- 补充：什么是SEO
  - SEO 是搜索引擎优化（Search Engine Optimization）的缩写，它是指通过对网站进行优化，以提高其在搜索引擎中的排名和可见性，从而吸引更多的有机（非付费）流量。SEO 的目标是使网站在搜索引擎结果页面（SERP）中出现在更高的位置，增加用户访问量，提高网站的曝光度和影响力。

- 补充：为什么hash路由会影响SEO
  - 搜索引擎在抓取和索引网页时通常会忽略 URL 中的 hash 部分。搜索引擎主要关注 URL 中的路径部分，而不会对 hash 部分进行解析和索引。

- 如何解决
  - 比如在服务器端重定向