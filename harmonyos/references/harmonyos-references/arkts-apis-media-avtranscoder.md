---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avtranscoder
title: Interface (AVTranscoder)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Interface (AVTranscoder)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:43+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:e9f968bdc1a78443b653bd6742b2316f05e73d7e678c9a49d044a3509b1a4459
---

视频转码管理类，用于视频转码。在调用AVTranscoder的方法前，需要先通过[createAVTranscoder()](arkts-apis-media-f.md#mediacreateavtranscoder12)构建一个AVTranscoder实例。

视频转码demo可参考：[视频转码开发指导](../harmonyos-guides/using-avtranscoder-for-transcodering.md)

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { media } from '@kit.MediaKit';
```

## 属性

PhonePC/2in1TabletTV

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fdSrc12+ | [AVFileDescriptor](arkts-apis-media-i.md#avfiledescriptor9) | 否 | 否 | 源媒体文件描述，通过该属性设置数据源。  **使用示例**：  假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor{ fd = 资源句柄; offset = 0; length = 100; }。  **说明：**  - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。  - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。 |
| fdDst12+ | number | 否 | 否 | 目标媒体文件描述，通过该属性设置数据输出。在创建AVTranscoder实例后，必须设置fdSrc和fdDst属性。  **说明：**  - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。  - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。 |

## prepare12+

PhonePC/2in1TabletTV

prepare(config: AVTranscoderConfig): Promise<void>

进行视频转码的参数设置。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AVTranscoderConfig](arkts-apis-media-i.md#avtranscoderconfig12) | 是 | 配置视频转码的相关参数。 当config中设置的目标视频分辨率宽videoFrameWidth大于原视频的宽或目标视频分辨率高videoFrameHeight大于原视频的高时，会上报错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |
| 5400106 | Unsupported format. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建转码实例。
6. let avTranscoder = await media.createAVTranscoder();
7. // 配置参数以实际硬件设备支持的范围为准。
8. let avTranscoderConfig: media.AVTranscoderConfig = {
9. audioBitrate : 200000,
10. audioCodec : media.CodecMimeType.AUDIO_AAC,
11. fileFormat : media.ContainerFormatType.CFT_MPEG_4,
12. videoBitrate : 3000000,
13. videoCodec : media.CodecMimeType.VIDEO_AVC,
14. };

16. avTranscoder.prepare(avTranscoderConfig).then(() => {
17. console.info('prepare success');
18. }).catch((err: BusinessError) => {
19. console.error('prepare failed and catch error is ' + err.message);
20. });
21. }
```

## start12+

PhonePC/2in1TabletTV

start(): Promise<void>

开始视频转码。使用Promise异步回调。

需要[prepare()](arkts-apis-media-avtranscoder.md#prepare12)事件成功触发后，才能调用start方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建转码实例。
6. let avTranscoder = await media.createAVTranscoder();
7. avTranscoder.start().then(() => {
8. console.info('start AVTranscoder success');
9. }).catch((err: BusinessError) => {
10. console.error('start AVTranscoder failed and catch error is ' + err.message);
11. });
12. }
```

## pause12+

PhonePC/2in1TabletTV

pause(): Promise<void>

暂停视频转码。使用Promise异步回调。

需要[start()](arkts-apis-media-avtranscoder.md#start12)事件成功触发后，才能调用pause方法，可以通过调用[resume()](arkts-apis-media-avtranscoder.md#resume12)接口来恢复转码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建转码实例。
6. let avTranscoder = await media.createAVTranscoder();
7. avTranscoder.pause().then(() => {
8. console.info('pause AVTranscoder success');
9. }).catch((err: BusinessError) => {
10. console.error('pause AVTranscoder failed and catch error is ' + err.message);
11. });
12. }
```

## resume12+

PhonePC/2in1TabletTV

resume(): Promise<void>

恢复视频转码。使用Promise异步回调。

需要在[pause()](arkts-apis-media-avtranscoder.md#pause12)事件成功触发后，才能调用resume方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建转码实例。
6. let avTranscoder = await media.createAVTranscoder();
7. avTranscoder.resume().then(() => {
8. console.info('resume AVTranscoder success');
9. }).catch((err: BusinessError) => {
10. console.error('resume AVTranscoder failed and catch error is ' + err.message);
11. });
12. }
```

## cancel12+

PhonePC/2in1TabletTV

cancel(): Promise<void>

取消视频转码。使用Promise异步回调。

需要在[prepare()](arkts-apis-media-avtranscoder.md#prepare12)、[start()](arkts-apis-media-avtranscoder.md#start12)、[pause()](arkts-apis-media-avtranscoder.md#pause12)或[resume()](arkts-apis-media-avtranscoder.md#resume12)事件成功触发后，才能调用cancel方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建转码实例。
6. let avTranscoder = await media.createAVTranscoder();
7. avTranscoder.cancel().then(() => {
8. console.info('cancel AVTranscoder success');
9. }).catch((err: BusinessError) => {
10. console.error('cancel AVTranscoder failed and catch error is ' + err.message);
11. });
12. }
```

## release12+

PhonePC/2in1TabletTV

release(): Promise<void>

释放视频转码资源。使用Promise异步回调。

释放视频转码资源之后，该AVTranscoder实例不能再进行任何操作。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

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
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建转码实例。
6. let avTranscoder = await media.createAVTranscoder();
7. avTranscoder.release().then(() => {
8. console.info('release AVTranscoder success');
9. }).catch((err: BusinessError) => {
10. console.error('release AVTranscoder failed and catch error is ' + err.message);
11. });
12. }
```

## on('progressUpdate')12+

PhonePC/2in1TabletTV

on(type:'progressUpdate', callback: Callback<number>):void

注册转码进度更新事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 进度更新事件回调类型，支持的事件：'progressUpdate'，在转码过程中系统会自动触发此事件。 |
| callback | [Callback<number>](js-apis-base.md#callback) | 是 | 回调函数，返回进度更新事件，函数中的参数number，表示当前转码进度。 |

**示例：**

```
1. import { media } from '@kit.MediaKit';

3. async function test() {
4. // 创建转码实例。
5. let avTranscoder = await media.createAVTranscoder();
6. avTranscoder.on('progressUpdate', (progress: number) => {
7. console.info('avTranscoder progressUpdate = ' + progress);
8. });
9. }
```

## off('progressUpdate')12+

PhonePC/2in1TabletTV

off(type:'progressUpdate', callback?: Callback<number>): void

取消注册转码进度更新事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 进度更新事件回调类型，支持的事件：'progressUpdate'。 |
| callback | [Callback<number>](js-apis-base.md#callback) | 否 | 已注册的进度更新事件回调。由于当前回调注册时，仅会保留最后一次注册的回调，建议此参数缺省。 |

**示例：**

```
1. import { media } from '@kit.MediaKit';

3. async function test() {
4. // 创建转码实例。
5. let avTranscoder = await media.createAVTranscoder();
6. avTranscoder.off('progressUpdate');
7. }
```

## on('error')12+

PhonePC/2in1TabletTV

on(type: 'error', callback: ErrorCallback): void

注册AVTranscoder的错误事件，该事件仅用于错误提示。如果AVTranscoder上报error事件，开发者需要通过[release()](arkts-apis-media-avtranscoder.md#release12)退出转码操作。使用callback异步回调。

开发者只能订阅一个错误事件的回调方法，当开发者重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 转码错误事件回调类型'error'。  - 'error'：录制过程中发生错误，触发该事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 转码错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 801 | Capability not supported. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupported format. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建转码实例。
6. let avTranscoder = await media.createAVTranscoder();
7. avTranscoder.on('error', (err: BusinessError) => {
8. console.info('case avTranscoder.on(error) called, errMessage is ' + err.message);
9. });
10. }
```

## off('error')12+

PhonePC/2in1TabletTV

off(type:'error', callback?: ErrorCallback): void

取消注册转码错误事件，取消后不再接收到AVTranscoder的错误事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 转码错误事件回调类型'error'。  - 'error'：转码过程中发生错误，触发该事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 错误事件回调方法。 |

**示例：**

```
1. import { media } from '@kit.MediaKit';

3. async function test() {
4. // 创建转码实例。
5. let avTranscoder = await media.createAVTranscoder();
6. avTranscoder.off('error');
7. }
```

## on('complete')12+

PhonePC/2in1TabletTV

on(type: 'complete', callback: Callback<void>): void

注册转码完成事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。

当AVTranscoder上报complete事件时，当前转码操作已完成，开发者需要通过[release()](arkts-apis-media-avtranscoder.md#release12)退出转码操作。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 完成事件回调类型，支持的事件：'complete'，在转码过程中系统会自动触发此事件。 |
| callback | [Callback<void>](js-apis-base.md#callback) | 是 | 回调函数，返回完成事件回调方法。 |

**示例：**

```
1. import { media } from '@kit.MediaKit';

3. async function test() {
4. let avTranscoder: media.AVTranscoder | undefined = undefined;
5. // 创建转码实例。
6. avTranscoder = await media.createAVTranscoder();
7. avTranscoder.on('complete', async () => {
8. console.info('avTranscoder complete');
9. if (avTranscoder != undefined) {
10. // 开发者须在此监听转码完成事件。
11. // 须等待avTranscoder.release()释放转码实例之后，再对转码后的文件进行转发、上传、转存等处理。
12. await avTranscoder.release();
13. avTranscoder = undefined;
14. }
15. });
16. }
```

## off('complete')12+

PhonePC/2in1TabletTV

off(type:'complete', callback?: Callback<void>): void

取消注册转码完成事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 转码完成事件回调类型，支持的事件：'complete'。 |
| callback | [Callback<void>](js-apis-base.md#callback) | 否 | 完成事件回调方法。 |

**示例：**

```
1. import { media } from '@kit.MediaKit';

3. async function test() {
4. // 创建转码实例。
5. let avTranscoder = await media.createAVTranscoder();
6. avTranscoder.off('complete');
7. }
```
