---
layout: post
title: 'leetcode: 无重复字符的最长子串'
info: '力扣第3题，滑动窗口'
date: 2023-10-17 18:35:54  +0800
categories: ['leetcode', 'python']
toc: True
---

## 知识总结

- 滑动窗口

- 判断数组中是否有重复元素

```py
def has_duplicate_chars(s):
    return len(set(s)) < len(s)
```

## 题目

- 地址：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
- 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


- 暴力自解：遍历所有子串

{% raw %}
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def has_duplicate_chars(s):
            return len(set(s)) < len(s)
        max_len = 0
        for index in range(len(s)):
            for sub_len in range(len(s)-index+1):
                sub_string = s[index:index+sub_len]
                if not has_duplicate_chars(sub_string):
                    max_len = max(max_len,sub_len)
        return max_len

print(Solution().lengthOfLongestSubstring("abcabcbb"))

# 虽然超时了，但has_duplicate_chars函数的实现方法还是值得一记的（毕竟gpt写的）
```
{% endraw %}

- ↑意料之中的超时了
- 实际上不应该遍历所有子串，当已经判定过一个子串的子串不符合条件后，就不用判断包含这个子串的所有父级子串了
- 应该用滑动窗口，窗口右侧添加新的字符，不满足条件时窗口左侧第一位弹出（窗口右滑）

- 判断是否有重复字符时，创建了一个哈希集合（set），左指针右移时从集合中移出一个字符，右指针右移时添加一个字符

{% raw %}
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

```
{% endraw %}



<!--![引入图片]({{site.url}}/image/leetcode/2023-10-17-LongestSubstring/image_1.jpg) -->