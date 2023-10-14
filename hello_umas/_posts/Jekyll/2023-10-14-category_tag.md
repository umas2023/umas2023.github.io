---
layout: post
title: 'jekyll: jekyll首页添加分类tag标签'
info: '早就想做这个了'
date: 2023-10-14 16:45:18  +0800
categories: ['jekyll']
toc: True
---


- 首先找到主页的模板，比如我的是./_layouts/home.html

- 查找里面的for循环就可以定位每条post的格式了

{% raw %}
```html
    {%- for post in posts -%}
    <li>
      <span class="post-meta">{{ post.date | date: date_format }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h3>
      <h5>{{ post.info | escape }}</h5>
      {%- if site.show_excerpts -%}
      {{ post.excerpt }}
      {%- endif -%}
    </li>
    {%- endfor -%}
```
{% endraw %}

- 在上面的title和info之间添加分类tag

{% raw %}
```html
    {%- for post in posts -%}
    <li>
      <span class="post-meta">{{ post.date | date: date_format }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h3>

      <!-- 添加分类标签 -->
      {% for category in post.categories %}
      <span class="category">{{ category }}</span>
      {% endfor %}

      <h5>{{ post.info | escape }}</h5>
      {%- if site.show_excerpts -%}
      {{ post.excerpt }}
      {%- endif -%}
    </li>
    {%- endfor -%}
```
{% endraw %}


- 底部再定义一些格式

{% raw %}
```html
<style scoped>

  span.category{
    padding: 2px 5px 2px 5px;
    border-radius: 5px;
    font-size: 0.5em;
    color: white;
    background-color: rgba(0, 0, 255, 0.4);
  }

</style>
```
{% endraw %}




![引入图片]({{site.url}}/image/jekyll/2023-10-14-category_tag/image_1.jpg)



- 文章内添加tag也一样，找到文章的模板后添加，我的是post.html
- 注意这里是page.categories而不是post.categories



{% raw %}
```html
---
layout: base
---
<article class="post">

  <!-- 标题 -->
  <header class="post-header">
    <h1 class="post-title">{{ page.title | escape }}</h1>
    
    <!-- 分类tag -->
    {% for category in page.categories %}
    <span class="category">{{ category }}</span>
    {% endfor %}

    <h3>{{ page.info | escape }}</h3>
  </header>

  <!-- 目录 -->
  <hr>
  {% toc %}
  <hr>

  <!-- 内容主体 -->
  <div class="post-content">
    {{ content }}
  </div>

</article>


<style scoped>

  span.category{
    padding: 2px 5px 2px 5px;
    border-radius: 5px;
    font-size: 0.5em;
    color: white;
    background-color: rgba(0, 0, 255, 0.4);
  }

</style>
```
{% endraw %}
