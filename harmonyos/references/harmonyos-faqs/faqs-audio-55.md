---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-55
title: 录音的时候播放音乐，如何自动中断录音
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 录音的时候播放音乐，如何自动中断录音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d7de8dd062f83532c5589c12462c4b5c75b0c3c2ab2835918a962d0f1c234cd3
---

## 问题现象

录音的时候打开音乐软件播放音乐，不会中断录音，使用[on('audioInterrupt')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onaudiointerrupt10)接口也无法监听到打断事件，怎么实现暂停录音？

## 背景知识

[AudioCapturer](../harmonyos-guides/using-audiocapturer-for-recording.md)是音频采集器，用于录制PCM（Pulse Code Modulation）音频数据，适合有音频开发经验的开发者实现更灵活的录制功能。

[on('audioInterrupt')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onaudiointerrupt10)可监听音频中断事件（当音频焦点发生变化时触发）。

[AudioStreamManager](../harmonyos-guides/audio-playback-stream-management.md#读取或监听所有音频流的变化)可以读取或监听所有音频流的变化信息。

## 解决方案

播放流（如音乐）与录制流（如录音）是相互独立的，焦点变化无法监听到。可通过[on('audioRendererChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#onaudiorendererchange9)监听音频输出流变化，并使用[isStreamActive](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isstreamactive20)判断音频流处于活跃状态时，主动暂停录音，关键示例代码如下：

```ts
let audioManager = audio.getAudioManager();
let audioStreamManager = audioManager.getStreamManager();
audioStreamManager.on('audioRendererChange', (AudioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  for (let i = 0; i < AudioRendererChangeInfoArray.length; i++) {
    let AudioRendererChangeInfo = AudioRendererChangeInfoArray[i];
    console.info(`RendererChange on is called for ${i}`, JSON.stringify(AudioRendererChangeInfo.rendererInfo));
    try {
      let isStreamActive = audioStreamManager.isStreamActive(AudioRendererChangeInfo.rendererInfo.usage);
      console.info(`RendererChange IsStreamActive: ${isStreamActive}.`);
      if (isStreamActive) {
        console.info(`RendererChange IsStreamActive stop capturer`);
        stop();
      }
    } catch (err) {
      console.error(`RendererChange. code: ${err.code}, message: ${err.message}`);
    }
  }
});
```

全部示例代码如下：

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { PromptAction } from '@kit.ArkUI';

let audioCapturer: audio.AudioCapturer | undefined = undefined;
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
let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};
let file: fs.File;
let readDataCallback: Callback<ArrayBuffer>;
let promptAction: PromptAction;

@Entry
@Component
export struct CapturerStopDemo {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    promptAction = this.getUIContext().getPromptAction();
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.context, ['ohos.permission.MICROPHONE']);
  }

  build() {
    Column({ space: 20 }) {
      Button('初始化').width('100%')
        .onClick(async () => {
          initArguments(this.context);
          init();
        });

      Button('开始录制').width('100%')
        .onClick(async () => {
          start();
        });

      Button('停止录制').width('100%')
        .onClick(async () => {
          stop();
        });

      Button('释放资源').width('100%')
        .onClick(async () => {
          release();
        });
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .padding(20)
    .height('100%')
    .width('100%');
  }
}

async function initArguments(context: common.UIAbilityContext) {
  let bufferSize: number = 0;
  let path = context.cacheDir;
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  readDataCallback = (buffer: ArrayBuffer) => {
    let options: WriteOptions = {
      offset: bufferSize,
      length: buffer.byteLength
    };
    fs.writeSync(file.fd, buffer, options);
    bufferSize += buffer.byteLength;
  };
}

// 初始化，创建实例，设置监听事件。
async function init() {
  audio.createAudioCapturer(audioCapturerOptions, (err, capturer) => { // 创建AudioCapturer实例。
    if (err) {
      console.error(`Invoke createAudioCapturer failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`create AudioCapturer success`);
    audioCapturer = capturer;
    if (audioCapturer !== undefined) {
      try {
        audioCapturer.on('readData', readDataCallback);
      } catch (error) {
        console.error(`create AudioCapturer error`);
      }
    }
    promptAction.showToast({
      message: 'init success'
    });
  });

  let audioManager = audio.getAudioManager();
  let audioStreamManager = audioManager.getStreamManager();
  audioStreamManager.on('audioRendererChange', (AudioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
    for (let i = 0; i < AudioRendererChangeInfoArray.length; i++) {
      let AudioRendererChangeInfo = AudioRendererChangeInfoArray[i];
      console.info(`RendererChange on is called for ${i}`, JSON.stringify(AudioRendererChangeInfo.rendererInfo));
      try {
        let isStreamActive = audioStreamManager.isStreamActive(AudioRendererChangeInfo.rendererInfo.usage);
        console.info(`RendererChange IsStreamActive: ${isStreamActive}.`);
        if (isStreamActive) {
          console.info(`RendererChange IsStreamActive stop capturer`);
          stop();
        }
      } catch (err) {
        console.error(`RendererChange. code: ${err.code}, message: ${err.message}`);
      }
    }
  });
}

// 开始一次音频采集。
async function start() {
  if (audioCapturer !== undefined) {
    let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
    if (stateGroup.indexOf(audioCapturer.state.valueOf()) ===
      -1) { // 当且仅当状态为STATE_PREPARED、STATE_PAUSED和STATE_STOPPED之一时才能启动采集。
      console.error(`start failed`);
      return;
    }

    // 启动采集。
    audioCapturer.start((err: BusinessError) => {
      if (err) {
        console.error('Capturer start failed.');
      } else {
        console.info('Capturer start success.');
        promptAction.showToast({
          message: 'start success'
        });
      }
    });
  }
}

// 停止采集。
async function stop() {
  if (audioCapturer !== undefined) {
    // 只有采集器状态为STATE_RUNNING或STATE_PAUSED的时候才可以停止。
    if (audioCapturer.state.valueOf() !== audio.AudioState.STATE_RUNNING &&
      audioCapturer.state.valueOf() !== audio.AudioState.STATE_PAUSED) {
      console.info('Capturer is not running or paused');
      return;
    }

    // 停止采集。
    audioCapturer.stop((err: BusinessError) => {
      if (err) {
        console.error('Capturer stop failed.');
      } else {
        console.info('Capturer stop success.');
        promptAction.showToast({
          message: 'stop success'
        });
      }
    });
  }
}

// 销毁实例，释放资源。
async function release() {
  if (audioCapturer !== undefined) {
    // 采集器状态不是STATE_RELEASED或STATE_NEW状态，才能release。
    if (audioCapturer.state.valueOf() === audio.AudioState.STATE_RELEASED ||
      audioCapturer.state.valueOf() === audio.AudioState.STATE_NEW) {
      console.info('Capturer already released');
      return;
    }
    // 释放资源。
    audioCapturer.release((err: BusinessError) => {
      if (err) {
        console.error('Capturer release failed.');
      } else {
        fs.closeSync(file);
        console.info('Capturer release success.');
        promptAction.showToast({
          message: 'release success'
        });
      }
    });
  }
}
```
