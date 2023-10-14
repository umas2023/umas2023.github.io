---
layout: post
title: 'leetcode: js反转二叉树'
info: '记得物面试代码题'
date: 2023-10-14 17:01:33  +0800
categories: ['leetcode', 'js']
toc: True
---


{% raw %}
```js
class TreeNode {
    constructor(val) {
      this.val = val;
      this.left = null;
      this.right = null;
    }
  }
  
  function invertBinaryTree(root) {
    if (!root) {
      return null;
    }
  
    // 交换左右子节点
    let temp = root.left;
    root.left = root.right;
    root.right = temp;
  
    // 递归反转左子树和右子树
    invertBinaryTree(root.left);
    invertBinaryTree(root.right);
  
    return root;
  }
  
  // 示例用例
  const root = new TreeNode(4);
  root.left = new TreeNode(2);
  root.right = new TreeNode(7);
  root.left.left = new TreeNode(1);
  root.left.right = new TreeNode(3);
  root.right.left = new TreeNode(6);
  root.right.right = new TreeNode(9);
  
  console.log('原始二叉树:');
  console.log(root);
  
  const invertedRoot = invertBinaryTree(root);
  
  console.log('反转后的二叉树:');
  console.log(invertedRoot);
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/leetcode/2023-10-14-category_tag/image_1.jpg) -->