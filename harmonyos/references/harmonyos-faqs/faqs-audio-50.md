---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-50
title: 如何调节系统音量
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何调节系统音量
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:b66d243ed32323fc5bc4d3d3a63a498fe1be3d609075f44e481163b215e37fa7
---

## 问题现象

有没有API可以调节系统媒体音量大小，[AudioManager.setVolume](../harmonyos-references/arkts-apis-audio-audiomanager.md#setvolumedeprecated)接口已废弃，如何调节系统音量？

## 背景知识

[AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)提供创建音量面板AVVolumePanel的功能，提供展示和调节系统音量的统一面板。

[AudioManager.setVolume](../harmonyos-references/arkts-apis-audio-audiomanager.md#setvolumedeprecated)接口已废弃，替代接口仅面向系统应用开放。

## 解决方案

应用无法直接调节系统音量，可以通过系统音量面板[AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)组件，让用户通过界面操作来调节音量。

注意事项：

* 应用如果希望自定义音量条，隐藏系统音量面板，可设置[AVVolumePanelParameter](../harmonyos-references/ohos-multimedia-avvolumepanel.md#avvolumepanelparameter)的position的x或y坐标值为负数。
* 调节系统音量时请设置合理大小，否则可能设置无效，可通过[getMinVolumeByStream](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#getminvolumebystream20)获取指定音频流的最小音量，通过[getMaxVolumeByStream](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#getmaxvolumebystream20)获取指定音频流的最大音量，通过[getVolumeByStream](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)获取指定音频流的当前音量。
* 应用如果希望进入页面后，设置默认音量值，可以在进入页面，延迟一定时间（例如1秒）等待页面渲染完成后，再通过音量面板AVVolumePanel修改音量值，否则可能会设置音量无效。

使用示例代码如下：

```ts
import { audio, AVVolumePanel } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioVolumeManager = audioManager.getVolumeManager();
let streamUsage = audio.StreamUsage.STREAM_USAGE_MUSIC;

@Entry
@Component
export struct AVVolumePanelDemo {
  @State volume: number = audioVolumeManager.getVolumeByStream(streamUsage); // 获取当前音量值
  volumeMin: number = audioVolumeManager.getMinVolumeByStream(streamUsage); // 获取最小音量值
  volumeMax: number = audioVolumeManager.getMaxVolumeByStream(streamUsage); // 获取最大音量值
  @State positionX: number = 1100;

  aboutToAppear(): void {
    // 监听音量变化
    audioVolumeManager.on('streamVolumeChange', streamUsage, (streamVolumeEvent: audio.StreamVolumeEvent) => {
      this.volume = streamVolumeEvent.volume;
    });
  }

  onDidBuild() {
    // 进入页面渲染延迟1秒设置默认音量值
    setTimeout(() => {
      this.volume = 6;
    }, 1000);
  }

  build() {
    Column({ space: 20 }) {
      Row() {
        Text('显示音量调节面板面板:');
        Toggle({ type: ToggleType.Switch, isOn: true })
          .onChange((isOn: boolean) => {
            this.positionX = isOn ? 1100 : -1; // 坐标值，正值显示在屏幕内，负值显示在屏幕外
          });
      };

      Row({ space: 20 }) {
        Button('-')
          .onClick(() => {
            if (this.volume > this.volumeMin) {
              this.volume--;
            }
          });
        Button('+')
          .onClick(() => {
            if (this.volume < this.volumeMax) {
              this.volume++;
            }
          });
      }.width('100%');

      Text(`当前音量值：${this.volume}`);

      AVVolumePanel({
        volumeLevel: this.volume,
        volumeParameter: {
          position: {
            x: this.positionX,
            y: 200
          }
        }
      })
        .height(1);
    }
    .padding(20)
    .alignItems(HorizontalAlign.Start)
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：三方应用能否在后台控制系统音量？

A：安全规格不允许三方应用在后台控制系统音量，应用需在前台通过[AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)组件让用户通过界面操作调节音量。
