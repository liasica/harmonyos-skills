---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bluetooth-hci-log-capture
title: 如何抓取蓝牙HCI日志
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 蓝牙常见问题 > 如何抓取蓝牙HCI日志
category: harmonyos-guides
scraped_at: 2026-09-24T06:50:03+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:b5ab8524d0ac9c5e7b51f55779162579f7b35a17ae61c3828aa616f02767e6b2
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Lx8pF_VrQh6bBcVtxX4reA/zh-cn_image_0000002769330767.png)

### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/-PxzcuKZSO-NrPQtUy59dQ/zh-cn_image_0000002769450629.png)

### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/iI2OUUVWTxujHkAIaQmrmg/zh-cn_image_0000002739891298.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/hrWpzc6-Sle7S5tOCMelOg/zh-cn_image_0000002739731420.png)

**说明** 

点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。

下拉通知栏的**开发者模式卡片**可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证**开发者模式开启**的情况下，**重启手机**，卡片才可重新生效。请勿随意移除开发者模式卡片。

### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/vep41mRqQIyNGvfk2IoSvg/zh-cn_image_0000002769330769.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/IL2OSrl-TR2f4gQQ9GkIGA/zh-cn_image_0000002769450631.png)

通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/6f9msrCoS9Sn3Bt_ZWHPCw/zh-cn_image_0000002739891300.png)

**说明** 

抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
