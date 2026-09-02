---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-18
title: 如何设置应用通知角标
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何设置应用通知角标
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:354242f127560aab6a5849f44b9c8d350c38c1735cedd271142125faa0b86a4a
---

## 问题现象

应用接收到消息或通知后会有通知角标提示，当点击阅读后，桌面的应用通知角标依然存在。如何设置应用通知角标，实现角标的累加和清零。

## 背景知识

通知角标设置按场景分为[Notification Kit](../harmonyos-guides/notification-kit.md)和[Push Kit](../harmonyos-guides/push-kit-guide.md)两种通知角标，两种场景实现不同。

* [Notification Kit](../harmonyos-guides/notification-overview.md)：用户通知服务，为开发者提供本地通知发布通道，应用通过Notification Kit将应用产生的通知在客户端本地推送给用户。当应用进程处于运行时，开发者可以使用Notification Kit向用户发布通知。当应用进程终止后，本地通知发布通道关闭，开发者需要接入[Push Kit](../harmonyos-guides/push-kit-introduction.md)进行云侧离线通知的发布。
* [Push Kit](../harmonyos-guides/push-kit-introduction.md)：推送服务，是华为提供的消息推送平台，建立了从云端到终端的消息推送通道，可以为应用实现实时消息推送，提升用户感知度。

## 解决方案

场景一、Notification通知角标。角标设置方式支持如下两种方式：

* 发布通知时，在[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)的badgeNumber字段里携带：桌面收到通知后，在原角标数上累加、呈现。
* 调用接口[setBadgeNumber()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)设置，桌面按设置的角标数呈现：使用此方法首先需要获取当前未读通知数量，在后续通知发布成功或阅读通知内容后，使用setBadgeNumber管理增减逻辑。可通过setBadgeNumber设置为0，实现清理角标数量。

**说明** 

setBadgeNumber为异步接口，使用setBadgeNumber连续设置角标时，为了确保执行顺序符合预期，需要确保上一次设置完成后才能进行下一次设置。使用async/await控制角标设置，可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/custom-notification-badge/blob/master/notification/src/main/ets/notification/NotificationManagementUtil.ets)。

场景二、Push通知角标设置。

发送[AlertPayload 通知消息](../harmonyos-references/push-scenariozed-api-request-param.md#alertpayload-通知消息)时携带[Badge](../harmonyos-references/push-scenariozed-api-request-param.md#badge)字段来设置应用收到通知消息后以数字的形式展示角标，提醒用户查看消息，具体参考Push Kit[通知角标](../harmonyos-guides/push-send-alert.md#通知角标)实现。角标设置方式支持如下两种方式：

* 自增长累加效果，可以在[Badge](../harmonyos-references/push-scenariozed-api-request-param.md#badge)字段设置addNum为应用角标需要累加数字即可。
* [Badge](../harmonyos-references/push-scenariozed-api-request-param.md#badge)字段设置setNum，设置的值为角标实际显示数字，且setNum优先级高于addNum。

**说明** 

打开应用或者点击、清理通知消息并不会清理角标数字，可通过[setBadgeNumber()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)方法清理角标。

## 常见FAQ

Q：[notificationManager.setBadgeNumber](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)调用成功，但是看不到通知角标。

A：角标显示应用需要完成[请求通知授权](../harmonyos-guides/notification-enable.md)，确认“桌面角标”选项已开启。如果在通知管理中关闭“桌面角标”，则无法显示角标数，可在应用中通过[notificationManager.openNotificationSettings](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettings13)完成二次申请授权。
