# 树莓派clash代理


- 参考：
  - https://kevinxli.medium.com/set-up-clash-client-on-your-raspberry-pi-4-54e77f7f7fe4




- 下载clash：
    ```
    wget https://github.com/Dreamacro/clash/releases/download/v1.15.1/clash-linux-armv7-v1.15.1.gz
    ```
    - 注意版本 linux-armv7
    - 如果最新的release没有这个版本, 找上一个


- 解压并赋予执行权限
    ```
    gzip -d xxx
    sudo chmod +x clash
    ```

- 从机场下载到yaml文件，放在：
    ```
    $HOME/.config/clash/config.yaml
    ```

- 配置系统代理
  1. 编辑环境变量
        ```
        sudo vim /etc/environment
        ```
        添加
        ```
        export http_proxy="http://127.0.0.1:7890"
        export https_proxy="http://127.0.0.1:7890"
        export no_proxy="localhost, 127.0.0.1"
        ```

  2. 为 sudo 操作启用代理
        ```
        sudo visudo
        ```
        添加
        ```
        Defaults    env_keep+="http_proxy https_proxy no_proxy"
        ```


- 运行clash
    ```
    ./clash
    ```
    - 注意这里不需要sudo，否则会在root目录下寻找配置文件
    - 如果报错：
    ```
    INFO[0000] Can't find MMDB, start download
    FATA[0000] Initial configuration directory error: can't initial MMDB: can't download MMDB: Get "https://cdn.jsdelivr.net/gh/Dreamacro/maxmind-geoip@release/Country.mmdb": proxyconnect tcp: dial tcp 127.0.0.1:7890: connect: connection refused
    ```

    - 可以手动下载这个文件
    https://gitee.com/mirrors/Pingtunnel/blob/master/GeoLite2-Country.mmdb
    - 放在：$HOME/.config/clash/Country.mmdb


- 两个dashboard
  - https://clash.razord.top/
  - https://yacd.haishan.me/



- 两个dashboard只能通过127.0.0.1访问，如果树莓派没有可视界面，可以在GitHub上把yacd项目clone到本地，部署局域网服务器（懒得搞了）



