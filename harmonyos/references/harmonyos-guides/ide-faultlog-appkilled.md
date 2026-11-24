---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-faultlog-appkilled
title: 查看App Killed（应用终止）日志
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 查看App Killed（应用终止）日志
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:279ac7d44cdabdbf2d51b97916905f79f24bd35e37433cfb4cda90a9982ddf42
---

从DevEco Studio 6.0.2 Beta1版本开始，提供**AppKilled**窗口，用于查看设备上应用终止的相关信息，包括应用异常退出的时间、进程名、是否前台应用、异常退出原因，点击**recordId**可以查看详细的FaultLog信息。支持按设备、应用和异常原因对信息进行过滤。

如需对问题进行排查处理，请参考[App Killed（应用终止）检测](appkilled-guidelines.md)。

**说明** 

2in1、Tablet设备不支持查看APP\_INPUT\_BLOCK和THREAD\_BLOCK\_6S类型的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/n8SeovUxSCuv-CEYmpqYRw/zh-cn_image_0000002779407248.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=635FC99C955DADDF1ECDF58D1E4548DA4050DA31B13D3E4C308994F4016DFAC6)
