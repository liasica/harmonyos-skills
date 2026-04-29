---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/call-introduction
title: Call Service Kit简介
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > Call Service Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a3658399f3a3cb30ec2eade29f4262981fddcc2a595663a778c435e19f920ea1
---

Call Service Kit（通话服务）是HarmonyOS为开发者提供的应用内通话管理服务。

开发者通过集成Call Service Kit，可以实现便捷的来电一键接听、横幅通知、静音与取消静音等功能，提升用户体验。

## 场景分类

应用内通话，主要分为来电场景、去电场景两类。

* 来电场景

  应用接收到来自网络的音/视频通话，称为来电场景。

  在来电场景中，应用需要将来电信息上报给Call Service Kit，系统会为用户展示来电横幅通知。用户可以在横幅上执行接听或拒接来电、静音与解除静音、挂断通话等操作。

  此外，Call Service Kit还支持锁屏来电通知、多路来电通知等。
* 去电场景

  应用主动发起音/视频通话，称为去电场景。去电场景与来电场景大部分功能相似，但有以下几点区别：

  + 去电时，由于应用在前台，不需要展示横幅通知，只在屏幕左上角展示通话胶囊。
  + 去电不支持多路共存，即同一时间，只能有1路去电存在。

## 与相关Kit的关系

当应用在后台时，如果有来电，需要[Push Kit（推送服务）](push-kit-introduction.md)先拉起应用主进程，应用才能给Call Service Kit上报来电。

业务流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/0pJ4lSCGSy6_pJufsk-nhg/zh-cn_image_0000002589325197.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053736Z&HW-CC-Expire=86400&HW-CC-Sign=046B804B6A424F4EF3E4EAED06DFFC5026D1BD7C7E849E9B6D1AD4D7A0A728C9)

## 约束和限制

### 设备限制

本示例仅支持标准系统上运行，不支持模拟器。

| 能力 | 支持设备 |
| --- | --- |
| 来电场景 | Phone、Tablet，Wearable。 |
| 去电场景 | Phone、Tablet，Wearable。 |
| 企业联系人信息来去电页面显示 | Phone、Tablet、PC/2in1、Wearable。 |

### 通话数量

* 同一时间，最多支持3路应用内来电。
* 同一时间，最多支持1路应用内去电。

### 支持的国家/地区

Call Service Kit提供的能力当前只支持中国大陆。

### 相关Kit的约束和限制

由于Call Service Kit依赖Push Kit，还需要参考[Push Kit的约束和限制](push-kit-introduction.md#约束和限制)。

## 模拟器支撑情况

本kit暂不支持模拟器
