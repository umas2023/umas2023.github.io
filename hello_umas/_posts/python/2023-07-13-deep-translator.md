---
layout: post
title: 'python: deep-translator调用谷歌翻译'
info: '拿来做日文ocr翻译'
date: 2023-07-13 12:43:41  +0800
categories: ['python', 'zip_pctools']
toc: True
---


- 网站：
  - https://pypi.org/project/deep-translator/


- 一个例子


{% raw %}
```py
from deep_translator import GoogleTranslator
text = "こんにちは" # Japanese string
translated = GoogleTranslator(source='ja', target='zh-CN').translate(text=text) # Chinese translation
print(translated) # prints 你好
```
{% endraw %}
