---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-distributed-overview
title: 跨设备协同通知概述
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 跨设备协同通知 > 跨设备协同通知概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:8d09c233a474bf6b008a0d06268ca8201c86783526d1db35a4f465730a9cfcff
---

[跨设备协同](notification-glossary.md#cross-device-collaboration跨设备协同)通知旨在以手机为中心，实现与手表等其他设备的通知消息协同交互。典型场景如下：

* [清除跨设备场景下的重复通知](notification-distributed-messageid.md)：清除跨设备协同消息和本地设备发布的重复消息，避免多源通知重复打扰用户。

## 约束条件

* [跨设备协同](notification-glossary.md#cross-device-collaboration跨设备协同)支持的设备：从API版本18开始，支持Phone与Wearable之间通知消息的协同；从API版本20开始，支持Phone与Tablet、PC/2in1设备之间通知消息的协同。
* 跨设备协同支持的[通知渠道](../harmonyos-references/js-apis-notificationmanager.md#slottype)：
  + Wearable：带快捷回复的社交通讯类通知（社交通讯）、实况窗。
  + Tablet：社交通讯、服务提醒、实况窗、客服消息。
  + PC/2in1：社交通讯、服务提醒、客服消息。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Ylr1ra79TfW6R7PQuq7sEQ/zh-cn_image_0000002815399973.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D4E4682AE16E9B280646BFDE45C42485E04F15E966BA4BA20D06684981BCA49)
