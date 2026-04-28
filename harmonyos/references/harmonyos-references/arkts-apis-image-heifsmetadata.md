---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-heifsmetadata
title: Class (HeifsMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (HeifsMetadata)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e70f494052665361f5bd958292e06ebc55b7df43e623a818b97015747ffe303
---

HeifsMetadata implements Metadata

HEIF序列图像元数据类，用于存储图像的元数据。

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
| heifsDelayTime | number | 是 | 是 | HEIF序列图片的每帧播放时长。单位为毫秒。 |

## createInstance

PhonePC/2in1TabletTVWearable

static createInstance(): HeifsMetadata

创建一个空的[HeifsMetadata](arkts-apis-image-heifsmetadata.md)实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HeifsMetadata](arkts-apis-image-heifsmetadata.md) | 返回HeifsMetadata的空实例。 |

**示例：**

```
1. async function heifsMetadataCreateInstance(context: Context) {
2. let heifsMetadata = image.HeifsMetadata.createInstance();
3. if (heifsMetadata != undefined) {
4. console.info("createInstance success");
5. }
6. }
```

## getProperties

PhonePC/2in1TabletTVWearable

getProperties(key: Array<string>): Promise<Record<string, string | null>>

获取图像元数据的属性值。使用Promise异步回调。

要查询的属性的具体信息请参考[HeifsPropertyKey](arkts-apis-image-e.md#heifspropertykey23)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | Array<string> | 是 | 要获取的值的属性名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, string | null>> | Promise对象，返回元数据要获取的属性的值，如果获取失败则返回错误码。 |

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
5. const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function heifsMetadataGetProperties(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
15. if (metaData != undefined && metaData.heifsMetadata != undefined) {
16. await metaData.heifsMetadata.getProperties(["HeifsDelayTime"]).then((data) => {
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

要查询的属性的具体信息请参考[HeifsPropertyKey](arkts-apis-image-e.md#heifspropertykey23)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<string, string | null> | 是 | 用户要修改HeifsMetadata对象的属性和值的键值对集合。 |

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
5. const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function heifsMetadataSetProperties(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
15. if (metaData != undefined && metaData.heifsMetadata != undefined) {
16. let setkey: Record<string, string | null> = {
17. "HeifsDelayTime": "200",
18. };
19. await metaData.heifsMetadata.setProperties(setkey).then(async () => {
20. console.info('Set properties success.');
21. }).catch((error: BusinessError) => {
22. console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
23. })
24. } else {
25. console.error('metadata is null. ');
26. }
27. }
```

## getAllProperties

PhonePC/2in1TabletTVWearable

getAllProperties(): Promise<Record<string, string | null>>

获取图片中所有元数据的属性的值。使用Promise异步回调。

要查询的属性的具体信息请参考[HeifsPropertyKey](arkts-apis-image-e.md#heifspropertykey23)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, string | null>> | Promise对象，返回元数据拥有的所有属性的值。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. function getFileFd(context: Context): number | undefined {
5. const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function heifsMetadataGetAllProperties(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
15. if (metaData != undefined && metaData.heifsMetadata != undefined) {
16. await metaData.heifsMetadata.getAllProperties().then((data) => {
17. const count = Object.keys(data).length;
18. console.info('Metadata have ', count, ' properties');
19. console.info(`Get metadata all properties: ${data}`);
20. }).catch((error: BusinessError) => {
21. console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
22. });
23. } else {
24. console.error('Metadata is null.');
25. }
26. }
```

## clone

PhonePC/2in1TabletTVWearable

clone(): Promise<HeifsMetadata>

对Heifs元数据进行克隆。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HeifsMetadata](arkts-apis-image-heifsmetadata.md)> | Promise对象，成功返回Heifs元数据实例。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. function getFileFd(context: Context): number | undefined {
5. const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
6. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
7. const fd: number = file?.fd;
8. return fd;
9. }

11. async function heifsMetadataClone(context: Context) {
12. let fd = getFileFd(context);
13. let imageSource = image.createImageSource(fd);
14. let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
15. if (metaData != undefined && metaData.heifsMetadata != undefined) {
16. let new_metadata = await metaData.heifsMetadata.clone();
17. new_metadata.getProperties(["HeifsDelayTime"]).then((data1) => {
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
4. const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
5. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
6. const fd: number = file?.fd;
7. return fd;
8. }

10. async function heifsMetadataGetBlob(context: Context) {
11. let fd = getFileFd(context);
12. let imageSource = image.createImageSource(fd);
13. let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
14. if (metaData != undefined && metaData.heifsMetadata != undefined) {
15. let blob = await metaData.heifsMetadata.getBlob();
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
4. const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
5. const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
6. const fd: number = file?.fd;
7. return fd;
8. }

10. async function heifsMetadataSetBlob(context: Context) {
11. let fd = getFileFd(context);
12. let imageSource = image.createImageSource(fd);
13. let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
14. if (metaData != undefined && metaData.heifsMetadata != undefined) {
15. let blob = await metaData.heifsMetadata.getBlob();
16. if (blob != undefined) {
17. console.info("get blob success");
18. metaData.heifsMetadata.setBlob(blob);
19. }
20. let new_blob = metaData.heifsMetadata.getBlob();
21. if (new_blob != undefined) {
22. console.info("new_blob is not undefined");
23. }
24. }
25. }
```
