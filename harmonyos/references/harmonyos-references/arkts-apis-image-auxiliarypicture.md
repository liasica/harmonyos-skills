---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-auxiliarypicture
title: Interface (AuxiliaryPicture)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (AuxiliaryPicture)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b861c9fe643241bf9ecd7afda4bc98a01b6ada05a4d08aec71297f3125bea1b
---

AuxiliaryPicture类，用于读取或写入图像的辅助图数据以及获取图像的辅助图信息。目前支持的辅助图类型可参考[AuxiliaryPictureType](arkts-apis-image-e.md#auxiliarypicturetype13)。

在调用AuxiliaryPicture的方法前，需要通过[image.createAuxiliaryPicture](arkts-apis-image-f.md#imagecreateauxiliarypicture13)或Picture的[getAuxiliaryPicture](arkts-apis-image-picture.md#getauxiliarypicture13)创建一个AuxiliaryPicture实例。

由于图片占用内存较大，所以当AuxiliaryPicture对象使用完成后，应主动调用[release](arkts-apis-image-auxiliarypicture.md#release13)方法及时释放对象。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该对象。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 13开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## writePixelsFromBuffer13+

PhonePC/2in1TabletTVWearable

writePixelsFromBuffer(data: ArrayBuffer): Promise<void>

读取ArrayBuffer中的辅助图片数据，并将数据写入AuxiliaryPicture对象。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 辅助图像素数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例:**

```
1. async function WritePixelsFromBuffer(context: Context) {
2. const resourceMgr = context.resourceManager;
3. const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // 需要支持hdr的图片。
4. let ops: image.SourceOptions = {
5. sourceDensity: 98,
6. }
7. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
8. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
9. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
10. let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
11. if(auxPictureObj != null) {
12. let auxBuffer: ArrayBuffer = await auxPictureObj.readPixelsToBuffer();
13. await auxPictureObj.writePixelsFromBuffer(auxBuffer);
14. console.info('Write pixels from buffer success.');
15. } else {
16. console.error('AuxPictureObj is null.');
17. }
18. }
```

## readPixelsToBuffer13+

PhonePC/2in1TabletTVWearable

readPixelsToBuffer(): Promise<ArrayBuffer>

读取图像像素映射数据并将数据写入ArrayBuffer。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象。返回辅助图像素数据。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ReadPixelsToBuffer(context: Context) {
4. const resourceMgr = context.resourceManager;
5. const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // 需要支持hdr的图片。
6. let ops: image.SourceOptions = {
7. sourceDensity: 98,
8. }
9. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
10. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
11. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
12. let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
13. if(auxPictureObj != null) {
14. await auxPictureObj.readPixelsToBuffer().then((pixelsBuffer: ArrayBuffer) => {
15. console.info('Read pixels to buffer success.' );
16. }).catch((error: BusinessError) => {
17. console.error(`Read pixels to buffer failed error.code: ${error.code}, error.message: ${error.message}`);
18. });
19. } else {
20. console.error('AuxPictureObj is null.');
21. }
22. }
```

## getType13+

PhonePC/2in1TabletTVWearable

getType(): AuxiliaryPictureType

获取辅助图的类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuxiliaryPictureType](arkts-apis-image-e.md#auxiliarypicturetype13) | 操作成功，返回辅助图的类型。 |

**示例：**

```
1. async function GetAuxiliaryPictureType(auxPictureObj : image.AuxiliaryPicture) {
2. if (auxPictureObj != null) {
3. let type: image.AuxiliaryPictureType = auxPictureObj.getType();
4. console.info('Success get auxiliary picture type ' +  JSON.stringify(type));
5. } else {
6. console.error('Failed get auxiliary picture type ');
7. }
8. }
```

## setMetadata13+

PhonePC/2in1TabletTVWearable

setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>

设置辅助图元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-apis-image-e.md#metadatatype13) | 是 | 元数据的类型，用于设置对应的元数据。 |
| metadata | [Metadata](arkts-apis-image-metadata.md) | 是 | 元数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function SetAuxPictureObjMetadata(exifContext: Context, auxPictureObj: image.AuxiliaryPicture) {
4. const exifResourceMgr = exifContext.resourceManager;
5. const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 图片包含exif metadata。
6. let exifOps: image.SourceOptions = {
7. sourceDensity: 98,
8. }
9. let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
10. let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
11. let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
12. if (exifPictureObj != null) {
13. console.info('Create picture succeeded');
14. } else {
15. console.error('Create picture failed');
16. }

18. if (auxPictureObj != null) {
19. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
20. let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
21. auxPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
22. console.info('Set metadata success');
23. }).catch((error: BusinessError) => {
24. console.error(`Set metadata failed.error.code: ${error.code}, error.message: ${error.message}`);
25. });
26. } else {
27. console.error('AuxPictureObjMetaData is null');
28. }
29. }
```

## getMetadata13+

PhonePC/2in1TabletTVWearable

getMetadata(metadataType: MetadataType): Promise<Metadata>

从辅助图中获取元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-apis-image-e.md#metadatatype13) | 是 | 元数据类型，用于获取对应类型的元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Metadata](arkts-apis-image-metadata.md)> | Promise对象，返回元数据的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```
1. async function GetAuxPictureObjMetadata(auxPictureObj: image.AuxiliaryPicture) {
2. if (auxPictureObj != null) {
3. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
4. let auxPictureObjMetaData: image.Metadata | null = await auxPictureObj.getMetadata(metadataType);
5. if (auxPictureObjMetaData != null) {
6. console.info('Get AuxPictureObj Metadata success' );
7. } else {
8. console.error('Get AuxPictureObj Metadata failed');
9. }
10. } else {
11. console.error('Get AuxPictureObj is null.');
12. }
13. }
```

## getAuxiliaryPictureInfo13+

PhonePC/2in1TabletTVWearable

getAuxiliaryPictureInfo(): AuxiliaryPictureInfo

获取有关此辅助图的图像信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuxiliaryPictureInfo](arkts-apis-image-i.md#auxiliarypictureinfo13) | 返回辅助图图像信息。 |

**示例：**

```
1. async function GetAuxiliaryPictureInfo(auxPictureObj: image.AuxiliaryPicture) {
2. if(auxPictureObj != null) {
3. let auxinfo: image.AuxiliaryPictureInfo = auxPictureObj.getAuxiliaryPictureInfo();
4. console.info('GetAuxiliaryPictureInfo Type: ' + auxinfo.auxiliaryPictureType +
5. ' height: ' + auxinfo.size.height + ' width: ' + auxinfo.size.width +
6. ' rowStride: ' +  auxinfo.rowStride +  ' pixelFormat: ' + auxinfo.pixelFormat +
7. ' colorSpace: ' +  auxinfo.colorSpace);
8. } else {
9. console.error('Get auxiliary picture information failed');
10. }
11. }
```

## setAuxiliaryPictureInfo13+

PhonePC/2in1TabletTVWearable

setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void

设置辅助图的图像信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [AuxiliaryPictureInfo](arkts-apis-image-i.md#auxiliarypictureinfo13) | 是 | 辅助图的图像信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. import { colorSpaceManager } from '@kit.ArkGraphics2D';

3. async function SetAuxiliaryPictureInfo(auxPictureObj: image.AuxiliaryPicture) {
4. if(auxPictureObj != null) {
5. let colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
6. let info: image.AuxiliaryPictureInfo = {
7. auxiliaryPictureType: image.AuxiliaryPictureType.GAINMAP,
8. size: {height: 100, width: 200},
9. pixelFormat: image.PixelMapFormat.RGBA_8888,
10. rowStride: 0,
11. colorSpace: colorSpaceManager.create(colorSpaceName),
12. };
13. auxPictureObj.setAuxiliaryPictureInfo(info);
14. }
15. }
```

## release13+

PhonePC/2in1TabletTVWearable

release():void

释放辅助图对象，无返回值。

由于图片占用内存较大，所以当AuxiliaryPicture对象使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**示例：**

```
1. async function Release(auxPictureObj: image.AuxiliaryPicture) {
2. let funcName = "Release";
3. if (auxPictureObj != null) {
4. auxPictureObj.release();
5. if (auxPictureObj.getType() == null) {
6. console.info(funcName, 'Success !');
7. } else {
8. console.error(funcName, 'Failed !');
9. }
10. } else {
11. console.error('PictureObj is null');
12. }
13. }
```
