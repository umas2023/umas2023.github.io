'''
2023.7.1
创建新文章
- 每次新建文章都要手动按时间命名，还要添加yaml头，挺麻烦的
- 添加图片创建目录也很麻烦
- 所以做了这个
'''


# 修改这里：md文件名
file_name = "add_new_test"
# 修改这里：md放在哪个目录下
dir = "jekyll"
# 修改这里：文章标题
title = "title"
# 修改这里：文章介绍
info = "info"
# 修改这里：文章分类
categories = ["jekyll"]


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
    md.write("\n\n![引入图片]({{site.url}}/image/%s/%s/image_1.png)" % (dir, file_name))
    # 写入raw代码
    md.write("\n\n{% raw %}\n")
    md.write("```\n")
    md.write("```\n")
    md.write("{% endraw %}\n")



# 创建图片目录
image_path = os.path.normpath(os.path.join(script_path,"hello_umas/image",dir,file_name))
gitkeep = os.path.normpath(os.path.join(image_path,".gitkeep"))
with open(gitkeep,"w+") as keep:
    pass