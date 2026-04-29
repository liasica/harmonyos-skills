---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-9
title: 应用处于后台时应用内如何接收消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 应用处于后台时应用内如何接收消息
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:59+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8e2cfdd3c380c3f1df52b85834233ab5ccf5f384dfd33fc149384ebf805b2a08
---

应用处于后台时仅有如下两个场景可以在应用内接收消息：

* 若应用需要实现语音播报等能力时，服务端可发送**语音播报消息**（即[push-type](../harmonyos-references/push-scenariozed-api-intro.md#场景介绍)为**2**）。该场景中客户端应用内消息接收请参考RemoteNotificationExtensionAbility中[接口调用示例](../harmonyos-references/push-remote-notification-extension-ability.md#onreceivemessage)。
* 若应用需要实现网络音视频通话能力时，服务端可发送**应用内通话消息**（即push-type为**10**）。该场景中客户端应用内消息接收请参考VoIPExtensionAbility中[接口调用示例](../harmonyos-references/push-voip-ability.md#onreceivemessage)。

当应用处于内容不频繁更新，不会显示通知、播放铃声或改变应用角标场景时，服务端可发送**后台消息**（即push-type为**6**），若[proxyData](../harmonyos-references/push-scenariozed-api-request-param.md#backgroundpayload-后台消息)为“ENABLE”时，Push Kit将后台消息写入到数据库中，不会拉起应用进程。
