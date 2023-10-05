# blog.md
编程学习记录极简版，基于jekyll，访问[主页](https://umas2023.github.io/)


## 目录说明

- hello_umas/
  - Jekyll博客
- docs/
  - Jekyll博客打包
- add.py
  - 脚本：添加新博客
- build.py
  - 脚本：博客项目打包至docs/
- serve.py
  - 脚本：启动本地服务器
- test.py
  - 随便写什么都可以
  - 一般用来本地测试leetcode题解


## server

- github page 自动部署
- 镜像由python命令在screen中启动

```bash
# 注意不要在服务器上build，会卡死！
screen -r blog
python3 -m http.server 25221 --directory /root/project/umas2023.github.io/docs
```


## 常用命令

- 新建一页
```bash
python add.py
```

- 启动本地服务器
```bash
cd hello_umas
jekyll serve
# 或
serve.py
```

- 打包（hello_umas同级目录）
```bash
jekyll build --source hello_umas --destination docs
# 或
build.py
```

- raw代码
{% raw %}{% endraw %}

{% raw %}
```
```
{% endraw %}

- 图片
![引入图片]({{site.url}}/image/windows/2023-06-28-env_path/image_1.png)




## jekyll待办

- 返回顶部按钮
- 进categories的时候右上角search没了
- categories有时候点击目录不能跳转
- 博文显示日期
- categories目录后加一个括号显示每个类别中的文章数量
- 增加公式支持（比如latex）












