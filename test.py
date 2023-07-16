

import os
import shutil

src_dir = r"./inner_vue/dist"
dst_dir = r"./hello_umas"
# 遍历源目录下的所有文件和子目录
for root, dirs, files in os.walk(src_dir):
    dst_root = os.path.join(dst_dir, os.path.relpath(root, src_dir))
    # 如果目标目录不存在，则先创建目标目录
    if not os.path.exists(dst_root):
        os.makedirs(dst_root)
    # 遍历当前目录下的所有文件
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dst_root, file)
        # 如果目标文件已经存在，则先删除目标文件
        if os.path.exists(dst_file):
            os.remove(dst_file)
        # 复制文件
        shutil.copy(src_file, dst_file)
