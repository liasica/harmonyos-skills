---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-56
title: AudioRenderer怎么判断音频播放结束
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioRenderer怎么判断音频播放结束
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:af9616a292c6bc7258abf4a73deb70ec955faa93851208872d81e901047e63b2
---

## 问题现象

AudioRenderer组件在播放PCM音频时如何监听到音频文件播放结束？

## 背景知识

[AudioRenderer](../harmonyos-guides/using-audiorenderer-for-playback.md)是音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据，相比AVPlayer而言，可以在输入前添加数据预处理，更适合有音频开发经验的开发者，以实现更灵活的播放功能。

[getAudioTimestampInfo](../harmonyos-references/arkts-apis-audio-audiorenderer.md#getaudiotimestampinfo19)获取输出音频流时间戳和位置信息。

## 解决方案

AudioRenderer通过回调[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)方法不停的写入音频数据播放，未提供播放结束的API。开发者可通过如下方式判断音频播放是否结束：

1. 定义一个定时器[setInterval](../atomic-ascf/apis-timer.md#setinterval)，每隔250ms调用getAudioTimestampInfo获取播放的音频流时间戳，并记录时间戳值preTimestamp。
2. 当最新的时间戳值和上次获取的时间戳值preTimestamp相等，表示音频渲染结束，否则继续定时轮询。

示例代码如下：

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
export struct PlayPcmEndDemo {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  audioData: Uint8Array = generateTestPCM(); // 测试PCM数据，按需替换为其他音频数据源
  writeOffset = 0;
  preTimestamp = 0;
  intervalId = 0;
  @State isEnd: boolean = false;

  async aboutToAppear(): Promise<void> {
    audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
    await this.init(); //初始化
  }

  async aboutToDisappear(): Promise<void> {
    await audioRenderer.release();
  }

  build() {
    Column({ space: 20 }) {
      Button('播放音频数据').width('100%')
        .onClick(async () => {
          this.writeOffset = 0;
          this.preTimestamp = 0;
          this.isEnd = false;
          await audioRenderer.start();

          this.checkPlayEnd(); //定时获取音频流时间戳，当时间戳不变时，播放结束
        });
      Button('停止播放').width('100%')
        .onClick(async () => {
          clearInterval(this.intervalId);
          this.stopAndFlush();
        });
      Text(`播放是否结束：${this.isEnd}`);
    }
    .padding(40)
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%');
  }

  //定时获取音频流时间戳，当时间戳不变时，播放结束
  checkPlayEnd() {
    this.intervalId = setInterval(() => {
      audioRenderer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
        console.info(`Current timestamp: ${JSON.stringify(audioTimestampInfo)}`);
        if (this.preTimestamp === audioTimestampInfo.timestamp) {
          console.info(`Last timestamp: ${this.preTimestamp}`);
          this.isEnd = true;
          clearInterval(this.intervalId);
        }
        this.preTimestamp = audioTimestampInfo.timestamp;
      }).catch((err: BusinessError) => {
        console.error(`ERROR: ${err}`);
      });
    }, 250);
  }

  async init() {
    audioRenderer.on('writeData', (buffer: ArrayBuffer) => {
      if (!this.audioData) {
        return audio.AudioDataCallbackResult.INVALID;
      }
      let bufferView = new Uint8Array(buffer);
      let writeLen = Math.min(buffer.byteLength, this.audioData.byteLength - this.writeOffset);
      if (writeLen <= 0) {
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
    });
    audioRenderer.flush().then(() => {
      console.error('Renderer flush ok.');
    }).catch((err: BusinessError) => {
      console.error('renderer flush err. ' + err);
    });
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
    6: 880.00, // A5
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
