---
layout: post
title:  "vue: hello_world 点亮第一个站点"
info: "vue基本操作"
date:   2023-06-28 09:55:00 +0800
categories: vue
toc: true
---


## 使用docker
```
docker pull vuejs/ci
sudo docker run -itd --name vue -p 11122:22 vuejs/ci /bin/bash
sudo docker exec -it vue  /bin/bash
apt update
apt install openssh-server
echo "root:mypassword" | chpasswd
echo "PermitRootLogin yes"        >> /etc/ssh/sshd_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
npm install -g @vue/cli
```


## 直接创建项目



### 1. 创建项目
- 首先安装node.js
- 安装vue脚手架并创建项目
```
npm install  -g @vue/cli
vue create hello_world
```
- 选择项目参数
    - Please pick a preset: Manually select features
    - Check the features needed for your project: Babel, TS, Router, Vuex, CSS Pre-processors, Linter
    - Choose a version of Vue.js that you want to start the project with 3.x
    - Use class-style component syntax? Yes
    - Use Babel alongside TypeScript (required for modern mode, auto-detected polyfills, transpiling JSX)? Yes
    - Use history mode for router? 
        - (Requires proper server setup for index fallback in production) Yes (选择是否使用历史模式,不使用历史模式时使用 hash 模式)
    - Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): Sass/SCSS (with dart-sass) 
        - (选择 CSS 预处理器。node-sass 是自动编译实时的，dart-sass 需要保存后才会生效)
    - Pick a linter / formatter config: Basic 
        - (eslint 校验规则,选择第一个默认配置)
    - Pick additional lint features: Lint on save 
        - (什么时候进行代码校验。Lint on save 保存时检查， Lint and fix on commit 提交时检查)
    - Where do you prefer placing config for Babel, ESLint, etc.? In package.json 
        - (选择如何存放配置,In dedicated config files 存放到独立文件中, In package.json 存放到 package.json 中)


- 启动项目
```
cd hello_world
npm run serve
```
在默认端口 http://localhost:8080/ 可以看到hello_world已经在运行了


### 2. 修改模板
- src/App.vue,这里使用HomeView.vue作为入口  
{% raw %}
```html
<template>
<div>
    <HomeView />
</div>
</template>
<script setup lang="ts">
import HomeView from './views/HomeView.vue';
</script>
```
{% endraw %}

- 在router/index.ts删除about页的router
- 删除views/AboutView.vue
- 修改views/HomeView.vue,添加hello world
{% raw %}
```html
<template>
<div class="home">
    <h1>hello world</h1>
</div>
</template>
```
{% endraw %}

- 现在主页是hello world了

### 3. 引入element-ui
- 安装
```
npm install element-plus --save
```
- 在main.ts中引入element
```js
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
createApp(App).use(store).use(router).use(ElementPlus).mount('#app')
```
- 在views/HomeView.vue中添加一个按钮
{% raw %}
```html
<template>
  <div class="home">
    <h1>hello world</h1>
    <el-button type="danger">click</el-button>
  </div>
</template>
```
{% endraw %}

### 4. 配置vue.config.js

- https://cli.vuejs.org/config/#vue-config-js

### 5. 一些常用的包


- cookie存取：js-cookie
```
npm install --save js-cookie
```

- 图表：echarts
```
npm install --save   echarts
```

### 6. 打包

- 打包

```bash
npm run build
# 生成/dist/目录
```

- github page 打包注意
  - 默认打包时资源索引路径定位在https://github.com/umas2022/xxx，如果不是github.io项目而是其他的子项目比如backyard，主页url是https://github.com/umas2022/backyard/，此时资源索引路径需要定位在这个子目录下，修改vue.config.js:

```js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir:"../docs",
  publicPath: process.env.NODE_ENV === 'production' ? '/backyard/' : '/',
})

```


- python测试服务器

```
python.exe -m http.server 8000
```

## 单页hello world
- 创建单个html文件的vue项目
- 下面是一个使用cdn引入vue和element-ui的例子,在vs-code中可以使用插件live-server实时查看它
{% raw %}
```html
<html>

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <!-- import Vue -->
    <script src="https://unpkg.com/vue@next"></script>
    <!-- import element CSS -->
    <link rel="stylesheet" href="https://unpkg.com/element-plus/dist/index.css">
    <!-- import element JavaScript -->
    <script src="https://unpkg.com/element-plus"></script>
    <title>hello world</title>
</head>

<body>
    <div id="app">
        <div class="main">
            <h1>{{text}}</h1> <br>
            <el-button type="danger" @click="testbutton">click</el-button>
        </div>
    </div>
    <script>
        const App = {
            data() {
                return {
                    text: "hello world",
                };
            },
            methods: {
                testbutton: function () {
                    this.text = "button clicked"
                }
            }
        };
        const app = Vue.createApp(App);
        app.use(ElementPlus);
        app.mount("#app");
    </script>
</body>
<style lang="scss">
</style>

</html>
```

{% endraw %}


## 可能出现的问题



> cnpm : 无法加载文件 C:\Users\umas2017\AppData\Roaming\npm\cnpm.ps1

- 解决：管理员powershell
```
set-ExecutionPolicy RemoteSigned
```


> vue : 无法将“vue”项识别为 cmdlet、函数、脚本文件或可运行程序的名称

- 解决：

重新全局安装一遍脚手架
```
cnpm install -g vue-cli
vue -V 显示版本为2.9.6
```
卸载重装最新版
```
npm uninstall vue-cli -g
```

https://cli.vuejs.org/zh/guide/installation.html
官网提示Vue CLI 4.x 需要 Node.js v8.9 或更高版本 (推荐 v10 以上)。
```
npm -v显示版本为8.1.2
```
先更新node，安装版本管理工具nvm
https://github.com/coreybutler/nvm-windows
下载安装包setup.zip

安装显示已有node版本是16，不更新了，重装vue-cli
```
npm install -g @vue/cli
显示vue/cli版本5.0.1
```

升级
```
npm update -g @vue/cli
```
如需升级项目中的 Vue CLI 相关模块（以 @vue/cli-plugin- 或 vue-cli-plugin- 开头），请在项目目录下运行 vue upgrade




