---
layout: post
title:  "bash: init_codeserver 一键部署codeserver在ubuntu主机上"
info: "部署在ubuntu"
date:   2023-06-29 14:10:00 +0800
categories: bash
toc: true
---

- 简单介绍codeserver
  - 略

- 脚本

{% raw %}

```bash
#! /bin/bash

# ### - init_codeserver [code_server网页版vscode服务器]
# - 脚本调用
# ```setup.sh```
# - 参数修改
#     - 登录密码：/init_codeserver/setup.sh - sed (line27)
#     - 默认端口：/init_codeserver/setup.sh - sed (line28)
#     - 安装版本：/init_codeserver/setup.sh - version (line6)
# - 注意
#     - curl直接从github下载，可能无法访问
#     - 默认下载amd64版本，在脚本中按需修改
#     - 默认使用端口8081
#     - code-server不能在vscode中启动，报错error Please specify at least one file or folder

# # github官方仓库
# https://github.com/coder/code-server/releases


version="4.6.0" # 2022.8.21
package="code-server-$version-amd64.rpm" # for wsl
# package="code-server-$version-arm64.rpm" # for android termux / linux
# package="code-server-$version-armhfp.rpm" # for raspberry pi (?)
port=8081
user="root"

# 确认参数
echo -e "\npackage select: $package"
echo -e "user: $user"
echo -e "port : $port\npress enter to continue..."
read -r input



# 检查是否已经安装
if [ -d "/$user/.config/code-server" ];then
    echo "code-server already installed"
    exit 1
fi

# 创建.user_profile文件并写入.bashrc启动项
if [ ! -e ~/.user_profile ];then
    touch ~/.user_profile
else
    echo "user_profile already exist"
fi
if !( cat /$user/.bashrc | grep "user_profile" > /dev/null );then
    echo -e "\necho 'setup command : ~/.user_profile'\n" >> /$user/.bashrc
    echo -e "if [ -f ~/.user_profile ]; then\n\t. ~/.user_profile\nfi" >> /$user/.bashrc
else
    echo "user_profile already loaded in bashrc"
fi

# 下载rpm包并安装
if [ ! -e $package ];then
    curl -OL https://github.com/coder/code-server/releases/download/v$version/$package
fi
rpm -ivh $package
rm $package

# 首次运行生成config文件
code-server > /dev/null 2>&1 &
echo -e "\n\nsleep 5s, waiting for the end of the first operation ...\n\n"
sleep 5
echo -e "\nmaybe done\n"
# 配置密码和端口，0.0.0.0代表本机所有ip地址
sed -i "/^password:*/cpassword: umas1970" ~/.config/code-server/config.yaml
sed -i "/^bind-addr:*/cbind-addr: 0.0.0.0:$port" ~/.config/code-server/config.yaml



# 加入.user_profile启动项
if !( cat /$user/.user_profile | grep "user profile: code-server" > /dev/null );then
    echo "# user profile: code-server" >> /$user/.user_profile
    echo "echo ' * code-server port $port starting ...'" >> /$user/.user_profile
    echo "code-server > /dev/null 2>&1 &" >> /$user/.user_profile
    # echo "nohup code-server &" >> /$user/.user_profile
fi

echo -e "\ncode-server setup finish\n"


```

{% endraw %}
