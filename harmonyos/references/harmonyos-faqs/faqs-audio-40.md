---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-40
title: 使用AudioCapturer录制音频时，如何获取音量分贝大小
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 使用AudioCapturer录制音频时，如何获取音量分贝大小
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:59f61358eeb45abcaeadc49c1a3c1d10ab47b8a0b22ab0b6c5c62a52eee3fd7a
---

## 问题现象

在使用AudioCapturer录制PCM音频数据时，需要监听音频音量大小，并通过绘制波形图等来反映出音频变化的趋势。该如何获取音量大小？

## 背景知识

* [AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)是音频采集器，用于录制PCM（Pulse Code Modulation）音频数据，需要开发者持续读取音频数据进行工作。应用可以在读取音频数据后添加数据处理。
* [getMaxAmplitudeForInputDevice](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#getmaxamplitudeforinputdevice12)：获取输入设备音频流的最大电平值，取值范围为[0, 1]。

## 解决方案

**方案一：计算PCM音频数据的音量分贝大小。**

计算PCM音频数据的音量分贝，需要先获得采样点的幅值，然后使用分贝公式计算，具体步骤如下：

1. 根据AudioCapturer的音频采样格式将PCM音频数据转化成对应的幅值。
2. 将所有采样点的幅值平方后求和，再除以采样点数后开平方，得到均方根能量值。
3. 将均方根能量值代入分贝公式计算得到音量分贝，分贝公式：db=20 \* log10(均方根能量值/参考幅度值)。

当AudioCapturer的采样格式为SAMPLE\_FORMAT\_S16LE时，根据PCM音频数据计算音量分贝大小的参考代码如下：

```ts
// buffer：AudioCapturer录制的PCM音频数据
private pcm2DB(buffer: ArrayBuffer): number {
  const refAmplitude = 32767; // 采样深度为有符号16bit时，参考振幅值为最大正值32767。
  const amplitudeArr = new Int16Array(buffer); // 16bit为一个采样点
  let sum: number = 0;
  for (let i = 0; i < amplitudeArr.length; i++) {
    sum += amplitudeArr[i] * amplitudeArr[i]; // 计算平方和
  }
  let rms = Math.sqrt(sum / amplitudeArr.length); // 计算均方根能量值
  let db = 20 * Math.log10(rms / refAmplitude); // 计算音量分贝大小
  return db;
}
```

**方案二：调用getMaxAmplitudeForInputDevice()获取输入设备音频流的最大电平值。**

如果需要获取音频流变化趋势，也可以调用getMaxAmplitudeForInputDevice()获取输入设备音频流的最大电平值，参考示例代码如下：

```ts
// 监听最大电平值
async getMaxAmplitude() {
  let audioManager = audio.getAudioManager();
  let audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
  let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;
  let audioVolumeGroupManager: audio.AudioVolumeGroupManager =
    await audioVolumeManager.getVolumeGroupManager(groupId);
  let deviceDescriptors: audio.AudioDeviceDescriptors | undefined =
    this.capturer?.getCurrentInputDevices();

  if (deviceDescriptors === undefined) {
    return;
  }
  audioVolumeGroupManager.getMaxAmplitudeForInputDevice(deviceDescriptors[0]).then((value) => {
    console.info(`max amplitude is: ${value}`);
  }).catch((err: BusinessError) => {
    console.error(`getMaxAmplitudeForInputDevice error. Code: ${err.code}, message: ${err.message}`);
  });
}
```

完整代码参考如下:

```ts
import { audio } from '@kit.AudioKit';
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  channels: audio.AudioChannel.CHANNEL_1,
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW,
};
let audioCapturerInfo: audio.AudioCapturerInfo = {
  capturerFlags: 0,
  source: audio.SourceType.SOURCE_TYPE_MIC,
};
let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo,
};

@Entry
@Component
struct Index {
  private capturer?: audio.AudioCapturer;
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    requestPermissions(this.context, ['ohos.permission.MICROPHONE']);
  }

  aboutToDisappear(): void {
    this.stopCapturer();
    this.releaseCapturer();
  }

  build() {
    Column({ space: 20 }) {
      Row() {
        Text('音频分贝大小:');

        Button('监听')
          .onClick(async () => {
            await this.initCapturerGetDb();
            await this.startCapturer();
          });

        Button('取消监听')
          .onClick(async () => {
            await this.stopCapturer();
            await this.releaseCapturer();
          });
      }
      .width('85%')
      .justifyContent(FlexAlign.SpaceEvenly);

      Row() {
        Text('音频振幅大小:');

        Button('监听')
          .onClick(async () => {
            await this.initCapturerGetMaxAmplitude();
            await this.startCapturer();
          });
        Button('取消监听')
          .onClick(async () => {
            await this.stopCapturer();
            await this.releaseCapturer();
          });
      }
      .width('85%')
      .justifyContent(FlexAlign.SpaceEvenly);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }

  // buffer：AudioCapturer录制的PCM音频数据
  private pcm2DB(buffer: ArrayBuffer): number {
    const refAmplitude = 32767; // 采样深度为有符号16bit时，参考振幅值为最大正值32767。
    const amplitudeArr = new Int16Array(buffer); // 16bit为一个采样点
    let sum: number = 0;
    for (let i = 0; i < amplitudeArr.length; i++) {
      sum += amplitudeArr[i] * amplitudeArr[i]; // 计算平方和
    }
    let rms = Math.sqrt(sum / amplitudeArr.length); // 计算均方根能量值
    let db = 20 * Math.log10(rms / refAmplitude); // 计算音量分贝大小
    return db;
  }

  async initCapturerGetDb(): Promise<void> {
    this.capturer = await audio.createAudioCapturer(audioCapturerOptions);

    try {
      this.capturer.on('readData', (buffer: ArrayBuffer) => {
        let db = this.pcm2DB(buffer);
        console.info(`DB Value: ${db}`);
      });
    } catch (err) {
      console.error(`failed to register readData event: ${JSON.stringify(err)}`);
    }
  }

  // 监听最大电平值
  async getMaxAmplitude() {
    let audioManager = audio.getAudioManager();
    let audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
    let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;
    let audioVolumeGroupManager: audio.AudioVolumeGroupManager =
      await audioVolumeManager.getVolumeGroupManager(groupId);
    let deviceDescriptors: audio.AudioDeviceDescriptors | undefined =
      this.capturer?.getCurrentInputDevices();

    if (deviceDescriptors === undefined) {
      return;
    }
    audioVolumeGroupManager.getMaxAmplitudeForInputDevice(deviceDescriptors[0]).then((value) => {
      console.info(`max amplitude is: ${value}`);
    }).catch((err: BusinessError) => {
      console.error(`getMaxAmplitudeForInputDevice error. Code: ${err.code}, message: ${err.message}`);
    });
  }

  async initCapturerGetMaxAmplitude(): Promise<void> {
    this.capturer = await audio.createAudioCapturer(audioCapturerOptions);

    try {
      this.capturer.on('readData', () => {
        this.getMaxAmplitude();
      });
    } catch (err) {
      console.error(`failed to register readData event: ${JSON.stringify(err)}`);
    }
  }

  async startCapturer(): Promise<void> {
    if (this.capturer === undefined) {
      throw new Error(`AudioCapturer is undefined`);
    }
    let state = this.capturer.state;
    if (state !== audio.AudioState.STATE_PREPARED && state !== audio.AudioState.STATE_STOPPED) {
      throw new Error(`AudioCapturer is at wrong state, ${state}`);
    }
    await this.capturer.start();
  }

  async stopCapturer(): Promise<void> {
    if (this.capturer === undefined) {
      throw new Error(`AudioCapturer is undefined`);
    }
    let state = this.capturer.state;
    if (state !== audio.AudioState.STATE_RUNNING) {
      throw new Error(`AudioCapturer is at wrong state, ${state}`);
    }

    await this.capturer.stop();
  }

  async releaseCapturer(): Promise<void> {
    if (this.capturer === undefined) {
      throw new Error(`AudioCapturer is undefined`);
    }
    let state = this.capturer.state;
    if (state !== audio.AudioState.STATE_PREPARED && state !== audio.AudioState.STATE_STOPPED) {
      throw new Error(`AudioCapturer is at wrong state, ${state}`);
    }

    try {
      this.capturer.off('readData');
    } catch (err) {
      console.error(`failed to unregister readData event: ${JSON.stringify(err)}`);
    }

    await this.capturer.release();
    this.capturer = undefined;
  }
}

function requestPermissions(context: common.UIAbilityContext, permissions: Permissions[]): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions)
    .then((result: PermissionRequestResult) => {
      let grantStatus: number[] = result.authResults;
      let length = grantStatus.length;
      for (let i = 0; i < length; i++) {
        if (grantStatus[i] !== 0) {
          console.info(`User reject to grant permission: ${permissions[i]}`);
        }
      }
    })
    .catch((err: BusinessError) => {
      console.error(`Request permissions from user failed, ${JSON.stringify(err)}`);
    });
}
```

**说明** 

应用可以调用麦克风录制音频，但该行为属于隐私敏感行为，在调用麦克风前，需要先[向用户申请权限](../harmonyos-guides/request-user-authorization.md)：ohos.permission.MICROPHONE。
