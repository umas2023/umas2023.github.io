---
layout: post
title: 'vue: 组件入门'
info: '组件传参，slot，其他用到再补'
date: 2023-08-24 19:50:10  +0800
categories: ['vue']
toc: True
---




## 组件传参

- props官方：https://cn.vuejs.org/guide/components/props#prop-passing-details



{% raw %}
<!-- 子组件类型定义 -->
```ts
const props = defineProps<{
    type: string 
}>();

const props = defineProps({
    type: {
        type: String,
        require: false
    }
});
```
{% endraw %}

{% raw %}
```html
<!-- 父组件 -->
<MyComponent greeting-message="hello" />
```
{% endraw %}


- defineProps不需要手动引入，但一些情况下可能报错 'defineProps' is not defined  no-undef
- 解决：在根目录下创建.eslintrc.js，写入以下内容
{% raw %}
```js
module.exports = {
    root: true,
    env: {
      node: true,
    },
    extends: [
      'plugin:vue/vue3-essential',
      '@vue/typescript/recommended',
    ],
    parserOptions: {
      parser: '@typescript-eslint/parser',
    },
    rules: {
      // 自定义规则可以在这里添加
    },
  };
```
{% endraw %}


## slot
  - 官方：https://cn.vuejs.org/guide/components/slots.html#slots
		

{% raw %}
```html
<!-- 组件 -->
<FancyButton>
  Click me! <!-- 插槽内容 -->
</FancyButton>
```
{% endraw %}
		
{% raw %}
```html
<!-- 模板 -->
<button class="fancy-btn">
  <slot></slot> <!-- 插槽出口 -->
</button>
```
{% endraw %}


- 具名插槽

{% raw %}
```html
<div class="container">
  <header>
    <slot name="header"></slot>
  </header>
  <main>
    <slot></slot>
  </main>
  <footer>
    <slot name="footer"></slot>
  </footer>
</div>
```
{% endraw %}



{% raw %}
```html
<BaseLayout>
  <template v-slot:header>
    <!-- header 插槽的内容放这里 -->
  </template>
</BaseLayout>
```
{% endraw %}



## 动态导入文件夹下所有组件

- 参考：https://stackoverflow.com/questions/54344164/how-to-import-all-vue-components-from-a-folder


{% raw %}
```js
const ComponentContext = require.context('./', true, /\.vue$/i, 'lazy');

ComponentContext.keys().forEach((componentFilePath) => {

    const componentName = componentFilePath.split('/').pop().split('.')[0];
    Vue.component(componentName, () => ComponentContext(componentFilePath));

});

```
{% endraw %}



- 其中```require.context(directory,useSubdirectories,regExp)```
  - directory:表示检索的目录
  - useSubdirectories：表示是否检索子文件夹
  - regExp:匹配文件的正则表达式,一般是文件名


- 如果目标是html文件，可能会需要附加插件
```
npm install --s html-loader
```

- 然后在vue.config.js里加入

```js
chainWebpack: config => {
    config.module
      .rule('html') 
      .test(/\.html$/)
      .use('html-loader')
      .loader('html-loader')
  }
```



<!-- ![引入图片]({{site.url}}/image/vue/2023-08-24-vue_components/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
