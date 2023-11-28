---
layout: post
title: 'python: 将变量嵌入字符串的几种方法'
info: '百分号，f-string，format'
date: 2023-11-27 14:13:45  +0800
categories: ['python']
toc: True
---


- 百分号法（Percent Formatting）/旧式字符串格式化（Old-style String Formatting）

{% raw %}
```py
title = "'%s: 将变量嵌入字符串的几种方法'" % basic_cat
```
{% endraw %}


-  f-strings（格式化字符串字面值）

{% raw %}
```py
basic_cat = "面试"
message = f"{basic_cat}: 记某面试手搓promise.all"
```
{% endraw %}

- 使用字符串的 format 方法

{% raw %}
```py
basic_cat = "面试"
message = "{}: 记某面试手搓promise.all".format(basic_cat)
message = "{0}: 记某面试手搓promise.all".format(basic_cat)
message = "{category}: 记某面试手搓promise.all".format(category=basic_cat)
```
{% endraw %}



- 好的剩下的我们以后遇到再补充

<!--![引入图片]({{site.url}}/image/python/2023-11-27-string_format/image_1.jpg) -->