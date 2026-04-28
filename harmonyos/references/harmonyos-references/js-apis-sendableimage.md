---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage
title: @ohos.multimedia.sendableImage (基于Sendable对象的图片处理)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.sendableImage (基于Sendable对象的图片处理)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:971b30c4aa405d5700c7d3bb00721031e98ef458a2803e1656d4821b94110de4
---

本模块基于[Sendable](../harmonyos-guides/arkts-sendable.md)对象，提供图片处理效果，包括通过属性创建PixelMap、读取图像像素数据、读取区域内的图片数据等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sendableImage } from '@kit.ImageKit';
```

## sendableImage.createPixelMap

PhonePC/2in1TabletTVWearable

createPixelMap(colors: ArrayBuffer, options: image.InitializationOptions): Promise<PixelMap>

通过属性创建PixelMap，默认采用BGRA\_8888格式处理数据。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | 默认按照BGRA\_8888格式处理的颜色数组。 |
| options | [image.InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度，尺寸，缩放值，像素格式和是否可编辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](js-apis-sendableimage.md#pixelmap)> | 返回PixelMap。  当创建的PixelMap大小超过原图大小时，返回原图PixelMap大小。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo() {
6. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
7. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
8. sendableImage.createPixelMap(color, opts).then((pixelMap: sendableImage.PixelMap) => {
9. console.info('Succeeded in creating pixelmap.');
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
12. })
13. }
```

## sendableImage.createPixelMapFromParcel

PhonePC/2in1TabletTVWearable

createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap

从MessageSequence中获取PixelMap。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存有PixelMap信息的MessageSequence。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](js-apis-sendableimage.md#pixelmap) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | Operation failed |
| 62980097 | IPC error |
| 62980115 | Invalid input parameter |
| 62980105 | Failed to get the data |
| 62980177 | Abnormal API environment |
| 62980178 | Failed to create the PixelMap |
| 62980179 | Abnormal buffer size |
| 62980180 | FD mapping failed |
| 62980246 | Failed to read the PixelMap |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { rpc } from '@kit.IPCKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. class MySequence implements rpc.Parcelable {
7. pixel_map: sendableImage.PixelMap;
8. constructor(conPixelmap: sendableImage.PixelMap) {
9. this.pixel_map = conPixelmap;
10. }
11. marshalling(messageSequence: rpc.MessageSequence) {
12. this.pixel_map.marshalling(messageSequence);
13. return true;
14. }
15. unmarshalling(messageSequence: rpc.MessageSequence) {
16. try {
17. this.pixel_map = sendableImage.createPixelMapFromParcel(messageSequence);
18. } catch(e) {
19. let error = e as BusinessError;
20. console.error(`createPixelMapFromParcel error. code is ${error.code}, message is ${error.message}`);
21. return false;
22. }
23. return true;
24. }
25. }
26. async function Demo() {
27. const color: ArrayBuffer = new ArrayBuffer(96);
28. let bufferArr: Uint8Array = new Uint8Array(color);
29. for (let i = 0; i < bufferArr.length; i++) {
30. bufferArr[i] = 0x80;
31. }
32. let opts: image.InitializationOptions = {
33. editable: true,
34. pixelFormat: 4,
35. size: { height: 4, width: 6 },
36. alphaType: 3
37. }
38. let pixelMap: sendableImage.PixelMap | undefined = undefined;
39. await sendableImage.createPixelMap(color, opts).then((srcPixelMap: sendableImage.PixelMap) => {
40. pixelMap = srcPixelMap;
41. })
42. if (pixelMap != undefined) {
43. // 序列化。
44. let parcelable: MySequence = new MySequence(pixelMap);
45. let data: rpc.MessageSequence = rpc.MessageSequence.create();
46. data.writeParcelable(parcelable);

48. // 反序列化rpc获取到data。
49. let ret: MySequence = new MySequence(pixelMap);
50. data.readParcelable(ret);

52. // 获取到PixelMap。
53. let newPixelMap = ret.pixel_map;
54. }
55. }
```

## sendableImage.createPixelMapFromSurface

PhonePC/2in1TabletTVWearable

createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>

根据Surface ID和区域信息创建一个PixelMap对象。该区域的大小由[Region](arkts-apis-image-i.md#region8).size指定。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 对应Surface的ID，可通过预览组件获取，如[XComponent](ts-basic-components-xcomponent.md)组件。 |
| region | [image.Region](arkts-apis-image-i.md#region8) | 是 | 截取的画面区域。仅支持从画面左上角开始截取部分或整个画面，即Region中的x和y必须为0，Region.size中width和height的取值范围分别为[1, 预览流宽度]和[1, 预览流高度]。如需截取任意区域，可先获取整个画面，再使用[crop](js-apis-sendableimage.md#crop)截取所需区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](js-apis-sendableimage.md#pixelmap)> | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980115 | If the image parameter invalid. |
| 62980105 | Failed to get the data |
| 62980178 | Failed to create the PixelMap |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo(surfaceId: string) {
6. let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
7. sendableImage.createPixelMapFromSurface(surfaceId, region).then(() => {
8. console.info('Succeeded in creating pixelmap from Surface');
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
11. });
12. }
```

## sendableImage.createPixelMapSync

PhonePC/2in1TabletTVWearable

createPixelMapSync(colors: ArrayBuffer, options: image.InitializationOptions): PixelMap

通过属性创建PixelMap，同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | BGRA\_8888格式的颜色数组。 |
| options | [image.InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度，尺寸，缩放值，像素格式和是否可编辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](js-apis-sendableimage.md#pixelmap) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo() {
6. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
7. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
8. let pixelMap : sendableImage.PixelMap = sendableImage.createPixelMapSync(color, opts);
9. return pixelMap;
10. }
```

## sendableImage.convertFromPixelMap

PhonePC/2in1TabletTVWearable

convertFromPixelMap(pixelmap: image.PixelMap): PixelMap

通过image下的PixelMap创建出一个sendableImage下的PixelMap，同步返回PixelMap结果。原PixelMap的方法均不可再调用。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image下的非sendable的PixelMap。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](js-apis-sendableimage.md#pixelmap) | 成功同步返回sendable的PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the image parameter invalid. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980104 | Failed to initialize the internal object. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';

4. async function Demo() {
5. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
6. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
7. let pixelMap : image.PixelMap = image.createPixelMapSync(color, opts);
8. let sendablePixelMap : sendableImage.PixelMap = sendableImage.convertFromPixelMap(pixelMap);
9. return sendablePixelMap;
10. }
```

## sendableImage.convertToPixelMap

PhonePC/2in1TabletTVWearable

convertToPixelMap(pixelmap: PixelMap): image.PixelMap

通过sendableImage下的PixelMap创建出一个image下的PixelMap，同步返回PixelMap结果。原PixelMap的方法均不可再调用。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | [PixelMap](js-apis-sendableimage.md#pixelmap) | 是 | sendableImage下的PixelMap。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回image下的非sendable的PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the image parameter invalid. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980104 | Failed to initialize the internal object. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';

4. async function Demo() {
5. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
6. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
7. let sendablePixelMap : sendableImage.PixelMap = sendableImage.createPixelMapSync(color, opts);
8. let pixelMap : image.PixelMap = sendableImage.convertToPixelMap(sendablePixelMap);
9. return pixelMap;
10. }
```

## ISendable

PhonePC/2in1TabletTVWearable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 类型 | 说明 |
| --- | --- |
| [lang.ISendable](js-apis-arkts-lang.md#langisendable) | 所有Sendable类型的父类型。 |

## PixelMap

PhonePC/2in1TabletTVWearable

图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[createPixelMap](js-apis-sendableimage.md#sendableimagecreatepixelmap)创建一个PixelMap实例。目前PixelMap序列化大小最大128MB，超过会送显失败。大小计算方式为（宽\*高\*每像素占用字节数）。

sendableImage下的PixelMap支持sendable属性，支持worker线程共享。sendableImage下的PixelMap，可以利用[Convert](js-apis-sendableimage.md#sendableimageconverttopixelmap)方法与image下的PixelMap进行互相转换。转换后，原对象的方法均不允许再调用，否则将报错501 无法调用接口。跨线程处理PixelMap时，需要考虑多线程问题。

在调用PixelMap的方法前，需要先通过[sendableImage.createPixelMap](js-apis-sendableimage.md#sendableimagecreatepixelmap)构建一个PixelMap对象。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isEditable | boolean | 是 | 否 | true表示图像像素可被编辑，false表示不可被编辑。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isStrideAlignment | boolean | 是 | 否 | true表示图像内存为DMA内存，false表示非DMA内存。DMA内存的PixelMap会做256字节内存对齐，行末会存在padding区域。 |

### readPixelsToBuffer

PhonePC/2in1TabletTVWearable

readPixelsToBuffer(dst: ArrayBuffer): Promise<void>

读取图像像素数据，结果写入ArrayBuffer里。使用Promise异步回调。

该接口指定BGRA\_8888格式创建pixelmap，读取的像素数据与原数据保持一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dst | ArrayBuffer | 是 | 缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](js-apis-sendableimage.md#getpixelbytesnumber)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取结果，失败时返回错误信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sendableImage } from '@kit.ImageKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
6. if (pixelMap != undefined) {
7. pixelMap.readPixelsToBuffer(readBuffer).then(() => {
8. console.info('Succeeded in reading image pixel data.'); // 符合条件则进入。
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`);// 不符合条件则进入。
11. })
12. }
13. }
```

### readPixelsToBufferSync

PhonePC/2in1TabletTVWearable

readPixelsToBufferSync(dst: ArrayBuffer): void

以同步方法读取PixelMap到Buffer里。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dst | ArrayBuffer | 是 | 缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](js-apis-sendableimage.md#getpixelbytesnumber)接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap: sendableImage.PixelMap) {
4. const bufferSize = pixelMap.getPixelBytesNumber();
5. const readBuffer: ArrayBuffer = new ArrayBuffer(bufferSize);
6. if (pixelMap != undefined) {
7. pixelMap.readPixelsToBufferSync(readBuffer);
8. }
9. }
```

### readPixels

PhonePC/2in1TabletTVWearable

readPixels(area: image.PositionArea): Promise<void>

读取区域内的图片数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [image.PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域大小，根据区域读取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取读取结果，失败时返回错误信息。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo(pixelMap : sendableImage.PixelMap) {
6. const area: image.PositionArea = {
7. pixels: new ArrayBuffer(8),
8. offset: 0,
9. stride: 8,
10. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
11. };
12. if (pixelMap != undefined) {
13. pixelMap.readPixels(area).then(() => {
14. console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
15. }).catch((error: BusinessError) => {
16. console.error(`Failed to read the image data in the area. code is ${error.code}, message is ${error.message}`);// 不符合条件则进入。
17. })
18. }
19. }
```

### readPixelsSync

PhonePC/2in1TabletTVWearable

readPixelsSync(area: image.PositionArea): void

读取区域内的图片数据并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [image.PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域大小，根据区域读取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. const area : image.PositionArea = {
6. pixels: new ArrayBuffer(8),
7. offset: 0,
8. stride: 8,
9. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
10. };
11. if (pixelMap != undefined) {
12. pixelMap.readPixelsSync(area);
13. }
14. }
```

### writePixels

PhonePC/2in1TabletTVWearable

writePixels(area: image.PositionArea): Promise<void>

将PixelMap写入指定区域内。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [image.PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域，根据区域写入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取写入结果，失败时返回错误信息。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo(pixelMap : sendableImage.PixelMap) {
6. const area: image.PositionArea = {
7. pixels: new ArrayBuffer(8),
8. offset: 0,
9. stride: 8,
10. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
11. };
12. let bufferArr: Uint8Array = new Uint8Array(area.pixels);
13. for (let i = 0; i < bufferArr.length; i++) {
14. bufferArr[i] = i + 1;
15. }
16. if (pixelMap != undefined) {
17. pixelMap.writePixels(area).then(() => {
18. console.info('Succeeded to write pixelmap into the specified area.');
19. }).catch((error: BusinessError) => {
20. console.error(`Failed to write pixelmap into the specified area. code is ${error.code}, message is ${error.message}`);
21. })
22. }
23. }
```

### writePixelsSync

PhonePC/2in1TabletTVWearable

writePixelsSync(area: image.PositionArea): void

以同步方法将PixelMap写入指定区域内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [image.PositionArea](arkts-apis-image-i.md#positionarea7) | 是 | 区域，根据区域写入。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. const area: image.PositionArea = {
6. pixels: new ArrayBuffer(8),
7. offset: 0,
8. stride: 8,
9. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
10. };
11. let bufferArr: Uint8Array = new Uint8Array(area.pixels);
12. for (let i = 0; i < bufferArr.length; i++) {
13. bufferArr[i] = i + 1;
14. }
15. if (pixelMap != undefined) {
16. pixelMap.writePixelsSync(area);
17. }
18. }
```

### writeBufferToPixels

PhonePC/2in1TabletTVWearable

writeBufferToPixels(src: ArrayBuffer): Promise<void>

读取缓冲区中的图片数据，结果写入PixelMap中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | ArrayBuffer | 是 | 图像像素数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取结果，失败时返回错误信息。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
6. let bufferArr: Uint8Array = new Uint8Array(color);
7. for (let i = 0; i < bufferArr.length; i++) {
8. bufferArr[i] = i + 1;
9. }
10. if (pixelMap != undefined) {
11. pixelMap.writeBufferToPixels(color).then(() => {
12. console.info("Succeeded in writing data from a buffer to a PixelMap.");
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
15. })
16. }
17. }
```

### writeBufferToPixelsSync

PhonePC/2in1TabletTVWearable

writeBufferToPixelsSync(src: ArrayBuffer): void

读取缓冲区中的图片数据，结果写入PixelMap并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | ArrayBuffer | 是 | 图像像素数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap: sendableImage.PixelMap) {
4. const bufferSize = pixelMap.getPixelBytesNumber();
5. const color : ArrayBuffer = new ArrayBuffer(bufferSize);
6. let bufferArr : Uint8Array = new Uint8Array(color);
7. for (let i = 0; i < bufferArr.length; i++) {
8. bufferArr[i] = i + 1;
9. }
10. if (pixelMap != undefined) {
11. pixelMap.writeBufferToPixelsSync(color);
12. }
13. }
```

### getImageInfo

PhonePC/2in1TabletTVWearable

getImageInfo(): Promise<image.ImageInfo>

获取图像像素信息。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.ImageInfo](arkts-apis-image-i.md#imageinfo)> | Promise实例，用于异步获取图像像素信息，失败时返回错误信息。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo(pixelMap : sendableImage.PixelMap) {
6. if (pixelMap != undefined) {
7. pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
8. if (imageInfo != undefined) {
9. console.info("Succeeded in obtaining the image pixel map information."+ imageInfo.size.height);
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
13. })
14. }
15. }
```

### getImageInfoSync

PhonePC/2in1TabletTVWearable

getImageInfoSync(): image.ImageInfo

以同步方法获取图像像素信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.ImageInfo](arkts-apis-image-i.md#imageinfo) | 图像像素信息。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 501 | Resource Unavailable |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { sendableImage } from '@kit.ImageKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. if (pixelMap != undefined) {
6. let imageInfo : image.ImageInfo = pixelMap.getImageInfoSync();
7. }
8. }
```

### getBytesNumberPerRow

PhonePC/2in1TabletTVWearable

getBytesNumberPerRow(): number

获取图像像素每行字节数。单位：字节。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图像像素的行字节数。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let rowCount: number = pixelMap.getBytesNumberPerRow();
5. }
```

### getPixelBytesNumber

PhonePC/2in1TabletTVWearable

getPixelBytesNumber(): number

获取图像像素的总字节数。单位：字节。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图像像素的总字节数。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
5. }
```

### getDensity

PhonePC/2in1TabletTVWearable

getDensity():number

获取当前图像像素的密度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图像像素的密度，单位为ppi。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let getDensity: number = pixelMap.getDensity();
5. }
```

### opacity

PhonePC/2in1TabletTVWearable

opacity(rate: number): Promise<void>

通过设置透明比率来让PixelMap达到对应的透明效果。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | number | 是 | 透明比率的值，取值范围是(0,1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取结果，失败时返回错误信息。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. let rate: number = 0.5;
6. if (pixelMap != undefined) {
7. pixelMap.opacity(rate).then(() => {
8. console.info('Succeeded in setting opacity.');
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to set opacity. code is ${err.code}, message is ${err.message}`);
11. })
12. }
13. }
```

### opacitySync

PhonePC/2in1TabletTVWearable

opacitySync(rate: number): void

设置PixelMap的透明比率，初始化PixelMap。

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
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let rate : number = 0.5;
5. if (pixelMap != undefined) {
6. pixelMap.opacitySync(rate);
7. }
8. }
```

### createAlphaPixelmap

PhonePC/2in1TabletTVWearable

createAlphaPixelmap(): Promise<PixelMap>

根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的PixelMap，可用于阴影效果。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](js-apis-sendableimage.md#pixelmap)> | Promise实例，返回PixelMap。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. if (pixelMap != undefined) {
6. pixelMap.createAlphaPixelmap().then((alphaPixelMap: sendableImage.PixelMap) => {
7. console.info('Succeeded in creating alpha pixelmap.');
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to create alpha pixelmap. code is ${error.code}, message is ${error.message}`);
10. })
11. }
12. }
```

### createAlphaPixelmapSync

PhonePC/2in1TabletTVWearable

createAlphaPixelmapSync(): PixelMap

根据Alpha通道的信息，生成一个仅包含Alpha通道信息的PixelMap，可用于阴影效果，同步返回PixelMap类型的结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](js-apis-sendableimage.md#pixelmap) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let resPixelMap : sendableImage.PixelMap = pixelMap.createAlphaPixelmapSync();
5. return resPixelMap;
6. }
```

### scale

PhonePC/2in1TabletTVWearable

scale(x: number, y: number): Promise<void>

根据输入的宽高对图片进行缩放。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 宽度的缩放倍数。 |
| y | number | 是 | 高度的缩放倍数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，异步返回结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. let scaleX: number = 2.0;
6. let scaleY: number = 1.0;
7. if (pixelMap != undefined) {
8. pixelMap.scale(scaleX, scaleY).then(() => {
9. console.info('Succeeded in scaling pixelmap.');
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);

13. })
14. }
15. }
```

### scaleSync

PhonePC/2in1TabletTVWearable

scaleSync(x: number, y: number): void

以同步方法根据输入的宽高对图片进行缩放。

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
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let scaleX: number = 2.0;
5. let scaleY: number = 1.0;
6. if (pixelMap != undefined) {
7. pixelMap.scaleSync(scaleX, scaleY);
8. }
9. }
```

### translate

PhonePC/2in1TabletTVWearable

translate(x: number, y: number): Promise<void>

根据输入的坐标对图片进行位置变换。使用Promise异步回调。

translate后的图片尺寸改变为：width+X，height+Y，建议translate后的图片尺寸宽高不超过屏幕的宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 区域横坐标。单位：像素。 |
| y | number | 是 | 区域纵坐标。单位：像素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，异步返回结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. let translateX: number = 50.0;
6. let translateY: number = 10.0;
7. if (pixelMap != undefined) {
8. pixelMap.translate(translateX, translateY).then(() => {
9. console.info('Succeeded in translating pixelmap.');
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}`);
12. })
13. }
14. }
```

### translateSync

PhonePC/2in1TabletTVWearable

translateSync(x: number, y: number): void

根据输入的坐标对图片进行位置变换并同步返回结果。

translate后的图片尺寸改变为：width+X，height+Y，建议translate后的图片尺寸宽高不超过屏幕的宽高。

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
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let translateX : number = 50.0;
5. let translateY : number = 10.0;
6. if (pixelMap != undefined) {
7. pixelMap.translateSync(translateX, translateY);
8. }
9. }
```

### rotate

PhonePC/2in1TabletTVWearable

rotate(angle: number): Promise<void>

根据输入的角度对图片进行旋转。使用Promise异步回调。

说明

* 图片旋转的角度取值范围：[0, 360]。超出取值范围时，根据圆周360度自动校正。例如，-100度与260度效果相同。
* 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 图片旋转的角度。单位：角度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，异步返回结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. let angle: number = 90.0;
6. if (pixelMap != undefined) {
7. pixelMap.rotate(angle).then(() => {
8. console.info('Succeeded in rotating pixelmap.');
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}`);
11. })
12. }
13. }
```

### rotateSync

PhonePC/2in1TabletTVWearable

rotateSync(angle: number): void

根据输入的角度对图片进行旋转并同步返回结果。

说明

* 图片旋转的角度取值范围：[0, 360]。超出取值范围时，根据圆周360度自动校正。例如，-100度与260度效果相同。
* 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

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
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let angle : number = 90.0;
5. if (pixelMap != undefined) {
6. pixelMap.rotateSync(angle);
7. }
8. }
```

### flip

PhonePC/2in1TabletTVWearable

flip(horizontal: boolean, vertical: boolean): Promise<void>

根据输入的条件对图片进行翻转。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontal | boolean | 是 | true表示进行水平翻转，false表示不进行水平翻转。 |
| vertical | boolean | 是 | true表示进行垂直翻转，false表示不进行垂直翻转。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，异步返回结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. let horizontal: boolean = true;
6. let vertical: boolean = false;
7. if (pixelMap != undefined) {
8. pixelMap.flip(horizontal, vertical).then(() => {
9. console.info('Succeeded in flipping pixelmap.');
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}`);

13. })
14. }
15. }
```

### flipSync

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
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. let horizontal : boolean = true;
5. let vertical : boolean = false;
6. if (pixelMap != undefined) {
7. pixelMap.flipSync(horizontal, vertical);
8. }
9. }
```

### crop

PhonePC/2in1TabletTVWearable

crop(region: image.Region): Promise<void>

根据输入的尺寸对图片进行裁剪。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [image.Region](arkts-apis-image-i.md#region8) | 是 | 裁剪的尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，异步返回结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo(pixelMap : sendableImage.PixelMap) {
6. let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
7. if (pixelMap != undefined) {
8. pixelMap.crop(region).then(() => {
9. console.info('Succeeded in cropping pixelmap.');
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}`);

13. });
14. }
15. }
```

### cropSync

PhonePC/2in1TabletTVWearable

cropSync(region: image.Region): void

根据输入的尺寸裁剪图片。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | [image.Region](arkts-apis-image-i.md#region8) | 是 | 裁剪的尺寸。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource Unavailable. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. let region : image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
6. if (pixelMap != undefined) {
7. pixelMap.cropSync(region);
8. }
9. }
```

### getColorSpace

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
| 62980101 | If the image data abnormal. |
| 62980103 | If the image data unsupport. |
| 62980115 | If the image parameter invalid. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(pixelMap : sendableImage.PixelMap) {
4. if (pixelMap != undefined) {
5. let csm = pixelMap.getColorSpace();
6. }
7. }
```

### setColorSpace

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
| 62980111 | If the operation invalid. |
| 62980115 | If the image parameter invalid. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { colorSpaceManager } from '@kit.ArkGraphics2D';

4. async function Demo(pixelMap : sendableImage.PixelMap) {
5. let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
6. let csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
7. if (pixelMap != undefined) {
8. pixelMap.setColorSpace(csm);
9. }
10. }
```

### applyColorSpace

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
| Promise<void> | Promise实例，异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980104 | Failed to initialize the internal object. |
| 62980108 | Failed to convert the color space. |
| 62980115 | Invalid image parameter. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { colorSpaceManager } from '@kit.ArkGraphics2D';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function Demo(pixelMap : sendableImage.PixelMap) {
6. let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
7. let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
8. pixelMap.applyColorSpace(targetColorSpace).then(() => {
9. console.info('Succeeded in applying color space for pixelmap object.');
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to apply color space for pixelmap object. code is ${error.code}, message is ${error.message}`);
12. })
13. }
```

### marshalling

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
| 62980097 | IPC error. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { rpc } from '@kit.IPCKit';

5. class MySequence implements rpc.Parcelable {
6. pixel_map: sendableImage.PixelMap;
7. constructor(conPixelMap : sendableImage.PixelMap) {
8. this.pixel_map = conPixelMap;
9. }
10. marshalling(messageSequence : rpc.MessageSequence) {
11. this.pixel_map.marshalling(messageSequence);
12. console.info('marshalling');
13. return true;
14. }
15. unmarshalling(messageSequence : rpc.MessageSequence) {
16. sendableImage.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel: sendableImage.PixelMap) => {
17. pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: sendableImage.PixelMap) => {
18. this.pixel_map = pixelMap;
19. pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
20. console.info("unmarshalling information h:" + imageInfo.size.height + "w:" + imageInfo.size.width);
21. })
22. })
23. });
24. return true;
25. }
26. }

28. async function Demo() {
29. const color: ArrayBuffer = new ArrayBuffer(96);
30. let bufferArr: Uint8Array = new Uint8Array(color);
31. for (let i = 0; i < bufferArr.length; i++) {
32. bufferArr[i] = 0x80;
33. }
34. let opts: image.InitializationOptions = {
35. editable: true,
36. pixelFormat: 4,
37. size: { height: 4, width: 6 },
38. alphaType: 3
39. }
40. let pixelMap: sendableImage.PixelMap | undefined = undefined;
41. await sendableImage.createPixelMap(color, opts).then((srcPixelMap: sendableImage.PixelMap) => {
42. pixelMap = srcPixelMap;
43. })
44. if (pixelMap != undefined) {
45. // 序列化。
46. let parcelable: MySequence = new MySequence(pixelMap);
47. let data: rpc.MessageSequence = rpc.MessageSequence.create();
48. data.writeParcelable(parcelable);

50. // 反序列化rpc获取到data。
51. let ret: MySequence = new MySequence(pixelMap);
52. data.readParcelable(ret);
53. }
54. }
```

### unmarshalling

PhonePC/2in1TabletTVWearable

unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>

从MessageSequence中获取PixelMap。使用Promise异步回调。

如需使用同步方式创建PixelMap可使用：[createPixelMapFromParcel](js-apis-sendableimage.md#sendableimagecreatepixelmapfromparcel)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存有PixelMap信息的MessageSequence。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](js-apis-sendableimage.md#pixelmap)> | Promise实例，用于异步获取结果，失败时返回错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980115 | Invalid image parameter. |
| 62980097 | IPC error. |
| 62980096 | The operation failed. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';
3. import { rpc } from '@kit.IPCKit';

5. class MySequence implements rpc.Parcelable {
6. pixel_map: sendableImage.PixelMap;
7. constructor(conPixelMap: sendableImage.PixelMap) {
8. this.pixel_map = conPixelMap;
9. }
10. marshalling(messageSequence: rpc.MessageSequence) {
11. this.pixel_map.marshalling(messageSequence);
12. console.info('marshalling');
13. return true;
14. }
15. unmarshalling(messageSequence: rpc.MessageSequence) {
16. sendableImage.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel : sendableImage.PixelMap) => {
17. pixelParcel.unmarshalling(messageSequence).then(async (pixelMap : sendableImage.PixelMap) => {
18. this.pixel_map = pixelMap;
19. pixelMap.getImageInfo().then((imageInfo : image.ImageInfo) => {
20. console.info("unmarshalling information h:" + imageInfo.size.height + "w:" + imageInfo.size.width);
21. })
22. })
23. });
24. return true;
25. }
26. }

28. async function Demo() {
29. const color: ArrayBuffer = new ArrayBuffer(96);
30. let bufferArr: Uint8Array = new Uint8Array(color);
31. for (let i = 0; i < bufferArr.length; i++) {
32. bufferArr[i] = 0x80;
33. }
34. let opts: image.InitializationOptions = {
35. editable: true,
36. pixelFormat: 4,
37. size: { height: 4, width: 6 },
38. alphaType: 3
39. }
40. let pixelMap: sendableImage.PixelMap | undefined = undefined;
41. await sendableImage.createPixelMap(color, opts).then((srcPixelMap : sendableImage.PixelMap) => {
42. pixelMap = srcPixelMap;
43. })
44. if (pixelMap != undefined) {
45. // 序列化。
46. let parcelable: MySequence = new MySequence(pixelMap);
47. let data : rpc.MessageSequence = rpc.MessageSequence.create();
48. data.writeParcelable(parcelable);

50. // 反序列化rpc获取到data。
51. let ret : MySequence = new MySequence(pixelMap);
52. data.readParcelable(ret);
53. }
54. }
```

### release

PhonePC/2in1TabletTVWearable

release():Promise<void>

释放PixelMap对象。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，异步返回释放结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sendableImage } from '@kit.ImageKit';

4. async function Demo(pixelMap: sendableImage.PixelMap) {
5. if (pixelMap != undefined) {
6. await pixelMap.release().then(() => {
7. console.info('Succeeded in releasing pixelmap object.');
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}`);
10. })
11. }
12. }
```

## Size

PhonePC/2in1TabletTVWearable

表示图片尺寸。

继承自[lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| height | number | 否 | 否 | 输出图片的高，单位：像素。 |
| width | number | 否 | 否 | 输出图片的宽，单位：像素。 |

## Region

PhonePC/2in1TabletTVWearable

表示区域信息。

继承自[lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [Size](js-apis-sendableimage.md#size) | 否 | 否 | 区域大小。 |
| x | number | 否 | 否 | 区域横坐标。单位：像素。 |
| y | number | 否 | 否 | 区域纵坐标。单位：像素。 |

## sendableImage.createImageSource

PhonePC/2in1TabletTVWearable

createImageSource(uri: string): ImageSource

通过传入的uri创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](js-apis-sendableimage.md#release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 图片路径，当前仅支持应用沙箱路径。  当前支持格式有：.jpg .png .gif .bmp .webp .dng [SVG](arkts-apis-image-f.md#svg标签说明) .ico。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](js-apis-sendableimage.md#imagesource) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo(context : Context) {
4. const path: string = context.cacheDir + "/test.jpg";
5. const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
6. }
```

## sendableImage.createImageSource

PhonePC/2in1TabletTVWearable

createImageSource(fd: number): ImageSource

通过传入文件描述符来创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](js-apis-sendableimage.md#release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符fd。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](js-apis-sendableimage.md#imagesource) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. async function Demo(context : Context) {
5. const path: string = context.cacheDir + "/test.jpg";
6. let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
7. const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(file.fd);
8. }
```

## sendableImage.createImageSource

PhonePC/2in1TabletTVWearable

createImageSource(buf: ArrayBuffer): ImageSource

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用[sendableImage.createPixelMap](js-apis-sendableimage.md#sendableimagecreatepixelmap)这一类方法。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](js-apis-sendableimage.md#release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 图像缓冲区数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](js-apis-sendableimage.md#imagesource) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';

3. async function Demo() {
4. const buf: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(buf);
6. }
```

## sendableImage.createImageReceiver

PhonePC/2in1TabletTVWearable

createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver

通过图片大小、图片格式、容量创建ImageReceiver实例。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](js-apis-sendableimage.md#release-3)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [image.Size](arkts-apis-image-i.md#size) | 是 | 图像的默认大小。 |
| format | [image.ImageFormat](arkts-apis-image-e.md#imageformat9) | 是 | 图像格式，取值为image.ImageFormat常量，目前仅支持 ImageFormat:JPEG。 |
| capacity | number | 是 | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageReceiver](js-apis-sendableimage.md#imagereceiver) | 如果操作成功，则返回ImageReceiver实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';

4. async function Demo() {
5. let size: image.Size = {
6. height: 8192,
7. width: 8
8. }
9. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
10. }
```

## ImageSource

PhonePC/2in1TabletTVWearable

ImageSource类，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过[sendableImage.createImageSource](js-apis-sendableimage.md#sendableimagecreateimagesource)构建一个ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](js-apis-sendableimage.md#release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

### createPixelMap

PhonePC/2in1TabletTVWearable

createPixelMap(options?: image.DecodingOptions): Promise<PixelMap>

通过图片解码参数创建PixelMap对象。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](js-apis-sendableimage.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [image.DecodingOptions](arkts-apis-image-i.md#decodingoptions7) | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](js-apis-sendableimage.md#pixelmap)> | Promise实例，用于异步返回创建结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(context : Context) {
5. const path: string = context.cacheDir + "/test.jpg";
6. const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
7. sendableImageSourceObj.createPixelMap().then((pixelMap: sendableImage.PixelMap) => {
8. console.info('Succeeded in creating pixelMap object through image decoding parameters.');
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to create pixelMap object through image decoding parameters. code ${error.code}, message is ${error.message}`);
11. })
12. }
```

### release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放ImageSource实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，异步返回结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function Demo(context : Context) {
5. const path: string = context.cacheDir + "/test.jpg";
6. const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
7. sendableImageSourceObj.release().then(() => {
8. console.info('Succeeded in releasing the image source instance.');
9. }).catch((error: BusinessError) => {
10. console.error(`Failed to release the image source instance. code ${error.code}, message is ${error.message}`);
11. })
12. }
```

## Image

PhonePC/2in1TabletTVWearable

提供基本的图像操作，包括获取图像信息、读写图像数据。调用[readNextImage](js-apis-sendableimage.md#readnextimage)和[readLatestImage](js-apis-sendableimage.md#readlatestimage)接口时会返回Image。继承自[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用[release](js-apis-sendableimage.md#release-2)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clipRect | [Region](js-apis-sendableimage.md#region) | 否 | 否 | 要裁剪的图像区域。 |
| size | [Size](js-apis-sendableimage.md#size) | 是 | 否 | 图像大小。  如果Image对象所存储的是相机预览流数据（YUV图像数据），那么获取到的size中的宽和高分别对应YUV图像的宽和高。  如果Image对象所存储的是相机拍照流数据（JPEG图像数据），由于已是编码后的文件，size中的宽等于JPEG文件大小，高等于1。  Image对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的是previewOutput还是captureOutput。  相机预览与拍照最佳实践请参考[双路预览(ArkTS)](../harmonyos-guides/camera-dual-channel-preview.md)与[拍照实践(ArkTS)](../harmonyos-guides/camera-shooting-case.md)。 |
| format | number | 是 | 否 | 图像格式，参考[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)。 |
| timestamp | number | 是 | 否 | 图像时间戳。时间戳以纳秒为单位，通常是单调递增的。时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。如果要获取某张照片的生成时间，可以通过[getImageProperty](arkts-apis-image-imagesource.md#getimageproperty11)接口读取相关的EXIF信息。 |

### getComponent

PhonePC/2in1TabletTVWearable

getComponent(componentType: image.ComponentType): Promise<image.Component>

根据图像的组件类型从图像中获取组件缓存。使用Promise异步回调。getComponent是线程不安全的。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| componentType | [image.ComponentType](arkts-apis-image-e.md#componenttype9) | 是 | 图像的组件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.Component](arkts-apis-image-i.md#component9)> | Promise实例，用于异步返回组件缓冲区。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. async function Demo() {
6. let size: image.Size = {
7. height: 8192,
8. width: 8
9. }
10. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
11. let img = await receiver.readNextImage();
12. img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
13. console.info('getComponent succeeded.');
14. }).catch((error: BusinessError) => {
15. console.error(`getComponent failed code ${error.code}, message is ${error.message}`);
16. })
17. }
```

### release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放当前图像。使用Promise异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | promise返回操作结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. async function Demo() {
6. let size: image.Size = {
7. height: 8192,
8. width: 8
9. }
10. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
11. let img = await receiver.readNextImage();
12. img.release().then(() => {
13. console.info('release succeeded.');
14. }).catch((error: BusinessError) => {
15. console.error(`release failed. code ${error.code}, message is ${error.message}`);
16. })
17. }
```

## ImageReceiver

PhonePC/2in1TabletTVWearable

图像接收类，用于获取组件Surface ID，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。

在调用以下方法前需要先创建ImageReceiver实例。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [image.Size](arkts-apis-image-i.md#size) | 是 | 否 | 图片大小。 |
| capacity | number | 是 | 否 | 同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |
| format | [image.ImageFormat](arkts-apis-image-e.md#imageformat9) | 是 | 否 | 图像格式。 |

### getReceivingSurfaceId

PhonePC/2in1TabletTVWearable

getReceivingSurfaceId(): Promise<string>

用于获取一个Surface ID供Camera或其他组件使用。使用promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 异步返回Surface ID。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. async function Demo() {
6. let size: image.Size = {
7. height: 8192,
8. width: 8
9. }
10. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
11. receiver.getReceivingSurfaceId().then((id: string) => {
12. console.info('Succeeded in getting the ReceivingSurfaceId.');
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to get the ReceivingSurfaceId.code ${error.code}, message is ${error.message}`);
15. })
16. }
```

### readLatestImage

PhonePC/2in1TabletTVWearable

readLatestImage(): Promise<Image>

从ImageReceiver读取最新的图片。使用promise异步回调。

注意

此接口需要在[on](js-apis-sendableimage.md#on)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](js-apis-sendableimage.md#image)对象使用完毕后需要调用[release](js-apis-sendableimage.md#release-2)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Image](js-apis-sendableimage.md#image)> | 异步返回最新图片。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. async function Demo() {
6. let size: image.Size = {
7. height: 8192,
8. width: 8
9. }
10. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
11. receiver.readLatestImage().then((img: sendableImage.Image) => {
12. console.info('readLatestImage succeeded.');
13. }).catch((error: BusinessError) => {
14. console.error(`readLatestImage failed. code ${error.code}, message is ${error.message}`);
15. })
16. }
```

### readNextImage

PhonePC/2in1TabletTVWearable

readNextImage(): Promise<Image>

从ImageReceiver读取下一张图片。使用promise异步回调。

注意

此接口需要在[on](js-apis-sendableimage.md#on)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](js-apis-sendableimage.md#image)对象使用完毕后需要调用[release](js-apis-sendableimage.md#release-2)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Image](js-apis-sendableimage.md#image)> | 异步返回下一张图片。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. async function Demo() {
6. let size: image.Size = {
7. height: 8192,
8. width: 8
9. }
10. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
11. receiver.readNextImage().then((img: sendableImage.Image) => {
12. console.info('readNextImage succeeded.');
13. }).catch((error: BusinessError) => {
14. console.error(`readNextImage failed. code ${error.code}, message is ${error.message}`);
15. })
16. }
```

### on

PhonePC/2in1TabletTVWearable

on(type: 'imageArrival', callback: AsyncCallback<void>): void

接收图片时注册。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册事件的类型，固定为'imageArrival'，接收图片时触发。 |
| callback | AsyncCallback<void> | 是 | 注册的事件回调。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { image } from '@kit.ImageKit';

4. async function Demo() {
5. let size: image.Size = {
6. height: 8192,
7. width: 8
8. }
9. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
10. receiver.on('imageArrival', () => {
11. // 接收到图片，实现回调函数逻辑。
12. })
13. }
```

### release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放ImageReceiver实例。使用promise异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异步返回操作结果。 |

**示例：**

```
1. import { sendableImage } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. async function Demo() {
6. let size: image.Size = {
7. height: 8192,
8. width: 8
9. }
10. let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
11. receiver.release().then(() => {
12. console.info('release succeeded.');
13. }).catch((error: BusinessError) => {
14. console.error(`release failed. code ${error.code}, message is ${error.message}`);
15. })
16. }
```
