---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool
title: SoundPool (音频池)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > multimedia > SoundPool (音频池)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:46+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bc88f1b8894dd99248fbb39e066366f15b8cadee42d26a284fdd4566e48e4bc6
---

音频池提供了短音频的加载、播放、音量设置、循环设置、停止播放、资源卸载等功能。

SoundPool需要和@ohos.multimedia.media配合使用，需要先通过[media.createSoundPool](arkts-apis-media-f.md#mediacreatesoundpool10)完成音频池实例的创建。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
2. import { audio } from '@kit.AudioKit';
```

## PlayParameters

PhonePC/2in1TabletTVWearable

表示音频池播放参数设置。

通过设置播放相关参数，来控制播放的音量，循环次数，播放优先级等参数。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| loop | number | 否 | 是 | 设置循环次数。  当loop≥0时，实际播放次数为loop+1。  当loop＜0时，表示一直循环。  默认值：0，表示仅播放一次。  当loop为浮点数时只截取整数部分。 |
| rate | number | 否 | 是 | 设置音频播放的倍速，具体倍速范围参照[AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8)。默认值：0。 |
| leftVolume | number | 否 | 是 | 设置左声道音量。设置范围为[0.0, 1.0]，默认值为1.0。  当音量超过边界值时自动设置为边界值。 |
| rightVolume | number | 否 | 是 | 设置右声道音量（当前不支持左右分别设置，将以左声道音量为准）。设置范围为[0.0, 1.0]，默认值为1.0。  当音量超过边界值时自动设置为边界值。 |
| priority | number | 否 | 是 | 音频流播放的优先级。0为最低优先级，数值越大优先级越高。  通过相互比较数值大小确定播放优先级，设置范围为大于等于0的整数。默认值为0。  当优先级为负数时自动设置为0，为浮点数时只截取整数部分。 |

## ErrorType20+

PhonePC/2in1TabletTVWearable

枚举，错误类型（用于区分错误发生阶段）。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOAD\_ERROR | 1 | 表示加载资源时发生错误。 |
| PLAY\_ERROR | 2 | 表示播放资源时发生错误。 |

## ErrorInfo20+

PhonePC/2in1TabletTVWearable

错误信息。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| errorCode | T | 否 | 否 | 错误码。errorCode的类型T为[BusinessError](js-apis-base.md#businesserror)类型。 |
| errorType | [ErrorType](js-apis-inner-multimedia-soundpool.md#errortype20) | 否 | 是 | 表示错误发生阶段。 |
| soundId | number | 否 | 是 | 发生错误的资源ID，load方法能够获取soundId。 |
| streamId | number | 否 | 是 | 发生错误的音频流ID，play方法能够获取streamId。 |

## SoundPool

PhonePC/2in1TabletTVWearable

音频池提供了系统声音的加载、播放、音量设置、循环设置、停止播放和资源卸载等功能，在调用SoundPool的接口前，需要先通过[media.createSoundPool](arkts-apis-media-f.md#mediacreatesoundpool10)创建实例。

说明

* 在使用SoundPool实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。
  + [on('loadComplete')](js-apis-inner-multimedia-soundpool.md#onloadcomplete)：监听资源加载完成。建议开发者监听此回调以确保音频在加载完成后进行播放。
  + [on('playFinishedWithStreamId')](js-apis-inner-multimedia-soundpool.md#onplayfinishedwithstreamid18)：监听播放完成，同时返回播放结束的音频的streamId。
  + [on('playFinished')](js-apis-inner-multimedia-soundpool.md#onplayfinished)：监听播放完成。
  + [on('error')](js-apis-inner-multimedia-soundpool.md#onerror)：监听错误事件。
  + [on('errorOccurred')](js-apis-inner-multimedia-soundpool.md#onerroroccurred20)：监听错误事件，同时返回[errorInfo](js-apis-inner-multimedia-soundpool.md#errorinfo20)。
* SoundPool目前不支持后台播放、设置音频打断等音频焦点策略和跳过音频头尾的静音帧。SoundPool低时延播放可参考[使用SoundPool播放短音频(ArkTS)](../harmonyos-guides/using-soundpool-for-playback.md)。

### load

PhonePC/2in1TabletTVWearable

load(uri: string, callback: AsyncCallback<number>): void

加载音频资源。使用callback异步回调。

通过callback异步回调获取资源ID，入参URL通过获取文件fd生成以"fd://"开头的文件描述字符串。

该方法不支持加载rawfile目录资源，需要通过[load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void](js-apis-inner-multimedia-soundpool.md#load-2)或者[load(fd: number, offset: number, length: number): Promise<number>](js-apis-inner-multimedia-soundpool.md#load-3)实现。

说明

* 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
* 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 音频文件的加载路径描述，一般以"fd://"开头的文件描述。 |
| callback | AsyncCallback<number> | 是 | 异步音频资源加载返回的资源id，有效值大于0。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { media } from '@kit.MediaKit';
4. import { audio } from '@kit.AudioKit';

6. // 创建soundPool实例。
7. let soundPool: media.SoundPool;
8. let audioRendererInfo: audio.AudioRendererInfo = {
9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
10. rendererFlags: 1
11. }
12. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
13. if (error) {
14. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
15. return;
16. } else {
17. soundPool = soundPool_;
18. console.info(`Succeeded in creating SoundPool`);
19. let uri:string = "";
20. let file: fileIo.File;
21. // 获取fd的uri路径。
22. fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
23. file = file_;
24. console.info("file fd: " + file.fd);
25. uri = 'fd://' + (file.fd).toString();
26. soundPool.load(uri, (error: BusinessError, soundId_: number) => {
27. if (error) {
28. console.error(`Failed to load soundPool: Code: ${error.code}, message: ${error.message}`);
29. } else {
30. console.info(`Succeeded in loading soundPool` + JSON.stringify(soundId_));
31. }
32. });
33. }); // '/test_01.mp3' 作为样例，使用时需要传入文件对应路径。
34. }
35. });
```

### load

PhonePC/2in1TabletTVWearable

load(uri: string): Promise<number>

加载音频资源。使用Promise异步回调。

通过Promise异步回调获取资源ID，入参URL通过获取文件fd生成以"fd://"开头的文件描述字符串。

该方法不支持加载rawfile目录资源，需要通过[load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void](js-apis-inner-multimedia-soundpool.md#load-2)或者[load(fd: number, offset: number, length: number): Promise<number>](js-apis-inner-multimedia-soundpool.md#load-3)实现。

说明

* 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
* 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 音频文件的加载路径描述，一般以"fd://"开头的文件描述。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回资源的id，有效值大于0。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { media } from '@kit.MediaKit';
4. import { audio } from '@kit.AudioKit';

6. // 创建soundPool实例。
7. let soundPool: media.SoundPool;
8. let audioRendererInfo: audio.AudioRendererInfo = {
9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
10. rendererFlags: 1
11. }
12. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
13. if (error) {
14. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
15. return;
16. } else {
17. soundPool = soundPool_;
18. console.info(`Succeeded in creating SoundPool`);
19. let uri:string = "";
20. let soundID: number = 0;
21. let file: fileIo.File;
22. // 获取fd的uri路径。
23. fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
24. file = file_;
25. console.info("file fd: " + file.fd);
26. uri = 'fd://' + (file.fd).toString();
27. soundPool.load(uri).then((soundId: number) => {
28. console.info('Succeeded in loading uri');
29. soundID = soundId;
30. }, (err: BusinessError) => {
31. console.error('Failed to load soundPool. Code: ${err.code}, message: ${err.message}');
32. });
33. }); // '/test_01.mp3' 作为样例，使用时需要传入文件对应路径。
34. }
35. });
```

### load

PhonePC/2in1TabletTVWearable

load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void

加载音频资源。使用callback异步回调。

通过callback异步回调获取资源ID，入参可手动传入资源信息或通过读取应用内置资源自动获取。

说明

* 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
* 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 资源句柄，通过[resourceManager.getRawFd](js-apis-resource-manager.md#getrawfd9)获取。 |
| offset | number | 是 | 资源偏移量，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。 |
| length | number | 是 | 资源长度，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。 |
| callback | AsyncCallback<number> | 是 | 获取回调的soundID，有效值大于0。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例1：**

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { media } from '@kit.MediaKit';
4. import { audio } from '@kit.AudioKit';

6. // 创建soundPool实例。
7. let soundPool: media.SoundPool;
8. let audioRendererInfo: audio.AudioRendererInfo = {
9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
10. rendererFlags: 1
11. }
12. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
13. if (error) {
14. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
15. return;
16. } else {
17. soundPool = soundPool_;
18. console.info(`Succeeded in creating SoundPool`);
19. let file: fileIo.File;
20. let soundID: number = 0;
21. let fileSize: number = 1; // 通过fileIo.stat()获取size值。
22. let uri: string = "";
23. // 获取fd的描述信息，test_01.mp3不是rawfile目录资源下面的音频。
24. fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
25. file = file_;
26. console.info("file fd: " + file.fd);
27. uri = 'fd://' + (file.fd).toString();
28. soundPool.load(file.fd, 0, fileSize, (error: BusinessError, soundId_: number) => {
29. if (error) {
30. console.error(`Failed to load soundPool: Code: ${error.code}, message: ${error.message}`);
31. } else {
32. soundID = soundId_;
33. console.info('Succeeded in loading soundId:' + soundId_);
34. }
35. });
36. }); // '/test_01.mp3' 作为样例，使用时需要传入文件对应路径。
37. }
38. });
```

**示例2：**

```
1. import { media } from '@kit.MediaKit';
2. import { audio } from '@kit.AudioKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. function create(context: Context) {
6. // 创建soundPool实例。
7. let soundPool: media.SoundPool;
8. let audioRendererInfo: audio.AudioRendererInfo = {
9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
10. rendererFlags: 1
11. }
12. let soundID: number = 0;
13. media.createSoundPool(5, audioRendererInfo, async (error: BusinessError, soundPool_: media.SoundPool) => {
14. if (error) {
15. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
16. return;
17. } else {
18. soundPool = soundPool_;
19. console.info(`Succeeded in createSoundPool`);
20. // test_01.mp3为rawfile目录资源下面的音频。
21. let fileDescriptor = await context.resourceManager.getRawFd('test_01.mp3');
22. soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length, (error: BusinessError, soundId_: number) => {
23. if (error) {
24. console.error(`Failed to load soundPool. Code: ${error.code}, message: ${error.message}`);
25. } else {
26. soundID = soundId_;
27. console.info('Succeeded in loading soundId:' + soundId_);
28. }
29. });
30. }
31. });
32. }
```

### load

PhonePC/2in1TabletTVWearable

load(fd: number, offset: number, length: number): Promise<number>

加载音频资源。使用Promise异步回调。

通过Promise异步回调获取资源ID，入参可手动传入资源信息或通过读取应用内置资源自动获取。

说明

* 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
* 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 资源句柄，通过[resourceManager.getRawFd](js-apis-resource-manager.md#getrawfd9)获取。 |
| offset | number | 是 | 资源偏移量，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。 |
| length | number | 是 | 资源长度，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回soundID，有效值大于0。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例1：**

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { media } from '@kit.MediaKit';
4. import { audio } from '@kit.AudioKit';

6. // 创建soundPool实例。
7. let soundPool: media.SoundPool;
8. let audioRendererInfo: audio.AudioRendererInfo = {
9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
10. rendererFlags: 1
11. }
12. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
13. if (error) {
14. console.error(`Failed to createSoundPool. Code: ${error.code}, message: ${error.message}`);
15. return;
16. } else {
17. soundPool = soundPool_;
18. console.info(`Succeeded in creating SoundPool`);
19. let file: fileIo.File;
20. let soundID: number = 0;
21. let fileSize: number = 1; // 通过fileIo.stat()获取size值。
22. let uri: string = "";
23. // 获取fd的描述信息，test_01.mp3不是rawfile目录资源下面的音频。
24. fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
25. file = file_;
26. console.info("file fd: " + file.fd);
27. uri = 'fd://' + (file.fd).toString();
28. soundPool.load(file.fd, 0, fileSize).then((soundId: number) => {
29. console.info('Succeeded in loading soundpool');
30. soundID = soundId;
31. }, (err: BusinessError) => {
32. console.error(`Failed to load soundpool.  Code: ${err.code}, message: ${err.message}`);
33. });
34. });
35. }
36. });
```

**示例2：**

```
1. import { media } from '@kit.MediaKit';
2. import { audio } from '@kit.AudioKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. function create(context: Context) {
6. // 创建soundPool实例。
7. let soundPool: media.SoundPool;
8. let audioRendererInfo: audio.AudioRendererInfo = {
9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
10. rendererFlags: 1
11. }
12. let soundID: number = 0;
13. media.createSoundPool(5, audioRendererInfo, async (error: BusinessError, soundPool_: media.SoundPool) => {
14. if (error) {
15. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
16. return;
17. } else {
18. soundPool = soundPool_;
19. console.info(`Succeeded in creating SoundPool`);
20. // test_01.mp3为rawfile目录资源下面的音频。
21. let fileDescriptor = await context.resourceManager.getRawFd('test_01.mp3');
22. soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length).then((soundId: number) => {
23. console.info('Succeeded in loading soundpool');
24. soundID = soundId;
25. }, (err: BusinessError) => {
26. console.error(`Failed to load soundpool. Code: ${err.code}, message: ${err.message}`);
27. });
28. }
29. });
30. }
```

### play

PhonePC/2in1TabletTVWearable

play(soundID: number, params: PlayParameters, callback: AsyncCallback<number>): void

播放音频资源，获取音频流streamID。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundID | number | 是 | 资源ID，通过load方法获取。 |
| params | [PlayParameters](js-apis-inner-multimedia-soundpool.md#playparameters) | 是 | play播放相关参数的设置。 |
| callback | AsyncCallback<number> | 是 | 获取回调的音频流ID，有效值大于0。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| 5400102 | Operation not allowed. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let soundID: number = 0;
19. let streamID: number = 0;
20. let playParameters: media.PlayParameters = {
21. loop: 3, // 循环3次。
22. rate: audio.AudioRendererRate.RENDER_RATE_NORMAL, // 正常倍速。
23. leftVolume: 0.5, // range = 0.0-1.0
24. rightVolume: 0.5, // range = 0.0-1.0
25. priority: 0, // 最低优先级。
26. }
27. soundPool.play(soundID, playParameters, (error: BusinessError, streamId: number) => {
28. if (error) {
29. console.error(`Failed to play soundpool: errCode is ${error.code}, errMessage is ${error.message}`);
30. } else {
31. streamID = streamId;
32. console.info('Succeeded in playing soundpool, streamId:' + streamId);
33. }
34. });
35. }
36. });
```

### play

PhonePC/2in1TabletTVWearable

play(soundID: number, callback: AsyncCallback<number>): void

使用默认参数播放音频资源，获取音频流streamID。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundID | number | 是 | 资源ID，通过load方法获取。 |
| callback | AsyncCallback<number> | 是 | 获取回调的音频流ID，有效值大于0。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| 5400102 | Operation not allowed. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in creating SoundPool`);
18. let soundID: number = 0;
19. let streamID: number = 0;
20. soundPool.play(soundID,  (error: BusinessError, streamId: number) => {
21. if (error) {
22. console.error(`Failed to play soundpool: errCode is ${error.code}, errMessage is ${error.message}`);
23. } else {
24. streamID = streamId;
25. console.info('Succeeded in playing soundpool, streamId:' + streamId);
26. }
27. });
28. }
29. });
```

### play

PhonePC/2in1TabletTVWearable

play(soundID: number, params?: PlayParameters): Promise<number>

播放音频资源，获取音频流streamID。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundID | number | 是 | 资源ID，通过load方法获取。 |
| params | [PlayParameters](js-apis-inner-multimedia-soundpool.md#playparameters) | 否 | play播放相关参数的设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回音频流ID，有效值大于0。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in creating SoundPool`);
18. let soundID: number = 0;
19. let streamID: number = 0;
20. let playParameters: media.PlayParameters = {
21. loop: 3, // 循环4次。
22. rate: audio.AudioRendererRate.RENDER_RATE_NORMAL, // 正常倍速。
23. leftVolume: 0.5, // range = 0.0-1.0。
24. rightVolume: 0.5, // range = 0.0-1.0。
25. priority: 0, // 最低优先级。
26. }

28. soundPool.play(soundID, playParameters).then((streamId: number) => {
29. console.info('Succeeded in playing soundpool');
30. streamID = streamId;
31. },(err: BusinessError) => {
32. console.error('Failed to play soundpool. Code: ${err.code}, message: ${err.message}');
33. });
34. }
35. });
```

### stop

PhonePC/2in1TabletTVWearable

stop(streamID: number, callback: AsyncCallback<void>): void

停止播放音频资源。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频池stop回调成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| 5400102 | Operation not allowed. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let streamID: number = 0;
19. // 先调用play方法给拿到对应的streamID。
20. soundPool.stop(streamID, (error: BusinessError) => {
21. if (error) {
22. console.error('Failed to stop soundpool Code: ${err.code}, message: ${err.message}');
23. } else {
24. console.info('Succeeded in stopping soundpool');
25. }
26. })
27. }
28. });
```

### stop

PhonePC/2in1TabletTVWearable

stop(streamID: number): Promise<void>

停止streamID对应的音频播放。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let streamID: number = 0;
19. // 先调用play方法给拿到对应的streamID。
20. soundPool.stop(streamID).then(() => {
21. console.info('Succeeded in stopping soundpool');
22. }, (err: BusinessError) => {
23. console.error(`Failed to stop soundpool Code: ${err.code}, message: ${err.message}`);
24. });
25. }
26. });
```

### setLoop

PhonePC/2in1TabletTVWearable

setLoop(streamID: number, loop: number, callback: AsyncCallback<void>): void

设置循环模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| loop | number | 是 | 设置循环次数。  当loop≥0时，实际播放次数为loop+1。  当loop＜0时，表示一直循环。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当setLoop的回调成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| 5400102 | Operation not allowed. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let streamID: number = 0;
19. // 先通过调用play方法获取到对应的streamID。
20. // 设置循环2次。
21. soundPool.setLoop(streamID, 2, (error: BusinessError) => {
22. if (error) {
23. console.error(`Failed to setLoop soundPool. Code: ${error.code}, message: ${error.message}`);
24. } else {
25. console.info('Succeeded in setLooping soundpool, streamID:' + streamID);
26. }
27. });
28. }
29. });
```

### setLoop

PhonePC/2in1TabletTVWearable

setLoop(streamID: number, loop: number): Promise<void>

设置循环模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| loop | number | 是 | 设置循环次数。  当loop≥0时，实际播放次数为loop+1。  当loop＜0时，表示一直循环。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in creating SoundPool`);
18. let streamID: number = 0;
19. // 先通过调用play方法获取到对应的streamID。
20. // 设置循环1次。
21. soundPool.setLoop(streamID, 1).then(() => {
22. console.info('Succeeded in setting Priority soundpool, streamID:' + streamID);
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to setLoop soundPool. Code: ${err.code}, message: ${err.message}`);
25. });
26. }
27. });
```

### setPriority

PhonePC/2in1TabletTVWearable

setPriority(streamID: number, priority: number, callback: AsyncCallback<void>): void

设置音频流播放的优先级。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| priority | number | 是 | 优先级，0表示最低优先级。设置范围为大于等于0的整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频池setPriority方法回调成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| 5400102 | Operation not allowed. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool. Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in creating SoundPool`);
18. let streamID: number = 0;
19. // 先调用play方法获取到对应资源的streamID。
20. // 给对应的streamID资源设置优先级为1。
21. soundPool.setPriority(streamID, 1, (error: BusinessError) => {
22. if (error) {
23. console.error(`Failed to setPriority soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
24. } else {
25. console.info('Succeeded in setPriority soundpool, streamID:' + streamID);
26. }
27. });
28. }
29. });
```

### setPriority

PhonePC/2in1TabletTVWearable

setPriority(streamID: number, priority: number): Promise<void>

设置音频流优先级。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| priority | number | 是 | 优先级，0表示最低优先级。设置范围为大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let streamID: number = 0;
19. // 先调用play方法获取到对应资源的streamID。
20. // 给对应的streamID资源设置优先级为1。

22. soundPool.setPriority(streamID, 1).then(() => {
23. console.info('Succeeded in setting Priority soundpool');
24. }, (err: BusinessError) => {
25. console.error('Failed to set Priority soundPool. Code: ${err.code}, message: ${err.message}');
26. });
27. }
28. });
```

### setRate

PhonePC/2in1TabletTVWearable

setRate(streamID: number, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void

设置音频流播放速率。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| rate | [audio.AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8) | 是 | 音频rate相关参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频池setRate方法回调成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| 5400102 | Operation not allowed. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool.  Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in creating SoundPool`);
18. let streamID: number = 0;
19. let selectedAudioRendererRate: audio.AudioRendererRate = audio.AudioRendererRate.RENDER_RATE_NORMAL; // 默认正常速率
20. // 先调用play方法获取到对应资源的streamID。
21. soundPool.setRate(streamID, selectedAudioRendererRate, (error: BusinessError) => {
22. if (error) {
23. console.error(`Failed to set Rate soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
24. } else {
25. console.info('Succeeded in setting Rate, streamID:' + streamID);
26. }
27. })
28. }
29. });
```

### setRate

PhonePC/2in1TabletTVWearable

setRate(streamID: number, rate: audio.AudioRendererRate): Promise<void>

设置音频流的播放速率。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| rate | [audio.AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8) | 是 | 音频rate相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool.  Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in creating SoundPool`);
18. let streamID: number = 0;
19. let selectedAudioRendererRate: audio.AudioRendererRate = audio.AudioRendererRate.RENDER_RATE_NORMAL; // 默认正常速率
20. // 先调用play方法获取到对应资源的streamID。
21. soundPool.setRate(streamID, selectedAudioRendererRate).then(() => {
22. console.info('Succeeded in setting Rate soundpool');
23. }, (err: BusinessError) => {
24. console.error(`Failed to set Rate. Code: ${err.code}, message: ${err.message}`);
25. });
26. }
27. });
```

### setVolume

PhonePC/2in1TabletTVWearable

setVolume(streamID: number, leftVolume: number, rightVolume: number, callback: AsyncCallback<void>): void

设置音频流播放音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| leftVolume | number | 是 | 左声道音量，设置范围为[0.0, 1.0]。 |
| rightVolume | number | 是 | 右声道音量，设置范围为[0.0, 1.0]，当前右声道设置无效，以左声道为准。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频池setVolume方法回调成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| 5400102 | Operation not allowed. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to create SoundPool.  Code: ${error.code}, message: ${error.message}`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let streamID: number = 0;
19. // 先调用play方法获取到对应资源的streamID。
20. // 设置音量为0.5。
21. soundPool.setVolume(streamID, 0.5, 0.5, (error: BusinessError) => {
22. if (error) {
23. console.error(`Failed to setVolume soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
24. } else {
25. console.info('Succeeded in setting Volume soundpool, streamID:' + streamID);
26. }
27. })
28. }
29. });
```

### setVolume

PhonePC/2in1TabletTVWearable

setVolume(streamID: number, leftVolume: number, rightVolume: number): Promise<void>

设置音频流的播放音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamID | number | 是 | 音频流ID，通过play方法获取。 |
| leftVolume | number | 是 | 左声道音量，设置范围为[0.0, 1.0]。 |
| rightVolume | number | 是 | 右声道音量，设置范围为[0.0, 1.0]，当前右声道设置无效，以左声道为准。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let streamID: number = 0;
19. // 先调用play方法获取到对应资源的streamID。

21. soundPool.setVolume(streamID, 0.5, 0.5).then(() => {
22. console.info('Succeeded in setVolume soundpool');
23. }, (err: BusinessError) => {
24. console.error('Failed to setVolume soundPool and catch error is ' + err.message);
25. });
26. }
27. });
```

### setInterruptMode23+

PhonePC/2in1TabletTVWearable

setInterruptMode(interruptMode: media.SoundInterruptMode): void

设置同一ID音频在播放时的打断模式。创建soundPool之后，该接口仅在首次调用soundPool的Play函数之前设置有效，期间可多次设置，否则将默认使用[SAME\_SOUND\_INTERRUPT](arkts-apis-media-e.md#soundinterruptmode23)，即对同一ID的音频，如果前者尚未播放完成，后者在播放前会先打断前者的播放。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interruptMode | [media.SoundInterruptMode](arkts-apis-media-e.md#soundinterruptmode23) | 是 | 同一ID音频在播放时的打断模式，通过media.SoundInterruptMode枚举获取。 |

**示例：**

```
1. import { media } from '@kit.MediaKit';

3. // 创建soundPool实例。
4. let soundPool: media.SoundPool;
5. let audioRendererInfo: audio.AudioRendererInfo = {
6. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
7. rendererFlags: 1
8. }
9. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
10. if (error) {
11. console.error(`Failed to createSoundPool`);
12. return;
13. } else {
14. soundPool = soundPool_;
15. console.info(`Succeeded in createSoundPool`);
16. // 选择模式1：同ID音频并行播放模式。
17. soundPool.setInterruptMode(media.SoundInterruptMode.NO_INTERRUPT);
18. // 选择模式2：同ID音频截断模式。
19. soundPool.setInterruptMode(media.SoundInterruptMode.SAME_SOUND_INTERRUPT);
20. }
21. });
```

### unload

PhonePC/2in1TabletTVWearable

unload(soundID: number, callback: AsyncCallback<void>): void

卸载音频资源。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundID | number | 是 | 资源ID，通过load方法获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频池unload方法回调成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let soundID: number = 0;
19. // 先调用load方法获取到对应资源的soundID。
20. soundPool.unload(soundID, (error: BusinessError) => {
21. if (error) {
22. console.error(`Failed to unload soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
23. } else {
24. console.info('Succeeded in unload soundPool');
25. }
26. })
27. }
28. });
```

### unload

PhonePC/2in1TabletTVWearable

unload(soundID: number): Promise<void>

卸载音频资源。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundID | number | 是 | 资源ID，通过load方法获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. let soundID: number = 0;
19. // 先调用load方法获取到对应资源的soundID。

21. soundPool.unload(soundID).then(() => {
22. console.info('Succeeded in unload soundPool');
23. }, (err: BusinessError) => {
24. console.error('Failed to unload soundPool and catch error is ' + err.message);
25. });
26. }
27. });
```

### release

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放音频池实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频池release方法回调成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.release((error: BusinessError) => {
19. if (error) {
20. console.error(`Failed to release soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
21. } else {
22. console.info('Succeeded in releasing soundPool');
23. }
24. })
25. }
26. });
```

### release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放音频池实例。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.release().then(() => {
19. console.info('Succeeded in releasing soundPool');
20. }, (err: BusinessError) => {
21. console.error('Failed to release soundPool and catch error is ' + err.message);
22. });
23. }
24. });
```

### on('loadComplete')

PhonePC/2in1TabletTVWearable

on(type: 'loadComplete', callback: Callback<number>): void

音频池资源加载完成监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 支持的事件：'loadComplete'，对应的ID加载完成会触发此回调。 |
| callback | Callback<number> | 是 | 回调函数，返回对应资源加载完成的资源ID。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.on('loadComplete', (soundId: number) => {
19. console.info('Succeeded in loadComplete, soundId：' + soundId);
20. })
21. }
22. });
```

### off('loadComplete')

PhonePC/2in1TabletTVWearable

off(type: 'loadComplete'): void

取消监听资源的加载完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消注册的事件：'loadComplete'。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.off('loadComplete');
19. }
20. });
```

### on('playFinishedWithStreamId')18+

PhonePC/2in1TabletTVWearable

on(type: 'playFinishedWithStreamId', callback: Callback<number>): void

音频池资源播放完成监听，同时返回播放结束的音频的streamId。使用callback异步回调。

当仅单独注册[on('playFinished')](js-apis-inner-multimedia-soundpool.md#onplayfinished)事件回调或者[on('playFinishedWithStreamId')](js-apis-inner-multimedia-soundpool.md#onplayfinishedwithstreamid18)事件回调时，当音频播放完成的时候，都会触发注册的回调。

当同时注册[on('playFinished')](js-apis-inner-multimedia-soundpool.md#onplayfinished)事件回调和[on('playFinishedWithStreamId')](js-apis-inner-multimedia-soundpool.md#onplayfinishedwithstreamid18)事件回调时，当音频播放完成的时候，仅会触发'playFinishedWithStreamId'事件回调，不会触发'playFinished'事件回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 支持的事件：'playFinishedWithStreamId'，音频流播放完成会触发此回调，并返回播放完成的音频的streamId。 |
| callback | Callback<number> | 是 | 回调函数，返回播放完成的音频的streamId。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool_: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. } else {
15. soundPool_ = soundPool;
16. console.info(`Succeeded in createSoundPool`);
17. soundPool_.on('playFinishedWithStreamId', (streamId) => {
18. console.info('The stream with streamId: ' + streamId + ' has finished playing.');
19. });
20. }
21. });
```

### off('playFinishedWithStreamId')18+

PhonePC/2in1TabletTVWearable

off(type: 'playFinishedWithStreamId'): void

取消监听音频池资源播放完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消注册的事件：'playFinishedWithStreamId'。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool_: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. } else {
15. soundPool_ = soundPool;
16. console.info(`Succeeded in createSoundPool`);
17. soundPool_.off('playFinishedWithStreamId');
18. }
19. });
```

### on('playFinished')

PhonePC/2in1TabletTVWearable

on(type: 'playFinished', callback: Callback<void>): void

音频池资源播放完成监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 支持的事件：'playFinished'，音频流播放完成会触发此回调。 |
| callback | Callback<void> | 是 | 异步'playFinished'的回调方法。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.on('playFinished', () => {
19. console.info('Succeeded in playFinished');
20. });
21. }
22. });
```

### off('playFinished')

PhonePC/2in1TabletTVWearable

off(type: 'playFinished'): void

取消监听音频池资源播放完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消注册的事件：'playFinished'。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.off('playFinished');
19. }
20. });
```

### on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听[SoundPool](js-apis-inner-multimedia-soundpool.md#soundpool)的错误事件，该事件仅用于错误提示。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'error'，用户操作和系统都会触发此事件。 |
| callback | ErrorCallback | 是 | 错误事件回调方法：使用播放器的过程中发生错误，会提供错误码ID和错误信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.on('error', (error: BusinessError) => {
19. console.error('error happened,and error message is :' + error.message);
20. console.error('error happened,and error code is :' + error.code);
21. })
22. }
23. });
```

### off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error'): void

取消监听音频池的错误事件。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，取消注册的事件：'error'。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.off('error');
19. }
20. });
```

### on('errorOccurred')20+

PhonePC/2in1TabletTVWearable

on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void

监听[SoundPool](js-apis-inner-multimedia-soundpool.md#soundpool)的错误事件，并返回包含错误码、错误发生阶段、资源ID和音频流ID的[ErrorInfo](js-apis-inner-multimedia-soundpool.md#errorinfo20)。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'errorOccurred'，当用户或系统操作导致错误，触发该事件。 |
| callback | Callback<[ErrorInfo](js-apis-inner-multimedia-soundpool.md#errorinfo20)> | 是 | 回调函数，返回错误事件回调方法。在使用播放器的过程中发生错误时，提供错误信息[ErrorInfo](js-apis-inner-multimedia-soundpool.md#errorinfo20)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.on('errorOccurred', (errorInfo) => {
19. console.error('error happened,and error message is :' + errorInfo.errorCode.message);
20. console.error('error happened,and error code is :' + errorInfo.errorCode.code);
21. console.error('error happened,and errorType is :' + errorInfo.errorType);
22. console.error('error happened,and soundId is :' + errorInfo.soundId);
23. console.error('error happened,and streamId is :' + errorInfo.streamId);
24. })
25. }
26. });
```

### off('errorOccurred')20+

PhonePC/2in1TabletTVWearable

off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void

取消监听音频池的错误事件。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，取消注册的事件为'errorOccurred'。 |
| callback | Callback<[ErrorInfo](js-apis-inner-multimedia-soundpool.md#errorinfo20)> | 否 | 错误事件回调方法。在使用播放器的过程中发生错误时，提供错误信息[ErrorInfo](js-apis-inner-multimedia-soundpool.md#errorinfo20)，不设置callback时不提供相关信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';
3. import { audio } from '@kit.AudioKit';

5. // 创建soundPool实例。
6. let soundPool: media.SoundPool;
7. let audioRendererInfo: audio.AudioRendererInfo = {
8. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
9. rendererFlags: 1
10. }
11. media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
12. if (error) {
13. console.error(`Failed to createSoundPool`);
14. return;
15. } else {
16. soundPool = soundPool_;
17. console.info(`Succeeded in createSoundPool`);
18. soundPool.off('errorOccurred');
19. }
20. });
```
