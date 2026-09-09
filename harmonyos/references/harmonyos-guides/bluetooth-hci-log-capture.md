---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bluetooth-hci-log-capture
title: 如何抓取蓝牙HCI日志
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 蓝牙常见问题 > 如何抓取蓝牙HCI日志
category: harmonyos-guides
scraped_at: 2026-09-10T06:22:35+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:c5c246fcfeeae5341fe243ed80d462295a7361f3c2f845b9f94744694a36c5c7
---

## 简介

蓝牙/全场景开发者，可以通过开发者模式，一键采集蓝牙连接HCI日志，高效完成APP连接性能调试。该功能具有以下特点：

* 一键采集：操作简单，下拉通知栏点击开发者模式卡片，点击收集按钮即可完成HCI日志采集。
* 本地管理：抓取的HCI日志保存在文件管理可访问路径下，日志文件由手机用户管理。

**说明** 

蓝牙HCI日志抓取功能面向开发者提供便捷高效的蓝牙HCI日志抓取能力。

开发者抓取蓝牙HCI日志功能从API版本26.0.0开始支持，目前支持Phone、Tablet。

## 操作步骤

### 步骤一：开启开发者模式

在调测手机上进入开发者模式，开启方法请参考 **[开启开发者选项](ide-developer-mode.md#section530763213432)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/x7eSQJdlSuyDTyBrmEKIJQ/zh-cn_image_0000002717771122.png)

### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/-t_TpsCpRHa-ayE7EkLtfg/zh-cn_image_0000002717611188.png)

### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/EcmFZ9bNR6qNNzFV1wpbLw/zh-cn_image_0000002747291141.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/hcCQsG8xSsidejxC9J7hqQ/zh-cn_image_0000002747211059.png)

**说明** 

点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。

下拉通知栏的**开发者模式卡片**可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证**开发者模式开启**的情况下，**重启手机**，卡片才可重新生效。请勿随意移除开发者模式卡片。

### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/VQSq6m51QAaAUT_-1JovGw/zh-cn_image_0000002717771124.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/EC73Pr42SimMbr-B4eThQw/zh-cn_image_0000002717611190.png)

通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Duhx0mBkRBSEcTFlZNfj2w/zh-cn_image_0000002747291143.png)

**说明** 

抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
