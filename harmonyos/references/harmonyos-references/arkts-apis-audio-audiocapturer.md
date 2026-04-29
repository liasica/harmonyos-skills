---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiocapturer
title: Interface (AudioCapturer)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioCapturer)
category: harmonyos-references
scraped_at: 2026-04-29T14:02:18+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:903595ed104d466e22c4d4470ab6d1a017cc3eaf41e3a5045dff9dd8bf5cad0d
---

提供音频采集的相关接口。

在使用AudioCapturer的接口之前，需先通过[createAudioCapturer](arkts-apis-audio-f.md#audiocreateaudiocapturer8)获取AudioCapturer实例。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 8开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state8+ | [AudioState](arkts-apis-audio-e.md#audiostate8) | 是 | 否 | 音频采集器状态。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let state: audio.AudioState = audioCapturer.state;
```

## getCapturerInfo8+

PhonePC/2in1TabletTVWearable

getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void

获取音频采集器信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8)> | 是 | 回调函数。当获取音频采集器信息成功，err为undefined，data为获取到的音频采集器信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getCapturerInfo((err: BusinessError, capturerInfo: audio.AudioCapturerInfo) => {
4. if (err) {
5. console.error('Failed to get capture info');
6. } else {
7. console.info('Capturer getCapturerInfo:');
8. console.info(`Capturer source: ${capturerInfo.source}`);
9. console.info(`Capturer flags: ${capturerInfo.capturerFlags}`);
10. }
11. });
```

## getCapturerInfo8+

PhonePC/2in1TabletTVWearable

getCapturerInfo(): Promise<AudioCapturerInfo>

获取音频采集器信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8)> | Promise对象，返回音频采集器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getCapturerInfo().then((audioParamsGet: audio.AudioCapturerInfo) => {
4. if (audioParamsGet != undefined) {
5. console.info('AudioFrameworkRecLog: Capturer CapturerInfo:');
6. console.info(`AudioFrameworkRecLog: Capturer SourceType: ${audioParamsGet.source}`);
7. console.info(`AudioFrameworkRecLog: Capturer capturerFlags: ${audioParamsGet.capturerFlags}`);
8. } else {
9. console.info(`AudioFrameworkRecLog: audioParamsGet is : ${audioParamsGet}`);
10. console.info('AudioFrameworkRecLog: audioParams getCapturerInfo are incorrect');
11. }
12. }).catch((err: BusinessError) => {
13. console.error(`AudioFrameworkRecLog: CapturerInfo :ERROR: ${err}`);
14. })
```

## getCapturerInfoSync10+

PhonePC/2in1TabletTVWearable

getCapturerInfoSync(): AudioCapturerInfo

获取音频采集器信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 返回音频采集器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let audioParamsGet: audio.AudioCapturerInfo = audioCapturer.getCapturerInfoSync();
5. console.info(`AudioFrameworkRecLog: Capturer SourceType: ${audioParamsGet.source}`);
6. console.info(`AudioFrameworkRecLog: Capturer capturerFlags: ${audioParamsGet.capturerFlags}`);
7. } catch (err) {
8. let error = err as BusinessError;
9. console.error(`AudioFrameworkRecLog: CapturerInfo :ERROR: ${error}`);
10. }
```

## getStreamInfo8+

PhonePC/2in1TabletTVWearable

getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void

获取音频采集器流信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8)> | 是 | 回调函数。当获取音频采集器流信息成功，err为undefined，data为获取到的音频采集器流信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getStreamInfo((err: BusinessError, streamInfo: audio.AudioStreamInfo) => {
4. if (err) {
5. console.error('Failed to get stream info');
6. } else {
7. console.info('Capturer GetStreamInfo:');
8. console.info(`Capturer sampling rate: ${streamInfo.samplingRate}`);
9. console.info(`Capturer channel: ${streamInfo.channels}`);
10. console.info(`Capturer format: ${streamInfo.sampleFormat}`);
11. console.info(`Capturer encoding type: ${streamInfo.encodingType}`);
12. }
13. });
```

## getStreamInfo8+

PhonePC/2in1TabletTVWearable

getStreamInfo(): Promise<AudioStreamInfo>

获取音频采集器流信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8)> | Promise对象，返回音频流信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getStreamInfo().then((audioParamsGet: audio.AudioStreamInfo) => {
4. console.info('getStreamInfo:');
5. console.info(`sampleFormat: ${audioParamsGet.sampleFormat}`);
6. console.info(`samplingRate: ${audioParamsGet.samplingRate}`);
7. console.info(`channels: ${audioParamsGet.channels}`);
8. console.info(`encodingType: ${audioParamsGet.encodingType}`);
9. }).catch((err: BusinessError) => {
10. console.error(`getStreamInfo :ERROR: ${err}`);
11. });
```

## getStreamInfoSync10+

PhonePC/2in1TabletTVWearable

getStreamInfoSync(): AudioStreamInfo

获取音频采集器流信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8) | 返回音频流信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let audioParamsGet: audio.AudioStreamInfo = audioCapturer.getStreamInfoSync();
5. console.info(`sampleFormat: ${audioParamsGet.sampleFormat}`);
6. console.info(`samplingRate: ${audioParamsGet.samplingRate}`);
7. console.info(`channels: ${audioParamsGet.channels}`);
8. console.info(`encodingType: ${audioParamsGet.encodingType}`);
9. } catch (err) {
10. let error = err as BusinessError;
11. console.error(`getStreamInfo :ERROR: ${error}`);
12. }
```

## getAudioStreamId9+

PhonePC/2in1TabletTVWearable

getAudioStreamId(callback: AsyncCallback<number>): void

获取音频流id。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取音频流id成功，err为undefined，data为获取到的音频流id；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getAudioStreamId((err: BusinessError, streamId: number) => {
4. console.info(`audioCapturer GetStreamId: ${streamId}`);
5. });
```

## getAudioStreamId9+

PhonePC/2in1TabletTVWearable

getAudioStreamId(): Promise<number>

获取音频流id。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回音频流id。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getAudioStreamId().then((streamId: number) => {
4. console.info(`audioCapturer getAudioStreamId: ${streamId}`);
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getAudioStreamIdSync10+

PhonePC/2in1TabletTVWearable

getAudioStreamIdSync(): number

获取音频流id。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音频流id。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let streamId: number = audioCapturer.getAudioStreamIdSync();
5. console.info(`audioCapturer getAudioStreamIdSync: ${streamId}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`ERROR: ${error}`);
9. }
```

## start8+

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

启动音频采集器，开始获取音频数据。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动音频采集器成功，err为undefined，否则为错误对象。异常将返回error对象：  错误码6800301：表示包含状态检查异常、焦点抢占失败、系统处理异常（具体错误查看系统日志）。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.start((err: BusinessError) => {
4. if (err) {
5. console.error('Capturer start failed.');
6. } else {
7. console.info('Capturer start success.');
8. }
9. });
```

## start8+

PhonePC/2in1TabletTVWearable

start(): Promise<void>

启动音频采集器，开始获取音频数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，成功表示启动音频采集器成功。异常将返回error对象：  错误码6800301：表示包含状态检查异常、焦点抢占失败、系统处理异常（具体错误查看系统日志）。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.start().then(() => {
4. console.info('Succeeded in doing start.');
5. if (audioCapturer.state == audio.AudioState.STATE_RUNNING) {
6. console.info('AudioFrameworkRecLog: AudioCapturer is in Running State');
7. }
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to start. Code: ${err.code}, message: ${err.message}`);
10. });
```

## stop8+

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止音频采集器，停止输入音频流。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止音频采集成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.stop((err: BusinessError) => {
4. if (err) {
5. console.error('Capturer stop failed');
6. } else {
7. console.info('Capturer stopped.');
8. }
9. });
```

## stop8+

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止音频采集器，停止输入音频流。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.stop().then(() => {
4. console.info('Succeeded in doing stop.');
5. if (audioCapturer.state == audio.AudioState.STATE_STOPPED){
6. console.info('AudioFrameworkRecLog: State is Stopped:');
7. }
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to stop. Code: ${err.code}, message: ${err.message}`);
10. });
```

## release8+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放音频采集器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放音频采集器成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.release((err: BusinessError) => {
4. if (err) {
5. console.error('capturer release failed');
6. } else {
7. console.info('capturer released.');
8. }
9. });
```

## release8+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放音频采集器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.release().then(() => {
4. console.info('AudioFrameworkRecLog: ---------RELEASE RECORD---------');
5. console.info('AudioFrameworkRecLog: Capturer release : SUCCESS');
6. console.info(`AudioFrameworkRecLog: AudioCapturer : STATE : ${audioCapturer.state}`);
7. }).catch((err: BusinessError) => {
8. console.error(`AudioFrameworkRecLog: Capturer stop: ERROR: ${err}`);
9. });
```

## getAudioTime8+

PhonePC/2in1TabletTVWearable

getAudioTime(callback: AsyncCallback<number>): void

获取当前录制位置的时间戳（从1970年1月1日开始），单位为纳秒。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取时间戳成功，err为undefined，data为获取到的时间戳；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getAudioTime((err: BusinessError, timestamp: number) => {
4. console.info(`Succeeded in getting audio time. Timestamp: ${timestamp}`);
5. });
```

## getAudioTime8+

PhonePC/2in1TabletTVWearable

getAudioTime(): Promise<number>

获取当前录制位置的时间戳（从1970年1月1日开始），单位为纳秒。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回时间戳（从1970年1月1日开始）。  单位为纳秒。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getAudioTime().then((timestamp: number) => {
4. console.info(`Succeeded in getting audio time. Timestamp: ${timestamp}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get audio time. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getAudioTimeSync10+

PhonePC/2in1TabletTVWearable

getAudioTimeSync(): number

获取当前录制位置的时间戳（从1970年1月1日开始），单位为纳秒。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回时间戳。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let timestamp: number = audioCapturer.getAudioTimeSync();
5. console.info(`Succeeded in getting audio time. Timestamp: ${timestamp}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get audio time. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getAudioTimestampInfo19+

PhonePC/2in1TabletTVWearable

getAudioTimestampInfo(): Promise<AudioTimestampInfo>

获取输入音频流时间戳和当前数据帧位置信息。

该接口可以获取到音频通道实际录制位置（framePos）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioTimestampInfo](arkts-apis-audio-i.md#audiotimestampinfo19)> | Promise对象，返回音频流时间戳和当前数据帧位置信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Operation not permit at current state. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
4. console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getAudioTimestampInfoSync19+

PhonePC/2in1TabletTVWearable

getAudioTimestampInfoSync(): AudioTimestampInfo

获取音频流时间戳和当前数据帧位置信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioTimestampInfo](arkts-apis-audio-i.md#audiotimestampinfo19) | 返回音频流时间戳和当前数据帧位置信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Operation not permit at current state. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let audioTimestampInfo: audio.AudioTimestampInfo = audioCapturer.getAudioTimestampInfoSync();
5. console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`ERROR: ${error}`);
9. }
```

## getBufferSize8+

PhonePC/2in1TabletTVWearable

getBufferSize(callback: AsyncCallback<number>): void

获取采集器合理的最小缓冲区大小。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取采集器合理的最小缓冲区大小成功，err为undefined，data为获取到的采集器合理的最小缓冲区大小；否则为错误对象。  单位为字节。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getBufferSize((err: BusinessError, bufferSize: number) => {
4. if (err) {
5. console.error(`Failed to get buffer size. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
8. }
9. });
```

## getBufferSize8+

PhonePC/2in1TabletTVWearable

getBufferSize(): Promise<number>

获取采集器合理的最小缓冲区大小。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回缓冲区大小。  单位为字节。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getBufferSize().then((bufferSize: number) => {
4. console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get buffer size. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getBufferSizeSync10+

PhonePC/2in1TabletTVWearable

getBufferSizeSync(): number

获取采集器合理的最小缓冲区大小。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回缓冲区大小，单位为字节。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let bufferSize = audioCapturer.getBufferSizeSync();
5. console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get buffer size. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getCurrentInputDevices11+

PhonePC/2in1TabletTVWearable

getCurrentInputDevices(): AudioDeviceDescriptors

获取录音流输入设备信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 同步接口，返回设备属性数组类型数据。 |

**示例：**

```
1. let deviceDescriptors: audio.AudioDeviceDescriptors = audioCapturer.getCurrentInputDevices();
2. console.info(`Device id: ${deviceDescriptors[0].id}`);
3. console.info(`Device type: ${deviceDescriptors[0].deviceType}`);
4. console.info(`Device role: ${deviceDescriptors[0].deviceRole}`);
5. console.info(`Device name: ${deviceDescriptors[0].name}`);
6. console.info(`Device address: ${deviceDescriptors[0].address}`);
7. console.info(`Device samplerates: ${deviceDescriptors[0].sampleRates[0]}`);
8. console.info(`Device channelcounts: ${deviceDescriptors[0].channelCounts[0]}`);
9. console.info(`Device channelmask: ${deviceDescriptors[0].channelMasks[0]}`);
10. if (deviceDescriptors[0].encodingTypes) {
11. console.info(`Device encodingTypes: ${deviceDescriptors[0].encodingTypes[0]}`);
12. }
```

## getCurrentAudioCapturerChangeInfo11+

PhonePC/2in1TabletTVWearable

getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo

获取录音流配置。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioCapturerChangeInfo](arkts-apis-audio-i.md#audiocapturerchangeinfo9) | 同步接口，返回描述音频采集器更改信息。 |

**示例：**

```
1. let info: audio.AudioCapturerChangeInfo = audioCapturer.getCurrentAudioCapturerChangeInfo();
2. console.info(`Info streamId: ${info.streamId}`);
3. console.info(`Info source: ${info.capturerInfo.source}`);
4. console.info(`Info capturerFlags: ${info.capturerInfo.capturerFlags}`);
5. console.info(`Info muted: ${info.muted}`);
6. console.info(`Info type: ${info.deviceDescriptors[0].deviceType}`);
7. console.info(`Info role: ${info.deviceDescriptors[0].deviceRole}`);
8. console.info(`Info name: ${info.deviceDescriptors[0].name}`);
9. console.info(`Info address: ${info.deviceDescriptors[0].address}`);
10. console.info(`Info samplerates: ${info.deviceDescriptors[0].sampleRates[0]}`);
11. console.info(`Info channelcounts: ${info.deviceDescriptors[0].channelCounts[0]}`);
12. console.info(`Info channelmask: ${info.deviceDescriptors[0].channelMasks[0]}`);
13. if (info.deviceDescriptors[0].encodingTypes) {
14. console.info(`Device encodingTypes: ${info.deviceDescriptors[0].encodingTypes[0]}`);
15. }
```

## on('audioInterrupt')10+

PhonePC/2in1TabletTVWearable

on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。

AudioCapturer对象在start事件时获取焦点，在pause、stop等事件时释放焦点，无需开发者主动申请。

调用此方法后，如果AudioCapturer对象获取焦点失败或发生中断事件（如被其他音频打断等），会收到[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)。建议应用根据InterruptEvent的信息进行进一步处理。更多信息请参阅文档[音频焦点介绍](../harmonyos-guides/audio-playback-concurrency.md)。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当音频焦点状态发生变化时，触发该事件。 |
| callback | Callback<[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)> | 是 | 回调函数，返回中断事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let isCapturing: boolean = false; // 标识符，表示是否正在采集。

5. audioCapturer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
6. // 在发生音频打断事件时，audioCapturer收到interruptEvent回调，此处根据其内容做相应处理。
7. // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
8. // 注意：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
9. // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
10. if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
11. // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
12. switch (interruptEvent.hintType) {
13. case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
14. // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
15. console.info('Force paused. Update capturing status and stop reading');
16. isCapturing = false; // 简化处理，代表应用切换至暂停状态的若干操作。
17. break;
18. case audio.InterruptHint.INTERRUPT_HINT_STOP:
19. // 音频流已被停止，永久失去焦点，若想恢复采集，需用户主动触发。
20. console.info('Force stopped. Update capturing status and stop reading');
21. isCapturing = false; // 简化处理，代表应用切换至暂停状态的若干操作。
22. break;
23. default:
24. console.info('Invalid interruptEvent');
25. break;
26. }
27. } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
28. // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
29. switch (interruptEvent.hintType) {
30. case audio.InterruptHint.INTERRUPT_HINT_RESUME:
31. // 建议应用继续采集（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复采集）。
32. // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
33. console.info('Resume force paused renderer or ignore');
34. // 若选择继续采集，需在此处主动执行开始采集的若干操作。
35. break;
36. default:
37. console.info('Invalid interruptEvent');
38. break;
39. }
40. }
41. });
```

## off('audioInterrupt')10+

PhonePC/2in1TabletTVWearable

off(type: 'audioInterrupt'): void

取消监听音频中断事件。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当取消监听音频中断事件时，触发该事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioCapturer.off('audioInterrupt');
```

## on('inputDeviceChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void

监听音频输入设备变化事件（当音频输入设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'inputDeviceChange'，当音频输入设备发生变化时，触发该事件。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) > | 是 | 回调函数，返回变化后的音频输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioCapturer.on('inputDeviceChange', (deviceChangeInfo: audio.AudioDeviceDescriptors) => {
2. console.info(`inputDevice id: ${deviceChangeInfo[0].id}`);
3. console.info(`inputDevice deviceRole: ${deviceChangeInfo[0].deviceRole}`);
4. console.info(`inputDevice deviceType: ${deviceChangeInfo[0].deviceType}`);
5. });
```

## off('inputDeviceChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void

取消监听音频输入设备更改事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'inputDeviceChange'，当取消监听音频输入设备更改事件时，触发该事件。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) > | 否 | 回调函数，返回音频输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioCapturer.off('inputDeviceChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let inputDeviceChangeCallback = (deviceChangeInfo: audio.AudioDeviceDescriptors) => {
6. console.info(`inputDevice id: ${deviceChangeInfo[0].id}`);
7. console.info(`inputDevice deviceRole: ${deviceChangeInfo[0].deviceRole}`);
8. console.info(`inputDevice deviceType: ${deviceChangeInfo[0].deviceType}`);
9. };

11. audioCapturer.on('inputDeviceChange', inputDeviceChangeCallback);

13. audioCapturer.off('inputDeviceChange', inputDeviceChangeCallback);
```

## on('audioCapturerChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void

监听录音流配置变化事件（当音频录制流状态变化、设备变化时触发）。使用callback异步回调。订阅内部是异步实现，是非精确回调，在录音流配置变化的同时注册回调，收到的返回结果存在变化可能性。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioCapturerChange'，当音频录制流状态变化、设备变化时，触发该事件。 |
| callback | Callback<[AudioCapturerChangeInfo](arkts-apis-audio-i.md#audiocapturerchangeinfo9)> | 是 | 回调函数，录音流配置或状态变化时返回监听的录音流当前配置和状态信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioCapturer.on('audioCapturerChange', (capturerChangeInfo: audio.AudioCapturerChangeInfo) => {
2. console.info(`Succeeded in using on function, AudioCapturerChangeInfo: ${capturerChangeInfo}.`);
3. });
```

## off('audioCapturerChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void

取消监听录音流配置变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioCapturerChange'，当取消监听录音流配置变化事件时，触发该事件。 |
| callback | Callback<[AudioCapturerChangeInfo](arkts-apis-audio-i.md#audiocapturerchangeinfo9)> | 否 | 回调函数，返回取消监听的录音流配置或状态变化。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioCapturer.off('audioCapturerChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let audioCapturerChangeCallback = (capturerChangeInfo: audio.AudioCapturerChangeInfo) => {
6. console.info(`Succeeded in using on or off function, AudioCapturerChangeInfo: ${capturerChangeInfo}.`);
7. };

9. audioCapturer.on('audioCapturerChange', audioCapturerChangeCallback);

11. audioCapturer.off('audioCapturerChange', audioCapturerChangeCallback);
```

## on('markReach')8+

PhonePC/2in1TabletTVWearable

on(type: 'markReach', frame: number, callback: Callback<number>): void

监听标记到达事件（当采集的帧数达到frame参数的值时触发，仅调用一次）。使用callback异步回调。

如果将frame设置为100，当采集帧数到达第100帧时，系统将上报信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'markReach'，当采集的帧数达到frame参数的值时，触发该事件。 |
| frame | number | 是 | 触发事件的帧数。该值必须大于0。 |
| callback | Callback<number> | 是 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. audioCapturer.on('markReach', 1000, (position: number) => {
2. if (position == 1000) {
3. console.info('ON Triggered successfully');
4. }
5. });
```

## off('markReach')8+

PhonePC/2in1TabletTVWearable

off(type: 'markReach', callback?: Callback<number>): void

取消监听标记到达事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'markReach'，当取消监听标记到达事件时，触发该事件。 |
| callback18+ | Callback<number> | 否 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioCapturer.off('markReach');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let markReachCallback = (position: number) => {
6. if (position == 1000) {
7. console.info('ON Triggered successfully');
8. }
9. };

11. audioCapturer.on('markReach', 1000, markReachCallback);

13. audioCapturer.off('markReach', markReachCallback);
```

## on('periodReach')8+

PhonePC/2in1TabletTVWearable

on(type: 'periodReach', frame: number, callback: Callback<number>): void

监听标记到达事件（当采集的帧数达到frame参数的值时触发，即按周期上报信息）。使用callback异步回调。

如果将frame设置为10，每渲染10帧数据均会上报信息（例如：第10帧、第20帧、第30帧......）。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'periodReach'，当采集的帧数达到frame参数的值时，触发该事件。 |
| frame | number | 是 | 触发事件的帧数。该值必须大于0。 |
| callback | Callback<number> | 是 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. audioCapturer.on('periodReach', 1000, (position: number) => {
2. if (position == 1000) {
3. console.info('ON Triggered successfully');
4. }
5. });
```

## off('periodReach')8+

PhonePC/2in1TabletTVWearable

off(type: 'periodReach', callback?: Callback<number>): void

取消监听标记到达事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'periodReach'，当取消监听标记到达事件时，触发该事件。 |
| callback18+ | Callback<number> | 否 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioCapturer.off('periodReach');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let periodReachCallback = (position: number) => {
6. if (position == 1000) {
7. console.info('ON Triggered successfully');
8. }
9. };

11. audioCapturer.on('periodReach', 1000, periodReachCallback);

13. audioCapturer.off('periodReach', periodReachCallback);
```

## on('stateChange')8+

PhonePC/2in1TabletTVWearable

on(type: 'stateChange', callback: Callback<AudioState>): void

监听状态变化事件（当AudioCapturer状态发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当AudioCapturer状态发生变化时，触发该事件。 |
| callback | Callback<[AudioState](arkts-apis-audio-e.md#audiostate8)> | 是 | 回调函数，返回当前音频的状态。 |

**示例：**

```
1. audioCapturer.on('stateChange', (state: audio.AudioState) => {
2. if (state == 1) {
3. console.info('audio capturer state is: STATE_PREPARED');
4. }
5. if (state == 2) {
6. console.info('audio capturer state is: STATE_RUNNING');
7. }
8. });
```

## off('stateChange')18+

PhonePC/2in1TabletTVWearable

off(type: 'stateChange', callback?: Callback<AudioState>): void

取消监听状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当取消监听状态变化事件时，触发该事件。 |
| callback | Callback<[AudioState](arkts-apis-audio-e.md#audiostate8)> | 否 | 回调函数，返回当前音频的状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioCapturer.off('stateChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let stateChangeCallback = (state: audio.AudioState) => {
6. if (state == 1) {
7. console.info('audio renderer state is: STATE_PREPARED');
8. }
9. if (state == 2) {
10. console.info('audio renderer state is: STATE_RUNNING');
11. }
12. };

14. audioCapturer.on('stateChange', stateChangeCallback);

16. audioCapturer.off('stateChange', stateChangeCallback);
```

## on('readData')11+

PhonePC/2in1TabletTVWearable

on(type: 'readData', callback: Callback<ArrayBuffer>): void

监听音频数据读取回调事件（当需要读取音频流数据时触发）。使用callback异步回调。

回调函数仅用来读取音频数据，请勿在回调函数中调用AudioCapturer相关接口。

为了消除麦克风硬件设计带来的上电杂音，通常会对录音启动后的前100ms数据进行静音。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readData'，当需要读取音频流数据时，触发该事件。 |
| callback | Callback<ArrayBuffer> | 是 | 回调函数，返回读到的数据缓冲区。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. class Options {
6. offset?: number;
7. length?: number;
8. }

10. let bufferSize: number = 0;
11. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
12. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. let path = context.cacheDir;
14. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
15. let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
16. let readDataCallback = (buffer: ArrayBuffer) => {
17. let options: Options = {
18. offset: bufferSize,
19. length: buffer.byteLength
20. };
21. fs.writeSync(file.fd, buffer, options);
22. bufferSize += buffer.byteLength;
23. }

25. audioCapturer.on('readData', readDataCallback);

27. audioCapturer.start((err: BusinessError) => {
28. if (err) {
29. console.error('Capturer start failed.');
30. } else {
31. console.info('Capturer start success.');
32. }
33. });
```

## off('readData')11+

PhonePC/2in1TabletTVWearable

off(type: 'readData', callback?: Callback<ArrayBuffer>): void

取消监听音频数据读取回调事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readData'，当取消监听音频数据读取回调事件时，触发该事件。 |
| callback | Callback<ArrayBuffer> | 否 | 回调函数，返回读到的数据缓冲区。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioCapturer.off('readData');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let readDataCallback = (data: ArrayBuffer) => {
6. console.info(`read data: ${data}`);
7. };

9. audioCapturer.on('readData', readDataCallback);

11. audioCapturer.off('readData', readDataCallback);
```

## getOverflowCount12+

PhonePC/2in1TabletTVWearable

getOverflowCount(): Promise<number>

获取当前录制音频流的过载音频帧数量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回音频流的过载音频帧数量。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getOverflowCount().then((value: number) => {
4. console.info(`Get overflow count Success! ${value}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Get overflow count Fail: ${err}`);
7. });
```

## getOverflowCountSync12+

PhonePC/2in1TabletTVWearable

getOverflowCountSync(): number

获取当前录制音频流的过载音频帧数量。同步返回数据。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音频流的过载音频帧数量。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: number = audioCapturer.getOverflowCountSync();
5. console.info(`Get overflow count Success! ${value}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Get overflow count Fail: ${error}`);
9. }
```

## setWillMuteWhenInterrupted20+

PhonePC/2in1TabletTVWearable

setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>

设置当前录制音频流是否启用[静音打断模式](../harmonyos-guides/using-audiocapturer-for-recording.md#设置静音打断模式)。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| muteWhenInterrupted | boolean | 是 | 设置当前录制音频流是否启用静音打断模式, true表示启用，false表示不启用，保持为默认打断模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Operation not permitted at current state. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.setWillMuteWhenInterrupted(true).then(() => {
4. console.info('setWillMuteWhenInterrupted Success!');
5. }).catch((err: BusinessError) => {
6. console.error(`setWillMuteWhenInterrupted Fail: ${err}`);
7. });
```

## read(deprecated)

PhonePC/2in1TabletTVWearable

read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void

读入缓冲区。使用callback异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[on('readData')](arkts-apis-audio-audiocapturer.md#onreaddata11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 读入的字节数。 |
| isBlockingRead | boolean | 是 | 是否阻塞读操作。true表示阻塞，false表示不阻塞。 |
| callback | AsyncCallback<ArrayBuffer> | 是 | 回调函数。当读入缓冲区成功，err为undefined，data为获取到的缓冲区；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getBufferSize().then((bufferSize: number) => {
4. console.info('Succeeded in doing getBufferSize.');
5. audioCapturer.read(bufferSize, true, (err: BusinessError, buffer: ArrayBuffer) => {
6. if (err) {
7. console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in doing read.');
11. });
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to getBufferSize. Code: ${err.code}, message: ${err.message}`);
14. });
```

## read(deprecated)

PhonePC/2in1TabletTVWearable

read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>

读入缓冲区。使用Promise异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[on('readData')](arkts-apis-audio-audiocapturer.md#onreaddata11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 读入的字节数。 |
| isBlockingRead | boolean | 是 | 是否阻塞读操作。true表示阻塞，false表示不阻塞。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回读取的缓冲区数据。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioCapturer.getBufferSize().then((bufferSize: number) => {
4. console.info('Succeeded in doing getBufferSize.');
5. audioCapturer.read(bufferSize, true).then((buffer: ArrayBuffer) => {
6. console.info('Succeeded in doing read.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
9. });
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to getBufferSize. Code: ${err.code}, message: ${err.message}`);
12. });
```
