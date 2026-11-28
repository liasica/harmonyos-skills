---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-faultlog-appkilled
title: 查看App Killed（应用终止）日志
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 查看App Killed（应用终止）日志
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:40+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:fc5a95a4ee395e707e1e4939ee845b30f7d3fc25fa31be1f137429651ef2634c
---

从DevEco Studio 6.0.2 Beta1版本开始，提供**AppKilled**窗口，用于查看设备上应用终止的相关信息，包括应用异常退出的时间、进程名、是否前台应用、异常退出原因，点击**recordId**可以查看详细的FaultLog信息。支持按设备、应用和异常原因对信息进行过滤。

如需对问题进行排查处理，请参考[App Killed（应用终止）检测](appkilled-guidelines.md)。

**说明** 

2in1、Tablet设备不支持查看APP\_INPUT\_BLOCK和THREAD\_BLOCK\_6S类型的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/9C7t7zfiR2GTpDbdiBEfXQ/zh-cn_image_0000002779407248.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=1785F166E036A39188DEC267760F78AC3530C2F62643DFC0406D2C968FEDA694)
