---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-subscriber-extension-ability
title: 通知订阅扩展能力概述
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 通知订阅扩展能力 > 通知订阅扩展能力概述
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:14+08:00
doc_updated_at: 2026-08-21
content_hash: sha256:33cd0f3adfc55d4854229eb2813de2731d1a6d4022b665999b9aac7108fef9be
---

## 功能简介

此扩展能力的核心作用是让三方应用接收系统通知，应用可在此扩展能力中实现与穿戴设备之间的数据传输。应用发送通知给[分布式通知](notification-glossary.md#distributed-notification分布式通知)服务后，该服务会把通知转发给三方应用实现的[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)。若一定时间内无新通知发布，当前运行的[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)会被系统自动销毁。

## 前提条件

* 用户已通过穿戴应用程序与穿戴设备配对。
* 用户已在穿戴应用中，通过[openSubscriptionSettingsWithResult](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettingswithresult)接口拉起的半模态弹窗中，开启了“允许获取本机通知”与“已获取的本机通知”的开关。
* 支持[HFP](terminology.md#hfp)连接的设备，需保证HFP连接一直处于连接状态。

## 应用场景

* **使用场景**：系统通知同步到穿戴设备
* **传输方式**：支持低功耗蓝牙（Bluetooth Low Energy）和传统蓝牙两种同步方式

## 约束条件

1. 本示例仅支持标准系统上运行，支持设备：Phone和Tablet。
2. 本示例为Stage模型，支持API22及以上版本SDK。
3. 本示例需要使用DevEco Studio 6.0.2 Release及以上版本才可编译运行。
4. 三方穿戴应用需申请[ohos.permission.SUBSCRIBE\_NOTIFICATION](restricted-permissions.md#ohospermissionsubscribe_notification)权限，权限为system\_basic级别。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/wHgxGV9bQsGUppgELZcc6Q/zh-cn_image_0000002712405290.png)
