---
layout: post
title: 'vue: 滚动监听'
info: '结合js实现滚动触发的效果'
date: 2023-09-20 18:10:18  +0800
categories: ['vue', 'css']
toc: True
---

- 希望随滚轮的滚动，底部的条目有依次进入的动效

- 单个元素距顶部的高度可以用```element.offsetTop```获得，页面滚动条的位置可以用```window.scrollY```获得，如果元素高度小于滚动条当前高度+页面高度，则开始加载

- 下面是homepage项目中的一个例子，每个条目用v-for在card-each中遍历

{% raw %}
```js
// 滚动条监听
onMounted(() => {
  const scroll_trigger = () => {
    let card_list = document.querySelectorAll(".card-each")
    card_list.forEach(card_each => {
      let card_element = card_each as HTMLElement
      if(card_element.offsetTop < window.scrollY + window.innerHeight){
        card_element.classList.add("active")
      } else{
        card_element.classList.remove("active")
      }
    })
  }
  window.addEventListener("scroll", scroll_trigger)
})
```
{% endraw %}



- 在另一个项目里发现window.scrollY始终是0，检查发现滚动条并不是由窗口触发的，而是在父组件的一个div中，这时需要在触发滚动事件的元素上用```@scroll```来监听。（区分 window 对象上的滚动事件和元素上的滚动事件）

- @scroll触发的函数通过event获取当前滚动高度

{% raw %}
```html
<!-- 内容主体 -->
<div id="main-box" @scroll="scrollTrigger">
    <div class="container">
        <div v-for="i in 60" :key="i" class="box"></div>
    </div>
</div>
```
{% endraw %}


{% raw %}
```js
function scrollTrigger(event:Event) {
    const mainBox = event.target;
    const scrollTop = mainBox!.scrollTop;

    let boxes = document.querySelectorAll(".box")
    boxes.forEach((boxxx) => {
        if (boxxx.offsetTop < scrollTop) {
            boxxx.classList.add("active")
        } else {
            boxxx.classList.remove("active")
        }
    })
}

```
{% endraw %}




<!-- ![引入图片]({{site.url}}/image/vue/2023-09-20-scroll_listen/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
