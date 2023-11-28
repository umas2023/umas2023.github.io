---
layout: post
title: 'vue: 使用fetch动态获取本地json文件'
info: '后端项目还没建，先用前端json凑合一下'
date: 2023-11-27 13:46:29  +0800
categories: ['vue', 'js']
toc: True
---



- 一般来说直接在头部import就可以导入json像这样

{% raw %}
```js
import image_list from "@/assets/list/image_list.json"
```
{% endraw %}


- 但如果需要在函数里动态导入json，可以使用fetch


{% raw %}
```js
const json_url = xxx
fetch(json_url)
    .then(response => response.json())
    .then(data => {
        res_text.value = input_id.value
        res_json.value = data
        console.log(res_json.value)
    })
    .catch(error => {
        console.error("Error fetching JSON:", error);
    });
```
{% endraw %}

<!--![引入图片]({{site.url}}/image/vue/2023-11-27-fetch_json/image_1.jpg) -->