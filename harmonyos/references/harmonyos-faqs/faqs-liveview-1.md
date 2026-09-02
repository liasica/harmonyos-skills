---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-liveview-1
title: 实况窗推送内容如何实现自定义
breadcrumb: FAQ > 应用服务开发 > 实况视图服务（Live View Kit） > 实况窗推送内容如何实现自定义
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:8f4442c23c979d2205d6405a8de0c79304f18ef19969932de392a690f0a994c2
---

## 问题现象

在HarmonyOS中，实况窗推送内容能否实现自定义？

## 解决方案

[ActivityData](../harmonyos-references/push-scenariozed-api-request-param.md#activitydata)字段可以填写实况窗数据。ActivityData中可传入的参数有以下三种：

* [NotificationData](../harmonyos-references/push-scenariozed-api-request-param.md#notificationdata)消息通知布局数据。
* [CapsuleData](../harmonyos-references/push-scenariozed-api-request-param.md#capsuledata)胶囊通知布局数据。
* [ExternalData](../harmonyos-references/push-scenariozed-api-request-param.md#externaldata)小外屏（Pocket等系列手机外屏）展示数据。

其中NotificationData中的clickAction结构体中的data可以传入开发者的自定义数据，不过该数据有[使用约束](../harmonyos-references/push-scenariozed-api-intro.md#使用约束)。

* 消息体最大不能超过4096Bytes（不包括Push Token）。
* 消息发送量，测试消息（参考消息体pushOptions.testMessage）每个项目限制所有应用共享1000条/天，正式消息区分场景有不同的配额，参考[消息频控](../harmonyos-references/push-msg-freq-control.md)说明。

出于用户体验一致性，实况窗布局是固定的无法自定义，但实况窗展示内容应用可自定义。当前系统已提供进度可视化模板、强调文本模板、左右文本模板、赛事比分模板、导航等[模板类型](../design-guides/system-features-live-view-0000001955186861.md#section1511241615274)供应用选择。应用发送实况窗需遵循[实况窗设计规范](../harmonyos-guides/liveview-design-formula.md)，不符合设计规范的方案将不予开通正式权限。需要注意的是：

1. 单个实况窗的生命周期最长不超过8小时，超过8小时后，系统会认为实况窗结束。
2. 为了确保用户看到内容的时效性，请开发者及时更新实况窗内容。系统会在以下情况自动调整实况窗的展示：超过2小时未更新：状态栏胶囊和锁屏胶囊将被隐藏，仅保留在通知中心展示；超过4小时未更新：系统将判定实况窗已结束，并从所有展示入口清除该实况窗。
