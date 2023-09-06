---
layout: post
title: 'python: 使用python驱动声卡播放音频(ubuntu)'
info: 'python通过wave库来实现，ubuntu可以用aplay命令播放'
date: 2023-09-06 14:16:58  +0800
categories: ['python']
toc: True
---


## ubuntu命令行播放音频

- aplay命令
```bash
sudo apt install alsa-utils
```

- 查看声卡设备
``` bash
cat /proc/asound/cards
```

- 指定声卡播放   
```bash
aplay -D default Hinomi_Chinese_lijun.wav
aplay -D plughw:2 Hinomi_Chinese_lijun.wav
```


## excel转json
- 由于拿到的目录是excel格式不方便程序操作，先转为json

```py
'''原程序找不到了，目录下面只有这个↓'''

import openpyxl # pip install openpyxl

def load_each_sheet():
    wb = openpyxl.load_workbook(filePath)
    for sheet in wb.worksheets:
        if sheet.title not in exceptSheets:
            yield wb, sheet
    fileNameOut = fileName.split(".xlsx")[0] + "-out.xlsx"
    wb.save(os.path.join(fileDir, fileNameOut))

```


## py播放音频

```py
import json
import os
import wave # pip install wave
import time
import threading


class SayHello:

    def __init__(self,
                 package_path='/home/nuc/test_voice_play/nio-voice',
                 default_sleep_time=3,
                 default_sound_volume=80):
        self.package_path = package_path
        self.default_sleep_time = default_sleep_time
        self.default_sound_volume = default_sound_volume

    # Get audio file duration
    def get_duration(self, path: str) -> float:
        wavfile = wave.open(path, 'rb')
        params = wavfile.getparams()
        framesra, frameswav = params[2], params[3]
        time = 1.0 / framesra * frameswav
        return time

    # Modify playback volume
    def set_volume(self, volume: int, card=0) -> None:
        '''
        Modify playback volume  \n
        volume : 0~100  \n
        card : default = 0 \n
        '''
        if volume > 100 or volume < 0:
            print("Ranges : 0 < volume < 100")
            return
        self.default_sound_volume = volume
        volume_percent = str(volume) + "%"
        os.system('amixer set -c %s Master %s 1>/dev/null 2>&1' % (str(card), volume_percent))

    # play one audio file
    def play_one(self, cmdstr: str, card=0, volume=80) -> str:
        '''
        play one single .wav file, return wav file path and content  \n
        cmdstr : eg:"Basic/wakeup/adult_male_nature"  \n
        card : default = 0  \n
        volume : default = 80
        '''
        try:
            self.set_volume(volume=volume, card=card)
        except BaseException:
            print("volume set error")
            return

        with open(os.path.join(self.package_path, "Voiceconfig.json"), 'r') as load_f:
            config = json.load(load_f)
            cmdlist = cmdstr.split("/")
            wav_path = ""
            try:
                wav_path = config[cmdlist[0]][cmdlist[1]][cmdlist[2]]["file"]
                wav_path = os.path.join(self.package_path, wav_path)
                content = config[cmdlist[0]][cmdlist[1]][cmdlist[2]]["content"]
                print("content : %s" % content)
                os.system('aplay -D plughw:%s %s 1>/dev/null 2>&1' % (str(card), wav_path))
                return wav_path
            except BaseException:
                print("command input illegal")
                return

    # play multi audio file by step in a list
    def play_step(self, cmdlist: [{"cmd": str, "sleep": int}], card=0, volume=80) -> None:
        '''
        play multi .wav file sequentially at once  \n
        sleep: default = 3
        card : default = 0  \n
        volume : default = 80
        '''
        for each_cmd in cmdlist:

            sleep_time = self.default_sleep_time
            if "sleep" in each_cmd:
                sleep_time = each_cmd["sleep"]

            try:
                wav_path = self.play_one(cmdstr=each_cmd['cmd'], card=card, volume=volume)
                print("sleep : %fs" % sleep_time)
                time.sleep(self.get_duration(wav_path) + sleep_time)
            except BaseException:
                print("command input illegal")
                return

    # Drive multiple sound cards at the same time
    def play_parallel(self, playlist: [{"card": int, "step": list, "volume": int}]) -> None:
        '''
        Drive multiple sound cards at the same time \n
        card : sound card number  \n
        step : eg. [{"cmd": "Basic/wakeup/adult_male_nature", "sleep": 2}]
        volume : default = 80
        '''
        thread_list = [i for i in range(len(playlist))]
        for i in range(len(playlist)):
            card = playlist[i]["card"]
            step = playlist[i]["step"]
            volume = self.default_sound_volume
            if "volume" in playlist[i]:
                volume = playlist[i]["volume"]
            thread_list[i] = threading.Thread(target=self.play_step, args=(step, card))

        try:
            for each_thread in thread_list:
                each_thread.start()
        except Exception as e:
            print("thread error : " + e)

```

## 功能

1. 单条指令播放

```python
a.play_one("Basic/wakeup/adult_male_nature")
```

2. 多条指令连续播放
参数card, volume, sleep有预设值

```python
a.play_step(
    card=0,
    volume=50,
    cmdlist=[
        {"cmd": "Basic/wakeup/adult_male_nature"},
        {"cmd": "Control/open_window/adult_male_nature", "sleep": 3},
        {"cmd": "Control/close_window/adult_male_nature", "sleep": 0}
    ])
```

3. 多声卡并行播放
参数sleep, volumn有预设值

```python
play_0 = [
    {"cmd": "Basic/wakeup/adult_male_nature", "sleep": 2},
    {"cmd": "Control/open_window/adult_male_nature", "sleep": 3},
    {"cmd": "Control/close_window/adult_male_nature", "sleep": 0}
]

play_1 = [
    {"cmd": "Basic/wakeup/adult_male_nature", "sleep": 2},
    {"cmd": "Control/open_window/adult_male_nature", "sleep": 3},
    {"cmd": "Control/close_window/adult_male_nature", "sleep": 0}
]

a.play_parallel([
    {"card": 0, "step": play_0, "volume": 60},
    {"card": 1, "step": play_1}
])
```

<!-- ![引入图片]({{site.url}}/image/python/2023-09-06-nio_voice_play/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}


