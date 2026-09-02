---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-9
title: 通知扩展消息语音播放提前退出
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 通知扩展消息语音播放提前退出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:2cafd106c57e05ecd965c3c41bfa52750b28478e8adf9ecd506f399d90d57133
---

## 问题现象

申请通知扩展消息权限进行语音播报，语音播报通过[SoundPool](../harmonyos-guides/media-kit-intro.md#soundpool)串行播放多个音频实现。文档中[通知扩展进程](../harmonyos-references/push-remote-notification-extension-ability.md)能持续10秒，实际使用中播报3秒就停止了。

## 背景知识

[发送通知扩展消息](../harmonyos-guides/push-send-extend-noti.md)：当应用进程不在前台时，Push Kit会将消息内容传递给通知扩展进程，您可以在该进程中自行完成业务处理（例如：语音播报、消息内容解密等）后，返回自定义消息内容，Push Kit将弹出通知提醒。您需要在10秒内返回消息内容，否则Push Kit将默认展示原有的消息内容。

## 问题定位

根据日志可知：

1. 16:58:51.707：push\_manager\_service启动通知扩展子进程RemoteNotificationExtensionAbility，处理扩展通知消息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/LMADvY3dRTqX6Kfyqc4m_A/zh-cn_image_0000002658913761.png "点击放大")
2. 16:58:51.790：触发[onReceiveMessage()](../harmonyos-references/push-remote-notification-extension-ability.md#onreceivemessage)回调，开始初始化SoundPool处理语音消息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/-IrsLZTbTjeySi7MF64Ahw/zh-cn_image_0000002658793815.png "点击放大")
3. 16:58:51.790：RemoteNotificationExtensionAbility子进程生命周期销毁。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/VSd_i0weQGWUOx7V7S3gaQ/zh-cn_image_0000002628394544.png "点击放大")

   但后续音频一直在播放，直到16:58:54.420。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/NDN7r4YBSwq_-N7OD6EzSA/zh-cn_image_0000002628554438.png "点击放大")
4. 16:58:54.808：触发系统冻结进程，音频播放终止。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/mJ4jsMroTDCI_ZoiOjz7iw/zh-cn_image_0000002658913763.png "点击放大")

结合代码可知，在onReceiveMessage()中收到消息后，语音播报逻辑未执行完，直接返回了处理后的消息。导致RemoteNotificationExtensionAbility提前结束了生命周期，使得语音播放没有播放完就系统冻结，进程挂起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/8uYu2jDjQg-2CbIFtkuvRw/zh-cn_image_0000002658793817.png "点击放大")

## 分析结论

语音播报代码时序问题：语音播报使用异步方法执行，导致扩展通知子进程提前结束。音频处理在子进程结束后，被系统冻结无法播放。

## 修改建议

使用[async/await](../harmonyos-guides/async-concurrency-overview.md#asyncawait)处理语音播报操作，确认音频播放完成后再在onReceiveMessage()中返回处理后的消息，确保RemoteNotificationExtensionAbility没有提前退出。

## 常见FAQ

Q：同时收到多条扩展消息通知后，语音播放消息内容超过1分20秒终止怎么处理？

A：检查是否是确认音频播放完成后再在onReceiveMessage()中返回的通知消息，保证播放的时序。

Q：播放长语音通知扩展消息后，发现应用通知角标未发生变化。

A：请检查原始消息体是否包含角标信息，原因如下：RemoteNotificationExtensionAbility子进程存活的时间是10秒，需要在10秒内返回消息内容，否则Push Kit将默认展示原有的消息内容。语音时间过长导致播放超过10秒时，如果原始的消息体中不含角标消息，则返回的通知也不含角标信息。
