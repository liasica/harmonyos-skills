---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-65
title: 怎么在播放音频时不打断其他APP音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 怎么在播放音频时不打断其他APP音频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:fc56336abc0974e118c63c18d7357c4dbc220e977e069df6fa38d759078b0866
---

## 问题现象

播放音频时，会暂停后台音乐播放，如何降低其他APP音量或者与其他音频同时播放？

## 背景知识

* 系统预设了默认的[音频焦点](../harmonyos-guides/audio-playback-concurrency.md#音频焦点)策略，根据音频流的类型及启动的先后顺序，对所有播放和录制音频流进行统一管理。
* 应用可利用[音频会话管理（AudioSessionManager）](../harmonyos-guides/audio-session-management.md)提供的接口，通过AudioSession主动管理应用内音频流的焦点，自定义本应用音频流的焦点策略。

## 解决方案

* **方案一**：

  应用可通过配置合适的音频流类型[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)，根据系统默认的音频焦点策略，达到降低音量或同时播放的效果。

  例如先播放STREAM\_USAGE\_MUSIC音乐音频，后播STREAM\_USAGE\_NAVIGATION导航音频可实现降低先播音频音量效果，详情可参考[系统默认焦点策略表](../best-practices/bpta-audio-focus-management.md#section2888185819153)。
* **方案二**：

  当系统默认焦点策略不满足应用焦点需求时，可通过[音频会话（AudioSession）](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)自定义本应用的焦点策略。

  系统预设四种并发模式可按需选择：

  + 默认模式（CONCURRENCY\_DEFAULT）：即系统默认的音频焦点策略。
  + 并发模式（CONCURRENCY\_MIX\_WITH\_OTHERS）：和其他音频流并发。
  + 降低音量模式（CONCURRENCY\_DUCK\_OTHERS）：和其他音频流并发，并且降低其他音频流的音量。
  + 暂停模式（CONCURRENCY\_PAUSE\_OTHERS）：暂停其他音频流，待释放焦点后通知其他音频流恢复。

  详细使用步骤可参考官网[使用AudioSession管理应用音频焦点(ArkTS)](../harmonyos-guides/audio-session-management.md)或者[使用AudioSession管理应用音频焦点(C/C++)](../harmonyos-guides/using-ohaudio-for-session.md)。

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

  let audioManager = audio.getAudioManager();
  let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();
  let strategy: audio.AudioSessionStrategy = {
    concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_DEFAULT
  };

  @Entry
  @Component
  export struct AudioSessionDemo {
    context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    audioData: Uint8Array = generateTestPCM(); // 测试PCM数据，按需替换为其他音频数据源
    writeOffset = 0;

    async aboutToAppear(): Promise<void> {
      audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
      await this.init(); //初始化
    }

    async aboutToDisappear(): Promise<void> {
      try {
        await audioSessionManager.deactivateAudioSession();
      } catch (error) {
        console.error(`deactivateAudioSession ${JSON.stringify(error)}`);
      }
      await audioRenderer.release();
    }

    build() {
      Column({ space: 10 }) {
        Select([{ value: '默认模式（CONCURRENCY_DEFAULT）' },
          { value: '并发模式（CONCURRENCY_MIX_WITH_OTHERS）' },
          { value: '降低音量模式（CONCURRENCY_DUCK_OTHERS）' },
          { value: '暂停模式（CONCURRENCY_PAUSE_OTHERS）' }])
          .value('默认模式（CONCURRENCY_DEFAULT）')
          .optionFont({ size: 12 })
          .onSelect((index: number, text: string) => {
            console.info('Select:' + index + text);
            strategy = {
              concurrencyMode: text === '并发模式（CONCURRENCY_MIX_WITH_OTHERS）' ?
                audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS :
                text === '降低音量模式（CONCURRENCY_DUCK_OTHERS）' ? audio.AudioConcurrencyMode.CONCURRENCY_DUCK_OTHERS :
                  text === '暂停模式（CONCURRENCY_PAUSE_OTHERS）' ? audio.AudioConcurrencyMode.CONCURRENCY_PAUSE_OTHERS :
                    audio.AudioConcurrencyMode.CONCURRENCY_DEFAULT
            };
          });

        Button('激活AudioSession并播放')
          .onClick(async () => {
            console.info(`strategy: ${JSON.stringify(strategy)}}`);
            try {
              await audioSessionManager.activateAudioSession(strategy);
              await this.stopAndFlush();
              await audioRenderer.start();
            } catch (error) {
              console.error(`activateAudioSession ${JSON.stringify(error)}`);
            }
          });

        Button('取消激活AudioSession并停止播放').onClick(async () => {
          try {
            await audioSessionManager.deactivateAudioSession();
            await this.stopAndFlush();
          } catch (error) {
            console.error(`deactivateAudioSession ${JSON.stringify(error)}`);
          }
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
          this.writeOffset = 0; //归零循环播放，测试用
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
