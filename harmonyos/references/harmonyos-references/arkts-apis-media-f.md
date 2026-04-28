---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f
title: Functions
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:13:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9839ab9c4a91b0983299000120df80aab22041bf586220684e44bba87b0cbd7a
---

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## media.createAVPlayer9+

PhonePC/2in1TabletTVWearable

createAVPlayer(callback: AsyncCallback<AVPlayer>): void

创建音视频播放实例。使用callback异步回调。

说明

* 推荐单个应用创建的音视频播放实例（即音频、视频、音视频三类相加）不超过16个。
* 应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVPlayer](arkts-apis-media-avplayer.md)> | 是 | 回调函数。异步返回AVPlayer实例，失败时返回null。可用于音视频播放。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avPlayer: media.AVPlayer;
4. media.createAVPlayer((error: BusinessError, video: media.AVPlayer) => {
5. if (video) {
6. avPlayer = video;
7. console.info('Succeeded in creating AVPlayer');
8. } else {
9. console.error(`Failed to create AVPlayer, error message:${error.message}`);
10. }
11. });
```

## media.createAVPlayer9+

PhonePC/2in1TabletTVWearable

createAVPlayer(): Promise<AVPlayer>

异步方式创建音视频播放实例。使用Promise异步回调。

说明

* 推荐单个应用创建的音视频播放实例（即音频、视频、音视频三类相加）不超过16个。
* 应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，导致系统终止应用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVPlayer](arkts-apis-media-avplayer.md)> | Promise对象。成功时异步返回AVPlayer实例，可用于音视频播放。失败时返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avPlayer: media.AVPlayer;
4. media.createAVPlayer().then((video: media.AVPlayer) => {
5. if (video) {
6. avPlayer = video;
7. console.info('Succeeded in creating AVPlayer');
8. } else {
9. console.error('Failed to create AVPlayer');
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to create AVPlayer, error message:${error.message}`);
13. });
```

## media.createAVRecorder9+

PhonePC/2in1TabletTVWearable

createAVRecorder(callback: AsyncCallback<AVRecorder>): void

创建音视频录制实例。使用callback异步回调。

说明

应用可创建多个音视频录制实例，但由于设备共用音频通路，一个设备仅能有一个实例进行音频录制。创建第二个实例录制音频时，将会因为音频通路冲突导致创建失败。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVRecorder](arkts-apis-media-avrecorder.md)> | 是 | 回调函数，返回AVRecorder实例，可用于录制音视频媒体。失败时返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let avRecorder: media.AVRecorder;

4. media.createAVRecorder((error: BusinessError, recorder: media.AVRecorder) => {
5. if (recorder) {
6. avRecorder = recorder;
7. console.info('Succeeded in creating AVRecorder');
8. } else {
9. console.error(`Failed to create AVRecorder, error message:${error.message}`);
10. }
11. });
```

## media.createAVRecorder9+

PhonePC/2in1TabletTVWearable

createAVRecorder(): Promise<AVRecorder>

创建音视频录制实例。使用Promise异步回调。

说明

应用可创建多个音视频录制实例，但由于设备共用音频通路，一个设备仅能有一个实例进行音频录制。创建第二个实例录制音频时，将会因为音频通路冲突导致创建失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVRecorder](arkts-apis-media-avrecorder.md)> | Promise对象，返回AVRecorder实例，可用于录制音视频媒体。失败时返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let avRecorder: media.AVRecorder;
3. media.createAVRecorder().then((recorder: media.AVRecorder) => {
4. if (recorder) {
5. avRecorder = recorder;
6. console.info('Succeeded in creating AVRecorder');
7. } else {
8. console.error('Failed to create AVRecorder');
9. }
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to create AVRecorder, error message:${error.message}`);
12. });
```

## media.createAVTranscoder12+

PhonePC/2in1TabletTV

createAVTranscoder(): Promise<AVTranscoder>

创建视频转码实例。使用Promise异步回调。

说明

可创建的视频转码实例不能超过2个。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVTranscoder](arkts-apis-media-avtranscoder.md)> | Promise对象。异步返回AVTranscoder实例，失败时返回null。可用于视频转码。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avTranscoder: media.AVTranscoder | undefined = undefined;
4. media.createAVTranscoder().then((transcoder: media.AVTranscoder) => {
5. if (transcoder) {
6. avTranscoder = transcoder;
7. console.info('Succeeded in creating AVTranscoder');
8. } else {
9. console.error('Failed to create AVTranscoder');
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to create AVTranscoder, error message:${error.message}`);
13. });
```

## media.createAVMetadataExtractor11+

PhonePC/2in1TabletTVWearable

createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void

创建AVMetadataExtractor实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVMetadataExtractor](arkts-apis-media-avmetadataextractor.md)> | 是 | 回调函数。当创建AVMetadataExtractor实例成功，err为undefined，data为获取到的AVMetadataExtractor实例，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Returned by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avMetadataExtractor: media.AVMetadataExtractor;
4. media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
5. if (extractor) {
6. avMetadataExtractor = extractor;
7. console.info('Succeeded in creating AVMetadataExtractor');
8. } else {
9. console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
10. }
11. });
```

## media.createAVMetadataExtractor11+

PhonePC/2in1TabletTVWearable

createAVMetadataExtractor(): Promise<AVMetadataExtractor>

创建AVMetadataExtractor实例。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVMetadataExtractor](arkts-apis-media-avmetadataextractor.md)> | Promise对象。异步返回元数据获取类对象（AVMetadataExtractor）。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avMetadataExtractor: media.AVMetadataExtractor;
4. media.createAVMetadataExtractor().then((extractor: media.AVMetadataExtractor) => {
5. if (extractor) {
6. avMetadataExtractor = extractor;
7. console.info('Succeeded in creating AVMetadataExtractor');
8. } else {
9. console.error(`Failed to create AVMetadataExtractor`);
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
13. });
```

## media.createSoundPool10+

PhonePC/2in1TabletTVWearable

createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo, callback: AsyncCallback<SoundPool>): void

创建音频池实例。使用callback异步回调。

说明

* API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。
* API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxStreams | number | 是 | soundPool实例的最大播放的流数，设置范围为1-32的正整数。 |
| audioRenderInfo | [audio.AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 是 | 音频播放参数信息。其中audioRenderInfo中的参数usage取值为STREAM\_USAGE\_UNKNOWN，STREAM\_USAGE\_MUSIC，STREAM\_USAGE\_MOVIE，STREAM\_USAGE\_AUDIOBOOK时，SoundPool播放短音时为混音模式，不会打断其他音频播放。SoundPool支持将rendererFlags设置为1用于低时延通路播放。 |
| callback | AsyncCallback<[SoundPool](js-apis-inner-multimedia-soundpool.md)> | 是 | 回调函数。异步返回SoundPool实例，失败时返回null。用于音频池实例的加载播放功能。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by callback. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let soundPool: media.SoundPool;
4. let audioRendererInfo: audio.AudioRendererInfo = {
5. usage : audio.StreamUsage.STREAM_USAGE_MUSIC,
6. rendererFlags : 0
7. };

9. media.createSoundPool(5, audioRendererInfo, (error, soundPool_: media.SoundPool) => {
10. if (error) {
11. console.error(`Failed to createSoundPool`);
12. return;
13. } else {
14. soundPool = soundPool_;
15. console.info(`Succeeded in createSoundPool`);
16. }
17. });
```

## media.createSoundPool10+

PhonePC/2in1TabletTVWearable

createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>

创建音频池实例。使用Promise异步回调。

说明

* API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。
* API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxStreams | number | 是 | soundPool实例的最大播放的流数，设置范围为1-32的正整数。 |
| audioRenderInfo | [audio.AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 是 | 音频播放参数信息 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SoundPool](js-apis-inner-multimedia-soundpool.md)> | Promise对象。异步返回SoundPool实例，失败时返回null。用于音频池实例的加载播放功能。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let soundPool: media.SoundPool;
5. let audioRendererInfo: audio.AudioRendererInfo = {
6. usage : audio.StreamUsage.STREAM_USAGE_MUSIC,
7. rendererFlags : 0
8. };

10. media.createSoundPool(5, audioRendererInfo).then((soundpool_: media.SoundPool) => {
11. if (soundpool_) {
12. soundPool = soundpool_;
13. console.info('Succeeded in creating SoundPool');
14. } else {
15. console.error('Failed to create SoundPool');
16. }
17. }, (error: BusinessError) => {
18. console.error(`soundpool catchCallback, error message:${error.message}`);
19. });
```

## media.createAVScreenCaptureRecorder12+

PhonePC/2in1TabletTV

createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>

创建屏幕录制实例，使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVScreenCaptureRecorder](arkts-apis-media-avscreencapturerecorder.md)> | Promise对象，返回AVScreenCaptureRecorder实例，失败时返回null。可用于进行屏幕录制。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder;
4. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
5. if (captureRecorder) {
6. avScreenCaptureRecorder = captureRecorder;
7. console.info('Succeeded in createAVScreenCaptureRecorder');
8. } else {
9. console.error('Failed to createAVScreenCaptureRecorder');
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
13. });
```

## media.createAVImageGenerator12+

PhonePC/2in1TabletTVWearable

createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void

创建AVImageGenerator实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVImageGenerator](arkts-apis-media-avimagegenerator.md)> | 是 | 回调函数。异步返回AVImageGenerator实例，失败时返回null。可用于获取视频缩略图。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Returned by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avImageGenerator: media.AVImageGenerator;
4. media.createAVImageGenerator((error: BusinessError, generator: media.AVImageGenerator) => {
5. if (generator) {
6. avImageGenerator = generator;
7. console.info('Succeeded in creating AVImageGenerator');
8. } else {
9. console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
10. }
11. });
```

## media.createAVImageGenerator12+

PhonePC/2in1TabletTVWearable

createAVImageGenerator(): Promise<AVImageGenerator>

创建AVImageGenerator对象。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVImageGenerator](arkts-apis-media-avimagegenerator.md)> | Promise对象。异步返回AVImageGenerator实例，失败时返回null。可用于获取视频缩略图。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let avImageGenerator: media.AVImageGenerator;
4. media.createAVImageGenerator().then((generator: media.AVImageGenerator) => {
5. if (generator) {
6. avImageGenerator = generator;
7. console.info('Succeeded in creating AVImageGenerator');
8. } else {
9. console.error('Failed to create AVImageGenerator');
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
13. });
```

## media.createMediaSourceWithUrl12+

PhonePC/2in1TabletTVWearable

createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource

创建流媒体预下载媒体来源实例方法。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | - 流媒体预下载媒体来源url，支持的流媒体格式：HLS、HTTP-FLV、Dash、Https。  - 本地m3u8的fd路径。 |
| headers | Record<string, string> | 否 | 支持流媒体预下载HttpHeader自定义。不传时为网络请求默认的HttpHeader。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaSource](arkts-apis-media-mediasource.md) | MediaSource返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400101 | No memory. |

**示例1：**

```
1. let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
2. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
```

**示例2：**

```
1. import { media } from "@kit.MediaKit";

3. async function test(context: Context){
4. // this.getUIContext().getHostContext();
5. let mgr = context?.resourceManager;
6. if (!mgr) {
7. return;
8. }
9. let fileDescriptor = await mgr.getRawFd("xxx.m3u8");

11. let fd: string = fileDescriptor.fd.toString();
12. let offset: string = fileDescriptor.offset.toString();
13. let length: string = fileDescriptor.length.toString();
14. let fdUrl: string = "fd://" + fd + "?offset=" + offset + "&size=" + length;

16. let mediaSource: media.MediaSource = media.createMediaSourceWithUrl(fdUrl);
17. }
```

## media.createMediaSourceWithStreamData19+

PhonePC/2in1TabletTVWearable

createMediaSourceWithStreamData(streams: Array<MediaStream>): MediaSource

创建流媒体多码率媒体来源实例方法，当前仅支持HTTP-FLV协议格式多码率。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streams | Array<[MediaStream](arkts-apis-media-i.md#mediastream19)> | 是 | 可设置MediaStream数组，支持的流媒体格式：HTTP-FLV。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaSource](arkts-apis-media-mediasource.md) | 返回MediaSource，用于媒体资源设置。 |

**示例：**

```
1. let streams : Array<media.MediaStream> = [];
2. streams.push({url: "http://xxx/480p.flv", width: 854, height: 480, bitrate: 800000});
3. streams.push({url: "http://xxx/720p.flv", width: 1280, height: 720, bitrate: 2000000});
4. streams.push({url: "http://xxx/1080p.flv", width: 1920, height: 1080, bitrate: 2000000});
5. let mediaSource : media.MediaSource = media.createMediaSourceWithStreamData(streams);
```

## media.createAudioPlayer(deprecated)

PhonePC/2in1TabletTVWearable

createAudioPlayer(): AudioPlayer

同步方式创建音频播放实例。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[createAVPlayer](arkts-apis-media-f.md#mediacreateavplayer9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioPlayer](arkts-apis-media-audioplayer.md) | 返回AudioPlayer类实例，失败时返回null。可用于音频播放、暂停、停止等操作。 |

**示例：**

```
1. let audioPlayer: media.AudioPlayer = media.createAudioPlayer();
```

## media.createVideoPlayer(deprecated)

PhonePC/2in1TabletTVWearable

createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void

异步方式创建视频播放实例，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[createAVPlayer](arkts-apis-media-f.md#mediacreateavplayer9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[VideoPlayer](arkts-apis-media-videoplayer.md)> | 是 | 回调函数。创建VideoPlayer实例成功时，err为undefined，data为获取到的VideoPlayer实例，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let videoPlayer: media.VideoPlayer;
4. media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
5. if (video) {
6. videoPlayer = video;
7. console.info('Succeeded in creating VideoPlayer');
8. } else {
9. console.error(`Failed to create VideoPlayer, error:${error}`);
10. }
11. });
```

## media.createVideoPlayer(deprecated)

PhonePC/2in1TabletTVWearable

createVideoPlayer(): Promise<VideoPlayer>

异步方式创建视频播放实例，通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[createAVPlayer](arkts-apis-media-f.md#mediacreateavplayer9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[VideoPlayer](arkts-apis-media-videoplayer.md)> | Promise对象。异步返回VideoPlayer实例，失败时返回null。可用于管理和播放视频媒体。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let videoPlayer: media.VideoPlayer;
4. media.createVideoPlayer().then((video: media.VideoPlayer) => {
5. if (video) {
6. videoPlayer = video;
7. console.info('Succeeded in creating VideoPlayer');
8. } else {
9. console.error('Failed to create VideoPlayer');
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to create VideoPlayer, error:${error}`);
13. });
```

## media.createAudioRecorder(deprecated)

PhonePC/2in1TabletTVWearable

createAudioRecorder(): AudioRecorder

创建音频录制的实例来控制音频的录制。一台设备只允许创建一个录制实例。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[createAVRecorder](arkts-apis-media-f.md#mediacreateavrecorder9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**返回值:**

| 类型 | 说明 |
| --- | --- |
| [AudioRecorder](arkts-apis-media-audiorecorder.md) | 返回AudioRecorder类实例，失败时返回null。可用于录制音频媒体。 |

**示例：**

```
1. let audioRecorder: media.AudioRecorder = media.createAudioRecorder();
```
