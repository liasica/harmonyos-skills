---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bluetooth-hci-log-capture
title: 如何抓取蓝牙HCI日志
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 蓝牙常见问题 > 如何抓取蓝牙HCI日志
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:39+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:5cd7e444e250b173fc738986d99f972ed8296acff7f5819c72f3fc1dd0e84a7e
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/bTrG8HneRpOphnY2JU1bgg/zh-cn_image_0000002793037392.png?HW-CC-KV=V1&HW-CC-Date=20261121T011013Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1D918DF688C4CCB0CB81A863EF62DF8FF22C679BE4457CF98BB23286C3F6E4A)

### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/DRLLq_UxSWqcH36A1kA07g/zh-cn_image_0000002792877422.png?HW-CC-KV=V1&HW-CC-Date=20261121T011013Z&HW-CC-Expire=31536000000&HW-CC-Sign=507120C52856157ACB9908CCF0C6997532D7DDE96676E9D856A7C51E7B49A1B6)

### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/m8kIVB4XS5Km0iHg8j9YaA/zh-cn_image_0000002821837329.png?HW-CC-KV=V1&HW-CC-Date=20261121T011013Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7A9C1D52ADFAAD44F28D425A70BFD3929E2D63FC5AB3CF6C02DBE520CB3C74B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/8rS4NA6VRjiZhSekLc7Qjw/zh-cn_image_0000002821757331.png?HW-CC-KV=V1&HW-CC-Date=20261121T011013Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D2D256710D00BF5C1EF926CE64105C132206C6EB2BF8722A26C75FFA55FBF5D)

**说明** 

点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。

下拉通知栏的**开发者模式卡片**可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证**开发者模式开启**的情况下，**重启手机**，卡片才可重新生效。请勿随意移除开发者模式卡片。

### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ODcgV4ONR7O9hHhfAHhbJQ/zh-cn_image_0000002793037394.png?HW-CC-KV=V1&HW-CC-Date=20261121T011013Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB9D112FA258B3F20C7B21C7CCBD3B270875DA616B5F6F08DC7DCE3126354224)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/7YPSl_u2Sd2ohvxdzI4Ghg/zh-cn_image_0000002792877424.png?HW-CC-KV=V1&HW-CC-Date=20261121T011013Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A583DEA97B984D250BC9F134EFE056AE76CA95C5BFF3AB8A369711FEDE943AF)

通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/fO_pasl9RLm5XtsSGs-MAA/zh-cn_image_0000002821837331.png?HW-CC-KV=V1&HW-CC-Date=20261121T011013Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BB307B38190B6A00FD0CF02CC0B32E4FE0AB417DFCB55CA46D9755B87E3980C)

**说明** 

抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
