---
layout: post
title: 'leetcode: 解决智力问题'
info: '动态规划又一题'
date: 2023-10-05 16:10:23  +0800
categories: ['leetcode', 'python']
toc: True
---

## 题目

- 链接：https://leetcode.cn/problems/solving-questions-with-brainpower/?envType=study-plan-v2&envId=dynamic-programming


给你一个下标从 0 开始的二维整数数组 questions ，其中 questions[i] = [points_i, brainpower_i] 。  

这个数组表示一场考试里的一系列题目，你需要 按顺序 （也就是从问题 0 开始依次解决），针对每个问题选择 解决 或者 跳过 操作。解决问题 i 将让你 获得  points_i 的分数，但是你将 无法 解决接下来的 brainpower_i 个问题（即只能跳过接下来的 brainpower_i 个问题）。如果你跳过问题 i ，你可以对下一个问题决定使用哪种操作。  

比方说，给你 questions = [[3, 2], [4, 3], [4, 4], [2, 5]] ：  
如果问题 0 被解决了， 那么你可以获得 3 分，但你不能解决问题 1 和 2 。  
如果你跳过问题 0 ，且解决问题 1 ，你将获得 4 分但是不能解决问题 2 和 3 。  
请你返回这场考试里你能获得的 最高 分数。  


## 题解

- dp[i]表示解决前i道问题的最高分数，边界dp[0] = 0，dp[1] = points_0
- 类似打家劫舍问题，只不过打劫间隔不是固定的1，而是由brainpower决定
- 类比打家劫舍可得dp[i] = max( dp[i-1], dp[i-?]+points_i )，其中dp[i-?]表示满足条件【解决问题i】最近的前一项，（注意满足条件的dp[i-?]可能不只有一项），为找出dp[i-?]可以遍历原数组，找出每一项在删除brainpower后对应的后一项，以此构建索引字典，比如下面的例子

```py
[[3,2],[3,1],[3,0],[1,1]]
# 第0，1，2，3项对应的后一项分别是第3,3,3,4项，因此可以构建字典如下
{
    0:[],
    1:[],
    2:[],
    3:[0,1,2],
    4:[3] # index>3没有意义
}
```

- 但显然这样会提高时间复杂度，官方题解采用了另一种思路
- 构建状态转移方程的意义在于找出相邻两项dp之间的关系，并不一定是dp[i]和dp[i-1]，也可以是dp[i]和dp[i+1]；我们可以反向思考：
- 如果不解决第1道题目，dp[i] = dp[i+1]
- 如果解决，下一道题目是```i + brainpower_i + 1```，也就是说此时有

<center>dp[i] = points_i + dp[i + brainpower_i + 1]</center> 

- 状态转移方程如下

<center>dp[i] = max( dp[i+1], points_i + dp[i + brainpower_i + 1] )</center> 

- 此时边界为dp[n] = 0，表示没有做任何题目，所求结果为dp[0]


{% raw %}
```py
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)   # 解决每道题及以后题目的最高分数
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], questions[i][0] + dp[min(n, i + questions[i][1] + 1)])
        return dp[0]
```
{% endraw %}

- 因为i + questions[i][1] + 1有可能超出边界，即后面没有可以解的题目，此时可以认为dp[i + brainpower_i + 1] = dp[n] = 0，所以例程中使用了min直接把0赋值给算式



<!--![引入图片]({{site.url}}/image/leetcode/2023-10-05-mostPoints/image_1.jpg) -->