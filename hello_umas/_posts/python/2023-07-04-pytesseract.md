---
layout: post
title: 'python: pytesseract 配置'
info: '免费ocr:tesseract.exe'
date: 2023-07-04 11:25:22  +0800
categories: ['python', 'zip_pctools']
toc: True
---

## 安装tesseract
- https://github.com/tesseract-ocr/tesseract


## 加入环境变量

![引入图片]({{site.url}}/image/python/2023-07-04-pytesseract/image_1.jpg)


## 直接添加路径
- 实际使用发现添加环境变量不一定好用，依然会报错tesseract not installed
- 这时候需要手动在pytesseract.py里添加tesseract安装路径
- 我的包安装位置：
{% raw %}
```
d:/p-program/pctools_venv/venv/Lib/site-packages/pytesseract/pytesseract.py
```
{% endraw %}


- 打开pytesseract.py，搜索tesseract_cmd，替换为tesseract安装路径
{% raw %}
```
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
{% endraw %}


## 下面是写在电脑配件里的实例

- 截图函数

{% raw %}
```py
def startShot(self):
    '''开始截图'''
    # 获取屏幕截图
    screenshot = np.array(pyautogui.screenshot())
    # 将RGB模式的屏幕截图转换为BGR模式
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 创建全屏窗口
    cv2.namedWindow("Screenshot", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Screenshot", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # 显示屏幕截图
    cv2.imshow("Screenshot", screenshot)

    # 等待用户选择区域
    region = cv2.selectROI("Screenshot", screenshot, fromCenter=False, showCrosshair=False)
    cv2.destroyAllWindows()

    # 获取用户选择的区域
    left, top, width, height = region

    # 截取用户选择的区域
    screenshot = screenshot[top:top + height, left:left + width]

    # 保存截图
    cv2.imwrite(self.jpg_path, screenshot)
```
{% endraw %}


- ocr函数

{% raw %}
```py
import pytesseract  # pip install pytesseract # 需要配置pytesseract路径

def get_text(self,jpg_path,target)->str:
    '''识别图片中的文字,返回去除空格和换行符的字符串'''
    img = Image.open(jpg_path)
    text = pytesseract.image_to_string(img, lang=target)
    text = str(text).replace(" ", "").replace("\n", "")
    return text
```
{% endraw %}

- 谷歌翻译函数

{% raw %}
```py
from deep_translator import GoogleTranslator  # pip install deep-translator

def get_translate(self,text,source,translate)->str:
    '''调用谷歌接口翻译文本\n
    source = ['ja']\n
    translate = ['zh-CN']'''
    translated = GoogleTranslator(source=source, target=translate).translate(text=text)  # Chinese translation
    return translated
```
{% endraw %}


- 日文注音函数
{% raw %}
```py
import pykakasi  # pip install Cython # pip install pykakasi

def get_romaji(self, text_jp) -> str:
    '''将输入的日文转换为罗马音输出'''
    text = text_jp
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    sentence = ""
    for item in result:
        word = item['orig']+"(%s)"%item['hira'] if not item['orig']==  item['hira'] else item['orig']
        sentence+=word
    return sentence

```
{% endraw %}
