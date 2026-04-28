---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-1
title: 如何后台播放音乐
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何后台播放音乐
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3860282cdb2373fd4beadc7324c72074b8c64fa4d09b6c49d5f128d96a3596de
---

AVSession管控媒体播放。当第三方应用从前台切换到后台或进入锁屏状态时，媒体播放会强制暂停，且应用不会感知。若需开发后台播放功能，应在后台任务管理中启动长时任务播放音乐，并接入AVSession能力，允许控制中心的播控面板控制第三方应用的播放功能。

**参考链接**

[backgroundTaskManager.startBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning12)

[媒体会话提供方](../harmonyos-guides/using-avsession-developer.md)
