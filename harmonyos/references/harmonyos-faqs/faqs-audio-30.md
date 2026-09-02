---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-30
title: 音频声音大小不符合调节预期
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 音频声音大小不符合调节预期
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:043fc40086b2bea763c2822ff95f1fab3d44390f8d68ffe0df6a690a8879e279
---

## 问题现象

在音频播放场景，通过音量侧键调节大小无效。如将声音调节至最小，依旧有声音播放。

## 背景知识

* [音频管理](../harmonyos-references/js-apis-audio.md)：音频管理提供基础的音频控制能力，包括音量调节、设备管理、数据采集及渲染。
* [StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)：音频流使用类型的枚举。

  | 名称 | 值 | 说明 | 使用音量类型 |
  | --- | --- | --- | --- |
  | STREAM\_USAGE\_MUSIC | 1 | 音乐 | 媒体语音 |
  | STREAM\_USAGE\_VOICE\_ASSISTANT | 3 | 语音播报 | 小艺语音 |
* 音频常用日志：

  | 日志关键字 | 说明 |
  | --- | --- |
  | volume key event/volume : x | 音量调节事件/调节大小x |
  | adev\_set\_voice\_volume | 音频播放音量大小 |
  | StreamClientState.\*usage | 音频流类型 |

## 问题定位

查看日志StreamClientState.\*usage:，确认音频流类型。如果usage为3，音频流类型设置为语音播报(STREAM\_USAGE\_VOICE\_ASSISTANT)，而音量侧键调节的是媒体类型的音量（默认）。

```txt
[Create]StreamClientState for Renderer::Create. content: 0, usage: 3, flags: 0, uid: -1
[SetParams]StreamClientState for Renderer::SetParams.
```

## 分析结论

音频流类型被设置为语音播报，而音量侧键调节的是媒体类型，导致音量键调节音频声音无效。

## 修改建议

建议应用参考[播放音频流类型](../harmonyos-guides/using-right-streamusage-for-playback.md)修改usage为媒体类型。
