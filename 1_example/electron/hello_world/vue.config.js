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
