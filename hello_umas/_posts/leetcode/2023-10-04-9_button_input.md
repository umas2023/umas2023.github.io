---
layout: post
title: 'Klook笔试 - 9键输入法组合'
info: '记录遇到的一个简单笔试题，返回按下后所有可能的组合情况'
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


## 2023.10.5补充


- 补充：笛卡尔积
- 两个集合X和Y的笛卡尔积 (Cartesian product)，又称直积，表示 X x Y，第一个对象是 X 的成员而第二个对象是 Y 的所有可能有序对的其中一个成员。

```
A = {a,b}, B = {0,1,2}，则

A×B = {(a, 0), (a, 1), (a, 2), (b, 0), (b, 1), (b, 2)}

B×A = {(0, a), (0, b), (1, a), (1, b), (2, a), (2, b)}
```


- 内置模块itertools

```py
from itertools import product

def cartesian_product(*sets):
    return list(product(*sets))

# 示例用法
set1 = [1, 2]
set2 = ['a', 'b', 'c']
set3 = [True, False]

result = cartesian_product(set1, set2, set3)
print(result)
```

```
[(1, 'a', True), (1, 'a', False), (1, 'b', True), (1, 'b', False), (1, 'c', True), (1, 'c', False), (2, 'a', True), (2, 'a', False), (2, 'b', True), (2, 'b', False), (2, 'c', True), (2, 'c', False)]
```

- 稍微修改上面的代码就可以得到题目要求的结果

```py
from itertools import product

def cartesian_product(*sets):
    result = []
    for element in product(*sets):
        result.append(''.join(element))
    return result

# 示例用法
set1 = ['a', 'b']
set2 = ['c', 'd']
set3 = ['e', 'f']

result = cartesian_product(set1, set2, set3)
print(result)
```

```
['ace', 'acf', 'ade', 'adf', 'bce', 'bcf', 'bde', 'bdf']
```