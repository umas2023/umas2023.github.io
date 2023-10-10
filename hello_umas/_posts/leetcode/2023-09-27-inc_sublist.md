---
layout: post
title: 'leetcode: dp-递增子序列问题'
info: '动态规划入门2，找到数组中最长严格递增子序列'
date: 2023-09-27 19:41:57  +0800
categories: ['leetcode', 'python']
toc: True
---

## 问题

- 接前篇青蛙跳阶问题，补充一个动态规划更有代表性的例子：递增子序列问题
- 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度

```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```

```
输入：nums = [0,1,0,3,2,3]
输出：4 
解释：[0,1,2,3]不一定必须是连续子序列
```

## 规律

- 首先遵循自底向上原则枚举分析分析规律：
- 如果新加入一个元素nums[i], 最长递增子序列要么是以nums[i]结尾的递增子序列，要么就是nums[i-1]的最长递增子序列。
- 对于一个以nums[i]结尾的数组nums，如果存在j属于区间[0，i-1],并且num[i]>num[j]的话，则有，dp(i) =max(dp(j))+1，


## 边界

- 当nums数组只有一个元素时，最长递增子序列的长度dp(1)=1,当nums数组有两个元素时，dp(2) =2或者1， 因此边界就是dp(1)=1。


## 最优子结构

- dp(i) =max(dp(j))+1，存在j属于区间[0，i-1],并且num[i]>num[j]。
- max(dp(j)) 就是最优子结构。


## 代码

{% raw %}
```py
def lengthOfList(nums):
    # 使用长度为nums长度的列表进行初始化
    dp = [0] * len(nums)  
    dp[0] = 1

    for i in range(1, len(nums)):
        dp[i] = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(lengthOfList([0, 1, 0, 3, 2, 3]))
```
{% endraw %}


<!-- ![引入图片]({{site.url}}/image/leetcode/2023-09-27-inc_sublist/image_1.jpg) -->

{% raw %}
```py
```
{% endraw %}
