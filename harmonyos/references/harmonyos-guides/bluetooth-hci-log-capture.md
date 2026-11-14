---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bluetooth-hci-log-capture
title: 如何抓取蓝牙HCI日志
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 蓝牙常见问题 > 如何抓取蓝牙HCI日志
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:34+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:81700385c9e92aa5fad9e4fc6e8158a9e91e521ebe3af446c61aedfab385f7b9
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/FKk0Pab2QYm6cUaYHj6qzw/zh-cn_image_0000002817506873.png?HW-CC-KV=V1&HW-CC-Date=20261114T004734Z&HW-CC-Expire=31536000000&HW-CC-Sign=B843DE158267962AE1336098C2C5D018DA03F42FA9130CA75463BF024A4391EE)

### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/g6TlWfRyRnGZ_GkeuTK55w/zh-cn_image_0000002788307442.png?HW-CC-KV=V1&HW-CC-Date=20261114T004734Z&HW-CC-Expire=31536000000&HW-CC-Sign=B94BEC2124E6C51117E4D4EEB014E05D36A17E1264497784C0E23A9585C96DED)

### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/HEaLaYlET-yuRnSNL4XzAw/zh-cn_image_0000002817426805.png?HW-CC-KV=V1&HW-CC-Date=20261114T004734Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBE06066BCC3194D790CD11173E47F3DB0DD73C6D1F10369FB48F7BCE2C23872)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/jLplTUBqS4mCkeE9KOnCwA/zh-cn_image_0000002788467386.png?HW-CC-KV=V1&HW-CC-Date=20261114T004734Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBC9B8CDC6AA06A1F171C813B4BC61F4995926F64FB12B1413EF93E9615C1244)

**说明** 

点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。

下拉通知栏的**开发者模式卡片**可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证**开发者模式开启**的情况下，**重启手机**，卡片才可重新生效。请勿随意移除开发者模式卡片。

### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/BtnEbKoeROq36Z8_qWjxmw/zh-cn_image_0000002817506875.png?HW-CC-KV=V1&HW-CC-Date=20261114T004734Z&HW-CC-Expire=31536000000&HW-CC-Sign=A47347CC901C1F594669495F40D780CE15325F586E887C8A63991784E8587719)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/zWiFcWIaSxWt_fzveaOPLQ/zh-cn_image_0000002788307444.png?HW-CC-KV=V1&HW-CC-Date=20261114T004734Z&HW-CC-Expire=31536000000&HW-CC-Sign=F63FCF48349CEF55A68B3951ED951574E2E370AB9D5F8950C92DED632E50589C)

通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/zWm53tU-RFmfOKbI5pDSCw/zh-cn_image_0000002817426807.png?HW-CC-KV=V1&HW-CC-Date=20261114T004734Z&HW-CC-Expire=31536000000&HW-CC-Sign=828F950AFBB2B11993FB638448F602C043B8D772AF6CFA3874380FF2CA0A3DB7)

**说明** 

抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
