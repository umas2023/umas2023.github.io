---
layout: post
title: 'leetcode: 递归-相同的树'
info: '递归基础，判断二叉树是否相同'
date: 2023-09-27 18:13:17  +0800
categories: ['leetcode', 'python']
toc: True
---

# leetcode 100.相同的树

- 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

- 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

- 输入：p = [1,2,3], q = [1,2,3]
- 输出：true


<!-- ![引入图片]({{site.url}}/image/leetcode/2023-09-27-isSameTree/image_1.jpg) -->

{% raw %}
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 两者都为None则返回True
        if not p and not q:
            return True
        # 其中一个为None则返回False
        if not p or not q:
            return False
        # 都不为None则比较值
        if p.val != q.val:
            return False
        # 对左右子树分别进行递归比较
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

```
{% endraw %}
