---
layout: post
title:  "electron: hello_world 从0开始搭建electron项目"
info: "从0开始搭建electron项目"
date:   2023-06-27 23:00:00 +0800
categories: electron
toc: true
---



##  一个简单的窗口
- 首先参见 vue/hello_world.md 创建一个基于vue的 hello world 项目
- 在项目中添加electron支持
```
vue add electron-builder
(Electron Version ^13.0.0)
```

- 在package.json中可以看到新增的命令
```
npm run electron:serve
npm run electron:build
```

- 直接使用```npm run electron:serve```启动测试时background.ts可能会报错Object is of type 'unknown',需要手动给报错的变量定义类型:any
```
catch (e) 改为 catch (e:any)
```

- 还有可能报错TypeError: loaderContext.getOptions is not a function,需要降低ts-loader的版本到8.2.0
```
npm install ts-loader@~8.2.0
```

- 还有可能在src/router/index.ts中报错File 'xxx/src/views/HomeView.vue.ts' is not a module.,这是因为HomeView.vue缺少了export,简单的修改方法是添加setup参数
```html
<script setup lang="ts">
或者
<script lang="ts">
export default {};
</script>
```

## 常用的一些打包选项
- 在vue.config.js中设置打包选项
{% raw %}
```js
const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  // 静态资源打包目录
  assetsDir: "static",

  // electron打包选项
  pluginOptions: {
    electronBuilder: {
      builderOptions: {
        "productName": "电脑配件", // 程序名
        "appId": "toolbox", // 包名
        "copyright": "umasnb", // 版权
        // "asar": true, // asar打包的python无法运行
        "asar": false, // 不使用asar打包

        // 复制到根目录/resources下
        extraResources: [
          "src/assets", // 相当于{ from: 'src/assets', to: 'src/assets' }
          // { from: 'src/assets', to: 'assets' }, // assets资源目录指定
          { from: 'public/static', to: 'static' }, // public静态资源拷贝目录,程序中用static/xxx可以直接访问
          { from: "../0-docs/develop.md", to: "static/info/develop.md" }//开发日志也打包进去
        ],

        // "directories": {
        //   "output": "dist_hello" // 输出文件夹
        // },

        "nsis": {
          "oneClick": false, // 是否一键安装
          "allowElevation": true, // 允许请求提升。若为false, 则用户必须使用提升的权限重新启动安装程序。
          "allowToChangeInstallationDirectory": true, //是否允许修改安装目录
          // "installerIcon": "public/static/icon/mati_spa_128.ico",// 安装时图标
          // "uninstallerIcon": "",//卸载时图标
          // "installerHeaderIcon": "", // 安装时头部图标
          "createDesktopShortcut": true, // 是否创建桌面图标
          "createStartMenuShortcut": true,// 是否创建开始菜单图标
          "shortcutName": "快速电脑配件", // 快捷方式名称
          "runAfterFinish": false,//是否安装完成后运行
        },
        "win": {
          // "icon": "public/static/icon/mati_ei_256.ico", // 打包图标
          "target": [
            {
              "target": "nsis", //利用nsis制作安装程序
              "arch": [
                "x64", //64位
                // "ia32" //32位
              ]
            }
          ]
        }
      },
      // 附加包列表
      externals: ['image-size', 'js-cookie']
    }
  }
});

```
{% endraw %}


## 窗口的一些附加参数

```js
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    frame: false,        // 隐藏默认窗口边框
    title:"hello_title", // 标题属性不能生效,真正的标题在public/index.html中
    resizable: false,    // 指定窗口是否可以被用户调整大小
    minimizable: false,  // 指定窗口是否可以被最小化或最大化
    maximizable: false, 
    fullscreen: true,    // 指定窗口是否全屏显示
    backgroundColor: "red", // 背景颜色
    transparent: true, // 指定窗口是否为透明,如果设置为 true,则可以使用 setOpacity 方法来设置窗口的透明度
  })

  // 设置窗口透明度,需要transparent: true
  win.setOpacity(0.5)
```





