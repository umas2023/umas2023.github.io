# nodejs基本操作

- 安装node.js：  
windows百度安装：https://nodejs.org/zh-cn/  
ubuntu：sudo apt install nodejs npm

- 查看版本
```
node -v
npm -v
```

- 更新nodejs：
```
sudo npm install n -g
sudo n stable
```

- 更新npm：
```
sudo npm install npm@latest -g
```

- cnpm国内镜像（二选一）：
```
sudo npm install -g cnpm --registry=https://registry.npmmirror.com
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org
```

- 或给npm改源（推荐）
```
sudo npm config set registry https://registry.npm.taobao.org
```
- vue脚手架：
```
sudo npm install -g @vue/cli
```
Vue CLI 的包名称由 vue-cli 改成了 @vue/cli。 如果你已经全局安装了旧版本的 vue-cli (1.x 或 2.x)，你需要先通过 npm uninstall vue-cli -g 或 yarn global remove vue-cli 卸载它。
(https://cli.vuejs.org/zh/guide/installation.html)


