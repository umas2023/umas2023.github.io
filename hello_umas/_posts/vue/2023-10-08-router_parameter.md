---
layout: post
title: 'vue: 读取router参数'
info: '主要是类型定义上存在一些问题'
date: 2023-10-08 14:36:17  +0800
categories: ['vue']
toc: True
---



- vue读取router参数


- 比如通过这样的链接访问网页：http://localhost:8080/#/home?id_input=10001
- 希望读取到id_input的值并赋给变量

```js
import { useRouter } from "vue-router";
const router = useRouter();

console.log(router.currentRoute.value.query.id_input)
```

- 在 Vue 3 中，router.currentRoute.value.query 返回的是一个包含查询参数的对象，其中每个查询参数的值是一个字符串数组（string[]）或单个字符串（string）

	
	
```js
id_input.value = (router.currentRoute.value.query.id_input as string)
```


{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/vue/2023-10-08-router_parameter/image_1.jpg) -->