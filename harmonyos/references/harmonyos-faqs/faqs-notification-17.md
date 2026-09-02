---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-17
title: 如何实现应用内提示音：通知与自定义消息场景
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何实现应用内提示音：通知与自定义消息场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f1ea776494e97bf5875af68afa35979b4978b1151acdd3a5df6b0310a63872b8
---

## 问题现象

在App中使用WebSocket，当消息通过WebSocket推送过来时，有一个提示音播放，请问有没有相关API？

## 背景知识

* [Notification Kit（用户通知服务）](../harmonyos-guides/notification-overview.md)：可借助Notification Kit将应用产生的通知直接在客户端本地推送给用户，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。
* [SoundPool](../harmonyos-guides/media-kit-intro.md#soundpool)：SoundPool可以实现简单的提示音。

## 解决方案

通过以下两种方式播放提示音：

* [使用SoundPool播放短音频(ArkTS)](../harmonyos-guides/using-soundpool-for-playback.md)以实现一些急促简短的音效播放。详情可见[运行示例工程](../harmonyos-guides/using-soundpool-for-playback.md#运行示例工程)。
* 使用[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)的sound字段设置自定义铃声文件。该文件放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。当不设置sound字段时，设备接收新消息时铃声会默认播放通知提示音。

## 常见FAQ

Q：播放短促提示音（如点赞、收藏、新消息等场景的提示音或音效），应该如何处理？

A：

* 推荐优先使用SoundPool，若应用使用SoundPool开发音频播放功能，且[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)指定为STREAM\_USAGE\_MUSIC、STREAM\_USAGE\_MOVIE、STREAM\_USAGE\_AUDIOBOOK等类型，播放短音，则其申请焦点时默认为并发模式，不会影响其他音频。
* 若应用不希望使用SoundPool，并且当前使用的流类型会打断其他音频播放，推荐使用[音频会话策略（AudioSessionStrategy）](../harmonyos-guides/audio-session-management.md#音频会话策略)相关接口，指定为CONCURRENCY\_MIX\_WITH\_OTHERS策略。
