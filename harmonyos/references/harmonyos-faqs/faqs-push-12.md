---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-12
title: 应用在前台时能否获取通知消息的内容
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 应用在前台时能否获取通知消息的内容
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:3dfc1b9a10ad50e64c70adbfbc43a7dbcdb2097a64770aa3bd7b49de57837abe
---

## 问题现象

应用在前台打开有什么接口能在获取到通知消息的内容，使用[pushService.receiveMessage()](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)并没有触发消息回调？

## 解决方案

应用内推送消息或通知内容可以分为以下几种场景：

应用处于后台场景：

仅有[语音播报消息](../harmonyos-guides/push-extend-noti.md)和[应用内通话消息](../harmonyos-guides/push-voip.md)可以在应用内接收消息，使用[后台消息](../harmonyos-guides/push-background.md)可以缓存消息，但不会拉起应用进程。

应用处于前台场景：

可以通过在UIAbility中调用[pushService.receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)接收Push场景化消息。

**说明** 

* UIAbility.onCreate是同步接口，不支持异步回调，需要在onCreate生命周期的入口，完成pushService.receiveMessage()注册，并且保证在注册前没有等待异步方法执行的调用。
* 需要在对应的UIAbility类型的组件的onCreate()中，调用receiveMessage()方法接收消息，并不是固定在EntryAbility的onCreate()中调用。

* 通知消息场景：
  1. 将REST API发送的通知消息体[Notification](../harmonyos-references/push-scenariozed-api-request-param.md#notification)中foregroundShow设置为false，此时通知消息将不会展示，可以通过pushService.receiveMessage()接收通知消息数据（foregroundShow为true时，无法通过pushService.receiveMessage()获取消息数据）。
  2. 在项目模块的“src/main/module.json5”文件的对应abilities模块中（以PushMessageAbility为例），配置skills标签的actions属性内容为action.ohos.push.listener，有且只能有一个ability定义该action，若同时添加uris参数，则uris内容需为空。
  3. 通过pushService.receiveMessage()方法传入PushType为"DEFAULT"获取通知消息，PushMessageAbility示例代码详情请参见[应用在前台时处理通知消息](../harmonyos-guides/push-send-alert.md#应用在前台时处理通知消息)。
* 语音播报消息场景：
  1. 完成[申请推送语音播报消息权益](../harmonyos-guides/push-apply-right.md#申请推送语音播报消息权益)。
  2. 在项目模块的“src/main/module.json5”文件的对应abilities模块中（以PushMessageAbility为例），配置skills标签的actions属性内容为action.ohos.push.listener，有且只能有一个ability定义该action，若同时添加uris参数，则uris内容需为空。
  3. 通过pushService.receiveMessage()方法传入PushType为"IM"获取语音播报消息，用于应用在前台时接收语音播报消息。

     调用示例代码请参考[开发步骤](../harmonyos-guides/push-send-extend-noti.md#开发步骤)中步骤3。
* 应用内通话场景：
  1. 完成[申请推送应用内通话消息权益](../harmonyos-guides/push-apply-right.md#申请推送应用内通话消息权益)。
  2. 在项目模块的“src/main/module.json5”文件的对应abilities模块中（以PushMessageAbility为例），配置skills标签的actions属性内容为action.ohos.push.listener，有且只能有一个ability定义该action，若同时添加uris参数，则uris内容需为空。
  3. 通过receiveMessage()方法传入PushType为"VoIP"获取应用内通话消息。调用示例代码请参考[开发步骤](../harmonyos-guides/push-send-extend-noti.md#开发步骤)中步骤2。
* 后台消息场景：
  1. 在项目工程的“src/main/module.json5”文件的abilities模块的skills标签中配置actions内容为action.ohos.push.listener（有且只能有一个ability定义该action，若同时添加uris参数，则uris内容需为空）。
  2. 通过pushService.receiveMessage()方法传入PushType为"BACKGROUND"获取后台消息。调用示例代码请参考[开发步骤](../harmonyos-guides/push-send-extend-noti.md#开发步骤)中步骤5。

获取通知栏消息内容场景：

调用[notificationManager.getActiveNotifications](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagergetactivenotifications-1)可以获取当前应用未删除的通知列表。可以通过读取返回值中[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)获取通知内容。
