---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-47
title: AudioRenderer怎么播放PCM音频流
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioRenderer怎么播放PCM音频流
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:417bb61f4a7988f34e77fab1612ff0e6b72c99d69e50c73c924b5d54c4b18fd9
---

## 问题现象

AudioRenderer怎么直接播放PCM音频流，音频流可能是网络返回的，或者代码生成的，而不是PCM文件？

## 背景知识

[AudioRenderer](../harmonyos-guides/using-audiorenderer-for-playback.md)是音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据，相比AVPlayer而言，可以在输入前添加数据预处理，更适合有音频开发经验的开发者，以实现更灵活的播放功能。

## 解决方案

AudioRenderer可通过[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)监听音频数据写入回调事件，如下示例介绍直接播放音频数据流：

* 代码生成临时的PCM音频数据，并赋值给Uint8Array变量audioData中。
* AudioRenderer监听'writeData'回调，播放audioData音频流数据。

```ts
import { audio } from '@kit.AudioKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioRenderer: audio.AudioRenderer;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_8000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_1, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

@Entry
@Component
export struct PlayPcmDataDemo {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  audioData: Uint8Array = generateTestPCM(); // 测试PCM数据，按需替换为其他音频数据源
  writeOffset = 0;

  async aboutToAppear(): Promise<void> {
    audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
    await this.init(); //初始化
  }

  async aboutToDisappear(): Promise<void> {
    await audioRenderer.release();
  }

  build() {
    Column({ space: 10 }) {
      Button('播放音频数据')
        .width('100%')
        .onClick(async () => {
          await audioRenderer.start();
        });
      Button('停止播放')
        .width('100%')
        .onClick(async () => {
          console.info('renderer status' + audioRenderer.state);
          this.stopAndFlush();
        });
    }
    .padding(20)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }

  async init() {
    audioRenderer.on('writeData', (buffer: ArrayBuffer) => {
      if (!this.audioData) {
        return audio.AudioDataCallbackResult.INVALID;
      }
      let bufferView = new Uint8Array(buffer);
      let writeLen = Math.min(buffer.byteLength, this.audioData.byteLength - this.writeOffset);
      if (writeLen <= 0) {
        this.writeOffset = 0;
        console.info('Play Done');
        return audio.AudioDataCallbackResult.INVALID;
      }
      bufferView.set(this.audioData.slice(this.writeOffset, this.writeOffset + writeLen));
      this.writeOffset += writeLen;
      return audio.AudioDataCallbackResult.VALID;
    });
  }

  async stopAndFlush() {
    console.info('renderer status' + audioRenderer.state);
    audioRenderer.stop().then(() => {
      console.error('Renderer stop ok.');
    }).catch((err: BusinessError) => {
      console.error('Renderer stop failed. ', err);
    })
    ;
    audioRenderer.flush().then(() => {
      console.error('Renderer flush ok.');
    }).catch((err: BusinessError) => {
      console.error('renderer flush err. ' + err);
    });
    this.writeOffset = 0;
  }
}

function generateTestPCM(): Uint8Array {
  const sampleRate = 8000;
  const noteDuration = 0.5;
  const amplitude = 0.35;

  const freqMap: Record<number, number> = {
    1: 523.25, // C5
    2: 587.33, // D5
    3: 659.25, // E5
    4: 698.46, // F5
    5: 783.99, // G5
    6: 880.00  // A5
  };

  const melody = [
    1, 1, 5, 5, 6, 6, 5, 0,
    4, 4, 3, 3, 2, 2, 1, 0,
    5, 5, 4, 4, 3, 3, 2, 0
  ];

  const samplesPerNote = Math.floor(sampleRate * noteDuration); // 4000
  const totalSamples = samplesPerNote * melody.length; // 96,000
  const buffer = new ArrayBuffer(totalSamples * 2); // 192,000 bytes
  const view = new DataView(buffer);

  let idx = 0;
  for (const note of melody) {
    const freq = note ? freqMap[note] : 0;
    for (let i = 0; i < samplesPerNote; i++) {
      const t = i / sampleRate;
      const wave = freq ? amplitude * Math.sin(2 * Math.PI * freq * t) : 0;
      const sample = Math.round(wave * 32767);
      const clamped = Math.max(-32768, Math.min(32767, sample));
      view.setInt16(idx * 2, clamped, true);
      idx++;
    }
  }
  return new Uint8Array(buffer);
}
```
