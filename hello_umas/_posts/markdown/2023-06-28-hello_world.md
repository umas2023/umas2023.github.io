---
layout: post
title:  "markdown: hello_world"
info: "markdown基本操作"
date:   2023-06-28 09:00:00 +0800
categories: markdown
toc: true
---


- 超链接  
[哔哩哔哩](https://www.bilibili.com/)
{% raw %}
```md
[哔哩哔哩](https://www.bilibili.com/)
```
{% endraw %}


- 引入图片
![引入图片]({{site.url}}/image/markdown/2023-06-28-hello_world/image_1.jpg)
{% raw %}
```md
![引入图片]({{site.url}}/image/markdown/2023-06-28-hello_world/image_1.jpg)
```
{% endraw %}


- 用html引入图片并控制格式


<img src="{{site.url}}/image/markdown/2023-06-28-hello_world/image_1.jpg" width="50%" height="50%">
{% raw %}
```md
<img src="{{site.url}}/image/markdown/2023-06-28-hello_world/image_1.jpg" width="50%" height="50%">
```
{% endraw %}


- 两种分割线  

---  
{% raw %}
```
---  
```
{% endraw %}

***

{% raw %}
```
*** 
```
{% endraw %}

- 删除线  
~~删除线~~
{% raw %}
```
~~删除线~~
```
{% endraw %}

- 加粗  
**加粗**
{% raw %}
```
**加粗**
```
{% endraw %}


- 斜体  
*斜体*
{% raw %}
```
*斜体*
```
{% endraw %}

- 下划线  
<u>带下划线文本</u>
{% raw %}
```
<u>带下划线文本</u>
```
{% endraw %}

- 嵌套结构  
> 最外层
>> 第一层嵌套
>>> 第二层嵌套  

{% raw %}
```
> 最外层
>> 第一层嵌套
>>> 第二层嵌套  
```
{% endraw %}


- 表格
  
| 布局           | 解释                |
| -------------- | ------------------- |
| QHBoxLayout    | 线性水平布局        |
| QVBoxLayout    | 线性垂直布局        |
| QGridLayout    | 在可转位网格 XxY 中 |
| QStackedLayout | 堆叠 （z） 彼此前面 |


{% raw %}
```
| 布局           | 解释                |
| -------------- | ------------------- |
| QHBoxLayout    | 线性水平布局        |
| QVBoxLayout    | 线性垂直布局        |
| QGridLayout    | 在可转位网格 XxY 中 |
| QStackedLayout | 堆叠 （z） 彼此前面 |
```
{% endraw %}
