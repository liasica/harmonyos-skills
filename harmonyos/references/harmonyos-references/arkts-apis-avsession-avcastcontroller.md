---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avcastcontroller
title: Interface (AVCastController)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Interface (AVCastController)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8239b3cfbebd6a97364a1239296953c300f046f0e6b3ab0b90b3d4825276fa00
---

在投播建立后，调用[avSession.getAVCastController](arkts-apis-avsession-avsession.md#getavcastcontroller10)后，返回会话控制器实例。控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 10开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { avSession } from '@kit.AVSessionKit';
```

## getAVPlaybackState10+

PhonePC/2in1TabletTV

getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVPlaybackState](arkts-apis-avsession-i.md#avplaybackstate10)> | 是 | 回调函数，返回远端播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getAVPlaybackState((state: avSession.AVPlaybackState) => {
2. console.info('Succeeded in getting AV playback state.');
3. });
```

## getAVPlaybackState10+

PhonePC/2in1TabletTV

getAVPlaybackState(): Promise<AVPlaybackState>

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVPlaybackState](arkts-apis-avsession-i.md#avplaybackstate10)> | Promise对象。返回远端播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getAVPlaybackState().then((state: avSession.AVPlaybackState) => {
2. console.info('Succeeded in getting AV playback state.');
3. });
```

## getSupportedDecoders19+

PhonePC/2in1TabletTV

getSupportedDecoders(): Promise<Array<DecoderType>>

获取当前远端设备的解码方式。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[DecoderType](arkts-apis-avsession-e.md#decodertype19)>> | Promise对象。返回远端设备所支持的解码能力列表。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getSupportedDecoders().then((decoderTypes: avSession.DecoderType[]) => {
2. console.info(`Succeeded in getting supported decoders, length: ${decoderTypes.length}`);
3. if (decoderTypes.length > 0 ) {
4. console.info(`Succeeded in getting supported decoder: ${decoderTypes[0]}`);
5. }
6. });
```

## getRecommendedResolutionLevel19+

PhonePC/2in1TabletTV

getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>

通过传递解码方式，获取推荐的分辨率。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decoderType | [DecoderType](arkts-apis-avsession-e.md#decodertype19) | 是 | 设备所支持的解码格式。  设备所支持的解码格式包括：  'OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC'：VIDEO AVC，  'OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC'：VIDEO HEVC，  'OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID'：AUDIO AV3A。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ResolutionLevel](arkts-apis-avsession-e.md#resolutionlevel19)> | Promise对象。返回远端设备推荐的分辨率。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. let decoderType = avSession.DecoderType.OH_AVCODEC_MIMETYPE_VIDEO_AVC;
2. avCastController.getRecommendedResolutionLevel(decoderType).then((resolutionLevel: avSession.ResolutionLevel) => {
3. console.info('Succeeded in getting recommended resolution level.');
4. });
```

## getSupportedHdrCapabilities19+

PhonePC/2in1TabletTV

getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>

获取当前的远端设备所支持的HDR能力。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[hdrCapability.HDRFormat](js-apis-hdrcapability.md#hdrformat)>> | Promise对象。返回远端设备所支持的HDR能力。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. import type hdrCapability from './@ohos.graphics.hdrCapability';

3. avCastController.getSupportedHdrCapabilities().then((hdrFormats: hdrCapability.HDRFormat[]) => {
4. console.info(`Succeeded in getting supported HDR capabilities, length: ${hdrFormats.length}`);
5. if (hdrFormats.length > 0 ) {
6. console.info(`Succeeded in getting supported HDR capability: ${hdrFormats[0]}`);
7. }
8. });
```

## getSupportedPlaySpeeds19+

PhonePC/2in1TabletTV

getSupportedPlaySpeeds(): Promise<Array<number>>

获取当前的远端设备所支持倍速播放列表。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象。返回远端设备所支持的倍速播放列表。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getSupportedPlaySpeeds().then((nums: number[]) => {
2. console.info(`Succeeded in getting supported play speeds, length: ${nums.length}`);
3. if (nums.length > 0 ) {
4. console.info(`Succeeded in getting supported play speed: ${nums[0]}`);
5. }
6. });
```

## sendControlCommand10+

PhonePC/2in1TabletTV

sendControlCommand(command: AVCastControlCommand): Promise<void>

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [AVCastControlCommand](arkts-apis-avsession-i.md#avcastcontrolcommand10) | 是 | 会话的相关命令和命令相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600105 | Invalid session command. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. let avCommand: avSession.AVCastControlCommand = {command:'play'};
2. avCastController.sendControlCommand(avCommand).then(() => {
3. console.info('Succeeded in sending control command.');
4. });
```

## sendControlCommand10+

PhonePC/2in1TabletTV

sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [AVCastControlCommand](arkts-apis-avsession-i.md#avcastcontrolcommand10) | 是 | 会话的相关命令和命令相关参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600105 | Invalid session command. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. let avCommand: avSession.AVCastControlCommand = {command:'play'};
2. avCastController.sendControlCommand(avCommand, () => {
3. console.info('Succeeded in sending control command.');
4. });
```

## sendCustomData20+

PhonePC/2in1TabletTV

sendCustomData(data: Record<string, Object>): Promise<void>

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record<string, Object> | 是 | 应用程序填充的自定义数据。  服务端仅解析key：string为'customData'，且Object为string类型的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |

**示例：**

```
1. avCastController.sendCustomData({customData : "This is custom data"});
```

## prepare10+

PhonePC/2in1TabletTV

prepare(item: AVQueueItem, callback: AsyncCallback<void>): void

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10) | 是 | 播放列表中单项的相关属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. // 设置播放参数，开始播放。
2. let playItem: avSession.AVQueueItem = {
3. itemId: 0,
4. description: {
5. assetId: '12345',
6. mediaType: 'AUDIO',
7. mediaUri: 'http://resource1_address',
8. mediaSize: 12345,
9. startPosition: 0,
10. duration: 0,
11. artist: 'mysong',
12. albumTitle: 'song1_title',
13. albumCoverUri: "http://resource1_album_address",
14. lyricUri: "http://resource1_lyric_address",
15. appName: 'MyMusic'
16. }
17. };
18. // 准备播放，这个不会触发真正的播放，会进行加载和缓冲。
19. avCastController.prepare(playItem, () => {
20. console.info('Succeeded in preparing.');
21. });
```

## prepare10+

PhonePC/2in1TabletTV

prepare(item: AVQueueItem): Promise<void>

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10) | 是 | 播放列表中单项的相关属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. // 设置播放参数，开始播放。
2. let playItem: avSession.AVQueueItem = {
3. itemId: 0,
4. description: {
5. assetId: '12345',
6. mediaType: 'AUDIO',
7. mediaUri: 'http://resource1_address',
8. mediaSize: 12345,
9. startPosition: 0,
10. duration: 0,
11. artist: 'mysong',
12. albumTitle: 'song1_title',
13. albumCoverUri: "http://resource1_album_address",
14. lyricUri: "http://resource1_lyric_address",
15. appName: 'MyMusic'
16. }
17. };
18. // 准备播放，这个不会触发真正的播放，会进行加载和缓冲。
19. avCastController.prepare(playItem).then(() => {
20. console.info('Succeeded in preparing.');
21. });
```

## start10+

PhonePC/2in1TabletTV

start(item: AVQueueItem, callback: AsyncCallback<void>): void

启动播放某个媒体资源。结果通过callback异步回调方式返回。

说明

在音视频投播场景下，当应用程序顺序调用[prepare](arkts-apis-avsession-avcastcontroller.md#prepare10)和start接口，且assetId不变时，如果prepare已经传入有效的mediaUri或fdSrc，则start接口将复用prepare阶段的完整的AVMediaDescription对象信息。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10) | 是 | 播放列表中单项的相关属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. // 设置播放参数，开始播放。
2. let playItem: avSession.AVQueueItem = {
3. itemId: 0,
4. description: {
5. assetId: '12345',
6. mediaType: 'AUDIO',
7. mediaUri: 'http://resource1_address',
8. mediaSize: 12345,
9. startPosition: 0,
10. duration: 0,
11. artist: 'mysong',
12. albumTitle: 'song1_title',
13. albumCoverUri: "http://resource1_album_address",
14. lyricUri: "http://resource1_lyric_address",
15. appName: 'MyMusic'
16. }
17. };

19. // 启动播放。
20. avCastController.start(playItem, () => {
21. console.info('Succeeded in starting.');
22. });
```

## start10+

PhonePC/2in1TabletTV

start(item: AVQueueItem): Promise<void>

启动播放某个媒体资源。结果通过Promise异步回调方式返回。

说明

在音视频投播场景下，当应用程序顺序调用[prepare](arkts-apis-avsession-avcastcontroller.md#prepare10)和start接口，且assetId不变时，如果prepare已经传入有效的mediaUri或fdSrc，则start接口将复用prepare阶段的完整的AVMediaDescription对象信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10) | 是 | 播放列表中单项的相关属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. // 设置播放参数，开始播放。
2. let playItem: avSession.AVQueueItem = {
3. itemId: 0,
4. description: {
5. assetId: '12345',
6. mediaType: 'AUDIO',
7. mediaUri: 'http://resource1_address',
8. mediaSize: 12345,
9. startPosition: 0,
10. duration: 0,
11. artist: 'mysong',
12. albumTitle: 'song1_title',
13. albumCoverUri: "http://resource1_album_address",
14. lyricUri: "http://resource1_lyric_address",
15. appName: 'MyMusic'
16. }
17. };
18. // 启动播放。
19. avCastController.start(playItem).then(() => {
20. console.info('Succeeded in starting.');
21. });
```

## getCurrentItem10+

PhonePC/2in1TabletTV

getCurrentItem(callback: AsyncCallback<AVQueueItem>): void

获取当前投播的资源信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10)> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getCurrentItem((value: avSession.AVQueueItem) => {
2. console.info('Succeeded in getting current item.');
3. });
```

## getCurrentItem10+

PhonePC/2in1TabletTV

getCurrentItem(): Promise<AVQueueItem>

获取当前投播的资源信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10)> | Promise对象，返回当前的播放资源，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getCurrentItem().then((value: avSession.AVQueueItem) => {
2. console.info('Succeeded in getting current item.');
3. });
```

## getValidCommands11+

PhonePC/2in1TabletTV

getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void

获取当前支持的命令。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[AVCastControlCommandType](arkts-apis-avsession-t.md#avcastcontrolcommandtype10)>> | 是 | 回调函数。返回当前支持的命令。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getValidCommands((state: avSession.AVCastControlCommandType[]) => {
2. console.info('Succeeded in getting valid commands.');
3. });
```

## getValidCommands11+

PhonePC/2in1TabletTV

getValidCommands(): Promise<Array<AVCastControlCommandType>>

获取当前支持的命令。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AVCastControlCommandType](arkts-apis-avsession-t.md#avcastcontrolcommandtype10)>> | Promise对象，返回当前支持的命令。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.getValidCommands().then((state: avSession.AVCastControlCommandType[]) => {
2. console.info('Succeeded in getting valid commands.');
3. });
```

## processMediaKeyResponse12+

PhonePC/2in1TabletTV

processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>

在线DRM资源投播时，处理许可证响应。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assetId | string | 是 | 媒体ID。 |
| response | Uint8Array | 是 | 许可证响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，当处理许可证响应成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |

**示例：**

```
1. let keyRequestCallback: avSession.KeyRequestCallback = async(assetId: string, requestData: Uint8Array) => {
2. // 根据assetId获取对应的DRM url。
3. let drmUrl = 'http://license.xxx.xxx.com:8080/drmproxy/getLicense';
4. // 从服务器获取许可证，需要开发者根据实际情况进行赋值。
5. let licenseResponseData: Uint8Array = new Uint8Array();
6. console.info(`Succeeded in get license by ${drmUrl}.`);
7. avCastController.processMediaKeyResponse(assetId, licenseResponseData);
8. }
```

## release11+

PhonePC/2in1TabletTV

release(callback: AsyncCallback<void>): void

销毁当前controller，结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令执行成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.release(() => {
2. console.info('Succeeded in releasing.');
3. });
```

## release11+

PhonePC/2in1TabletTV

release(): Promise<void>

销毁当前controller。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，controller销毁成功，无结果返回，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.release().then(() => {
2. console.info('Succeeded in releasing.');
3. });
```

## on('playbackStateChange')10+

PhonePC/2in1TabletTV

on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void

设置播放状态变化的监听事件。使用callback异步回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'playbackStateChange'：当播放状态变化时，触发该事件。 |
| filter | Array<keyof AVPlaybackState>|'all' | 是 | 'all' 表示关注播放状态所有字段变化；Array<keyof AVPlaybackstate> 表示关注Array中的字段变化。 |
| callback | (state: [AVPlaybackState](arkts-apis-avsession-i.md#avplaybackstate10)) => void | 是 | 回调函数，参数state是变化后的播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
2. console.info(`on playbackStateChange state : ${playbackState.state}`);
3. });

5. let playbackFilter: Array<keyof avSession.AVPlaybackState> = ['state', 'speed', 'loopMode'];
6. avCastController.on('playbackStateChange', playbackFilter, (playbackState: avSession.AVPlaybackState) => {
7. console.info(`on playbackStateChange state : ${playbackState.state}`);
8. });
```

## off('playbackStateChange')10+

PhonePC/2in1TabletTV

off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'playbackStateChange'。 |
| callback | (state: [AVPlaybackState](arkts-apis-avsession-i.md#avplaybackstate10)) => void | 否 | 回调函数，参数state是变化后的播放状态。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('playbackStateChange');
```

## on('mediaItemChange')10+

PhonePC/2in1TabletTV

on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void

设置投播当前播放媒体内容的监听事件。使用callback异步回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'mediaItemChange'：当播放的媒体内容变化时，触发该事件。 |
| callback | Callback<[AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10)> | 是 | 回调函数，参数AVQueueItem是当前正在播放的媒体内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('mediaItemChange', (item: avSession.AVQueueItem) => {
2. console.info(`on mediaItemChange state : ${item.itemId}`);
3. });
```

## off('mediaItemChange')10+

PhonePC/2in1TabletTV

off(type: 'mediaItemChange'): void

取消设置投播当前播放媒体内容事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'mediaItemChange'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('mediaItemChange');
```

## on('playNext')10+

PhonePC/2in1TabletTV

on(type: 'playNext', callback: Callback<void>): void

设置播放下一首资源的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'playNext'：当播放下一首状态变化时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('playNext', () => {
2. console.info('on playNext');
3. });
```

## off('playNext')10+

PhonePC/2in1TabletTV

off(type: 'playNext'): void

取消设置播放下一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'playNext'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('playNext');
```

## on('playPrevious')10+

PhonePC/2in1TabletTV

on(type: 'playPrevious', callback: Callback<void>): void

设置播放上一首资源的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'playPrevious'：当播放上一首状态变化时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('playPrevious', () => {
2. console.info('on playPrevious');
3. });
```

## off('playPrevious')10+

PhonePC/2in1TabletTV

off(type: 'playPrevious'): void

取消设置播放上一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'playPrevious'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('playPrevious');
```

## on('requestPlay')11+

PhonePC/2in1TabletTV

on(type: 'requestPlay', callback: Callback<AVQueueItem>): void

设置请求播放的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'requestPlay'：当请求播放状态变化时，触发该事件。 |
| callback | Callback<[AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10)> | 是 | 回调函数，参数AVQueueItem是当前正在播放的媒体内容。当监听事件注册成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('requestPlay', (item: avSession.AVQueueItem) => {
2. console.info(`on requestPlay state : ${item.itemId}`);
3. });
```

## off('requestPlay')11+

PhonePC/2in1TabletTV

off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void

取消设置请求播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'requestPlay'。 |
| callback | Callback<[AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10)> | 否 | 回调函数，参数AVQueueItem是当前正在播放的媒体内容。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('requestPlay');
```

## on('endOfStream')11+

PhonePC/2in1TabletTV

on(type: 'endOfStream', callback: Callback<void>): void

设置播放结束的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'endOfStream'：当资源播放结束时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。当监听事件注册成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('endOfStream', () => {
2. console.info('on endOfStream');
3. });
```

## off('endOfStream')11+

PhonePC/2in1TabletTV

off(type: 'endOfStream', callback?: Callback<void>): void

取消设置播放结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'endOfStream'。 |
| callback | Callback<void> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('endOfStream');
```

## on('seekDone')10+

PhonePC/2in1TabletTV

on(type: 'seekDone', callback: Callback<number>): void

设置seek结束的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'seekDone'：当seek结束时，触发该事件。 |
| callback | Callback<number> | 是 | 回调函数，返回seek后播放的位置。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('seekDone', (pos: number) => {
2. console.info(`on seekDone pos：${pos} `);
3. });
```

## off('seekDone')10+

PhonePC/2in1TabletTV

off(type: 'seekDone'): void

取消设置seek结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'seekDone'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('seekDone');
```

## on('validCommandChange')11+

PhonePC/2in1TabletTV

on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'validCommandChange'：当检测到会话的合法命令发生改变时，触发该事件。 |
| callback | Callback<Array<[AVCastControlCommandType](arkts-apis-avsession-t.md#avcastcontrolcommandtype10)>> | 是 | 回调函数。参数commands是有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avCastController.on('validCommandChange', (validCommands: avSession.AVCastControlCommandType[]) => {
2. console.info(`Succeeded in valid command change, size: ${validCommands.length}`);
3. console.info(`Succeeded in valid command change, validCommands: ${validCommands.values()}`);
4. });
```

## off('validCommandChange')11+

PhonePC/2in1TabletTV

off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)

取消会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'validCommandChange'。 |
| callback | Callback<Array<[AVCastControlCommandType](arkts-apis-avsession-t.md#avcastcontrolcommandtype10)>> | 否 | 回调函数。参数commands是有效命令的集合。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
1. avCastController.off('validCommandChange');
```

## on('videoSizeChange')12+

PhonePC/2in1TabletTV

on(type: 'videoSizeChange', callback: (width: number, height: number) => void): void

媒体控制器监听视频尺寸变化变化的事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

系统能力： SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'videoSizeChange'：当检测到会话的合法命令发生改变时，触发该事件。 |
| callback | (width: number, height: number) => void | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('videoSizeChange', (width: number, height: number) => {
2. console.info(`Succeeded in video size change, size: ${width}, ${height}`);
3. });
```

## off('videoSizeChange')12+

PhonePC/2in1TabletTV

off(type: 'videoSizeChange'): void

取消视频尺寸事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

系统能力： SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'videoSizeChange'：当检测到会话的合法命令发生改变时，触发该事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('videoSizeChange');
```

## on('error')10+

PhonePC/2in1TabletTV

on(type: 'error', callback: ErrorCallback): void

监听远端播放器的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'error'，用户操作和系统都会触发此事件。 |
| callback | ErrorCallback | 是 | 错误事件回调方法：远端播放过程中发生的错误，会提供错误码ID和错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)、[Media错误码](errorcode-media.md)以及[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupport format. |
| 6600101 | Session service exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. avCastController.on('error', (error: BusinessError) => {
4. console.info(`error happened, error code: ${error.code}, error message : ${error.message}.`)
5. })
```

## off('error')10+

PhonePC/2in1TabletTV

off(type: 'error'): void

取消播放的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，取消注册的事件：'error'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)、[Media错误码](errorcode-media.md)以及[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupport format. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('error')
```

## on('keyRequest')12+

PhonePC/2in1TabletTV

on(type: 'keyRequest', callback: KeyRequestCallback): void

在线DRM资源投播时，设置许可证请求的事件监听。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'keyRequest'：当DRM资源播放需要许可证时，触发该事件。 |
| callback | [KeyRequestCallback](arkts-apis-avsession-t.md#keyrequestcallback12) | 是 | 回调函数，媒体资源及许可证请求数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. let keyRequestCallback: avSession.KeyRequestCallback = async(assetId: string, requestData: Uint8Array) => {
2. console.info(`Succeeded in keyRequestCallback. assetId: ${assetId}, requestData: ${requestData}`);
3. }
4. avCastController.on('keyRequest', keyRequestCallback);
```

## off('keyRequest')12+

PhonePC/2in1TabletTV

off(type: 'keyRequest', callback?: KeyRequestCallback): void

取消许可证请求事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'keyRequest'。 |
| callback | [KeyRequestCallback](arkts-apis-avsession-t.md#keyrequestcallback12) | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('keyRequest');
```

## on('castControlGenericError')13+

PhonePC/2in1TabletTV

on(type: 'castControlGenericError', callback: ErrorCallback): void

监听投播通用错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'castControlGenericError'。 |
| callback | ErrorCallback | 是 | 投播通用错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6611000 | The error code for cast control is unspecified. |
| 6611001 | An unspecified error occurs in the remote player. |
| 6611002 | The playback position falls behind the live window. |
| 6611003 | The process of cast control times out. |
| 6611004 | The runtime check failed. |
| 6611100 | Cross-device data transmission is locked. |
| 6611101 | The specified seek mode is not supported. |
| 6611102 | The position to seek to is out of the range of the media asset or the specified seek mode is not supported. |
| 6611103 | The specified playback mode is not supported. |
| 6611104 | The specified playback speed is not supported. |
| 6611105 | The action failed because either the media source device or the media sink device has been revoked. |
| 6611106 | The parameter is invalid, for example, the url is illegal to play. |
| 6611107 | Allocation of memory failed. |
| 6611108 | Operation is not allowed. |

**示例：**

```
1. avCastController.on('castControlGenericError', (error: BusinessError) => {
2. console.info(`castControlGenericError happened, error code: ${error.code}, error message : ${error.message}.`)
3. })
```

## off('castControlGenericError')13+

PhonePC/2in1TabletTV

off(type: 'castControlGenericError', callback?: ErrorCallback): void

取消投播通用的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'castControlGenericError'。 |
| callback | ErrorCallback | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. avCastController.off('castControlGenericError');
```

## on('castControlIoError')13+

PhonePC/2in1TabletTV

on(type: 'castControlIoError', callback: ErrorCallback): void

监听投播输入/输出的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'castControlIoError'。 |
| callback | ErrorCallback | 是 | 投播输入/输出的错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6612000 | An unspecified input/output error occurs. |
| 6612001 | Network connection failure. |
| 6612002 | Network timeout. |
| 6612003 | Invalid "Content-Type" HTTP header. |
| 6612004 | The HTTP server returns an unexpected HTTP response status code. |
| 6612005 | The file does not exist. |
| 6612006 | No permission is granted to perform the IO operation. |
| 6612007 | Access to cleartext HTTP traffic is not allowed by the app's network security configuration. |
| 6612008 | Reading data out of the data bound. |
| 6612100 | The media does not contain any contents that can be played. |
| 6612101 | The media cannot be read, for example, because of dust or scratches. |
| 6612102 | This resource is already in use. |
| 6612103 | The content using the validity interval has expired. |
| 6612104 | Using the requested content to play is not allowed. |
| 6612105 | The use of the allowed content cannot be verified. |
| 6612106 | The number of times this content has been used as requested has reached the maximum allowed number of uses. |
| 6612107 | An error occurs when sending packet from source device to sink device. |

**示例：**

```
1. avCastController.on('castControlIoError', (error: BusinessError) => {
2. console.info(`castControlIoError happened, error code: ${error.code}, error message : ${error.message}.`)
3. })
```

## off('castControlIoError')13+

PhonePC/2in1TabletTV

off(type: 'castControlIoError', callback?: ErrorCallback): void

取消投播输入/输出的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'castControlIoError'。 |
| callback | ErrorCallback | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. avCastController.off('castControlIoError');
```

## on('castControlParsingError')13+

PhonePC/2in1TabletTV

on(type: 'castControlParsingError', callback: ErrorCallback): void

监听投播解析的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'castControlParsingError'。 |
| callback | ErrorCallback | 是 | 投播解析的错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6613000 | Unspecified error related to content parsing. |
| 6613001 | Parsing error associated with media container format bit streams. |
| 6613002 | Parsing error associated with the media manifest. |
| 6613003 | An error occurs when attempting to extract a file with an unsupported media container format or an unsupported media container feature. |
| 6613004 | Unsupported feature in the media manifest. |

**示例：**

```
1. avCastController.on('castControlParsingError', (error: BusinessError) => {
2. console.info(`castControlParsingError happened, error code: ${error.code}, error message : ${error.message}.`)
3. })
```

## off('castControlParsingError')13+

PhonePC/2in1TabletTV

off(type: 'castControlParsingError', callback?: ErrorCallback): void

取消投播解析的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'castControlParsingError'。 |
| callback | ErrorCallback | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. avCastController.off('castControlParsingError');
```

## on('castControlDecodingError')13+

PhonePC/2in1TabletTV

on(type: 'castControlDecodingError', callback: ErrorCallback): void

监听投播解码的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'castControlDecodingError'。 |
| callback | ErrorCallback | 是 | 投播解码的错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6614000 | Unspecified decoding error. |
| 6614001 | Decoder initialization failed. |
| 6614002 | Decoder query failed. |
| 6614003 | Decoding the media samples failed. |
| 6614004 | The format of the content to decode exceeds the capabilities of the device. |
| 6614005 | The format of the content to decode is not supported. |

**示例：**

```
1. avCastController.on('castControlDecodingError', (error: BusinessError) => {
2. console.info(`castControlDecodingError happened, error code: ${error.code}, error message : ${error.message}.`)
3. })
```

## off('castControlDecodingError')13+

PhonePC/2in1TabletTV

off(type: 'castControlDecodingError', callback?: ErrorCallback): void

取消投播解码的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'castControlDecodingError'。 |
| callback | ErrorCallback | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. avCastController.off('castControlDecodingError');
```

## on('castControlAudioRendererError')13+

PhonePC/2in1TabletTV

on(type: 'castControlAudioRendererError', callback: ErrorCallback): void

监听投播音频渲染器的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'castControlAudioRendererError'。 |
| callback | ErrorCallback | 是 | 投播音频渲染器的错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6615000 | Unspecified errors related to the audio renderer. |
| 6615001 | Initializing the audio renderer failed. |
| 6615002 | The audio renderer fails to write data. |

**示例：**

```
1. avCastController.on('castControlAudioRendererError', (error: BusinessError) => {
2. console.info(`castControlAudioRendererError happened, error code: ${error.code}, error message : ${error.message}.`)
3. })
```

## off('castControlAudioRendererError')13+

PhonePC/2in1TabletTV

off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void

取消投播音频渲染器的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'castControlAudioRendererError'。 |
| callback | ErrorCallback | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. avCastController.off('castControlAudioRendererError');
```

## on('castControlDrmError')13+

PhonePC/2in1TabletTV

on(type: 'castControlDrmError', callback: ErrorCallback): void

监听投播drm的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'castControlDrmError'。 |
| callback | ErrorCallback | 是 | 投播drm的错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6616000 | Unspecified error related to DRM. |
| 6616001 | The chosen DRM protection scheme is not supported by the device. |
| 6616002 | Device provisioning failed. |
| 6616003 | The DRM-protected content to play is incompatible. |
| 6616004 | Failed to obtain a license. |
| 6616005 | The operation is disallowed by the license policy. |
| 6616006 | An error occurs in the DRM system. |
| 6616007 | The device has revoked DRM privileges. |
| 6616008 | The DRM license being loaded into the open DRM session has expired. |
| 6616100 | An error occurs when the DRM processes the key response. |

**示例：**

```
1. avCastController.on('castControlDrmError', (error: BusinessError) => {
2. console.info(`castControlDrmError happened, error code: ${error.code}, error message : ${error.message}.`)
3. })
```

## off('castControlDrmError')13+

PhonePC/2in1TabletTV

off(type: 'castControlDrmError', callback?: ErrorCallback): void

取消投播drm的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'castControlDrmError'。 |
| callback | ErrorCallback | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. avCastController.off('castControlDrmError');
```

## on('customDataChange')20+

PhonePC/2in1TabletTV

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远端设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持'customDataChange'事件。媒体提供方发送自定义数据时触发。 |
| callback | Callback<Record<string, Object>> | 是 | 回调函数，用于接收自定义数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.on('customDataChange', (callback) => {
2. console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
3. });
```

## off('customDataChange')20+

PhonePC/2in1TabletTV

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消对自定义数据的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'customDataChange'。 |
| callback | Callback<Record<string, Object>> | 否 | 注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. avCastController.off('customDataChange');
```
