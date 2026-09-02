---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-1
title: 进入应用阅读消息后，下滑通知栏中的消息通知没有自动消失
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 进入应用阅读消息后，下滑通知栏中的消息通知没有自动消失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a8f3ee7f5b9f28c0f7b4579c00b46433aa7dba981c12de50fdb2c4c7c2dad1a1
---

## 问题现象

打开应用查看消息通知后，通知栏里对应的提醒依然显示，未自动消失。

## 背景知识

* [notificationManager.cancel](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagercancel-2)：根据指定的通知ID取消已发布的通知。
* [notificationManager.cancelAll](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagercancelall)：取消当前应用所有已发布的通知。

## 问题定位

1. 在日志中搜索'Process push message'，可以看到应用推送了两条消息通知。

   ```txt
   C05300/push_manager_service/push50100073: Process push message begin, uniqMsgId: 4114A4E2A1666936, pushType: 0, packageName: 应用包名, userId: 100, appIndex: 0
   C05300/push_manager_service/push50100073: Process push message end, uniqMsgId: 4114A4E2A1666936, pushType: 0, packageName: 应用包名, userId: 100, appIndex: 0
   C05300/push_manager_service/push50100073: Process push message begin, uniqMsgId: 52B4A4E2E0707924, pushType: 0, packageName: 应用包名, userId: 100, appIndex: 0
   C05300/push_manager_service/push50100073: Process push message end, uniqMsgId: 52B4A4E2E0707924, pushType: 0, packageName: 应用包名, userId: 100, appIndex: 0
   ```
2. 然后搜索CancelNotification|Cancel Key，如果应用实现了取消已发布的通知的功能，可以搜到如下相关日志。

   ```txt
   02-11 10:50:54.697   1565-13357    C01203/foundation/Ans           foundation            I     CancelNotification key = __100_20020203_com.example__520749943-
   02-11 10:50:54.697   3220-3027     C01203/com.ohos.sceneboard/Ans  com.ohos.sceneboard   I     Cancel Key=__100_20020203_com.example__520749943,sortingMap size=0,reason=8
   ```

   如果是应用自身取消某个通知，则打印reason=8。

   如果是应用自身取消所有通知，则打印reason=9。

## 分析结论

结合问题现象和日志分析，通知栏发布该应用的通知消息后，用户打开应用查看消息，但是应用没有取消该应用的某个或者所有已发布的通知，导致用户发现通知栏的消息没有自动消失。

## 修改建议

建议打开应用时，根据消息ID使用notificationManager.cancel接口对当前应用的消息通知做清除操作。
