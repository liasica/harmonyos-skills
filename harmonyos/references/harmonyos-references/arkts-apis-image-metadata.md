---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-metadata
title: Interface (Metadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (Metadata)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8b91ef4743dd89a6d9aa938e772a99f49aa52e13f5ebb0b8bcbe4a2f62aeca2
---

Metadata类，用于存储图像的元数据。目前支持的元数据类型可参考[MetadataType](arkts-apis-image-e.md#metadatatype13)。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 13开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## getProperties13+

PhonePC/2in1TabletTVWearable

getProperties(key: Array<string>): Promise<Record<string, string | null>>

获取图像中属性的值。使用Promise异步回调。

如要查询属性值信息请参考[PropertyKey](arkts-apis-image-e.md#propertykey7)、[FragmentMapPropertyKey](arkts-apis-image-e.md#fragmentmappropertykey13)和[GifPropertyKey](arkts-apis-image-e.md#gifpropertykey20)和[HeifsPropertyKey](arkts-apis-image-e.md#heifspropertykey23)。

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

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetProperties(context: Context) {
4. const resourceMgr = context.resourceManager;
5. const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
6. let ops: image.SourceOptions = {
7. sourceDensity: 98,
8. }
9. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
10. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
11. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
12. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
13. let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
14. if (metaData != null) {
15. await metaData.getProperties(["ImageWidth", "ImageLength"]).then((data2) => {
16. console.info('Get properties ',JSON.stringify(data2));
17. }).catch((error: BusinessError) => {
18. console.error(`Get properties failed error.code is ${error.code}, error.message is ${error.message}`);
19. });
20. } else {
21. console.error('Metadata is null.');
22. }
23. }
```

## setProperties13+

PhonePC/2in1TabletTVWearable

setProperties(records: Record<string, string | null>): Promise<void>

批量设置图片元数据中的指定属性的值。使用Promise异步回调。

如要查询属性值信息请参考[PropertyKey](arkts-apis-image-e.md#propertykey7)、[FragmentMapPropertyKey](arkts-apis-image-e.md#fragmentmappropertykey13)和[GifPropertyKey](arkts-apis-image-e.md#gifpropertykey20)和[HeifsPropertyKey](arkts-apis-image-e.md#heifspropertykey23)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<string, string | null> | 是 | 要修改的属性和值的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，如获取失败则返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function SetProperties(context: Context) {
4. const resourceMgr = context.resourceManager;
5. const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
6. let ops: image.SourceOptions = {
7. sourceDensity: 98,
8. }
9. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
10. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
11. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
12. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
13. let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
14. if (metaData != null) {
15. let setkey: Record<string, string | null> = {
16. "ImageWidth": "200",
17. "ImageLength": "300"
18. };
19. await metaData.setProperties(setkey).then(async () => {
20. console.info('Set AuxPictureObj properties success.');
21. }).catch((error: BusinessError) => {
22. console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
23. })
24. } else {
25. console.error('AuxPictureObj metadata is null. ');
26. }
27. }
```

## getAllProperties13+

PhonePC/2in1TabletTVWearable

getAllProperties(): Promise<Record<string, string | null>>

获取图片中所有元数据的属性和值。使用Promise异步回调。

如要查询属性值信息请参考[PropertyKey](arkts-apis-image-e.md#propertykey7)、[FragmentMapPropertyKey](arkts-apis-image-e.md#fragmentmappropertykey13)和[GifPropertyKey](arkts-apis-image-e.md#gifpropertykey20)和[HeifsPropertyKey](arkts-apis-image-e.md#heifspropertykey23)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, string | null>> | Promise对象，返回元数据拥有的所有属性的值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetAllProperties(context: Context) {
4. const resourceMgr = context.resourceManager;
5. const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
6. let ops: image.SourceOptions = {
7. sourceDensity: 98,
8. }
9. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
10. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
11. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
12. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
13. let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
14. if (metaData != null) {
15. await metaData.getAllProperties().then((data2) => {
16. const count = Object.keys(data2).length;
17. console.info('Metadata have ', count, ' properties');
18. console.info(`Get metadata all properties: ${data2}`);
19. }).catch((error: BusinessError) => {
20. console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
21. });
22. } else {
23. console.error('Metadata is null.');
24. }
25. }
```

## clone13+

PhonePC/2in1TabletTVWearable

clone(): Promise<Metadata>

对元数据进行克隆。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Metadata](arkts-apis-image-metadata.md)> | Promise对象，成功返回元数据实例。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Clone(context: Context) {
4. const resourceMgr = context.resourceManager;
5. const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
6. let ops: image.SourceOptions = {
7. sourceDensity: 98,
8. }
9. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
10. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
11. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
12. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
13. let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
14. if (metaData != null) {
15. let new_metadata: image.Metadata = await metaData.clone();
16. new_metadata.getProperties(["ImageWidth"]).then((data1) => {
17. console.info(`Clone new_metadata and get Properties: ${data1}`);
18. }).catch((err: BusinessError) => {
19. console.error(`Clone new_metadata failed, error : ${err}`);
20. });
21. } else {
22. console.error('Metadata is null.');
23. }
24. }
```

## getBlob23+

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

10. async function GetBlob(context: Context) {
11. let fd = getFileFd(context);
12. let imageSource = image.createImageSource(fd);
13. let pictureObj: image.Picture = await imageSource.createPicture();
14. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
15. let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
16. if (metaData != null) {
17. let blob = await metaData.getBlob();
18. if (blob != undefined) {
19. console.info("get blob success");
20. }
21. }
22. }
```

## setBlob23+

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

10. async function setBlob(context: Context) {
11. let fd = getFileFd(context);
12. let imageSource = image.createImageSource(fd);
13. let pictureObj: image.Picture = await imageSource.createPicture();
14. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
15. let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
16. if (metaData != null) {
17. let blob = await metaData.getBlob();
18. if (blob != undefined) {
19. console.info("get blob success");
20. metaData.setBlob(blob);
21. }
22. let new_blob = metaData.getBlob();
23. if (new_blob != undefined) {
24. console.info("new_blob is not undefined");
25. }
26. }
27. }
```
