---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/input-overview
title: Input Kit简介
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > Input Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7c556a792ed239c11d20fb780ed8bc2f7b705f33fbdd483172c9a04d41f14e34
---

## 功能介绍

Input Kit（多模输入Kit）为多种输入设备提供服务，如触控板、触摸屏、鼠标、键盘等。通过对这些输入设备上报驱动事件的归一化处理，确保不同输入设备与用户交互体验统一和流畅。

Input Kit除了提供基础的输入事件服务之外，还提供了获取输入设备列表、改变鼠标光标样式等功能和接口。

## 运作机制

多模输入能力作为系统为应用提供的一种基础服务，通过处理上报的输入设备驱动事件，完成输入事件管理、接收、预处理、分发，通过inner SDK与JSkit上报应用，具体运行机制如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/mpENaAOnTZKfL4Gt4nzNfg/zh-cn_image_0000002583438505.png?HW-CC-KV=V1&HW-CC-Date=20260427T234430Z&HW-CC-Expire=86400&HW-CC-Sign=ACC643A08BE688BE5AE31F3EC8831EBADB3FBD609098A79D4C54F5DB277DBD87)
