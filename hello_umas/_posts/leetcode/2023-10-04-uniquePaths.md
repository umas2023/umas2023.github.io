---
layout: post
title: 'leetcode: 不同路径'
info: '动态规划又一题'
date: 2023-10-04 19:19:58  +0800
categories: ['leetcode', 'python']
toc: True
---


## 题目

- 链接：https://leetcode.cn/problems/unique-paths/description/?envType=study-plan-v2&envId=dynamic-programming


- 题目：一个机器人位于一个 m x n 网格的左上角。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。问总共有多少条不同的路径？


## 题解

- 自解（动态规划）：易知dp[i][j] = dp[i-1][j] + dp[i][j-1]，边界是当i或j=1时dp[i][j]=1

{% raw %}
```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        print(dp)
        for i in range(1,m+1):
            for j in range(1,n+1):
                print(i,j)
                if i==1:
                    dp[i][j] = 1
                elif j==1:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m][n]

print(Solution().uniquePaths(m=3,n=2))

```
{% endraw %}




- （因为最近在刷动态规划，双眼被蒙蔽了）
- 想要走到右下角，总步数是固定的m+n-2，向右几步和向下几步也都是固定的，向下m-1次，向右n-1次；所以路径总是就是从m+n-2次移动中选择m-1次向下移动的方案数，即组合数：

```
C(m-1)(m+n-2) = (m+n-2)! / (m-1)!(n-1)!
```

- 一行公式就可以解决


{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/leetcode/2023-10-04-uniquePaths/image_1.jpg) -->