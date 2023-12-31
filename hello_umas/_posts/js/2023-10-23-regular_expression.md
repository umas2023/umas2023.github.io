---
layout: post
title: 'js: 正则表达式'
info: '整理一些常用的，以js的replace函数为例'
date: 2023-10-23 13:18:39  +0800
categories: ['js', 'knowhow']
toc: True
---


- 头尾两个斜杠 // 通常用于包裹正则表达式的模式，用来标识正则表达式的开始和结束


- 常用的特殊字符转义序列

{% raw %}
```
\w：匹配包括字母、数字和下划线的任何单词字符（相当于 [a-zA-Z0-9_]）。

\W：匹配任何非单词字符（相当于 [^a-zA-Z0-9_]）。

\b：匹配单词边界，即单词和非单词字符之间的位置。

\B：匹配非单词边界。

\d：匹配任何数字字符（相当于 [0-9]）。

\D：匹配任何非数字字符（相当于 [^0-9]）。

\s：匹配任何空白字符，包括空格、制表符、换行符等。

\S：匹配任何非空白字符。

\t：匹配制表符。

\n：匹配换行符。

\r：匹配回车符。

.：匹配除换行符外的任何字符。
```
{% endraw %}



- 斜杠后可以添加修饰符，可以叠加，常用如下

```
g 匹配全部
使用示例：/abc/g
描述：返回所有匹配项，比如abc_abc_abc_abc

i 修饰符（不区分大小写）：
使用示例：/abc/i
描述：使正则表达式匹配时不区分大小写。

m 修饰符（多行匹配）：
使用示例：/abc/m
描述：使正则表达式匹配多行文本。

s 修饰符（单行匹配）：
使用示例：/abc/s
描述：使 . 元字符匹配包括换行符在内的任意字符。

u 修饰符（Unicode 匹配）：
使用示例：/abc/u
描述：启用 Unicode 匹配模式，用于处理 Unicode 字符。

y 修饰符（粘附匹配）：
使用示例：/abc/y
描述：执行粘附匹配，从目标字符串的当前位置开始匹配。
```

- 常用符号

{% raw %}
```
[]：方括号用于定义一个字符类，表示在该位置可以匹配方括号内列举的任意一个字符。
    例如，正则表达式 /[aeiou]/ 可以匹配任何一个元音字母
[^]：在字符类的开始位置使用 ^ 表示否定，表示匹配除列举字符之外的任意字符。
    例如，正则表达式 /[^0-9]/ 可以匹配任何非数字字符。
+：符号，它表示匹配前面的模式的一个或多个连续出现。
*：表示匹配零个或多个
.：匹配除换行符 \n 之外的任意单个字符。
    例如，正则表达式 /a.b/ 可以匹配 "aab"、"acb"、"a@b" 等字符串
?：匹配前面的模式零次或一次（可选匹配）
    例如，正则表达式 /colou?r/ 可以匹配 "color" 或 "colour" 字符串
()：创建捕获组，用于分组和提取匹配的子字符串。
    例如，正则表达式 /(ab)+/ 可以匹配 "ab"、"abab"、"ababab" 等字符串，并且捕获组可以提取出匹配的子字符串。
    捕获组可以在正则表达式中使用括号进行嵌套和组合，以构建更复杂的模式。在匹配成功后，可以通过索引或特殊变量来引用捕获组中提取的子字符串。例如，在 JavaScript 中，可以使用 $1、$2、$3 等变量来引用第一个、第二个、第三个捕获组提取的子字符串。
{}：大括号 {} 用于指定匹配的重复次数
    例如，\d{4} 匹配恰好四位数字
    {n,}：匹配前面的模式至少出现 n 次，例如，\d{2,} 匹配至少两位数字
    {n,m}：匹配前面的模式出现 n 到 m 次，例如，\d{2,4} 匹配两位到四位数字
```
{% endraw %}


- 一个例子

{% raw %}
```js
// 匹配电子邮件格式
const email = "example@example.com";
const isValidEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
console.log(isValidEmail); // Output: true

// .test() 是 JavaScript 正则表达式对象的一个方法。它用于测试一个字符串是否与正则表达式匹配。
```
{% endraw %}


{% raw %}
```
^：匹配输入的开始位置。
[^\s@]+：匹配一个或多个非空白字符和非 @ 字符的字符。
@：匹配 @ 字符。
[^\s@]+：匹配一个或多个非空白字符和非 @ 字符的字符。
\.：匹配 . 字符。需要使用 \ 进行转义，因为 . 在正则表达式中是一个特殊字符，表示匹配任意字符。
[^\s@]+：匹配一个或多个非空白字符和非 @ 字符的字符。
$：匹配输入的结束位置。
```
{% endraw %}


- 另一个例子，把xx2020-01-01yy改成xx2020年01月01日

{% raw %}
```js
let str = 'xx2020-01-01yy';
let res = str.replace(/(\d{4})-(\d{2})-(\d{2})/,
  (match, p1, p2, p3) => { return p1 + '年' + p2 + '月' + p3 + '日'; });

console.log(res) // xx2020年01月01日yy
```
{% endraw %}



{% raw %}
```
/(\d{4})-(\d{2})-(\d{2})/ 匹配形如 "yyyy-mm-dd" 格式的日期

匹配成功后，replace() 方法会调用一个回调函数，用于处理匹配到的结果。这个回调函数接受多个参数，其中第一个参数 match 是匹配到的完整字符串，后面的参数 p1、p2、p3 分别是匹配到的子字符串，即年、月、日。

```
{% endraw %}


<!--![引入图片]({{site.url}}/image/vue/2023-10-23-regular_expression/image_1.jpg) -->