---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-62
title: 低功耗模式后台播放或息屏时，音频播放不完整
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 低功耗模式后台播放或息屏时，音频播放不完整
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:94898de59e6598921564d39b80942a7823dc56a762278addf9797541acea9dce
---

## 问题现象

AudioRenderer或OHAudio播放音频时，退到后台或息屏后，音频进度不对，播放不完整，没结束就跳到下一个音频，怎么解决？

## 背景知识

* [AudioRenderer](../harmonyos-guides/using-audiorenderer-for-playback.md)是音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据。
* [OHAudio](../harmonyos-guides/using-ohaudio-for-playback.md)是系统在API version 10中引入的一套C API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输出功能的场景。
* [低功耗音频播放](../harmonyos-guides/power-saving-for-playback.md)是一种通过软硬芯协同设计实现的音频渲染方案。其核心机制是增大音频渲染器的内部缓存，使系统能够一次性填充大量音频数据，从而允许主处理器长时间休眠，减少频繁处理音频数据的功耗，显著降低系统级功耗负载。

## 解决方案

音频播放流[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)类型使用STREAM\_USAGE\_MUSIC、STREAM\_USAGE\_AUDIOBOOK时，系统默认为低功耗渲染器，且无法关闭低功耗模式。熄屏场景下，系统会一次性向应用请求大量音频数据缓存起来，应用数据写完不代表已经播完，需要应用侧增加判断，否则会出现音频播放不完整的问题。

**解决方案一：**

如果非音乐、有声读物场景，可以选择其他[音频流类型](../harmonyos-references/arkts-apis-audio-e.md#streamusage)，规避低功耗渲染模式。

**解决方案二:**

修改播放结束跳转下一首逻辑，定时调用获取音频时间戳接口[getAudioTimestampInfo](../harmonyos-references/arkts-apis-audio-audiorenderer.md#getaudiotimestampinfo19)或[OH\_AudioRenderer\_GetAudioTimestampInfo](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_getaudiotimestampinfo)（建议大于200ms一次，以免影响系统性能），当2个周期内时间戳不变，即为播完，可以继续播放下一个音频。

示例代码如下：

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { common, wantAgent } from '@kit.AbilityKit';

let audioRenderer: audio.AudioRenderer;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_8000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_1, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};
let sessionAv: avSession.AVSession;

@Entry
@Component
export struct RendererLowpowerDemo {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  audioData: Uint8Array = generateTestPCM(); // 测试PCM数据，按需替换为其他音频数据源
  writeOffset = 0;
  @State writeFinishTimeStamp: number = 0;
  @State playFinishTimeStamp: number = 0;
  intervalId = 0;
  preTimestamp = 0;
  @State selectUsage: string = 'STREAM_USAGE_MUSIC';

  async aboutToDisappear(): Promise<void> {
    await this.clear();
  }

  build() {
    Column({ space: 20 }) {
      Select([
        { value: 'STREAM_USAGE_MUSIC' },
        { value: 'STREAM_USAGE_MOVIE' },
        { value: 'STREAM_USAGE_AUDIOBOOK' },
      ])
        .value($$this.selectUsage);

      Button('播放音频数据')
        .width('100%')
        .onClick(async () => {
          await this.clear();

          await this.init(); // 初始化

          sessionAv = await avSession.createAVSession(this.context, 'test', 'audio');

          BackgroundUtil.startContinuousTask(this.context); //启动后台任务

          await audioRenderer.start();

          this.intervalGetTimestamp(); // 定时获取播放时间戳，判断渲染是否结束
        });
      Button('停止播放')
        .width('100%')
        .onClick(async () => {
          this.stopAndFlush();

          await this.clear();
        });

      Text(`应用数据写完时间戳/秒：${this.writeFinishTimeStamp / 1000}`);
      Text(`系统播放结束时间戳/秒：${this.playFinishTimeStamp / 1000}`);
    }
    .padding(20)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }

  async clear() {
    sessionAv?.destroy();
    BackgroundUtil.stopContinuousTask(this.context);
    clearInterval(this.intervalId);
    await audioRenderer?.release();

    this.writeOffset = 0;
    this.writeFinishTimeStamp = 0;
    this.playFinishTimeStamp = 0;
    this.intervalId = 0;
    this.preTimestamp = 0;
  }

  intervalGetTimestamp() {
    this.intervalId = setInterval(() => {
      audioRenderer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
        console.info(`Current timestamp: ${JSON.stringify(audioTimestampInfo)}`);
        if (this.preTimestamp === audioTimestampInfo.timestamp) {
          console.info(`Last timestamp: ${this.preTimestamp}`);
          this.playFinishTimeStamp = systemDateTime.getTime();
          console.info(`audioRenderer play finish ${this.playFinishTimeStamp / 1000}`);
          clearInterval(this.intervalId);
        }
        this.preTimestamp = audioTimestampInfo.timestamp;
      }).catch((err: BusinessError) => {
        console.error(`ERROR: ${err}`);
      });
    }, 250);
  }

  async init() {
    let streamUsage = audio.StreamUsage.STREAM_USAGE_MUSIC;
    if (this.selectUsage === 'STREAM_USAGE_MOVIE') {
      streamUsage = audio.StreamUsage.STREAM_USAGE_MOVIE;
    } else if (this.selectUsage === 'STREAM_USAGE_AUDIOBOOK') {
      streamUsage = audio.StreamUsage.STREAM_USAGE_AUDIOBOOK;
    }

    let audioRendererInfo: audio.AudioRendererInfo = {
      usage: streamUsage, // 音频流使用类型,根据业务场景配置，参考StreamUsage。
      rendererFlags: 0 // 音频渲染器标志。
    };
    let audioRendererOptions: audio.AudioRendererOptions = {
      streamInfo: audioStreamInfo,
      rendererInfo: audioRendererInfo
    };

    audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
    audioRenderer.on('writeData', (buffer: ArrayBuffer) => {
      if (!this.audioData) {
        return audio.AudioDataCallbackResult.INVALID;
      }
      let bufferView = new Uint8Array(buffer);
      let writeLen = Math.min(buffer.byteLength, this.audioData.byteLength - this.writeOffset);
      if (writeLen <= 0) {
        if (this.writeFinishTimeStamp === 0) {
          this.writeFinishTimeStamp = systemDateTime.getTime();
          console.info(`audioRenderer writeData finish ${this.writeFinishTimeStamp / 1000}`);
        }
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
    6: 880.00, // A5
  };

  const melody = [
    1, 1, 5, 5, 6, 6, 5, 0,
    4, 4, 3, 3, 2, 2, 1, 0,
    5, 5, 4, 4, 3, 3, 2, 0,
    1, 1, 5, 5, 6, 6, 5, 0,
    4, 4, 3, 3, 2, 2, 1, 0,
    5, 5, 4, 4, 3, 3, 2, 0,
    1, 1, 5, 5, 6, 6, 5, 0,
    4, 4, 3, 3, 2, 2, 1, 0,
    5, 5, 4, 4, 3, 3, 2, 0,
    1, 1, 5, 5, 6, 6, 5, 0,
    4, 4, 3, 3, 2, 2, 1, 0,
    5, 5, 4, 4, 3, 3, 2, 0,
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

export class BackgroundUtil {
  public static startContinuousTask(context?: common.UIAbilityContext): void {
    if (!context) {
      console.error('startContinuousTask failed', `context undefined`);
      return;
    }
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: context.abilityInfo.bundleName,
          abilityName: context.abilityInfo.name
        }
      ],
      actionType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: Object) => {
      try {
        backgroundTaskManager.startBackgroundRunning(context,
          backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
          console.info('this audioRenderer: ', 'startBackgroundRunning succeeded');
        }).catch((error: BusinessError) => {
          console.error('this audioRenderer: ', `startBackgroundRunning failed Cause: code ${error.code}`);
        });
      } catch (error) {
        console.error(`startBackgroundRunning failed.message ${(error as BusinessError).message}`);
      }
    });
  }

  public static stopContinuousTask(context: common.UIAbilityContext): void {
    try {
      backgroundTaskManager.stopBackgroundRunning(context).then(() => {
        console.info('this audioRenderer: ', 'stopBackgroundRunning succeeded');
      }).catch((error: BusinessError) => {
        console.error('this audioRenderer: ', `stopBackgroundRunning failed Cause: code ${error.code}`);
      });
    } catch (error) {
      console.error(`stopBackgroundRunning failed. message ${(error as BusinessError).message}`);
    }
  }
}
```
