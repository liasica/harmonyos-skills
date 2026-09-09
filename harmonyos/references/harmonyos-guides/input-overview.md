---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/input-overview
title: Input Kit简介
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > Input Kit简介
category: harmonyos-guides
scraped_at: 2026-09-10T06:22:41+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:82dd88edafe1e03bffb7d37cd98926a9174920037e9550dd4abea5906b38f8b6
---

## 功能介绍

Input Kit（多模输入Kit）为多种输入设备提供服务，如触控板、触摸屏、鼠标、键盘等。通过对这些输入设备上报驱动事件的归一化处理，确保不同输入设备与用户交互体验统一和流畅。

Input Kit除了提供基础的输入事件服务之外，还提供了获取输入设备列表、改变鼠标光标样式等功能和接口。

## 运作机制

多模输入能力作为系统为应用提供的一种基础服务，通过处理上报的输入设备驱动事件，完成输入事件管理、接收、预处理、分发，通过inner SDK与JSkit上报应用，具体运行机制如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/BZyH1S0MRRuH_L0cXx08rA/zh-cn_image_0000002717771180.png)

## 模拟器支持情况

本Kit支持模拟器，但与真机存在差异，具体差异如下。

* 通用差异：详情请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 模拟器不支持鼠标光标属性相关设置。
