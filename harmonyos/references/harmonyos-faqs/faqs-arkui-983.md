---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-983
title: 智能表结合ArcButton实现调节系统音量
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 智能表结合ArcButton实现调节系统音量
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:99d6fb1d00e21833c10e4a7c22d7ab69aa0873d5d22417638057dc7c569093bc
---

## 问题现象

智能表为圆形屏幕的穿戴设备，如何在页面显示弧形按钮，并通过页面按钮实现调节智能表的系统音量？

## 背景知识

* [ArcButton](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbutton-1)：弧形按钮组件用于圆形屏幕的穿戴设备，提供强调、普通、警告等样式按钮。
* [AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md#avvolumepanel)：应用无法直接调节系统音量，可以通过系统音量面板，让用户通过界面操作来调节音量。

## 解决方案

1. 页面初始化时，通过[getVolumeByStream](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)获取指定音频流（以音乐为例）的音量并赋值。
2. 通过[ArcButton](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbutton-1)实现两个调节音量按钮，分别显示在页面顶部和底部，点击事件中改变音量值，并通过监听音量变化获取当前音量值进行弹窗提示。
3. 通过[AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md#avvolumepanel)组件实现调节系统音量，该组件在智能表上无UI显示。

完整代码示例如下：

```screen
import { BusinessError } from '@kit.BasicServicesKit';
import { audio, AVVolumePanel } from '@kit.AudioKit';
import {
  LengthMetrics,
  LengthUnit,
  ArcButton,
  ArcButtonOptions,
  ArcButtonStatus,
  ArcButtonStyleMode,
  ArcButtonPosition,
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local topOptions: ArcButtonOptions = new ArcButtonOptions({});
  @Local bottomOptions: ArcButtonOptions = new ArcButtonOptions({});
  @Local volume: number = 0;

  initVolume() {
    try {
      this.volume = audio.getAudioManager().getVolumeManager().getVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to obtains the volume of a stream, error: ${error}`);
    }
  }

  aboutToAppear(): void {
    this.initVolume();

    this.topOptions = new ArcButtonOptions({
      label: '调高音量',
      status: ArcButtonStatus.NORMAL,
      position: ArcButtonPosition.TOP_EDGE,
      styleMode: ArcButtonStyleMode.NORMAL_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      onClick: () => {
        if (this.volume < 15) {
          this.volume++;
        }
        let audioManager = audio.getAudioManager();
        let audioVolumeManager = audioManager.getVolumeManager();
        try {
          audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC,
            (streamVolumeEvent: audio.StreamVolumeEvent) => {
              console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
              console.info(`Volume level: ${streamVolumeEvent.volume} `);
              this.getUIContext().getPromptAction().showToast({
                message: `当前音量为：${streamVolumeEvent.volume}`,
                duration: 2000
              });
            });
        } catch (error) {
          console.error(`Failed to listen for stream volume change events, error: ${error}`);
        }
      }
    });

    this.bottomOptions = new ArcButtonOptions({
      label: '调低音量',
      styleMode: ArcButtonStyleMode.NORMAL_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      onClick: () => {
        if (this.volume > 0) {
          this.volume--;
        }
        let audioManager = audio.getAudioManager();
        let audioVolumeManager = audioManager.getVolumeManager();
        try {
          audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC,
            (streamVolumeEvent: audio.StreamVolumeEvent) => {
              console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
              console.info(`Volume level: ${streamVolumeEvent.volume} `);
              this.getUIContext().getPromptAction().showToast({
                message: `当前音量为：${streamVolumeEvent.volume}`,
                duration: 2000
              });
            });
        } catch (error) {
          console.error(`Failed to listen for stream volume change events, error: ${error}`);
        }
      }
    });
  }

  build() {
    Stack() {
      AVVolumePanel({
        volumeLevel: this.volume,
        volumeParameter: {
          position: {
            x: 0,
            y: 0
          }
        }
      }).width('100%').height('100%');

      Column() {
        ArcButton({ options: this.topOptions });
        Blank();
        ArcButton({ options: this.bottomOptions });
      }.width('100%').height('100%');

    }.width(233).height(233);
  }
}
```
