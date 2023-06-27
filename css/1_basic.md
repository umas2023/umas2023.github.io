

## scss基本语法

- 多个class用空格叠加，可以快速赋予属性，结合动态class名可以实现动态样式
```scss
<div class="padding10 inline">

// 全局：div不换行
div.inline {
  display: inline-block;
}
// 全局：间距10px
.padding10 {
  padding: 10px;
}
```

- class空格叠加时单独定义样式，此时css语句中点是连续的
```scss
<div class="box rai">
<div class="box di">
div.box.rai {}
div.box.di {}
```

- 空格叠加与多级叠加区分
  - 多级叠加时css用空格分开
  ```	scss
  <div class="box di">
  <div class="select">
  div.box.rai .select { …
  ```
  - 上面的空格等价于多级嵌套
  ```scss
  div.box.rai { …
    .select { … }
  }
  ```	
		

- import
```scss
	<style lang="less" scoped>
	  @import "../less/login.less";
	</style>
```




## 选择器

1. 兄弟选择器
- 要求: 有两个并列的div,当鼠标悬停在div-1时它的宽度增加200,同时div-2的宽度减少200
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

2. 父元素引用：&

- &用来引用父元素，例：
```scss
.side-container {
&.unfolded {
....
```

- 区分：
```
.side-container {
.unfolded {
....
```
- 编译成css之后
  - 前者为.side-container.unfolded，是同级
  - 后者为.side-container .unfolded，是父子级，去区别在于中间的空格


- 另一个例子
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


3. before: 在每个指定标签之前之前插入内容和样式
```scss
p:before {
  content: "Read this -";
  background-color: yellow;
  color: red;
  font-weight: bold;
}
```
