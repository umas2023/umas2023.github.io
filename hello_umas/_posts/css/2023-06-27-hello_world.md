---
layout: post
title:  "css: hello_world 基础语法"
info: "css/scss基础语法"
date:   2023-06-27 11:00:00 +0800
categories: css
toc: true
---


## 常用的属性


### 圆角

```css
border-radius: 20px;
border-radius: 50% / 100% 100% 0 0;
/* 表示水平和垂直方向上的四个角都具有相同的圆角半径，半径的大小是元素宽度和高度的50%。 */
/* 100% 100% 0 0：表示分别设置了左上角、右上角、右下角和左下角的圆角半径。具体数值表示的是相对于元素宽度和高度的百分比 */
/* 上面这行生成一个半圆形 */
```

### 旋转

```
transform = rotate(180deg)
```


### 运动

- 使用keyframes定义关键帧
```css
@keyframes dance-animation {
  0% { transform: translate(0, 0); }
  25% { transform: translate(100px, 0); }
  50% { transform: translate(100px, 100px); }
  75% { transform: translate(0, 100px); }
  100% { transform: translate(0, 0); }
}


animation: dance-animation 4s infinite;
```




## scss基本语法
{:toc}

### 多class
- 多个class用空格叠加，可以赋予多个属性，结合动态class名可以实现动态样式

```html
<div class="padding10 inline">
```
```scss
div.inline {
  display: inline-block;
}
.padding10 {
  padding: 10px;
}
```

- class空格叠加时单独定义样式，此时css语句中点是连续的

```html
<div class="box rai">
<div class="box di">
```
```scss
div.box.rai { ... }
div.box.di { ... }
```

- 多级叠加时css用空格分开
  
```html
<div class="box di">
<div class="select">
```
```scss
div.box.rai .select { …
```

- 上面的空格等价于多级嵌套
  
```scss
div.box.rai { …
  .select { … }
}
```	
		

### import导入外部样式
  
```scss
<style scoped lang="scss">
@import 'animate.css';
```




## 选择器

### 兄弟选择器："~"
- 例子: 有两个并列的div,当鼠标悬停在div-1时它的宽度增加200,同时div-2的宽度减少200

```html
<div class="container">
<div class="div-1"></div>
<div class="div-2"></div>
</div>
```
```css
.container {
  display: flex;
}

.div-1 {
  width: 200px;
  height: 100px;
  background-color: red;
  transition: width 0.3s ease;
}

.div-2 {
  width: 200px;
  height: 100px;
  background-color: blue;
  transition: width 0.3s ease;
}

.div-1:hover {
  width: 400px;
}

.div-1:hover ~ .div-2 {
  width: 0px;
}

```

### 父元素引用："&"
- &用来引用父元素，例：
  
```scss
.side-container {
&.unfolded {
....
```

- 注意区分上面的语句和下面这个：
  
```
.side-container {
.unfolded {
....
```

- 编译成css之后
  - 前者为.side-container.unfolded，是同级
  - 后者为.side-container .unfolded，是父子级，去区别在于中间的空格


- 另一个例子：
  
```scss
.dashboard {
&-container {
&-text {
```

- 编译之后嵌套结构会被展平
  
```scss
.dashboard-container {
.dashboard-text {
```


### 伪元素选择器：before
- 在每个指定标签之前之前插入内容和样式
  
```scss
p:before {
  content: "Read this -";
  background-color: yellow;
  color: red;
  font-weight: bold;
}
```

- 比如下面的代码可以让底部边框border-bottom居中显示80%

```scss
.el-menu-item.collapse::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 10%;
  width: 80%;
  border-bottom: solid 1px rgba(0, 0, 0, 0.3);
}
```

- 关于冒号：在 CSS3 中，为了区分伪类和伪元素，伪元素的语法改为使用双冒号 :: 表示，例如 ::before。但是，为了兼容旧的 CSS2 代码，使用单冒号 : 仍然可以使用。即css3中:before 和 ::before都可以表示伪元素
- 伪类和伪元素的主要区别在于它们描述的内容不同。伪类描述元素的状态，而伪元素描述元素的位置