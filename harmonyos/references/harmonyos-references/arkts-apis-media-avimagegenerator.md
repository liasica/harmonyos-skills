---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avimagegenerator
title: Interface (AVImageGenerator)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Interface (AVImageGenerator)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:73b79b52c0b4547a9649af1d47942cf329e3526dec9e58889b00b899434cdcd4
---

视频缩略图获取类，用于从视频资源中获取缩略图。在调用AVImageGenerator的方法前，需要先通过[createAVImageGenerator()](arkts-apis-media-f.md#mediacreateavimagegenerator12)构建一个AVImageGenerator实例。

获取视频缩略图的demo可参考：[获取视频缩略图开发指导](../harmonyos-guides/avimagegenerator.md)。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fdSrc12+ | [AVFileDescriptor](arkts-apis-media-i.md#avfiledescriptor9) | 否 | 是 | 媒体文件描述，通过该属性设置数据源。  **使用示例**：  假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }。  **说明：**  将资源句柄（fd）传递给AVImageGenerator实例之后，不允许通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频缩略图数据获取异常。 |

## fetchFrameByTime12+

PhonePC/2in1TabletTVWearable

fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams, callback: AsyncCallback<image.PixelMap>): void

获取视频缩略图。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeUs | number | 是 | 需要获取的缩略图在视频中的时间点，单位为微秒（μs）。 |
| options | [AVImageQueryOptions](arkts-apis-media-e.md#avimagequeryoptions12) | 是 | 需要获取的缩略图时间点与视频帧的对应关系。 |
| param | [PixelMapParams](arkts-apis-media-i.md#pixelmapparams12) | 是 | 需要获取的缩略图的格式参数。 |
| callback | AsyncCallback<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。获取缩略图成功时，err为undefined，data为PixelMap实例，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Returned by callback. |
| 5400106 | Unsupported format. Returned by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';
3. import { media } from '@kit.MediaKit';

5. let avImageGenerator: media.AVImageGenerator | undefined = undefined;
6. let pixel_map: image.PixelMap | undefined = undefined;

8. // 初始化入参。
9. let timeUs: number = 0;

11. let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;

13. let param: media.PixelMapParams = {
14. width: 300,
15. height: 300,
16. };

18. // 获取缩略图。
19. media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
20. if (generator) {
21. avImageGenerator = generator;
22. console.info(`Succeeded in creating AVImageGenerator`);
23. avImageGenerator.fetchFrameByTime(timeUs, queryOption, param, (error: BusinessError, pixelMap) => {
24. if (error) {
25. console.error(`Failed to fetch FrameByTime, err = ${JSON.stringify(error)}`);
26. return;
27. }
28. pixel_map = pixelMap;
29. });
30. } else {
31. console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
32. }
33. });
```

## fetchFrameByTime12+

PhonePC/2in1TabletTVWearable

fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>

获取视频缩略图。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeUs | number | 是 | 需要获取的缩略图在视频中的时间点，单位为微秒（μs）。 |
| options | [AVImageQueryOptions](arkts-apis-media-e.md#avimagequeryoptions12) | 是 | 需要获取的缩略图时间点与视频帧的对应关系。 |
| param | [PixelMapParams](arkts-apis-media-i.md#pixelmapparams12) | 是 | 需要获取的缩略图的格式参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回视频缩略图对象。 |

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

5. let avImageGenerator: media.AVImageGenerator | undefined = undefined;
6. let pixel_map: image.PixelMap | undefined = undefined;

8. // 初始化入参。
9. let timeUs: number = 0;

11. let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;

13. let param: media.PixelMapParams = {
14. width: 300,
15. height: 300,
16. };

18. // 获取缩略图。
19. media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
20. if (generator) {
21. avImageGenerator = generator;
22. console.info(`Succeeded in creating AVImageGenerator`);
23. avImageGenerator.fetchFrameByTime(timeUs, queryOption, param).then((pixelMap: image.PixelMap) => {
24. pixel_map = pixelMap;
25. }).catch((error: BusinessError) => {
26. console.error(`Failed to fetch FrameByTime, error message:${error.message}`);
27. });
28. } else {
29. console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
30. }
31. });
```

## fetchScaledFrameByTime20+

PhonePC/2in1TabletTVWearable

fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):Promise<image.PixelMap>

支持按比例缩放提取视频缩略图。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeUs | number | 是 | 在视频中需要获取的缩略图的时间点，单位为微秒（μs）。 |
| queryMode | [AVImageQueryOptions](arkts-apis-media-e.md#avimagequeryoptions12) | 是 | 需要获取的缩略图时间点与视频帧的对应关系。 |
| outputSize | [OutputSize](arkts-apis-media-i.md#outputsize20) | 否 | 定义帧的输出大小。默认按原图大小显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回视频缩略图对象。 |

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

5. let avImageGenerator: media.AVImageGenerator | undefined = undefined;
6. let pixel_map: image.PixelMap | undefined = undefined;
7. // 初始化入参。
8. let timeUs: number = 0;
9. let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
10. let outputSize: media.OutputSize = {
11. width: 300,
12. height: 300,
13. };
14. // 获取缩略图。
15. media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
16. if (generator) {
17. avImageGenerator = generator;
18. console.info(`Succeeded in creating AVImageGenerator`);
19. avImageGenerator.fetchScaledFrameByTime(timeUs, queryOption, outputSize).then((pixelMap: image.PixelMap) => {
20. pixel_map = pixelMap;
21. }).catch((error: BusinessError) => {
22. console.error(`Failed to fetch ScaledFrameByTime, error message:${error.message}`);
23. });
24. } else {
25. console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
26. }
27. });
```

## release12+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放资源。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

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

4. let avImageGenerator: media.AVImageGenerator | undefined = undefined;

6. // 释放资源。
7. media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
8. if (generator) {
9. avImageGenerator = generator;
10. console.info(`Succeeded in creating AVImageGenerator`);
11. avImageGenerator.release((error: BusinessError) => {
12. if (error) {
13. console.error(`Failed to release, err = ${JSON.stringify(error)}`);
14. return;
15. }
16. console.info(`Succeeded in releasing`);
17. });
18. } else {
19. console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
20. }
21. });
```

## release12+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放资源。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

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

4. let avImageGenerator: media.AVImageGenerator | undefined = undefined;

6. // 释放资源。
7. media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
8. if (generator) {
9. avImageGenerator = generator;
10. console.info(`Succeeded in creating AVImageGenerator`);
11. avImageGenerator.release().then(() => {
12. console.info(`Succeeded in releasing.`);
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to release, error message:${error.message}`);
15. });
16. } else {
17. console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
18. }
19. });
```
