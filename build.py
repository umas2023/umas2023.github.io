# 打包并上传Jekyll项目


commit_txt = "leet"

import os
import subprocess
import sys
script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)

print("\n===== jekyll build =====\n")
os.system("jekyll build --source hello_umas --destination docs")


print("\n===== push source =====\n")
subprocess.run(["git", "add", "."], cwd=".", shell=True)
subprocess.run(["git", "commit", "-m", commit_txt], cwd=".", shell=True)
subprocess.run(["git", "push"], cwd=".", shell=True)




