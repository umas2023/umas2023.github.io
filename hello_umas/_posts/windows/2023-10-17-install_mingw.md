---
layout: post
title: 'windows: windows安装gcc'
info: 'MinGW'
date: 2023-10-17 13:04:31  +0800
categories: ['windows', 'cpp']
toc: True
---


- 下载：https://sourceforge.net/projects/mingw/

- 一路next，等待MinGW Installation Manager启动，勾选mingw-gcc-g++-bin，点击左上角Installation -> Apply Changes

- 环境变量添加C:\MinGW\bin、C:\MinGW\lib、C:\MinGW\include

{% raw %}
```cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "hello world" << endl;
    return 0;
}
```
{% endraw %}

```
gcc .\test.cpp -o test -lstdc++
```

<!--![引入图片]({{site.url}}/image/windows/2023-10-17-add_date/image_1.jpg) -->