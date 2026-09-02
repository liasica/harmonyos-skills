---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-30
title: Windows x86模拟器卡在开机界面，无法进入桌面
breadcrumb: FAQ > DevEco Studio > 应用运行 > Windows x86模拟器卡在开机界面，无法进入桌面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:35+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:e79fd95abb05eb290849c6c89da1ac5e9d8108a328d2d69a782ac2bd8ddc097e
---

**问题现象**

Windows x86模拟器卡在开机界面，无法进入桌面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/AuPPjaRMRpWRH04_8gdh6Q/zh-cn_image_0000002635735156.png "点击放大")

场景一：

检查本机CPU是否支持AES指令集。模拟器需要AES指令集支持。

场景二：

本机计算机系统CPU、内存资源不足。

可通过任务管理器，查看当前运行模拟器时本机CPU、内存占用，若发现CPU或内存占用过高时，可能导致模拟器无法启动。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Eoi_vtvLTvuDp-BhtB-oTQ/zh-cn_image_0000002666054267.png "点击放大")

**解决措施：**

1. 更换支持AES指令集支持的CPU。
2. 若是因为CPU负载过高时，需根据CPU使用的TOP应用排名，清除掉一部分高cpu消耗的应用；若是因为内存负载过高时，需根据内存使用的TOP应用排名，清除掉一部分高内存消耗的应用。反复执行此操作，确保cpu、内存资源充足，再启动模拟器。

   **说明** 

   例如，CPU型号为Intel Core i7-12700，内存为32G的Windows 11机器，需要确保模拟器启动时，CPU占用率低于97%，内存需预留4G或以上。
