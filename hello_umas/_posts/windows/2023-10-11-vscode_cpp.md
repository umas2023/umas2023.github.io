---
layout: post
title: 'windows: vscode配置c++开发环境'
info: '好麻烦的，建议直接使用visual studio'
date: 2023-10-11 20:39:41  +0800
categories: ['windows', 'cpp']
toc: True
---

- 网上清一色安装MinGW，看起来超麻烦
- 试一试vscode推荐的方法，新建窗口时欢迎页右侧有C++开发入门，介绍了环境的设置方法
1. 安装MSVC，在下载页面搜索【Visual Studio 2022 生成工具】，页面：https://visualstudio.microsoft.com/zh-hans/downloads/
2. 安装程序中选择C++ 生成工具，我没找到，把c++全选了
3. 安装完成后终端键入cl，检查MSVC安装

（直接运行cpp时右下角会报错：仅当从 VS 开发人员命令提示符处运行 VS Code 时，cl.exe 生成和调试才可用。）

4. 开始菜单搜索developer，会找到Developer Powershell for VS 2022，打开它，在这个终端里输入code，会启动一个新的vscode界面，在这里写hello_world，点击F5或者右上角运行，选择C++什么调试器忘了，没及时记录


5. 但有一说一实际上这里编译运行的速度依然很美，还会生成许多中间文件，不如直接使用visual studio；或者在wsl里手动```gcc test.cpp -o test```，测试时发现报错找不到标准库，可以手动链接```g++ test.cpp -o test -lstdc++```


{% raw %}
```cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "hello" << endl;
    system("pause");
    return 0;
}

```
{% endraw %}


<!--![引入图片]({{site.url}}/image/windows/2023-10-11-vscode_cpp/image_1.jpg) -->
