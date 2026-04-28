---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avmetadataextractor
title: Interface (AVMetadataExtractor)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Interface (AVMetadataExtractor)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:765e251452b5c4792931ef8646ca86ed7eb9aabbb90eab2804379e6f5acb0678
---

元数据获取类，用于从媒体资源中获取元数据、缩略图。在调用AVMetadataExtractor的方法前，需要先通过[media.createAVMetadataExtractor](arkts-apis-media-f.md#mediacreateavmetadataextractor11)构建一个AVMetadataExtractor实例。

获取音频或视频元数据、视频缩略图的demo可参考：[使用AVMetadataExtractor提取音视频元数据信息(ArkTS)](../harmonyos-guides/avmetadataextractor.md)。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fdSrc11+ | [AVFileDescriptor](arkts-apis-media-i.md#avfiledescriptor9) | 否 | 是 | 媒体文件描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。  **使用示例**：  假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }。  **说明：**  将资源句柄（fd）传递给AVMetadataExtractor实例之后，不允许通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致音视频元数据获取异常。 |
| dataSrc11+ | [AVDataSrcDescriptor](arkts-apis-media-i.md#avdatasrcdescriptor10) | 否 | 是 | 流式媒体资源描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。  当应用从远端获取音视频媒体文件，在应用未下载完整音视频资源时，可以设置dataSrc提前获取该资源的元数据。 |

## setUrlSource20+

PhonePC/2in1TabletTVWearable

setUrlSource(url: string, headers?: Record<string, string>): void

网络点播资源地址描述，通过该接口设置数据源。只支持获取网络[fetchMetadata](arkts-apis-media-avmetadataextractor.md#fetchmetadata11)（元数据）和[fetchFrameByTime](arkts-apis-media-avmetadataextractor.md#fetchframebytime20)（缩略图），在获取之前，必须设置媒体资源URL。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 媒体资源URL。  1. 支持的视频格式包括：mp4、mpeg-ts、mkv。  2. 支持的音频格式包括：m4a、aac、mp3、ogg、wav、flac、amr。  **支持路径示例**：  1. http网络播放：http://xx。  2. https网络播放：https://xx。  **说明：** 不支持设置HLS/Dash、直播资源。 |
| headers | Record<string, string> | 否 | 支持访问网络资源HttpHeader自定义。默认为空。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;

6. media.createAVMetadataExtractor(async (error: BusinessError, extractor: media.AVMetadataExtractor) => {
7. if (extractor) {
8. avMetadataExtractor = extractor;
9. console.info('Succeeded in creating AVMetadataExtractor');
10. let url = "http://xx";
11. let headers: Record<string, string> = {
12. "User-Agent": "User-Agent-Value"
13. };
14. avMetadataExtractor.setUrlSource(url, headers);
15. } else {
16. console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
17. }
18. });
```

## fetchFrameByTime20+

PhonePC/2in1TabletTVWearable

fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>

获取视频缩略图。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeUs | number | 是 | 需要获取的缩略图在视频中的时间点，单位为微秒（us）。 |
| options | [AVImageQueryOptions](arkts-apis-media-e.md#avimagequeryoptions12) | 是 | 需要获取的缩略图时间点与视频帧的对应关系。 |
| param | [PixelMapParams](arkts-apis-media-i.md#pixelmapparams12) | 是 | 需要获取的缩略图的格式参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回视频缩略图对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |
| 5400108 | Parameter check failed. Returned by promise. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';
3. import { media } from '@kit.MediaKit';

5. let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;
6. let pixelMap: image.PixelMap | undefined = undefined;

8. // 初始化入参。
9. let timeUs: number = 0;
10. let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_PREVIOUS_SYNC;
11. let param: media.PixelMapParams = {
12. width: 300,
13. height: 300
14. };
15. // 获取缩略图。
16. media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
17. if (extractor) {
18. avMetadataExtractor = extractor;
19. console.info('Succeeded in creating AVMetadataExtractor');
20. avMetadataExtractor.fetchFrameByTime(timeUs, queryOption, param).then((pixelMap: image.PixelMap) => {
21. pixelMap = pixelMap;
22. }).catch((error: BusinessError) => {
23. console.error(`Failed to fetch FrameByTime, error message:${error.message}`);
24. });
25. } else {
26. console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
27. }
28. });
```

## fetchFramesByTimes23+

PhonePC/2in1TabletTVWearable

fetchFramesByTimes(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, callback: OnFrameFetched): void

批量获取视频缩略图。使用Callback异步回调。

说明

* 先对给定的视频资源进行解码，随后依据提供的参数options和param，从timesUs数组中的每个时间点提取图像帧。
* 当每一次图像提取完成时，系统将调用回调函数并传递提取结果。请注意，回调函数的执行顺序会与timesUs数组中时间点的先后顺序不一致。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timesUs | number[] | 是 | 需要获取的所有缩略图在视频中的时间点集合。  时间单位为微秒（μs），数组长度取值范围为(0, 4096]。 |
| queryOption | [AVImageQueryOptions](arkts-apis-media-e.md#avimagequeryoptions12) | 是 | 需要获取的缩略图时间点与视频帧的对应关系。 |
| param | [PixelMapParams](arkts-apis-media-i.md#pixelmapparams12) | 是 | 需要获取的缩略图的格式参数。 |
| callback | [OnFrameFetched](arkts-apis-media-t.md#onframefetched23) | 是 | 需要返回的缩略图信息及可能的异常类型。  异常类型请参考具体返回的错误码信息。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by callback. |
| 5400104 | Fetch timeout. Returned by callback. |
| 5400106 | Unsupported format. Returned by callback. |
| 5400105 | Service died. |
| 5400108 | Parameter check failed. e.g. The size of timesUs is larger than 4096. |
| 5411012 | Http cleartext not permitted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';
3. import { media } from '@kit.MediaKit';

5. async function fetchFramesByTimesDemo() {
6. // 初始化入参。
7. let timesUs: number[] = [0];
8. let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_PREVIOUS_SYNC;
9. let param: media.PixelMapParams = {
10. width: 300,
11. height: 300
12. };
13. // 获取缩略图。
14. let avMetadataExtractor = await media.createAVMetadataExtractor();
15. if (avMetadataExtractor !== null) {
16. console.info('Succeeded in creating AVMetadataExtractor');
17. avMetadataExtractor.fetchFramesByTimes(timesUs, queryOption, param, async (frameInfo: media.FrameInfo, err: BusinessError) => {
18. if (err) {
19. console.info(`fetchFramesByTimes callback failed, error = ${JSON.stringify(err)}`);
20. return;
21. }
22. if (frameInfo != undefined && frameInfo.image != undefined) {
23. let pixelMap = frameInfo.image;
24. }});
25. }
26. }
```

## cancelAllFetchFrames23+

PhonePC/2in1TabletTVWearable

cancelAllFetchFrames(): void

取消正在进行的批量获取缩略图任务（已完成部分不受影响）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**示例：**

```
1. import { media } from '@kit.MediaKit';

3. let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;

5. media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
6. if (extractor) {
7. avMetadataExtractor = extractor;
8. console.info('Succeeded in creating AVMetadataExtractor');
9. avMetadataExtractor.cancelAllFetchFrames();
10. } else {
11. console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
12. }
13. });
```

## fetchMetadata11+

PhonePC/2in1TabletTVWearable

fetchMetadata(callback: AsyncCallback<AVMetadata>): void

获取媒体元数据。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVMetadata](arkts-apis-media-i.md#avmetadata11)> | 是 | 回调函数。异步返回音视频元数据对象（AVMetadata）。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by callback. |
| 5400106 | Unsupported format. Returned by callback. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建AVMetadataExtractor对象。
6. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
7. avMetadataExtractor.fetchMetadata((error: BusinessError, metadata: media.AVMetadata) => {
8. if (error) {
9. console.error(`Failed to fetch Metadata, err = ${JSON.stringify(error)}`);
10. return;
11. }
12. console.info(`Succeeded in fetching Metadata, genre: ${metadata.genre}`);
13. });
14. }
```

## fetchMetadata11+

PhonePC/2in1TabletTVWearable

fetchMetadata(): Promise<AVMetadata>

获取媒体元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVMetadata](arkts-apis-media-i.md#avmetadata11)> | Promise对象。异步返回音视频元数据对象（AVMetadata）。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建AVMetadataExtractor对象。
6. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
7. avMetadataExtractor.fetchMetadata().then((metadata: media.AVMetadata) => {
8. console.info(`Succeeded in fetching Metadata, genre: ${metadata.genre}`);
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to fetch Metadata, error message:${error.message}`);
11. });
12. }
```

## fetchAlbumCover11+

PhonePC/2in1TabletTVWearable

fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void

获取音频专辑封面。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。异步返回专辑封面。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400106 | Unsupported format. Returned by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';
3. import { media } from '@kit.MediaKit';

5. async function test() {
6. // 创建AVMetadataExtractor对象。
7. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
8. let pixel_map: image.PixelMap | undefined = undefined;

10. avMetadataExtractor.fetchAlbumCover((error: BusinessError, pixelMap: image.PixelMap) => {
11. if (error) {
12. console.error(`Failed to fetch AlbumCover, error = ${JSON.stringify(error)}`);
13. return;
14. }
15. pixel_map = pixelMap;
16. });
17. }
```

## fetchAlbumCover11+

PhonePC/2in1TabletTVWearable

fetchAlbumCover(): Promise<image.PixelMap>

获取专辑封面。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。异步返回专辑封面。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';
3. import { media } from '@kit.MediaKit';

5. async function test() {
6. // 创建AVMetadataExtractor对象。
7. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
8. let pixel_map: image.PixelMap | undefined = undefined;

10. avMetadataExtractor.fetchAlbumCover().then((pixelMap: image.PixelMap) => {
11. pixel_map = pixelMap;
12. }).catch((error: BusinessError) => {
13. console.error(`Failed to fetch AlbumCover, error message:${error.message}`);
14. });
15. }
```

## release11+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放资源。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放资源成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建AVMetadataExtractor对象。
6. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
7. avMetadataExtractor.release((error: BusinessError) => {
8. if (error) {
9. console.error(`Failed to release, err = ${JSON.stringify(error)}`);
10. return;
11. }
12. console.info(`Succeeded in releasing.`);
13. });
14. }
```

## release11+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放资源。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异步方式释放资源release方法的Promise返回值。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { media } from '@kit.MediaKit';

4. async function test() {
5. // 创建AVMetadataExtractor对象。
6. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
7. avMetadataExtractor.release().then(() => {
8. console.info(`Succeeded in releasing.`);
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to release, error message:${error.message}`);
11. });
12. }
```
