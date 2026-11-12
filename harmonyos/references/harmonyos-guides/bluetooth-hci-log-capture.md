---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bluetooth-hci-log-capture
title: 如何抓取蓝牙HCI日志
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 蓝牙常见问题 > 如何抓取蓝牙HCI日志
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:fc3c6f162b08e867e3891305e7a5ea1e0c1ed8da94fb08b89bb0586b5a30e6ce
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/lN_6Au6PRTSyybqi_HeanA/zh-cn_image_0000002815399213.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=50EE3ED3AB02AAB4C2B5B8081F9E47EC73BAC848FB244F53AD98E6D679186527)

### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/kKR4F19QRXeVDDyB8wYMWw/zh-cn_image_0000002786519638.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=E52A88098F3D18F197EB1BF7C651EDA29894FD36856D1384DEF867380F9FC2F2)

### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/fVvXThb7R3WMVhNm7qvIQQ/zh-cn_image_0000002786359710.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=3206C5F02D420730E20D9A1383843812B8CB8F73F52345ABFC71AD93801DB4D6)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/aY9WdwJzRp2Y3RNsTZo0lg/zh-cn_image_0000002815559131.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CDC60882AF3A57403C842A5120188A523DAD986479D04BAF2F99582234FB8A0)

**说明** 

点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。

下拉通知栏的**开发者模式卡片**可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证**开发者模式开启**的情况下，**重启手机**，卡片才可重新生效。请勿随意移除开发者模式卡片。

### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/DfIve96zSxanrNKRjhNzjw/zh-cn_image_0000002815399215.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5D4B187211A6346BB78D59F17817914C1B222331D311C4B217C18940AD0F45A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/9eGScgXrRFeO6HzQXxzWxw/zh-cn_image_0000002786519640.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EDAF35CE0F160C893D653AC2E4F703C7A17F47AF70952F6EFCE81FEDCEFEAA1)

通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/CT1HTCauTmSOnr5DGmq3PA/zh-cn_image_0000002786359712.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C855D1732345EDE909785C21E483B46FD75A62A539DA5AF60FD0049BA1E4E76)

**说明** 

抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
