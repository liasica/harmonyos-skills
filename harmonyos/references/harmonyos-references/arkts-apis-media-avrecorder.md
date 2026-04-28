---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder
title: Interface (AVRecorder)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Interface (AVRecorder)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b3dad6f719ee17f0501ef991bf8403c214a20276b7b1ea2b00a645f9093e868
---

音视频录制管理类，用于音视频媒体录制。在调用AVRecorder的方法前，需要先调用[createAVRecorder](arkts-apis-media-f.md#mediacreateavrecorder9)接口构建一个AVRecorder实例。

音视频录制demo可参考：[音频录制开发指导](../harmonyos-guides/using-avrecorder-for-recording.md)、[视频录制开发指导](../harmonyos-guides/video-recording.md)。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。
* 相机视频录制功能需配合相机模块使用，相机模块接口的使用详情请参考[相机管理](arkts-apis-camera.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state9+ | [AVRecorderState](arkts-apis-media-t.md#avrecorderstate9) | 是 | 否 | 音视频录制的状态。  **元服务API：** 从API version 12 开始，该接口支持在元服务中使用。 |

## prepare9+

PhonePC/2in1TabletTVWearable

prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void

音视频录制的参数设置。使用callback异步回调。

**需要权限：** ohos.permission.MICROPHONE

不涉及音频录制时，无需获取ohos.permission.MICROPHONE权限。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AVRecorderConfig](arkts-apis-media-i.md#avrecorderconfig9) | 是 | 配置音视频录制的相关参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当prepare接口成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Return by callback. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operate not permit. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 配置参数以实际硬件设备支持的范围为准。
4. let avRecorderProfile: media.AVRecorderProfile = {
5. audioBitrate : 48000,
6. audioChannels : 2,
7. audioCodec : media.CodecMimeType.AUDIO_AAC,
8. audioSampleRate : 48000,
9. fileFormat : media.ContainerFormatType.CFT_MPEG_4,
10. videoBitrate : 2000000,
11. videoCodec : media.CodecMimeType.VIDEO_AVC,
12. videoFrameWidth : 640,
13. videoFrameHeight : 480,
14. videoFrameRate : 30
15. };
16. let videoMetaData: media.AVMetadata = {
17. videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
18. };
19. let avRecorderConfig: media.AVRecorderConfig = {
20. audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
21. videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
22. profile : avRecorderProfile,
23. url : 'fd://', // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数，eg.fd://45
24. metadata: videoMetaData,
25. location : { latitude : 30, longitude : 130 }
26. };

28. avRecorder.prepare(avRecorderConfig, (err: BusinessError) => {
29. if (err) {
30. console.error(`Failed to prepare and error is: Code: ${err.code}, message: ${err.message}`);
31. } else {
32. console.info('Succeeded in preparing');
33. }
34. });
```

## prepare9+

PhonePC/2in1TabletTVWearable

prepare(config: AVRecorderConfig): Promise<void>

音视频录制的参数设置。使用Promise异步回调。

**需要权限：** ohos.permission.MICROPHONE

不涉及音频录制时，无需获取ohos.permission.MICROPHONE权限。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AVRecorderConfig](arkts-apis-media-i.md#avrecorderconfig9) | 是 | 配置音视频录制的相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Return by promise. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operate not permit. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 配置参数以实际硬件设备支持的范围为准。
4. let avRecorderProfile: media.AVRecorderProfile = {
5. audioBitrate : 48000,
6. audioChannels : 2,
7. audioCodec : media.CodecMimeType.AUDIO_AAC,
8. audioSampleRate : 48000,
9. fileFormat : media.ContainerFormatType.CFT_MPEG_4,
10. videoBitrate : 2000000,
11. videoCodec : media.CodecMimeType.VIDEO_AVC,
12. videoFrameWidth : 640,
13. videoFrameHeight : 480,
14. videoFrameRate : 30
15. };
16. let videoMetaData: media.AVMetadata = {
17. videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
18. };
19. let avRecorderConfig: media.AVRecorderConfig = {
20. audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
21. videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
22. profile : avRecorderProfile,
23. url : 'fd://',  // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数，eg.fd://45
24. metadata : videoMetaData,
25. location : { latitude : 30, longitude : 130 }
26. };

28. avRecorder.prepare(avRecorderConfig).then(() => {
29. console.info('Succeeded in preparing');
30. }).catch((err: Error) => {
31. let error: BusinessError = err as BusinessError;
32. console.error(`Failed to prepare and error is: Code: ${error.code}, message: ${error.message}`);
33. });
```

## getInputSurface9+

PhonePC/2in1TabletTVWearable

getInputSurface(callback: AsyncCallback<string>): void

获得录制需要的surface。使用callback异步回调。

开发者从此surface中获取surfaceBuffer，填入相应的视频数据。

应当注意，填入的视频数据需要携带时间戳（单位ns）和buffersize。时间戳的起始时间请以系统启动时间为基准。

需在[prepare](arkts-apis-media-avrecorder.md#prepare9)接口成功调用后，才能调用getInputSurface接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取surface成功，err为undefined，data为获取到的surfaceId，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let surfaceID: string; // 该surfaceID用于传递给相机接口创建videoOutput。

5. avRecorder.getInputSurface((err: BusinessError, surfaceId: string) => {
6. if (err) {
7. console.error(`Failed to do getInputSurface and error is: Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info('Succeeded in doing getInputSurface');
10. surfaceID = surfaceId;
11. }
12. });
```

## getInputSurface9+

PhonePC/2in1TabletTVWearable

getInputSurface(): Promise<string>

获得录制需要的surface。使用Promise异步回调。

开发者从此surface中获取surfaceBuffer，填入相应的视频数据。

应当注意，填入的视频数据需要携带时间戳（单位ns）和buffersize。时间戳的起始时间请以系统启动时间为基准。

需在[prepare](arkts-apis-media-avrecorder.md#prepare9-1)接口成功调用后，才能调用getInputSurface接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回surface中获取的surfaceBuffer。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let surfaceID: string; // 该surfaceID用于传递给相机接口创建videoOutput。

5. avRecorder.getInputSurface().then((surfaceId: string) => {
6. console.info('Succeeded in getting InputSurface');
7. surfaceID = surfaceId;
8. }).catch((err: Error) => {
9. let error: BusinessError = err as BusinessError;
10. console.error(`Failed to get InputSurface and error is: Code: ${error.code}, message: ${error.message}`);
11. });
```

## updateRotation12+

PhonePC/2in1TabletTVWearable

updateRotation(rotation: number): Promise<void>

更新视频旋转角度。使用Promise异步回调。

当且仅当[prepare](arkts-apis-media-avrecorder.md#prepare9-1)接口成功调用后，且在[start](arkts-apis-media-avrecorder.md#start9)接口之前，才能调用updateRotation接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | number | 是 | 旋转角度，取值仅支持0、90、180、270度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let rotation = 90;

5. avRecorder.updateRotation(rotation).then(() => {
6. console.info('Succeeded in doing updateRotation');
7. }).catch((err: Error) => {
8. let error: BusinessError = err as BusinessError;
9. console.error(`Failed to do updateRotation and error is: Code: ${error.code}, message: ${error.message}`);
10. });
```

## setWillMuteWhenInterrupted20+

PhonePC/2in1TabletTVWearable

setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>

设置当前录制音频流是否启用静音打断模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| muteWhenInterrupted | boolean | 是 | 设置当前录制音频流是否启用静音打断模式, true表示启用，false表示不启用，保持为默认打断模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.setWillMuteWhenInterrupted(true).then(() => {
4. console.info('Succeeded in doing setWillMuteWhenInterrupted');
5. }).catch((err: Error) => {
6. let error: BusinessError = err as BusinessError;
7. console.error(`Failed to do setWillMuteWhenInterrupted and error is: Code: ${error.code}, message: ${error.message}`);
8. });
```

## start9+

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

开始视频录制。使用callback异步回调。

纯音频录制需在[prepare](arkts-apis-media-avrecorder.md#prepare9)接口成功调用后，才能调用start接口。纯视频录制，音视频录制需在[getInputSurface](arkts-apis-media-avrecorder.md#getinputsurface9)接口成功调用后，才能调用start接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当开始录制视频成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.start((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to start AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info('Succeeded in starting AVRecorder');
8. }
9. });
```

## start9+

PhonePC/2in1TabletTVWearable

start(): Promise<void>

开始视频录制。使用Promise异步回调。

纯音频录制需在[prepare](arkts-apis-media-avrecorder.md#prepare9-1)接口成功调用后，才能调用start接口。纯视频录制，音视频录制需在[getInputSurface](arkts-apis-media-avrecorder.md#getinputsurface9-1)接口成功调用后，才能调用start接口。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.start().then(() => {
4. console.info('Succeeded in starting AVRecorder');
5. }).catch((err: Error) => {
6. let error: BusinessError = err as BusinessError;
7. console.error(`Failed to start AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
8. });
```

## pause9+

PhonePC/2in1TabletTVWearable

pause(callback: AsyncCallback<void>): void

暂停视频录制。使用callback异步回调。

需要[start](arkts-apis-media-avrecorder.md#start9)接口成功调用后，才能调用pause接口，可以通过调用[resume](arkts-apis-media-avrecorder.md#resume9)接口来恢复录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当暂停视频录制成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.pause((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to pause AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info('Succeeded in pausing');
8. }
9. });
```

## pause9+

PhonePC/2in1TabletTVWearable

pause(): Promise<void>

暂停视频录制。使用Promise异步回调。

需要[start](arkts-apis-media-avrecorder.md#start9-1)接口成功调用后，才能调用pause接口，可以通过调用[resume](arkts-apis-media-avrecorder.md#resume9-1)接口来恢复录制。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.pause().then(() => {
4. console.info('Succeeded in pausing');
5. }).catch((err: Error) => {
6. let error: BusinessError = err as BusinessError;
7. console.error(`Failed to pause AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
8. });
```

## resume9+

PhonePC/2in1TabletTVWearable

resume(callback: AsyncCallback<void>): void

恢复视频录制。使用callback异步回调。

需要在[pause](arkts-apis-media-avrecorder.md#pause9)接口成功调用后，才能调用resume接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当恢复视频录制成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.resume((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to resume AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info('Succeeded in resuming AVRecorder');
8. }
9. });
```

## resume9+

PhonePC/2in1TabletTVWearable

resume(): Promise<void>

恢复视频录制。使用Promise异步回调。

需要在[pause](arkts-apis-media-avrecorder.md#pause9-1)接口成功调用后，才能调用resume接口。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.resume().then(() => {
4. console.info('Succeeded in resuming AVRecorder');
5. }).catch((err: Error) => {
6. let error: BusinessError = err as BusinessError;
7. console.error(`Failed to resume AVRecorder failed and error is: Code: ${error.code}, message: ${error.message}`);
8. });
```

## stop9+

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止视频录制。使用callback异步回调。

需要在[start](arkts-apis-media-avrecorder.md#start9)或[pause](arkts-apis-media-avrecorder.md#pause9)接口成功调用后，才能调用stop接口。

纯音频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9)和[getInputSurface](arkts-apis-media-avrecorder.md#getinputsurface9)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止视频录制成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.stop((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to stop AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info('Succeeded in stopping AVRecorder');
8. }
9. });
```

## stop9+

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止视频录制。使用Promise异步回调。

需要在[start](arkts-apis-media-avrecorder.md#start9-1)或[pause](arkts-apis-media-avrecorder.md#pause9-1)接口成功调用后，才能调用stop接口。

纯音频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9-1)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9-1)和[getInputSurface](arkts-apis-media-avrecorder.md#getinputsurface9-1)接口才能重新录制。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.stop().then(() => {
4. console.info('Succeeded in stopping AVRecorder');
5. }).catch((err: Error) => {
6. let error: BusinessError = err as BusinessError;
7. console.error(`Failed to stop AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
8. });
```

## reset9+

PhonePC/2in1TabletTVWearable

reset(callback: AsyncCallback<void>): void

重置音视频录制。使用callback异步回调。

纯音频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9)和[getInputSurface](arkts-apis-media-avrecorder.md#getinputsurface9)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当重置音视频录制成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.reset((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to reset AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info('Succeeded in resetting AVRecorder');
8. }
9. });
```

## reset9+

PhonePC/2in1TabletTVWearable

reset(): Promise<void>

重置音视频录制。使用Promise异步回调。

纯音频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9-1)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](arkts-apis-media-avrecorder.md#prepare9-1)和[getInputSurface](arkts-apis-media-avrecorder.md#getinputsurface9-1)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.reset().then(() => {
4. console.info('Succeeded in resetting AVRecorder');
5. }).catch((err: Error) => {
6. let error: BusinessError = err as BusinessError;
7. console.error(`Failed to reset AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
8. });
```

## release9+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放音视频录制资源。使用callback异步回调。

释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放音视频录制资源成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.release((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to release AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info('Succeeded in releasing AVRecorder');
8. }
9. });
```

## release9+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放音视频录制资源。使用Promise异步回调。

释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.release().then(() => {
4. console.info('Succeeded in releasing AVRecorder');
5. }).catch((err: Error) => {
6. let error: BusinessError = err as BusinessError;
7. console.error(`Failed to release AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
8. });
```

## getCurrentAudioCapturerInfo11+

PhonePC/2in1TabletTVWearable

getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void

获取当前音频采集参数。使用callback异步回调。

在[prepare](arkts-apis-media-avrecorder.md#prepare9)接口成功调用后，才能调用此接口。在[stop](arkts-apis-media-avrecorder.md#stop9)接口成功调用后，调用此接口会报错。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[audio.AudioCapturerChangeInfo](arkts-apis-audio-i.md#audiocapturerchangeinfo9)> | 是 | 回调函数。当获取音频采集参数成功时，err为undefined，data为获取到的audio.AudioCapturerChangeInfo，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400105 | Service died. Return by callback. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { audio } from '@kit.AudioKit';

4. let currentCapturerInfo: audio.AudioCapturerChangeInfo;

6. avRecorder.getCurrentAudioCapturerInfo((err: BusinessError, capturerInfo: audio.AudioCapturerChangeInfo) => {
7. if (err) {
8. console.error(`Failed to get CurrentAudioCapturerInfo and error is: Code: ${err.code}, message: ${err.message}`);
9. } else {
10. console.info('Succeeded in getting CurrentAudioCapturerInfo');
11. currentCapturerInfo = capturerInfo;
12. }
13. });
```

## getCurrentAudioCapturerInfo11+

PhonePC/2in1TabletTVWearable

getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>

获取当前音频采集参数。使用Promise异步回调。

在[prepare](arkts-apis-media-avrecorder.md#prepare9)接口成功调用后，才能调用此接口。在[stop](arkts-apis-media-avrecorder.md#stop9)接口成功调用后，调用此接口会报错。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[audio.AudioCapturerChangeInfo](arkts-apis-audio-i.md#audiocapturerchangeinfo9)> | Promise对象，返回获取的当前音频采集参数。 |

**错误码**：

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400105 | Service died. Return by promise. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { audio } from '@kit.AudioKit';

4. let currentCapturerInfo: audio.AudioCapturerChangeInfo;

6. avRecorder.getCurrentAudioCapturerInfo().then((capturerInfo: audio.AudioCapturerChangeInfo) => {
7. console.info('Succeeded in getting CurrentAudioCapturerInfo');
8. currentCapturerInfo = capturerInfo;
9. }).catch((err: Error) => {
10. let error: BusinessError = err as BusinessError;
11. console.error(`Failed to get CurrentAudioCapturerInfo and error is: Code: ${error.code}, message: ${error.message}`);
12. });
```

## getAudioCapturerMaxAmplitude11+

PhonePC/2in1TabletTVWearable

getAudioCapturerMaxAmplitude(callback: AsyncCallback<number>): void

获取当前音频最大振幅。使用callback异步回调。

在[prepare](arkts-apis-media-avrecorder.md#prepare9)接口成功调用后，才能调用此接口。在[stop](arkts-apis-media-avrecorder.md#stop9)接口成功调用后，调用此接口会报错。

调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间里面的最大值。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。获取当前音频最大振幅成功时，err为undefined，data为获取到的最大振幅，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by callback. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let maxAmplitude: number;

5. avRecorder.getAudioCapturerMaxAmplitude((err: BusinessError, amplitude: number) => {
6. if (err) {
7. console.error(`Failed to get AudioCapturerMaxAmplitude and error is: Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info('Succeeded in getting AudioCapturerMaxAmplitude');
10. maxAmplitude = amplitude;
11. }
12. });
```

## getAudioCapturerMaxAmplitude11+

PhonePC/2in1TabletTVWearable

getAudioCapturerMaxAmplitude(): Promise<number>

获取当前音频最大振幅。使用Promise异步回调。

在[prepare](arkts-apis-media-avrecorder.md#prepare9)接口成功调用后，才能调用此接口。在[stop](arkts-apis-media-avrecorder.md#stop9)接口成功调用后，调用此接口会报错。

调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间里面的最大值。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回获取的当前音频最大振幅。 |

**错误码**：

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by promise. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let maxAmplitude: number;

5. avRecorder.getAudioCapturerMaxAmplitude().then((amplitude: number) => {
6. console.info('Succeeded in getting AudioCapturerMaxAmplitude');
7. maxAmplitude = amplitude;
8. }).catch((err: Error) => {
9. let error: BusinessError = err as BusinessError;
10. console.error(`Failed to get AudioCapturerMaxAmplitude and error is: Code: ${error.code}, message: ${error.message}`);
11. });
```

## getAvailableEncoder11+

PhonePC/2in1TabletTVWearable

getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void

获取可用的编码器参数。使用callback异步回调。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[EncoderInfo](arkts-apis-media-i.md#encoderinfo11)>> | 是 | 回调函数。获取可用的编码器参数成功时，err为undefined，data为获取到的编码器参数，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by callback. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let encoderInfo: media.EncoderInfo;

5. avRecorder.getAvailableEncoder((err: BusinessError, info: media.EncoderInfo[]) => {
6. if (err) {
7. console.error(`Failed to get AvailableEncoder and error is: Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info('Succeeded in getting AvailableEncoder');
10. if (info.length > 0) {
11. encoderInfo = info[0];
12. } else {
13. console.error('No available encoder');
14. }
15. }
16. });
```

## getAvailableEncoder11+

PhonePC/2in1TabletTVWearable

getAvailableEncoder(): Promise<Array<EncoderInfo>>

获取可用的编码器参数。使用Promise异步回调。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[EncoderInfo](arkts-apis-media-i.md#encoderinfo11)>> | Promise对象，返回获取的可用的编码器参数。 |

**错误码**：

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by promise. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let encoderInfo: media.EncoderInfo;

5. avRecorder.getAvailableEncoder().then((info: media.EncoderInfo[]) => {
6. console.info('Succeeded in getting AvailableEncoder');
7. if (info.length > 0) {
8. encoderInfo = info[0];
9. } else {
10. console.error('No available encoder');
11. }
12. }).catch((err: Error) => {
13. let error: BusinessError = err as BusinessError;
14. console.error(`Failed to get AvailableEncoder and error is: Code: ${error.code}, message: ${error.message}`);
15. });
```

## getAVRecorderConfig11+

PhonePC/2in1TabletTVWearable

getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void

获取实时的配置参数。使用callback异步回调。

只能在[prepare](arkts-apis-media-avrecorder.md#prepare9)接口调用成功后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVRecorderConfig](arkts-apis-media-i.md#avrecorderconfig9)> | 是 | 回调函数。获取实时配置的参数成功时，err为undefined，data为获取到的配置参数，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avConfig: media.AVRecorderConfig;

5. avRecorder.getAVRecorderConfig((err: BusinessError, config: media.AVRecorderConfig) => {
6. if (err) {
7. console.error(`Failed to get avConfig and error is: Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info('Succeeded in getting AVRecorderConfig');
10. avConfig = config;
11. }
12. });
```

## getAVRecorderConfig11+

PhonePC/2in1TabletTVWearable

getAVRecorderConfig(): Promise<AVRecorderConfig>;

获取实时的配置参数。使用Promise异步回调。

只能在[prepare](arkts-apis-media-avrecorder.md#prepare9-1)接口调用成功后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVRecorderConfig](arkts-apis-media-i.md#avrecorderconfig9)> | Promise对象。返回实时配置参数。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avConfig: media.AVRecorderConfig;

5. avRecorder.getAVRecorderConfig().then((config: media.AVRecorderConfig) => {
6. console.info('Succeeded in getting AVRecorderConfig');
7. avConfig = config;
8. }).catch((err: Error) => {
9. let error: BusinessError = err as BusinessError;
10. console.error(`Failed to get AVRecorderConfig and error is: Code: ${error.code}, message: ${error.message}`);
11. });
```

## on('stateChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void

订阅录制状态机AVRecorderState切换的事件，当AVRecorderState状态机发生变化时，会通过订阅的回调方法通知用户。用户只能订阅一个录制状态机切换事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制状态机切换事件回调类型，支持的事件：'stateChange'，用户操作和系统都会触发此事件。 |
| callback | [OnAVRecorderStateChangeHandler](arkts-apis-media-t.md#onavrecorderstatechangehandler12) | 是 | 回调函数，返回录制状态机切换事件。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. avRecorder.on('stateChange', async (state: media.AVRecorderState, reason: media.StateChangeReason) => {
2. console.info('case state has changed, new state is: ' + state + ', and reason is: ' + reason);
3. });
```

## off('stateChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void

取消订阅录制状态机[AVRecorderState](arkts-apis-media-t.md#avrecorderstate9)切换的事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制状态机切换事件回调类型，支持的事件：'stateChange'，用户操作和系统都会触发此事件。 |
| callback12+ | [OnAVRecorderStateChangeHandler](arkts-apis-media-t.md#onavrecorderstatechangehandler12) | 否 | 回调函数，返回录制状态机切换事件。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。  从API version 12开始支持此参数。 |

**示例：**

```
1. avRecorder.off('stateChange');
```

## on('error')9+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅AVRecorder的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。如果此时[AVRecorderState](arkts-apis-media-t.md#avrecorderstate9)也切换至error状态，用户需要通过[reset](arkts-apis-media-avrecorder.md#reset9)或者[release](arkts-apis-media-avrecorder.md#release9)接口退出录制操作。使用callback异步回调。

用户只能订阅一个错误事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制错误事件回调类型'error'。  - 'error'：录制过程中发生错误，触发该事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，返回录制错误事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupported format. |
| 5400107 | Audio interrupted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avRecorder.on('error', (err: BusinessError) => {
4. console.error(`case avRecorder.on(error) called. Code: ${err.code}, message: ${err.message}`);
5. });
```

## off('error')9+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅录制错误事件，取消后不再接收到AVRecorder的错误事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制错误事件回调类型'error'。  - 'error'：录制过程中发生错误，触发该事件。 |
| callback12+ | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，返回录制错误事件。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。  从API version 12开始支持此参数。 |

**示例：**

```
1. avRecorder.off('error');
```

## on('audioCapturerChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void

订阅录音配置变化的回调，任意录音配置的变化会触发变化后的录音配置全量信息回调。使用callback异步回调。

当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录音配置变化的回调类型，支持的事件：'audioCapturerChange'。 |
| callback | Callback<[audio.AudioCapturerChangeInfo](arkts-apis-audio-i.md#audiocapturerchangeinfo9)> | 是 | 回调函数，返回变化后的录音配置全量信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. import { audio } from '@kit.AudioKit'

3. let capturerChangeInfo: audio.AudioCapturerChangeInfo;

5. avRecorder.on('audioCapturerChange',  (audioCapturerChangeInfo: audio.AudioCapturerChangeInfo) => {
6. console.info('audioCapturerChange called');
7. capturerChangeInfo = audioCapturerChangeInfo;
8. });
```

## off('audioCapturerChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void

取消订阅录音变化的回调事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录音配置变化的回调类型，支持的事件：'audioCapturerChange'。 |
| callback12+ | Callback<[audio.AudioCapturerChangeInfo](arkts-apis-audio-i.md#audiocapturerchangeinfo9)> | 否 | 回调函数，返回变化后的录音配置全量信息。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。  从API version 12开始支持此参数。 |

**示例：**

```
1. avRecorder.off('audioCapturerChange');
```

## on('photoAssetAvailable')12+

PhonePC/2in1TabletTVWearable

on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void

订阅媒体资源回调事件，当[FileGenerationMode](arkts-apis-media-e.md#filegenerationmode12)枚举设置为系统创建媒体文件时，会在[stop](arkts-apis-media-avrecorder.md#stop9)操作结束后把[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)对象回调给应用。使用callback异步回调。

当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录像资源的回调类型，支持的事件：'photoAssetAvailable'。 |
| callback | Callback<[photoAccessHelper.PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 回调函数，返回系统创建的资源文件对应的PhotoAsset对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. let photoAsset: photoAccessHelper.PhotoAsset;

4. // 例：处理photoAsset回调，保存video。
5. async function saveVideo(context: Context, asset: photoAccessHelper.PhotoAsset) {
6. console.info("saveVideo called");
7. try {
8. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
9. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
10. assetChangeRequest.saveCameraPhoto();
11. await phAccessHelper.applyChanges(assetChangeRequest);
12. console.info('apply saveVideo successfully');
13. } catch (err) {
14. console.error(`apply saveVideo failed with error: ${err.code}, ${err.message}`);
15. }
16. }
17. // 注册photoAsset监听。
18. avRecorder.on('photoAssetAvailable', (asset: photoAccessHelper.PhotoAsset) => {
19. console.info('photoAssetAvailable called');
20. if (asset != undefined) {
21. photoAsset = asset;
22. // 处理photoAsset回调。
23. // 例：this.saveVideo(context, asset);
24. } else {
25. console.error('photoAsset is undefined');
26. }
27. });
```

## off('photoAssetAvailable')12+

PhonePC/2in1TabletTVWearable

off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void

取消订阅媒体资源的回调类型。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录音配置变化的回调类型，支持的事件：'photoAssetAvailable'。 |
| callback | Callback<[photoAccessHelper.PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 否 | 回调函数，返回系统创建的资源文件对应的PhotoAsset对象。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。 |

**示例：**

```
1. avRecorder.off('photoAssetAvailable');
```
