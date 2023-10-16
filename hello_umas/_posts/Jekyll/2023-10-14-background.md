---
layout: post
title: 'jekyll: 添加背景图片'
info: '找准目标模板就没问题，路径仿照文章中的图片引用路径即可'
date: 2023-10-14 22:06:39  +0800
categories: ['jekyll']
toc: True
---


- 一开始想加在home.html中发现没有效果，查看发现home.html上面还有一行layout: base，也就是说base.html才是真正的根节点


{% raw %}
```html
<!DOCTYPE html>
<html lang="{{ page.lang | default: site.lang | default: " en" }}">

{%- include head.html -%}

<body>
  <!-- 背景图 -->
  <div class="bg-img"></div>

  {%- include header.html -%}

  <main class="page-content" aria-label="Content">
    <div class="wrapper">
      {{ content }}
    </div>
  </main>

  {%- include footer.html -%}

</body>

<style scoped>
  /* 背景图片 */
  div.bg-img {
    background-image: url("{{site.url}}/static/background.svg");
    position: absolute;
    height: 100%;
    width: 100%;
    background-repeat: repeat;
    background-size: 400px;
    z-index: -2;
    opacity: 0.1;
  }
</style>

</html>
```
{% endraw %}


- 2023.10.16修改：position应该为fixed，设为fixed后背景图片不随滚动条滚动，始终占满整个页面
- 而absolute仅能填满一个vh的高度，滚动到下面就没了



{% raw %}
```
```
{% endraw %}


<!--![引入图片]({{site.url}}/image/jekyll/2023-10-14-background/image_1.jpg) -->