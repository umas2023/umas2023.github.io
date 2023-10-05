---
layout: post
title: 'leetcode: 完全平方数'
info: '动态规划又一题'
date: 2023-10-05 17:31:28  +0800
categories: ['leetcode', 'python']
toc: True
---

## 题目

- 链接：https://leetcode.cn/problems/perfect-squares/?envType=study-plan-v2&envId=dynamic-programming

给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。  

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。  

```
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
```


```
输入：n = 13
输出：2
解释：13 = 4 + 9
```




## 题解

- 难点在于dp矩阵如何构建，以及如何拆分子问题
- 设dp[i]表示最少需要多少个数的平方来表示整数i
- 遍历[1,i]（实际上只需遍历[1,sqrt(i)]），设当前遍历到j，认为i中拆分出的平方数中包含j，那么只需找到i-j^2包含多少平方数即可，即有dp[i] = 1 + dp[i-j^2]；对于遍历的每一个j都可以得出一个解，其中的最小值即为对i的解



{% raw %}
```py
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1,n+1):
            minn = float('inf')
            for j in range(1,int(i**0.5)+1):
                minn = min(minn,dp[i-j*j])
            dp[i] = minn +1
        return dp[n]
    
print(Solution().numSquares(12))
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/leetcode/2023-10-05-numSquares/image_1.jpg) -->