---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessibilitykit-overview
title: Accessibility Kit 简介
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > Accessibility Kit 简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:06+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:895ec14df8957b8c4a751518f8821628a8b7839208ee3f9e4dc54006c22159ed
---

## 概述

Accessibility（信息无障碍）指的是确保任何人在任何情况下都能平等、便捷地获取并利用信息。其目标在于缩小社会各阶层、各地区、各年龄段以及不同健康状况人群在信息理解、交互和利用方面的数字鸿沟，使他们能够更加便捷地融入社会生活，充分享受数字化发展带来的便利。

所以，无论是开发新的应用，还是对已有应用的更新，都应该考虑到无障碍需求，让应用能够被更多的人所使用。Accessibility Kit（无障碍服务）则为应用更好的适配无障碍，开放了必要的能力，如为组件添加无障碍焦点、无障碍朗读文本等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/-FbEZBNfS8CVgmAaj2LcFg/zh-cn_image_0000002583477515.png?HW-CC-KV=V1&HW-CC-Date=20260427T233805Z&HW-CC-Expire=86400&HW-CC-Sign=06E9D47D1FC09D9F43ABC4E2EAE4BD02D1FEF1C7128454259DE28243333E6489)

* **系统服务：** 系统针对不同的障碍人群和障碍场景，提供了多种辅助服务能力，如屏幕朗读、大字体、高对比度文字、色彩校正、颜色反转、单声道音频、音量平衡、屏幕触控等。
* **开放能力：** 基于系统服务，为应用提供了无障碍开放能力，如屏幕朗读开启状态的查询，无障碍朗读文本的设置、主动播报等。
* **应用：** 应用在设计时，需要在布局、配色、字体、交互、播报、反馈维度等多个方面，都要考虑到信息获取和应用使用的无障碍，并结合Accessibility Kit提供的开放能力，更好的适配无障碍。

## 能力范围

* **无障碍状态查询：** 为应用提供无障碍服务开启状态、触摸浏览开启状态查询接口，以便应用根据无障碍功能开启状态，更好的服务于障碍人群和障碍场景。
* **无障碍事件发送：** 为应用提供主动聚焦、主动朗读等无障碍事件发送接口，以便应用结合业务场景，做到更好的无障碍体验。

## 与相关Kit的关系

ArkUI Kit为Accessibility提供无障碍组件属性定义、无障碍事件发送能力，应用可基于ArkUI Kit为组件设置无障碍文本、描述信息等属性。

## 模拟器支持情况

本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下。

* 通用差异：请参见[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)。
* 不支持放大手势、声音修复、助听设备、闪烁提醒等功能。
