---
layout: post
title:  "crawler: bookwalker 漫画爬虫"
info: "能力有限，采用了屏幕截图的办法获取图片（实在获取不到src）"
date:   2023-06-28 10:20:00 +0800
categories: crawler
toc: true
---


- 已经集成在电脑配件项目中
  - https://github.com/umas2022/pctools

- 因为没能解析{% raw %}```<canvas>```{% endraw %}标签,没能拿到图片的地址,所以改用屏幕截图的方法保存图片
- 登录次数过多会触发网站的真人验证,所以登录的步骤改为手动,代码仅执行截图
- 代码如下


```py
'''
create: 2023.1.1
bookwalker漫画爬虫

思路:
    1. 手动启动chrome打开debug端口,转交selenium
    2. 代码截图,点击进入下一页,根据viewport0的显示状态判断点击是否成功
    3. 图片锐化(+信息删除)和截图双线程同步进行(jpg节省空间)
    4. 截图保存后检查文件大小,小于设定值的截图被判断为loading页,重新截图
问题:
    1.截图清晰度受屏幕分辨率影响,质量较低;网页截图比平板截屏质量差
    2.对div.loading状态的判断不完全可靠,检查图片大小的方法也可能存在误判
    3.保存截图会花费约0.5s,使用多线程并行运行时报错
    4.ActionChains的点击动作会花费约0.5s,需要优化

chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"

https://bookwalker.jp/bookshelf1/

'''


import time
import threading
from utils_logger.log import logger_re as logger
import os
import sys
import copy
# 删除图片信息
import piexif  # pip install piexif
# 图片锐化
from PIL import Image, ImageEnhance
# 爬虫主程序
from selenium import webdriver  # pip install selenium
# 查找元素
from selenium.webdriver.common.by import By
# 添加反爬参数
from selenium.webdriver import ChromeOptions
# 鼠标动作
from selenium.webdriver.common.action_chains import ActionChains


class CrawlerBookwalker():
    def __init__(self, json_set) -> None:
        '''只有一个total_page是必须参数,其他都有预设值'''
        try:
            # 截图总页数(设为1截取单页)
            self.total_page = int(json_set["total_page"])
            # 起始页码(截图保存命名用)
            self.current_page = int(json_set["current_page"]) if "current_page" in json_set else 1
            # 图片保存位置(路径下不要有其他图片)
            self.save_path = json_set["save_path"] if "save_path" in json_set else r"D:\s-workspace\crawler_save"
            # 图片锐化系数(1为原图,实测2效果还行)
            self.sharp_factor = int(json_set["sharp_factor"]) if "sharp_factor" in json_set else 2
            # debug模式chrome数据位置(用于chrome的脚本启动)
            self.chrome_path = json_set["chrome_path"] if "chrome_path" in json_set else r"D:\\p-data\\chrome_temp"
            # chrome端口,一般不会被占用(用于chrome的脚本启动)
            self.chrome_port = int(json_set["chrome_port"]) if "chrome_port" in json_set else 9222
            # chrome driver位置(注意要和chrome版本一致)
            # https://chromedriver.chromium.org/downloads
            self.driver_path = json_set["driver_path"] if "driver_path" in json_set else r"D:\p-tools\chromedriver\chromedriver108.exe"
            # 重新截图大小(KB)(不同截图环境loading页大小不相同)
            self.reshot_size = int(json_set["reshot_size"]) if "reshot_size" in json_set else 200
            # 截图/点击,重试次数上限
            self.retry_times = int(json_set["retry_times"]) if "retry_times" in json_set else 8
            # y轴翻页点击位置(单位:像素,顶部为0)
            self.click_point_y = int(json_set["click_point_y"]) if "click_point_y" in json_set else 300
            # x轴翻页点击位置(单位:像素,左边为0)
            self.click_point_x = int(json_set["click_point_x"]) if "click_point_x" in json_set else 100

        except Exception as e:
            logger.error("key error: %s" % e)
            return

    def __init_chrome(self):
        '''实例化浏览器'''
        option = ChromeOptions()
        option.add_experimental_option('debuggerAddress', '127.0.0.1:%d' % self.chrome_port)
        # 实例化谷歌
        driver = webdriver.Chrome(executable_path=self.driver_path, options=option)
        # 窗口尺寸不能超过显示尺寸,只能考虑找一台高分辨率显示器或者多屏拼接
        # driver.set_window_size(1080,1920)
        return driver

    def __sharpen_main(self, shot_path):
        '''子线程:图片锐化+删除信息主函数'''
        shot_path_list = shot_path.split("/")
        img = Image.open(shot_path)
        enhancer = ImageEnhance.Sharpness(img)
        im_s = enhancer.enhance(self.sharp_factor)
        shot_path_list[-1] = shot_path_list[-1].replace("shot", "sharp")
        sharp_path = "/".join(shot_path_list)
        # jpg节省点空间
        im_s = im_s.convert('RGB')
        sharp_path = sharp_path.replace(".png", ".jpg")
        im_s.save(sharp_path)
        os.remove(shot_path)
        # 删除信息(其实正常截图本来就不含信息)
        piexif.remove(sharp_path)

    def open_chrome(self):
        '''启动debug模式chrome'''
        os.system('chrome.exe --remote-debugging-port=%d --user-data-dir="%s"' % (self.chrome_port, self.chrome_path))

    def run(self):
        '''开始处理'''
        # 实例化浏览器
        driver = self.__init_chrome()

        '''进入漫画页并逐页截屏'''
        time_start = time.time()
        # 当前激活标签页为0
        driver.switch_to.window(driver.window_handles[0])
        viewport_before = driver.find_element(By.CSS_SELECTOR, 'div[id="viewport0"').is_displayed()
        for i in range(self.total_page):
            num = i + self.current_page
            # 等待loading状态结束(对loading的判断并不完全可靠,建议翻页后的wait_time>0.5s)
            div_loading = driver.find_element(By.CSS_SELECTOR, 'div[class="loading"')
            while div_loading.is_displayed():
                logger.info("loading ...")
                time.sleep(1)
            # 浏览器全屏截图(截图动作占用约0.5s,并行报错暂未解决)
            time_cost = int(time.time() - time_start)
            time_left = int(time_cost / (i + 1) * (self.total_page - i - 1))
            logger.info("shot : %d / %d , page : %d, remaining : %d s" % (i + 1, self.total_page, num, time_left))
            shot_path = os.path.join(self.save_path, "shot_%d.png" % num)
            driver.save_screenshot(shot_path)
            # 检查截图大小,小于设定值为loading页,重新截图
            shot_retry = 0
            while True:
                shot_retry += 1
                shot_size = os.path.getsize(shot_path) / 1024
                if shot_size > self.reshot_size:
                    break
                if shot_retry > self.retry_times:
                    logger.warning("shot %d times retry! file: %s" % (self.retry_times, shot_path))
                    break
                time.sleep(1)
                logger.info("shot retry %d ..." % shot_retry)
                driver.save_screenshot(shot_path)
            # 锐化程序并行进行
            th = threading.Thread(target=self.__sharpen_main, args=[shot_path], daemon=True)
            th.start()
            # 点击进入下一页(即使设置了duration,这个动作仍然会占用约0.5s的时间)
            click_retry = 0
            while True:
                click_retry += 1
                ActionChains(driver, duration=10).move_by_offset(self.click_point_x, self.click_point_y).click().move_by_offset(0 - self.click_point_x, 0 - self.click_point_y).perform()
                time.sleep(0.5)
                viewport_now = driver.find_element(By.CSS_SELECTOR, 'div[id="viewport0"').is_displayed()
                if viewport_now != viewport_before:
                    break
                else:
                    time.sleep(1)
                    viewport_now = driver.find_element(By.CSS_SELECTOR, 'div[id="viewport0"').is_displayed()
                    if viewport_now != viewport_before:
                        break
                    logger.info("click retry %d ..." % click_retry)
                    if click_retry > self.retry_times:
                        logger.error("click %d times retry!" % self.retry_times)
                        exit(1)

            viewport_before = viewport_now
            # wait_here = input("go >>")

        logger.info("shot-function finish")
        driver.quit()

```



