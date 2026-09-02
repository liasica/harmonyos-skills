---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-135
title: VPN接入状态下，应用访问内网资源的流量未路由至VPN链路
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > VPN接入状态下，应用访问内网资源的流量未路由至VPN链路
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:cae64dc0c601440b5a8ed5b909576784e47fbb8e13781b176f0d3ea29a44fa7b
---

## 问题现象

应用请求为外网服务时，请求走VPN网络；应用请求为内网时，请求不走VPN网络。

## 背景知识

* 路由的概念：路由起到请求转发的作用，将应用的请求转发至VPN虚拟网卡转发或者物理网卡。路由在VPN中的位置：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/z43ODh5IQEeh9WBwfyLBlw/zh-cn_image_0000002709508215.png "点击放大")
* 默认路由: 所有未匹配到其它路由流量的兜底出口；在VPN网络未配置路由时，所有的流程都会走VPN隧道。IPv4默认路由为0.0.0.0/0；IPv6默认路由为::/0。
* VPN路由的分类：全隧道模式和分流路由。
  1. 全隧道模式：客户端默认路由（0.0.0.0/0）指向VPN网关，所有流量（包括上网、访问内网）都走VPN。
  2. 分流路由：仅让特定目标流量走VPN，其余流量走本地默认路由。

* [VpnConfig](../harmonyos-references/js-apis-net-vpnextension.md#vpnconfig)关键配置项：
  + isInternal：是否支持内置VPN，默认值为false。设置为true时支持内置VPN，流量将通过tun网卡转发。
  + isBlocking：是否阻止非VPN连接，默认值为false。设置为true时，未走VPN的连接将被阻止。

## 问题定位

1.网络的主要配置信息如下：

| 名称 | IP地址 |
| --- | --- |
| 本地设备IP | 192.xxx.x.9 |
| 默认网关 | 192.xxx.x.1 |
| 路由1 | 192.xxx.x.10 |
| 路由2 | 182.xx.xxx.108 |
| 虚拟网卡地址 | 10.x.x.5 |

2.WireShark条件搜索ip.src == 182.xx.xxx.108 && ip.dst == 10.x.x.5，表示搜索从182.xx.xxx.108路由到10.x.x.5网卡的流量，说明应用的外网请求通过VPN网络转发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/O7fsfWGlTSa_NOYavC2RFw/zh-cn_image_0000002679948954.png "点击放大")

3.WireShark条件搜索ip.src == 192.xxx.x.10 && ip.dst == 10.x.x.5，表示搜索从192.xxx.x.10路由到10.x.x.5网卡的流量，说明应用的内网请求不通过VPN网络转发，直接走内网的路由规则。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/ggunvxdoS1i0VQbSZBoXTQ/zh-cn_image_0000002709628759.png "点击放大")

## 分析结论

内网路由优先级默认高于VPN路由导致内网流量不走VPN网络。

## 修改建议

方案1：避免网段重叠，内网和VPN网段尽量不重叠，比如内网用192.xxx.x.0/24网段，VPN用10.x.x.0/24网段。

方案2：最长前缀匹配，通过设置某个网段的掩码越长路由优先级越高，比如VPN网段为192.xxx.x.10/32的掩码长度32比内网网段192.xxx.x.0/23的掩码长度23大，能够保证前者的路由优先级比后者大。

方案3：配置[VpnConfig](../harmonyos-references/js-apis-net-vpnextension.md#vpnconfig)参数，确保流量路由至VPN链路：

1. 将isInternal设置为true，启用内置VPN，使流量通过tun网卡转发。
2. 将isBlocking设置为true，阻止未走VPN的连接。
3. routes仅保留默认路由0.0.0.0/0，使所有流量均匹配VPN路由规则。

## 常见FAQ

Q：HarmonyOS系统如何查看设备路由规则？

A：连接设备后，执行hdc shell netstat -r；其中Destination表示下一跳路由。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/tp8F2pjURYWrSo2PNd849A/zh-cn_image_0000002679949968.png "点击放大")

## 总结

VPN网络访问问题通常需要使用网络包工具分析TcpDump包进行定位定界；根据数据包日志可以定位网络请求是否经过VPN网络，达到网络问题定位定界能力。
