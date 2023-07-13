---
layout: post
title: 'amtc: mjpg-streamer给网页添加usb摄像头实时监控'
info: '学习工厂上班（摄像头拿楼上了）'
date: 2023-07-13 10:21:02  +0800
categories: ['amtc']
toc: True
---


- mjp-streamer
  - https://github.com/jacksonliam/mjpg-streamer/tree/master


- 下载编译使用

{% raw %}
```bash
apt-get install cmake libjpeg8-dev
sudo apt-get install gcc g++
```
{% endraw %}

{% raw %}
```bash
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental/
make
make install
```
{% endraw %}

- 目录下有不同的input/output.so文件，根据格式按需使用

{% raw %}
```bash
mjpg_streamer -i input_uvc.so -o output_http.so
```
{% endraw %}


- 浏览器访问`192.168.1.101:8080/?action=stream_0`


- 前端添加直播窗口

{% raw %}
```html
<img src="http://192.168.1.101:8080/?action=stream_0" />
```
{% endraw %}



