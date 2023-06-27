---
layout: post
title:  "cpp: hello_world"
info: "cpp基础语法"
date:   2023-06-27 11:00:00 +0800
categories: cpp
toc: true
---

- 创建hello_world
```cpp
#include<stdio.h>
int main(void)
{
printf("Hello! This is a test prgoram.\n");
return0;
}
```




- 安装编译工具
```
sudo apt-get install build-essential manpages-dev
```

- 编译
```
gcc hello.cpp -o hello
```