# javascript基础

### 常用函数

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