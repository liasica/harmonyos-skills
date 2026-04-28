---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-subscriber-extension-ability
title: NotificationSubscriberExtensionAbility (开发概述)
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 通知订阅扩展能力 > NotificationSubscriberExtensionAbility (开发概述)
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:03+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:8f5d5e90b6796347266389a521360ad799fef9cdce05a965447b0b31e66b119c
---

## 功能简介

此扩展能力的核心作用是让三方应用接收系统通知，应用可在此扩展能力中实现手机与穿戴设备之间的数据传输。应用发送通知给分布式通知服务后，该服务会把通知转发给三方应用实现的[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)。若一定时间内无新通知发布，当前运行的[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)会被系统自动销毁。

## 前提条件

* 用户已通过手机中的穿戴应用程序与穿戴设备配对。
* 用户已在手机的穿戴应用中，通过[openSubscriptionSettings](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettings)接口拉起的半模态弹窗中，开启了“允许获取本机通知”与“已获取的本机通知”的开关。
* 支持[HFP](terminology.md#hfp)连接的设备，需保证HFP连接一直处于连接状态。

## 应用场景

* **使用场景**：手机通知同步到穿戴设备
* **传输方式**：支持低功耗蓝牙（Bluetooth Low Energy）和传统蓝牙两种同步方式

## 约束条件

1. 本示例仅支持标准系统上运行，支持设备：手机和平板。
2. 本示例为Stage模型，支持API22及以上版本SDK。
3. 本示例需要使用DevEco Studio 6.0.2 Release及以上版本才可编译运行。
4. 三方穿戴应用需申请[ohos.permission.SUBSCRIBE\_NOTIFICATION](restricted-permissions.md#ohospermissionsubscribe_notification)权限，权限为system\_basic级别。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/ue7MeeuCQ-GRzRmqGcLttw/zh-cn_image_0000002552799414.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=8FABF4AC436D2177BE7CE3E0CB1A7ADE8378E56BD028CD5C17B5AEA1BD87B892)
