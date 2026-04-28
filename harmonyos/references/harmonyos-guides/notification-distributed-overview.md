---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-distributed-overview
title: 跨设备协同通知概述
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 跨设备协同通知 > 跨设备协同通知概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fd5d4a4b281227371b2ecc8d6949bb33365b8da1a5bec9f98d50f9c21bf2a87b
---

跨设备协同通知旨在以手机为中心，实现与手表等其他设备的通知消息协同交互。典型场景如下：

* [清除跨设备场景下的重复通知](notification-distributed-messageid.md)：清除跨设备协同消息和本地设备发布的重复消息，避免多源通知重复打扰用户。

## 约束条件

* 跨设备协同支持的设备：从API Version 18开始，支持手机与手表之间通知消息的协同；从API Version 20开始，支持手机与平板、2in1设备之间通知消息的协同。
* 跨设备协同支持的[通知渠道](../harmonyos-references/js-apis-notificationmanager.md#slottype)：
  + 手表：带快捷回复的社交通信类通知（社交通信）、实况窗。
  + 平板：社交通信、服务提醒、实况窗、客服消息。
  + 2in1：社交通信、服务提醒、客服消息。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/wJmm47CPRlmew9NQBhAVLw/zh-cn_image_0000002552959062.png?HW-CC-KV=V1&HW-CC-Date=20260427T235001Z&HW-CC-Expire=86400&HW-CC-Sign=C944BB65F5BB25460EFE02FFD6C83473FE7DF3BD2A6778AC3209010616ABBEF6)
