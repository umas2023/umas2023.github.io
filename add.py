'''
2023.7.1
创建新文章
- 每次新建文章都要手动按时间命名，还要添加yaml头，挺麻烦的
- 添加图片创建目录也很麻烦
- 所以做了这个

- 分类快捷copy

amtc
bash
cpp
crawler
css
django
docker
electron
git
jekyll
js
knowhow
linux
markdown
mysql
nginx
pyqt
python
raspberry_pi
tampermonkey
ts
vue
windows
zip_backyard
zip_pctools
'''


# 修改这里：md文件名后面会跟时间拼接起来
file_name = "terraria"
# 修改这里：md文件放在哪个目录下
dir = "windows"
# 修改这里：文章标题
title = "'windows: 华为云搭建泰拉瑞亚云服务器'"
# 修改这里：文章介绍
info = "'泰拉瑞亚服务器'"
# 修改这里：文章分类
categories = ["windows"]


import os
from datetime import datetime
import sys
script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)


yaml = {
    'layout': "post",
    'title': title,
    'info': info,
    # 注意时间必须要有+0800才能正确识别
    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S %z") + " +0800",
    'categories': categories,
    'toc': True,
}


# 创建md文件
file_name = datetime.now().strftime("%Y-%m-%d") + "-" + file_name
file_name_md = file_name + ".md"
file_path = os.path.normpath(os.path.join(script_path, "hello_umas/_posts", dir, file_name_md))
with open(file_path, "w+", encoding="utf-8") as md:
    md.write("---\n")
    for key in yaml:
        md.write(str(key))
        md.write(": ")
        md.write(str(yaml[key]))
        md.write("\n")
    md.write("---\n")
    # 写入一张图片
    md.write("\n\n![引入图片]({{site.url}}/image/%s/%s/image_1.jpg)" % (dir, file_name))
    # 写入raw代码
    md.write("\n\n{% raw %}\n")
    md.write("```\n")
    md.write("```\n")
    md.write("{% endraw %}\n")



# 创建图片目录
image_path = os.path.normpath(os.path.join(script_path,"hello_umas/image",dir,file_name))
gitkeep = os.path.normpath(os.path.join(image_path,".gitkeep"))
if not os.path.exists(image_path):
    os.makedirs(image_path)
with open(gitkeep,"w+") as keep:
    pass

# 打开图片目录
os.system("explorer.exe %s" % image_path)

# 打开新md文件
vscode = r'"D:\p-program\vscode\Microsoft VS Code\Code.exe"'
os.system("%s %s" % (vscode,file_path))
