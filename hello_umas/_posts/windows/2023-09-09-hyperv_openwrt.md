---
layout: post
title: 'windows: hyperv虚拟机软路由'
info: '不花钱加速局域网内学习机'
date: 2023-09-09 11:57:03  +0800
categories: ['windows']
toc: True
---

## 下载镜像

- 下载openwrt镜像
  - https://downloads.openwrt.org/releases/22.03.5/targets/x86/64/


![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_1.png)


- combined：文件系统 + 内核
- rootfs： 只有文件系统

- 注意下载之后的压缩包用7z解压可能报错，可以用winrar

- starwind软件将img转为vmdk
    - 选localfile，VHD/VHDX，VHDX growable image


## 启动虚拟机

- 确认hyperv已经打开
- windows管理工具->hyper-v管理器

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_2.png)


- 外部网络选择当前使用的网卡

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_3.png)


- 创建虚拟机

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_4.png)

- 第二代，不使用动态内存，连接选刚才的wrt_lan，使用现有虚拟硬盘找到刚才的vhdx

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_5.png)



- 安全 -> 启用安全启动 - 关掉
- 网络适配器 -> 高级功能 -> 启用mac地址欺骗
- 检查点 -> 使用自动检查点 - 关掉
- 自动启动 -> 有需要的话开启始终自动启动


- 右键连接openwrt，编辑
- Vim etc/config/network
- 改成和当前路由器相同网段

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_6.png)

- reboot

- 浏览器输入上面的ip：192.168.31.31
- 没有密码

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_7.png)


- 修改lan，网关指向主路由

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_8.png)

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_9.png)


- DHCP服务器：忽略此接口

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_10.png)

- 禁用桥接

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_11.png)

- Dns 8.8.8.8

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_12.png)


- ping downloads.openwrt.org


- 安装中文语言包
- Index of /releases/22.03.5/packages/x86_64/luci/ (openwrt.org)
- 搜base-zh-cn

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_13.png)


![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_14.png)


- 更换阿里源

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_15.png)

- 将 /etc/opkg/distfeeds.conf 下的 downloads.openwrt.org 替换为mirrors.aliyun.com/openwrt 

```
src/gz openwrt_core https://downloads.openwrt.org/releases/22.03.5/targets/x86/64/packages
src/gz openwrt_base https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/base
src/gz openwrt_luci https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/luci
src/gz openwrt_packages https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/packages
src/gz openwrt_routing https://do
```


- 完了update一下：```opkg update```

- 注意第一行的targets不要改，会报错（2023.5.28）


## 安装clash

- 参考：https://github.com/vernesong/OpenClash/wiki/%E5%AE%89%E8%A3%85


- 首先删掉dnsmasq

- 下载ipk
- Releases · vernesong/OpenClash (github.com)
- 安装依赖

```
opkg update
opkg install coreutils-nohup --force-overwrite
opkg install bash --force-overwrite
opkg install iptables --force-overwrite
opkg install dnsmasq-full --force-overwrite
opkg install curl --force-overwrite
opkg install ca-certificates --force-overwrite
opkg install ipset --force-overwrite
opkg install i
```

- 整合↑

```
opkg install coreutils-nohup  bash  iptables  dnsmasq-full  curl  ca-certificates  ipset  ip-full  iptables-mod-tproxy  iptables-mod-extra  libcap  libcap-bin  ruby  ruby-yaml  kmod-tun --force-overwrite 

```

- ipk文件拷贝到远程主机
```
scp .\luci-app-openclash_0.45.121-beta_all.ipk root@192.168.31.31:/root
```

- opkg install
```
opkg install luci-app-openclash_0.45.121-beta_all.ipk
```

- 报错 module 'luci.cbi.datatypes' not found 
    - 参考：https://github.com/vernesong/OpenClash/issues/2364
    - 参考：https://blog.csdn.net/xs18952904/article/details/124600025

- 命令报错找不到：opkg install luci-compat，需要手动下载
    - https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/luci/

```
scp .\luci-compat_git-23.093.42303-ef4cd04_all.ipk root@192.168.31.31:/root
opkg install luci-compat_git-23.093.42303-ef4cd04_all.ipk
```

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_16.png)


- 这里没有手动下载内核，如果配置完成后内核自动下载失败，需要手动下载

- 不行，它不能自动下载，还是要手动下

- 下载内核，三个不存在的都下载
    - md好麻烦，还是安一个winscp吧

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_17.png)



- 拷过去之后加权限

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_18.png)
![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_19.png)


- 启用fake-ip模式（在底部点击）记得点保存应用

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_20.png)

- 启动之后在 server logs 报错
- 警告：OpenClash 启动成功，检测到您启用了IPv6的DHCP服务，可能会造成连接异常！
- 接口编辑里关掉这个：

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_21.png)





- 安装主题
- [luci-theme-argon/README_ZH.md at master · jerrykuku/luci-theme-argon · GitHub](https://github.com/jerrykuku/luci-theme-argon/blob/master/README_ZH.md)
- 可以用wget
```
opkg install luci-compat
opkg install luci-lib-ipkg
wget --no-check-certificate https://github.com/jerrykuku/luci-theme-argon/releases/download/v2.3/luci-theme-argon_2.3_all.ipk
opkg install luci-theme-argon*.ipk
```

- 报错找不到的话update一下
```
opkg update
```

- 也可以直接下载：
-  https://github.com/jerrykuku/



## windows连接

- 修改默认网关
- 不需要在路由器里固定ip地址
- 设置的网卡必须是之前open wrt连接的网卡，双网卡要选对，第三方手机不能连接
- 首选dns是wrt地址
注意连接后需要等待2-3分钟，期间会无法联网

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_22.png)
![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_23.png)


- 经测试下面这个方法不太行

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_24.png)

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_25.png)


- 1、网络前缀长度24，对应子网掩码【255.255.255.0】；
- 2、网络前缀长度18，对应子网掩码【255.255.240.0】；
- 3、网络前缀长度16，对应子网掩码【255.255.0.0】



## 热点转发

- 实际测试时发现只有电脑本机可以正常上网，安卓苹果switch都不行
- 可以将电脑的网络通过热点转发给其他设备

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_26.png)


- 打开共享后可以看到多出一个网络设备

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_27.png)


- 在当前电脑连接wifi的设备属性里打开共享，没有开启共享时手机连上会显示没有网络

![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_28.png)


- 补充一点，如果手机长时间连接不上的话，把上面的勾去掉试试



- 如果电脑连接后可以正常上网翻墙，但右下角显示无internet，这时无法开启热点，可以尝试：
  - 更换节点
  - 或者关闭ipv4校验，关闭后重新启动clash并重新连接，


![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_29.png)


![引入图片]({{site.url}}/image/windows/2023-09-09-hyperv_openwrt/image_30.png)



{% raw %}
```
```
{% endraw %}


## 后记

- 由于虚拟机性能限制，switch连接后nat无法满足联机需要
- 加钱买了个小米路由器，刷机教程详见另一篇