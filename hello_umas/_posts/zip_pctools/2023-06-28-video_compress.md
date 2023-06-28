---
layout: post
title:  "pctools: video_compress 电脑配件功能:视频压缩"
info: "解决硬盘危机（暂时）"
date:   2023-06-28 10:32:00 +0800
categories: zip_pctools windows
toc: true
---


### 使用moviepy
- 官方：https://zulko.github.io/moviepy/
- 写入函数：write_videofile
  - https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=write_videofile#moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip.write_videofile
    
- 测试可用，总比特率设定2k kbps时3分钟视频仅40MB（原片4.8w kbps，60fps，大小1G），但质量较差
- 总比特率1w kbps，结果203MB
降至20fps，结果204MB，明显感觉帧数不够，帧数居然不影响视频大小

- 安装ffmpg: https://www.gyan.dev/ffmpeg/builds/
- 将bin目录添加到环境变量
- 验证安装，控制台输入：ffmpeg.exe -version


