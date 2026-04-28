---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker
title: Interface (ImagePacker)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (ImagePacker)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2ac13952eebcd050b659ab35af1c0755e58a0b3484c611dcef43b6ab0489f85e
---

ImagePacker类，用于图片压缩和编码。

在调用ImagePacker的方法前，需要先通过[image.createImagePacker](arkts-apis-image-f.md#imagecreateimagepacker)构建一个ImagePacker实例。

编码期间，请避免修改或释放作为输入的ImageSource/PixelMap/Picture对象，以免出现crash或其他未定义行为。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](arkts-apis-image-imagepacker.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

当前支持的格式有：jpeg、webp、png、heic12+、gif18+（不同硬件设备支持情况不同，可通过ImagePacker的supportedFormats属性查看）。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedFormats | Array<string> | 是 | 否 | 图片编码支持的格式，包括：jpeg、webp、png、heic12+、gif18+（不同硬件设备支持情况不同）。 |

## packToData13+

PhonePC/2in1TabletTVWearable

packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>

图片压缩或重新编码。使用Promise异步回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-apis-image-imagesource.md) | 是 | 编码的ImageSource。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回压缩或编码后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function PackToData(context : Context) {
4. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
5. let filePath: string = context.filesDir + "/test.jpg";
6. const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
7. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
8. const imagePackerObj: image.ImagePacker = image.createImagePacker();
9. imagePackerObj.packToData(imageSourceObj, packOpts)
10. .then((data: ArrayBuffer) => {
11. console.info('Succeeded in packing the image.');
12. }).catch((error: BusinessError) => {
13. console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
14. })
15. }
```

## packToData13+

PhonePC/2in1TabletTVWearable

packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>

图片压缩或重新编码。使用Promise异步回调。

注意

接口如果返回401错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 编码的PixelMap源。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回压缩或编码后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function PackToData() {
4. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
6. image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
7. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
8. const imagePackerObj: image.ImagePacker = image.createImagePacker();
9. imagePackerObj.packToData(pixelMap, packOpts)
10. .then((data: ArrayBuffer) => {
11. console.info('Succeeded in packing the image.');
12. }).catch((error: BusinessError) => {
13. console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
14. })
15. }).catch((error: BusinessError) => {
16. console.error(`Failed to create PixelMap.code ${error.code},message is ${error.message}`);
17. })
18. }
```

## packing13+

PhonePC/2in1TabletTVWearable

packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>

将图像压缩或重新编码。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| picture | [Picture](arkts-apis-image-picture.md) | 是 | 编码的Picture对象。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回压缩或编码后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Packing(context: Context) {
4. const resourceMgr = context.resourceManager;
5. const rawFile = await resourceMgr.getRawFileContent("test.jpg");
6. let ops: image.SourceOptions = {
7. sourceDensity: 98,
8. }
9. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
10. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
11. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
12. const imagePackerObj: image.ImagePacker = image.createImagePacker();
13. let funcName = "Packing";
14. if (imagePackerObj != null) {
15. let opts: image.PackingOption = {
16. format: "image/jpeg",
17. quality: 98,
18. desiredDynamicRange: image.PackingDynamicRange.AUTO,
19. needsPackProperties: true};
20. await imagePackerObj.packing(pictureObj, opts).then((data: ArrayBuffer) => {
21. console.info(funcName, 'Succeeded in packing the image.'+ data);
22. }).catch((error: BusinessError) => {
23. console.error(funcName, `Failed to pack the image.code ${error.code},message is ${error.message}`);
24. });
25. }
26. }
```

## packToDataFromPixelmapSequence18+

PhonePC/2in1TabletTVWearable

packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>

将多个PixelMap编码成GIF数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmapSequence | Array<[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 待编码的PixelMap序列。 |
| options | [PackingOptionsForSequence](arkts-apis-image-i.md#packingoptionsforsequence18) | 是 | 动图编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回编码后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Failed to encode image. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function PackToDataFromPixelmapSequence(context : Context) {
4. const resourceMgr = context.resourceManager;
5. // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
6. const fileData = await resourceMgr.getRawFileContent('moving_test.gif');
7. const color = fileData.buffer as ArrayBuffer;
8. let imageSource = image.createImageSource(color);
9. let pixelMapList = await imageSource.createPixelMapList();
10. let ops: image.PackingOptionsForSequence = {
11. frameCount: 3,  // 指定GIF编码中的帧数为3。
12. delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
13. disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
14. loopCount: 0 // 指定GIF编码中循环次数为无限循环。
15. };
16. let packer = image.createImagePacker();
17. packer.packToDataFromPixelmapSequence(pixelMapList, ops)
18. .then((data: ArrayBuffer) => {
19. console.info('Succeeded in packing.');
20. }).catch((error: BusinessError) => {
21. console.error('Failed to packing.');
22. })
23. }
```

## release

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放图片编码实例。使用callback异步回调。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当释放图片编码实例成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release() {
4. const imagePackerObj: image.ImagePacker = image.createImagePacker();
5. imagePackerObj.release((err: BusinessError)=>{
6. if (err) {
7. console.error(`Failed to release image packaging.code ${err.code},message is ${err.message}`);
8. } else {
9. console.info('Succeeded in releasing image packaging.');
10. }
11. })
12. }
```

## release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放图片编码实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release() {
4. const imagePackerObj: image.ImagePacker = image.createImagePacker();
5. imagePackerObj.release().then(() => {
6. console.info('Succeeded in releasing image packaging.');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to release image packaging.code ${error.code},message is ${error.message}`);
9. })
10. }
```

## packToFile11+

PhonePC/2in1TabletTVWearable

packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void

指定编码参数，将ImageSource直接编码进文件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-apis-image-imagesource.md) | 是 | 编码的ImageSource。 |
| fd | number | 是 | 文件描述符。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当编码进文件成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. async function PackToFile(context : Context) {
5. // 此处'test.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
6. const path: string = context.filesDir + "/test.png";
7. const imageSourceObj: image.ImageSource = image.createImageSource(path);
8. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
9. const filePath: string = context.filesDir + "/image_source.jpg";
10. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
11. const imagePackerObj: image.ImagePacker = image.createImagePacker();
12. imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts, (err: BusinessError) => {
13. if (err) {
14. console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
15. } else {
16. console.info('Succeeded in packing the image to file.');
17. }
18. })
19. }
```

## packToFile11+

PhonePC/2in1TabletTVWearable

packToFile (source: ImageSource, fd: number, options: PackingOption): Promise<void>

指定编码参数，将ImageSource直接编码进文件。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-apis-image-imagesource.md) | 是 | 编码的ImageSource。 |
| fd | number | 是 | 文件描述符。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. async function PackToFile(context : Context) {
5. // 此处'test.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
6. const path: string = context.filesDir + "/test.png";
7. const imageSourceObj: image.ImageSource = image.createImageSource(path);
8. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
9. const filePath: string = context.filesDir + "/image_source.jpg";
10. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
11. const imagePackerObj: image.ImagePacker = image.createImagePacker();
12. imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts).then(() => {
13. console.info('Succeeded in packing the image to file.');
14. }).catch((error: BusinessError) => {
15. console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
16. })
17. }
```

## packToFile11+

PhonePC/2in1TabletTVWearable

packToFile (source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void

指定编码参数，将PixelMap直接编码进文件。使用callback异步回调。

注意

接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 编码的PixelMap资源。 |
| fd | number | 是 | 文件描述符。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当编码图片进文件成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. async function PackToFile(context : Context) {
5. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
6. let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
7. const path: string = context.filesDir + "/pixel_map.jpg";
8. image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
9. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
10. let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
11. const imagePackerObj: image.ImagePacker = image.createImagePacker();
12. imagePackerObj.packToFile(pixelmap, file.fd, packOpts, (err: BusinessError) => {
13. if (err) {
14. console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
15. } else {
16. console.info('Succeeded in packing the image to file.');
17. }
18. })
19. })
20. }
```

## packToFile11+

PhonePC/2in1TabletTVWearable

packToFile (source: PixelMap, fd: number, options: PackingOption): Promise<void>

指定编码参数，将PixelMap直接编码进文件。使用Promise异步回调。

注意

接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 编码的PixelMap资源。 |
| fd | number | 是 | 文件描述符。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. async function PackToFile(context : Context) {
5. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
6. let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
7. const path: string = context.filesDir + "/pixel_map.jpg";
8. image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
9. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
10. let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
11. const imagePackerObj: image.ImagePacker = image.createImagePacker();
12. imagePackerObj.packToFile(pixelmap, file.fd, packOpts)
13. .then(() => {
14. console.info('Succeeded in packing the image to file.');
15. }).catch((error: BusinessError) => {
16. console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
17. })
18. })
19. }
```

## packToFile13+

PhonePC/2in1TabletTVWearable

packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>

指定编码参数，将Picture直接编码进文件。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| picture | [Picture](arkts-apis-image-picture.md) | 是 | 编码的Picture资源。 |
| fd | number | 是 | 文件描述符。 |
| options | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. async function PackToFile(context: Context) {
5. const resourceMgr = context.resourceManager;
6. const rawFile = await resourceMgr.getRawFileContent("test.jpg");
7. let ops: image.SourceOptions = {
8. sourceDensity: 98,
9. }
10. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
11. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
12. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);

14. let funcName = "PackToFile";
15. const imagePackerObj: image.ImagePacker = image.createImagePacker();
16. if (imagePackerObj != null) {
17. const filePath: string = context.filesDir + "/test.jpg";
18. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
19. let packOpts: image.PackingOption = {
20. format: "image/jpeg",
21. quality: 98,
22. desiredDynamicRange: image.PackingDynamicRange.AUTO,
23. needsPackProperties: true};
24. await imagePackerObj.packToFile(pictureObj, file.fd, packOpts).then(() => {
25. console.info(funcName, 'Succeeded in packing the image to file.');
26. }).catch((error: BusinessError) => {
27. console.error(funcName, `Failed to pack the image to file.code ${error.code},message is ${error.message}`);
28. });
29. }
30. }
```

## packToFileFromPixelmapSequence18+

PhonePC/2in1TabletTVWearable

packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>

指定编码参数，将多个PixelMap编码成GIF文件。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmapSequence | Array<[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 待编码的PixelMap序列。 |
| fd | number | 是 | 文件描述符。 |
| options | [PackingOptionsForSequence](arkts-apis-image-i.md#packingoptionsforsequence18) | 是 | 动图编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Failed to encode image. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. async function PackToFile(context : Context) {
5. const resourceMgr = context.resourceManager;
6. // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
7. const fileData = await resourceMgr.getRawFileContent('moving_test.gif');
8. const color = fileData.buffer;
9. let imageSource = image.createImageSource(color);
10. let pixelMapList = await imageSource.createPixelMapList();
11. let path: string = context.cacheDir + '/result.gif';
12. let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
13. let ops: image.PackingOptionsForSequence = {
14. frameCount: 3,  // 指定GIF编码中的帧数为3。
15. delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
16. disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
17. loopCount: 0 // 指定GIF编码中循环次数为无限循环。
18. };
19. let packer = image.createImagePacker();
20. packer.packToFileFromPixelmapSequence(pixelMapList, file.fd, ops)
21. .then(() => {
22. console.info('Succeeded in packToFileMultiFrames.');
23. }).catch((error: BusinessError) => {
24. console.error('Failed to packToFileMultiFrames.');
25. })
26. }
```

## packing(deprecated)

PhonePC/2in1TabletTVWearable

packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void

图片压缩或重新编码。使用callback异步回调。

说明

从API version 6开始支持，从API version 13开始废弃，建议使用[packToData](arkts-apis-image-imagepacker.md#packtodata13)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-apis-image-imagesource.md) | 是 | 编码的ImageSource。 |
| option | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |
| callback | AsyncCallback<ArrayBuffer> | 是 | 回调函数，当图片编码成功，err为undefined，data为获取到的压缩或编码数据；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Packing(context : Context) {
4. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
5. let filePath: string = context.filesDir + "/test.jpg";
6. const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
7. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
8. const imagePackerObj: image.ImagePacker = image.createImagePacker();
9. imagePackerObj.packing(imageSourceObj, packOpts, (err: BusinessError, data: ArrayBuffer) => {
10. if (err) {
11. console.error(`Failed to pack the image.code ${err.code},message is ${err.message}`);
12. } else {
13. console.info('Succeeded in packing the image.');
14. }
15. })
16. }
```

## packing(deprecated)

PhonePC/2in1TabletTVWearable

packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>

图片压缩或重新编码。使用Promise异步回调。

说明

从API version 6开始支持，从API version 13开始废弃，建议使用[packToData](arkts-apis-image-imagepacker.md#packtodata13)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-apis-image-imagesource.md) | 是 | 编码的ImageSource。 |
| option | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回压缩或编码后的数据。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Packing(context : Context) {
4. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
5. let filePath: string = context.filesDir + "/test.jpg";
6. const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
7. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
8. const imagePackerObj: image.ImagePacker = image.createImagePacker();
9. imagePackerObj.packing(imageSourceObj, packOpts)
10. .then((data: ArrayBuffer) => {
11. console.info('Succeeded in packing the image.');
12. }).catch((error: BusinessError) => {
13. console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
14. })
15. }
```

## packing(deprecated)

PhonePC/2in1TabletTVWearable

packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void

图片压缩或重新编码。使用callback异步回调。

说明

从API version 8开始支持，从API version 13开始废弃，建议使用[packToData](arkts-apis-image-imagepacker.md#packtodata13)代替。

注意

接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 编码的PixelMap资源。 |
| option | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |
| callback | AsyncCallback<ArrayBuffer> | 是 | 回调函数，当图片编码成功，err为undefined，data为获取到的压缩或编码数据；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Packing() {
4. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
6. image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
7. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
8. const imagePackerObj: image.ImagePacker = image.createImagePacker();
9. imagePackerObj.packing(pixelMap, packOpts, (err: BusinessError, data: ArrayBuffer) => {
10. if (err) {
11. console.error(`Failed to pack the image.code ${err.code},message is ${err.message}`);
12. } else {
13. console.info('Succeeded in packing the image.');
14. }
15. })
16. }).catch((error: BusinessError) => {
17. console.error(`Failed to create the PixelMap.code ${error.code},message is ${error.message}`);
18. })
19. }
```

## packing(deprecated)

PhonePC/2in1TabletTVWearable

packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>

图片压缩或重新编码。使用Promise异步回调。

说明

从API version 8开始支持，从API version 13开始废弃，建议使用[packToData](arkts-apis-image-imagepacker.md#packtodata13)代替。

注意

接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 编码的PixelMap源。 |
| option | [PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置编码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回压缩或编码后的数据。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Packing() {
4. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
6. image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
7. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
8. const imagePackerObj: image.ImagePacker = image.createImagePacker();
9. imagePackerObj.packing(pixelMap, packOpts)
10. .then((data: ArrayBuffer) => {
11. console.info('Succeeded in packing the image.');
12. }).catch((error: BusinessError) => {
13. console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
14. })
15. }).catch((error: BusinessError) => {
16. console.error(`Failed to create PixelMap.code ${error.code},message is ${error.message}`);
17. })
18. }
```
