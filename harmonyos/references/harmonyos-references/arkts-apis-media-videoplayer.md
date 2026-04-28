---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-videoplayer
title: 废弃的Interface (VideoPlayer, deprecated)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > 废弃的Interface (VideoPlayer, deprecated)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a133744a07ffd0d9307ec911f778bfd2803f1e12b681c2b7f252ab82859efde5
---

视频播放管理类，用于管理和播放视频媒体。在调用VideoPlayer的方法前，需要先通过[createVideoPlayer()](arkts-apis-media-f.md#mediacreatevideoplayerdeprecated)构建一个VideoPlayer实例。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer](arkts-apis-media-avplayer.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url8+ | string | 否 | 否 | 视频媒体URL，支持当前主流的视频格式(mp4、mpeg-ts、mkv)。  **支持路径示例**：  1. fd类型播放：fd://xx    2. http网络播放: http://xx  3. https网络播放: https://xx  4. hls网络播放路径：http://xx或者https://xx  5. file类型: file://xx  **说明：**  从API version 11开始不支持webm。 |
| fdSrc9+ | [AVFileDescriptor](arkts-apis-media-i.md#avfiledescriptor9) | 否 | 否 | 视频媒体文件描述，使用场景：应用中的视频资源被连续存储在同一个文件中。  **使用示例**：  假设一个连续存储的音乐文件:  视频1(地址偏移:0，字节长度:100)  视频2(地址偏移:101，字节长度:50)  视频3(地址偏移:151，字节长度:150)  1. 播放视频1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }  2. 播放视频2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; }  3. 播放视频3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; }  假设是一个独立的视频文件: 请使用src=fd://xx |
| loop8+ | boolean | 否 | 否 | 视频循环播放属性，设置为'true'表示循环播放。 |
| videoScaleType9+ | [VideoScaleType](arkts-apis-media-e.md#videoscaletype9) | 否 | 是 | 视频缩放模式。默认值为VIDEO\_SCALE\_TYPE\_FIT。 |
| audioInterruptMode9+ | [audio.InterruptMode](arkts-apis-audio-e.md#interruptmode9) | 否 | 是 | 音频焦点模式。 |
| currentTime8+ | number | 是 | 否 | 视频的当前播放位置，单位为毫秒（ms）。 |
| duration8+ | number | 是 | 否 | 视频时长，单位为毫秒（ms），返回-1表示直播模式。 |
| state8+ | [VideoPlayState](arkts-apis-media-t.md#videoplaystatedeprecated) | 是 | 否 | 视频播放的状态。 |
| width8+ | number | 是 | 否 | 视频宽，单位为像素（px）。 |
| height8+ | number | 是 | 否 | 视频高，单位为像素（px）。 |

## setDisplaySurface(deprecated)

PhonePC/2in1TabletTVWearable

setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void

设置SurfaceId。通过回调函数获取返回值。

说明

* SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。
* 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.surfaceId](arkts-apis-media-avplayer.md#属性)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考[XComponent](ts-basic-components-xcomponent.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置SurfaceId成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let surfaceId: string = '';
4. videoPlayer.setDisplaySurface(surfaceId, (err: BusinessError) => {
5. if (err) {
6. console.error('Failed to set DisplaySurface!');
7. } else {
8. console.info('Succeeded in setting DisplaySurface!');
9. }
10. });
```

## setDisplaySurface(deprecated)

PhonePC/2in1TabletTVWearable

setDisplaySurface(surfaceId: string): Promise<void>

设置SurfaceId。通过Promise获取返回值。

说明

* SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。
* 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.surfaceId](arkts-apis-media-avplayer.md#属性)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考[XComponent](ts-basic-components-xcomponent.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 设置SurfaceId的Promise返回值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let surfaceId: string = '';
4. videoPlayer.setDisplaySurface(surfaceId).then(() => {
5. console.info('Succeeded in setting DisplaySurface');
6. }).catch((error: BusinessError) => {
7. console.error(`video catchCallback, error:${error}`);
8. });
```

## prepare(deprecated)

PhonePC/2in1TabletTVWearable

prepare(callback: AsyncCallback<void>): void

准备播放视频。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.prepare](arkts-apis-media-avplayer.md#prepare9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当准备播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.prepare((err: BusinessError) => {
4. if (err) {
5. console.error('Failed to prepare!');
6. } else {
7. console.info('Succeeded in preparing!');
8. }
9. });
```

## prepare(deprecated)

PhonePC/2in1TabletTVWearable

prepare(): Promise<void>

准备播放视频。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.prepare](arkts-apis-media-avplayer.md#prepare9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 准备播放视频的Promise返回值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.prepare().then(() => {
4. console.info('Succeeded in preparing');
5. }).catch((error: BusinessError) => {
6. console.error(`video catchCallback, error:${error}`);
7. });
```

## play(deprecated)

PhonePC/2in1TabletTVWearable

play(callback: AsyncCallback<void>): void

开始播放视频。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.play](arkts-apis-media-avplayer.md#play9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当开始播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.play((err: BusinessError) => {
4. if (err) {
5. console.error('Failed to play!');
6. } else {
7. console.info('Succeeded in playing!');
8. }
9. });
```

## play(deprecated)

PhonePC/2in1TabletTVWearable

play(): Promise<void>

开始播放视频。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.play](arkts-apis-media-avplayer.md#play9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 开始播放视频的Promise返回值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.play().then(() => {
4. console.info('Succeeded in playing');
5. }).catch((error: BusinessError) => {
6. console.error(`video catchCallback, error:${error}`);
7. });
```

## pause(deprecated)

PhonePC/2in1TabletTVWearable

pause(callback: AsyncCallback<void>): void

通过回调方式暂停播放视频。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.pause](arkts-apis-media-avplayer.md#pause9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当暂停播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.pause((err: BusinessError) => {
4. if (err) {
5. console.error('Failed to pause!');
6. } else {
7. console.info('Succeeded in pausing!');
8. }
9. });
```

## pause(deprecated)

PhonePC/2in1TabletTVWearable

pause(): Promise<void>

暂停播放视频。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.pause](arkts-apis-media-avplayer.md#pause9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 暂停播放视频的Promise返回值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.pause().then(() => {
4. console.info('Succeeded in pausing');
5. }).catch((error: BusinessError) => {
6. console.error(`video catchCallback, error:${error}`);
7. });
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

通过回调方式停止播放视频。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.stop](arkts-apis-media-avplayer.md#stop9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.stop((err: BusinessError) => {
4. if (err) {
5. console.error('Failed to stop!');
6. } else {
7. console.info('Succeeded in stopping!');
8. }
9. });
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止播放视频。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.stop](arkts-apis-media-avplayer.md#stop9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 停止播放视频的Promise返回值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.stop().then(() => {
4. console.info('Succeeded in stopping');
5. }).catch((error: BusinessError) => {
6. console.error(`video catchCallback, error:${error}`);
7. });
```

## reset(deprecated)

PhonePC/2in1TabletTVWearable

reset(callback: AsyncCallback<void>): void

重置播放视频。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.reset](arkts-apis-media-avplayer.md#reset9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当重置播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.reset((err: BusinessError) => {
4. if (err) {
5. console.error('Failed to reset!');
6. } else {
7. console.info('Succeeded in resetting!');
8. }
9. });
```

## reset(deprecated)

PhonePC/2in1TabletTVWearable

reset(): Promise<void>

重置播放视频。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.reset](arkts-apis-media-avplayer.md#reset9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.reset().then(() => {
4. console.info('Succeeded in resetting');
5. }).catch((error: BusinessError) => {
6. console.error(`video catchCallback, error:${error}`);
7. });
```

## seek(deprecated)

PhonePC/2in1TabletTVWearable

seek(timeMs: number, callback: AsyncCallback<number>): void

跳转到指定播放位置，默认跳转到指定时间点的上一个关键帧。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-apis-media-avplayer.md#seek9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| callback | AsyncCallback<number> | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let videoPlayer: media.VideoPlayer;
4. media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
5. if (video != null) {
6. videoPlayer = video;
7. console.info('Succeeded in creating VideoPlayer');
8. } else {
9. console.error(`Failed to create VideoPlayer, error:${error}`);
10. }
11. });

13. let seekTime: number = 5000;
14. videoPlayer.seek(seekTime, (err: BusinessError, result: number) => {
15. if (err) {
16. console.error('Failed to do seek!');
17. } else {
18. console.info('Succeeded in doing seek!');
19. }
20. });
```

## seek(deprecated)

PhonePC/2in1TabletTVWearable

seek(timeMs: number, mode:SeekMode, callback: AsyncCallback<number>): void

跳转到指定播放位置。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-apis-media-avplayer.md#seek9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| mode | [SeekMode](arkts-apis-media-e.md#seekmode8) | 是 | 跳转模式。 |
| callback | AsyncCallback<number> | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let videoPlayer: media.VideoPlayer | null = null;
4. media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
5. if (video != null) {
6. videoPlayer = video;
7. console.info('Succeeded in creating VideoPlayer');
8. } else {
9. console.error(`Failed to create VideoPlayer, error:${error}`);
10. }
11. });
12. let seekTime: number = 5000;
13. if (videoPlayer) {
14. (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC, (err: BusinessError, result: number) => {
15. if (err) {
16. console.error('Failed to do seek!');
17. } else {
18. console.info('Succeeded in doing seek!');
19. }
20. });
21. }
```

## seek(deprecated)

PhonePC/2in1TabletTVWearable

seek(timeMs: number, mode?:SeekMode): Promise<number>

跳转到指定播放位置，如果没有设置mode则跳转到指定时间点的上一个关键帧。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-apis-media-avplayer.md#seek9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| mode | [SeekMode](arkts-apis-media-e.md#seekmode8) | 否 | 基于视频I帧的跳转模式，默认为SEEK\_PREV\_SYNC模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 跳转到指定播放位置的Promise返回值，单位ms。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let videoPlayer: media.VideoPlayer | null = null;
4. media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
5. if (video != null) {
6. videoPlayer = video;
7. console.info('Succeeded in creating VideoPlayer');
8. } else {
9. console.error(`Failed to create VideoPlayer, error:${error}`);
10. }
11. });
12. let seekTime: number = 5000;
13. if (videoPlayer) {
14. (videoPlayer as media.VideoPlayer).seek(seekTime).then((seekDoneTime: number) => { // seekDoneTime表示seek完成后的时间点。
15. console.info('Succeeded in doing seek');
16. }).catch((error: BusinessError) => {
17. console.error(`video catchCallback, error:${error}`);
18. });

20. (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC).then((seekDoneTime: number) => {
21. console.info('Succeeded in doing seek');
22. }).catch((error: BusinessError) => {
23. console.error(`video catchCallback, error:${error}`);
24. });
25. }
```

## setVolume(deprecated)

PhonePC/2in1TabletTVWearable

setVolume(vol: number, callback: AsyncCallback<void>): void

设置音量。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setVolume](arkts-apis-media-avplayer.md#setvolume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vol | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置音量成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let vol: number = 0.5;
4. videoPlayer.setVolume(vol, (err: BusinessError) => {
5. if (err) {
6. console.error('Failed to set Volume!');
7. } else {
8. console.info('Succeeded in setting Volume!');
9. }
10. });
```

## setVolume(deprecated)

PhonePC/2in1TabletTVWearable

setVolume(vol: number): Promise<void>

设置音量。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setVolume](arkts-apis-media-avplayer.md#setvolume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vol | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 设置音量的Promise返回值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let vol: number = 0.5;
4. videoPlayer.setVolume(vol).then(() => {
5. console.info('Succeeded in setting Volume');
6. }).catch((error: BusinessError) => {
7. console.error(`video catchCallback, error:${error}`);
8. });
```

## release(deprecated)

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放视频资源。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.release](arkts-apis-media-avplayer.md#release9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放视频资源成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.release((err: BusinessError) => {
4. if (err) {
5. console.error('Failed to release!');
6. } else {
7. console.info('Succeeded in releasing!');
8. }
9. });
```

## release(deprecated)

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放视频资源。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.release](arkts-apis-media-avplayer.md#release9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 释放视频资源的Promise返回值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.release().then(() => {
4. console.info('Succeeded in releasing');
5. }).catch((error: BusinessError) => {
6. console.error(`video catchCallback, error:${error}`);
7. });
```

## getTrackDescription(deprecated)

PhonePC/2in1TabletTVWearable

getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void

获取视频轨道信息。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.getTrackDescription](arkts-apis-media-avplayer.md#gettrackdescription9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[MediaDescription](arkts-apis-media-i.md#mediadescription8)>> | 是 | 回调函数。获取视频轨道信息成功时，err为undefined，data为获取到的视频轨道信息MediaDescription数组，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
4. if ((arrList) != null) {
5. console.info('Succeeded in getting TrackDescription');
6. } else {
7. console.error(`Failed to get TrackDescription, error:${error}`);
8. }
9. });
```

## getTrackDescription(deprecated)

PhonePC/2in1TabletTVWearable

getTrackDescription(): Promise<Array<MediaDescription>>

获取视频轨道信息。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.getTrackDescription](arkts-apis-media-avplayer.md#gettrackdescription9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[MediaDescription](arkts-apis-media-i.md#mediadescription8)>> | Promise对象，返回获取的视频轨道信息MediaDescription数组。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
4. if (arrList != null) {
5. console.info('Succeeded in getting TrackDescription');
6. } else {
7. console.error('Failed to get TrackDescription');
8. }
9. }).catch((error: BusinessError) => {
10. console.error(`video catchCallback, error:${error}`);
11. });
```

## setSpeed(deprecated)

PhonePC/2in1TabletTVWearable

setSpeed(speed: number, callback: AsyncCallback<number>): void

设置播放速度。通过回调函数获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setSpeed](arkts-apis-media-avplayer.md#setspeed9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 是 | 指定播放视频速度，具体见[PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8)。 |
| callback | AsyncCallback<number> | 是 | 回调函数。设置播放速度成功时，err为undefined，data为设置的播放速度，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let videoPlayer: media.VideoPlayer | null = null;
4. media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
5. if (video != null) {
6. videoPlayer = video;
7. console.info('Succeeded in creating VideoPlayer');
8. } else {
9. console.error(`Failed to create VideoPlayer, error:${error}`);
10. }
11. });
12. let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
13. if (videoPlayer) {
14. (videoPlayer as media.VideoPlayer).setSpeed(speed, (err: BusinessError, result: number) => {
15. if (err) {
16. console.error('Failed to set Speed!');
17. } else {
18. console.info('Succeeded in setting Speed!');
19. }
20. });
21. }
```

## setSpeed(deprecated)

PhonePC/2in1TabletTVWearable

setSpeed(speed: number): Promise<number>

设置播放速度。通过Promise获取返回值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setSpeed](arkts-apis-media-avplayer.md#setspeed9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 是 | 指定播放视频速度，具体见[PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回设置的播放速度，具体见[PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let videoPlayer: media.VideoPlayer | null = null;
4. media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
5. if (video != null) {
6. videoPlayer = video;
7. console.info('Succeeded in creating VideoPlayer');
8. } else {
9. console.error(`Failed to create VideoPlayer, error:${error}`);
10. }
11. });
12. let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
13. if (videoPlayer) {
14. (videoPlayer as media.VideoPlayer).setSpeed(speed).then((result: number) => {
15. console.info('Succeeded in setting Speed');
16. }).catch((error: BusinessError) => {
17. console.error(`Failed to set Speed, error:${error}`);// todo:: error.
18. });
19. }
```

## on('playbackCompleted')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'playbackCompleted', callback: Callback<void>): void

开始监听视频播放完成事件。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('stateChange')](arkts-apis-media-avplayer.md#onstatechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放完成事件回调类型，支持的事件：'playbackCompleted'。 |
| callback | Callback<void> | 是 | 视频播放完成事件回调方法。 |

**示例：**

```
1. videoPlayer.on('playbackCompleted', () => {
2. console.info('playbackCompleted called!');
3. });
```

## on('bufferingUpdate')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void

开始监听视频缓存更新事件。仅网络播放支持该订阅事件。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('bufferingUpdate')](arkts-apis-media-avplayer.md#onbufferingupdate9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频缓存事件回调类型，支持的事件：'bufferingUpdate'。 |
| callback | function | 是 | 视频缓存事件回调方法。  [BufferingInfoType](arkts-apis-media-e.md#bufferinginfotype8)value值固定为0。 |

**示例：**

```
1. videoPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
2. console.info('video bufferingInfo type: ' + infoType);
3. console.info('video bufferingInfo value: ' + value);
4. });
```

## on('startRenderFrame')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'startRenderFrame', callback: Callback<void>): void

开始监听视频播放首帧送显上报事件。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('startRenderFrame')](arkts-apis-media-avplayer.md#onstartrenderframe9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放首帧送显上报事件回调类型，支持的事件：'startRenderFrame'。 |
| callback | Callback<void> | 是 | 视频播放首帧送显上报事件回调方法。 |

**示例：**

```
1. videoPlayer.on('startRenderFrame', () => {
2. console.info('startRenderFrame called!');
3. });
```

## on('videoSizeChanged')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void

开始监听视频播放宽高变化事件。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('videoSizeChange')](arkts-apis-media-avplayer.md#onvideosizechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放宽高变化事件回调类型，支持的事件：'videoSizeChanged'。 |
| callback | function | 是 | 视频播放宽高变化事件回调方法，width表示宽，height表示高。 |

**示例：**

```
1. videoPlayer.on('videoSizeChanged', (width: number, height: number) => {
2. console.info('video width is: ' + width);
3. console.info('video height is: ' + height);
4. });
```

## on('audioInterrupt')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void

监听音频焦点变化事件，参考[audio.InterruptEvent](arkts-apis-audio-i.md#interruptevent9)。

说明

从API version 9开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('audioInterrupt')](arkts-apis-media-avplayer.md#onaudiointerrupt9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 音频焦点变化事件回调类型，支持的事件：'audioInterrupt'。 |
| callback | function | 是 | 音频焦点变化事件回调方法。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. videoPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
4. console.info('audioInterrupt called,and InterruptEvent info is:' + info);
5. });
```

## on('error')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

开始监听视频播放错误事件，当上报error错误事件后，用户需处理error事件，退出播放操作。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('error')](arkts-apis-media-avplayer.md#onerror9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 播放错误事件回调类型，支持的事件包括：'error'。  - 'error'：视频播放中发生错误，触发该事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 播放错误事件回调方法。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. videoPlayer.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
4. console.error(`video error called, error: ${error}`);
5. });
6. videoPlayer.url = 'fd://error';  // 设置错误的播放地址，触发'error'事件。
```
