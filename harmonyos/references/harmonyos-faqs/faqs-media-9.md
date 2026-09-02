---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-9
title: 点击音频播放按钮，音频未播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 点击音频播放按钮，音频未播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8db77e5f977f0dd961490956587a067bbd4f94225fef1c6eb4eb0ccf2a1fb631
---

## 问题现象

点击播放音频的组件，点击后未播放音频。

## 背景知识

* [SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md)提供了短音频的加载、播放、音量设置、循环设置、停止播放、资源卸载等功能。
* [unload](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#unload)方法用来卸载音频已经加载的音频。

## 问题定位

1. 在hilog日志中查找关键字“SoundPool::Play”，找到问题发生时间播放的音频ID。

   记录下音频的ID和播放的时间。

   ```txt
   04-29 18:02:32.140 SoundPool::Play soundID::74,priority:0
   ```
2. 再在日志中查找关键字“SoundPool::Unload soundID::音频ID”，查看音频unload的时间。

   ```txt
   04-29 18:02:30.235 SoundPool::Unload soundID::74
   ```

## 分析结论

若音频unload的时间早于音频播放的时间，说明应用在音频播放完成前卸载了音频，导致未播放音频。

## 修改建议

监听SoundPool的[on('playFinished')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onplayfinished)的事件，在回调函数中对音频进行unload。

```ts
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('create & listen')
        .onClick(() => createSoundPoolAndListen());
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}

let soundPool: media.SoundPool;
let soundId: number = -1;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
};

function createSoundPoolAndListen() {
  media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
    if (error) {
      console.error(`Failed to createSoundPool`);
      return;
    } else {
      soundPool = soundPool_;
      console.info(`Succeeded in createSoundPool`);
      soundPool.on('playFinished', () => {
        console.info('Succeeded in playFinished');
        // 在此处执行音频unload方法
        if (soundId !== -1) {
          soundPool.unload(soundId);
        }
        soundPool.off('playFinished');
        console.info('audio unloaded');
      });
    }
  });
}
```
