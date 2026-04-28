---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap
title: Interface (PixelMap)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (PixelMap)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:12+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:27b942d12fe97a398fa014729d7081a7c4010c65c1ea5c6666957737606c253c
---

图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[image.createPixelMap](arkts-apis-image-f.md#imagecreatepixelmap8)创建一个PixelMap实例。目前PixelMap序列化大小最大128MB，超过会送显失败。大小计算方式为（宽\*高\*[每像素占用字节数](arkts-apis-image-e.md#pixelmapformat7)）。

从API version 11开始，PixelMap支持通过[Worker](js-apis-worker.md)跨线程调用。当PixelMap通过[Worker](js-apis-worker.md)跨线程后，原线程的PixelMap的所有接口均不能调用，否则将报错501 服务器不具备完成请求的功能。

在调用PixelMap的方法前，可以通过[image.createPixelMap](arkts-apis-image-f.md#imagecreatepixelmap8)传入像素数据创建一个PixelMap对象，也可以通过[ImageSource](arkts-apis-image-imagesource.md)进行图片解码创建PixelMap对象。

开发元服务请通过[ImageSource](arkts-apis-image-imagesource.md)构建PixelMap对象。

图片使用的内存往往较大，在PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 7开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isEditable7+ | boolean | 是 | 否 | 图像像素是否可被编辑。true表示可被编辑，false表示不可被编辑。为false时，图像的渲染和传输性能更好。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。 |
| isStrideAlignment11+ | boolean | 是 | 否 | 图像的行数据是否已进行内存对齐。true表示已进行内存对齐，每行数据的末尾可能有空白字节填充以满足对齐要求；false表示未进行内存对齐，每行数据紧密排列，末尾无空白字节填充。 |

## readPixelsToBuffer7+

PhonePC/2in1TabletTVWearable

readPixelsToBuffer(dst: ArrayBuffer): Promise<void>

按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dst | ArrayBuffer | 是 | 缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
4. const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. if (pixelMap != undefined) {
6. pixelMap.readPixelsToBuffer(readBuffer).then(() => {
7. console.info('Succeeded in reading image pixel data.'); // 符合条件则进入。
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`);// 不符合条件则进入。
10. })
11. }
12. }
```

## readPixelsToBuffer7+

PhonePC/2in1TabletTVWearable

readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void

按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dst | ArrayBuffer | 是 | 缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)接口获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当读取像素数据到ArrayBuffer成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
4. const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. if (pixelMap != undefined) {
6. pixelMap.readPixelsToBuffer(readBuffer, (error: BusinessError, res: void) => {
7. if(error) {
8. console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`);// 不符合条件则进入。
9. return;
10. } else {
11. console.info('Succeeded in reading image pixel data.');  // 符合条件则进入。
12. }
13. })
14. }
15. }
```

## readPixelsToBufferSync12+

PhonePC/2in1TabletTVWearable

readPixelsToBufferSync(dst: ArrayBuffer): void

按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中，同步返回结果。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dst | ArrayBuffer | 是 | 缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function ReadPixelsToBufferSync(pixelMap : image.PixelMap) {
2. const bufferSize = pixelMap.getPixelBytesNumber();
3. const readBuffer = new ArrayBuffer(bufferSize);
4. if (pixelMap != undefined) {
5. pixelMap.readPixelsToBufferSync(readBuffer);
6. }
7. }
```

## readPixels7+

PhonePC/2in1TabletTVWearable

readPixels(area: PositionArea): Promise<void>

固定按照BGRA\_8888格式，读取PixelMap指定区域内的图像像素数据，并写入[PositionArea](arkts-apis-image-i.md#positionarea7).pixels缓冲区中，该区域由[PositionArea](arkts-apis-image-i.md#positionarea7).region指定。使用Promise异步回调。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width \* height}）\* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width \* height}）\* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域大小，根据区域读取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
4. const area: image.PositionArea = {
5. pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
6. offset: 0,
7. stride: 8,
8. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
9. };
10. if (pixelMap != undefined) {
11. pixelMap.readPixels(area).then(() => {
12. console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
13. console.info('RGBA data is ', new Uint8Array(area.pixels));
14. }).catch((error: BusinessError) => {
15. console.error("Failed to read the image data in the area. code is ", error);// 不符合条件则进入。
16. })
17. }
18. }

20. async function ReadPixelsYUV(pixelMap : image.PixelMap) {
21. const area: image.PositionArea = {
22. pixels: new ArrayBuffer(6),  // 6为需要创建的像素buffer大小，取值为：height * width *1.5。
23. offset: 0,
24. stride: 8,
25. region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
26. };
27. if (pixelMap != undefined) {
28. pixelMap.readPixels(area).then(() => {
29. console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
30. console.info('YUV data is ', new Uint8Array(area.pixels));
31. }).catch((error: BusinessError) => {
32. console.error("Failed to read the image data in the area. code is ", error);// 不符合条件则进入。
33. })
34. }
35. }
```

## readPixels7+

PhonePC/2in1TabletTVWearable

readPixels(area: PositionArea, callback: AsyncCallback<void>): void

固定按照BGRA\_8888格式，读取PixelMap指定区域内的图像像素数据，并写入[PositionArea](arkts-apis-image-i.md#positionarea7).pixels缓冲区中，该区域由[PositionArea](arkts-apis-image-i.md#positionarea7).region指定，使用callback形式返回。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width \* height}）\* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width \* height}）\* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域大小，根据区域读取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当读取区域内的图片数据成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
4. const area: image.PositionArea = {
5. pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
6. offset: 0,
7. stride: 8,
8. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
9. };
10. if (pixelMap != undefined) {
11. pixelMap.readPixels(area, (error: BusinessError) => {
12. if (error) {
13. console.error("Failed to read pixelmap from the specified area. code is ", error);
14. return;
15. } else {
16. console.info('Succeeded in reading pixelmap from the specified area.');
17. console.info('RGBA data is ', new Uint8Array(area.pixels));
18. }
19. })
20. }
21. }

23. async function ReadPixelsYUV(pixelMap : image.PixelMap) {
24. const area: image.PositionArea = {
25. pixels: new ArrayBuffer(6), // 6为需要创建的像素buffer大小，取值为：height * width *1.5。
26. offset: 0,
27. stride: 8,
28. region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
29. };
30. if (pixelMap != undefined) {
31. pixelMap.readPixels(area, (error: BusinessError) => {
32. if (error) {
33. console.error("Failed to read pixelmap from the specified area. code is ", error);
34. return;
35. } else {
36. console.info('Succeeded in reading pixelmap from the specified area.');
37. console.info('YUV data is ', new Uint8Array(area.pixels));
38. }
39. })
40. }
41. }
```

## readPixelsSync12+

PhonePC/2in1TabletTVWearable

readPixelsSync(area: PositionArea): void

固定按照BGRA\_8888格式，读取PixelMap指定区域内的图像像素数据，并写入[PositionArea](arkts-apis-image-i.md#positionarea7).pixels缓冲区中，该区域由[PositionArea](arkts-apis-image-i.md#positionarea7).region指定，同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域大小，根据区域读取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function ReadPixelsSync(pixelMap : image.PixelMap) {
2. const area : image.PositionArea = {
3. pixels: new ArrayBuffer(8),
4. offset: 0,
5. stride: 8,
6. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
7. };
8. if (pixelMap != undefined) {
9. pixelMap.readPixelsSync(area);
10. }
11. }
```

## writePixels7+

PhonePC/2in1TabletTVWearable

writePixels(area: PositionArea): Promise<void>

固定按照BGRA\_8888格式，读取[PositionArea](arkts-apis-image-i.md#positionarea7).pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由[PositionArea](arkts-apis-image-i.md#positionarea7).region指定。使用Promise异步回调。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width \* height}）\* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width \* height}）\* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域，根据区域写入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function WritePixelsRGBA(pixelMap:image.PixelMap) {
4. const area: image.PositionArea = {
5. pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
6. offset: 0,
7. stride: 8,
8. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
9. };
10. let bufferArr: Uint8Array = new Uint8Array(area.pixels);
11. for (let i = 0; i < bufferArr.length; i++) {
12. bufferArr[i] = i + 1;
13. }
14. if (pixelMap != undefined) {
15. pixelMap.writePixels(area).then(() => {
16. console.info('Succeeded in writing pixelmap into the specified area.');
17. }).catch((error: BusinessError) => {
18. console.error("Failed to write pixelmap into the specified area. code is ", error);
19. })
20. }
21. }

23. async function WritePixelsYUV(pixelMap:image.PixelMap) {
24. const area: image.PositionArea = {
25. pixels: new ArrayBuffer(6), // 6为需要创建的像素buffer大小，取值为：height * width *1.5。
26. offset: 0,
27. stride: 8, // PixelMap为yuv格式时，writePixels函数不使用该变量。
28. region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
29. };
30. let bufferArr: Uint8Array = new Uint8Array(area.pixels);
31. for (let i = 0; i < bufferArr.length; i++) {
32. bufferArr[i] = i + 1;
33. }
34. if (pixelMap != undefined) {
35. pixelMap.writePixels(area).then(() => {
36. console.info('Succeeded in writing pixelmap into the specified area.');
37. }).catch((error: BusinessError) => {
38. console.error("Failed to write pixelmap into the specified area. code is ", error);
39. })
40. }
41. }
```

## writePixels7+

PhonePC/2in1TabletTVWearable

writePixels(area: PositionArea, callback: AsyncCallback<void>): void

固定按照BGRA\_8888格式，读取[PositionArea](arkts-apis-image-i.md#positionarea7).pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由[PositionArea](arkts-apis-image-i.md#positionarea7).region指定，使用callback形式返回。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width \* height}）\* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width \* height}）\* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域，根据区域写入。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当写入成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function WritePixelsRGBA(pixelMap:image.PixelMap) {
4. const area: image.PositionArea = { pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
5. offset: 0,
6. stride: 8,
7. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
8. };
9. let bufferArr: Uint8Array = new Uint8Array(area.pixels);
10. for (let i = 0; i < bufferArr.length; i++) {
11. bufferArr[i] = i + 1;
12. }
13. if (pixelMap != undefined) {
14. pixelMap.writePixels(area, (error : BusinessError) => {
15. if (error) {
16. console.error("Failed to write pixelmap into the specified area. code is ", error);
17. return;
18. } else {
19. console.info('Succeeded in writing pixelmap into the specified area.');
20. }
21. })
22. }
23. }

25. async function WritePixelsYUV(pixelMap:image.PixelMap) {
26. const area: image.PositionArea = { pixels: new ArrayBuffer(6), // 6为需要创建的像素buffer大小，取值为：height * width * 1.5。
27. offset: 0,
28. stride: 8, // PixelMap为yuv格式时，writePixels函数不使用该变量。
29. region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
30. };
31. let bufferArr: Uint8Array = new Uint8Array(area.pixels);
32. for (let i = 0; i < bufferArr.length; i++) {
33. bufferArr[i] = i + 1;
34. }
35. if (pixelMap != undefined) {
36. pixelMap.writePixels(area, (error : BusinessError) => {
37. if (error) {
38. console.error("Failed to write pixelmap into the specified area. code is ", error);
39. return;
40. } else {
41. console.info('Succeeded in writing pixelmap into the specified area.');
42. }
43. })
44. }
45. }
```

## writePixelsSync12+

PhonePC/2in1TabletTVWearable

writePixelsSync(area: PositionArea): void

固定按照BGRA\_8888格式，读取[PositionArea](arkts-apis-image-i.md#positionarea7).pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由[PositionArea](arkts-apis-image-i.md#positionarea7).region指定，同步返回结果。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域，根据区域写入。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function WritePixelsSync(pixelMap:image.PixelMap) {
2. const area: image.PositionArea = {
3. pixels: new ArrayBuffer(8),
4. offset: 0,
5. stride: 8,
6. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
7. };
8. let bufferArr: Uint8Array = new Uint8Array(area.pixels);
9. for (let i = 0; i < bufferArr.length; i++) {
10. bufferArr[i] = i + 1;
11. }
12. if (pixelMap != undefined) {
13. pixelMap.writePixelsSync(area);
14. }
15. }
```

## writeBufferToPixels7+

PhonePC/2in1TabletTVWearable

writeBufferToPixels(src: ArrayBuffer): Promise<void>

按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | ArrayBuffer | 是 | 缓冲区，函数执行时会将该缓冲区中的图像像素数据写入到PixelMap。缓冲区大小由[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function WriteBufferToPixels(pixelMap:image.PixelMap) {
4. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let bufferArr: Uint8Array = new Uint8Array(color);
6. for (let i = 0; i < bufferArr.length; i++) {
7. bufferArr[i] = i + 1;
8. }
9. if (pixelMap != undefined) {
10. pixelMap.writeBufferToPixels(color).then(() => {
11. console.info("Succeeded in writing data from a buffer to a PixelMap.");
12. }).catch((error: BusinessError) => {
13. console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
14. })
15. }
16. }
```

## writeBufferToPixels7+

PhonePC/2in1TabletTVWearable

writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void

按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | ArrayBuffer | 是 | 缓冲区，函数执行时会将该缓冲区中的图像像素数据写入到PixelMap。缓冲区大小由[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)接口获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当缓冲区中的图像像素数据写入PixelMap成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function WriteBufferToPixels(pixelMap:image.PixelMap) {
4. const color: ArrayBuffer = new ArrayBuffer(96);  // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let bufferArr: Uint8Array = new Uint8Array(color);
6. for (let i = 0; i < bufferArr.length; i++) {
7. bufferArr[i] = i + 1;
8. }
9. if (pixelMap != undefined) {
10. pixelMap.writeBufferToPixels(color, (error: BusinessError) => {
11. if (error) {
12. console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
13. return;
14. } else {
15. console.info("Succeeded in writing data from a buffer to a PixelMap.");
16. }
17. })
18. }
19. }
```

## writeBufferToPixelsSync12+

PhonePC/2in1TabletTVWearable

writeBufferToPixelsSync(src: ArrayBuffer): void

按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap，同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | ArrayBuffer | 是 | 缓冲区，函数执行时会将该缓冲区中的图像像素数据写入到PixelMap。缓冲区大小由[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function WriteBufferToPixelsSync(pixelMap:image.PixelMap) {
2. const color : ArrayBuffer = new ArrayBuffer(96);  // 96为需要创建的像素buffer大小，取值为：height * width *4。
3. let bufferArr : Uint8Array = new Uint8Array(color);
4. for (let i = 0; i < bufferArr.length; i++) {
5. bufferArr[i] = i + 1;
6. }
7. if (pixelMap != undefined) {
8. pixelMap.writeBufferToPixelsSync(color);
9. }
10. }
```

## getImageInfo7+

PhonePC/2in1TabletTVWearable

getImageInfo(): Promise<ImageInfo>

获取图像像素信息。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ImageInfo](arkts-apis-image-i.md#imageinfo)> | Promise对象，返回图像像素信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function GetImageInfo(pixelMap: image.PixelMap) {
4. if (pixelMap != undefined) {
5. pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
6. if (imageInfo != undefined) {
7. console.info(`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}`);
8. }
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
11. })
12. }
13. }
```

## getImageInfo7+

PhonePC/2in1TabletTVWearable

getImageInfo(callback: AsyncCallback<ImageInfo>): void

获取图像像素信息，使用callback形式返回获取的图像像素信息。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ImageInfo](arkts-apis-image-i.md#imageinfo)> | 是 | 回调函数。当获取图像像素信息成功，err为undefined，data为获取到的图像像素信息；否则为错误对象。 |

**示例:**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function GetImageInfoSync(pixelMap : image.PixelMap){
4. if (pixelMap != undefined) {
5. pixelMap.getImageInfo((error: BusinessError, imageInfo: image.ImageInfo) => {
6. if (error) {
7. console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
8. return;
9. } else {
10. console.info(`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}`);
11. }
12. })
13. }
14. }
```

## getImageInfoSync12+

PhonePC/2in1TabletTVWearable

getImageInfoSync(): ImageInfo

以同步方法获取图像像素信息。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageInfo](arkts-apis-image-i.md#imageinfo) | 图像像素信息。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 501 | Resource Unavailable |

**示例：**

```
1. function GetImageInfoSync(pixelMap:image.PixelMap) {
2. if (pixelMap != undefined) {
3. let imageInfo : image.ImageInfo = pixelMap.getImageInfoSync();
4. return imageInfo;
5. }
6. return undefined;
7. }
```

## getBytesNumberPerRow7+

PhonePC/2in1TabletTVWearable

getBytesNumberPerRow(): number

获取图像像素每行字节数。单位：字节。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图像像素的行字节数。 |

**示例：**

```
1. function GetBytesNumberPerRow(pixelMap: image.PixelMap) {
2. let rowCount: number = pixelMap.getBytesNumberPerRow();
3. }
```

## getPixelBytesNumber7+

PhonePC/2in1TabletTVWearable

getPixelBytesNumber(): number

获取图像像素的总字节数。单位：字节。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图像像素的总字节数。 |

**示例：**

```
1. function GetPixelBytesNumber(pixelMap: image.PixelMap) {
2. let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
3. }
```

## getDensity9+

PhonePC/2in1TabletTVWearable

getDensity():number

获取当前图像像素的密度。单位：ppi（像素/英寸）。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图像像素的密度，单位为ppi。 |

**示例：**

```
1. function GetDensity(pixelMap: image.PixelMap) {
2. let getDensity: number = pixelMap.getDensity();
3. }
```

## opacity9+

PhonePC/2in1TabletTVWearable

opacity(rate: number, callback: AsyncCallback<void>): void

通过设置透明比率来让PixelMap达到对应的透明效果，yuv图片不支持设置透明度，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | number | 是 | 透明比率的值，取值范围是(0,1]。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置透明比率成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Opacity(pixelMap:image.PixelMap) {
4. let rate: number = 0.5;
5. if (pixelMap != undefined) {
6. pixelMap.opacity(rate, (err: BusinessError) => {
7. if (err) {
8. console.error(`Failed to set opacity. code is ${err.code}, message is ${err.message}`);
9. return;
10. } else {
11. console.info("Succeeded in setting opacity.");
12. }
13. })
14. }
15. }
```

## opacity9+

PhonePC/2in1TabletTVWearable

opacity(rate: number): Promise<void>

通过设置透明比率来让PixelMap达到对应的透明效果，yuv图片不支持设置透明度。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | number | 是 | 透明比率的值，取值范围是(0,1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Opacity(pixelMap:image.PixelMap) {
4. let rate: number = 0.5;
5. if (pixelMap != undefined) {
6. pixelMap.opacity(rate).then(() => {
7. console.info('Succeeded in setting opacity.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set opacity. code is ${err.code}, message is ${err.message}`);
10. })
11. }
12. }
```

## opacitySync12+

PhonePC/2in1TabletTVWearable

opacitySync(rate: number): void

设置PixelMap的透明比率，yuv图片不支持设置透明度，初始化PixelMap并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | number | 是 | 透明比率的值，取值范围是(0,1]。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function OpacitySync(pixelMap:image.PixelMap) {
2. let rate : number = 0.5;
3. if (pixelMap != undefined) {
4. pixelMap.opacitySync(rate);
5. }
6. }
```

## createAlphaPixelmap9+

PhonePC/2in1TabletTVWearable

createAlphaPixelmap(): Promise<PixelMap>

根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的PixelMap，生成的新PixelMap不可编辑，可用于阴影效果。YUV格式不支持此接口。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
4. if (pixelMap != undefined) {
5. pixelMap.createAlphaPixelmap().then((alphaPixelMap: image.PixelMap) => {
6. console.info('Succeeded in creating alpha pixelmap.');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to create alpha pixelmap. code is ${error.code}, message is ${error.message}`);
9. })
10. }
11. }
```

## createAlphaPixelmap9+

PhonePC/2in1TabletTVWearable

createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void

根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的PixelMap，生成的新PixelMap不可编辑，可用于阴影效果。YUV格式不支持此接口。使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数，当创建PixelMap成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
4. if (pixelMap != undefined) {
5. pixelMap.createAlphaPixelmap((err: BusinessError, alphaPixelMap: image.PixelMap) => {
6. if (alphaPixelMap == undefined) {
7. console.error(`Failed to obtain new pixel map. code is ${err.code}, message is ${err.message}`);
8. return;
9. } else {
10. console.info('Succeeded in obtaining new pixel map.');
11. }
12. })
13. }
14. }
```

## createAlphaPixelmapSync12+

PhonePC/2in1TabletTVWearable

createAlphaPixelmapSync(): PixelMap

根据Alpha通道的信息，生成一个仅包含Alpha通道信息的PixelMap，生成的新PixelMap不可编辑，可用于阴影效果。YUV格式不支持此接口。同步返回PixelMap类型的结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function CreateAlphaPixelmapSync(pixelMap:image.PixelMap) {
2. if (pixelMap != undefined) {
3. let pixelmap : image.PixelMap = pixelMap.createAlphaPixelmapSync();
4. return pixelmap;
5. }
6. return undefined;
7. }
```

## scale9+

PhonePC/2in1TabletTVWearable

scale(x: number, y: number, callback: AsyncCallback<void>): void

根据输入的宽高的缩放倍数对图片进行缩放，使用callback形式返回。

说明

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
2. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当对图片进行缩放成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Scale(pixelMap:image.PixelMap) {
4. let scaleX: number = 2.0;
5. let scaleY: number = 1.0;
6. if (pixelMap != undefined) {
7. pixelMap.scale(scaleX, scaleY, (err: BusinessError) => {
8. if (err) {
9. console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
10. return;
11. } else {
12. console.info("Succeeded in scaling pixelmap.");
13. }
14. })
15. }
16. }
```

## scale9+

PhonePC/2in1TabletTVWearable

scale(x: number, y: number): Promise<void>

根据输入的宽高的缩放倍数对图片进行缩放。使用Promise异步回调。

说明

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
2. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Scale(pixelMap:image.PixelMap) {
4. let scaleX: number = 2.0;
5. let scaleY: number = 1.0;
6. if (pixelMap != undefined) {
7. pixelMap.scale(scaleX, scaleY).then(() => {
8. console.info('Succeeded in scaling pixelmap.');
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
11. })
12. }
13. }
```

## scaleSync12+

PhonePC/2in1TabletTVWearable

scaleSync(x: number, y: number): void

根据输入的宽高的缩放倍数对图片进行缩放，同步返回结果。

说明

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
2. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function ScaleSync(pixelMap: image.PixelMap) {
2. let scaleX: number = 2.0;
3. let scaleY: number = 1.0;
4. if (pixelMap != undefined) {
5. pixelMap.scaleSync(scaleX, scaleY);
6. }
7. }
```

## scale12+

PhonePC/2in1TabletTVWearable

scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>

根据指定的缩放算法和输入的宽高的缩放倍数对图片进行缩放。使用Promise异步回调。

说明

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
2. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |
| level | [AntiAliasingLevel](arkts-apis-image-e.md#antialiasinglevel12) | 是 | 采用的缩放算法。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function ScaleSync(pixelMap:image.PixelMap) {
4. let scaleX: number = 2.0;
5. let scaleY: number = 1.0;
6. if (pixelMap != undefined) {
7. pixelMap.scale(scaleX, scaleY, image.AntiAliasingLevel.LOW).then(() => {
8. console.info('Succeeded in scaling pixelmap.');
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
11. })
12. }
13. }
```

## scaleSync12+

PhonePC/2in1TabletTVWearable

scaleSync(x: number, y: number, level: AntiAliasingLevel): void

根据指定的缩放算法和输入的宽高的缩放倍数对图片进行缩放，同步返回结果。

说明

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
2. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |
| level | [AntiAliasingLevel](arkts-apis-image-e.md#antialiasinglevel12) | 是 | 采用的缩放算法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function ScaleSync(pixelMap: image.PixelMap) {
2. let scaleX: number = 2.0;
3. let scaleY: number = 1.0;
4. if (pixelMap != undefined) {
5. pixelMap.scaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
6. }
7. }
```

## createScaledPixelMap18+

PhonePC/2in1TabletTVWearable

createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>

根据指定的缩放算法和输入的宽高的缩放倍数，创建一个新的缩放后的图片，生成的新PixelMap不可编辑。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |
| level | [AntiAliasingLevel](arkts-apis-image-e.md#antialiasinglevel12) | 否 | 采用的缩放算法，默认值为AntiAliasingLevel.NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreateScaledPixelMap(pixelMap:image.PixelMap) {
4. let scaleX: number = 2.0;
5. let scaleY: number = 1.0;
6. if (pixelMap != undefined) {
7. pixelMap.createScaledPixelMap(scaleX, scaleY, image.AntiAliasingLevel.LOW).then((scaledPixelMap: image.PixelMap) => {
8. console.info('Succeeded in creating scaledPixelMap.');
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to create scaledPixelMap. Error code is ${error.code}, error message is ${error.message}`);
11. })
12. }
13. }
```

## createScaledPixelMapSync18+

PhonePC/2in1TabletTVWearable

createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap

根据指定的缩放算法和输入的宽高的缩放倍数，创建一个新的缩放后的图片，生成的新PixelMap不可编辑。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |
| level | [AntiAliasingLevel](arkts-apis-image-e.md#antialiasinglevel12) | 否 | 采用的缩放算法，默认值为AntiAliasingLevel.NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function CreateScaledPixelMapSync(pixelMap:image.PixelMap) {
2. let scaleX: number = 2.0;
3. let scaleY: number = 1.0;
4. if (pixelMap != undefined) {
5. let scaledPixelMap = pixelMap.createScaledPixelMapSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
6. }
7. }
```

## createCroppedAndScaledPixelMap22+

PhonePC/2in1TabletTVWearable

createCroppedAndScaledPixelMap(region: Region, x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>

根据指定的裁剪区域、宽高的缩放倍数和缩放算法，创建一个新的裁剪并缩放后的图片。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-image-i.md#region8) | 是 | 裁剪的区域。取值范围不能超过图片的宽和高（单位：像素）。 |
| x | number | 是 | 宽度的缩放倍数。不能为0。 |
| y | number | 是 | 高度的缩放倍数。不能为0。 |
| level | [AntiAliasingLevel](arkts-apis-image-e.md#antialiasinglevel12) | 否 | 采用的缩放算法。默认值是AntiAliasingLevel.NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | The PixelMap has been released. |
| 7600204 | Invalid region. |
| 7600205 | Unsupported memory format or pixel format. |
| 7600301 | Memory alloc failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function DemoCreateCroppedAndScaledPixelMap(pixelMap: PixelMap) {
4. const imageInfo = pixelMap.getImageInfoSync();
5. const region: image.Region = {
6. size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
7. x: imageInfo.size.width / 4,
8. y: imageInfo.size.height / 4
9. };
10. const scaleX: number = 2.0;
11. const scaleY: number = 2.0;
12. pixelMap.createCroppedAndScaledPixelMap(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH)
13. .then((croppedAndScaled: PixelMap) => {
14. console.info('PixelMap crop and scale succeeded.');
15. })
16. .catch((error: BusinessError) => {
17. console.error(`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}`);
18. });
19. }
```

## createCroppedAndScaledPixelMapSync22+

PhonePC/2in1TabletTVWearable

createCroppedAndScaledPixelMapSync(region: Region, x: number, y: number, level?: AntiAliasingLevel): PixelMap

根据指定的裁剪区域、宽高的缩放倍数和缩放算法，创建一个新的裁剪并缩放后的图片。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-image-i.md#region8) | 是 | 裁剪的区域。取值范围不能超过图片的宽和高（单位：像素）。 |
| x | number | 是 | 宽度的缩放倍数。不能为0。 |
| y | number | 是 | 高度的缩放倍数。不能为0。 |
| level | [AntiAliasingLevel](arkts-apis-image-e.md#antialiasinglevel12) | 否 | 采用的缩放算法。默认值是AntiAliasingLevel.NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功则同步返回PixelMap对象，失败则抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | The PixelMap has been released. |
| 7600204 | Invalid region. |
| 7600205 | Unsupported memory format or pixel format. |
| 7600301 | Memory alloc failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function DemoCreateCroppedAndScaledPixelMapSync(pixelMap: PixelMap) {
4. const imageInfo = pixelMap.getImageInfoSync();
5. const region: image.Region = {
6. size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
7. x: imageInfo.size.width / 4,
8. y: imageInfo.size.height / 4
9. };
10. const scaleX: number = 2.0;
11. const scaleY: number = 2.0;
12. try {
13. const croppedAndScaled = pixelMap.createCroppedAndScaledPixelMapSync(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH);
14. } catch (e) {
15. const error = e as BusinessError;
16. console.error(`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}`);
17. }
18. }
```

## clone18+

PhonePC/2in1TabletTVWearable

clone(): Promise<PixelMap>

拷贝一份当前Pixelmap对象。使用Promise异步回调。

**系统能力：**: SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 501 | Resource unavailable. |
| 62980102 | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| 62980103 | Image YUV And ASTC types are not supported. |
| 62980104 | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Clone(pixelMap:image.PixelMap) {
4. if (pixelMap != undefined) {
5. pixelMap.clone().then((clonePixelMap: image.PixelMap) => {
6. console.info('Succeeded clone pixelmap.');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to clone pixelmap. code is ${error.code}, message is ${error.message}`);
9. })
10. }
11. }
```

## cloneSync18+

PhonePC/2in1TabletTVWearable

cloneSync(): PixelMap

拷贝一份当前Pixelmap对象, 同步返回结果。

**系统能力：**: SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 501 | Resource unavailable. |
| 62980102 | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| 62980103 | Image YUV And ASTC types are not supported. |
| 62980104 | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function CloneSync(pixelMap: image.PixelMap) {
4. if (pixelMap != undefined) {
5. try {
6. let clonedPixelMap:image.PixelMap = pixelMap.cloneSync();
7. } catch(e) {
8. let error = e as BusinessError;
9. console.error(`clone pixelmap error. code is ${error.code}, message is ${error.message}`);
10. }
11. }
12. }
```

## translate9+

PhonePC/2in1TabletTVWearable

translate(x: number, y: number, callback: AsyncCallback<void>): void

根据输入的坐标对图片进行位置变换，使用callback形式返回。

translate后的图片尺寸改变为：width+X ，height+Y，建议translate后的图片尺寸宽高不要超过屏幕的宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 区域横坐标。单位：像素。 |
| y | number | 是 | 区域纵坐标。单位：像素。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当对图片进行位置变换成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Translate(pixelMap:image.PixelMap) {
4. let translateX: number = 50.0;
5. let translateY: number = 10.0;
6. if (pixelMap != undefined) {
7. pixelMap.translate(translateX, translateY, (err: BusinessError) => {
8. if (err) {
9. console.error(`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}`);
10. return;
11. } else {
12. console.info("Succeeded in translating pixelmap.");
13. }
14. })
15. }
16. }
```

## translate9+

PhonePC/2in1TabletTVWearable

translate(x: number, y: number): Promise<void>

根据输入的坐标对图片进行位置变换。使用Promise异步回调。

translate后的图片尺寸改变为：width+X ，height+Y，建议translate后的图片尺寸宽高不要超过屏幕的宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 区域横坐标。单位：像素。 |
| y | number | 是 | 区域纵坐标。单位：像素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Translate(pixelMap:image.PixelMap) {
4. let translateX: number = 50.0;
5. let translateY: number = 10.0;
6. if (pixelMap != undefined) {
7. pixelMap.translate(translateX, translateY).then(() => {
8. console.info('Succeeded in translating pixelmap.');
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}`);
11. })
12. }
13. }
```

## translateSync12+

PhonePC/2in1TabletTVWearable

translateSync(x: number, y: number): void

根据输入的坐标对图片进行位置变换，同步返回结果。

translate后的图片尺寸改变为：width+X ，height+Y，建议translate后的图片尺寸宽高不要超过屏幕的宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 区域横坐标。单位：像素。 |
| y | number | 是 | 区域纵坐标。单位：像素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function TranslateSync(pixelMap:image.PixelMap) {
2. let translateX : number = 50.0;
3. let translateY : number = 10.0;
4. if (pixelMap != undefined) {
5. pixelMap.translateSync(translateX, translateY);
6. }
7. }
```

## rotate9+

PhonePC/2in1TabletTVWearable

rotate(angle: number, callback: AsyncCallback<void>): void

根据输入的角度对图片进行旋转，使用callback形式返回。

说明

1. 图片旋转的角度取值范围：[0, 360]。超出取值范围时，根据圆周360度自动矫正。例如，-100度与260度效果相同。
2. 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 图片旋转的角度。单位：角度。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当对图片进行旋转成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Rotate(pixelMap:image.PixelMap) {
4. let angle: number = 90.0;
5. if (pixelMap != undefined) {
6. pixelMap.rotate(angle, (err: BusinessError) => {
7. if (err) {
8. console.error(`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}`);
9. return;
10. } else {
11. console.info("Succeeded in rotating pixelmap.");
12. }
13. })
14. }
15. }
```

## rotate9+

PhonePC/2in1TabletTVWearable

rotate(angle: number): Promise<void>

根据输入的角度对图片进行旋转。使用Promise异步回调。

说明

1. 图片旋转的角度取值范围：[0, 360]。超出取值范围时，根据圆周360度自动矫正。例如，-100度与260度效果相同。
2. 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 图片旋转的角度。单位：角度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Rotate(pixelMap:image.PixelMap) {
4. let angle: number = 90.0;
5. if (pixelMap != undefined) {
6. pixelMap.rotate(angle).then(() => {
7. console.info('Succeeded in rotating pixelmap.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}`);
10. })
11. }
12. }
```

## rotateSync12+

PhonePC/2in1TabletTVWearable

rotateSync(angle: number): void

根据输入的角度对图片进行旋转，同步返回结果。

说明

1. 图片旋转的角度取值范围：[0, 360]。超出取值范围时，根据圆周360度自动矫正。例如，-100度与260度效果相同。
2. 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 图片旋转的角度。单位：角度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. function RotateSync(pixelMap: image.PixelMap) {
2. let angle : number = 90.0;
3. if (pixelMap != undefined) {
4. pixelMap.rotateSync(angle);
5. }
6. }
```

## flip9+

PhonePC/2in1TabletTVWearable

flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void

根据输入的条件对图片进行翻转，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontal | boolean | 是 | true表示进行水平翻转，false表示不进行水平翻转。 |
| vertical | boolean | 是 | true表示进行垂直翻转，false表示不进行垂直翻转。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当对图片翻转成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Flip(pixelMap:image.PixelMap) {
4. let horizontal: boolean = true;
5. let vertical: boolean = false;
6. if (pixelMap != undefined) {
7. pixelMap.flip(horizontal, vertical, (err: BusinessError) => {
8. if (err) {
9. console.error(`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}`);
10. return;
11. } else {
12. console.info("Succeeded in flipping pixelmap.");
13. }
14. })
15. }
16. }
```

## flip9+

PhonePC/2in1TabletTVWearable

flip(horizontal: boolean, vertical: boolean): Promise<void>

根据输入的条件对图片进行翻转。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontal | boolean | 是 | true表示进行水平翻转，false表示不进行水平翻转。 |
| vertical | boolean | 是 | true表示进行垂直翻转，false表示不进行垂直翻转。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Flip(pixelMap:image.PixelMap) {
4. let horizontal: boolean = true;
5. let vertical: boolean = false;
6. if (pixelMap != undefined) {
7. pixelMap.flip(horizontal, vertical).then(() => {
8. console.info('Succeeded in flipping pixelmap.');
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}`);
11. })
12. }
13. }
```

## flipSync12+

PhonePC/2in1TabletTVWearable

flipSync(horizontal: boolean, vertical: boolean): void

根据输入的条件对图片进行翻转并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontal | boolean | 是 | true表示进行水平翻转，false表示不进行水平翻转。 |
| vertical | boolean | 是 | true表示进行垂直翻转，false表示不进行垂直翻转。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function FlipSync(pixelMap:image.PixelMap) {
4. let horizontal : boolean = true;
5. let vertical : boolean = false;
6. if (pixelMap != undefined) {
7. pixelMap.flipSync(horizontal, vertical);
8. }
9. }
```

## crop9+

PhonePC/2in1TabletTVWearable

crop(region: Region, callback: AsyncCallback<void>): void

根据输入的尺寸对图片进行裁剪，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-image-i.md#region8) | 是 | 裁剪的尺寸。取值范围不能超过图片的宽高。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当对图片进行裁剪成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Crop(pixelMap:image.PixelMap) {
4. let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
5. if (pixelMap != undefined) {
6. pixelMap.crop(region, (err: BusinessError) => {
7. if (err) {
8. console.error(`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}`);
9. return;
10. } else {
11. console.info("Succeeded in cropping pixelmap.");
12. }
13. })
14. }
15. }
```

## crop9+

PhonePC/2in1TabletTVWearable

crop(region: Region): Promise<void>

根据输入的尺寸对图片进行裁剪。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-image-i.md#region8) | 是 | 裁剪的尺寸。取值范围不能超过图片的宽高。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Crop(pixelMap:image.PixelMap) {
4. let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
5. if (pixelMap != undefined) {
6. pixelMap.crop(region).then(() => {
7. console.info('Succeeded in cropping pixelmap.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}`);

11. });
12. }
13. }
```

## cropSync12+

PhonePC/2in1TabletTVWearable

cropSync(region: Region): void

根据输入的尺寸裁剪图片。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [Region](arkts-apis-image-i.md#region8) | 是 | 裁剪的尺寸。取值范围不能超过图片的宽高。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function CropSync(pixelMap:image.PixelMap) {
4. let region : image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
5. if (pixelMap != undefined) {
6. pixelMap.cropSync(region);
7. }
8. }
```

## getColorSpace10+

PhonePC/2in1TabletTVWearable

getColorSpace(): colorSpaceManager.ColorSpaceManager

获取图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [colorSpaceManager.ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | 图像广色域信息。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980115 | Invalid image parameter. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function GetColorSpace(pixelMap:image.PixelMap) {
4. if (pixelMap != undefined) {
5. let csm = pixelMap.getColorSpace();
6. }
7. }
```

## setColorSpace10+

PhonePC/2in1TabletTVWearable

setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void

设置图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | [colorSpaceManager.ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | 是 | 图像广色域信息。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980111 | The image source data is incomplete. |
| 62980115 | If the image parameter invalid. |

**示例：**

```
1. import { colorSpaceManager } from '@kit.ArkGraphics2D';

3. function SetColorSpace(pixelMap:image.PixelMap) {
4. let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
5. let csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
6. if (pixelMap != undefined) {
7. pixelMap.setColorSpace(csm);
8. }
9. }
```

## applyColorSpace11+

PhonePC/2in1TabletTVWearable

applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void

根据输入的目标色彩空间对图像像素颜色进行色彩空间转换，使用callback形式返回。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetColorSpace | [colorSpaceManager.ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | 是 | 目标色彩空间，支持SRGB、DCI\_P3、DISPLAY\_P3、ADOBE\_RGB\_1998。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当对图像像素颜色进行色彩空间转换成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980104 | Failed to initialize the internal object. |
| 62980108 | Failed to convert the color space. |
| 62980115 | Invalid image parameter. |

**示例：**

```
1. import { colorSpaceManager } from '@kit.ArkGraphics2D';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function ApplyColorSpace(pixelMap:image.PixelMap) {
5. let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
6. let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
7. if (pixelMap != undefined) {
8. try {
9. pixelMap.applyColorSpace(targetColorSpace, (error: BusinessError) => {
10. if (error) {
11. console.error(`ApplyColorSpace failed. code is ${error.code}, message is ${error.message}`);
12. return;
13. } else {
14. console.info("Succeeded ApplyColorSpace.");
15. }
16. });
17. } catch (error) {
18. console.error(`Failed to apply color space for pixelmap object, error code is ${error}`);
19. return;
20. }
21. console.info('Succeeded in applying color space for pixelmap object.');
22. }
23. }
```

## applyColorSpace11+

PhonePC/2in1TabletTVWearable

applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>

根据输入的目标色彩空间对图像像素颜色进行色彩空间转换。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetColorSpace | [colorSpaceManager.ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | 是 | 目标色彩空间，支持SRGB、DCI\_P3、DISPLAY\_P3、ADOBE\_RGB\_1998。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980104 | Failed to initialize the internal object. |
| 62980108 | Failed to convert the color space. |
| 62980115 | Invalid image parameter. |

**示例：**

```
1. import { colorSpaceManager } from '@kit.ArkGraphics2D';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function ApplyColorSpace(pixelMap:image.PixelMap) {
5. let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
6. let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
7. if (pixelMap != undefined) {
8. pixelMap.applyColorSpace(targetColorSpace).then(() => {
9. console.info('Succeeded in applying color space for pixelmap object.');
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to apply color space for pixelmap object, error code is ${error}`);
12. return;
13. });
14. }
15. }
```

## toSdr12+

PhonePC/2in1TabletTVWearable

toSdr(): Promise<void>

将HDR的图像内容转换为SDR的图像内容。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980137 | Invalid image operation. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ToSdr(context: Context) {
4. // 此处'app.media.startIcon'需要替换为本地hdr图片。
5. let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
6. let imageSource = image.createImageSource(img.buffer.slice(0));
7. let decodingOptions: image.DecodingOptions = {
8. desiredDynamicRange: image.DecodingDynamicRange.AUTO
9. };
10. let pixelmap = imageSource.createPixelMapSync(decodingOptions);
11. if (pixelmap != undefined) {
12. console.info('Succeeded in creating pixelMap object.');
13. pixelmap.toSdr().then(() => {
14. let imageInfo = pixelmap.getImageInfoSync();
15. console.info("after toSdr ,imageInfo isHdr:" + imageInfo.isHdr);
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to set sdr. code is ${err.code}, message is ${err.message}`);
18. });
19. } else {
20. console.error('Failed to create pixelMap.');
21. }
22. }
```

## getMetadata12+

PhonePC/2in1TabletTVWearable

getMetadata(key: HdrMetadataKey): HdrMetadataValue

从PixelMap中获取元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12) | 是 | HDR元数据的关键字，可用于查询对应值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HdrMetadataValue](arkts-apis-image-t.md#hdrmetadatavalue12) | 返回元数据的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource unavailable. |
| 62980173 | The DMA memory does not exist. |
| 62980302 | Memory copy failed. Possibly caused by invalid metadata value. |

**示例：**

```
1. async function GetMetadata(context: Context) {
2. // 此处'app.media.startIcon'需要替换为本地hdr图片。
3. let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
4. let imageSource = image.createImageSource(img.buffer.slice(0));
5. let decodingOptions: image.DecodingOptions = {
6. desiredDynamicRange: image.DecodingDynamicRange.AUTO
7. };
8. let pixelmap = imageSource.createPixelMapSync(decodingOptions);
9. if (pixelmap != undefined) {
10. console.info('Succeeded in creating pixelMap object.');
11. try {
12. let staticMetadata = pixelmap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
13. console.info(`getMetadata:${staticMetadata}`);
14. } catch (e) {
15. console.error('pixelmap create failed' + e);
16. }
17. } else {
18. console.error('Failed to create pixelMap.');
19. }
20. }
```

## setMetadata12+

PhonePC/2in1TabletTVWearable

setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>

设置PixelMap元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12) | 是 | HDR元数据的关键字，用于设置对应值。 |
| value | [HdrMetadataValue](arkts-apis-image-t.md#hdrmetadatavalue12) | 是 | 元数据的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource unavailable. |
| 62980173 | The DMA memory does not exist. |
| 62980302 | Memory copy failed. Possibly caused by invalid metadata value. |

**示例：**

创建DMA\_ALLOC内存的PixelMap方法请参考: [系统默认的内存分配方式](../harmonyos-guides/image-allocator-type.md#系统默认的内存分配方式)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import {image} from '@kit.ImageKit';

4. function SetMetadata(pixelMap: image.PixelMap) { // 入参pixelMap内存类型需为DMA_ALLOC内存类型，其创建方法请参考上方链接。
5. let staticMetadata: image.HdrStaticMetadata = {
6. displayPrimariesX: [1.1, 1.1, 1.1],
7. displayPrimariesY: [1.2, 1.2, 1.2],
8. whitePointX: 1.1,
9. whitePointY: 1.2,
10. maxLuminance: 2.1,
11. minLuminance: 1.0,
12. maxContentLightLevel: 2.1,
13. maxFrameAverageLightLevel: 2.1,
14. };
15. pixelMap.setMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA, staticMetadata).then(() => {
16. console.info('Succeeded in setting pixelMap metadata.');
17. }).catch((error: BusinessError) => {
18. console.error("Failed to set the metadata.code ", error);
19. })
20. }
```

## setTransferDetached12+

PhonePC/2in1TabletTVWearable

setTransferDetached(detached: boolean): void

pixelmap在跨线程传输时，断开原线程的引用。适用于需立即释放pixelmap的场景。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detached | boolean | 是 | true表示断开原线程引用，false表示不断开原线程引用。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 501 | Resource Unavailable |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { taskpool } from '@kit.ArkTS';

4. @Concurrent
5. // 子线程方法。
6. async function loadPixelMap(rawFileDescriptor: number): Promise<PixelMap> {
7. // 创建imageSource。
8. const imageSource = image.createImageSource(rawFileDescriptor);
9. // 创建pixelMap。
10. const pixelMap = imageSource.createPixelMapSync();
11. // 释放imageSource。
12. imageSource.release();
13. // 使pixelMap在跨线程传输完成后，断开原线程的引用。
14. pixelMap.setTransferDetached(true);
15. // 返回pixelMap给主线程。
16. return pixelMap;
17. }

19. @Entry
20. @Component
21. struct Demo {
22. @State pixelMap: PixelMap | undefined = undefined;
23. // 主线程方法。
24. private loadImageFromThread(): void {
25. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
26. const resourceMgr = context.resourceManager;
27. // 此处‘example.jpg’仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
28. resourceMgr.getRawFd('example.jpg').then(rawFileDescriptor => {
29. taskpool.execute(loadPixelMap, rawFileDescriptor).then(pixelMap => {
30. if (pixelMap) {
31. this.pixelMap = pixelMap as PixelMap;
32. console.info('Succeeded in creating pixelMap.');
33. // 主线程释放pixelMap。由于子线程返回pixelMap时已调用setTransferDetached，所以此处能够立即释放pixelMap。
34. this.pixelMap.release();
35. } else {
36. console.error('Failed to create pixelMap.');
37. }
38. });
39. });
40. }
41. build() {
42. // ...
43. }
44. }
```

## marshalling10+

PhonePC/2in1TabletTVWearable

marshalling(sequence: rpc.MessageSequence): void

将PixelMap序列化后写入MessageSequence。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 新创建的MessageSequence。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980115 | Invalid image parameter. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';

3. class MySequence implements rpc.Parcelable {
4. pixel_map: image.PixelMap;
5. constructor(conPixelMap : image.PixelMap) {
6. this.pixel_map = conPixelMap;
7. }
8. marshalling(messageSequence : rpc.MessageSequence) {
9. this.pixel_map.marshalling(messageSequence);
10. console.info('marshalling');
11. return true;
12. }
13. unmarshalling(messageSequence : rpc.MessageSequence) {
14. image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel: image.PixelMap) => {
15. pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
16. this.pixel_map = pixelMap;
17. pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
18. console.info(`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}`);
19. })
20. })
21. });
22. return true;
23. }
24. }
25. async function Marshalling() {
26. const color: ArrayBuffer = new ArrayBuffer(96);
27. let bufferArr: Uint8Array = new Uint8Array(color);
28. for (let i = 0; i < bufferArr.length; i++) {
29. bufferArr[i] = 0x80;
30. }
31. let opts: image.InitializationOptions = {
32. editable: true,
33. pixelFormat: image.PixelMapFormat.BGRA_8888,
34. size: { height: 4, width: 6 },
35. alphaType: image.AlphaType.UNPREMUL
36. }
37. let pixelMap: image.PixelMap | undefined = undefined;
38. await image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
39. pixelMap = srcPixelMap;
40. })
41. if (pixelMap != undefined) {
42. // 序列化。
43. let parcelable: MySequence = new MySequence(pixelMap);
44. let data: rpc.MessageSequence = rpc.MessageSequence.create();
45. data.writeParcelable(parcelable);

47. // 反序列化rpc获取到data。
48. let ret: MySequence = new MySequence(pixelMap);
49. data.readParcelable(ret);
50. }
51. }
```

## unmarshalling10+

PhonePC/2in1TabletTVWearable

unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>

从MessageSequence中获取PixelMap，如需使用同步方式创建PixelMap可使用：[createPixelMapFromParcel](arkts-apis-image-f.md#imagecreatepixelmapfromparcel11)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存有PixelMap信息的MessageSequence。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980115 | Invalid image parameter. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';

3. class MySequence implements rpc.Parcelable {
4. pixel_map: image.PixelMap;
5. constructor(conPixelMap: image.PixelMap) {
6. this.pixel_map = conPixelMap;
7. }
8. marshalling(messageSequence: rpc.MessageSequence) {
9. this.pixel_map.marshalling(messageSequence);
10. console.info('marshalling');
11. return true;
12. }
13. unmarshalling(messageSequence: rpc.MessageSequence) {
14. image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel : image.PixelMap) => {
15. pixelParcel.unmarshalling(messageSequence).then(async (pixelMap : image.PixelMap) => {
16. this.pixel_map = pixelMap;
17. pixelMap.getImageInfo().then((imageInfo : image.ImageInfo) => {
18. console.info(`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}`);
19. })
20. })
21. });
22. return true;
23. }
24. }
25. async function Unmarshalling() {
26. const color: ArrayBuffer = new ArrayBuffer(96);
27. let bufferArr: Uint8Array = new Uint8Array(color);
28. for (let i = 0; i < bufferArr.length; i++) {
29. bufferArr[i] = 0x80;
30. }
31. let opts: image.InitializationOptions = {
32. editable: true,
33. pixelFormat: image.PixelMapFormat.BGRA_8888,
34. size: { height: 4, width: 6 },
35. alphaType: image.AlphaType.UNPREMUL
36. }
37. let pixelMap: image.PixelMap | undefined = undefined;
38. await image.createPixelMap(color, opts).then((srcPixelMap : image.PixelMap) => {
39. pixelMap = srcPixelMap;
40. })
41. if (pixelMap != undefined) {
42. // 序列化。
43. let parcelable: MySequence = new MySequence(pixelMap);
44. let data : rpc.MessageSequence = rpc.MessageSequence.create();
45. data.writeParcelable(parcelable);

47. // 反序列化rpc获取到data。
48. let ret : MySequence = new MySequence(pixelMap);
49. data.readParcelable(ret);
50. }
51. }
```

## release7+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放PixelMap对象（释放后，任何访问该对象内部数据的方法调用都会失败）。使用Promise异步回调。

图片使用的内存往往较大，在PixelMap对象使用完成后，应主动调用该方法及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

注意

释放指的是ArkTS对象释放与之关联的native对象的管理权。仅当所有管理该native对象的ArkTS对象都被释放时，native对象占用的内存才会被回收。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release(pixelMap:image.PixelMap) {
4. if (pixelMap != undefined) {
5. await pixelMap.release().then(() => {
6. console.info('Succeeded in releasing pixelmap object.');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}`);
9. })
10. }
11. }
```

## release7+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放PixelMap对象（释放后，任何访问该对象内部数据的方法调用都会失败）。使用callback形式返回释放结果。

图片使用的内存往往较大，在PixelMap对象使用完成后，应主动调用该方法及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

注意

释放指的是ArkTS对象释放与之关联的native对象的管理权。仅当所有管理该native对象的ArkTS对象都被释放时，native对象占用的内存才会被回收。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当对PixelMap对象释放成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release(pixelMap:image.PixelMap) {
4. if (pixelMap != undefined) {
5. pixelMap.release((err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to release pixelmap object. code is ${err.code}, message is ${err.message}`);
8. return;
9. } else {
10. console.info('Succeeded in releasing pixelmap object.');
11. }
12. })
13. }
14. }
```

## convertPixelFormat12+

PhonePC/2in1TabletTVWearable

convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>

YUV和RGB类型互转。使用Promise异步回调。

支持NV12/NV21与RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16互转，YCRCB\_P010/YCBCR\_P010与RGBA1010102互转。

从API18开始，可用于ASTC\_4x4类型转为RGBA\_8888类型，目前仅支持ASTC\_4x4转为RGBA\_8888。

注意

仅在ASTC\_4x4格式的图像需要进行像素访问时，建议调用此接口将ASTC\_4x4类型转为RGBA\_8888类型。由于使用ASTC\_4x4反解为RGBA\_8888时延较高，其余情况下不推荐使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetPixelFormat | [PixelMapFormat](arkts-apis-image-e.md#pixelmapformat7) | 是 | 目标像素格式，用于YUV和RGB类型互转，或者ASTC\_4x4类型转为RGBA\_8888类型。目前仅支持NV12/NV21与RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16互转，YCRCB\_P010/YCBCR\_P010与RGBA1010102互转，ASTC\_4x4转为RGBA\_8888。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid input parameter. |
| 62980178 | Failed to create the pixelmap. |
| 62980274 | The conversion failed |
| 62980276 | The type to be converted is an unsupported target pixel format |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function ConvertPixelFormat(pixelMap: image.PixelMap) {
4. if (pixelMap != undefined) {
5. // 设置目标像素格式为NV12。
6. let targetPixelFormat = image.PixelMapFormat.NV12;
7. pixelMap.convertPixelFormat(targetPixelFormat).then(() => {
8. // pixelMap转换成NV12格式成功。
9. console.info('PixelMapFormat convert Succeeded');
10. }).catch((error: BusinessError) => {
11. // pixelMap转换成NV12格式失败。
12. console.error(`PixelMapFormat convert Failed. code is ${error.code}, message is ${error.message}`);
13. })
14. }
15. }
```

## setMemoryNameSync13+

PhonePC/2in1TabletTVWearable

setMemoryNameSync(name: string): void

设置PixelMap内存标识符。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | pixelmap内存标识符，只允许DMA和ASHMEM内存形式的pixelmap设置。DMA内存设置名字长度取值范围为[1, 255]，ASHMEM内存设置名字长度取值范围为[1, 244]，单位字节。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.The length of the input parameter is too long. 2.Parameter verification failed. |
| 501 | Resource unavailable. |
| 62980286 | Memory format not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function SetMemoryNameSync(pixelMap:image.PixelMap) {
4. if (pixelMap != undefined) {
5. try {
6. pixelMap.setMemoryNameSync("PixelMapName Test");
7. } catch(e) {
8. let error = e as BusinessError;
9. console.error(`setMemoryNameSync error. code is ${error.code}, message is ${error.message}`);
10. }
11. }
12. }
```

## getUniqueId22+

PhonePC/2in1TabletTVWearable

getUniqueId(): number

获取PixelMap的唯一ID。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 唯一ID。取值为正整数。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | The PixelMap has been released. |

**示例：**

```
1. function DemoGetUniqueId(pixelMap: PixelMap) {
2. const uniqueId: number = pixelMap.getUniqueId();
3. }
```

## isReleased22+

PhonePC/2in1TabletTVWearable

isReleased(): boolean

检查PixelMap对象是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失败。

注意

释放指的是ArkTS对象释放与之关联的native对象的管理权。仅当所有管理该native对象的ArkTS对象都被释放时，native对象占用的内存才会被回收。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | PixelMap是否已被释放。返回true表示已被释放，否则返回false。 |

**示例：**

```
1. async function DemoIsReleased(pixelMap: PixelMap) { // 未释放的PixelMap。
2. pixelMap.isReleased(); // 返回false。
3. await pixelMap.release();
4. pixelMap.isReleased(); // 返回true。
5. }
```
