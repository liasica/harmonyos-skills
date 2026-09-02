---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-16
title: 无线投屏时不能切换声音输出
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 无线投屏时不能切换声音输出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6cc6d6dad4280927634e9a87f060791d4909e1be6c9a4e0a5c581779741da4bd
---

## 问题现象

在使用系统无线投屏时，部分音频流无法投屏。

## 背景知识

* [音频流](../harmonyos-guides/audio-kit-intro.md#音频流介绍)类型是定义音频数据播放和录制方式的关键属性。对于播放流，其类型由StreamUsage确定；为了确保音频行为符合预期并提供优质的用户体验，应用开发者应根据具体业务场景和实际需求，为音频选择恰当的流类型。
* 无线投屏：HarmonyOS 的无线投屏功能为系统级能力，支持将手机、平板等终端设备的完整屏幕画面，通过无线方式实时投射至智慧屏、投影仪等显示设备，实现全域画面共享与跨设备协同。该功能区别于应用内投播，不局限于特定应用内容，具备更高的通用性与系统集成度。

## 问题定位

使用正则表达式搜索：audio\_server.\*usage:，查看应用使用的音频流类型。

```txt
01-29 15:49:35.406   810   985 W C02B8B/audio_server/AudioPolicyService: [GetPreferredOutputDeviceDescInner]Invalid usage[0], return current device.
```

可见，应用的音频流类型：streamUsage:0，进一步查看[音频流使用类型的枚举](../harmonyos-references/arkts-apis-audio-e.md#streamusage)。根据枚举类型查阅，STREAM\_USAGE\_UNKNOWN的值是0，属于未知类型的音频流。可见应用使用的音频流类型为未知类型。

## 分析结论

应用使用了未知类型的音频流，投屏场景下，未知类型的音频流无法选择分布式设备播放，只能选择默认的扬声器设备。

## 修改建议

建议应用根据业务场景选用合适的音频流类型，目前在分布式设备上投播可支持的常见音频流类型包括：STREAM\_USAGE\_MOVIE、STREAM\_USAGE\_AUDIOBOOK、STREAM\_USAGE\_GAME、STREAM\_USAGE\_MUSIC、STREAM\_USAGE\_NAVIGATION、STREAM\_USAGE\_ACCESSIBILITY、STREAM\_USAGE\_VOICE\_ASSISTANT。
