---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audiorecorder
title: 废弃的Interface (AudioRecorder, deprecated)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > 废弃的Interface (AudioRecorder, deprecated)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:45+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:708c80d902fa28c50a64415805e5dd52a7abc674ab479a58e26c73fc9741a297
---

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder](arkts-apis-media-avrecorder.md)替代。

音频录制管理类，用于录制音频媒体。在调用AudioRecorder的方法前，需要先通过[createAudioRecorder()](arkts-apis-media-f.md#mediacreateaudiorecorderdeprecated) 构建一个AudioRecorder实例。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## prepare(deprecated)

PhonePC/2in1TabletTVWearable

prepare(config: AudioRecorderConfig): void

录音准备。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.prepare](arkts-apis-media-avrecorder.md#prepare9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AudioRecorderConfig](arkts-apis-media-i.md#audiorecorderconfigdeprecated) | 是 | 配置录音的相关参数，包括音频输出URI、编码格式、采样率、声道数、输出格式等。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied |

**示例：**

```
1. let audioRecorderConfig: media.AudioRecorderConfig = {
2. audioEncoder : media.AudioEncoder.AAC_LC,
3. audioEncodeBitRate : 64000,
4. audioSampleRate : 44100,
5. numberOfChannels : 2,
6. format : media.AudioOutputFormat.AAC_ADTS,
7. uri : 'fd://1',       // 文件需先由调用者创建，并给予适当的权限。
8. location : { latitude : 30, longitude : 130},
9. };
10. audioRecorder.on('prepare', () => {    // 设置'prepare'事件回调。
11. console.info('prepare called');
12. });
13. audioRecorder.prepare(audioRecorderConfig);
```

## start(deprecated)

PhonePC/2in1TabletTVWearable

start(): void

开始录制，需在'prepare'事件成功触发后，才能调用start方法。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.start](arkts-apis-media-avrecorder.md#start9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```
1. audioRecorder.on('start', () => {    // 设置'start'事件回调。
2. console.info('audio recorder start called');
3. });
4. audioRecorder.start();
```

## pause(deprecated)

PhonePC/2in1TabletTVWearable

pause():void

暂停录制，需要在'start'事件成功触发后，才能调用pause方法。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.pause](arkts-apis-media-avrecorder.md#pause9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```
1. audioRecorder.on('pause', () => {    // 设置'pause'事件回调。
2. console.info('audio recorder pause called');
3. });
4. audioRecorder.pause();
```

## resume(deprecated)

PhonePC/2in1TabletTVWearable

resume():void

恢复录制，需要在'pause'事件成功触发后，才能调用resume方法。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.resume](arkts-apis-media-avrecorder.md#resume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```
1. audioRecorder.on('resume', () => {    // 设置'resume'事件回调。
2. console.info('audio recorder resume called');
3. });
4. audioRecorder.resume();
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(): void

停止录音。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.stop](arkts-apis-media-avrecorder.md#stop9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```
1. audioRecorder.on('stop', () => {    // 设置'stop'事件回调。
2. console.info('audio recorder stop called');
3. });
4. audioRecorder.stop();
```

## release(deprecated)

PhonePC/2in1TabletTVWearable

release(): void

释放录音资源。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.release](arkts-apis-media-avrecorder.md#release9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```
1. audioRecorder.on('release', () => {    // 设置'release'事件回调。
2. console.info('audio recorder release called');
3. });
4. audioRecorder.release();
5. audioRecorder = undefined;
```

## reset(deprecated)

PhonePC/2in1TabletTVWearable

reset(): void

重置录音。

进行重置录音之前，需要先调用stop()停止录音。重置录音之后，需要调用prepare()设置录音参数项，才能再次进行录音。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.reset](arkts-apis-media-avrecorder.md#reset9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```
1. audioRecorder.on('reset', () => {    // 设置'reset'事件回调。
2. console.info('audio recorder reset called');
3. });
4. audioRecorder.reset();
```

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void

开始订阅音频录制事件。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('stateChange')](arkts-apis-media-avrecorder.md#onstatechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制事件回调类型，支持的事件包括：'prepare' | 'start' | 'pause' | ’resume‘ | 'stop' | 'release' | 'reset'。  - 'prepare' ：完成prepare调用，音频录制参数设置完成，触发该事件。  - 'start' ：完成start调用，音频录制开始，触发该事件。  - 'pause': 完成pause调用，音频暂停录制，触发该事件。  - 'resume': 完成resume调用，音频恢复录制，触发该事件。  - 'stop' ：完成stop调用，音频停止录制，触发该事件。  - 'release' ：完成release调用，音频释放录制资源，触发该事件。  - 'reset'：完成reset调用，音频重置为初始状态，触发该事件。 |
| callback | ()=>void | 是 | 录制事件回调方法。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let audioRecorder: media.AudioRecorder = media.createAudioRecorder();  // 创建一个音频录制实例。
4. let audioRecorderConfig: media.AudioRecorderConfig = {
5. audioEncoder : media.AudioEncoder.AAC_LC,
6. audioEncodeBitRate : 64000,
7. audioSampleRate : 44100,
8. numberOfChannels : 2,
9. format : media.AudioOutputFormat.AAC_ADTS,
10. uri : 'fd://xx',  // 文件需先由调用者创建，并给予适当的权限。
11. location : { latitude : 30, longitude : 130}
12. };
13. audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
14. console.error(`audio error called, error: ${error}`);
15. });
16. audioRecorder.on('prepare', () => {  // 设置'prepare'事件回调。
17. console.info('prepare called');
18. audioRecorder.start();  // 开始录制，并触发'start'事件回调。
19. });
20. audioRecorder.on('start', () => {  // 设置'start'事件回调。
21. console.info('audio recorder start called');
22. });
23. audioRecorder.on('pause', () => {  // 设置'pause'事件回调。
24. console.info('audio recorder pause called');
25. });
26. audioRecorder.on('resume', () => {  // 设置'resume'事件回调。
27. console.info('audio recorder resume called');
28. });
29. audioRecorder.on('stop', () => {  // 设置'stop'事件回调。
30. console.info('audio recorder stop called');
31. });
32. audioRecorder.on('release', () => {  // 设置'release'事件回调。
33. console.info('audio recorder release called');
34. });
35. audioRecorder.on('reset', () => {  // 设置'reset'事件回调。
36. console.info('audio recorder reset called');
37. });
38. audioRecorder.prepare(audioRecorderConfig)  // 设置录制参数 ，并触发'prepare'事件回调。
```

## on('error')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

开始订阅音频录制错误事件，当上报error错误事件后，用户需处理error事件，退出录制操作。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('error')](arkts-apis-media-avrecorder.md#onerror9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制错误事件回调类型'error'。  - 'error'：音频录制过程中发生错误，触发该事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 录制错误事件回调方法。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let audioRecorderConfig: media.AudioRecorderConfig = {
4. audioEncoder : media.AudioEncoder.AAC_LC,
5. audioEncodeBitRate : 22050,
6. audioSampleRate : 22050,
7. numberOfChannels : 2,
8. format : media.AudioOutputFormat.AAC_ADTS,
9. uri : 'fd://xx',   // 文件需先由调用者创建，并给予适当的权限。
10. location : { latitude : 30, longitude : 130}
11. };
12. audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
13. console.error(`audio error called, error: ${error}`);
14. });
15. audioRecorder.prepare(audioRecorderConfig);  // prepare不设置参数，触发'error'事件。
```
