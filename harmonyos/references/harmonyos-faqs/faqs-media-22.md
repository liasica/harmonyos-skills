---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-22
title: 节拍器节拍不均
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 节拍器节拍不均
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:65b63926ef8b90a48aa0a9b2efd00fabf81e2925d99c1e2eba5c1dd365ddf31e
---

## 问题现象

节拍播放器节拍不均。

## 背景知识

* [使用AVPlayer播放音频(ArkTS)](../harmonyos-guides/using-avplayer-for-playback.md)：使用AVPlayer可以实现端到端播放原始媒体资源。
* AVPlayer.[play](../harmonyos-references/arkts-apis-media-avplayer.md#play9)：开始播放音视频资源，只能在prepared/paused/completed状态调用。play是耗时接口。
* [使用AudioRenderer开发音频播放功能](../harmonyos-guides/using-audiorenderer-for-playback.md)：AudioRenderer是音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据，相比AVPlayer而言，可以在输入前添加数据预处理，更适合有音频开发经验的开发者，以实现更灵活的播放功能。AudioRenderer支持同时播放多个音频流。

## 问题定位

1. 查看播放器的实现方式，存在AVPlayer，确定为AVPlayer实现。如以下示例：

   ```screen
   import { BusinessError } from '@kit.BasicServicesKit';
   import { media } from '@kit.MediaKit';

   avPlayer.play().then(() => {
     console.info('Succeeded in playing');
   }, (err: BusinessError) => {
     console.error(`Failed to play,error message is: ${err.message}`);
   });
   ```
2. 查看节拍的实现逻辑，对于16节拍，每个节拍都使用一个AVPlayer做控制，AVPlayer.play是耗时接口，快速播放音效时，有一定的延迟，所以速度快的时候就会出现节拍不均的情况。

## 分析结论

应用使用多个AVPlayer轮流play播放节拍，AVPlayer.play是耗时接口，快速播放音效时，有一定的延迟，所以速度快的时候就会出现节拍不均的情况。

## 修改建议

采用AudioRenderer音频渲染器，对音频数据预处理，可避免AVPlayer接口耗时造成的延迟问题。可参考官网文档[使用AudioRenderer开发音频播放功能](../harmonyos-guides/using-audiorenderer-for-playback.md)中的示例。
