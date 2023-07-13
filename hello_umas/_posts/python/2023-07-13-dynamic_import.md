---
layout: post
title: 'python: 动态import'
info: '导入一个文件夹下的所有module'
date: 2023-07-13 13:52:41  +0800
categories: ['python',"zip_pctools"]
toc: True
---


- 调用的模组名是一个string变量，可以用importlib.import_module(name)导入
  - ispkg: 判断是否是一个module
  - （模组统一命名为MainClass，下面有统一的run()函数）
    
```py
for filefiner,name,ispkg in pkgutil.iter_modules([get_data["py_path"]]):
    if name == get_data["function"]:
        importlib.import_module(name)
        module = sys.modules[name]
        mc = module.MainClass(json_set = get_data)
        mc.run()
```


- 要想文件夹被识别为module，需要有__init__.py
- MainClass定义在__init__.py中：

```py
from sp_compress_image.img_compress import ImgCompress as MainClass
```

- 如果要调用mc下的一个函数：
  - get_button是一个字符串函数名

```py
get_button = get_data["button"] if "button" in get_data else ""
called_func = getattr(mc, get_button)
called_func()
```




<!-- ![引入图片]({{site.url}}/image/python/2023-07-13-dynamic_import/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
