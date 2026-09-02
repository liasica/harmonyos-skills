---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-66
title: 如何判断麦克风正在录音
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何判断麦克风正在录音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c965c805314a391dbbf11e010247378603e261a93702a0cbb5c681783fdf3687
---

## 问题现象

怎么判断设备正在录音，麦克风正在被占用？涉及隐私或敏感的业务场景需要此状态提示用户。

## 背景知识

[getCurrentAudioCapturerInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiocapturerinfoarray9)获取当前音频采集器的信息。

[getMaxAmplitudeForInputDevice](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#getmaxamplitudeforinputdevice12)获取输入设备音频流的最大电平值，取值范围为[0,1]。

[isMicrophoneMute](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#ismicrophonemute9-1)获取麦克风静音状态。

## 解决方案

1. 通过AudioStreamManager音频流管理的[getCurrentAudioCapturerInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiocapturerinfoarray9)接口获取当前音频采集器的信息。
2. 遍历获取到的音频采集器的信息，调用[getMaxAmplitudeForInputDevice](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#getmaxamplitudeforinputdevice12)接口获取每个采集器音频流的最大电平值，当电平值大于0，说明设备采集到声音，设备正在录音。

示例代码如下：

```ts
import { audio } from '@kit.AudioKit';

const audioManager = audio.getAudioManager();
const audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
const audioStreamManager = audioManager.getStreamManager();

@Entry
@Component
export struct AudioRecordingCheckDemo {
  @State isRecording: boolean = false;
  intervalID = -1;

  aboutToDisappear(): void {
    if (this.intervalID > -1) {
      clearInterval(this.intervalID);
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('检查设备是否正在录音')
        .onClick(async () => {
          this.intervalID = setInterval(async () => {
            this.isRecording = await this.checkMicIsRecording();
          }, 500);
        });
      Text(`设备是否正在录音：${this.isRecording}`);
    }
    .justifyContent(FlexAlign.Center)
    .padding(30)
    .height('100%')
    .width('100%');
  }

  //获取麦克风是否在录音
  async checkMicIsRecording(): Promise<boolean> {
    try {
      const audioVolumeGroupManager: audio.AudioVolumeGroupManager =
        await audioVolumeManager.getVolumeGroupManager(audio.DEFAULT_VOLUME_GROUP_ID);
      let array = await audioStreamManager.getCurrentAudioCapturerInfoArray();
      console.info(`checkCapturerChanges size: ${array.length}`); //存在录音流不一定正在录音
      for (let changeInfo of array) {
        for (let deviceDescriptor of changeInfo.deviceDescriptors) {
          let maxAmplitude = await audioVolumeGroupManager.getMaxAmplitudeForInputDevice(deviceDescriptor);
          if (maxAmplitude > 0) { //录音设备电平值大于0，说明录音设备采集到声音
            console.warn(`checkCapturerChanges true maxAmplitude:${maxAmplitude} deviceType:${deviceDescriptor.deviceType}}`);
            return true;
          }
        }
      }
    } catch (err) {
      console.error(`checkCapturerChanges error:${JSON.stringify(err)}`);
      throw new Error(`checkCapturerChanges error:${JSON.stringify(err)}`);
    }
    return false;
  }
}
```
