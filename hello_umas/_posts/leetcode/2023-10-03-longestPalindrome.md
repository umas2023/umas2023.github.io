---
layout: post
title: 'leetcode: dp-最长回文子串'
info: '动态规划又一题，找到字符串中的最长回文子串'
date: 2023-10-03 17:38:37  +0800
categories: ['leetcode', 'python']
toc: True
---

- 原题链接：https://leetcode.cn/problems/longest-palindromic-substring/

- 题目：

```
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
```


- 边界：字符串长度为1，是回文串；字符串长度为2，若两字符相对，则为回文串
- 递推：判断s(i,j)为回文串的两个条件：首先s[i]=s[j]；其次s(i+1,j-1)是回文串



- 用db[i,j]:bool来表示s(i,j)是否为回文串


```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        lens = len(s)
        dp = [[0] * lens for _ in range(lens)]
        # 字串长度
        for sub_len in range(lens):
            # 起点
            for sub_start in range(lens - sub_len):
                sub_end = sub_start + sub_len
                # 边界
                if sub_len == 0:
                    dp[sub_len][sub_start] = 1
                elif sub_len == 1:
                    dp[sub_len][sub_start] = (s[sub_start] == s[sub_end])

                # 递推
                else:
                    dp[sub_len][sub_start] = (s[sub_start] == s[sub_end] and dp[sub_len - 2][sub_start + 1])

                # 回文字串长度
                if dp[sub_len][sub_start] and len(ans) < sub_len + 1:
                    ans = s[sub_start:sub_end + 1]

        return ans


print(Solution().longestPalindrome("abac"))


```


<!-- ![引入图片]({{site.url}}/image/leetcode/2023-10-03-longestPalindrome/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
