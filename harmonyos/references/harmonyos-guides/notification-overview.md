---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-overview
title: Notification Kit简介
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > Notification Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d0ca98ca16ffcca2910b902b83fe939ff2e602fbe3b8bb3678fefbcbd29f3ee7
---

Notification Kit（用户通知服务）为开发者提供本地通知发布通道，开发者可借助Notification Kit将应用产生的通知直接在客户端本地推送给用户，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。

## 使用场景

当应用进程处于运行时，开发者可以使用Notification Kit向用户发布通知。当应用进程终止后，本地通知发布通道关闭，开发者需要接入[Push Kit](push-kit-introduction.md)进行云侧离线通知的发布。

开发者可以在多种场景中运用本地通知能力。如同步用户的上传下载进度、发布即时的客服支付通知、更新运动步数等。

## 能力范围

Notification Kit支持的能力主要包括：

* 发布文本、进度条等类型通知。
* 携带或更新应用通知数字角标。
* 取消曾经发布的某条或全部通知。
* 查询已发布的通知列表。
* 查询应用自身通知开关状态。
* 应用通知用户的能力默认关闭，开发者可拉起授权框，请求用户授权发布通知。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/gY-frg8hTh2VM2qzZbLyfQ/zh-cn_image_0000002558765560.png?HW-CC-KV=V1&HW-CC-Date=20260429T053921Z&HW-CC-Expire=86400&HW-CC-Sign=776F5F990DF28C1CB1360B1E9F34DC0789845BCAF2AF7E3FAEA16523B63FA12E)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/36lbroFaRDuVF5Syisc7Cg/zh-cn_image_0000002558605904.png?HW-CC-KV=V1&HW-CC-Date=20260429T053921Z&HW-CC-Expire=86400&HW-CC-Sign=8E7176FB20DD22AA69BB74C5CBDF9FFFD5065E306933939D716EE9BA77104A52)

使用Notification Kit的主要业务流程如下：

1.请求通知授权。

2.应用发布通知到通知服务。

3.将通知展示到通知中心。

## 通知样式

说明

实际显示效果依赖设备能力和通知中心UI设计样式。

Notification Kit中常用的通知样式如下：

| 类型 | 通知样式 | 规格描述 |
| --- | --- | --- |
| [文本](text-notification.md) |  | 通知文本内容最多显示三行，超长后以“...”截断。 |
| [多行文本](text-notification.md) |  | 最多可显示三行内容，每行内容超长后以“...”截断。 |
| [通知角标](notification-badge.md) |  | 以数字的形式展示在右上角。 |
| [进度条](progress-bar-notification.md) |  | 进度类通知。 |

## 约束限制

* 单个应用已发布的通知在通知中心等系统入口的留存数量有限（当前规格最多24条）。
* 通知的长度不能超过200KB（跨进程序列化大小限制）。
* 通知的发布频次和更新频次需要满足如下要求，否则会导致发布或更新失败，返回相应错误码。
  + 单个应用发布新通知的频次累计不能超过每秒10条，更新通知的频次累计不能超过每秒20条。
  + 所有三方应用发布新通知的频次累计不能超过每秒15条，更新通知的频次累计不能超过每秒30条。

## 违规处罚

应用发送的通知需遵守Push Kit的[通知内容原则](push-detail-rules.md)，如出现违反通知内容原则的行为，将被视为违规。

违规行为及相应的处理措施请参见[违规分类、违规行为及违规处罚标准](push-punishment-standards.md)。

## 与相关Kit的关系

* Notification Kit创建的通知会即时显示在通知中心等系统入口。如果开发者希望在应用退到后台或进程终止后仍然有一些提醒用户的定时类通知，例如购物类应用抢购提醒等，可通过[Background Tasks Kit](background-task-overview.md)创建。目前支持基于倒计时、日历、闹钟等类型的通知提醒功能。
* 开发者可通过[Ability Kit](abilitykit-overview.md)的[getWantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md#wantagentgetwantagent)接口设置用户点击通知后的行为意图。
* 开发者可通过[Push Kit](push-kit-introduction.md)远程推送用户通知到本地。

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](ide-emulator-specification.md)”。
