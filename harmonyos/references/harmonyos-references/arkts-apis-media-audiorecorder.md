---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audiorecorder
title: 废弃的Interface (AudioRecorder, deprecated)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > 废弃的Interface (AudioRecorder, deprecated)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:25ed94f2e122a94d7fc4252794e561fcd6cd98a5a94d8478c298d9c2be5a041d
---

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder](arkts-apis-media-avrecorder.md)替代。

音频录制管理接口，用于录制音频媒体，支持音频录制的准备、开始、暂停、恢复、停止、释放和重置等操作，适用于语音备忘录、通话录音、音乐录制等需要录制音频的场景。在调用AudioRecorder的方法前，需要先通过[createAudioRecorder()](arkts-apis-media-f.md#mediacreateaudiorecorderdeprecated) 构建一个AudioRecorder实例。

## 导入模块

```ts
import { media } from '@kit.MediaKit';
```

## prepare(deprecated)

prepare(config: AudioRecorderConfig): void

录制准备，根据传入的配置参数初始化录制资源（包括编码器、采样率、声道数等），完成录制前的准备工作。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.prepare](arkts-apis-media-avrecorder.md#prepare9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AudioRecorderConfig](arkts-apis-media-i.md#audiorecorderconfigdeprecated) | 是 | 配置录制的相关参数，包括音频输出URI、编码格式、采样率、声道数、输出格式等。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied.  适用版本：12+ |

**示例：**

```ts
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://1',       // fd通过fs.open()获取。文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    // 设置'prepare'事件回调。
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);
```

## start(deprecated)

start(): void

开始录制。需在'prepare'事件成功触发后，才能调用start方法。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.start](arkts-apis-media-avrecorder.md#start9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('start', () => {    // 设置'start'事件回调。
  console.info('audio recorder start called');
});
audioRecorder.start();
```

## pause(deprecated)

pause():void

暂停录制。需在'start'事件成功触发后，才能调用pause方法。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.pause](arkts-apis-media-avrecorder.md#pause9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('pause', () => {    // 设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.pause();
```

## resume(deprecated)

resume():void

恢复录制。需在'pause'事件成功触发后，才能调用resume方法。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.resume](arkts-apis-media-avrecorder.md#resume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('resume', () => {    // 设置'resume'事件回调。
  console.info('audio recorder resume called');
});
audioRecorder.resume();
```

## stop(deprecated)

stop(): void

停止录制，并保存已录制的音频数据到文件。需在'start'事件成功触发后，才能调用stop方法。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.stop](arkts-apis-media-avrecorder.md#stop9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('stop', () => {    // 设置'stop'事件回调。
  console.info('audio recorder stop called');
});
audioRecorder.stop();
```

## release(deprecated)

release(): void

释放录制资源。释放资源后，不能再调用其它录制方法。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.release](arkts-apis-media-avrecorder.md#release9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('release', () => {    // 设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

## reset(deprecated)

reset(): void

重置录制。

进行重置录制之前，需要先调用stop()停止录制。重置录制之后，需要调用prepare()设置录制参数项，才能再次进行录制。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.reset](arkts-apis-media-avrecorder.md#reset9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('reset', () => {    // 设置'reset'事件回调。
  console.info('audio recorder reset called');
});
audioRecorder.reset();
```

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')(deprecated)

on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void

订阅音频录制事件。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('stateChange')](arkts-apis-media-avrecorder.md#onstatechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制事件回调类型，支持的事件包括：'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset'。  - 'prepare' ：完成prepare调用，音频录制参数设置完成，触发该事件。  - 'start' ：完成start调用，音频录制开始，触发该事件。  - 'pause' ：完成pause调用，音频暂停录制，触发该事件。  - 'resume' ：完成resume调用，音频恢复录制，触发该事件。  - 'stop' ：完成stop调用，音频停止录制，触发该事件。  - 'release' ：完成release调用，音频释放录制资源，触发该事件。  - 'reset' ：完成reset调用，音频重置为初始状态，触发该事件。 |
| callback | ()=>void | 是 | 录制事件回调方法。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorder: media.AudioRecorder = media.createAudioRecorder();  // 创建一个音频录制实例。
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://xx',  // fd通过fs.open()获取。文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`audio error called, error code: ${error.code}, message: ${error.message}`);
});
audioRecorder.on('prepare', () => {  // 设置'prepare'事件回调。
  console.info('prepare called');
  audioRecorder.start();  // 开始录制，并触发'start'事件回调。
});
audioRecorder.on('start', () => {  // 设置'start'事件回调。
  console.info('audio recorder start called');
});
audioRecorder.on('pause', () => {  // 设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.on('resume', () => {  // 设置'resume'事件回调。
  console.info('audio recorder resume called');
});
audioRecorder.on('stop', () => {  // 设置'stop'事件回调。
  console.info('audio recorder stop called');
});
audioRecorder.on('release', () => {  // 设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.on('reset', () => {  // 设置'reset'事件回调。
  console.info('audio recorder reset called');
});
audioRecorder.prepare(audioRecorderConfig);  // 设置录制参数 ，并触发'prepare'事件回调。
```

## on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

订阅音频录制错误事件，收到错误回调后，需处理错误、释放资源并退出当前录制。

**说明** 

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('error')](arkts-apis-media-avrecorder.md#onerror9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制错误事件回调类型'error'。  - 'error'：音频录制过程中发生错误，触发该事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 录制错误事件回调方法。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 22050,
  audioSampleRate : 22050,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://xx',   // fd通过fs.open()获取。文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`audio error called, error code: ${error.code}, message: ${error.message}`);
});
audioRecorder.prepare(audioRecorderConfig);  // prepare设置无效参数，触发'error'事件。
```
