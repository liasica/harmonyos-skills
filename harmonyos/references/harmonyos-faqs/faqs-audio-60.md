---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-60
title: 通过监听距离来实现音频播放设备在扬声器和听筒之间切换
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 通过监听距离来实现音频播放设备在扬声器和听筒之间切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4339f2ce56770726104008d0d8c492621fdf9c9a7e8cab7e4fafb4f93313ac20
---

## 问题现象

IM类软件聊天会话中发送或接收的语音类型消息（是短消息不是语音通话），在播放过程中通过监听距离传感器来切换听筒和扬声器播放。语音播放使用AVPlayer，如何实现；

## 背景知识

* [sensor模块](../harmonyos-references/js-apis-sensor.md)：设备传感器模块，可用于订阅设备传感器信息，如重力传感器、计步器等，其中[接近光传感器](../harmonyos-references/js-apis-sensor.md#sensoronsensoridproximity9)可用于监测设备前置相机距离障碍物的距离变化。
* 管理全局音频输出设备:从API 20开始，AudioSessionManager提供了部分输出设备管理的接口，支持通过[AudioSession管理全局音频输出](../harmonyos-guides/audio-output-device-management.md#通过audiosession查询和监听音频输出设备)，方便在使用AudioSession管理音频焦点的同时管理音频输出。
* [setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)：设置默认发声设备。仅适用于[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为语音消息、VoIP语音通话或者VoIP视频通话的场景，支持听筒、扬声器和系统默认设备，使用前需要调用[activateAudioSession](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#activateaudiosession12)激活。

## 解决方案

1. 设置管理全局音频输出设备的接口：

   ```ts
   let audioManager = audio.getAudioManager(); // 需要先创建AudioManager实例。
   let audioSessionManager = audioManager.getSessionManager(); // 再调用AudioManager的方法创建AudioSessionManager实例。
   let strategy: audio.AudioSessionStrategy = {
     concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_PAUSE_OTHERS
   };
   ```
2. 设置传感器接口，当设备贴近耳朵时，将全局播放设备切换为听筒，当设备远离时，全局播放设备切换为扬声器：

   ```ts
   sensor.on(sensor.SensorId.PROXIMITY, (response) => {
     if (response.distance === 0) {
       this.sessionIsSpeaker = false;
       audioSessionManager.setDefaultOutputDevice(audio.DeviceType.EARPIECE)
         .then(() => {
           console.info('AudioSession Succeeded in setting default EARPIECE device.');
         }).catch((err: BusinessError) => {
         console.error(`AudioSession setDefaultOutputDevice Fail: ${err}`);
       });
     } else if (response.distance === 5) {
       this.sessionIsSpeaker = true;
       audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER)
         .then(() => {
           console.info('AudioSession Succeeded in setting SPEAKER output device.');
         }).catch((err: BusinessError) => {
         console.error(`AudioSession setDefaultOutputDevice Fail: ${err}`);
       });
     }
   }, { interval: 1000000000 }); //采样周期1000000000ns，即1s
   ```

完整示例如下：

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { sensor } from '@kit.SensorServiceKit';
import { common } from '@kit.AbilityKit';
import { media } from '@kit.MediaKit';

let audioManager = audio.getAudioManager(); // 需要先创建AudioManager实例。
let audioSessionManager = audioManager.getSessionManager(); // 再调用AudioManager的方法创建AudioSessionManager实例。
let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_PAUSE_OTHERS
};

// 请用户切换为自己的播放逻辑，此处仅做模拟演示。
class AvPlayer {
  static avPlayer: media.AVPlayer | undefined;

  static async initAvplayer() {
    AvPlayer.avPlayer = await media.createAVPlayer();
    AvPlayer.avPlayer.on('stateChange', (state) => {
      if (!AvPlayer.avPlayer) {
        return;
      }
      switch (state) {
        case 'idle':
          console.info('触发了播放器idle状态');
          break;
        case 'initialized':
          AvPlayer.avPlayer.audioRendererInfo = {
            usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
            rendererFlags: 0
          };
          console.info('触发了播放器initialized状态');
          AvPlayer.avPlayer.prepare();
          break;
        case 'prepared':
          console.info('触发了播放器prepared状态');
          AvPlayer.avPlayer.play();
          break;
        case 'completed':
          console.info('触发了播放器completed状态');
          break;
      }
    });
  }

  static async playMusic(url: media.AVFileDescriptor) {
    if (!AvPlayer.avPlayer) {
      return;
    }
    AvPlayer.avPlayer.fdSrc = url;
  }
}

@Entry
@ComponentV2
struct Index {
  @Local sessionIsSpeaker: boolean = true;

  aboutToAppear(): void {
    AvPlayer.initAvplayer();
    audioSessionManager.activateAudioSession(strategy);
    try {
      sensor.on(sensor.SensorId.PROXIMITY, (response) => {
        if (response.distance === 0) {
          this.sessionIsSpeaker = false;
          audioSessionManager.setDefaultOutputDevice(audio.DeviceType.EARPIECE)
            .then(() => {
              console.info('AudioSession Succeeded in setting default EARPIECE device.');
            }).catch((err: BusinessError) => {
            console.error(`AudioSession setDefaultOutputDevice Fail: ${err}`);
          });
        } else if (response.distance === 5) {
          this.sessionIsSpeaker = true;
          audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER)
            .then(() => {
              console.info('AudioSession Succeeded in setting SPEAKER output device.');
            }).catch((err: BusinessError) => {
            console.error(`AudioSession setDefaultOutputDevice Fail: ${err}`);
          });
        }
      }, { interval: 1000000000 }); //采样周期1000000000ns，即1s
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
    }
  }

  aboutToDisappear(): void {
    try {
      sensor.off(sensor.SensorId.PROXIMITY, () => {
        console.info('Succeeded in invoking off. Distance');
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Failed to invoke off. Code: ${e.code}, message: ${e.message}`);
    }
  }

  build() {
    Column({ space: 10 }) {
      Button('播放音乐')
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          // 请用户切换为自己的播放资源
          let fileDescriptor = await context.resourceManager.getRawFd('test.mp3');
          let avFileDescriptor: media.AVFileDescriptor =
            { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };
          AvPlayer.playMusic(avFileDescriptor);
        });
      Row() {
        Text(this.sessionIsSpeaker ? 'Speaker' : 'Ear');
      };
    }.width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
