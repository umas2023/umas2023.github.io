---
layout: post
title: 'leetcode: 宇量昇复活赛笔试'
info: '快乐数、字符串消消乐、正则匹配（动态规划）'
date: 2023-11-03 15:16:29  +0800
categories: ['leetcode', 'python']
toc: True
---

- 没想到面试挂了之被另一个hr捞起来打复活赛了


## 知识总结

- （快乐数）小技巧：py不能直接遍历int数字的每一位，但用str转化为字符串就可以直接用for遍历了


## 快乐数

-  快乐数：每一位的平方相加和，迭代等于1
-  19 -> 82 -> 68 -> 100 -> true


{% raw %}
```py
class Solution:
    def happynum(self, n: int) -> bool:
        recordList = []

        def iterfunc(num):
            if num == 1:
                return True
            if num in recordList:
                return False
            recordList.append(num)
            next_n = 0
            for each in str(num):
                next_n += int(each) * int(each)
            print(next_n,recordList)
            return iterfunc(next_n)

        return iterfunc(n)


print(Solution().happynum(19))
```
{% endraw %}




## 消消乐

- 消消乐，消除字符串相邻相同的字符，迭代
- bcaac -> bcc -> b
- 自解通过率只有20%

- 思路是先把字符串转为数组，把所有符合条件的项改为True，然后一次性删除，再迭代

{% raw %}
```py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        sl = list(s)

        def removeDuplicatesList(str_list: list) -> list:

            # print("start:", str_list)

            same_str = ""
            for index in range(len(str_list)):
                this_str = str_list[index]
                next_str = False if index == len(str_list) - 1 else str_list[index + 1]
                if (this_str == next_str) or (this_str == same_str):
                    str_list[index] = True
                    same_str = this_str
                else:
                    same_str = ""

            # print(str_list)

            if not True in str_list:
                return str_list
            return removeDuplicatesList([x for x in str_list if not x == True])

        return "".join(removeDuplicatesList(sl))


# print(Solution().removeDuplicates("bcaac") == "b")
# print(Solution().removeDuplicates("aaaaa") == "")
# print(Solution().removeDuplicates("bbab") == "ab")
print(Solution().removeDuplicates("bba")) 

```
{% endraw %}



- 力扣1047，删除字符串中的所有相邻重复项
- 根据力扣的判题结果显示，aaaaaaaaa输出应该是a而不是空字符串，是我理解错题意了
- 力扣题目中明确提到每次操作删除相邻两个项，也就是说奇数的重复项会留下一项，宇量昇笔试题目描述不清楚，自解直接删除了所有连通的相同项



## 正则匹配

- 碰到原题了，参见力扣10：https://leetcode.cn/problems/regular-expression-matching/
- 但很离谱的是按照答案提交通过率只有74.29%，应该没有哪里写错



<!--![引入图片]({{site.url}}/image/leetcode/2023-11-03-yuliangsheng/image_1.jpg) -->