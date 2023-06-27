# bug记录


## cnpm : 无法加载文件 C:\Users\umas2017\AppData\Roaming\npm\cnpm.ps1

- 解决：管理员powershell
```
set-ExecutionPolicy RemoteSigned
```


## vue : 无法将“vue”项识别为 cmdlet、函数、脚本文件或可运行程序的名称

- 解决：

重新全局安装一遍脚手架

cnpm install -g vue-cli
vue -V 显示版本为2.9.6

卸载重装最新版
npm uninstall vue-cli -g

https://cli.vuejs.org/zh/guide/installation.html
官网提示Vue CLI 4.x 需要 Node.js v8.9 或更高版本 (推荐 v10 以上)。

npm -v显示版本为8.1.2
先更新node，安装版本管理工具nvm
https://github.com/coreybutler/nvm-windows
下载安装包setup.zip

安装显示已有node版本是16，不更新了，重装vue-cli

npm install -g @vue/cli
显示vue/cli版本5.0.1

升级
npm update -g @vue/cli
如需升级项目中的 Vue CLI 相关模块（以 @vue/cli-plugin- 或 vue-cli-plugin- 开头），请在项目目录下运行 vue upgrade




