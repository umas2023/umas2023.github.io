---
layout: post
title:  "zip_backyard: duplicate_rm 弔图主页后端图片去重"
info: "由于华为云同步问题，许多图片被重复上传，目标是找出并删除这些内容完全一致的文件（文件名可能不同）"
date:   2023-06-28 22:10:00 +0800
categories: zip_backyard
toc: true
---


## about
- 项目脚本：
  - https://github.com/umas2022/backyard_store/blob/main/duplicate_rm.py



## 准备

- 图片遍历
{% raw %}
```py
def get_file(path_in):
    '''所有层级文件遍历'''
    for root, dirs, files in os.walk(path_in):
        for fileName in files:
            if fileName == ".gitkeep":
                continue
            full_path = os.path.normpath(os.path.join(root, fileName))
            yield full_path
```
{% endraw %}

- 结果保存json
{% raw %}
```py
# 写入结果
duplicate_list = {
        "sticker": duplicate_sticker_list,
        "image": duplicate_image_list
    }
with open(result_json, 'w', encoding="utf-8") as file:
    js_str = json.dumps(duplicate_list, ensure_ascii=False)
    file.write(js_str)
```
{% endraw %}


## hash过滤

- 过滤函数

{% raw %}
```py
def hash_filter(image_paths):
    '''寻找相同图片(哈希)'''
    image_hashes = defaultdict(list)
    duplicate_dict = defaultdict(list)
    for image_path in image_paths:
        image = Image.open(image_path)
        image_hash = imagehash.average_hash(image)
        image_hashes[image_hash].append(image_path)

        if len(image_hashes[image_hash]) > 1:
            duplicate_dict[image_hash] = list(set(duplicate_dict[image_hash] + image_hashes[image_hash]))
            print("\nfind duplicate : ")
            for item in duplicate_dict[image_hash]:
                print(item)

    duplicate_list = [image_list for image_list in duplicate_dict.values()]

    return duplicate_list
```
{% endraw %}


- 加入计时函数对表情包测试效果：
{% raw %}
```py
# 表情包查重
now = time.time()
sticker_list = [img for img in get_file(sticker_path)]
duplicate_sticker_list = hash_filter(sticker_list)
time_spent_ms = int(1000 * (time.time() - now))
time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
print(time_spent)
```
{% endraw %}
- 结果9.671s，共输出7组重复，人工检查输出结果发现没有哈希冲突（误判）
- 表情包和沙雕图一起检查，用时104.542s，人工检查发现沙雕图区输出的结果有大量的冲突


## 仅判断尺寸

- 过滤函数
{% raw %}
```py
def dim_filter(image_paths):
    '''寻找相同图片(尺寸)'''
    image_dims = defaultdict(list)
    duplicate_dict = defaultdict(list)
    for image_path in image_paths:
        image = Image.open(image_path)
        width, height = image.size
        image_dim = str(width)+"-"+str(height)
        image_dims[image_dim].append(image_path)

        if len(image_dims[image_dim]) > 1:
            duplicate_dict[image_dim] = list(set(duplicate_dict[image_dim] + image_dims[image_dim]))
            print("\nfind duplicate : ")
            for item in duplicate_dict[image_dim]:
                print(item)

    duplicate_list = [image_list for image_list in duplicate_dict.values()]

    return duplicate_list
```
{% endraw %}


- 加入计时函数对表情包测试效果：
{% raw %}
```py
# 表情包查重
now = time.time()
sticker_list = [img for img in get_file(sticker_path)]
# duplicate_sticker_list = hash_filter(sticker_list)
duplicate_sticker_list = dim_filter(sticker_list)
time_spent_ms = int(1000 * (time.time() - now))
time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
print(time_spent)
```
{% endraw %}
- 结果0.990s，虽然很快但和预想一样，尺寸相同但内容不同的图片很多，共输出了34组结果
- 可以作为预筛选


## 仅判断体积

- 过滤函数
{% raw %}
```py
def size_filter(image_paths):
    '''寻找相同图片(大小)'''
    image_size_list = defaultdict(list)
    duplicate_dict = defaultdict(list)
    for image_path in image_paths:
        image = Image.open(image_path)
        width, height = image.size
        img_size = os.path.getsize(image_path)
        image_size_list[img_size].append(image_path)

        if len(image_size_list[img_size]) > 1:
            duplicate_dict[img_size] = list(set(duplicate_dict[img_size] + image_size_list[img_size]))
            print("\nfind duplicate : ")
            for item in duplicate_dict[img_size]:
                print(item)

    duplicate_list = [image_list for image_list in duplicate_dict.values()]

    return duplicate_list
```
{% endraw %}


- 加入计时函数对表情包测试效果：
{% raw %}
```py
# 表情包查重
now = time.time()
sticker_list = [img for img in get_file(sticker_path)]
# duplicate_sticker_list = hash_filter(sticker_list)
# duplicate_sticker_list = dim_filter(sticker_list)
duplicate_sticker_list = size_filter(sticker_list)
time_spent_ms = int(1000 * (time.time() - now))
time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
print(time_spent)
print(len(duplicate_sticker_list))
```
{% endraw %}
- 结果0.480s，意料之外的是仅输出了5组结果
- 和hash结果对比发现确实存在体积不同但内容和分辨率相同的图片，检查发现体积较小的图片的水平和垂直分辨率都是1dpi，这类重复可能不是由华为云的错误同步导致的。（可能是qq群收的图片被压缩？尚待验证）



## 整合

- 由于体积判断存在漏判，所以暂不选用
- 用尺寸判断作为哈希判断的预筛选，代码如下
{% raw %}
```py
# 表情包查重
now = time.time()
sticker_list = [img for img in get_file(sticker_path)]
duplicate_list_dim = dim_filter(sticker_list)
duplicate_list_hash = []
for list_dim in duplicate_list_dim:
    if not hash_filter(list_dim) == []:
        duplicate_list_hash.append(hash_filter(list_dim)[0]) 
duplicate_sticker_list = duplicate_list_hash
time_spent_ms = int(1000 * (time.time() - now))
time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
print(time_spent)
print(len(duplicate_sticker_list))
```
{% endraw %}

- 用时2.047s，结果和单hash一致输出了7组，没有误判
- 加入沙雕图一起筛选，用时23.988s，沙雕图输出了21组结果，检查发现推特@meetissai的截图全都被判断为相同了
- 把hash过滤中的均值哈希average_hash()改为感知哈希phash()，沙雕图输出18组结果，检查没有发现错误

- PIL库中支持的其他hash函数
```
均值哈希（Average Hash）：average_hash()
感知哈希（Perceptual Hash）：phash()
差异哈希（Difference Hash）：dhash()
块哈希（Block Hash）：block_mean_hash()
渐变哈希（Gradient Hash）：gradient_hash()
```

- 区别
  - 均值哈希（Average Hash）：将图像缩小为固定大小，计算图像的平均灰度值，并将每个像素与平均值进行比较，生成二进制哈希值。适用于图像整体相似度的比较。

  - 感知哈希（Perceptual Hash）：基于离散余弦变换（DCT）来提取图像的频率特征。通过计算图像的DCT变换系数，并根据变换系数的高低生成二进制哈希值。适用于在不同尺度和旋转下仍具有相似感知的图像比较。

  - 差异哈希（Difference Hash）：计算图像相邻像素之间的差异，并根据差异生成二进制哈希值。适用于检测图像的微小变化或图像剪裁的比较。

  - 块哈希（Block Hash）：将图像划分为多个块，计算每个块的平均灰度值，并将每个块的灰度与整体平均灰度进行比较，生成二进制哈希值。适用于在局部区域内比较图像相似度。

  - 渐变哈希（Gradient Hash）：基于图像梯度的方向和强度来生成哈希值。通过计算图像的梯度信息，并根据梯度的方向和强度生成二进制哈希值。适用于检测图像的边缘和纹理的比较。



## 完整代码

{% raw %}
```py
'''
图片去重
对比图片哈希, 只能找出像素完全相同的图片
'''

import json
import os
from PIL import Image
import imagehash  # pip install imagehash
from collections import defaultdict
import cv2
import numpy as np
import skimage.metrics
import skimage.measure
import time

import sys
script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)


# auto_rm = False
result_json = os.path.normpath(os.path.join(script_path, "output/duplicate.json"))
sticker_path = os.path.normpath(os.path.join(script_path, "storage/sticker"))
image_path = os.path.normpath(os.path.join(script_path, "storage/image"))


def get_file(path_in):
    '''所有层级文件遍历'''
    for root, dirs, files in os.walk(path_in):
        for fileName in files:
            if fileName == ".gitkeep":
                continue
            full_path = os.path.normpath(os.path.join(root, fileName))
            yield full_path


def hash_filter(image_paths):
    '''寻找相同图片(哈希)'''
    image_hashes = defaultdict(list)
    duplicate_dict = defaultdict(list)
    for image_path in image_paths:
        image = Image.open(image_path)
        # image_hash = imagehash.average_hash(image)
        image_hash = imagehash.phash(image)
        image_hashes[image_hash].append(image_path)

        if len(image_hashes[image_hash]) > 1:
            duplicate_dict[image_hash] = list(set(duplicate_dict[image_hash] + image_hashes[image_hash]))
            print("\nfind duplicate : (hash)")
            for item in duplicate_dict[image_hash]:
                print(item)

    duplicate_list = [image_list for image_list in duplicate_dict.values()]

    return duplicate_list


def dim_filter(image_paths):
    '''寻找相同图片(尺寸)'''
    image_dims = defaultdict(list)
    duplicate_dict = defaultdict(list)
    for image_path in image_paths:
        image = Image.open(image_path)
        width, height = image.size
        image_dim = str(width) + "-" + str(height)
        image_dims[image_dim].append(image_path)

        if len(image_dims[image_dim]) > 1:
            duplicate_dict[image_dim] = list(set(duplicate_dict[image_dim] + image_dims[image_dim]))
            print("\nfind duplicate (dimension): ")
            for item in duplicate_dict[image_dim]:
                print(item)

    duplicate_list = [image_list for image_list in duplicate_dict.values()]

    return duplicate_list


def size_filter(image_paths):
    '''寻找相同图片(大小)'''
    '''实际测试发现了一些分辨率和尺寸都相同但大小不同的图片，因此不采用这个方法'''
    image_size_list = defaultdict(list)
    duplicate_dict = defaultdict(list)
    for image_path in image_paths:
        image = Image.open(image_path)
        width, height = image.size
        img_size = os.path.getsize(image_path)
        image_size_list[img_size].append(image_path)

        if len(image_size_list[img_size]) > 1:
            duplicate_dict[img_size] = list(set(duplicate_dict[img_size] + image_size_list[img_size]))
            print("\nfind duplicate (size): ")
            for item in duplicate_dict[img_size]:
                print(item)

    duplicate_list = [image_list for image_list in duplicate_dict.values()]

    return duplicate_list


# 表情包查重
sticker_list = [img for img in get_file(sticker_path)]
duplicate_list_dim = dim_filter(sticker_list)
duplicate_list_hash = []
for list_dim in duplicate_list_dim:
    if not hash_filter(list_dim) == []:
        duplicate_list_hash.append(hash_filter(list_dim)[0])
duplicate_sticker_list = duplicate_list_hash


# 图片查重
image_list = [img for img in get_file(image_path)]
duplicate_list_dim = dim_filter(image_list)
duplicate_list_hash = []
for list_dim in duplicate_list_dim:
    if not hash_filter(list_dim) == []:
        duplicate_list_hash.append(hash_filter(list_dim)[0])
duplicate_image_list = duplicate_list_hash


# 写入结果
duplicate_list = {
    "sticker": duplicate_sticker_list,
    "image": duplicate_image_list
}
with open(result_json, 'w', encoding="utf-8") as file:
    js_str = json.dumps(duplicate_list, ensure_ascii=False)
    file.write(js_str)


del_list = duplicate_sticker_list + duplicate_image_list

wait_here = input("\n\nFind Find %d sets of duplicate images.\n\
Press Enter to delete duplicate images. Press Ctrl+C to exit.\n\
It is recommended to check './output/duplicate.json' before deleting ..." %len(del_list))



for dp_list in del_list:
    for image in dp_list[1:]:
        print("delete: %s" % image)
        os.remove(image)

```
{% endraw %}