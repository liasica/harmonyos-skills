---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-33
title: 播放视频，摘下耳机后暂停播放，佩戴上以后未恢复播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 播放视频，摘下耳机后暂停播放，佩戴上以后未恢复播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:05fe40ae5cb0185fa4bfbe567929f56e9bf87a206db6b0c189b5b8fd1ce96fa8
---

## 问题现象

播放视频，耳机断开连接后暂停播放，耳机再次连接后未恢复播放。

## 背景知识

1. [AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)：提供音频输入输出设备管理能力，包括查询输入输出设备信息、监听设备连接状态变化等。
2. [on('deviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#ondevicechange9)：监听音频设备连接状态变化事件（当音频设备连接状态发生变化时触发）。使用callback异步回调。回调返回的参数有设备连接状态变化[DeviceChangeType](../harmonyos-references/arkts-apis-audio-e.md#devicechangetype)和设备信息[AudioDeviceDescriptors](../harmonyos-references/arkts-apis-audio-t.md#audiodevicedescriptors)。设备连接状态变化DeviceChangeType有以下两种状态：

   | 名称 | 值 | 说明 |
   | --- | --- | --- |
   | CONNECT | 0 | 设备连接 |
   | DISCONNECT | 1 | 断开设备连接 |

## 问题定位

1. 检查是否有音频设备连接状态发生变化的监听。
2. 如果有监听，检查在监听函数里是否有再次连接后开启播放的逻辑。

## 分析结论

未增加音频设备连接状态的监听函数或无再次连接时播放视频的逻辑，导致耳机再次连接时无法继续播放。

## 修改建议

添加音频设备连接状态发生变化的监听，在监听里完成再次连接后开启播放的逻辑。

```screen
import audio from '@ohos.multimedia.audio';

@Entry
@Component
struct AudioConnectPlayExample {
  private controller: VideoController = new VideoController();
  private videoSrc: string = 'https://xxxxxxxxxx.mp4'; // 具体的视频地址
  private audioManager = audio.getAudioManager();
  private isPlay = false;

  aboutToAppear(): void {
    let audioRoutingManager = this.audioManager.getRoutingManager();
    // 注册音频输出设备改变状态事件
    audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT_DEVICES_FLAG,
      (deviceChanged: audio.DeviceChangeAction) => {
        // 设备连接状态变化，0为连接，1为断开连接
        if (deviceChanged.type === 1 && this.isPlay) {
          this.controller.pause();
        } else if (deviceChanged.type === 0 && !this.isPlay) {
          this.controller.start();
        }
      });
  }

  aboutToDisappear(): void {
    let audioRoutingManager = this.audioManager.getRoutingManager();
    // 注销音频输出设备改变状态事件
    audioRoutingManager.off('deviceChange');
  }

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        controller: this.controller
      })
        .onStart(() => {
          this.isPlay = true;
        })
        .onPause(() => {
          this.isPlay = false;
        })
    }
  }
}
```
