---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bluetooth-hci-log-capture
title: 如何抓取蓝牙HCI日志
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 蓝牙常见问题 > 如何抓取蓝牙HCI日志
category: harmonyos-guides
scraped_at: 2026-10-11T07:21:34+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:81eb3b7ef72d50f5cf5c32a85b2703165fef7b743e4e919685ad63cf0c443376
---

## 简介

蓝牙/全场景开发者，可以通过开发者模式，一键采集蓝牙连接HCI日志，高效完成APP连接性能调试。该功能具有以下特点：

* 一键采集：操作简单，下拉通知栏点击开发者模式卡片，点击收集按钮即可完成HCI日志采集。
* 本地管理：抓取的HCI日志保存在文件管理可访问路径下，日志文件由手机用户管理。

**说明** 

蓝牙HCI日志抓取功能面向开发者提供便捷高效的蓝牙HCI日志抓取能力。

开发者抓取蓝牙HCI日志功能从API版本26.0.0开始支持，目前支持Phone、Tablet。

Release版本出于数据安全与隐私保护，会屏蔽HCI日志中蓝牙报文的payload数据，仅保留Header信息，因此若HCI日志报文数据解析不完整属正常现象。

## 操作步骤

### 步骤一：开启开发者模式

在调测手机上进入开发者模式，开启方法请参考 **[开启开发者选项](ide-developer-mode.md#section530763213432)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/8OKNezDmQD6csdDtOnjSIw/zh-cn_image_0000002784582895.png)

### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/5c2mwhXFTwOVWJILGI7_Cg/zh-cn_image_0000002784663075.png)

### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/8fWF-G-rQJGmIMYh_sNdbg/zh-cn_image_0000002755024142.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/6FVZszK8R-qEeUuZdLfKfw/zh-cn_image_0000002755184030.png)

**说明** 

点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。

下拉通知栏的**开发者模式卡片**可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证**开发者模式开启**的情况下，**重启手机**，卡片才可重新生效。请勿随意移除开发者模式卡片。

### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/avKtE66HQOS7qSDPv_hOWg/zh-cn_image_0000002784582897.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/_K9IYHbAQyO7kZmzLhqB7A/zh-cn_image_0000002784663077.png)

通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/TEQqqrqKSmWLXum5f5DhoA/zh-cn_image_0000002755024144.png)

**说明** 

抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
