---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-67
title: 音频录制默认打断策略表
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 音频录制默认打断策略表
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a786e42d615194836b0a2a42fc0bfd1659bf31d777b77f6334f3af99bdcf8be9
---

## 问题现象

使用AudioCapture实现音频录制时，选择不同的录制音频流会造成不同的音频打断效果，本文提供手机场景下常见音频流类型与系统默认焦点策略之间的关联矩阵表，帮助用户选择合适的音频流，来满足用户预期录制行为。

## 背景知识

* [AudioCapturer](../harmonyos-guides/using-audiocapturer-for-recording.md)：用于音频输入的ArkTS/JS API，仅支持PCM格式，需要应用持续读取音频数据进行工作。应用可以在音频输出后添加数据处理，要求开发者具备音频处理的基础知识，适用于更专业、更多样化的媒体录制应用开发。
* 应用调用麦克风录音时，需要先[向用户申请授权](../harmonyos-guides/request-user-authorization.md)：ohos.permission.MICROPHONE。另外后台录制需要申请长时任务避免进入挂起（Suspend）状态。具体参考[长时任务(ArkTS)](../harmonyos-guides/continuous-task.md)。
* [SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)：录制音频流类型的枚举。

## 解决方案

|  | 后录制的音频流 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 先  录  制  的  音  频  流 | 音频流类型 | SOURCE\_TYPE\_MIC | SOURCE\_TYPE\_VOICE\_RECOGNITION | SOURCE\_TYPE\_VOICE\_COMMUNICATION | SOURCE\_TYPE\_VOICE\_MESSAGE | SOURCE\_TYPE\_CAMCORDER | SOURCE\_TYPE\_UNPROCESSED | SOURCE\_TYPE\_LIVE |
| SOURCE\_TYPE\_MIC | 同时录制 | 同时录制 | 停止先录音频 | 同时录制 | 同时录制 | 拒绝后录音频 | 拒绝后录音频 |
| SOURCE\_TYPE\_VOICE\_RECOGNITION | 同时录制 | 拒绝后录音频 | 暂停先录音频 | 暂停先录音频 | 暂停先录音频 | 同时录制 | 同时录制 |
| SOURCE\_TYPE\_VOICE\_COMMUNICATION | 拒绝后录音频 | 拒绝后录音频 | 暂停先录音频 | 拒绝后录音频 | 同时录制 | 拒绝后录音频 | 拒绝后录音频 |
| SOURCE\_TYPE\_VOICE\_MESSAGE | 同时录制 | 拒绝后录音频 | 停止先录音频 | 同时录制 | 同时录制 | 拒绝后录音频 | 拒绝后录音频 |
| SOURCE\_TYPE\_CAMCORDER | 同时录制 | 拒绝后录音频 | 停止先录音频 | 同时录制 | 同时录制 | 同时录制 | 拒绝后录音频 |
| SOURCE\_TYPE\_UNPROCESSED | 拒绝后录音频 | 拒绝后录音频 | 停止先录音频 | 拒绝后录音频 | 拒绝后录音频 | 拒绝后录音频 | 拒绝后录音频 |
| SOURCE\_TYPE\_LIVE | 拒绝后录音频 | 同时录制 | 停止先录音频 | 拒绝后录音频 | 拒绝后录音频 | 拒绝后录音频 | 拒绝后录音频 |
