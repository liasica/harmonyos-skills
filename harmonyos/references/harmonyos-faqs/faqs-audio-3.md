---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-3
title: OpenSL ES音频录制示例调用崩溃
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > OpenSL ES音频录制示例调用崩溃
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5fa5041625aca3d450e886b5010515a49b32738c4225f7b465863962c6275a6c
---

## 问题现象

OpenSL ES音频录制接口调用失败，程序崩溃。报错日志信息如下：

08-06 00:39:20.042 5198-5219/? E C02b00/AudioFramework: [audio\_service\_client.cpp] Client doesn't have MICROPHONE permission

## 解决措施

需要申请ohos.permission.MICROPHONE权限。详情请参见[开放权限（用户授权）](../harmonyos-guides/permissions-for-all-user.md)。
