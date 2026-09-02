---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-20
title: 音频被收藏操作打断
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 音频被收藏操作打断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:066ff9db5debb72c495793cf7ef6e1de9a63f2393083f4c55f6dc011b763a000
---

## 问题现象

用户播放音频时，点击画面的收藏操作，音频会暂停播放。

## 背景知识

[AVPlayer.on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)：监听播放状态机AVPlayerState切换的事件。

## 问题定位

1. 查看Hilog日志关键字Click accepted，日志打印Click accepted,tag: Image，判断收藏图片做了Click事件消费。
2. 查看Hilog日志AVPlayer state，日志在收藏动作后紧接着打印AVPlayer state stopped called，判断音频在做收藏操作时候主动做了停止播放的逻辑。

   ```screen
   [(100000:100000:scope)] Click try accept
   [(100000:100000:scope)] Click accepted, tag: Image
   [(100000:100000:scope)] id: 0, log: {types: Click, node: Image, prcd: Down, state: READY, extraInfo: ETF: 0 CFP: 0, prcd: Up, state: SUCCEED, extraInfo: ETF: 0 CFP: 0}{types: Sequenced, node: Image, prcd: Down, state: READY, prcd: Up, state: FAIL}{types: LongPress, node: Image, prcd: Down, state: DETECTING, prcd: Up, state: FAIL}{types: Pan, node: Image}{types: LongPress, node: Image, prcd: Down, state: DETECTING, prcd: Up, state: FAIL}
   IC AVPlayer state playing called.
   #113 0xCD4D60 StopClick
   #167 0x893438 ClickThread End
   IC AVPlayer state stopped called.
   ```

## 分析结论

应用音频停止/暂停播放逻辑实现问题，在非停止/暂停播放场景调用了停止/暂停播放逻辑。

## 修改建议

修改业务逻辑，在执行收藏等非音频操作行为时，不要调用音频停止/暂停接口。
