---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-picture
title: Interface (Picture)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (Picture)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30ffc70baceb1d0be1661d871a7f1d3ff5fa796d6d8461422f620c6035a7f3be
---

Picture类，一些包含特殊信息的图片可以解码为Picture（也可以称为多图对象）。多图对象一般包含主图、辅助图和元数据。其中主图包含图像的大部分信息，主要用于显示图像内容；辅助图用于存储与主图相关但不同的数据，展示图像更丰富的信息；元数据一般用来存储关于图像文件的信息。多图对象类用于读取或写入多图对象。在调用Picture的方法前，需要先通过[image.createPicture](arkts-apis-image-f.md#imagecreatepicture13)创建一个Picture实例。

由于图片占用内存较大，所以当Picture实例使用完成后，应主动调用[release](arkts-apis-image-picture.md#release13)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 13开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## getMainPixelmap13+

PhonePC/2in1TabletTVWearable

getMainPixelmap(): PixelMap

获取主图的pixelmap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 同步返回PixelMap对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetMainPixelmap(pictureObj : image.Picture) {
4. let funcName = "getMainPixelmap";
5. if (pictureObj != null) {
6. let mainPixelmap: image.PixelMap = pictureObj.getMainPixelmap();
7. if (mainPixelmap != null) {
8. mainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
9. if (imageInfo != null) {
10. console.info('GetMainPixelmap information height:' + imageInfo.size.height + ' width:' + imageInfo.size.width);
11. }
12. }).catch((error: BusinessError) => {
13. console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
14. });
15. }
16. } else {
17. console.error('PictureObj is null');
18. }
19. }
```

## getHdrComposedPixelmap13+

PhonePC/2in1TabletTVWearable

getHdrComposedPixelmap(): Promise<PixelMap>

合成HDR图并获取HDR图的pixelmap。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600901 | Inner unknown error. Please check the logs for detailed information. |
| 7600201 | Unsupported operation. e.g.,1. The picture does not has a gainmap. 2. MainPixelMap's allocator type is not DMA. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetHdrComposedPixelmap(pictureObj : image.Picture) {
4. let funcName = "getHdrComposedPixelmap";
5. if (pictureObj != null) { // 图片包含Hdr图。
6. let hdrComposedPixelmap: image.PixelMap = await pictureObj.getHdrComposedPixelmap();
7. if (hdrComposedPixelmap != null) {
8. hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
9. if (imageInfo != null) {
10. console.info(`GetHdrComposedPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
11. }
12. }).catch((error: BusinessError) => {
13. console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
14. });
15. }
16. } else {
17. console.error('PictureObj is null');
18. }
19. }
```

## getHdrComposedPixelmapWithOptions23+

PhonePC/2in1TabletTVWearable

getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>

合成HDR图像并返回HDR图像的PixelMap，支持传入合成参数（如PixelMapFormat等）。使用Promise异步回调。

调用该接口的Picture对象中必须包含主图、增益图和元数据。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [HdrComposeOptions](arkts-apis-image-i.md#hdrcomposeoptions23) | 否 | 合成HDR的选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md) | undefined> | Promise对象，返回PixelMap或undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | Unsupported operation. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function GetHdrComposedPixelmapWithOptions(picture : image.Picture) {
5. if (picture == null) {
6. console.error('picture is null');
7. return;
8. }

10. let opt: image.HdrComposeOptions = {
11. desiredPixelFormat: image.PixelMapFormat.RGBA_1010102
12. };
13. let hdrComposedPixelmap: image.PixelMap | undefined = await picture.getHdrComposedPixelmapWithOptions(opt);
14. if (hdrComposedPixelmap == null || hdrComposedPixelmap == undefined) {
15. console.error(`GetHdrComposedPixelmapWithOptions failed`);
16. return;
17. }

19. hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
20. if (imageInfo !== null) {
21. console.info(`GetHdrComposedPixelmapWithOptions information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
22. }
23. }).catch((error: BusinessError) => {
24. console.error(`GetHdrComposedPixelmapWithOptions information failed error.code: ${error.code} ,error.message: ${error.message}`);
25. });
26. }
```

## getGainmapPixelmap13+

PhonePC/2in1TabletTVWearable

getGainmapPixelmap(): PixelMap | null

获取增益图的pixelmap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | null | 返回Pixelmap对象，如果没有则返回null。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetGainmapPixelmap(pictureObj : image.Picture) {
4. let funcName = "getGainmapPixelmap";
5. if (pictureObj != null) { // 图片包含增益图。
6. let gainPixelmap: image.PixelMap | null = pictureObj.getGainmapPixelmap();
7. if (gainPixelmap != null) {
8. gainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
9. if (imageInfo != null) {
10. console.info(`GetGainmapPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
11. } else {
12. console.error('GainPixelmap is null');
13. }
14. }).catch((error: BusinessError) => {
15. console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
16. });
17. } else {
18. console.info('GainPixelmap is null');
19. }
20. } else {
21. console.error('PictureObj is null');
22. }
23. }
```

## setAuxiliaryPicture13+

PhonePC/2in1TabletTVWearable

setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void

设置辅助图。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-apis-image-e.md#auxiliarypicturetype13) | 是 | 辅助图类型。 |
| auxiliaryPicture | [AuxiliaryPicture](arkts-apis-image-auxiliarypicture.md) | 是 | 辅助图对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. async function SetAuxiliaryPicture(context: Context) {
2. const resourceMgr = context.resourceManager;
3. const rawFile = await resourceMgr.getRawFileContent("hdr.jpg");// 需要支持hdr的图片。
4. let ops: image.SourceOptions = {
5. sourceDensity: 98,
6. }
7. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
8. let pixelMap: image.PixelMap = await imageSource.createPixelMap();
9. let pictureObj: image.Picture = image.createPicture(pixelMap);
10. if (pictureObj != null) {
11. console.info('Create picture succeeded');
12. } else {
13. console.error('Create picture failed');
14. }

16. if (pictureObj != null) {
17. let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
18. let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
19. if (auxPictureObj != null) {
20. pictureObj.setAuxiliaryPicture(type, auxPictureObj);
21. }
22. }
23. }
```

## getAuxiliaryPicture13+

PhonePC/2in1TabletTVWearable

getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null

根据类型获取辅助图。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-apis-image-e.md#auxiliarypicturetype13) | 是 | 辅助图类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuxiliaryPicture](arkts-apis-image-auxiliarypicture.md) | null | 返回AuxiliaryPicture对象，如果没有则返回null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. async function GetAuxiliaryPicture(pictureObj : image.Picture) {
2. if (pictureObj != null) {
3. let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
4. let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
5. }
6. }
```

## setMetadata13+

PhonePC/2in1TabletTVWearable

setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>

设置主图的元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-apis-image-e.md#metadatatype13) | 是 | 元数据类型。 |
| metadata | [Metadata](arkts-apis-image-metadata.md) | 是 | 元数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function SetPictureObjMetadata(exifContext: Context) {
4. const exifResourceMgr = exifContext.resourceManager;
5. const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 含有exif metadata的图片。
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

18. if (exifPictureObj != null) {
19. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
20. let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
21. exifPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
22. console.info('Set metadata success');
23. }).catch((error: BusinessError) => {
24. console.error('Failed to set metadata. error.code: ' +JSON.stringify(error.code) + ' ,error.message:' + JSON.stringify(error.message));
25. });
26. } else {
27. console.error('exifPictureObj is null');
28. }
29. }
```

## getMetadata13+

PhonePC/2in1TabletTVWearable

getMetadata(metadataType: MetadataType): Promise<Metadata>

获取主图的元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-apis-image-e.md#metadatatype13) | 是 | 元数据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Metadata](arkts-apis-image-metadata.md)> | Promise对象。返回元数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```
1. async function GetPictureObjMetadataProperties(pictureObj : image.Picture) {
2. if (pictureObj != null) {
3. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
4. let pictureObjMetaData: image.Metadata = await pictureObj.getMetadata(metadataType);
5. if (pictureObjMetaData != null) {
6. console.info('get picture metadata success');
7. } else {
8. console.error('get picture metadata is failed');
9. }
10. } else {
11. console.error(" pictureObj is null");
12. }
13. }
```

## marshalling13+

PhonePC/2in1TabletTVWearable

marshalling(sequence: rpc.MessageSequence): void

将picture序列化后写入MessageSequence。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 新创建的MessageSequence。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { rpc } from '@kit.IPCKit';

4. class MySequence implements rpc.Parcelable {
5. picture: image.Picture | null = null;
6. constructor(conPicture: image.Picture) {
7. this.picture = conPicture;
8. }
9. marshalling(messageSequence: rpc.MessageSequence) {
10. if(this.picture != null) {
11. this.picture.marshalling(messageSequence);
12. console.info('Marshalling success !');
13. return true;
14. } else {
15. console.error('Marshalling failed !');
16. return false;
17. }
18. }
19. unmarshalling(messageSequence : rpc.MessageSequence) {
20. this.picture = image.createPictureFromParcel(messageSequence);
21. this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
22. console.info(`Unmarshalling to get mainPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
23. }).catch((error: BusinessError) => {
24. console.error(`Unmarshalling failed error.code: ${error.code} ,error.message: ${error.message}`);
25. });
26. return true;
27. }
28. }

30. async function Marshalling_UnMarshalling(pictureObj : image.Picture) {
31. if (pictureObj != null) {
32. let parcelable: MySequence = new MySequence(pictureObj);
33. let data: rpc.MessageSequence = rpc.MessageSequence.create();
34. // 序列化。
35. data.writeParcelable(parcelable);
36. let ret: MySequence = new MySequence(pictureObj);
37. // 反序列化。
38. data.readParcelable(ret);
39. } else {
40. console.error('PictureObj is null');
41. }
42. }
```

## release13+

PhonePC/2in1TabletTVWearable

release(): void

释放picture对象。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用该方法及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**示例：**

```
1. async function Release(pictureObj : image.Picture) {
2. let funcName = "Release";
3. if (pictureObj != null) {
4. pictureObj.release();
5. if (pictureObj.getMainPixelmap() == null) {
6. console.info(funcName, 'Success !');
7. } else {
8. console.error(funcName, 'Failed !');
9. }
10. } else {
11. console.error('PictureObj is null');
12. }
13. }
```
