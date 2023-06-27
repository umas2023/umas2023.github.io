# hello vue
vue项目基本操作

## hello world
- 使用vue脚手架创建一个完整的vue应用
- 项目位置: 1_example/vue/hello_world

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
- 在router/index.ts删除about页的router
- 删除views/AboutView.vue
- 修改views/HomeView.vue,添加hello world
```html
<template>
<div class="home">
    <h1>hello world</h1>
</div>
</template>
```
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
```html
<template>
  <div class="home">
    <h1>hello world</h1>
    <el-button type="danger">click</el-button>
  </div>
</template>
```

### vue.config.js

- https://cli.vuejs.org/config/#vue-config-js
- 

## 单页hello world
- 创建单个html文件的vue项目
- 项目位置: 1_example/vue/hello_world_cdn
- 下面是一个使用cdn引入vue和element-ui的例子,在vs-code中可以使用插件live-server实时查看它
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
