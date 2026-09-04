---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-packet-analysis
title: 使用网络报文分析功能实现tcpdump抓包
breadcrumb: 指南 > 系统 > 网络 > 网络调试调优 > 使用网络报文分析功能实现tcpdump抓包
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:31+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c929d0e84cd717922faa55318928f09809b8c0bddcd742b4f227e7a715e263c1
---

## 网络报文分析简介

网络报文分析是HarmonyOS提供的一种开发者调试能力，开发者可以在Windows PC安装Wireshark工具，对设备的网络报文进行分析。在移动应用开发过程中，网络通信调试是常见需求。网络报文分析功能提供了一种即插即用的解决措施，开发者只需将Phone或Tablet通过USB连接到PC，即可在PC端捕获设备上的网络报文。常用于应用网络请求调试（HTTP/HTTPS/WebSocket等）、网络协议分析（TCP/UDP等）、网络性能问题排查。

**说明** 

网络报文分析功能从API版本26.0.0开始支持。

### 能力范围

* 实时流量镜像：开发者可以在Windows PC Wireshark中实时观察到Phone或Tablet上的网络请求，无需在Phone或Tablet上安装任何抓包工具。
* 透明抓包：对Phone或Tablet上的应用完全透明，应用无需任何适配即可被抓包。抓包过程中不影响应用的正常运行和网络通信质量。
* 多协议支持：支持TCP、UDP、ICMP等传输层协议，以及HTTP、HTTPS、DNS等应用层协议。可以完整解析常见网络协议的请求和响应内容。

### 亮点特征

* 即插即用

USB连接后系统自动识别设备并创建以太网卡，无需手动安装驱动或进行复杂配置。在开发者选项中一键开启，即可立即在Wireshark中看到网络报文。

* 实时性强

延迟低，适合需要实时观察网络请求、调试WebSocket长连接、分析DNS解析等场景，能够快速定位问题。也可支持通过Wireshark将抓包结果导出为pcap文件进行二次分析。

## 约束与限制

### 设备限制

本功能仅适用于Phone和Tablet设备。

### 功能限制

* Phone或Tablet端需要开启开发者选项。
* 开启网络报文分析功能前，Phone或Tablet需通过USB数据线连接到Windows PC。

### 网络报文分析开关状态说明

| 状态 | 说明 | 操作 |
| --- | --- | --- |
| 开启 | 正在抓取网络报文 | 可手动关闭 |
| 关闭 | 未抓取网络报文 | USB连接后可开启 |
| 不可用（灰色） | USB未连接，功能不可操作 | 连接USB后可开启 |

## 使用指导

### 前提条件

1. Phone或Tablet通过USB数据线连接到Windows PC。
2. Windows PC端已安装Wireshark（建议使用v4.4.3及以上版本）。

### 设备端操作步骤

步骤一：进入开发者选项

当您首次使用该功能时，可根据[开启开发者选项](ide-developer-mode.md#section530763213432)指引先开启设备的开发者模式，然后点击设置->系统->开发者选项进入开发者选项页面。

步骤二：连接USB

1. 使用USB数据线将设备连接到PC。
2. 在设备的USB连接弹窗中，选择合适的连接模式（建议选择"仅充电"）。

**说明** 

如果开发者选项中的"网络报文分析"开关显示为灰色（不可用状态），请检查USB连接是否正常。

步骤三：开启网络报文分析

1. 在开发者选项中找到网络报文分析。
2. 点击开关弹窗确认允许后将其开启。
3. 开启后胶囊实况窗会提示"报文分析运行中"，设备网络报文会被抓取到Windows PC Wireshark。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/cqPPBpWESpSpdxyYLFEA_Q/zh-cn_image_0000002712244608.png)

**说明** 

1、USB调试过程中开启网络报文分析功能，USB调试功能将自动关闭。

2、抓包过程中开启USB调试功能，网络报文分析功能将自动关闭。

3、USB断开后，开关会自动变为灰色（不可用）状态，重新连接USB后可再次操作打开。

### Windows PC端操作步骤（Wireshark抓包）

步骤一：确认以太网卡

1. 打开Wireshark。
2. 在网卡列表中查找功能开启后新增的以太网卡，通常显示为"以太网 x"（如"以太网 2"）。
3. 记录该以太网卡的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ie9RQZ5bT0a1F5s4Xb2Ffg/zh-cn_image_0000002742003561.png)

**说明** 

如果看不到新增的以太网卡，请检查：

1、USB连接是否正常。

2、Phone或Tablet网络报文分析功能是否已开启。

步骤二：开始抓包

1. 在Wireshark网卡列表中，双击选中的以太网卡，开始抓包。
2. 报文数据会显示在抓包窗口中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/PypRpb3hS52E1W-y3rEAWA/zh-cn_image_0000002712404574.png)

步骤三：解读抓包结果

抓包窗口主要分为三个区域：

| 区域 | 说明 |
| --- | --- |
| 报文列表 | 显示捕获的所有数据包概览 |
| 报文详情 | 显示选中数据包的详细协议信息 |
| 字节区域 | 显示选中数据包的原始字节数据 |

报文列表中各列含义：

| 列名 | 说明 |
| --- | --- |
| No. | 数据包序号 |
| Time | 相对时间（从抓包开始算起） |
| Source | 源地址（IP或MAC） |
| Destination | 目标地址（IP或MAC） |
| Protocol | 协议类型（如TCP、UDP、HTTP） |
| Length | 包长度（字节） |
| Info | 包的基本描述 |

Wireshark通过颜色区分不同类型的报文：

| 颜色 | 含义 | 示例 |
| --- | --- | --- |
| 绿色 | 正常传输的TCP流量 | 数据传输 |
| 深蓝色 | TCP控制报文 | SYN、FIN、ACK |
| 浅蓝色 | UDP流量 | DNS查询、QUIC |
| 黄色 | 警告或异常 | TCP重传、乱序 |
| 红色 | 错误或异常 | TCP错误、校验和错误 |
| 黑色 | 畸形数据包 | 损坏的包 |

更详细的Wireshark网络报文分析说明请参考[Wireshark官网](https://www.wireshark.org/)或互联网公开资料。

步骤四：设置过滤条件（可选）

为减少无关流量，可以使用过滤器：

| 过滤条件 | 说明 | 示例 |
| --- | --- | --- |
| 按协议过滤 | 只显示特定协议的包 | tcp、udp、http |
| 按IP过滤 | 只显示与特定IP相关的包 | ip.addr == 192.168.1.100 |
| 按端口过滤 | 只显示特定端口的包 | tcp.port == 8080 |
| 组合过滤 | 多个条件组合 | tcp and ip.addr == 192.168.1.100 |

步骤五：停止抓包并保存

1. 点击工具栏上的红色停止按钮停止抓包。
2. 使用Ctrl+Shift+S保存抓包文件。
3. 选择保存路径和文件名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/TQv5PtMhStCd14e6JKDAtw/zh-cn_image_0000002742123523.png)

### 关闭网络报文分析步骤

方式一：通过开关关闭

1. 在Phone或Tablet端设置->系统->开发者选项中找到网络报文分析开关。
2. 点击开关，将其关闭。

**说明** 

关闭功能后再次打开，PC端Wireshark需要重新关闭抓包窗口后重新选择新增的以太网卡再次进行抓包。

方式二：断开USB连接

Phone或Tablet断开USB连接，网络报文分析功能自动关闭。

## 常见问题

### 网络报文分析开关为灰色，无法点击

**问题现象**

开发者选项中的网络报文分析开关显示为灰色，无法操作。

**可能原因**

USB未连接或连接不稳定。

**解决措施**

* 检查USB连接，确保数据线支持数据传输。
* 重新插拔USB数据线。
* 如问题持续，可能是Phone或Tablet硬件不支持此功能。

### 网络报文分析功能已开启但Wireshark中无新增以太网卡

**问题现象**

Phone或Tablet设备的网络报文分析功能已开启，但Wireshark网卡列表中没有新增的以太网卡。

**解决措施**

* 重新开启Phone或Tablet的网络报文分析功能。
* 重启Wireshark并在Wireshark中点击刷新网卡列表按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/jCPsf54aQfip_7AYBrsuXA/zh-cn_image_0000002712244610.png)

### 抓包数据为空或很少

**问题现象**

开启功能并开始抓包，但捕获到数据包为空。

**可能原因**

Phone或Tablet没有实际网络流量。

Wireshark过滤器设置过于严格，例如限制特定IP、端口等。

**解决措施**

* Phone或Tablet上打开浏览器访问网页或播放视频，观察是否有流量。
* 检查Wireshark过滤器是否设置正确，尝试清除所有过滤器。
* 确认以太网卡是否在接收数据（查看Wireshark底部状态栏的包统计）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/_30jK2PJRzCs_CK_eoTrtA/zh-cn_image_0000002742003563.png)

### 功能使用期间出现中断

**问题现象**

网络报文抓取过程中功能自动中断。

**可能原因**

网络抓包过程中开启USB调试开关或USB共享网络。

USB连接不稳定，USB意外断开并恢复连接后，网络抓包功能需要手动重新开启。

Wireshark软件异常。

**解决措施**

* 网络报文抓取过程中不要开启USB调试或USB共享网络。
* 使用接触良好的USB数据线。
* 重启Wireshark并重新选择Phone或Tablet对应的以太网卡。

### 开启功能后Phone或Tablet发热

**问题现象**

开启网络报文分析后，设备发热。

**解决措施**

开启功能后Phone或Tablet发热增加属于正常现象，调试完成后及时关闭网络报文分析功能。
