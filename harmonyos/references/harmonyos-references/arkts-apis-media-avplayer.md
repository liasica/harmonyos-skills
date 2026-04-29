---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer
title: Interface (AVPlayer)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Interface (AVPlayer)
category: harmonyos-references
scraped_at: 2026-04-29T14:04:20+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c2846eff7338c5fc65580da85f033a174137658dad49e9b13eda633ae2a3feb4
---

播放管理类，用于管理和播放媒体资源。在调用AVPlayer的方法前，需要先通过[createAVPlayer()](arkts-apis-media-f.md#mediacreateavplayer9)构建一个AVPlayer实例。

在使用AVPlayer实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。[on('stateChange')](arkts-apis-media-avplayer.md#onstatechange9)：监听播放状态机AVPlayerState切换。[on('error')](arkts-apis-media-avplayer.md#onerror9)：监听错误事件。

应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。

Audio/Video播放demo可参考：[音频播放开发指导](../harmonyos-guides/using-avplayer-for-playback.md)、[视频播放开发指导](../harmonyos-guides/video-playback.md)。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url9+ | string | 否 | 是 | 媒体URL，只允许在**idle**状态下设置。  支持的视频格式：mp4、mpeg-ts、mkv。  支持的音频格式：m4a、aac、mp3、ogg、wav、flac、amr、ape。  **支持路径示例**：  1. fd类型播放：fd://xx。    2. http网络播放：http\://xx。  3. https网络播放：https\://xx。  4. HLS网络播放路径：http\://xx或者https\://xx。  **说明：**  - 设置网络播放路径，需[声明权限](../harmonyos-guides/declare-permissions.md)：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，相关错误码: [201 权限校验失败](errorcode-universal.md#section201-权限校验失败)。  - 从API version 11开始不支持webm。  - 将资源句柄（fd）传递给AVPlayer实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer / AVMetadataExtractor / AVImageGenerator / AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致媒体播放器数据获取异常。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fdSrc9+ | [AVFileDescriptor](arkts-apis-media-i.md#avfiledescriptor9) | 否 | 是 | 媒体文件描述，只允许在**idle**状态下设置。  **使用场景**：应用中的媒体资源被连续存储在同一个文件中。  支持的视频格式（mp4、mpeg-ts、mkv）。  支持的音频格式（m4a、aac、mp3、ogg、wav、flac、amr、ape）。  **使用示例**：  假设一个连续存储的媒体文件：  视频1（地址偏移：0，字节长度:100）；  视频2（地址偏移：101，字节长度：50）；  视频3（地址偏移：151，字节长度：150）；  1. 播放视频1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }。  2. 播放视频2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; }。  3. 播放视频3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; }。  假设是一个独立的媒体文件: 请使用src=fd://xx。  **说明：**  从API version 11开始不支持webm。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| dataSrc10+ | [AVDataSrcDescriptor](arkts-apis-media-i.md#avdatasrcdescriptor10) | 否 | 是 | 流式媒体资源描述，只允许在**idle**状态下设置。  **使用场景**：应用播放从远端下载到本地的文件，在应用未下载完整音视频资源时，提前播放已获取的资源数据。若将已获取的资源数据写入到本地文件中，同时从本地文件中读取数据，即可实现边播边缓存的能力。  支持的视频格式（mp4、mpeg-ts、mkv）。  支持的音频格式（m4a、aac、mp3、ogg、wav、flac、amr、ape）。  **使用示例**：  假设用户正在从远端服务器获取音视频媒体文件，希望下载到本地的同时播放已经下载好的部分：  1.用户需要获取媒体文件的总大小size（单位为字节），获取不到时设置为-1。  2.用户需要实现回调函数func用于填写数据，如果size = -1，则func形式为：func(buffer: ArrayBuffer, length: number)，此时播放器只会按照顺序获取数据；否则func形式为：func(buffer: ArrayBuffer, length: number, pos: number)，播放器会按需跳转并获取数据。  3.用户设置AVDataSrcDescriptor {fileSize = size, callback = func}。  **注意事项**：  如果播放的是mp4/m4a格式用户需要保证moov字段（媒体信息字段）在mdat字段（媒体数据字段）之前，或者moov之前的字段小于10M，否则会导致解析失败无法播放。  **说明：**  从API version 11开始不支持webm。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| surfaceId9+ | string | 否 | 是 | 视频窗口ID，默认无窗口。  仅支持在**initialized**状态下初始化。  初始化后可以在**prepared**/**playing**/**paused**/**completed**/**stopped**状态下重新设置，重新设置后视频播放将在新的窗口渲染。  使用场景：视频播放时的窗口渲染（纯音频播放时不涉及）。  **使用示例**：  通过[getXComponentSurfaceId](ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)接口创建surfaceId。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| loop9+ | boolean | 否 | 否 | 视频循环播放属性，默认false，设置为true表示循环播放，动态属性。  只允许在**prepared**/**playing**/**paused**/**completed**状态下设置。  直播场景不支持loop设置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| videoScaleType9+ | [VideoScaleType](arkts-apis-media-e.md#videoscaletype9) | 否 | 是 | 视频缩放模式，默认VIDEO\_SCALE\_TYPE\_FIT，动态属性。  只允许在**prepared**/**playing**/**paused**/**completed**状态下设置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| audioInterruptMode9+ | [audio.InterruptMode](arkts-apis-audio-e.md#interruptmode9) | 否 | 是 | 音频焦点模型，默认SHARE\_MODE，动态属性。  只允许在**prepared**/**playing**/**paused**/**completed**状态下设置。  在第一次调用[play()](arkts-apis-media-avplayer.md#play9)之前设置， 以便此后中断模式生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| audioRendererInfo10+ | [audio.AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 否 | 是 | 设置音频渲染信息。若媒体源包含视频，则usage默认值为STREAM\_USAGE\_MOVIE，否则usage默认值为STREAM\_USAGE\_MUSIC。rendererFlags默认值为0。若默认usage不满足需求，则须主动配置[audio.AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8)。  只允许在**initialized**状态下设置。  在第一次调用[prepare()](arkts-apis-media-avplayer.md#prepare9)之前设置，以便音频渲染器信息在之后生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| audioEffectMode10+ | [audio.AudioEffectMode](arkts-apis-audio-e.md#audioeffectmode10) | 否 | 是 | 设置音频音效模式，默认值为EFFECT\_DEFAULT，动态属性。audioRendererInfo的usage变动时会恢复为默认值，只允许在**prepared**/**playing**/**paused**/**completed**状态下设置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| state9+ | [AVPlayerState](arkts-apis-media-t.md#avplayerstate9) | 是 | 否 | 音视频播放的状态，全状态有效，可查询参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| currentTime9+ | number | 是 | 否 | 视频的当前播放位置，单位为毫秒（ms），可查询参数。  返回为（-1）表示无效值，**prepared**/**playing**/**paused**/**completed**状态下有效。  直播场景默认返回（-1）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| duration9+ | number | 是 | 否 | 视频时长，单位为毫秒（ms），可查询参数。  返回为（-1）表示无效值，**prepared**/**playing**/**paused**/**completed**状态下有效。  直播场景默认返回（-1）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| width9+ | number | 是 | 否 | 视频宽，单位为像素（px），可查询参数。  返回为（0）表示无效值，**prepared**/**playing**/**paused**/**completed**状态下有效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| height9+ | number | 是 | 否 | 视频高，单位为像素（px），可查询参数。  返回为（0）表示无效值，**prepared**/**playing**/**paused**/**completed**状态下有效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## on('stateChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void

监听播放状态机AVPlayerState切换的事件。

**元服务API：** 从API version 11 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态机切换事件回调类型，支持的事件：'stateChange'，用户操作和系统都会触发此事件。 |
| callback12+ | [OnAVPlayerStateChangeHandle](arkts-apis-media-t.md#onavplayerstatechangehandle12) | 是 | 状态机切换事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听播放状态机AVPlayerState切换的事件。
4. avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
5. switch (state) {
6. case 'idle':
7. console.info('state idle called');
8. break;
9. case 'initialized':
10. console.info('initialized prepared called');
11. break;
12. case 'prepared':
13. console.info('state prepared called');
14. break;
15. case 'playing':
16. console.info('state playing called');
17. break;
18. case 'paused':
19. console.info('state paused called');
20. break;
21. case 'completed':
22. console.info('state completed called');
23. break;
24. case 'stopped':
25. console.info('state stopped called');
26. break;
27. case 'released':
28. console.info('state released called');
29. break;
30. case 'error':
31. console.info('state error called');
32. break;
33. default:
34. console.info('unknown state :' + state);
35. break;
36. }
37. });
38. }
```

## off('stateChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void

取消监听播放状态机[AVPlayerState](arkts-apis-media-t.md#avplayerstate9)切换的事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态机切换事件回调类型，取消注册的事件：'stateChange' |
| callback12+ | [OnAVPlayerStateChangeHandle](arkts-apis-media-t.md#onavplayerstatechangehandle12) | 否 | 状态机切换事件回调方法。如果填写该参数，仅取消注册此回调的方法，否则取消注册stateChange事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收播放状态机AVPlayerState切换的事件。
4. avPlayer.off('stateChange');
5. }
```

## on('error')9+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听[AVPlayer](arkts-apis-media-avplayer.md)的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。如果此时[AVPlayerState](arkts-apis-media-t.md#avplayerstate9)也切至error状态，用户需要通过[reset()](arkts-apis-media-avplayer.md#reset9)或者[release()](arkts-apis-media-avplayer.md#release9)退出播放操作。若调用[reset()](arkts-apis-media-avplayer.md#reset9)方法后，播放状态仍为error状态，建议直接调用[release()](arkts-apis-media-avplayer.md#release9)方法，退出播放操作。

**元服务API：** 从API version 11 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'error'，用户操作和系统都会触发此事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 错误事件回调方法，使用播放器的过程中发生错误，会提供错误码ID和错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

在API version 9-13，针对网络、服务器等数据流异常，接口上报5400103；从API version 14开始，对应错误细化为错误码5411001-5411012。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupported format. |
| 5410002 | Seek continuous unsupported. |
| 5411001 | IO can not find host. |
| 5411002 | IO connection timeout. |
| 5411003 | IO network abnormal. |
| 5411004 | IO network unavailable. |
| 5411005 | IO no permission. |
| 5411006 | IO request denied. |
| 5411007 | IO resource not found. |
| 5411008 | IO SSL client cert needed. |
| 5411009 | IO SSL connect fail. |
| 5411010 | IO SSL server cert untrusted. |
| 5411011 | IO unsupported request. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. async function test(){
3. let avPlayer = await media.createAVPlayer();
4. // 监听AVPlayer的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。
5. avPlayer.on('error', (error: BusinessError) => {
6. console.info('error happened,and error message is :' + error.message);
7. console.info('error happened,and error code is :' + error.code);
8. });
9. }
```

## off('error')9+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消监听播放的错误事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，取消注册的事件：'error' |
| callback12+ | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 错误事件回调方法，使用播放器的过程中发生错误，会提供错误码ID和错误信息。如果填写该参数，仅取消注册此回调方法，否则取消注册error事件的所有回调方法。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function test(){
4. let avPlayer = await media.createAVPlayer();
5. // 取消后，不再监听AVPlayer的错误事件。
6. avPlayer.off('error');
7. }
```

## setMediaSource12+

PhonePC/2in1TabletTVWearable

setMediaSource(src:MediaSource, strategy?: PlaybackStrategy): Promise<void>

流媒体预下载资源设置，下载URL对应的流媒体数据并暂存在内存中，此接口只能在idle状态下调用。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [MediaSource](arkts-apis-media-mediasource.md) | 是 | 流媒体预下载媒体来源。 |
| strategy | [PlaybackStrategy](arkts-apis-media-i.md#playbackstrategy12) | 否 | 流媒体预下载播放策略。 |

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

**示例：**

```
1. async function test(){
2. let player = await media.createAVPlayer();
3. let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
4. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
5. let playStrategy : media.PlaybackStrategy = {
6. preferredWidth: 1,
7. preferredHeight: 2,
8. preferredBufferDuration: 3,
9. preferredHdr: false,
10. preferredBufferDurationForPlaying: 1,
11. thresholdForAutoQuickPlay: 5
12. };
13. player.setMediaSource(mediaSource, playStrategy);
14. }
```

## setPlaybackStrategy12+

PhonePC/2in1TabletTVWearable

setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>

设置播放策略，只能在initialized状态下调用。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [PlaybackStrategy](arkts-apis-media-i.md#playbackstrategy12) | 是 | 播放策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. let player = await media.createAVPlayer();
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let fileDescriptor = await context.resourceManager.getRawFd('xxx.mp4');
6. player.fdSrc = fileDescriptor
7. let playStrategy : media.PlaybackStrategy = {
8. preferredWidth: 1,
9. preferredHeight: 2,
10. preferredBufferDuration: 3,
11. preferredHdr: false,
12. mutedMediaType: media.MediaType.MEDIA_TYPE_AUD,
13. preferredBufferDurationForPlaying: 1,
14. thresholdForAutoQuickPlay: 5
15. };
16. player.setPlaybackStrategy(playStrategy);
```

## setPlaybackRange18+

PhonePC/2in1TabletTVWearable

setPlaybackRange(startTimeMs: number, endTimeMs: number, mode?: SeekMode) : Promise<void>

设置播放区间，并通过指定的[SeekMode](arkts-apis-media-e.md#seekmode8)跳转到区间开始位置。设置之后，只播放音视频文件设定区间内的内容。使用Promise异步回调。可在**initialized**/**prepared**/**paused**/**stopped**/**completed**状态下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startTimeMs | number | 是 | 区间开始位置，单位ms，取值[0, duration)。可以设置-1值，系统将会从0位置开始播放。 |
| endTimeMs | number | 是 | 区间结束位置，单位ms，取值(startTimeMs, duration]。可以设置-1值，系统将会播放到资源末尾。 |
| mode | [SeekMode](arkts-apis-media-e.md#seekmode8) | 否 | 支持SeekMode.SEEK\_PREV\_SYNC和SeekMode.SEEK\_CLOSEST,  默认值: SeekMode.SEEK\_PREV\_SYNC。 |

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. avPlayer.setPlaybackRange(0, 6000, media.SeekMode.SEEK_CLOSEST).then(() => {
6. console.info('Succeeded setPlaybackRange');
7. }).catch((err: BusinessError) => {
8. console.error('Failed to setPlaybackRange' + err.message);
9. });
10. }
```

## prepare9+

PhonePC/2in1TabletTVWearable

prepare(callback: AsyncCallback<void>): void

准备播放音频/视频，需在[stateChange](arkts-apis-media-avplayer.md#onstatechange9)事件成功触发至initialized状态后，才能调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 准备播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400106 | Unsupported format. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
6. avPlayer.prepare((err: BusinessError) => {
7. if (err) {
8. console.error('Failed to prepare,error message is :' + err.message);
9. } else {
10. console.info('Succeeded in preparing');
11. }
12. });
13. }
```

## prepare9+

PhonePC/2in1TabletTVWearable

prepare(): Promise<void>

准备播放音频/视频，需在[stateChange](arkts-apis-media-avplayer.md#onstatechange9)事件成功触发至initialized状态后，才能调用。使用Promise异步回调。

如果应用使用到多个短视频频繁切换的场景，为了提升切换性能，可以考虑创建多个AVPlayer对象，提前准备下一个视频，详情参见[在线短视频流畅切换](../best-practices/bpta-smooth-switching.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400106 | Unsupported format. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
6. avPlayer.prepare().then(() => {
7. console.info('Succeeded in preparing');
8. }, (err: BusinessError) => {
9. console.error('Failed to prepare,error message is :' + err.message);
10. });
11. }
```

## setMediaMuted12+

PhonePC/2in1TabletTVWearable

setMediaMuted(mediaType: MediaType, muted: boolean ): Promise<void>

设置音频静音/取消音频静音，从API version 20开始，增加支持设置画面显示/不显示。使用Promise异步回调。

只能在prepared/playing/paused/completed状态下调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaType | [MediaType](arkts-apis-media-e.md#mediatype8) | 是 | 媒体类型枚举。  **API version 12-19**：仅支持设置MEDIA\_TYPE\_AUD。  **API version 20及以后**：增加支持设置MEDIA\_TYPE\_VID。 |
| muted | boolean | 是 | **API version 12-19**：仅支持设置音频播放策略，表示音频是否静音播放。true为静音播放，false为取消静音播放。  **API version 20及以后**：增加支持设置视频播放策略，表示视频画面是否关闭。true为关闭画面，false为恢复画面。 |

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
6. avPlayer.prepare().then(() => {
7. console.info('Succeeded in preparing');
8. avPlayer.setMediaMuted(media.MediaType.MEDIA_TYPE_AUD, true);
9. }, (err: BusinessError) => {
10. console.error('Failed to prepare,error message is :' + err.message);
11. });
12. }
```

## play9+

PhonePC/2in1TabletTVWearable

play(callback: AsyncCallback<void>): void

开始播放音视频资源，只能在prepared/paused/completed状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 开始播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/paused/completed状态后才能调用。
6. avPlayer.play((err: BusinessError) => {
7. if (err) {
8. console.error('Failed to play,error message is :' + err.message);
9. } else {
10. console.info('Succeeded in playing');
11. }
12. });
13. }
```

## play9+

PhonePC/2in1TabletTVWearable

play(): Promise<void>

开始播放音视频资源，只能在prepared/paused/completed状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/paused/completed状态后才能调用。
6. avPlayer.play().then(() => {
7. console.info('Succeeded in playing');
8. }, (err: BusinessError) => {
9. console.error('Failed to play,error message is :' + err.message);
10. });
11. }
```

## pause9+

PhonePC/2in1TabletTVWearable

pause(callback: AsyncCallback<void>): void

暂停播放音视频资源，只能在playing状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 暂停播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
6. avPlayer.pause((err: BusinessError) => {
7. if (err) {
8. console.error('Failed to pause,error message is :' + err.message);
9. } else {
10. console.info('Succeeded in pausing');
11. }
12. });
13. }
```

## pause9+

PhonePC/2in1TabletTVWearable

pause(): Promise<void>

暂停播放音视频资源，只能在playing状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
6. avPlayer.pause().then(() => {
7. console.info('Succeeded in pausing');
8. }, (err: BusinessError) => {
9. console.error('Failed to pause,error message is :' + err.message);
10. });
11. }
```

## stop9+

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止播放音视频资源，只能在prepared/playing/paused/completed状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 停止播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
6. avPlayer.stop((err: BusinessError) => {
7. if (err) {
8. console.error('Failed to stop,error message is :' + err.message);
9. } else {
10. console.info('Succeeded in stopping');
11. }
12. });
13. }
```

## stop9+

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止播放音视频资源，只能在prepared/playing/paused/completed状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
6. avPlayer.stop().then(() => {
7. console.info('Succeeded in stopping');
8. }, (err: BusinessError) => {
9. console.error('Failed to stop,error message is :' + err.message);
10. });
11. }
```

## reset9+

PhonePC/2in1TabletTVWearable

reset(callback: AsyncCallback<void>): void

重置播放，只能在initialized/prepared/playing/paused/completed/stopped/error状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 重置播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped/error状态后才能调用。
6. avPlayer.reset((err: BusinessError) => {
7. if (err) {
8. console.error('Failed to reset,error message is :' + err.message);
9. } else {
10. console.info('Succeeded in resetting');
11. }
12. });
13. }
```

## reset9+

PhonePC/2in1TabletTVWearable

reset(): Promise<void>

重置播放，只能在initialized/prepared/playing/paused/completed/stopped/error状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped/error状态后才能调用。
6. avPlayer.reset().then(() => {
7. console.info('Succeeded in resetting');
8. }, (err: BusinessError) => {
9. console.error('Failed to reset,error message is :' + err.message);
10. });
11. }
```

## release9+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

销毁播放资源，除released状态外，均可以调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 销毁播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
6. avPlayer.release((err: BusinessError) => {
7. if (err) {
8. console.error('Failed to release,error message is :' + err.message);
9. } else {
10. console.info('Succeeded in releasing');
11. }
12. });
13. }
```

## release9+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

销毁播放资源，除released状态，都可以调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
6. avPlayer.release().then(() => {
7. console.info('Succeeded in releasing');
8. }, (err: BusinessError) => {
9. console.error('Failed to release,error message is :' + err.message);
10. });
11. }
```

## getTrackDescription9+

PhonePC/2in1TabletTVWearable

getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void

获取音视频轨道信息，可以在prepared/playing/paused状态调用。获取所有音视轨道信息，应在数据加载回调后调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[MediaDescription](arkts-apis-media-i.md#mediadescription8)>> | 是 | 回调函数，当获取音视频轨道信息成功，err为undefined，data为获取到的MediaDescription数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused状态后才能调用。
6. avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
7. if ((arrList) != null) {
8. console.info('Succeeded in doing getTrackDescription');
9. } else {
10. console.error(`Failed to do getTrackDescription, error:${error}`);
11. }
12. });
13. }
```

## getTrackDescription9+

PhonePC/2in1TabletTVWearable

getTrackDescription(): Promise<Array<MediaDescription>>

获取音视频轨道信息，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[MediaDescription](arkts-apis-media-i.md#mediadescription8)>> | Promise对象，返回音视频轨道信息MediaDescription数组。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused状态后才能调用。
6. avPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
7. console.info('Succeeded in getting TrackDescription');
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to get TrackDescription, error:${error}`);
10. });
11. }
```

## getSelectedTracks12+

PhonePC/2in1TabletTVWearable

getSelectedTracks(): Promise<Array<number>>

获取已选择的音视频轨道索引，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回已选择音视频轨道索引数组。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused状态后才能调用。
6. avPlayer.getSelectedTracks().then((arrList: Array<number>) => {
7. console.info('Succeeded in getting SelectedTracks');
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to get SelectedTracks, error:${error}`);
10. });
11. }
```

## getPlaybackInfo12+

PhonePC/2in1TabletTVWearable

getPlaybackInfo(): Promise<PlaybackInfo>

获取播放过程信息，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PlaybackInfo](arkts-apis-media-i.md#playbackinfo12)> | Promise对象，返回播放器信息PlaybackInfo。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avPlayer: media.AVPlayer | undefined;
4. let playbackInfo: media.PlaybackInfo | undefined;
5. media.createAVPlayer(async (err: BusinessError, player: media.AVPlayer) => {
6. if (player != null) {
7. avPlayer = player;
8. console.info(`Succeeded in creating AVPlayer`);
9. if (avPlayer) {
10. try {
11. playbackInfo = await avPlayer.getPlaybackInfo();
12. console.info(`AVPlayer getPlaybackInfo = ${JSON.stringify(playbackInfo)}`); // 打印整个PlaybackInfo的值。
13. } catch (error) {
14. console.error(`error = ${error}`);
15. }
16. }
17. } else {
18. console.error(`Failed to create AVPlayer, error message:${err.message}`);
19. }
20. });
```

## getPlaybackPosition18+

PhonePC/2in1TabletTVWearable

getPlaybackPosition(): number

获取当前播放位置，可以在prepared/playing/paused/completed状态调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前播放位置的时间，单位：毫秒（ms）。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
6. avPlayer.prepare().then(() => {
7. console.info('Succeeded in preparing');
8. let playbackPosition: number = avPlayer.getPlaybackPosition();
9. console.info(`AVPlayer getPlaybackPosition== ${playbackPosition}`);
10. }, (err: BusinessError) => {
11. console.error('Failed to prepare,error message is :' + err.message);
12. });
13. }
```

## getCurrentPresentationTimestamp23+

PhonePC/2in1TabletTVWearable

getCurrentPresentationTimestamp() : number

获取当前播放位置，可以在播放（playing）/暂停（paused）/完成（completed）状态调用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前播放位置的时间，单位：微秒（μs）。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
6. avPlayer.play().then(() => {
7. console.info('Succeeded in playing');
8. let currentPresentation: number = avPlayer.getCurrentPresentationTimestamp();
9. console.info(`AVPlayer getCurrentPresentationTimestamp== ${currentPresentation}`);
10. }, (err: BusinessError) => {
11. console.error('Failed to prepare,error message is :' + err.message);
12. });
13. }
```

## selectTrack12+

PhonePC/2in1TabletTVWearable

selectTrack(index: number, mode?: SwitchMode): Promise<void>

使用AVPlayer播放多音视频轨资源时，选择指定轨道播放，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 多音视频资源的轨道索引，可通过[getTrackDescription](arkts-apis-media-avplayer.md#gettrackdescription9-1)接口获取当前资源的所有轨道信息[MediaDescription](arkts-apis-media-i.md#mediadescription8)。 |
| mode | [SwitchMode](arkts-apis-media-e.md#switchmode12) | 否 | 切换视频轨道模式，默认为SMOOTH模式，**仅在DASH协议网络流视频轨切换时生效**，其他场景当前暂不支持。 |

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function  test(){
4. let avPlayer: media.AVPlayer = await media.createAVPlayer();
5. let audioTrackIndex: Object = 0;
6. avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
7. if (arrList != null) {
8. for (let i = 0; i < arrList.length; i++) {
9. if (i != 0) {
10. // 获取音频轨道列表。
11. audioTrackIndex = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
12. }
13. }
14. } else {
15. console.error(`Failed to get TrackDescription, error:${error}`);
16. }
17. });

19. // 选择其中一个音频轨道。
20. avPlayer.selectTrack(parseInt(audioTrackIndex.toString()));
21. }
```

## deselectTrack12+

PhonePC/2in1TabletTVWearable

deselectTrack(index: number): Promise<void>

使用AVPlayer播放多音轨视频时取消指定音视频轨道播放，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 多音视频资源的轨道索引，来自[getTrackDescription](arkts-apis-media-avplayer.md#gettrackdescription9-1)接口所获取的轨道信息[MediaDescription](arkts-apis-media-i.md#mediadescription8)。 |

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avPlayer: media.AVPlayer = await media.createAVPlayer();
4. let audioTrackIndex: Object = 0;
5. avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
6. if (arrList != null) {
7. for (let i = 0; i < arrList.length; i++) {
8. if (i != 0) {
9. // 获取音频轨道列表。
10. audioTrackIndex = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
11. }
12. }
13. } else {
14. console.error(`Failed to get TrackDescription, error:${error}`);
15. }
16. });

18. // 选择其中一个音频轨道。
19. avPlayer.selectTrack(parseInt(audioTrackIndex.toString()));
20. // 取消选择上次选中的音频轨道，并恢复到默认音频轨道。
21. avPlayer.deselectTrack(parseInt(audioTrackIndex.toString()));
```

## setDecryptionConfig11+

PhonePC/2in1TabletTVWearable

setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void

设置解密配置。当收到[on('mediaKeySystemInfoUpdate')](arkts-apis-media-avplayer.md#onmediakeysysteminfoupdate11)事件时，需根据事件上报的信息创建相关配置并设置解密配置，否则无法播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeySession | [drm.MediaKeySession](arkts-apis-drm-mediakeysession.md) | 是 | 解密会话 |
| secureVideoPath | boolean | 是 | 安全视频通路，true表示选择安全视频通路，false表示选择非安全视频通路 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

关于drm模块的示例具体可见[@ohos.multimedia.drm](arkts-apis-drm.md)。

```
1. import { drm } from '@kit.DrmKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 创建MediaKeySystem系统。
6. let keySystem:drm.MediaKeySystem = drm.createMediaKeySystem('com.wiseplay.drm');
7. // 创建MediaKeySession解密会话。
8. let keySession:drm.MediaKeySession = keySystem.createMediaKeySession(drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
9. // 生成许可证请求、设置许可证响应等。
10. // 安全视频通路标志。
11. let secureVideoPath:boolean = false;
12. // 设置解密配置。
13. avPlayer.setDecryptionConfig(keySession, secureVideoPath);
14. }
```

## getMediaKeySystemInfos11+

PhonePC/2in1TabletTVWearable

getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>

获取当前播放的媒体资源的MediaKeySystemInfo。需要在[on('mediaKeySystemInfoUpdate')](arkts-apis-media-avplayer.md#onmediakeysysteminfoupdate11)事件触发成功后才能调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[drm.MediaKeySystemInfo](arkts-apis-drm-i.md#mediakeysysteminfo)> | MediaKeySystemInfo数组，MediaKeySystemInfo具有uuid和pssh两个属性。当返回值为undefined时，表示mediaKeySystemInfoUpdate事件未触发。 |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. async function  test(){
4. let avPlayer = await media.createAVPlayer();
5. // 此处仅为示意，实际开发中需要在mediaKeySystemInfoUpdate事件触发成功后才能调用。
6. const infos = avPlayer.getMediaKeySystemInfos();
7. console.info('GetMediaKeySystemInfos count: ' + infos.length);
8. for (let i = 0; i < infos.length; i++) {
9. console.info('GetMediaKeySystemInfos uuid: ' + infos[i]["uuid"]);
10. console.info('GetMediaKeySystemInfos pssh: ' + infos[i]["pssh"]);
11. }
12. }
```

## seek9+

PhonePC/2in1TabletTVWearable

seek(timeMs: number, mode?:SeekMode): void

跳转到指定播放位置，只能在prepared/playing/paused/completed状态调用，可以通过[on('seekDone')](arkts-apis-media-avplayer.md#onseekdone9)事件确认是否生效。

注意

直播场景不支持seek。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, [duration](arkts-apis-media-avplayer.md#属性)]。  当模式为[SEEK\_CONTINUOUS](arkts-apis-media-e.md#seekmode8)时，可以取值-1，表示SEEK\_CONTINUOUS模式结束。 |
| mode | [SeekMode](arkts-apis-media-e.md#seekmode8) | 否 | 基于视频I帧的跳转模式，默认为SEEK\_PREV\_SYNC模式，**仅在视频资源播放时设置**。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. let seekTime: number = 1000;
4. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
5. avPlayer.seek(seekTime, media.SeekMode.SEEK_PREV_SYNC);
6. }
```

```
1. async function  test(){
2. // SEEK_CONTINUOUS 可以结合Slider的onChange回调方法进行对应处理，当slideMode为Moving时，触发拖动过程的SeekContinuous。
3. let avPlayer = await media.createAVPlayer();
4. let slideMovingTime: number = 2000;
5. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
6. avPlayer.seek(slideMovingTime, media.SeekMode.SEEK_CONTINUOUS);

8. // 当slideMode为End时，调用seek(-1, media.SeekMode.SEEK_CONTINUOUS)结束seek。
9. avPlayer.seek(-1, media.SeekMode.SEEK_CONTINUOUS);
10. }
```

## isSeekContinuousSupported18+

PhonePC/2in1TabletTVWearable

isSeekContinuousSupported() : boolean

查询媒体源是否支持以SEEK\_CONTINUOUS模式[SeekMode](arkts-apis-media-e.md#seekmode8)进行[seek](arkts-apis-media-avplayer.md#seek9)，在prepared/playing/paused/completed状态调用返回实际值，其余状态调用返回false。对于不支持SEEK\_CONTINUOUS模式进行seek的设备，返回false。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 媒体源是否支持以SEEK\_CONTINUOUS模式进行seek。true表示支持，false表示不支持。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
4. let isSupported = avPlayer.isSeekContinuousSupported();
5. }
```

## on('seekDone')9+

PhonePC/2in1TabletTVWearable

on(type: 'seekDone', callback: Callback<number>): void

监听seek生效的事件。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | seek生效的事件回调类型，支持的事件：'seekDone'，除SEEK\_CONTINUOUS外的[SeekMode](arkts-apis-media-e.md#seekmode8)每次调用seek后都会回调此事件。 |
| callback | Callback<number> | 是 | 回调函数。seek生效的事件回调方法，只会上报用户请求的time位置。  **视频播放：**[SeekMode](arkts-apis-media-e.md#seekmode8)会造成实际跳转位置与用户设置产生偏差，精准位置需要通过currentTime获取，事件回调的time仅代表完成用户某一次请求。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收seek生效的事件回调。
4. avPlayer.on('seekDone', (seekDoneTime:number) => {
5. console.info('seekDone called,and seek time is:' + seekDoneTime);
6. });
7. }
```

## off('seekDone')9+

PhonePC/2in1TabletTVWearable

off(type: 'seekDone', callback?: Callback<number>): void

取消监听seek生效的事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | seek生效的事件回调类型，取消注册的事件：'seekDone'。 |
| callback12+ | Callback<number> | 否 | 回调函数。seek生效的事件回调方法，只会上报用户请求的time位置。  **视频播放：**[SeekMode](arkts-apis-media-e.md#seekmode8)会造成实际跳转位置与用户设置产生偏差，精准位置需要通过currentTime获取，事件回调的time仅代表完成用户某一次请求。如果填写该参数，仅取消注册此回调的方法，否则取消注册seekDone事件的所有回调方法。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收seek生效的事件回调。
4. avPlayer.off('seekDone');
5. }
```

## setSpeed9+

PhonePC/2in1TabletTVWearable

setSpeed(speed: PlaybackSpeed): void

设置倍速模式，只能在prepared/playing/paused/completed状态调用，可以通过[on('speedDone')](arkts-apis-media-avplayer.md#onspeeddone9)事件确认是否生效。

注意

直播场景不支持setSpeed。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | [PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8) | 是 | 指定播放倍速模式。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
4. avPlayer.setSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
5. }
```

## on('speedDone')9+

PhonePC/2in1TabletTVWearable

on(type: 'speedDone', callback: Callback<number>): void

监听setSpeed生效的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setSpeed生效的事件回调类型，支持的事件：'speedDone'，每次调用setSpeed后都会回调此事件。 |
| callback | Callback<number> | 是 | 回调函数。当setSpeed成功，上报生效的倍速模式，具体见[PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8)。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收setSpeed生效事件回调。
4. avPlayer.on('speedDone', (speed:number) => {
5. console.info('speedDone called,and speed value is:' + speed);
6. });
7. }
```

## off('speedDone')9+

PhonePC/2in1TabletTVWearable

off(type: 'speedDone', callback?: Callback<number>): void

取消监听setSpeed生效的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setSpeed生效的事件回调类型，取消注册的事件：'speedDone'。 |
| callback12+ | Callback<number> | 否 | 回调函数。当setSpeed成功，上报生效的倍速模式，具体见[PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8)。如果填写该参数，仅取消注册此回调方法，否则取消注册speedDone事件的所有回调方法。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收setSpeed生效事件回调。
4. avPlayer.off('speedDone');
5. }
```

## setPlaybackRate20+

PhonePC/2in1TabletTVWearable

setPlaybackRate(rate: number): void

设置倍速模式。只能在prepared/playing/paused/completed状态调用，取值范围是[0.125, 4.0]，可以通过[playbackRateDone](arkts-apis-media-avplayer.md#onplaybackratedone20)事件确认是否生效。

注意

直播场景不支持setPlaybackRate。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | number | 是 | 指定播放倍速速率，取值范围为[0.125, 4.0]。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400108 | The parameter check failed, parameter value out of range. |
| 5400102 | Operation not allowed，if invalid state or live stream. |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
4. avPlayer.setPlaybackRate(2.0);
5. }
```

## getPlaybackRate23+

PhonePC/2in1TabletTVWearable

getPlaybackRate(): Promise<number>

获取当前播放器的播放速率。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回播放倍速速率。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. avPlayer.getPlaybackRate().then((rate: number) => {
4. console.info('Succeeded getPlaybackRate' + rate);
5. });
6. }
```

## on('playbackRateDone')20+

PhonePC/2in1TabletTVWearable

on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void

监听[setPlaybackRate](arkts-apis-media-avplayer.md#setplaybackrate20)生效的事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setPlaybackRate生效的事件回调类型，支持的事件：'playbackRateDone'，每次调用setPlaybackRate后都会回调此事件。 |
| callback | [OnPlaybackRateDone](arkts-apis-media-t.md#onplaybackratedone20) | 是 | setPlaybackRate生效的事件回调方法，上报设置后的播放速率。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收setPlaybackRate生效的事件。
4. avPlayer.on('playbackRateDone', (rate:number) => {
5. console.info('playbackRateDone called,and rate value is:' + rate);
6. });
7. }
```

## off('playbackRateDone')20+

PhonePC/2in1TabletTVWearable

off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void

取消监听[setPlaybackRate](arkts-apis-media-avplayer.md#setplaybackrate20)生效的事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setPlaybackRate生效的事件回调类型，取消注册的事件：'playbackRateDone'。 |
| callback | [OnPlaybackRateDone](arkts-apis-media-t.md#onplaybackratedone20) | 否 | setPlaybackRate生效的事件回调方法，上报设置后的播放速率。如果填写该参数，仅取消注册此回调方法，否则取消注册playbackRateDone事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收setPlaybackRate生效的事件。
4. avPlayer.off('playbackRateDone');
5. }
```

## setBitrate9+

PhonePC/2in1TabletTVWearable

setBitrate(bitrate: number): void

设置比特率，以播放所指定比特率的流媒体资源，当前仅对**HLS/DASH协议网络流**有效。默认情况下，AVPlayer会根据网络连接速度选择合适的比特率。只能在prepared/playing/paused/completed状态调用，可以通过[bitrateDone](arkts-apis-media-avplayer.md#onbitratedone9)事件确认是否生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitrate | number | 是 | 指定比特率，须通过[availableBitrates](arkts-apis-media-avplayer.md#onavailablebitrates9)事件获得当前HLS/DASH协议网络流可用的比特率列表，如果用户指定的比特率不在此列表中，则播放器将从可用比特率列表中选择最接近的比特率。如果通过availableBitrates事件获得的比特率列表长度为0，则不支持指定比特率，也不会产生bitrateDone回调。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. let bitrate: number = 96000;
4. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
5. avPlayer.setBitrate(bitrate);
6. }
```

## on('bitrateDone')9+

PhonePC/2in1TabletTVWearable

on(type: 'bitrateDone', callback: Callback<number>): void

监听setBitrate生效的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setBitrate生效的事件回调类型，支持的事件：'bitrateDone'，每次调用setBitrate后都会回调此事件。 |
| callback | Callback<number> | 是 | setBitrate生效的事件回调方法，上报生效的比特率。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收setBitrate生效事件回调。
4. avPlayer.on('bitrateDone', (bitrate:number) => {
5. console.info('bitrateDone called,and bitrate value is:' + bitrate);
6. });
7. }
```

## off('bitrateDone')9+

PhonePC/2in1TabletTVWearable

off(type: 'bitrateDone', callback?: Callback<number>): void

取消监听setBitrate生效的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setBitrate生效的事件回调类型，取消注册的事件：'bitrateDone'。 |
| callback12+ | Callback<number> | 否 | setBitrate生效的事件回调方法，上报生效的比特率。如果填写该参数，仅取消注册此回调方法，否则取消注册bitrateDone事件的所有回调方法。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收setBitrate生效事件回调。
4. avPlayer.off('bitrateDone');
5. }
```

## on('availableBitrates')9+

PhonePC/2in1TabletTVWearable

on(type: 'availableBitrates', callback: Callback<Array<number>>): void

监听HLS/DASH协议网络流可用的比特率列表，只会在切换prepared状态后上报。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | HLS/DASH协议网络流可用比特率上报事件回调类型，支持的事件：'availableBitrates'，只会在prepared之后上报一次。 |
| callback | Callback<Array<number>> | 是 | HLS/DASH协议网络流可用比特率上报事件回调方法，使用数组存放支持的比特率。如果数组长度为0，则不支持指定比特率。 |

**示例：**

```
1. async function  test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，播放状态切换prepared状态时，接收到HLS/DASH协议网络流可用的比特率列表回调。
4. avPlayer.on('availableBitrates', (bitrates: Array<number>) => {
5. console.info('availableBitrates called,and availableBitrates length is:' + bitrates.length);
6. });
7. }
```

## off('availableBitrates')9+

PhonePC/2in1TabletTVWearable

off(type: 'availableBitrates', callback?: Callback<Array<number>>): void

取消监听HLS/DASH协议网络流可用的比特率列表，调用[prepare](arkts-apis-media-avplayer.md#prepare9)后，上报此事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | HLS/DASH协议网络流可用比特率上报事件回调类型，取消注册的事件：'availableBitrates'。 |
| callback12+ | Callback<Array<number>> | 否 | HLS/DASH协议网络流可用比特率上报事件回调方法，使用数组存放支持的比特率。如果数组长度为0，则不支持指定比特率。如果填写该参数，仅取消注册此回调方法，否则取消注册availableBitrates事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收HLS/DASH协议网络流可用的比特率列表回调。
4. avPlayer.off('availableBitrates');
5. }
```

## on('mediaKeySystemInfoUpdate')11+

PhonePC/2in1TabletTVWearable

on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void

监听mediaKeySystemInfoUpdate事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 版权保护信息更新上报事件回调类型，支持的事件：'mediaKeySystemInfoUpdate'，当播放内容的版权保护信息更新时上报事件。 |
| callback | Callback<Array<drm.[MediaKeySystemInfo](arkts-apis-drm-i.md#mediakeysysteminfo)>> | 是 | 版权保护信息更新上报事件回调方法，上报MediaKeySystemInfo数组。 |

**示例：**

```
1. import { drm } from '@kit.DrmKit';

3. async function test(){
4. let avPlayer = await media.createAVPlayer();
5. // 监听后，开始接收mediaKeySystemInfoUpdate事件回调。
6. avPlayer.on('mediaKeySystemInfoUpdate', (mediaKeySystemInfo: Array<drm.MediaKeySystemInfo>) => {
7. for (let i = 0; i < mediaKeySystemInfo.length; i++) {
8. console.info('mediaKeySystemInfoUpdate happened uuid: ' + mediaKeySystemInfo[i]["uuid"]);
9. console.info('mediaKeySystemInfoUpdate happened pssh: ' + mediaKeySystemInfo[i]["pssh"]);
10. }
11. });
12. }
```

## off('mediaKeySystemInfoUpdate')11+

PhonePC/2in1TabletTVWearable

off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void;

取消监听mediaKeySystemInfoUpdate事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 版权保护信息更新上报事件回调类型，取消注册的事件：'mediaKeySystemInfoUpdate'。 |
| callback | Callback<Array<drm.[MediaKeySystemInfo](arkts-apis-drm-i.md#mediakeysysteminfo)>> | 否 | 版权保护信息更新上报事件回调方法，上报版权保护信息数组。如果填写该参数，仅取消注册此回调方法，否则取消注册mediaKeySystemInfoUpdate事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收mediaKeySystemInfoUpdate事件回调。
4. avPlayer.off('mediaKeySystemInfoUpdate');
5. }
```

## setLoudnessGain21+

PhonePC/2in1TabletTVWearable

setLoudnessGain(loudnessGain: number): Promise<void>

设置播放器的响度。调用该接口后，响度增益立即生效。使用Promise异步回调。

说明

* 当播放处于prepared/playing/paused/completed/stopped状态时，可调用该接口。
* 调用此接口时，需确保已设置音频渲染信息AVPlayer.audioRendererInfo，audioRendererInfo的usage参数必须是[STREAM\_USAGE\_MUSIC](arkts-apis-audio-e.md#streamusage)、[STREAM\_USAGE\_MOVIE](arkts-apis-audio-e.md#streamusage)、[STREAM\_USAGE\_AUDIOBOOK](arkts-apis-audio-e.md#streamusage)其中之一。
* 该接口不支持高清通路的响度设置。
* 音频流的时延模式必须是普通时延。
* 该接口错误信息通过[on('error')](arkts-apis-media-avplayer.md#onerror9)回调。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loudnessGain | number | 是 | 设置播放器的响度值，单位为dB，响度范围为[-90.0, 24.0]。默认值为0.0dB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. async function test(){
4. let avPlayer = await media.createAVPlayer();

6. let loudnessGain: number = 1.0;
7. avPlayer.audioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MOVIE,
9. rendererFlags: 0
10. }
11. avPlayer.setLoudnessGain(loudnessGain);
12. }
```

## setVolume9+

PhonePC/2in1TabletTVWearable

setVolume(volume: number): void

设置媒体播放音量，只能在prepared/playing/paused/completed状态调用，可以通过[on('volumeChange')](arkts-apis-media-avplayer.md#onvolumechange9)事件确认是否生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. let volume: number = 1.0;
4. avPlayer.setVolume(volume);
5. }
```

## on('volumeChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'volumeChange', callback: Callback<number>): void

监听setVolume生效的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setVolume生效的事件回调类型，支持的事件：'volumeChange'，每次调用setVolume后都会回调此事件。 |
| callback | Callback<number> | 是 | setVolume生效的事件回调方法，上报生效的媒体音量。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收setVolume生效的事件回调。
4. avPlayer.on('volumeChange', (vol: number) => {
5. console.info('volumeChange called,and new volume is :' + vol);
6. });
7. }
```

## off('volumeChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'volumeChange', callback?: Callback<number>): void

取消监听setVolume生效的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setVolume生效的事件回调类型，取消注册的事件：'volumeChange'。 |
| callback12+ | Callback<number> | 否 | setVolume生效的事件回调方法，上报生效的媒体音量。如果填写该参数，仅取消注册此回调方法，否则取消注册volumeChange事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收setVolume生效的事件。
4. avPlayer.off('volumeChange');
5. }
```

## on('endOfStream')9+

PhonePC/2in1TabletTVWearable

on(type: 'endOfStream', callback: Callback<void>): void

监听资源播放至结尾的事件；如果用户设置[loop](arkts-apis-media-avplayer.md#属性)=true，播放会跳转至开头重播；如果用户没有设置loop，会通过[stateChange](arkts-apis-media-avplayer.md#onstatechange9)上报completed状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 资源播放至结尾的事件回调类型，支持的事件：'endOfStream'，当播放至结尾时会上报此事件。 |
| callback | Callback<void> | 是 | 资源播放至结尾的事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收endOfStream事件回调。
4. avPlayer.on('endOfStream', () => {
5. console.info('endOfStream called');
6. });
7. }
```

## off('endOfStream')9+

PhonePC/2in1TabletTVWearable

off(type: 'endOfStream', callback?: Callback<void>): void

取消监听资源播放至结尾的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 资源播放至结尾的事件回调类型，取消注册的事件：'endOfStream'。 |
| callback12+ | Callback<void> | 否 | 资源播放至结尾的事件回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册endOfStream事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收endOfStream事件回调。
4. avPlayer.off('endOfStream');
5. }
```

## on('timeUpdate')9+

PhonePC/2in1TabletTVWearable

on(type: 'timeUpdate', callback: Callback<number>): void

监听资源播放当前时间，单位为毫秒（ms），用于刷新进度条当前位置，默认间隔100ms时间上报，因用户操作（seek）产生的时间变化会立刻上报。

注意

* 直播场景不支持timeUpdate上报。
* 操作（seek）时必须等待seekdone结束才能根据timeUpdate来更新进度条。
* 在pause状态下，缓冲结束时播放器会上报timeUpdate事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时间更新的回调类型，支持的事件：'timeUpdate'。 |
| callback | Callback<number> | 是 | 回调函数。返回当前时间。 |

**示例1：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收资源播放当前时间事件回调。
4. avPlayer.on('timeUpdate', (time:number) => {
5. console.info('timeUpdate called,and new time is :' + time);
6. });
7. }
```

**示例2：**

```
1. async function test() {
2. let avPlayer = await media.createAVPlayer();

4. let isSeeking = false;    // 标记是否正在seek。
5. let seekTargetTime = 0;   // 记录目标时间（单位：毫秒）。

7. // 1.监听seekDone：确认跳转完成。
8. avPlayer.on('seekDone', (seekDoneTime: number) => {
9. console.info('seekDone called, and seek time is: ' + seekDoneTime);
10. isSeeking = false;
11. seekTargetTime = seekDoneTime; // 可选：记录最终定位时间。
12. });

14. // 2.监听timeUpdate：只在seekDone后才更新进度。
15. avPlayer.on('timeUpdate', (time: number) => {
16. // 关键逻辑：只有seekDone之后才允许更新进度条。
17. if (isSeeking) {
18. console.info('seek in progress, ignore timeUpdate');
19. return; // 忽略seek期间的timeUpdate。
20. }

22. // 真正的播放进度更新（seekDone后才生效）。
23. console.info('timeUpdate: ' + time + ' ms');
24. // 此处进行进度条更新。
25. });

27. // 3.模拟seek操作。
28. let seekTime: number = 1000;
29. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
30. avPlayer.seek(seekTime, media.SeekMode.SEEK_PREV_SYNC); // 单位：毫秒。
31. isSeeking = true; // 标记正在seek。
32. }
```

## off('timeUpdate')9+

PhonePC/2in1TabletTVWearable

off(type: 'timeUpdate', callback?: Callback<number>): void

取消监听资源播放当前时间。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时间更新的回调类型，取消注册的事件：'timeUpdate'。 |
| callback12+ | Callback<number> | 否 | 回调函数。返回当前时间。如果填写该参数，仅取消注册此回调方法，否则取消注册timeUpdate事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收资源播放当前时间事件回调。
4. avPlayer.off('timeUpdate');
5. }
```

## on('durationUpdate')9+

PhonePC/2in1TabletTVWearable

on(type: 'durationUpdate', callback: Callback<number>): void

监听资源播放资源的时长，单位为毫秒（ms），用于刷新进度条长度，默认只在prepared上报一次，同时允许一些特殊码流刷新多次时长。

注意

直播场景不支持durationUpdate上报。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时长更新的回调类型，支持的事件：'durationUpdate'。 |
| callback | Callback<number> | 是 | 回调函数。返回资源时长。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收资源播放资源的时长事件回调。
4. avPlayer.on('durationUpdate', (duration: number) => {
5. console.info('durationUpdate called,new duration is :' + duration);
6. });
7. }
```

## off('durationUpdate')9+

PhonePC/2in1TabletTVWearable

off(type: 'durationUpdate', callback?: Callback<number>): void

取消监听资源播放资源的时长。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时长更新的回调类型，取消注册的事件：'durationUpdate'。 |
| callback12+ | Callback<number> | 否 | 回调函数。返回资源时长。如果填写该参数，仅取消注册此回调方法，否则取消注册durationUpdate事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收资源播放资源的时长事件回调。
4. avPlayer.off('durationUpdate');
5. }
```

## on('bufferingUpdate')9+

PhonePC/2in1TabletTVWearable

on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void

订阅音视频缓存更新事件，仅网络播放支持该订阅事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 播放缓存事件回调类型，支持的事件：'bufferingUpdate'。 |
| callback | [OnBufferingUpdateHandler](arkts-apis-media-t.md#onbufferingupdatehandler12) | 是 | 播放缓存事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收音视频缓存更新事件回调。
4. avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
5. console.info('bufferingUpdate called,and infoType value is:' + infoType + ', value is :' + value);
6. });
7. }
```

## off('bufferingUpdate')9+

PhonePC/2in1TabletTVWearable

off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void

取消监听音视频缓存更新事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 播放缓存事件回调类型，取消注册的事件：'bufferingUpdate'。 |
| callback | [OnBufferingUpdateHandler](arkts-apis-media-t.md#onbufferingupdatehandler12) | 否 | 播放缓存事件回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册bufferingUpdate事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收资源播放资源的时长事件回调。
4. avPlayer.off('bufferingUpdate');
5. }
```

## on('startRenderFrame')9+

PhonePC/2in1TabletTVWearable

on(type: 'startRenderFrame', callback: Callback<void>): void

订阅视频播放开始首帧渲染的更新事件，仅视频播放支持该订阅事件，该事件仅代表播放服务将第一帧画面送显示模块，实际效果依赖显示服务渲染性能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放开始首帧渲染事件回调类型，支持的事件：'startRenderFrame'。 |
| callback | Callback<void> | 是 | 视频播放开始首帧渲染事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听后，开始接收视频播放开始首帧渲染的更新事件回调。
4. avPlayer.on('startRenderFrame', () => {
5. console.info('startRenderFrame called');
6. });
7. }
```

## off('startRenderFrame')9+

PhonePC/2in1TabletTVWearable

off(type: 'startRenderFrame', callback?: Callback<void>): void

取消监听视频播放开始首帧渲染的更新事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放开始首帧渲染事件回调类型，取消注册的事件：'startRenderFrame'。 |
| callback12+ | Callback<void> | 否 | 视频播放开始首帧渲染事件回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册startRenderFrame事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收视频播放开始首帧渲染的更新事件回调。
4. avPlayer.off('startRenderFrame');
5. }
```

## on('videoSizeChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void

监听视频播放宽高变化事件，仅视频播放支持该订阅事件，默认只在prepared状态上报一次，但HLS协议码流会在切换分辨率时上报。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放宽高变化事件回调类型，支持的事件：'videoSizeChange'。 |
| callback | [OnVideoSizeChangeHandler](arkts-apis-media-t.md#onvideosizechangehandler12) | 是 | 视频播放宽高变化事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 监听视频播放宽高变化事件，仅视频播放支持该订阅事件，默认只在prepared状态上报一次。
4. avPlayer.on('videoSizeChange', (width: number, height: number) => {
5. console.info('videoSizeChange called,and width is:' + width + ', height is :' + height);
6. });
7. }
```

## off('videoSizeChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void

取消监听视频播放宽高变化事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放宽高变化事件回调类型，取消注册的事件：'videoSizeChange'。 |
| callback12+ | [OnVideoSizeChangeHandler](arkts-apis-media-t.md#onvideosizechangehandler12) | 否 | 视频播放宽高变化事件回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册videoSizeChange事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再监听视频播放宽高变化事件。
4. avPlayer.off('videoSizeChange');
5. }
```

## on('audioInterrupt')9+

PhonePC/2in1TabletTVWearable

on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void

监听音频焦点变化事件，多个音视频资源同时播放时，会根据音频焦点模型[audio.InterruptMode](arkts-apis-audio-e.md#interruptmode9)触发此事件。应用需根据不同焦点变化事件作相应处理。具体可参考[处理音频焦点事件](../harmonyos-guides/audio-playback-concurrency.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 音频焦点变化事件回调类型，支持的事件：'audioInterrupt'。 |
| callback | Callback<[audio.InterruptEvent](arkts-apis-audio-i.md#interruptevent9)> | 是 | 音频焦点变化事件回调方法。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. async function test(){
4. let avPlayer = await media.createAVPlayer();
5. // 监听音频焦点变化事件，多个音视频资源同时播放时，会根据音频焦点模型audio.InterruptMode触发此事件。
6. avPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
7. console.info('audioInterrupt called,and InterruptEvent info is:' + info);
8. });
9. }
```

## off('audioInterrupt')9+

PhonePC/2in1TabletTVWearable

off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void

取消监听音频焦点变化事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 音频焦点变化事件回调类型，取消注册的事件：'audioInterrupt'。 |
| callback12+ | Callback<[audio.InterruptEvent](arkts-apis-audio-i.md#interruptevent9)> | 否 | 音频焦点变化事件回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册audioInterrupt事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收音频焦点变化事件回调。
4. avPlayer.off('audioInterrupt');
5. }
```

## on('audioOutputDeviceChangeWithInfo')11+

PhonePC/2in1TabletTVWearable

on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void

订阅监听音频流输出设备变化及原因，使用callback方式返回结果。

在订阅此监听时，建议参考[响应输出设备变更时合理暂停](../harmonyos-guides/audio-output-device-change.md)自行实现设备连接或者断开时的播放器行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'audioOutputDeviceChangeWithInfo'。 |
| callback | Callback<[audio.AudioStreamDeviceChangeInfo](arkts-apis-audio-i.md#audiostreamdevicechangeinfo11)> | 是 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. async function test(){
4. let avPlayer = await media.createAVPlayer();
5. // 开始监听音频流输出设备变化及原因。
6. avPlayer.on('audioOutputDeviceChangeWithInfo', (data: audio.AudioStreamDeviceChangeInfo) => {
7. console.info(`${JSON.stringify(data)}`);
8. });
9. }
```

## off('audioOutputDeviceChangeWithInfo')11+

PhonePC/2in1TabletTVWearable

off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void

取消订阅监听音频流输出设备变化及原因，使用callback方式返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'audioOutputDeviceChangeWithInfo'。 |
| callback | Callback<[audio.AudioStreamDeviceChangeInfo](arkts-apis-audio-i.md#audiostreamdevicechangeinfo11)> | 否 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。如果填写该参数，仅取消注册此回调方法，否则取消注册audioOutputDeviceChangeWithInfo事件的所有回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收音频流输出设备变化事件。
4. avPlayer.off('audioOutputDeviceChangeWithInfo');
5. }
```

## addSubtitleFromFd12+

PhonePC/2in1TabletTVWearable

addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>

依据fd为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 资源句柄，通过[resourceManager.getRawFd](js-apis-resource-manager.md#getrawfd9)获取。 |
| offset | number | 否 | 资源偏移量，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误，默认值:0。 |
| length | number | 否 | 资源长度，默认值为文件中从偏移量开始的剩余字节，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误，默认值:0。 |

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

**示例：**

```
1. import { common } from '@kit.AbilityKit'

3. let avPlayer = await media.createAVPlayer();
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let fileDescriptor = await context.resourceManager.getRawFd('xxx.srt');

7. avPlayer.addSubtitleFromFd(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
```

## addSubtitleFromUrl12+

PhonePC/2in1TabletTVWearable

addSubtitleFromUrl(url: string): Promise<void>

依据url为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 外挂字幕文件地址。 |

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

**示例：**

```
1. async function test(){
2. let fdUrl:string = 'http://xxx.xxx.xxx/xx/index.srt';
3. let avPlayer: media.AVPlayer = await media.createAVPlayer();
4. avPlayer.addSubtitleFromUrl(fdUrl);
5. }
```

## on('subtitleUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void

订阅获取外挂字幕的事件，当有外挂字幕时，会通过订阅的回调方法通知用户。用户只能订阅一个外挂字幕事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'subtitleUpdate'。 |
| callback | Callback<[SubtitleInfo](arkts-apis-media-i.md#subtitleinfo12)> | 是 | 外挂字幕事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 订阅获取外挂字幕的事件，当有外挂字幕时，会触发事件。
4. avPlayer.on('subtitleUpdate', async (info: media.SubtitleInfo) => {
5. if (info) {
6. let text = (!info.text) ? '' : info.text
7. let startTime = (!info.startTime) ? 0 : info.startTime
8. let duration = (!info.duration) ? 0 : info.duration
9. console.info('subtitleUpdate info: text=' + text + ' startTime=' + startTime +' duration=' + duration);
10. } else {
11. console.info('subtitleUpdate info is null');
12. }
13. });
14. }
```

## off('subtitleUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void

取消订阅获取外挂字幕的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'subtitleUpdate'。 |
| callback | Callback<[SubtitleInfo](arkts-apis-media-i.md#subtitleinfo12)> | 否 | 取消外挂字幕事件的回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册subtitleUpdate事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收获取外挂字幕的事件。
4. avPlayer.off('subtitleUpdate');
5. }
```

## on('trackChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'trackChange', callback: OnTrackChangeHandler): void

订阅获取轨道变更的事件，当播放的轨道变更时，会通过订阅的回调方法通知用户。用户只能订阅一个轨道变更事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackChange'。 |
| callback | [OnTrackChangeHandler](arkts-apis-media-t.md#ontrackchangehandler12) | 是 | 轨道变更事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 订阅获取轨道变更的事件，当播放的轨道变更时，会触发事件回调。
4. avPlayer.on('trackChange', (index: number, isSelect: boolean) => {
5. console.info('trackChange info: index=' + index + ' isSelect=' + isSelect);
6. });
7. }
```

## off('trackChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'trackChange', callback?: OnTrackChangeHandler): void

取消订阅获取轨道变更的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackChange'。 |
| callback | [OnTrackChangeHandler](arkts-apis-media-t.md#ontrackchangehandler12) | 否 | 取消轨道变更事件的回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册trackChange事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收轨道变更的事件。
4. avPlayer.off('trackChange');
5. }
```

## on('trackInfoUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void

订阅获取轨道信息更新的事件，当播放的轨道有更新时，会通过订阅的回调方法通知用户。用户只能订阅一个轨道变更事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackInfoUpdate'。 |
| callback | Callback<Array<[MediaDescription](arkts-apis-media-i.md#mediadescription8)>> | 是 | 轨道信息更新事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 订阅获取轨道信息更新的事件，当播放的轨道有更新时，会触发事件回调。
4. avPlayer.on('trackInfoUpdate', (info: Array<media.MediaDescription>) => {
5. if (info) {
6. for (let i = 0; i < info.length; i++) {
7. let propertyIndex: Object = info[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
8. let propertyType: Object = info[i][media.MediaDescriptionKey.MD_KEY_TRACK_TYPE];
9. console.info('track info: index=' + propertyIndex + ' tracktype=' + propertyType);
10. }
11. } else {
12. console.info('track info is null');
13. }
14. });
15. }
```

## off('trackInfoUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void

取消订阅获取轨道信息更新的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackInfoUpdate'。 |
| callback | Callback<Array<[MediaDescription](arkts-apis-media-i.md#mediadescription8)>> | 否 | 取消轨道信息更新事件的回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册trackInfoUpdate事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收轨道信息更新的事件。
4. avPlayer.off('trackInfoUpdate');
5. }
```

## on('amplitudeUpdate')13+

PhonePC/2in1TabletTVWearable

on(type: 'amplitudeUpdate', callback: Callback<Array<number>>): void

订阅音频最大电平值，音频资源播放时定时上报。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'amplitudeUpdate'。 |
| callback | Callback<Array<number>> | 是 | 音频最大电平值更新事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 订阅音频最大电平值，音频资源播放时定时上报。
4. avPlayer.on('amplitudeUpdate', (value: Array<number>) => {
5. console.info(`amplitudeUpdate called,and amplitudeUpdate = ${value}`);
6. });
7. }
```

## off('amplitudeUpdate')13+

PhonePC/2in1TabletTVWearable

off(type: 'amplitudeUpdate', callback?: Callback<Array<number>>): void

取消订阅获取音频最大电平值事件。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'amplitudeUpdate'。 |
| callback | Callback<Array<number>> | 否 | 取消音频最大电平值更新事件回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册amplitudeUpdate事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收获取音频最大电平值事件上报。
4. avPlayer.off('amplitudeUpdate');
5. }
```

## on('seiMessageReceived')18+

PhonePC/2in1TabletTVWearable

on(type: 'seiMessageReceived', payloadTypes: Array<number>, callback: OnSeiMessageHandle): void

订阅获取SEI信息事件，仅适用于HTTP-FLV直播，视频流中包含SEI信息时上报。需在prepare之前订阅，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'seiMessageReceived'。 |
| payloadTypes | Array<number> | 是 | SEI信息的订阅负载类型数组。当前仅支持负载类型为5，即payloadType = 5。 |
| callback | [OnSeiMessageHandle](arkts-apis-media-t.md#onseimessagehandle18) | 是 | 用于监听SEI信息事件的回调函数，接收订阅的负载类型。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. async function test(){
4. let avPlayer = await media.createAVPlayer();

6. // 监听后，开始接收seiMessageReceived事件回调。
7. avPlayer.on('seiMessageReceived', [5], (messages: Array<media.SeiMessage>, playbackPosition?: number) =>
8. {
9. console.info('seiMessageReceived playbackPosition ' + playbackPosition);

11. for (let key = 0; key < messages.length; key++) {
12. console.info('seiMessageReceived messages payloadType ' + messages[key].payloadType + ' payload size ' + messages[key].payload.byteLength);

14. let textDecoder = util.TextDecoder.create("utf-8",{ignoreBOM: true});
15. let ab = messages[key]?.payload?.slice(16, messages[key].payload.byteLength);
16. let result: Uint8Array = new Uint8Array(ab);
17. let retStr: string = textDecoder.decodeToString(result);
18. console.info('seiMessageReceived messages payload ' + retStr);
19. }
20. });
21. }
```

## off('seiMessageReceived')18+

PhonePC/2in1TabletTVWearable

off(type: 'seiMessageReceived', payloadTypes?: Array<number>, callback?: OnSeiMessageHandle): void

取消订阅获取SEI信息事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'seiMessageReceived'。 |
| payloadTypes | Array<number> | 否 | SEI信息的订阅负载类型。 |
| callback | [OnSeiMessageHandle](arkts-apis-media-t.md#onseimessagehandle18) | 否 | 用于监听SEI信息事件的回调函数，接收订阅的负载类型。如果填写该参数，仅取消注册此回调方法，否则取消注册seiMessageReceived事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收seiMessageReceived事件回调。
4. avPlayer.off('seiMessageReceived');
5. }
```

## setSuperResolution18+

PhonePC/2in1TabletTVWearable

setSuperResolution(enabled: boolean) : Promise<void>

动态开启/关闭超分算法，可在 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' 状态下调用。使用Promise异步回调。

说明

* 在调用[prepare()](arkts-apis-media-avplayer.md#prepare9)前先通过[PlaybackStrategy](arkts-apis-media-i.md#playbackstrategy12)使能超分。
* 默认目标分辨率为1920x1080，单位为像素。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 表示是否开启超分。true表示开启超分，false表示关闭超分。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5410003 | Super-resolution not supported. Return by promise. |
| 5410004 | Missing enable super-resolution feature in [PlaybackStrategy](arkts-apis-media-i.md#playbackstrategy12). Return by promise. |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. let url: string = 'http://abc.bcd.efg/aa/test.mp4';    // 此处仅为示意，请替换为真实资源文件URL。
4. avPlayer.url = url;
5. let playStrategy : media.PlaybackStrategy = {
6. enableSuperResolution: true
7. };
8. avPlayer.setPlaybackStrategy(playStrategy);
9. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped状态后才能调用。
10. avPlayer.setSuperResolution(true);
11. }
```

## setVideoWindowSize18+

PhonePC/2in1TabletTVWearable

setVideoWindowSize(width: number, height: number) : Promise<void>

动态设置超分算法的输出分辨率。可在 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' 状态下调用。使用Promise异步回调。

输入参数须在320x320~1920x1080范围内，单位为像素。

在调用[prepare()](arkts-apis-media-avplayer.md#prepare9)前先通过[PlaybackStrategy](arkts-apis-media-i.md#playbackstrategy12)使能超分。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 超分算法的目标输出视频宽度，取值范围为[320-1920]，单位为像素。 |
| height | number | 是 | 超分算法的目标输出视频高度，取值范围为[320-1080]，单位为像素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5410003 | Super-resolution not supported. Return by promise. |
| 5410004 | Missing enable super-resolution feature in [PlaybackStrategy](arkts-apis-media-i.md#playbackstrategy12). Return by promise. |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. let url: string = 'http://abc.bcd.efg/aa/test.mp4';    // 此处仅为示意，请替换为真实资源文件URL。
4. avPlayer.url = url;
5. let playStrategy : media.PlaybackStrategy = {
6. enableSuperResolution: true
7. };
8. avPlayer.setPlaybackStrategy(playStrategy);
9. avPlayer.setSuperResolution(true);
10. // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped状态后才能调用。
11. avPlayer.setVideoWindowSize(1920, 1080);
12. }
```

## on('superResolutionChanged')18+

PhonePC/2in1TabletTVWearable

on(type:'superResolutionChanged', callback: OnSuperResolutionChanged): void

订阅监听超分算法开启/关闭事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'superResolutionChanged'，当超分算法开启/关闭状态变化时，触发该事件。 |
| callback | [OnSuperResolutionChanged](arkts-apis-media-t.md#onsuperresolutionchanged-18) | 是 | 超分开关事件回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 订阅监听超分算法开启/关闭事件。
4. avPlayer.on('superResolutionChanged', (enabled: boolean) => {
5. console.info('superResolutionChanged called, and enabled is:' + enabled);
6. });
7. }
```

## off('superResolutionChanged')18+

PhonePC/2in1TabletTVWearable

off(type:'superResolutionChanged', callback?: OnSuperResolutionChanged): void

取消监听超分算法开启/关闭事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'superResolutionChanged'，当超分算法开启/关闭状态变化时，触发该事件。 |
| callback | [OnSuperResolutionChanged](arkts-apis-media-t.md#onsuperresolutionchanged-18) | 否 | 超分开关事件回调方法。如果填写该参数，仅取消注册此回调方法，否则取消注册superResolutionChanged事件的所有回调方法。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. // 取消后，不再接收超分算法开启/关闭事件。
4. avPlayer.off('superResolutionChanged');
5. }
```

## getPlaybackStatisticMetrics23+

PhonePC/2in1TabletTVWearable

getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>

获取当前播放器的统计指标信息，可以在准备（prepared）/播放（playing）/暂停（paused）/完成（completed）/停止（stopped）状态调用。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PlaybackMetrics](arkts-apis-media-t.md#playbackmetrics23)> | Promise对象，返回当前播放器的指标信息PlaybackMetrics。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avPlayer: media.AVPlayer | undefined;
4. let playbackMetrics: media.PlaybackMetrics | undefined;
5. media.createAVPlayer(async (err: BusinessError, player: media.AVPlayer) => {
6. if (player != null) {
7. avPlayer = player;
8. console.info(`Succeeded in creating AVPlayer`);
9. if (avPlayer) {
10. try {
11. playbackMetrics = await avPlayer.getPlaybackStatisticMetrics();
12. console.info(`AVPlayer getPlaybackStatisticMetrics = ${JSON.stringify(playbackMetrics)}`); // 打印整个playbackMetrics的值。
13. } catch (error) {
14. console.error(`error = ${error}`);
15. }
16. }
17. } else {
18. console.error(`Failed to create AVPlayer, error message:${err.message}`);
19. }
20. });
```

## onMetricsEvent23+

PhonePC/2in1TabletTVWearable

onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void

订阅播放过程中的指标事件。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<[AVMetricsEvent](arkts-apis-media-i.md#avmetricsevent23)>> | 是 | 上报的指标事件信息的方法。使用callback异步回调。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. avPlayer.onMetricsEvent((info: Array<media.AVMetricsEvent>) => {
4. if (info) {
5. for (let i = 0; i < info.length; i++) {
6. console.info('metrics info: index=' + i + ' info=' + JSON.stringify(info));
7. }
8. } else {
9. console.info('metrics info is null');
10. }
11. });
12. }
```

## offMetricsEvent23+

PhonePC/2in1TabletTVWearable

offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void

取消订阅播放过程中的指标事件。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<[AVMetricsEvent](arkts-apis-media-i.md#avmetricsevent23)>> | 否 | 上报的指标事件信息的方法。使用callback异步回调。 |

**示例：**

```
1. async function test(){
2. let avPlayer = await media.createAVPlayer();
3. avPlayer.offMetricsEvent();
4. }
```
