---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-61
title: AudioCapturer如何录制音频数据流，而不是文件
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioCapturer如何录制音频数据流，而不是文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3da47615047b9333fd85d7af745810e53a9831bd101d5fcfea01fe47b6fd24e0
---

## 问题现象

怎么采集录音数据流，如何避免不断的写入文件，浪费性能？

## 背景知识

[AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)是音频采集器，用于录制PCM（Pulse Code Modulation）音频数据。调用前需要申请麦克风权限ohos.permission.MICROPHONE，申请方式参考：[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。

## 解决方案

1. 定义[Queue](../harmonyos-references/js-apis-queue.md)队列用于缓存音频数据。
2. 通过[AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)录音时，在回调函数[on('readData')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onreaddata11)中不断的将音频数据存入队列。
3. 在需要使用音频数据的时候，从队列中读取数据。

示例代码如下：

```ts
import { audio } from '@kit.AudioKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { Queue } from '@kit.ArkTS';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};

@Entry
@Component
export struct AudioCapturerDataDemo {
  atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  capturerDemo = new CapturerDemo(this.context, audioStreamInfo, audioCapturerInfo);

  async aboutToAppear(): Promise<void> {
    await this.atManager.requestPermissionsFromUser(this.context, ['ohos.permission.MICROPHONE']); //权限申请
  }

  async aboutToDisappear(): Promise<void> {
    await this.capturerDemo.stop();
    await this.capturerDemo.release();
  }

  build() {
    Column({ space: 20 }) {
      Button('录制start').width('100%')
        .onClick(async () => {
          await this.capturerDemo.init();
          await this.capturerDemo.start();
        });

      Button('录制stop').width('100%')
        .onClick(async () => {
          await this.capturerDemo.stop();
          await this.capturerDemo.release();
        });
    }
    .justifyContent(FlexAlign.Center)
    .padding(30)
    .height('100%')
    .width('100%');
  }
}

class CapturerDemo {
  audioStreamInfo: audio.AudioStreamInfo;
  audioCapturerInfo: audio.AudioCapturerInfo;
  context: common.UIAbilityContext;
  bufferQueue = new Queue<ArrayBuffer>();
  audioCapturer?: audio.AudioCapturer;

  constructor(context: common.UIAbilityContext, audioStreamInfo: audio.AudioStreamInfo,
    audioCapturerInfo: audio.AudioCapturerInfo) {
    this.context = context;
    this.audioStreamInfo = audioStreamInfo;
    this.audioCapturerInfo = audioCapturerInfo;
  }

  // 初始化
  async init() {
    let audioCapturerOptions: audio.AudioCapturerOptions = {
      streamInfo: this.audioStreamInfo,
      capturerInfo: this.audioCapturerInfo
    };
    try {
      this.audioCapturer = await audio.createAudioCapturer(audioCapturerOptions); // 创建AudioCapturer实例。
      console.info(`createAudioCapturer success`);
      this.audioCapturer.on('readData', (buffer: ArrayBuffer) => {
        this.bufferQueue.add(buffer.slice(0)); //录音数据入队列
      });
    } catch (err) {
      console.error(`createAudioCapturer failed, code is ${err.code}, message is ${err.message}`);
    }
  }

  // 开始一次音频采集。
  async start() {
    try {
      this.bufferQueue = new Queue<ArrayBuffer>();
      await this.audioCapturer?.start();
      console.info(`start success`);
    } catch (err) {
      console.error(`Capturer start failed. ${JSON.stringify(err)}`);
    }
  }

  // 停止采集。
  async stop() {
    try {
      await this.audioCapturer?.stop();
      this.handleAudioData(); //根据业务，处理音频数据
      console.info(`stop success`);
    } catch (err) {
      console.error(`Capturer stop failed. ${JSON.stringify(err)}`);
    }
  }

  // 销毁实例，释放资源。
  async release() {
    try {
      await this.audioCapturer?.release();
      console.info(`release success`);
    } catch (err) {
      console.error(`Capturer release failed. ${JSON.stringify(err)}`);
    }
  }

  handleAudioData() {
    // 以下示例将bufferQueue数据保存到文件，根据业务需要调整
    let filePath = this.context.cacheDir + '/StarWars10s-2C-48000-4SW.pcm';
    let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    let offset = 0;
    for (let buff of this.bufferQueue) {
      fs.writeSync(file.fd, buff, {
        offset: offset,
        length: buff.byteLength
      });
      offset += buff.byteLength;
    }
    fs.close(file);
  }
}
```
