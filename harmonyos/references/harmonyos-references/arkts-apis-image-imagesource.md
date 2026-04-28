---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource
title: Interface (ImageSource)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (ImageSource)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d95caf8f721d7695ae439bb155baa8ea5d215f9efbcc2c3ed9282388cf28cf9
---

ImageSource类，用于获取图片相关信息。

在调用ImageSource的方法前，需要先通过[image.createImageSource](arkts-apis-image-f.md#imagecreateimagesource)构建一个ImageSource实例。

ImageSource的所有方法均不支持并发调用。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedFormats | Array<string> | 是 | 否 | 支持的图片格式，包括：png、jpeg、bmp、gif、webp、dng、heic12+、wbmp23+、heifs23+、tiff23+。部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats20+](arkts-apis-image-f.md#imagegetimagesourcesupportedformats20)接口，动态查询当前设备上的解码能力。 |

## getImageInfo

PhonePC/2in1TabletTVWearable

getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void

获取指定序号的图片信息。使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 创建ImageSource时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：[0, (帧数-1)]。 |
| callback | AsyncCallback<[ImageInfo](arkts-apis-image-i.md#imageinfo)> | 是 | 回调函数。当获取图片信息成功，err为undefined，data为获取到的图片信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageInfo(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getImageInfo(0, (error: BusinessError, imageInfo: image.ImageInfo) => {
5. if (error) {
6. console.error(`Failed to obtain the image information.code is ${error.code}, message is ${error.message}`);
7. } else {
8. console.info('Succeeded in obtaining the image information.');
9. }
10. })
11. }
```

## getImageInfo

PhonePC/2in1TabletTVWearable

getImageInfo(callback: AsyncCallback<ImageInfo>): void

获取图片信息。使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ImageInfo](arkts-apis-image-i.md#imageinfo)> | 是 | 回调函数。当获取图片信息成功，err为undefined，data为获取到的图片信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageInfo(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getImageInfo((err: BusinessError, imageInfo: image.ImageInfo) => {
5. if (err) {
6. console.error(`Failed to obtain the image information.code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('Succeeded in obtaining the image information.');
9. }
10. })
11. }
```

## getImageInfo

PhonePC/2in1TabletTVWearable

getImageInfo(index?: number): Promise<ImageInfo>

获取图片信息。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 否 | 创建ImageSource时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：[0, (帧数-1)]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ImageInfo](arkts-apis-image-i.md#imageinfo)> | Promise对象，返回获取到的图片信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageInfo(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getImageInfo(0)
5. .then((imageInfo: image.ImageInfo) => {
6. console.info('Succeeded in obtaining the image information.');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to obtain the image information.code is ${error.code}, message is ${error.message}`);
9. })
10. }
```

## getImageInfoSync12+

PhonePC/2in1TabletTVWearable

getImageInfoSync(index?: number): ImageInfo

获取指定序号的图片信息，使用同步形式返回图片信息。

说明

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](../harmonyos-guides/time-consuming-task-overview.md)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 否 | 创建ImageSource时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：[0, (帧数-1)]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageInfo](arkts-apis-image-i.md#imageinfo) | 同步返回获取到的图片信息。 |

**示例：**

```
1. function GetImageInfoSync(context : Context) {
2. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
3. let filePath: string = context.filesDir + "/test.jpg";
4. let imageSource = image.createImageSource(filePath);
5. let imageInfo = imageSource.getImageInfoSync(0);
6. if (imageInfo == undefined) {
7. console.error('Failed to obtain the image information.');
8. } else {
9. console.info('Succeeded in obtaining the image information.');
10. console.info('imageInfo.size.height:' + imageInfo.size.height);
11. console.info('imageInfo.size.width:' + imageInfo.size.width);
12. }
13. }
```

## getImageProperty11+

PhonePC/2in1TabletTVWearable

getImageProperty(key:PropertyKey, options?: ImagePropertyOptions): Promise<string>

获取图片中给定索引处图像的指定属性键的值。用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF12+、WEBP23+和DNG23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [PropertyKey](arkts-apis-image-e.md#propertykey7) | 是 | 图片属性名。 |
| options | [ImagePropertyOptions](arkts-apis-image-i.md#imagepropertyoptions11) | 否 | 图片属性，包括图片序号与默认属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回图片属性值，如获取失败则返回属性默认值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980103 | The image data is not supported. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980123 | The image does not support EXIF decoding. |
| 62980135 | The EXIF value is invalid. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageProperty(imageSourceObj : image.ImageSource) {
4. let options: image.ImagePropertyOptions = { index: 0, defaultValue: '9999' }
5. imageSourceObj.getImageProperty(image.PropertyKey.BITS_PER_SAMPLE, options)
6. .then((data: string) => {
7. console.info('Succeeded in getting the value of the specified attribute key of the image.');
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
10. })
11. }
```

## getImageProperties12+

PhonePC/2in1TabletTVWearable

getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>

批量获取图片中的指定属性键的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF、WEBP23+和DNG23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | Array<[PropertyKey](arkts-apis-image-e.md#propertykey7)> | 是 | 图片属性名的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<[PropertyKey](arkts-apis-image-e.md#propertykey7), string | null>> | Promise对象，返回图片属性值，如获取失败则返回null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980116 | Failed to decode the image. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageProperties(imageSourceObj : image.ImageSource) {
4. let key = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH];
5. imageSourceObj.getImageProperties(key).then((data) => {
6. console.info(JSON.stringify(data));
7. }).catch((err: BusinessError) => {
8. console.error(JSON.stringify(err));
9. });
10. }
```

## getImagePropertySync20+

PhonePC/2in1TabletTVWearable

getImagePropertySync(key:PropertyKey): string

获取图片Exif指定属性键的值，使用同步形式返回结果。

说明

* 该方法仅支持JPEG、PNG、HEIF、WEBP23+和DNG23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。
* Exif信息是图片的元数据，包含拍摄时间、相机型号、光圈、焦距、ISO等。
* 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](../harmonyos-guides/time-consuming-task-overview.md)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [PropertyKey](arkts-apis-image-e.md#propertykey7) | 是 | 图片属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回图片Exif中指定属性键的值（如获取失败则返回属性默认值），各个数据值作用请参考[PropertyKey](arkts-apis-image-e.md#propertykey7)。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. For example, key is not supported. |

**示例：**

```
1. function GetImagePropertySync(context : Context) {
2. let resourceMgr = context.resourceManager;
3. if (resourceMgr == null) {
4. return;
5. }
6. let fd = resourceMgr.getRawFdSync("example.jpg");

8. const imageSourceObj = image.createImageSource(fd);
9. console.info("getImagePropertySync");
10. let bits_per_sample = imageSourceObj.getImagePropertySync(image.PropertyKey.BITS_PER_SAMPLE);
11. console.info("bits_per_sample : " + bits_per_sample);
12. }
```

## modifyImageProperty11+

PhonePC/2in1TabletTVWearable

modifyImageProperty(key: PropertyKey, value: string): Promise<void>

通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [PropertyKey](arkts-apis-image-e.md#propertykey7) | 是 | 图片属性名。 |
| value | string | 是 | 属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; |
| 62980123 | The image does not support EXIF decoding. |
| 62980133 | The EXIF data is out of range. |
| 62980135 | The EXIF value is invalid. |
| 62980146 | The EXIF data failed to be written to the file. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
4. imageSourceObj.modifyImageProperty(image.PropertyKey.IMAGE_WIDTH, "120").then(() => {
5. imageSourceObj.getImageProperty(image.PropertyKey.IMAGE_WIDTH).then((width: string) => {
6. console.info(`ImageWidth is :${width}`);
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to get the Image Width, error.code ${error.code}, error.message ${error.message}`);
9. })
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to modify the Image Width, error.code ${error.code}, error.message ${error.message}`);
12. })
13. }
```

## modifyImageProperties12+

PhonePC/2in1TabletTVWearable

modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>

批量通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

调用modifyImageProperties修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperties会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<[PropertyKey](arkts-apis-image-e.md#propertykey7), string | null> | 是 | 包含图片属性名和属性值的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980123 | The image does not support EXIF decoding. |
| 62980135 | The EXIF value is invalid. |
| 62980146 | The EXIF data failed to be written to the file. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ModifyImageProperties(imageSourceObj : image.ImageSource) {
4. let keyValues: Record<PropertyKey, string|null> = {
5. [image.PropertyKey.IMAGE_WIDTH] : "1024",
6. [image.PropertyKey.IMAGE_LENGTH] : "1024"
7. };
8. let checkKey = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH];
9. imageSourceObj.modifyImageProperties(keyValues).then(() => {
10. imageSourceObj.getImageProperties(checkKey).then((data) => {
11. console.info(`Image Width and Image Height:${data}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
14. });
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
17. });
18. }
```

## modifyImagePropertiesEnhanced22+

PhonePC/2in1TabletTVWearable

modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>

批量修改图片属性。使用Promise异步回调。

说明

* 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-apis-image-f.md#imagecreateimagesource7)实例或通过传入的uri创建[image.createImageSource](arkts-apis-image-f.md#imagecreateimagesource)实例。
* 该方法在内存中完成批量数据修改后会一次性写入文件，相比[modifyImageProperties](arkts-apis-image-imagesource.md#modifyimageproperties12)更高效。
* 支持修改JPEG、PNG、HEIF和WEBP文件类型的图片属性，图片需要包含Exif信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<string, string | null> | 是 | 包含图片属性名和属性值的键值对集合。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. For example, the property key is not supported, or the property value is invalid. |
| 7700304 | Failed to write image properties to the file. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function ModifyImagePropertiesEnhanced(imageSourceObj : image.ImageSource) {
5. let keyValues: Record<string, string|null> = {
6. "ImageWidth" : "1024",
7. "ImageLength" : "1024"
8. };
9. let checkKey = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH];
10. imageSourceObj.modifyImagePropertiesEnhanced(keyValues).then(() => {
11. imageSourceObj.getImageProperties(checkKey).then((data) => {
12. console.info(`Image Width and Image Height:${data}`);
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
15. });
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
18. });
19. }
```

## readImageMetadata23+

PhonePC/2in1TabletTVWearable

readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>

读取图像源的元数据，使用propertyKeys指定元数据字段。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF、WEBP和DNG（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

读取DNG格式图片时，该接口对部分propertyKeys有特殊处理。以下字段的字符串取值请参考[PropertyKey](arkts-apis-image-e.md#propertykey7)中的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propertyKeys | string[] | 否 | 图片属性名的数组。若未指定propertyKeys，则返回所有支持的元数据。 |
| index | number | 否 | 感兴趣的索引，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ImageMetadata](arkts-apis-image-i.md#imagemetadata23)> | Promise对象，返回ImageMetadata对象，其中含有图片属性名对应的metadata对象，通过ImageMetadata中的metadata对象可以获取图片属性值。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. |
| 7700204 | Invalid parameter. Possible causes: 1. The index is negative. 2. The index is greater than or equal to the number of frames in the image. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ReadImageMetadata(imageSourceObj : image.ImageSource) {
4. let propertyKeys = ["ImageWidth", "HwMnoteIsXmageSupported"];
5. await imageSourceObj.readImageMetadata(propertyKeys).then((metaData: image.ImageMetadata) => {
6. if (metaData != undefined && metaData.exifMetadata != undefined &&
7. metaData.makerNoteHuaweiMetadata != undefined) {
8. console.info("ImageWidth: " + metaData.exifMetadata.imageWidth +
9. " HwMnoteIsXmageSupported: " + metaData.makerNoteHuaweiMetadata.isXmageSupported);
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`ReadImageMetadata failed error.code is ${error.code}, error.message is ${error.message}`);
13. })
14. }
```

## writeImageMetadata23+

PhonePC/2in1TabletTVWearable

writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>

批量修改图片属性。使用Promise异步回调。

说明

* 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-apis-image-f.md#imagecreateimagesource7)实例或通过传入的uri创建[image.createImageSource](arkts-apis-image-f.md#imagecreateimagesource)实例。
* 该方法在内存中完成批量数据修改后会一次性写入文件，相比[modifyImageProperties](arkts-apis-image-imagesource.md#modifyimageproperties12)更高效。
* 支持修改JPEG、PNG和HEIF文件类型的图片属性，图片需要包含Exif信息。修改属性前，先通过supportedFormats属性查询设备是否支持HEIF格式的Exif读写。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageMetadata | [ImageMetadata](arkts-apis-image-i.md#imagemetadata23) | 是 | 图像的元数据集。若imageMetadata中的属性值都为空，则清空所有Exif元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. |
| 7700204 | Invalid parameter. Possible causes: The imageSource object is released. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function WriteImageMetadata(imageSourceObj : image.ImageSource) {
4. let propertyKeys = ["ImageWidth", "HwMnoteIsXmageSupported"];
5. let metaData = await imageSourceObj.readImageMetadata(propertyKeys);
6. if (metaData != undefined && metaData.exifMetadata != undefined) {
7. metaData.exifMetadata.imageLength = 3072;
8. }
9. await imageSourceObj.writeImageMetadata(metaData).then(() => {
10. console.info(`write image metadata success.`);
11. }).catch((error: BusinessError) => {
12. console.error(`writeImageMetadata failed error.code is ${error.code}, error.message is ${error.message}`);
13. });
14. }
```

## updateData9+

PhonePC/2in1TabletTVWearable

updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number): Promise<void>

更新增量数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 存放增量数据的buffer。 |
| isFinished | boolean | 是 | true表示数据更新完成，当前buffer内存放最后一段数据；false表示数据还未更新完成，需要继续更新。 |
| offset | number | 是 | 即当前buffer中的数据首地址，相对于整个图片文件首地址的偏移量。单位：字节。 |
| length | number | 是 | 当前buffer的长度。单位：字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function UpdateDatay(imageSourceObj : image.ImageSource) {
4. const array: ArrayBuffer = new ArrayBuffer(100);
5. imageSourceObj.updateData(array, false, 0, 10).then(() => {
6. console.info('Succeeded in updating data.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to update data.code is ${err.code},message is ${err.message}`);
9. })
10. }
```

## updateData9+

PhonePC/2in1TabletTVWearable

updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number, callback: AsyncCallback<void>): void

更新增量数据。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 存放增量数据的buffer。 |
| isFinished | boolean | 是 | true表示数据更新完成，当前buffer内存放最后一段数据；false表示数据还未更新完成，需要继续更新。 |
| offset | number | 是 | 即当前buffer中的数据首地址，相对于整个图片文件首地址的偏移量。单位：字节。 |
| length | number | 是 | 当前buffer的长度。单位：字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当更新增量数据成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function UpdateDatay(imageSourceObj : image.ImageSource) {
4. const array: ArrayBuffer = new ArrayBuffer(100);
5. imageSourceObj.updateData(array, false, 0, 10, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to update data.code is ${err.code},message is ${err.message}`);
8. } else {
9. console.info('Succeeded in updating data.');
10. }
11. })
12. }
```

## createPicture13+

PhonePC/2in1TabletTVWearable

createPicture(options?: DecodingOptionsForPicture): Promise<Picture>

通过图片解码参数创建Picture对象。使用Promise异步回调。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-apis-image-picture.md#release13)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptionsForPicture](arkts-apis-image-i.md#decodingoptionsforpicture13) | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Picture](arkts-apis-image-picture.md)> | Promise对象，返回Picture。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.2.Incorrect parameter types; 3.Parameter verification failed. |
| 7700203 | Unsupported options. For example, unsupported desiredPixelFormat causes a failure in converting an image into the desired pixel format. |
| 7700301 | Decode failed. |

**示例：**

```
1. async function CreatePicture(imageSourceObj : image.ImageSource) {
2. let options: image.DecodingOptionsForPicture = {
3. desiredAuxiliaryPictures: [image.AuxiliaryPictureType.GAINMAP] // GAINMAP为需要解码的辅助图类型。
4. };
5. let pictureObj: image.Picture = await imageSourceObj.createPicture(options);
6. if (pictureObj != null) {
7. console.info('Create picture succeeded');
8. } else {
9. console.error('Create picture failed');
10. }
11. }
```

## createPictureAtIndex20+

PhonePC/2in1TabletTVWearable

createPictureAtIndex(index: number): Promise<Picture>

通过指定序号的图片（目前仅支持GIF和HEIF23+图像序列格式）创建Picture对象。使用Promise异步回调。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-apis-image-picture.md#release13)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 解码图片序号。图片序号有效的取值范围为：[0, (帧数-1)]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Picture](arkts-apis-image-picture.md)> | Promise对象，返回Picture。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700101 | Bad source. |
| 7700102 | Unsupported MIME type. |
| 7700103 | Image too large. |
| 7700203 | Unsupported options. For example, index is invalid. |
| 7700301 | Decoding failed. |

**示例：**

```
1. async function CreatePictures(imageSourceObj : image.ImageSource) {
2. let frameCount: number = await imageSourceObj.getFrameCount();
3. for (let index = 0; index < frameCount; index++) {
4. try {
5. let pictureObj: image.Picture = await imageSourceObj.createPictureAtIndex(index);
6. console.info('Create picture succeeded for frame: ' + index);
7. } catch (e) {
8. console.error('Create picture failed for frame: ' + index);
9. }
10. }
11. }
```

## createPixelMap7+

PhonePC/2in1TabletTVWearable

createPixelMap(options?: DecodingOptions): Promise<PixelMap>

通过图片解码参数创建PixelMap对象。使用Promise异步回调。

从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-apis-image-imagesource.md#createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](arkts-apis-image-e.md#allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../harmonyos-guides/image-allocator-type.md)。

说明

* 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。
* 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。
* 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMap(imageSourceObj : image.ImageSource) {
4. imageSourceObj.createPixelMap().then((pixelMap: image.PixelMap) => {
5. console.info('Succeeded in creating pixelMap object through image decoding parameters.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to create pixelMap object through image decoding parameters, error.code ${error.code}, error.message ${error.message}`);
8. })
9. }
```

## createPixelMap7+

PhonePC/2in1TabletTVWearable

createPixelMap(callback: AsyncCallback<PixelMap>): void

通过默认参数创建PixelMap对象。使用callback异步回调。

从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-apis-image-imagesource.md#createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](arkts-apis-image-e.md#allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../harmonyos-guides/image-allocator-type.md)。

说明

* 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。
* 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。
* 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数，当创建PixelMap对象成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMap(imageSourceObj : image.ImageSource) {
4. imageSourceObj.createPixelMap((err: BusinessError, pixelMap: image.PixelMap) => {
5. if (err) {
6. console.error(`Failed to create pixelMap.code is ${err.code},message is ${err.message}`);
7. } else {
8. console.info('Succeeded in creating pixelMap object.');
9. }
10. })
11. }
```

## createPixelMap7+

PhonePC/2in1TabletTVWearable

createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void

通过图片解码参数创建PixelMap对象。使用callback异步回调。

从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-apis-image-imagesource.md#createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](arkts-apis-image-e.md#allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../harmonyos-guides/image-allocator-type.md)。

说明

* 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。
* 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。
* 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 是 | 解码参数。 |
| callback | AsyncCallback<[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数，当创建PixelMap对象成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMap(imageSourceObj : image.ImageSource) {
4. let decodingOptions: image.DecodingOptions = {
5. sampleSize: 1,
6. editable: true,
7. desiredSize: { width: 1, height: 2 },
8. rotate: 10,
9. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
10. desiredRegion: { size: { width: 1, height: 2 }, x: 0, y: 0 },
11. // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
12. cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
13. index: 0
14. };
15. imageSourceObj.createPixelMap(decodingOptions, (err: BusinessError, pixelMap: image.PixelMap) => {
16. if (err) {
17. console.error(`Failed to create pixelMap.code is ${err.code},message is ${err.message}`);
18. } else {
19. console.info('Succeeded in creating pixelMap object.');
20. }
21. })
22. }
```

## createPixelMapSync12+

PhonePC/2in1TabletTVWearable

createPixelMapSync(options?: DecodingOptions): PixelMap

通过图片解码参数同步创建PixelMap对象。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

从API version 15开始，推荐使用[createPixelMapUsingAllocatorSync](arkts-apis-image-imagesource.md#createpixelmapusingallocatorsync15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](arkts-apis-image-e.md#allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../harmonyos-guides/image-allocator-type.md)。

说明

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](../harmonyos-guides/time-consuming-task-overview.md)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 用于同步返回创建结果。 |

**示例：**

```
1. function CreatePixelMapSync(context : Context) {
2. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
3. let filePath: string = context.filesDir + "/test.jpg";
4. let imageSource = image.createImageSource(filePath);
5. let decodingOptions: image.DecodingOptions = {
6. sampleSize: 1,
7. editable: true,
8. desiredSize: { width: 1, height: 2 },
9. rotate: 10,
10. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
11. desiredRegion: { size: { width: 1, height: 2 }, x: 0, y: 0 },
12. // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
13. cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
14. index: 0
15. };
16. let pixelmap = imageSource.createPixelMapSync(decodingOptions);
17. if (pixelmap != undefined) {
18. console.info('Succeeded in creating pixelMap object.');
19. } else {
20. console.error('Failed to create pixelMap.');
21. }
22. }
```

## createPixelMapList10+

PhonePC/2in1TabletTVWearable

createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>

通过图片解码参数创建PixelMap数组。使用Promise异步回调。

针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

说明

* 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。
* 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。
* 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。
* 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[PixelMap](arkts-apis-image-pixelmap.md)>> | 异步返回PixelMap数组。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
4. let decodeOpts: image.DecodingOptions = {
5. sampleSize: 1,
6. editable: true,
7. desiredSize: { width: 198, height: 202 },
8. rotate: 0,
9. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
10. index: 0,
11. };
12. imageSourceObj.createPixelMapList(decodeOpts).then((pixelMapList: Array<image.PixelMap>) => {
13. console.info('Succeeded in creating pixelMapList object.');
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to create pixelMapList object, error code is ${err}`);
16. })
17. }
```

## createPixelMapList10+

PhonePC/2in1TabletTVWearable

createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void

通过默认参数创建PixelMap数组。使用callback异步回调。

针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

说明

* 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。
* 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。
* 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。
* 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[PixelMap](arkts-apis-image-pixelmap.md)>> | 是 | 回调函数，当创建PixelMap对象数组成功，err为undefined，data为获取到的PixelMap对象数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
4. imageSourceObj.createPixelMapList((err: BusinessError, pixelMapList: Array<image.PixelMap>) => {
5. if (err) {
6. console.error(`Failed to create pixelMapList object, error code is ${err}`);
7. } else {
8. console.info('Succeeded in creating pixelMapList object.');
9. }
10. })
11. }
```

## createPixelMapList10+

PhonePC/2in1TabletTVWearable

createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void

通过图片解码参数创建PixelMap数组。使用callback异步回调。

针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

说明

* 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。
* 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。
* 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。
* 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 是 | 解码参数。 |
| callback | AsyncCallback<Array<[PixelMap](arkts-apis-image-pixelmap.md)>> | 是 | 回调函数，当创建PixelMap对象数组成功，err为undefined，data为获取到的PixelMap对象数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
4. let decodeOpts: image.DecodingOptions = {
5. sampleSize: 1,
6. editable: true,
7. desiredSize: { width: 198, height: 202 },
8. rotate: 0,
9. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
10. index: 0,
11. };
12. imageSourceObj.createPixelMapList(decodeOpts, (err: BusinessError, pixelMapList: Array<image.PixelMap>) => {
13. if (err) {
14. console.error(`Failed to create pixelMapList object, error code is ${err}`);
15. } else {
16. console.info('Succeeded in creating pixelMapList object.');
17. }
18. })
19. }
```

## createPixelMapUsingAllocator15+

PhonePC/2in1TabletTVWearable

createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>

使用指定的分配器根据图像解码参数异步创建PixelMap对象。使用Promise异步回调。接口使用详情请参考[图片解码内存优化(ArkTS)](../harmonyos-guides/image-allocator-type.md)。

说明

* 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。
* 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。
* 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 否 | 解码参数。 |
| allocatorType | [AllocatorType](arkts-apis-image-e.md#allocatortype15) | 否 | 用于图像解码的内存类型。默认值为AllocatorType.AUTO。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed. |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported mimetype. |
| 7700103 | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| 7700201 | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| 7700203 | Unsupported options, e.g., cannot convert image into desired pixel format. |
| 7700301 | Failed to decode image. |
| 7700302 | Failed to allocate memory. |

**示例：**

```
1. async function CreatePixelMapUsingAllocator(context : Context) {
2. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
3. let filePath: string = context.filesDir + "/test.jpg";
4. let imageSource = image.createImageSource(filePath);
5. let decodingOptions: image.DecodingOptions = {
6. editable: true,
7. desiredSize: { width: 3072, height: 4096 },
8. rotate: 10,
9. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
10. desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
11. // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
12. cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
13. index: 0
14. };
15. let pixelmap = imageSource.createPixelMapUsingAllocator(decodingOptions, image.AllocatorType.AUTO);
16. if (pixelmap != undefined) {
17. console.info('Succeeded in creating pixelMap object.');
18. } else {
19. console.error('Failed to create pixelMap.');
20. }
21. }
```

## createPixelMapUsingAllocatorSync15+

PhonePC/2in1TabletTVWearable

createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap

根据指定的分配器同步创建一个基于图像解码参数的PixelMap对象。接口使用详情请参考[图片解码内存优化(ArkTS)](../harmonyos-guides/image-allocator-type.md)。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

说明

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](../harmonyos-guides/time-consuming-task-overview.md)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 否 | 解码参数。 |
| allocatorType | [AllocatorType](arkts-apis-image-e.md#allocatortype15) | 否 | 用于图像解码的内存类型。默认值为AllocatorType.AUTO。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 用于同步返回创建结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed. |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported mimetype. |
| 7700103 | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| 7700201 | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| 7700203 | Unsupported options, e.g., cannot convert image into desired pixel format. |
| 7700301 | Failed to decode image. |
| 7700302 | Failed to allocate memory. |

**示例：**

```
1. async function CreatePixelMapUsingAllocator(context : Context) {
2. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
3. let filePath: string = context.filesDir + "/test.jpg";
4. let imageSource = image.createImageSource(filePath);
5. let decodingOptions: image.DecodingOptions = {
6. editable: true,
7. desiredSize: { width: 3072, height: 4096 },
8. rotate: 10,
9. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
10. desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
11. // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
12. cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
13. index: 0
14. };
15. let pixelmap = imageSource.createPixelMapUsingAllocatorSync(decodingOptions, image.AllocatorType.AUTO);
16. if (pixelmap != undefined) {
17. console.info('Succeeded in creating pixelMap object.');
18. } else {
19. console.error('Failed to create pixelMap.');
20. }
21. }
```

## getDelayTimeList10+

PhonePC/2in1TabletTVWearable

getDelayTimeList(callback: AsyncCallback<Array<number>>): void

获取图像延迟时间数组。使用callback异步回调。此接口仅用于gif图片和webp图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，当获取图像延迟时间数组成功，err为undefined，data为获取到的图像延时时间数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980149 | Invalid MIME type for the image source. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetDelayTimeList(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getDelayTimeList((err: BusinessError, delayTimes: Array<number>) => {
5. if (err) {
6. console.error(`Failed to get delayTimes object.code is ${err.code},message is ${err.message}`);
7. } else {
8. console.info('Succeeded in getting delayTimes object.');
9. }
10. })
11. }
```

## getDelayTimeList10+

PhonePC/2in1TabletTVWearable

getDelayTimeList(): Promise<Array<number>>

获取图像延迟时间数组。使用Promise异步回调。此接口仅用于gif图片和webp图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回延迟时间数组。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980149 | Invalid MIME type for the image source. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetDelayTimeList(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getDelayTimeList().then((delayTimes: Array<number>) => {
5. console.info('Succeeded in getting delayTimes object.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get delayTimes object.code is ${err.code},message is ${err.message}`);
8. })
9. }
```

## getFrameCount10+

PhonePC/2in1TabletTVWearable

getFrameCount(callback: AsyncCallback<number>): void

获取图像帧数。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，当获取图像帧数成功，err为undefined，data为获取到的图像帧数；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980137 | Invalid media operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetFrameCount(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getFrameCount((err: BusinessError, frameCount: number) => {
5. if (err) {
6. console.error(`Failed to get frame count.code is ${err.code},message is ${err.message}`);
7. } else {
8. console.info('Succeeded in getting frame count.');
9. }
10. })
11. }
```

## getFrameCount10+

PhonePC/2in1TabletTVWearable

getFrameCount(): Promise<number>

获取图像帧数。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回图像帧数。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980137 | Invalid media operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetFrameCount(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getFrameCount().then((frameCount: number) => {
5. console.info('Succeeded in getting frame count.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get frame count.code is ${err.code},message is ${err.message}`);
8. })
9. }
```

## getDisposalTypeList12+

PhonePC/2in1TabletTVWearable

getDisposalTypeList(): Promise<Array<number>>

获取图像帧过渡模式数组。使用Promise异步回调。此接口仅用于gif图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回帧过渡模式数组。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980137 | Invalid media operation. |
| 62980149 | Invalid MIME type for the image source. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetDisposalTypeList(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getDisposalTypeList().then((disposalTypes: Array<number>) => {
5. console.info('Succeeded in getting disposalTypes object.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get disposalTypes object.code ${err.code},message is ${err.message}`);
8. })
9. }
```

## release

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放ImageSource实例。使用callback异步回调。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当资源释放成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release(imageSourceObj : image.ImageSource) {
4. imageSourceObj.release((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
7. } else {
8. console.info('Succeeded in releasing the image source instance.');
9. }
10. })
11. }
```

## release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放ImageSource实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release(imageSourceObj : image.ImageSource) {
4. imageSourceObj.release().then(() => {
5. console.info('Succeeded in releasing the image source instance.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to release the image source instance.code ${error.code},message is ${error.message}`);
8. })
9. }
```

## getImageProperty(deprecated)

PhonePC/2in1TabletTVWearable

getImageProperty(key:string, options?: GetImagePropertyOptions): Promise<string>

获取图片中给定索引处图像的指定属性键的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](arkts-apis-image-imagesource.md#getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| options | [GetImagePropertyOptions](arkts-apis-image-i.md#getimagepropertyoptionsdeprecated) | 否 | 图片属性，包括图片序号与默认属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回图片属性值，如获取失败则返回属性默认值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageProperty(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getImageProperty("BitsPerSample")
5. .then((data: string) => {
6. console.info('Succeeded in getting the value of the specified attribute key of the image.');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
9. })
10. }
```

## getImageProperty(deprecated)

PhonePC/2in1TabletTVWearable

getImageProperty(key:string, callback: AsyncCallback<string>): void

获取图片中给定索引处图像的指定属性键的值。使用callback异步回调。

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](arkts-apis-image-imagesource.md#getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| callback | AsyncCallback<string> | 是 | 回调函数，当获取图片属性值成功，err为undefined，data为获取到的图片属性值；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageProperty(imageSourceObj : image.ImageSource) {
4. imageSourceObj.getImageProperty("BitsPerSample", (error: BusinessError, data: string) => {
5. if (error) {
6. console.error('Failed to get the value of the specified attribute key of the image.');
7. } else {
8. console.info('Succeeded in getting the value of the specified attribute key of the image.');
9. }
10. })
11. }
```

## getImageProperty(deprecated)

PhonePC/2in1TabletTVWearable

getImageProperty(key:string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void

获取图片指定属性键的值。使用callback异步回调。

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](arkts-apis-image-imagesource.md#getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| options | [GetImagePropertyOptions](arkts-apis-image-i.md#getimagepropertyoptionsdeprecated) | 是 | 图片属性，包括图片序号与默认属性值。 |
| callback | AsyncCallback<string> | 是 | 回调函数，当获取图片属性值成功，err为undefined，data为获取到的图片属性值；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageProperty(imageSourceObj : image.ImageSource) {
4. let property: image.GetImagePropertyOptions = { index: 0, defaultValue: '9999' }
5. imageSourceObj.getImageProperty("BitsPerSample", property, (error: BusinessError, data: string) => {
6. if (error) {
7. console.error('Failed to get the value of the specified attribute key of the image.');
8. } else {
9. console.info('Succeeded in getting the value of the specified attribute key of the image.');
10. }
11. })
12. }
```

## modifyImageProperty(deprecated)

PhonePC/2in1TabletTVWearable

modifyImageProperty(key: string, value: string): Promise<void>

通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

* 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。
* 从API version 9开始支持，从API version 11废弃，建议使用[modifyImageProperty](arkts-apis-image-imagesource.md#modifyimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| value | string | 是 | 属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
4. imageSourceObj.modifyImageProperty("ImageWidth", "120").then(() => {
5. imageSourceObj.getImageProperty("ImageWidth").then((width: string) => {
6. console.info(`ImageWidth is :${width}`);
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to get the Image Width, error.code ${error.code}, error.message ${error.message}`);
9. })
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to modify the Image Width, error.code ${error.code}, error.message ${error.message}`);
12. })
13. }
```

## modifyImageProperty(deprecated)

PhonePC/2in1TabletTVWearable

modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void

通过指定的键修改图片属性的值。使用callback异步回调。

仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

说明

* 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。
* 从API version 9开始支持，从API version 11废弃，建议使用[modifyImageProperty](arkts-apis-image-imagesource.md#modifyimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| value | string | 是 | 属性值。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当修改图片属性值成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
4. imageSourceObj.modifyImageProperty("ImageWidth", "120", (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to modify the Image Width.code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('Succeeded in modifying the Image Width.');
9. }
10. })
11. }
```
