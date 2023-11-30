---
layout: post
title: 'vue: ts环境下导入public目录下的json'
info: '记一下'
date: 2023-09-08 19:50:10  +0800
categories: ['vue']
toc: True
---


- 一般在assets或者utils目录下导入json时可以直接用@定义路径，在tsconfig.json中添加```"resolveJsonModule": true,```即可

{% raw %}
```js
import assets_json from "@/utils/assets_conf.json"
```
{% endraw %}



- 如果json在public路径下，直接导入会报错
- 在项目根目录（或者如果已经定义了utils.d.ts的话在utils目录也可以）下新建.d.ts，比如assets_conf.d.ts，写入以下内容

{% raw %}
```ts
declare module "*.json" {
    const value: any;
    export default value;
  }
```
{% endraw %}


- 这时再导入就不会报错了

{% raw %}
```js
import assets_json from "/public/config/assets_conf.json"
```
{% endraw %}


- 或者使用fetch（推荐）
  - 参见某日的另一篇

{% raw %}
```
```
{% endraw %}
