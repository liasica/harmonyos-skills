---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-52
title: Slider组件调节系统音量
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > Slider组件调节系统音量
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:43fd50e17ce0982a8f0b7c2a473f8152440a719cd00c4ebb646c5f7011f0c547
---

## 问题现象

自定义[Slider](../harmonyos-references/ts-basic-components-slider.md)组件如何调节系统音量，同时系统音量调节如何同步到Slider组件？

## 背景知识

[Slider](../harmonyos-references/ts-basic-components-slider.md)滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。[音量面板AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)提供展示和调节系统音量的统一面板。[on('streamVolumeChange')](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#onstreamvolumechange20)监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。

## 解决方案

Slider组件可以通过音量面板AVVolumePanel调节系统音量，同时可以通过on('streamVolumeChange')监听系统音量变化同步给Slider组件。示例代码如下：

```ts
import { audio, AVVolumePanel } from '@kit.AudioKit';

let streamUsage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_MUSIC;
let audioManager = audio.getAudioManager();
let audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
let volumeMin: number = audioVolumeManager.getMinVolumeByStream(streamUsage);
let volumeMax: number = audioVolumeManager.getMaxVolumeByStream(streamUsage);
const tag = '[SliderVolumeDemo]';

@Entry
@Component
export struct SliderVolumeDemo {
  @State volumeLevel: number = 0; // 音量值和滑块值使用同一个变量

  aboutToAppear(): void {
    console.info(`${tag} volume min:${volumeMin} max:${volumeMax}`);

    this.volumeLevel = audioVolumeManager.getVolumeByStream(streamUsage);
    // 监听音量变化，同时改变滑块值
    audioVolumeManager.on('streamVolumeChange', streamUsage, (streamVolumeEvent: audio.StreamVolumeEvent) => {
      console.info(`${tag} volumeLevel:${streamVolumeEvent.volume}`);
      this.volumeLevel = streamVolumeEvent.volume;
    });

  }

  build() {
    Column({ space: 8 }) {
      Row() {
        Slider({
          value: $$this.volumeLevel,
          min: volumeMin,
          max: volumeMax,
          style: SliderStyle.OutSet
        })
          .showTips(true);
      }
      .width('100%');

      Row() {
        // 音量面板
        AVVolumePanel({
          volumeLevel: this.volumeLevel,
          volumeParameter: {
            position: {
              x: 1100, // 音量面板位置，当不需要显示面板时，position的x，y值可设置负数
              y: 300
            }
          }
        });
      }
      .width('100%');
    }
    .padding(20)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
