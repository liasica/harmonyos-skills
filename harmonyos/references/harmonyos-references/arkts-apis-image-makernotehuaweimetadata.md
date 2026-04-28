---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-makernotehuaweimetadata
title: Class (MakerNoteHuaweiMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (MakerNoteHuaweiMetadata)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4eae0f53e9e5e719dff461863e4f3245501f0c31ed7f339ade0be2b17d48254c
---

MakerNoteHuaweiMetadata implements Metadata

来自Huawei相机的照片元数据。

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isXmageSupported | boolean | 否 | 是 | 是否支持XMAGE。true表示支持，false表示不支持。 |
| xmageWatermarkMode | number | 否 | 是 | XMAGE水印模式。具体取值请参考[Constants](arkts-apis-image-c.md)。 |
| xmageLeft | number | 否 | 是 | 当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的左边界（相对于图片左上角原点）的水平坐标。单位为像素（px）。 |
| xmageTop | number | 否 | 是 | 当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的上边界（相对于图片左上角原点）的垂直坐标。单位为像素（px）。 |
| xmageRight | number | 否 | 是 | 当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的右边界（相对于图片左上角原点）的水平坐标。单位为像素（px）。 |
| xmageBottom | number | 否 | 是 | 当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的下边界（相对于图片左上角原点）的垂直坐标。单位为像素（px）。 |
| xmageColorMode | [XmageColorMode](arkts-apis-image-e.md#xmagecolormode23) | 否 | 是 | XMAGE颜色模式。 |
| isCloudEnhanced | boolean | 否 | 是 | 图像是否存在云端增强。true表示存在，false表示不存在。 |
| cloudLabel | string | 否 | 是 | 云增强标签。 |
| isWindSnapshot | boolean | 否 | 是 | 是否采用风快照模式拍摄。true表示采用，false表示不采用。  该模式是针对拍摄快速移动物体或容易产生模糊场景（如大风中、抓拍运动物体）的专门摄影。 |
| sceneVersion | number | 否 | 是 | 场景识别算法版本号。 |
| sceneFoodConfidence | number | 否 | 是 | 拍摄场景：美食置信度。 |
| sceneStageConfidence | number | 否 | 是 | 拍摄场景：舞台演出置信度。 |
| sceneBlueSkyConfidence | number | 否 | 是 | 拍摄场景：蓝天置信度。 |
| sceneGreenPlantConfidence | number | 否 | 是 | 拍摄场景：绿色植物置信度。 |
| sceneBeachConfidence | number | 否 | 是 | 拍摄场景：海滩置信度。 |
| sceneSnowConfidence | number | 否 | 是 | 拍摄场景：雪景置信度。 |
| sceneSunsetConfidence | number | 否 | 是 | 拍摄场景：日落置信度。 |
| sceneFlowersConfidence | number | 否 | 是 | 拍摄场景：花卉置信度。 |
| sceneNightConfidence | number | 否 | 是 | 拍摄场景：夜景置信度。 |
| sceneTextConfidence | number | 否 | 是 | 拍摄场景：文本置信度。 |
| faceCount | number | 否 | 是 | 人脸数。 |
| faceConfidences | number[] | 否 | 是 | 对指定数量的面孔置信度。 |
| faceSmileScores | number[] | 否 | 是 | 特定数量面孔的微笑得分。 |
| captureMode | number | 否 | 是 | 捕获模式。 |
| burstNumber | number | 否 | 是 | 连拍数量。 |
| isFrontCamera | boolean | 否 | 是 | 是否使用前置摄像头。true表示使用，false表示不使用。 |
| rollAngle | number | 否 | 是 | 左右滚动角度。 |
| pitchAngle | number | 否 | 是 | 俯仰角度。 |
| physicalAperture | number | 否 | 是 | 物理光圈值。单位是fNumber。 |
| focusMode | [FocusMode](arkts-apis-image-e.md#focusmode23) | 否 | 是 | 镜头对焦控制策略，决定相机如何调整焦距。 |

## createInstance

PhonePC/2in1TabletTVWearable

static createInstance(): MakerNoteHuaweiMetadata

返回[MakerNoteHuaweiMetadata](arkts-apis-image-makernotehuaweimetadata.md)的空实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MakerNoteHuaweiMetadata](arkts-apis-image-makernotehuaweimetadata.md) | 返回MakerNoteHuaweiMetadata的空实例。 |

**示例：**

```
1. async function makerNoteHuaweiCreateInstance(context: Context) {
2. let makerNoteHuaweiMetadata = image.MakerNoteHuaweiMetadata.createInstance();
3. if (makerNoteHuaweiMetadata != undefined) {
4. console.info("createInstance success");
5. }
6. }
```

## getProperties

PhonePC/2in1TabletTVWearable

getProperties(key: Array<string>): Promise<Record<string, string | null>>

获取图像中属性的值。使用Promise异步回调。

要查询的属性的具体信息请参考[PropertyKey](arkts-apis-image-e.md#propertykey7)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | Array<string> | 是 | 要获取其值的属性的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, string | null>> | Promise对象，返回元数据要获取的属性的值，如获取失败则返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600202 | Unsupported metadata. Possible causes: unsupported metadata type. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. function getFileFd(context: Context): number | undefined {
5. const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function makerNoteHuaweiGetProperties(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
15. if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
16. await metaData.makerNoteHuaweiMetadata.getProperties(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]).then((data) => {
17. console.info('Get properties ',JSON.stringify(data));
18. }).catch((error: BusinessError) => {
19. console.error(`Get properties failed error.code is ${error.code}, error.message is ${error.message}`);
20. });
21. } else {
22. console.error('Metadata is null.');
23. }
24. }
```

## setProperties

PhonePC/2in1TabletTVWearable

setProperties(records: Record<string, string | null>): Promise<void>

批量设置图片元数据中的指定属性的值。使用Promise异步回调。

要查询的属性的具体信息请参考[PropertyKey](arkts-apis-image-e.md#propertykey7)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<string, string | null> | 是 | 包含要修改的MakerNoteHuaweiMetadata对象属性键值对的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600202 | Unsupported metadata. Possible causes: unsupported metadata type. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. function getFileFd(context: Context): number | undefined {
5. const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function makerNoteHuaweiSetProperties(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
15. if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
16. let setkey: Record<string, string | null> = {
17. "HwMnoteIsXmageSupported": "1",
18. "HwMnoteXmageMode": "9"
19. };
20. await metaData.makerNoteHuaweiMetadata.setProperties(setkey).then(async () => {
21. console.info('Set properties success.');
22. }).catch((error: BusinessError) => {
23. console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
24. })
25. } else {
26. console.error('metadata is null. ');
27. }
28. }
```

## getAllProperties

PhonePC/2in1TabletTVWearable

getAllProperties(): Promise<Record<string, string | null>>

获取图片中所有元数据的属性和值。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, string | null>> | Promise对象，返回元数据中定义的所有键值对。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. function getFileFd(context: Context): number | undefined {
5. const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function makerNoteHuaweiGetAllProperties(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
15. if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
16. await metaData.makerNoteHuaweiMetadata.getAllProperties().then((data) => {
17. const count = Object.keys(data).length;
18. console.info(`Get metadata all properties: ${data}`);
19. }).catch((error: BusinessError) => {
20. console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
21. });
22. } else {
23. console.error('Metadata is null.');
24. }
25. }
```

## clone

PhonePC/2in1TabletTVWearable

clone(): Promise<MakerNoteHuaweiMetadata>

对[MakerNoteHuaweiMetadata](arkts-apis-image-makernotehuaweimetadata.md)元数据进行克隆。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MakerNoteHuaweiMetadata](arkts-apis-image-makernotehuaweimetadata.md)> | Promise对象，当成功获取元数据时返回MakerNoteHuaweiMetadata元数据实例。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. function getFileFd(context: Context): number | undefined {
5. const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function makerNoteHuaweiClone(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
15. if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
16. let new_metadata = await metaData.makerNoteHuaweiMetadata.clone();
17. new_metadata.getProperties(["HwMnoteIsXmageSupported"]).then((data1) => {
18. console.info(`Clone new_metadata and get Properties: ${data1}`);
19. }).catch((err: BusinessError) => {
20. console.error(`Clone new_metadata failed, error : ${err}`);
21. });
22. } else {
23. console.error('Metadata is null.');
24. }
25. }
```

## getBlob

PhonePC/2in1TabletTVWearable

getBlob(): Promise<ArrayBuffer>

以二进制数据的形式获取元数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回元数据的二进制数据。 |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. function getFileFd(context: Context): number | undefined {
4. const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
5. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
6. const fd: number = file?.fd;
7. return fd;
8. }

10. async function makerNoteHuaweiGetBlob(context: Context) {
11. let fd = getFileFd(context);
12. let imageSource = image.createImageSource(fd);
13. let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
14. if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
15. let blob = await metaData.makerNoteHuaweiMetadata.getBlob();
16. if (blob != undefined) {
17. console.info("get blob success");
18. }
19. }
20. }
```

## setBlob

PhonePC/2in1TabletTVWearable

setBlob(blob: ArrayBuffer): Promise<void>

使用二进制数据替换当前元数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blob | ArrayBuffer | 是 | 要替换的二进制数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid parameter. Possible causes: The blob is empty or has a length of 0. |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. function getFileFd(context: Context): number | undefined {
4. const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
5. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
6. const fd: number = file?.fd;
7. return fd;
8. }

10. async function makerNoteHuaweiSetBlob(context: Context) {
11. let fd = getFileFd(context);
12. let imageSource = image.createImageSource(fd);
13. let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
14. if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
15. let blob = await metaData.makerNoteHuaweiMetadata.getBlob();
16. if (blob != undefined) {
17. console.info("get blob success");
18. metaData.makerNoteHuaweiMetadata.setBlob(blob);
19. }
20. let new_blob = metaData.makerNoteHuaweiMetadata.getBlob();
21. if (new_blob != undefined) {
22. console.info("new_blob is not undefined");
23. }
24. }
25. }
```
