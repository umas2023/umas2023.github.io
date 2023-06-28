---
layout: post
title:  "js: hello_world"
info: "JavaScript基础语法"
date:   2023-06-28 08:20:00 +0800
categories: js
toc: true
---


## 常用函数

- 定时器
  ```js
    // 时间间隔
    let time_interval = 3000
    // 设置定时器
    let set_id = setInterval(get_list_check, time_interval)
    // 定时清除
    setTimeout(() => {
        clearInterval(set_id)
    }, 10 * time_interval)
  ```