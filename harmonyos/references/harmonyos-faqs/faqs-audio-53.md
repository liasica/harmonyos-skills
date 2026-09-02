---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-53
title: 如何实现扬声器听筒的切换
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何实现扬声器听筒的切换
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:21+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:97a72b07258a9072fe2e49688b31b02086c6b9b0f8f2e23807103e0b569fc5b0
---

## 问题现象

音频播放场景，有没有API可以切换扬声器或听筒播放声音？

## 背景知识

应用可通过AVCastPicker或setDefaultOutputDevice实现音频输出设备路由切换，可参考[实现音频输出设备路由切换](../harmonyos-guides/audio-output-device-switcher.md)。

## 解决方案

* **方案一：[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)投播组件**：
  + 支持用户在页面手动切换不同的音频输出设备。
  + 支持有线耳机、蓝牙耳机等外接设备设备间的切换。
* **方案二：setDefaultOutputDevice：**
  + 包括AudioRenderer的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)（C接口[OH\_AudioRenderer\_SetDefaultOutputDevice](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setdefaultoutputdevice)）和AudioSessionManager的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)（C接口[OH\_AudioSessionManager\_SetDefaultOutputDevice](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setdefaultoutputdevice)）。
  + 当使用AudioRenderer播放音频时，可直接使用setDefaultOutputDevice切换扬声器和听筒，但优先级低于AudioSessionManager的setDefaultOutputDevice。
  + 三方SDK播放器、AVPlayer等其他播放方式，可使用AudioSessionManager的setDefaultOutputDevice实现，使用前需要调用[activateAudioSession](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#activateaudiosession12)激活。
  + AudioSessionManager的setDefaultOutputDevice优先级低于AVCastPicker。如果使用AVCastPicker切换过发声设备，再次调用AudioSessionManager切换设备将不生效。
  + 仅支持VOIP场景，即[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为语音消息、VOIP语音通话或者VOIP视频通话的场景。如果无法配置音频流参数，可调用[setAudioSessionScene](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setaudiosessionscene20)设置音频会话场景[AudioSessionScene](../harmonyos-references/arkts-apis-audio-e.md#audiosessionscene20)为VoIP语音通话音频会话场景。
  + 插入蓝牙耳机等外接设备时，不支持切换。

  **说明** 

  如需在连接蓝牙耳机等外接设备时将音频输出切换到扬声器，可使用AudioSessionManager的[setMediaOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setmediaoutputdevice)接口设置媒体音频输出设备，该接口支持在蓝牙设备连接后指定输出设备为扬声器。可基于HarmonyOS 7.0(26.0.0) Beta1版本验收。

使用示例代码如下：

```ts
import { audio } from '@kit.AudioKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AVCastPicker, avSession } from '@kit.AVSessionKit';

let audioRenderer: audio.AudioRenderer;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_8000, // 采样率
  channels: audio.AudioChannel.CHANNEL_1, // 通道
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型
  rendererFlags: 0 // 音频渲染器标志
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioManager = audio.getAudioManager(); // 需要先创建AudioManager实例
let audioSessionManager = audioManager.getSessionManager(); // 再调用AudioManager的方法创建AudioSessionManager实例
let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_PAUSE_OTHERS
};
let sessionAv: avSession.AVSession;

@Entry
@Component
export struct SwitchAudioDeviceDemo {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  audioData: Uint8Array = genTestPCM(); // 测试PCM数据，按需替换为其他音频数据源
  writeOffset = 0;
  @State renderIsSpeaker: boolean = false;
  @State sessionIsSpeaker: boolean = false;

  async aboutToAppear(): Promise<void> {
    audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
    await this.init(); // 初始化

    audioSessionManager.activateAudioSession(strategy).then(() => { // 激活audioSession
      console.info('Succeeded in activating audio session.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to activate audio session. Code: ${err.code}, message: ${err.message}`);
    });

    sessionAv = await avSession.createAVSession(this.context, 'voiptest', 'voice_call');
  }

  async aboutToDisappear(): Promise<void> {
    await audioRenderer.release();

    await sessionAv.destroy();

    await audioSessionManager.deactivateAudioSession().then(() => {
      console.info('Succeeded in deactivating audio session.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to deactivate audio session. Code: ${err.code}, message: ${err.message}`);
    });
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

      Row() {
        Text('AudioRenderer切换播放设备：');
        Toggle({ type: ToggleType.Switch, isOn: this.renderIsSpeaker })
          .onChange((isOn: boolean) => {
            this.renderIsSpeaker = isOn;
            audioRenderer.setDefaultOutputDevice(isOn ? audio.DeviceType.SPEAKER :
              audio.DeviceType.EARPIECE)
              .then(() => {
                console.info('AudioRenderer Succeeded in setting default output device.');
              }).catch((err: BusinessError) => {
              console.error(`AudioRenderer setDefaultOutputDevice Fail: ${err}`);
            });
          });
        Text(`${this.renderIsSpeaker ? '扬声器' : '听筒'}`);
      }
      .width('100%')
      .justifyContent(FlexAlign.Start);

      Row() {
        Text('AudioSession   切换播放设备：');
        Toggle({ type: ToggleType.Switch, isOn: this.sessionIsSpeaker })
          .onChange((isOn: boolean) => {
            this.sessionIsSpeaker = isOn;
            audioSessionManager.setDefaultOutputDevice(isOn ? audio.DeviceType.SPEAKER :
              audio.DeviceType.EARPIECE)
              .then(() => {
                console.info('AudioSession Succeeded in setting default output device.');
              }).catch((err: BusinessError) => {
              console.error(`AudioSession setDefaultOutputDevice Fail: ${err}`);
            });
          });
        Text(`${this.sessionIsSpeaker ? '扬声器' : '听筒'}`);
      }
      .width('100%')
      .justifyContent(FlexAlign.Start);

      AVCastPicker({}).width('50').height('50');
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
    });
    audioRenderer.flush().then(() => {
      console.error('Renderer flush ok.');
    }).catch((err: BusinessError) => {
      console.error('renderer flush err. ' + err);
    });
    this.writeOffset = 0;
  }
}

function genTestPCM(): Uint8Array {
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
