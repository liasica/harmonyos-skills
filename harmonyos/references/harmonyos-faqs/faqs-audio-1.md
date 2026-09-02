---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-1
title: 如何后台播放音乐
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何后台播放音乐
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5d94a0935f28c8f953e536cf01a6db202f3d7487ee2ea4e6e1630992a96cc3fe
---

AVSession管控媒体播放。当第三方应用从前台切换到后台或进入锁屏状态时，媒体播放会强制暂停，且应用不会感知。若需开发后台播放功能，应在后台任务管理中启动长时任务播放音乐，并接入AVSession能力，允许控制中心的播控面板控制第三方应用的播放功能。

## 参考链接

[backgroundTaskManager.startBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning12)

[媒体会话提供方](../harmonyos-guides/using-avsession-developer.md)
