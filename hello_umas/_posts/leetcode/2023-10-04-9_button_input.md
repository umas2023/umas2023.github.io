---
layout: post
title: 'leetcode: 9键输入法组合'
info: '记录遇到的一个简单笔试题'
date: 2023-10-04 20:42:31  +0800
categories: ['leetcode', 'python']
toc: True
---


- Klook笔试题，因为原题是英文给的，事后没有找到完全一样的原题
- 简述一下题目大意：9键输入法，给定按键序列，返回所有组合

```
比如按下23
所有可能的组合有['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
```

- 题目本身不难，循环嵌套再拼接就行了

{% raw %}
```py
import sys

for line in sys.stdin:
    a = line.split()
    ans = []
    dic9={
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"],
    }

    if len(a) == 0:
        ans = []
    else:
        ans = dic9[a[0][-1]]
        for index in reversed(a[0][:-1]):
            sv = []
            for letter in dic9[index]:
                for item in ans:
                    sv.append(letter+item)
            ans = sv
        print(ans)

```
{% endraw %}



- （但是他妈的，python打印字符串列表时默认使用单引号，牛客判定结果用双引号，我的程序通过率是0%）
- （↑转义成纯字符串也通不过，妈的真是触及到知识盲区了）

<!--![引入图片]({{site.url}}/image/leetcode/2023-10-04-9_button_input/image_1.jpg) -->