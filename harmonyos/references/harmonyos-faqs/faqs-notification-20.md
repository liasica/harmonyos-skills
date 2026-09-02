---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-20
title: 通知订阅扩展能力常见问题
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 通知订阅扩展能力常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:2d052b3887c9220b8ef21595a7ae44b8b330a659a723fb5baafc1983270893d5
---

## 问题现象

使用通知订阅能力，已使用[openSubscriptionSettings](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettings)接口完成通知授权和设备连接订阅，仍然无法在[onReceiveMessage](../harmonyos-references/js-apis-notificationsubscriberextensionability.md#onreceivemessage)中收到回调，该如何排查问题。

## 解决方案

**onReceiveMessage未收到回调原因排查：**

* 检查点一、确认用户已通过手机中的穿戴应用程序与穿戴设备配对。可以在设置-星闪和蓝牙-已配对设备中查看穿戴设备配对状态。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/TtWD1yX9T5OAkDwa0eLuqw/zh-cn_image_0000002628554622.png "点击放大")

  手机与穿戴设备配对有两种方式：

  1. 星闪和蓝牙-其他设备列表中选择设备，手动完成配对操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/n0HqIqTJSr6wyuhwZm1WmA/zh-cn_image_0000002658913945.png "点击放大")
  2. 应用内使用[connection.pairDevice](../harmonyos-references/js-apis-bluetooth-connection.md#connectionpairdevice)接口主动发起配对。

     **说明** 

     支持[HFP](../harmonyos-guides/terminology.md#hfp)连接的设备，需保证HFP连接一直处于连接状态。
* 检查点二、确认已使用[openSubscriptionSettings](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettings)接口完成通知授权。
* 检查点三、确认使用[蓝牙模块](../harmonyos-guides/connectivity-kit-intro.md#蓝牙简介)接口与穿戴设备配对后获取的地址，通过[subscribe](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionsubscribe)接口订阅通知。未订阅时[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)无法收到onReceiveMessage回调。

**onReceiveMessage回调日志排查和断点调试：**

完成上述检查后请确认onReceiveMessage可以收到回调消息，需要注意的是：

1. NotificationSubscriberExtensionAbility是[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)运行在独立进程，IDE查看日志不能筛选当前主进程，需要选择“No fliters”。
2. 调试NotificationSubscriberExtensionAbility时，请参考[extension调试](../harmonyos-guides/ide-debug-arkts-extension.md)。

**通知转发到穿戴设备：**

使用onReceiveMessage收到回调后，穿戴设备不会自动显示消息通知，需要应用自行开发相关代码，调用蓝牙等协议转发通知消息给穿戴设备。

**说明** 

可参考官网示例：[传统蓝牙连接示例](../harmonyos-guides/notification-subscriber-extension-ability-development-steps.md)。注：示例仅作流程参考。
