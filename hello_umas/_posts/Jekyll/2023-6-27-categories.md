---
layout: post
title:  "jekyll: categories"
info: "jekyll博客添加分类"
date:   2023-06-27 13:00:00 +0800
categories: jekyll
toc: true
---


## 参考
- [Jekyll个人博客添加分类Category功能](https://zoharandroid.github.io/2019-08-02-Jekyll%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%E6%B7%BB%E5%8A%A0%E5%88%86%E7%B1%BBCategory%E5%8A%9F%E8%83%BD/)


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
    title: categories
    ---
    <div id="archives">
        <ul>
            {% for category in site.categories %}
            <li>
                <a href="{{ site.baseurl }}/{{ category | first | slugify }}">{{ category | first }}</a>
            </li>
            {% endfor %}
        </ul>
    </div>
    ```
    {% endraw %}

5. 效果

![home]({{site.url}}/image/jekyll/2023-6-27-230627_categories/image_1.jpg)
![cate]({{site.url}}/image/jekyll/2023-6-27-230627_categories/image_2.jpg)

