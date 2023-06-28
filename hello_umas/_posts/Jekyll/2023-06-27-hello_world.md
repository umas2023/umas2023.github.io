---
layout: post
title:  "jekyll: hello_world 从0开始搭建Jekyll个人博客"
info: "还挺简单的"
categories: jekyll
date:   2023-06-27 12:00:00 +0800
toc: true
---

## 参考
- [官方](https://www.jekyll.com.cn/docs/)


## 创建hello_world

1. 安装Ruby  
- https://rubyinstaller.org/downloads/  
- 查看安装：```ruby -v ```

2. 安装 Jekyll 和 bundler gems（要很久）
   
    ```
    gem install jekyll bundler
    ```

3. 创建并启动项目
  ```
  jekyll new hello_umas
  cd hello_umas
  bundle exec jekyll serve
  ```

4. 在浏览器中打开 http://localhost:4000 网址


5. 添加markdown文件
   - 在 Jekyll 项目的 _posts 目录下创建Markdown 文件，文件名必须遵循 YYYY-MM-DD-title.md 的格式，其中 YYYY-MM-DD 表示文章的发布日期，title 表示文章的标题，文件名中的单词必须用短横线 - 分隔
   - _posts支持多级目录，可以用文件夹管理md文件
   - 注意md文件中的代码块可能被解析，如果发现和原文不一致需要用{% raw %}{% raw %{% endraw %}{% raw %}}{% endraw %{% endraw %}{% raw %}}{% endraw %}来包裹代码块，比如下面引入图片的代码块如果不加raw的话就会直接显示图片。（这句话中的{% raw %}{% raw {% endraw %}{% raw %}}{% endraw %{% endraw %}{% raw %}}{% endraw %}也要用这个方法嵌套才能显示在页面中，而且必须以大括号为分隔进行三次嵌套才能显示）
   - 添加图片的方法：项目根目录下新建文件夹存放图片，不要放在_posts文件夹下，比如/image/jekyll/image_1.jpg，然后在md文件引入图片：
    {% raw %}
    ```md
    ![home]({{site.url}}/image/jekyll/2023-6-27-230627_categories/image_1.jpg)
    ```
    {% endraw %}
  - 标题的日期优先级低于yaml前置格式的日期，如果一天内上传了多份md，可以通过前置格式的日期指定时间来排序
    ```yaml
    ---
    layout: post
    title:  "Welcome to Jekyll!"
    date:   2023-06-26 11:35:28 +0800
    ---
    ```
  - 注意代码块中如果包含空行，可能导致代码块缩进错误，尽量不要有空行

6. 打包
    ```
    jekyll build --source hello_umas --destination docs
    ```
    - 这条命令将网页构建到_site文件夹中，之后可以托管在服务器上

7. 打包后可以先用python启动本地服务器看一下效果

    ```
    python -m http.server
    ```
    - 访问：http://localhost:8000/




## 套用主题

- 官方主题：http://jekyllthemes.org/
- 选择主题点击demo可以查看
- 可以在github fork方便后续开发
- download解压之后进入主题目录运行
  ```
  bundle install
  jekyll serve
  ```
- 具体部署方法可能因项目而异，最好点进GitHub看一下readme
- 项目默认主题minima就很好，深得我心，直接用默认了
- 注意直接新建的项目虽然使用了minima主题（可以在about页看到），但layout文件并没有在本地，需要到GitHub主页把layout文件内容复制到本地才可以进行二次开发（https://github.com/jekyll/minima）




## 可能的问题

1. 启动服务器时报错一个语法错误

```
244 │     padding: ($spacing-unit / 3) ($spacing-unit / 2);
    │               ^^^^^^^^^^^^^^^^^
```

不影响服务器的启动，没找到解决办法


## 其他

- 以下是创建项目时gpt推荐的支持markdown的博客框架：

Jekyll：Jekyll 是一个简单、易用、支持 Markdown 的静态网站生成器，它能够将 Markdown 文件转换成静态的 HTML 网页。Jekyll 的优点在于它易于安装和使用，并且支持 GitHub Pages，可以免费托管网站。

Hexo：Hexo 是一个快速、简洁且高效的博客框架，它基于 Node.js 平台，支持 Markdown 语法，可以生成静态的 HTML 文件。Hexo 的优点在于它的速度非常快，而且支持插件扩展，可以实现更多的功能。

Hugo：Hugo 是一个快速、灵活、易用的静态网站生成器，它支持 Markdown 语法，并且可以生成静态的 HTML 文件。Hugo 的优点在于它的速度非常快，而且支持多种主题和插件，可以满足不同的需求。

Gatsby：Gatsby 是一个基于 React 的静态网站生成器，它支持 Markdown 语法，并且可以生成静态的 HTML 文件。Gatsby 的优点在于它支持多种数据源，可以从多种数据源中获取数据，而且支持多种插件和主题，可以实现更多的功能。