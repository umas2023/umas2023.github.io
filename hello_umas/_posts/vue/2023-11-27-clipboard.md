---
layout: post
title: 'vue: 拷贝按钮-点击复制文本到剪贴板'
info: '可以直接用原生函数实现不需要导入外部包'
date: 2023-11-27 13:52:27  +0800
categories: ['vue', 'js']
toc: True
---

- 实现方法:document.execCommand("copy");


{% raw %}
```js
const textarea = document.createElement("textarea");
textarea.value = "ccccccccccccccc"
document.body.appendChild(textarea);
textarea.select();
document.execCommand("copy");
document.body.removeChild(textarea);
alert("已复制到剪贴板");
```
{% endraw %}


- 这是以前用过的一个其他方法，也记录一下

{% raw %}
```js
// npm install vue-clipboard3

import useClipboard from "vue-clipboard3";

// 复制到剪贴板
const { toClipboard } = useClipboard();
const copyCode = (value) => {
    toClipboard(value);
    ElMessage.success({
    message: "编码已复制到剪贴板",
    });
};
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/vue/2023-11-27-clipboard/image_1.jpg) -->