---
layout: post
title: 'vue: webpack loader'
info: '记一个得物面试问题，关于什么是webpack和loader，以及Vite'
date: 2023-10-14 16:01:56  +0800
categories: ['vue', 'knowhow']
toc: True
---


- 参考：https://juejin.cn/post/6992754161221632030
- 参考：https://zhuanlan.zhihu.com/p/104205895


## webpack

- Webpack 是一个模块化打包工具，它被广泛地应用在前端领域的大多数项目中。利用 Webpack 我们不仅可以打包 JS 文件，还可以打包图片、CSS、字体等其他类型的资源文件。而支持打包非 JS 文件的特性是基于 Loader 机制来实现的。

- webpack做的事情，仅仅是分析出各种模块的依赖关系，然后形成资源列表，最终打包生成到指定的文件中。
  

## vite和webpack

- vite

基于原生 ES-Module 的前端构建工具
Vite，一个基于浏览器原生 ES imports 的开发服务器。利用浏览器去解析 imports，在服务器端按需编译返回，完全跳过了打包这个概念，服务器随起随用。

vite是基于es modules的，因为vite不允许commonjs的规范，所以vite就不会将所有的依赖读取一遍，也就提升了运行效率；而webpack则更多的关注兼容性，webpack在启动的时候需要读取所有的依赖，统一模块化代码，再启动服务器；而vite则是直接启动服务器按需加载，未用到的模块不会加载。webpack更关注兼容性，vite关注浏览器端的开发体验。

- vite和vue-cli

vue-cli 基于 webpack 封装，生产环境和开发环境都是基于 Webpack 打包。



## loader

- Loader 本质上是导出函数的 JavaScript 模块

- 常见的loader：
  - image-loader：加载并且压缩图片文件
  - css-loader：帮助webpack打包处理css文件，使用css-loader必须要配合使用style-loader
  - style-loader：用于将css编译完成的样式，挂载到页面的style标签上。但是要注意loader执行顺序，style-loader要放在第一位，loader都是从后往前执行
  - babel-loader：把 ES6 转换成 ES5
  - sass-loader: css预处理器，能更好的编写css
  - postcss-loader: 用于补充css样式在各种浏览器的前缀，很方便，不需要手动写了
  - eslint-loader:用于检查代码是否符合规范，是否存在语法错误
  - url-loader:处理图片类型资源，可以根据图片的大小进行不同的操作，如果图片大小大于指定大小，则将图片进行资源打包，否则将图片转换为base64格式字符串，再把这个字符串打包到 JS文件里。


- loader接收三个输入参数

```js
/**
 * @param {string|Buffer} content 源文件的内容
 * @param {object} [map] 可以被 https://github.com/mozilla/source-map 使用的 SourceMap 数据
 * @param {any} [meta] meta 数据，可以是任何内容
 */
function webpackLoader(content, map, meta) {
  // 你的webpack loader代码
}
module.exports = webpackLoader;
```


- 自定义一个简单的loader

```js
function simpleLoader(content, map, meta) {
  console.log("我是 SimpleLoader");
  return content;
}
module.exports = simpleLoader;
```

-以上的 simpleLoader 并不会对输入的内容进行任何处理，只是在该 Loader 执行时输出相应的信息。Webpack 允许用户为某些资源文件配置多个不同的 Loader，比如在处理 .css 文件的时候，我们用到了 style-loader 和 css-loader，具体配置方式如下所示：

```js
// webpack.config.js

const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
     filename: 'bundle.js',
     path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
```

- Webpack 这样设计的好处，是可以保证每个 Loader 的职责单一。同时，也方便后期 Loader 的组合和扩展。比如，你想让 Webpack 能够处理 Scss 文件，你只需先安装 sass-loader，然后在配置 Scss 文件的处理规则时，设置 rule 对象的 use 属性为 ['style-loader', 'css-loader', 'sass-loader'] 即可。






## 写一个loader

- 参考：https://www.cnblogs.com/yincheng/p/webpack-loader.html



{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/vue/2023-10-14-webpack_loader/image_1.jpg) -->