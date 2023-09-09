---
layout: post
title:  "windows: redmi-ax6000路由器刷openwrt固件"
info: "解锁特色功能"
date:   2023-06-30 09:48:00 +0800
categories: ['windows','openwrt']
toc: true
---


- 参考：
  - https://blog.csdn.net/sxf1061700625/article/details/130328437

- 路由器初始管理页面192.168.31.1
- 常用设置 - 系统设置 - 手动升级，选中刚才下载的redmi-ax6000-1.2.8.bin

- 管理页url可以看到stoc

```
http://192.168.31.1/cgi-bin/luci/;stok=2d884ca60cc3e0b7d0976cd02a662e41/web/setting/upgrade
```
```
stok=2d884ca60cc3e0b7d0976cd02a662e41
```

- 开启调试模式：替换下面代码的stock，浏览器打开这个链接，返回{code:0}

```
http://192.168.31.1/cgi-bin/luci/;stok=2d884ca60cc3e0b7d0976cd02a662e41/api/misystem/set_sys_time?timezone=%20%27%20%3B%20zz%3D%24%28dd%20if%3D%2Fdev%2Fzero%20bs%3D1%20count%3D2%202%3E%2Fdev%2Fnull%29%20%3B%20printf%20%27%A5%5A%25c%25c%27%20%24zz%20%24zz%20%7C%20mtd%20write%20-%20crash%20%3B%20
```

- 请求重启

```
http://192.168.31.1/cgi-bin/luci/;stok=2d884ca60cc3e0b7d0976cd02a662e41/api/misystem/set_sys_time?timezone=%20%27%20%3b%20reboot%20%3b%20
```

- 开启telnet

```
http://192.168.31.1/cgi-bin/luci/;stok=05f781c1c50e025342246e4c9a4765e3/api/misystem/set_sys_time?timezone=%20%27%20%3B%20bdata%20set%20telnet_en%3D1%20%3B%20bdata%20set%20ssh_en%3D1%20%3B%20bdata%20set%20uart_en%3D1%20%3B%20bdata%20commit%20%3B%20
```

- 重启，等待白灯亮起

```
http://192.168.31.1/cgi-bin/luci/;stok=05f781c1c50e025342246e4c9a4765e3/api/misystem/set_sys_time?timezone=%20%27%20%3b%20reboot%20%3b%20
```

- 打开终端用telnet连接（windows默认没这个命令，可以用wsl）

```
telnet 192.168.31.1
```


- 连接后用下面的命令解锁ssh

```
cd /tmp && curl --silent -O https://fastly.jsdelivr.net/gh/miaoermua/unlock-redmi-ax6000@main/setup.sh && chmod +x setup.sh && ./setup.sh
```

- 通过ssh进入路由器，密码admin

```
ssh root@192.168.31.1
```


- 下载uboot

```
cd /tmp && curl --silent -O https://fastly.jsdelivr.net/gh/miaoermua/unlock-redmi-ax6000@main/uboot.sh && chmod +x uboot.sh && ./uboot.sh
```


- 备份原系统

```
scp root@192.168.31.1:/tmp/mtd4_Factory.bin D:\s-workspace\ax6000\backup\
scp root@192.168.31.1:/tmp/mtd5_FIP.bin D:\s-workspace\ax6000\backup\
```

- 刷入uboot

```
mtd erase FIP
mtd write /tmp/mt7986_redmi_ax6000-fip-fixed-parts.bin FIP
mtd verify /tmp/mt7986_redmi_ax6000-fip-fixed-parts.bin FIP
```






- 网线插入，网络和共享中心里修改以太网属性，ipv4

```
IP 地址：192.168.31.2
子网掩码：255.255.255.0
网关地址：192.168.31.1
```

- 断电，按住reset后通电，至少按住15秒
- 访问http://192.168.31.1/可以看到固件升级页面

- 下载固件
  - https://github.com/miaoermua/CatWrt/releases/tag/v23.2-Wireless-mt7986a



- 在固件升级页面中上传，点击update，等待complete或者白灯亮起，progess页面需要刷新才能显示complete，如果显示failed就再上传刷写一次

- 之后记得把电脑的ipv4改为自动

- 刷完之后从192.168.1.4进入openwrt管理页，账号root，密码password


- openwrt设置：
- 网络 - 接口 - lan，修改ipv4网关192.168.1.4，ipv4广播192.168.1.0

- wan口里设置pppoe拨号


- wifi名和密码在 [网络 - 无线 - 接口配置] 里面修改

- clash没有内核，需要手动下载然后scp


