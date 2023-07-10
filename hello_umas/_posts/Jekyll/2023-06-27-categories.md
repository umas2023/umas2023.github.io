---
layout: post
title:  "jekyll: categories 添加分类"
info: "jekyll博客添加分类"
date:   2023-06-27 13:00:00 +0800
categories: jekyll
toc: true
---


## 参考
- [Jekyll个人博客添加分类Category功能](https://zoharandroid.github.io/2019-08-02-Jekyll%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%E6%B7%BB%E5%8A%A0%E5%88%86%E7%B1%BBCategory%E5%8A%9F%E8%83%BD/)
- [3 Simple steps to setup Jekyll Categories and Tags](https://blog.webjeda.com/jekyll-categories/)

## 实现


1. 首先md文件添加在yaml前置格式中添加分类

    ```yml
    ---
    layout: post
    title: awesome title
    categories: Personal
    ---
    ```
   - 多个类别直接用空格隔开就可以

2. 修改 config.yaml
    ```yaml
    # 默认是通过日期做子目录的方式
    # permalink   : date
    # 改为使用category做子目录
    permalink: /:categories/:title/
    ```

3. category需要一个单独的页面，决定放在右上角about旁边。使用默认主题时，只需要在根目录下新建md或是html，前置格式指定如下即可在右上角添加导航
    ```yml
    layout: page
    title: Help
    permalink: /help/
    ```

4. 根目录下创建categories.html，内容如下

    {% raw %}
    ```html
    ---
    layout: page
    permalink: /categories/
    title: Categories
    ---


    <div id="archives">

    {% for category in site.categories %}
    <div class="archive-group">
        {% capture category_name %}{{ category | first }}{% endcapture %}
        <div id="#{{ category_name | slugize }}"></div>
        <p></p>

        <h3 class="category-head">{{ category_name }}</h3>
        <a name="{{ category_name | slugize }}"></a>
        {% for post in site.categories[category_name] %}
        <article class="archive-item">
        <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
        </article>
        {% endfor %}
    </div>
    {% endfor %}
    </div>
    ```
    {% endraw %}

5. 上面的categories.html直接显示了所有的文章，当文章数量很多时很不友好，可以在顶部添加一个对category的导航
   {% raw %}
    ```html
    <!-- 顶部导航 -->
    <hr>
    <nav id="category-toc">
    <ul>
        {% for category in site.categories %}
        <li><a href="#{{ category | first | slugify }}">{{ category | first }}</a></li>
        {% endfor %}
    </ul>
    </nav>
    <hr>
    ```
    {% endraw %}
    
6. 效果

![home]({{site.url}}/image/jekyll/2023-6-27-230627_categories/image_1.jpg)
![cate]({{site.url}}/image/jekyll/2023-6-27-230627_categories/image_2.jpg)


## 补充：按字母顺序排列

- 分类默认按照时间顺序排列，要按字母排序，可以使用sort过滤器
- 新的categories.html


{% raw %}
```html
<div id="archives">
  <!-- 顶部导航 -->
  <hr>
  <nav id="category-toc">
    <ul>
      {% assign sorted_categories = site.categories | sort %}
      {% for category in sorted_categories %}
        <li><a href="#{{ category | first | slugify }}">{{ category | first }}</a></li>
      {% endfor %}
    </ul>
  </nav>
  <hr>

  <!-- 所有文章 -->
  {% assign sorted_categories = site.categories | sort %}
  {% for category in sorted_categories %}
    <div class="archive-group">
      {% capture category_name %}{{ category | first }}{% endcapture %}
      <div id="#{{ category_name | slugize }}"></div>
      <p></p>

      <h3 class="category-head">{{ category_name }}</h3>
      <a name="{{ category_name | slugize }}"></a>
      {% for post in site.categories[category_name] %}
        <article class="archive-item">
          <h4><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h4>
        </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>
```
{% endraw %}