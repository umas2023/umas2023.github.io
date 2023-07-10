---
layout: post
title: 'git: hello_world'
info: 'git基本操作'
date: 2023-07-10 12:34:42  +0800
categories: ['git']
toc: True
---


## 基操push add

{% raw %}
```bash
git add .
git commit -m "xxx"
git push
```
{% endraw %}


## 查看/切换分支

{% raw %}
```bash
git branch -a
git checkout xxx
```
{% endraw %}




## 撤销commit和add

- 首先查看记录（q键退出）
  
{% raw %}
```bash
git log
```
{% endraw %}


- 回退到上一个commit

{% raw %}
```bash
git reset --soft <上一个的id>
```
{% endraw %}


- 撤销add

{% raw %}
```bash
git reset <文件名>
```
{% endraw %}
 
		
		
		
## 删除项目所有内容
	
{% raw %}
```bash
git rm -r .
# 这将递归删除所有文件和文件夹，包括 `.git` 文件夹。
git commit -m "Remove all files"
git push origin main
```
{% endraw %}



## 清空历史记录

{% raw %}
```bash
git checkout --orphan latest_branch
git add -A
git commit -am "Initial commit"
git branch -D main
git branch -m main
git push -f origin main
```
{% endraw %}




- 上述命令的作用是创建一个新的分支 `latest_branch`，将所有文件添加到该分支并提交一个新的空的初始提交，然后删除 `main` 分支并将 `latest_branch` 分支重命名为 `main` 分支。最后，使用 `git push -f` 命令强制推送到远程仓库。



