---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f
title: Functions
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:13:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df0dda51ed1642f10209c4faf35a02474f1ce8b67594c00f921caedc5dba3b0a
---

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## image.createPicture13+

PhonePC/2in1TabletTVWearable

createPicture(mainPixelmap : PixelMap): Picture

通过主图的pixelmap创建一个Picture对象。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-apis-image-picture.md#release13)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mainPixelmap | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 主图的pixelmap。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Picture](arkts-apis-image-picture.md) | 返回Picture对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed. |

**示例：**

```
1. async function CreatePicture(context: Context) {
2. const resourceMgr = context.resourceManager;
3. const rawFile = await resourceMgr.getRawFileContent("test.jpg");
4. let ops: image.SourceOptions = {
5. sourceDensity: 98,
6. }
7. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
8. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
9. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
10. if (pictureObj != null) {
11. console.info('Create picture succeeded');
12. } else {
13. console.error('Create picture failed');
14. }
15. }
```

## image.createPictureFromParcel13+

PhonePC/2in1TabletTVWearable

createPictureFromParcel(sequence: rpc.MessageSequence): Picture

从MessageSequence中获取Picture。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-apis-image-picture.md#release13)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存有Picture信息的MessageSequence。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Picture](arkts-apis-image-picture.md) | 返回Picture对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

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

30. async function Marshalling_UnMarshalling(context: Context) {
31. const resourceMgr = context.resourceManager;
32. const rawFile = await resourceMgr.getRawFileContent("test.jpg");
33. let ops: image.SourceOptions = {
34. sourceDensity: 98,
35. }
36. let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
37. let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
38. let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
39. if (pictureObj != null) {
40. let parcelable: MySequence = new MySequence(pictureObj);
41. let data: rpc.MessageSequence = rpc.MessageSequence.create();
42. // 序列化。
43. data.writeParcelable(parcelable);
44. let ret: MySequence = new MySequence(pictureObj);
45. // 反序列化。
46. data.readParcelable(ret);
47. } else {
48. console.error('PictureObj is null');
49. }
50. }
```

## image.createPixelMap8+

PhonePC/2in1TabletTVWearable

createPixelMap(colors: ArrayBuffer, options: InitializationOptions): Promise<PixelMap>

通过像素数据和图像属性创建PixelMap，传入的像素数据默认按BGRA\_8888格式解析。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | 图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](arkts-apis-image-i.md#initializationoptions8).srcPixelFormat指定，否则默认缓冲区的像素格式为BGRA\_8888。  **说明：** 图像像素数据的缓冲区长度：length = width \* height \* 单位像素字节数。 |
| options | [InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。  当创建的pixelMap大小超过原图大小时，返回原图pixelMap大小。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMap() {
4. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let opts: image.InitializationOptions = {
6. size: { height: 4, width: 6 },
7. srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
8. pixelFormat: image.PixelMapFormat.RGBA_8888, // 新创建的PixelMap的像素格式。
9. editable: true
10. };
11. image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
12. console.info('Succeeded in creating pixelmap.');
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
15. })
16. }
```

## image.createPixelMap8+

PhonePC/2in1TabletTVWearable

createPixelMap(colors: ArrayBuffer, options: InitializationOptions, callback: AsyncCallback<PixelMap>): void

通过像素数据和图像属性创建PixelMap，传入的像素数据默认按BGRA\_8888格式解析。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | 图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](arkts-apis-image-i.md#initializationoptions8).srcPixelFormat指定，否则默认缓冲区的像素格式为BGRA\_8888。  **说明：** 图像像素数据的缓冲区长度：length = width \* height \* 单位像素字节数。 |
| options | [InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。 |
| callback | AsyncCallback<[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数，当创建PixelMap成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMap() {
4. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let opts: image.InitializationOptions = {
6. size: { height: 4, width: 6 },
7. srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
8. pixelFormat: image.PixelMapFormat.RGBA_8888, // 新创建的PixelMap的像素格式。
9. editable: true
10. };
11. image.createPixelMap(color, opts, (error: BusinessError, pixelMap: image.PixelMap) => {
12. if(error) {
13. console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
14. return;
15. } else {
16. console.info('Succeeded in creating pixelmap.');
17. }
18. })
19. }
```

## image.createPixelMapUsingAllocator20+

PhonePC/2in1TabletTVWearable

createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>

通过属性创建以及指定内存类型创建PixelMap，默认采用BGRA\_8888格式处理数据。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | 图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，必须通过[InitializationOptions](arkts-apis-image-i.md#initializationoptions8).srcPixelFormat指定缓冲区中的像素格式。  **说明：** 图像像素数据的缓冲区长度：length = width \* height \* 单位像素字节数。 |
| param | [InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。 |
| allocatorType | [AllocatorType](arkts-apis-image-e.md#allocatortype15) | 否 | 指定创建pixelmap的内存类型，默认内存类型是AllocatorType.AUTO。  1. image.AllocatorType.AUTO：不支持该内存类型的格式有UNKNOWN、YCBCR\_P010、YCRCB\_P010和ASTC\_4x4。RGBA\_1010102默认申请DMA内存。其他格式（RGB\_565、RGBA\_8888、BGRA\_8888和RGBAF\_16）尺寸大于512\*512默认申请DMA内存，否则申请共享内存。  2. image.AllocatorType.DMA：RGBA\_1010102、RGB\_565、RGBA\_8888、BGRA\_8888和RGBAF\_16支持DMA内存类型，其余格式不支持。  3. image.AllocatorType.SHARED：UNKNOWN、RGBA\_1010102、YCBCR\_P010、YCRCB\_P010和ASTC\_4x4不支持共享内存，其余格式支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | Unsupported operation. |
| 7600301 | Memory alloc failed. |
| 7600302 | Memory copy failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMapUseAllocator() {
4. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
5. let opts: image.InitializationOptions = {
6. size: { height: 4, width: 6 },
7. srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
8. pixelFormat: image.PixelMapFormat.RGBA_8888, // 新创建的PixelMap的像素格式。
9. editable: true
10. };
11. image.createPixelMapUsingAllocator(color, opts, image.AllocatorType.AUTO).then((pixelMap: image.PixelMap) => {
12. console.info('Succeeded in creating pixelmap.');
13. }).catch((error: BusinessError) => {
14. console.error("Failed to create pixelmap. code is ", error.code);
15. })
16. }
```

## image.createPixelMapFromParcel11+

PhonePC/2in1TabletTVWearable

createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap

从MessageSequence中获取PixelMap。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 保存有PixelMap信息的MessageSequence。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |
| 62980115 | Invalid input parameter. |
| 62980105 | Failed to get the data. |
| 62980177 | Abnormal API environment. |
| 62980178 | Failed to create the PixelMap. |
| 62980179 | Abnormal buffer size. |
| 62980180 | FD mapping failed. Possible cause: 1. Size and address does not match. 2. Memory map in memalloc failed. |
| 62980246 | Failed to read the PixelMap. |

**示例：**

```
1. import { rpc } from '@kit.IPCKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class MySequence implements rpc.Parcelable {
5. pixel_map: image.PixelMap;
6. constructor(conPixelmap: image.PixelMap) {
7. this.pixel_map = conPixelmap;
8. }
9. marshalling(messageSequence: rpc.MessageSequence) {
10. this.pixel_map.marshalling(messageSequence);
11. return true;
12. }
13. unmarshalling(messageSequence: rpc.MessageSequence) {
14. try {
15. this.pixel_map = image.createPixelMapFromParcel(messageSequence);
16. } catch(e) {
17. let error = e as BusinessError;
18. console.error(`createPixelMapFromParcel error. code is ${error.code}, message is ${error.message}`);
19. return false;
20. }
21. return true;
22. }
23. }
24. async function CreatePixelMapFromParcel() {
25. const color: ArrayBuffer = new ArrayBuffer(96);
26. let bufferArr: Uint8Array = new Uint8Array(color);
27. for (let i = 0; i < bufferArr.length; i++) {
28. bufferArr[i] = 0x80;
29. }
30. let opts: image.InitializationOptions = {
31. editable: true,
32. pixelFormat: image.PixelMapFormat.BGRA_8888,
33. size: { height: 4, width: 6 },
34. alphaType: image.AlphaType.UNPREMUL
35. }
36. let pixelMap: image.PixelMap | undefined = undefined;
37. await image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
38. pixelMap = srcPixelMap;
39. })
40. if (pixelMap != undefined) {
41. // 序列化。
42. let parcelable: MySequence = new MySequence(pixelMap);
43. let data: rpc.MessageSequence = rpc.MessageSequence.create();
44. data.writeParcelable(parcelable);

46. // 反序列化rpc获取到data。
47. let ret: MySequence = new MySequence(pixelMap);
48. data.readParcelable(ret);

50. // 获取到pixelmap。
51. let newPixelmap = ret.pixel_map;
52. }
53. }
```

## image.createPixelMapFromSurface11+

PhonePC/2in1TabletTVWearable

createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>

根据Surface ID和区域信息创建一个PixelMap对象。该区域的大小由[Region](arkts-apis-image-i.md#region8).size指定。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

说明

当设备为折叠屏，且折叠状态切换时，可能因Surface自带旋转角度导致接口创建失败。需将宽高适配旋转角度。推荐使用[image.createPixelMapFromSurface](arkts-apis-image-f.md#imagecreatepixelmapfromsurface15)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 对应Surface的ID，可通过预览组件获取，如[XComponent](ts-basic-components-xcomponent.md)组件。 |
| region | [Region](arkts-apis-image-i.md#region8) | 是 | 截取的画面区域。仅支持从画面左上角开始截取部分或整个画面，即Region中的x和y必须为0，Region.size中width和height的取值范围分别为[1, 预览流宽度]和[1, 预览流高度]。如需截取任意区域，可先使用[image.createPixelMapFromSurface](arkts-apis-image-f.md#imagecreatepixelmapfromsurface15)获取整个画面，再使用[crop](arkts-apis-image-pixelmap.md#crop9)截取所需区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980115 | If the image parameter invalid. |
| 62980105 | Failed to get the data. |
| 62980178 | Failed to create the PixelMap. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMapFromSurface(surfaceId: string) {
4. let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
5. image.createPixelMapFromSurface(surfaceId, region).then(() => {
6. console.info('Succeeded in creating pixelmap from Surface');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
9. });
10. }
```

## image.createPixelMapFromSurfaceSync12+

PhonePC/2in1TabletTVWearable

createPixelMapFromSurfaceSync(surfaceId: string, region: Region): PixelMap

以同步方式，根据Surface ID和区域信息创建一个PixelMap对象。该区域的大小由[Region](arkts-apis-image-i.md#region8).size指定。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

说明

当设备为折叠屏，且折叠状态切换时，可能因Surface自带旋转角度导致接口创建失败。需将宽高适配旋转角度。推荐使用[image.createPixelMapFromSurfaceSync](arkts-apis-image-f.md#imagecreatepixelmapfromsurfacesync15)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 对应Surface的ID，可通过预览组件获取，如[XComponent](ts-basic-components-xcomponent.md)组件。 |
| region | [Region](arkts-apis-image-i.md#region8) | 是 | 截取的画面区域。仅支持从画面左上角开始截取部分或整个画面，即Region中的x和y必须为0，Region.size中width和height的取值范围分别为[1, 预览流宽度]和[1, 预览流高度]。如需截取任意区域，可先使用[image.createPixelMapFromSurfaceSync](arkts-apis-image-f.md#imagecreatepixelmapfromsurfacesync15)获取整个画面，再使用[cropSync](arkts-apis-image-pixelmap.md#cropsync12)截取所需区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980105 | Failed to get the data. |
| 62980178 | Failed to create the PixelMap. |

**示例：**

```
1. async function Demo(surfaceId: string) {
2. let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
3. let pixelMap: image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region);
4. return pixelMap;
5. }
```

## image.createPixelMapFromSurface15+

PhonePC/2in1TabletTVWearable

createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>

从Surface ID创建一个PixelMap对象。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 对应Surface的ID，可通过预览组件获取，如[XComponent](ts-basic-components-xcomponent.md)组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980105 | Failed to get the data |
| 62980178 | Failed to create the PixelMap |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePixelMapFromSurface(surfaceId: string) {
4. image.createPixelMapFromSurface(surfaceId).then(() => {
5. console.info('Succeeded in creating pixelmap from Surface');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
8. });
9. }
```

## image.createPixelMapFromSurfaceSync15+

PhonePC/2in1TabletTVWearable

createPixelMapFromSurfaceSync(surfaceId: string): PixelMap

从Surface ID创建一个PixelMap对象，同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 对应Surface的ID，可通过预览组件获取，如[XComponent](ts-basic-components-xcomponent.md)组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980105 | Failed to get the data |
| 62980178 | Failed to create the PixelMap |

**示例：**

```
1. async function CreatePixelMapFromSurfaceSync(surfaceId: string) {
2. let pixelMap : image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId);
3. return pixelMap;
4. }
```

## image.createPixelMapFromSurfaceWithTransformation23+

PhonePC/2in1TabletTVWearable

createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>

通过Surface的ID创建一个预览流画面的PixelMap对象。该Surface可能携带旋转或翻转的变换信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 对应Surface的ID，可通过预览组件获取，如[XComponent](ts-basic-components-xcomponent.md)组件。 |
| transformEnabled | boolean | 是 | 是否对携带变换信息的Surface预先进行逆变换来消除PixelMap的旋转或翻转效果。若Surface未携带变换信息，本参数不生效。  true：进行逆变换，变换的角度与Surface携带的角度一致且方向相反，输出的PixelMap无旋转或翻转效果。  false：不进行逆变换，输出的PixelMap会根据Surface中的变换信息而带有旋转或翻转效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600104 | Failed to get the data from Surface. |
| 7600201 | Unsupported operation, e.g. on cross-platform. |
| 7600206 | Invalid parameter. |
| 7600305 | Failed to create the PixelMap. |

**示例：**

```
1. function DemoCreatePixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean) {
2. image.createPixelMapFromSurfaceWithTransformation(surfaceId, transformEnabled).then((pixelMap: image.PixelMap) => {
3. console.info('PixelMap created successfully.');
4. }).catch((e: Error) => {
5. console.error(`Failed to create PixelMap. Code: ${e}`);
6. });
7. }
```

## image.createPixelMapFromSurfaceWithTransformationSync23+

PhonePC/2in1TabletTVWearable

createPixelMapFromSurfaceWithTransformationSync(surfaceId: string, transformEnabled: boolean): PixelMap

通过Surface的ID创建一个预览流画面的PixelMap对象。该Surface可能携带旋转或翻转的变换信息。同步返回PixelMap结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 对应Surface的ID，可通过预览组件获取，如[XComponent](ts-basic-components-xcomponent.md)组件。 |
| transformEnabled | boolean | 是 | 是否对携带变换信息的Surface预先进行逆变换来消除PixelMap的旋转或翻转效果。若Surface未携带变换信息，本参数不生效。  true：进行逆变换，变换的角度与Surface携带的角度一致且方向相反，输出的PixelMap无旋转或翻转效果。  false：不进行逆变换，输出的PixelMap会根据Surface中的变换信息而带有旋转或翻转效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功会同步返回PixelMap对象，失败则抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600104 | Failed to get the data from Surface. |
| 7600201 | Unsupported operation, e.g. on cross-platform. |
| 7600206 | Invalid parameter. |
| 7600305 | Failed to create the PixelMap. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function DemoCreatePixelMapFromSurfaceWithTransformationSync(surfaceId: string, transformEnabled: boolean) {
4. try {
5. const pixelMap: image.PixelMap = image.createPixelMapFromSurfaceWithTransformationSync(surfaceId, transformEnabled);
6. console.info('PixelMap created successfully.');
7. } catch (e) {
8. const error = e as BusinessError;
9. console.error(`Failed to create PixelMap. Code: ${error.code}, message: ${error.message}`);
10. }
11. }
```

## image.createPixelMapSync12+

PhonePC/2in1TabletTVWearable

createPixelMapSync(colors: ArrayBuffer, options: InitializationOptions): PixelMap

通过像素数据和图像属性创建PixelMap，传入的像素数据默认按BGRA\_8888格式解析。同步返回结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | 图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](arkts-apis-image-i.md#initializationoptions8).srcPixelFormat指定，否则默认缓冲区的像素格式为BGRA\_8888。  **说明：** 图像像素数据的缓冲区长度：length = width \* height \* 单位像素字节数。 |
| options | [InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |

**示例：**

```
1. function CreatePixelMapSync() {
2. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
3. let opts: image.InitializationOptions = {
4. size: { height: 4, width: 6 },
5. srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
6. pixelFormat: image.PixelMapFormat.RGBA_8888, // 新创建的PixelMap的像素格式。
7. editable: true
8. };
9. let pixelMap : image.PixelMap = image.createPixelMapSync(color, opts);
10. return pixelMap;
11. }
```

## image.createPixelMapSync12+

PhonePC/2in1TabletTVWearable

createPixelMapSync(options: InitializationOptions): PixelMap

通过图像属性创建空白PixelMap，同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |

**示例：**

```
1. function CreatePixelMapSync() {
2. let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
3. let pixelMap : image.PixelMap = image.createPixelMapSync(opts);
4. return pixelMap;
5. }
```

## image.createPixelMapUsingAllocatorSync20+

PhonePC/2in1TabletTVWearable

createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): PixelMap

通过像素数据和图像属性创建PixelMap，可以指定内存类型。同步返回结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | 图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，必须通过[InitializationOptions](arkts-apis-image-i.md#initializationoptions8).srcPixelFormat指定缓冲区中的像素格式。  **说明：** 图像像素数据的缓冲区长度：length = width \* height \* 单位像素字节数。 |
| param | [InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。 |
| allocatorType | [AllocatorType](arkts-apis-image-e.md#allocatortype15) | 否 | 指定创建pixelmap的内存类型，默认内存类型是AllocatorType.AUTO。  1. image.AllocatorType.AUTO：不支持该内存类型的格式有UNKNOWN、YCBCR\_P010、YCRCB\_P010和ASTC\_4x4。RGBA\_1010102默认申请DMA内存。其他格式（RGB\_565、RGBA\_8888、BGRA\_8888和RGBAF\_16）尺寸大于512\*512默认申请DMA内存，否则申请共享内存。  2. image.AllocatorType.DMA：RGBA\_1010102、RGB\_565、RGBA\_8888、BGRA\_8888和RGBAF\_16支持DMA内存类型，其余格式不支持。  3. image.AllocatorType.SHARED：UNKNOWN、RGBA\_1010102、YCBCR\_P010、YCRCB\_P010和ASTC\_4x4不支持共享内存，其余格式支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | Unsupported operation. |
| 7600301 | Memory alloc failed. |
| 7600302 | Memory copy failed. |

**示例：**

```
1. function CreatePixelMapSync() {
2. const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
3. let opts: image.InitializationOptions = {
4. size: { height: 4, width: 6 },
5. srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
6. pixelFormat: image.PixelMapFormat.RGBA_8888, // 新创建的PixelMap的像素格式。
7. editable: true
8. };
9. let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(color, opts, image.AllocatorType.AUTO);
10. return pixelMap;
11. }
```

## image.createPixelMapUsingAllocatorSync20+

PhonePC/2in1TabletTVWearable

createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap

通过图像属性创建空白PixelMap，可以指定内存类型。同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [InitializationOptions](arkts-apis-image-i.md#initializationoptions8) | 是 | 创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。 |
| allocatorType | [AllocatorType](arkts-apis-image-e.md#allocatortype15) | 否 | 指定创建pixelmap的内存类型，默认内存类型是AllocatorType.AUTO。  1. image.AllocatorType.AUTO：不支持该内存类型的格式有UNKNOWN和ASTC\_4x4。RGBA\_1010102、YCBCR\_P010、YCRCB\_P010格式默认申请DMA内存。其他格式（RGB\_565, RGBA\_8888, BGRA\_8888, RGBAF\_16）尺寸大于512\*512默认申请DMA内存，否则申请共享内存。  2. image.AllocatorType.DMA：RGB\_565、RGBA\_8888、BGRA\_8888、RGBAF\_16、RGBA\_1010102、YCBCR\_P010和YCRCB\_P010支持DMA内存类型，其余格式不支持。  3. image.AllocatorType.SHARED：UNKNOWN、RGBA\_1010102、YCBCR\_P010、YCRCB\_P010和ASTC\_4x4不支持共享内存，其余格式支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 成功同步返回PixelMap对象，失败抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | Unsupported operation. |
| 7600301 | Memory alloc failed. |

**示例：**

```
1. function CreatePixelMapSync() {
2. let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
3. let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(opts, image.AllocatorType.AUTO);
4. return pixelMap;
5. }
```

## image.createPremultipliedPixelMap12+

PhonePC/2in1TabletTVWearable

createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void

将PixelMap的透明通道非预乘模式转变为预乘模式，转换后的数据存入目标PixelMap。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 源PixelMap对象。 |
| dst | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 目标PixelMap对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当创建PixelMap成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980103 | The image data is not supported |
| 62980246 | Failed to read the pixelMap |
| 62980248 | Pixelmap not allow modify |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePremultipliedPixelMap() {
4. const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
5. let bufferArr = new Uint8Array(color);
6. for (let i = 0; i < bufferArr.length; i += 4) {
7. bufferArr[i] = 255;
8. bufferArr[i+1] = 255;
9. bufferArr[i+2] = 122;
10. bufferArr[i+3] = 122;
11. }
12. let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
13. let srcPixelmap = image.createPixelMapSync(color, optsForUnpre);
14. let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
15. let dstPixelMap = image.createPixelMapSync(optsForPre);
16. image.createPremultipliedPixelMap(srcPixelmap, dstPixelMap, (error: BusinessError) => {
17. if(error) {
18. console.error(`Failed to convert pixelmap, error code is ${error}`);
19. return;
20. } else {
21. console.info('Succeeded in converting pixelmap.');
22. }
23. })
24. }
```

## image.createPremultipliedPixelMap12+

PhonePC/2in1TabletTVWearable

createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>

将PixelMap数据按照透明度非预乘格式转为预乘格式，转换后的数据存入另一个PixelMap。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 源PixelMap对象。 |
| dst | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 目标PixelMap对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980103 | The image data is not supported |
| 62980246 | Failed to read the pixelMap |
| 62980248 | Pixelmap not allow modify |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreatePremultipliedPixelMap() {
4. const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
5. let bufferArr = new Uint8Array(color);
6. for (let i = 0; i < bufferArr.length; i += 4) {
7. bufferArr[i] = 255;
8. bufferArr[i+1] = 255;
9. bufferArr[i+2] = 122;
10. bufferArr[i+3] = 122;
11. }
12. let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
13. let srcPixelmap = image.createPixelMapSync(color, optsForUnpre);
14. let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
15. let dstPixelMap = image.createPixelMapSync(optsForPre);
16. image.createPremultipliedPixelMap(srcPixelmap, dstPixelMap).then(() => {
17. console.info('Succeeded in converting pixelmap.');
18. }).catch((error: BusinessError) => {
19. console.error(`Failed to convert pixelmap, error code is ${error}`);
20. })
21. }
```

## image.createUnpremultipliedPixelMap12+

PhonePC/2in1TabletTVWearable

createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void

将PixelMap的透明通道预乘模式转变为非预乘模式，转换后的数据存入目标PixelMap。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 源PixelMap对象。 |
| dst | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 目标PixelMap对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当创建PixelMap成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980103 | The image data is not supported |
| 62980246 | Failed to read the pixelMap |
| 62980248 | Pixelmap not allow modify |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreateUnpremultipliedPixelMap() {
4. const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
5. let bufferArr = new Uint8Array(color);
6. for (let i = 0; i < bufferArr.length; i += 4) {
7. bufferArr[i] = 255;
8. bufferArr[i+1] = 255;
9. bufferArr[i+2] = 122;
10. bufferArr[i+3] = 122;
11. }
12. let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
13. let srcPixelmap = image.createPixelMapSync(color, optsForPre);
14. let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
15. let dstPixelMap = image.createPixelMapSync(optsForUnpre);
16. image.createUnpremultipliedPixelMap(srcPixelmap, dstPixelMap, (error: BusinessError) => {
17. if(error) {
18. console.error(`Failed to convert pixelmap, error code is ${error}`);
19. return;
20. } else {
21. console.info('Succeeded in converting pixelmap.');
22. }
23. })
24. }
```

## image.createUnpremultipliedPixelMap12+

PhonePC/2in1TabletTVWearable

createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>

将PixelMap的透明通道预乘模式转变为非预乘模式，转换后的数据存入目标PixelMap。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-apis-image-pixelmap.md#release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 源PixelMap对象。 |
| dst | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 目标PixelMap对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980103 | The image data is not supported. |
| 62980246 | Failed to read the pixelMap. |
| 62980248 | Pixelmap not allow modify. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreateUnpremultipliedPixelMap() {
4. const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
5. let bufferArr = new Uint8Array(color);
6. for (let i = 0; i < bufferArr.length; i += 4) {
7. bufferArr[i] = 255;
8. bufferArr[i+1] = 255;
9. bufferArr[i+2] = 122;
10. bufferArr[i+3] = 122;
11. }
12. let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
13. let srcPixelmap = image.createPixelMapSync(color, optsForPre);
14. let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
15. let dstPixelMap = image.createPixelMapSync(optsForUnpre);
16. image.createUnpremultipliedPixelMap(srcPixelmap, dstPixelMap).then(() => {
17. console.info('Succeeded in converting pixelmap.');
18. }).catch((error: BusinessError) => {
19. console.error(`Failed to convert pixelmap, error code is ${error}`);
20. })
21. }
```

## image.createImageSource

PhonePC/2in1TabletTVWearable

createImageSource(uri: string): ImageSource

通过传入的uri创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 图片路径，当前仅支持应用沙箱路径。  当前支持格式有：.jpg .png .gif .bmp .webp .dng .heic12+ .wbmp23+ .heifs23+ .tiff23+ [.svg10+](arkts-apis-image-f.md#svg标签说明) .ico11+。部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats20+](arkts-apis-image-f.md#imagegetimagesourcesupportedformats20)接口，动态查询当前设备上的解码能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. async function CreateImageSource(context : Context) {
2. // 此处'test.jpg'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
3. const path: string = context.filesDir + "/test.jpg";
4. const imageSourceObj: image.ImageSource = image.createImageSource(path);
5. }
```

## image.createImageSource9+

PhonePC/2in1TabletTVWearable

createImageSource(uri: string, options: SourceOptions): ImageSource

通过传入的uri创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 图片路径，当前仅支持应用沙箱路径。  当前支持格式有：.jpg .png .gif .bmp .webp .dng .heic12+ .wbmp23+ .heifs23+ .tiff23+ [.svg10+](arkts-apis-image-f.md#svg标签说明) .ico11+。部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats20+](arkts-apis-image-f.md#imagegetimagesourcesupportedformats20)接口，动态查询当前设备上的解码能力。 |
| options | [SourceOptions](arkts-apis-image-i.md#sourceoptions9) | 是 | 图片属性，包括图片像素密度、像素格式和图片尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. async function CreateImageSource(context : Context) {
2. let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
3. // 此处'test.png'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
4. const path: string = context.filesDir + "/test.png";
5. let imageSourceObj: image.ImageSource = image.createImageSource(path, sourceOptions);
6. }
```

## image.createImageSource7+

PhonePC/2in1TabletTVWearable

createImageSource(fd: number): ImageSource

通过传入文件描述符来创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符fd。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. async function CreateImageSource(context : Context) {
4. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
5. let filePath: string = context.filesDir + "/test.jpg";
6. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
7. const imageSourceObj: image.ImageSource = image.createImageSource(file.fd);
8. }
```

## image.createImageSource9+

PhonePC/2in1TabletTVWearable

createImageSource(fd: number, options: SourceOptions): ImageSource

通过传入文件描述符来创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符fd。 |
| options | [SourceOptions](arkts-apis-image-i.md#sourceoptions9) | 是 | 图片属性，包括图片像素密度、像素格式和图片尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. async function CreateImageSource(context : Context) {
4. let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
5. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
6. const filePath: string = context.filesDir + "/test.jpg";
7. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
8. const imageSourceObj: image.ImageSource = image.createImageSource(file.fd, sourceOptions);
9. }
```

## image.createImageSource9+

PhonePC/2in1TabletTVWearable

createImageSource(buf: ArrayBuffer): ImageSource

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用[image.createPixelMapSync](arkts-apis-image-f.md#imagecreatepixelmapsync12)这一类接口。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 图像缓冲区数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. async function CreateImageSource() {
2. const buf: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
3. const imageSourceObj: image.ImageSource = image.createImageSource(buf);
4. }
```

## image.createImageSource9+

PhonePC/2in1TabletTVWearable

createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用[image.createPixelMapSync](arkts-apis-image-f.md#imagecreatepixelmapsync12)这一类接口。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 图像缓冲区数组。 |
| options | [SourceOptions](arkts-apis-image-i.md#sourceoptions9) | 是 | 图片属性，包括图片像素密度、像素格式和图片尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. async function CreateImageSource() {
2. const data: ArrayBuffer = new ArrayBuffer(112);
3. let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
4. const imageSourceObj: image.ImageSource = image.createImageSource(data, sourceOptions);
5. }
```

## image.createImageSource11+

PhonePC/2in1TabletTVWearable

createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource

通过图像资源文件的RawFileDescriptor创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rawfile | [resourceManager.RawFileDescriptor](js-apis-resource-manager.md#rawfiledescriptor9) | 是 | 图像资源文件的RawFileDescriptor。 |
| options | [SourceOptions](arkts-apis-image-i.md#sourceoptions9) | 否 | 图片属性，包括图片像素密度、像素格式和图片尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource类实例，失败时返回undefined。 |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function CreateImageSource(context : Context) {
5. // 获取resourceManager资源管理器。
6. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
7. // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
8. resourceMgr.getRawFd('test.jpg').then((rawFileDescriptor: resourceManager.RawFileDescriptor) => {
9. const imageSourceObj: image.ImageSource = image.createImageSource(rawFileDescriptor);
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to get RawFileDescriptor.code is ${error.code}, message is ${error.message}`);
12. })
13. }
```

## image.CreateIncrementalSource9+

PhonePC/2in1TabletTVWearable

CreateIncrementalSource(buf: ArrayBuffer): ImageSource

通过缓冲区以增量的方式创建ImageSource实例，IncrementalSource不支持读写Exif信息。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

以增量方式创建的ImageSource实例，仅支持使用以下功能，同步、异步callback、异步Promise均支持。

* 获取图片信息：指定序号-[getImageInfo](arkts-apis-image-imagesource.md#getimageinfo)、直接获取-[getImageInfo](arkts-apis-image-imagesource.md#getimageinfo-1)
* 获取图片中给定索引处图像的指定属性键的值：[getImageProperty](arkts-apis-image-imagesource.md#getimageproperty11)
* 批量获取图片中的指定属性键的值：[getImageProperties](arkts-apis-image-imagesource.md#getimageproperties12)
* 更新增量数据：[updateData](arkts-apis-image-imagesource.md#updatedata9)
* 创建PixelMap对象：通过图片解码参数创建-[createPixelMap](arkts-apis-image-imagesource.md#createpixelmap7)、通过默认参数创建-[createPixelMap](arkts-apis-image-imagesource.md#createpixelmap7-1) 、通过图片解码参数-[createPixelMap](arkts-apis-image-imagesource.md#createpixelmap7-2)
* 释放ImageSource实例：[release](arkts-apis-image-imagesource.md#release)

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 增量数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource，失败时返回undefined。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreateIncrementalImageSource(context : Context) {
4. let imageArray = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id); // 获取图像资源。
5. // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageArray创建失败会导致后续无法正常执行。
6. let splitBuff1 = imageArray.slice(0, imageArray.byteLength / 2);  // 分片。
7. let splitBuff2 = imageArray.slice(imageArray.byteLength / 2);
8. const imageSourceIncrementalSApi: image.ImageSource = image.CreateIncrementalSource(new ArrayBuffer(imageArray.byteLength));
9. imageSourceIncrementalSApi.updateData(splitBuff1, false, 0, splitBuff1.byteLength).then(() => {
10. imageSourceIncrementalSApi.updateData(splitBuff2, true, 0, splitBuff2.byteLength).then(() => {
11. let pixelMap = imageSourceIncrementalSApi.createPixelMapSync();
12. let imageInfo = pixelMap.getImageInfoSync();
13. console.info('Succeeded in creating pixelMap');
14. }).catch((error : BusinessError) => {
15. console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
16. })
17. }).catch((error : BusinessError) => {
18. console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
19. })
20. }
```

## image.CreateIncrementalSource9+

PhonePC/2in1TabletTVWearable

CreateIncrementalSource(buf: ArrayBuffer, options?: SourceOptions): ImageSource

通过缓冲区以增量的方式创建ImageSource实例，IncrementalSource不支持读写Exif信息。

此接口支持的功能与[CreateIncrementalSource(buf: ArrayBuffer): ImageSource](arkts-apis-image-f.md#imagecreateincrementalsource9)所生成的实例支持的功能相同。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-apis-image-imagesource.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 增量数据。 |
| options | [SourceOptions](arkts-apis-image-i.md#sourceoptions9) | 否 | 图片属性，包括图片像素密度、像素格式和图片尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageSource](arkts-apis-image-imagesource.md) | 返回ImageSource，失败时返回undefined。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function CreateIncrementalImageSource(context : Context) {
4. let imageArray = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id); // 获取图像资源。
5. // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageArray创建失败会导致后续无法正常执行。
6. let splitBuff1 = imageArray.slice(0, imageArray.byteLength / 2);  // 分片。
7. let splitBuff2 = imageArray.slice(imageArray.byteLength / 2);
8. let sourceOptions: image.SourceOptions = { sourceDensity: 120};

10. const imageSourceIncrementalSApi: image.ImageSource = image.CreateIncrementalSource(new ArrayBuffer(imageArray.byteLength), sourceOptions);
11. imageSourceIncrementalSApi.updateData(splitBuff1, false, 0, splitBuff1.byteLength).then(() => {
12. imageSourceIncrementalSApi.updateData(splitBuff2, true, 0, splitBuff2.byteLength).then(() => {
13. let pixelMap = imageSourceIncrementalSApi.createPixelMapSync();
14. let imageInfo = pixelMap.getImageInfoSync();
15. console.info('Succeeded in creating pixelMap');
16. }).catch((error : BusinessError) => {
17. console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
18. })
19. }).catch((error : BusinessError) => {
20. console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
21. })
22. }
```

## image.getImageSourceSupportedFormats20+

PhonePC/2in1TabletTVWearable

getImageSourceSupportedFormats(): string[]

获取支持解码的图片格式，图片格式以mime type表示。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持解码的图片格式（mime type）列表。 |

**示例：**

```
1. async function GetImageSourceSupportedFormats() {
2. let formats = image.getImageSourceSupportedFormats();
3. console.info('formats:', formats);
4. }

6. async function IsSupportedTiffFormat() {
7. let formats = image.getImageSourceSupportedFormats();
8. return formats.includes("image/tiff");
9. }
```

## image.createImagePacker

PhonePC/2in1TabletTVWearable

createImagePacker(): ImagePacker

创建ImagePacker实例。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](arkts-apis-image-imagepacker.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImagePacker](arkts-apis-image-imagepacker.md) | 返回ImagePacker实例。 |

**示例：**

```
1. async function CreateImagePacker() {
2. const imagePackerObj: image.ImagePacker = image.createImagePacker();
3. }
```

## image.getImagePackerSupportedFormats20+

PhonePC/2in1TabletTVWearable

getImagePackerSupportedFormats(): string[]

获取支持编码的图片格式，图片格式以mime type表示。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持编码的图片格式（mime type）列表。 |

**示例：**

```
1. async function GetImagePackerSupportedFormats() {
2. let formats = image.getImagePackerSupportedFormats();
3. console.info('formats:', formats);
4. }
```

## image.createAuxiliaryPicture13+

PhonePC/2in1TabletTVWearable

createAuxiliaryPicture(buffer: ArrayBuffer, size: Size, type: AuxiliaryPictureType): AuxiliaryPicture

通过ArrayBuffer图片数据、辅助图尺寸、辅助图类型创建AuxiliaryPicture实例。该接口仅支持传入BGRA的连续像素数据，会创建出RGBA的辅助图。

由于图片占用内存较大，所以当AuxiliaryPicture实例使用完成后，应主动调用[release](arkts-apis-image-auxiliarypicture.md#release13)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 以buffer形式存放的图像数据。 |
| size | [Size](arkts-apis-image-i.md#size) | 是 | 辅助图的尺寸。单位：像素。 |
| type | [AuxiliaryPictureType](arkts-apis-image-e.md#auxiliarypicturetype13) | 是 | 辅助图类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuxiliaryPicture](arkts-apis-image-auxiliarypicture.md) | 如果操作成功，则返回AuxiliaryPicture实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. async function CreateAuxiliaryPicture(context: Context) {
2. let funcName = "CreateAuxiliaryPicture";
3. const resourceMgr = context.resourceManager;
4. const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // 需要支持hdr的图片。
5. let auxBuffer: ArrayBuffer = rawFile.buffer as ArrayBuffer;
6. let auxSize: Size = {
7. height: 180,
8. width: 240
9. };
10. let auxType: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
11. let auxPictureObj: image.AuxiliaryPicture | null = image.createAuxiliaryPicture(auxBuffer, auxSize, auxType);
12. if(auxPictureObj != null) {
13. let type: image.AuxiliaryPictureType = auxPictureObj.getType();
14. console.info(funcName, `CreateAuxiliaryPicture succeeded this.Aux_picture.type ${type}`);
15. } else {
16. console.error(funcName, 'CreateAuxiliaryPicture failed');
17. }
18. }
```

## image.createImageReceiver11+

PhonePC/2in1TabletTVWearable

createImageReceiver(size: Size, format: ImageFormat, capacity: number): ImageReceiver

通过图片大小、图片格式、容量创建ImageReceiver实例。ImageReceiver做为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流[createPreviewOutput](arkts-apis-camera-cameramanager.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-apis-image-imagereceiver.md#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Size](arkts-apis-image-i.md#size) | 是 | 图像的默认大小。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。 |
| format | [ImageFormat](arkts-apis-image-e.md#imageformat9) | 是 | 图像格式，取值为[ImageFormat](arkts-apis-image-e.md#imageformat9)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机）。 |
| capacity | number | 是 | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageReceiver](arkts-apis-image-imagereceiver.md) | 如果操作成功，则返回ImageReceiver实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; |

**示例：**

```
1. let size: image.Size = {
2. height: 8192,
3. width: 8192
4. }
5. let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
```

## image.createImageReceiver23+

PhonePC/2in1TabletTVWearable

createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined

通过ImageReceiverOptions创建ImageReceiver实例。ImageReceiver做为图片的接收方、消费者，其参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流[createPreviewOutput](arkts-apis-camera-cameramanager.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-apis-image-imagereceiver.md#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ImageReceiverOptions](arkts-apis-image-i.md#imagereceiveroptions23) | 否 | 创建ImageReceiver的属性，包括图片的默认大小和同时访问的最大图片数。  未传入options时，默认的size为1920\*1080，单位为像素（px），表示期望接收宽为1920px，高为1080px的图片。  未传入options时，默认的capacity为3，表示期望同时最多有3张图片等待读取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageReceiver](arkts-apis-image-imagereceiver.md) | undefined | 操作成功时返回ImageReceiver实例，否则返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7900201 | Invalid parameter. |

**示例：**

```
1. let options: image.ImageReceiverOptions = {
2. size: { width: 480, height: 480 },
3. capacity: 3
4. }
5. let receiver: image.ImageReceiver | undefined = image.createImageReceiver(options);
```

## image.createImageCreator11+

PhonePC/2in1TabletTVWearable

createImageCreator(size: Size, format: ImageFormat, capacity: number): ImageCreator

通过图片大小、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-apis-image-imagecreator.md#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Size](arkts-apis-image-i.md#size) | 是 | 图像的默认大小。 |
| format | [ImageFormat](arkts-apis-image-e.md#imageformat9) | 是 | 图像格式，如YCBCR\_422\_SP，JPEG。 |
| capacity | number | 是 | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageCreator](arkts-apis-image-imagecreator.md) | 如果操作成功，则返回ImageCreator实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; |

**示例：**

```
1. let size: image.Size = {
2. height: 8192,
3. width: 8192
4. }
5. let creator: image.ImageCreator = image.createImageCreator(size, image.ImageFormat.JPEG, 8);
```

## image.createImageReceiver(deprecated)

PhonePC/2in1TabletTVWearable

createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver

通过宽、高、图片格式、容量创建ImageReceiver实例。ImageReceiver做为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流[createPreviewOutput](arkts-apis-camera-cameramanager.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-apis-image-imagereceiver.md#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

说明

从API version 9开始支持，从API version 11废弃，建议使用[createImageReceiver](arkts-apis-image-f.md#imagecreateimagereceiver11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 图像的默认宽度。单位：像素。该参数不会影响接收到的图片宽度，实际宽度由生产者决定，如相机。 |
| height | number | 是 | 图像的默认高度。单位：像素。该参数不会影响接收到的图片高度，实际高度由生产者决定，如相机。 |
| format | number | 是 | 图像格式，取值为[ImageFormat](arkts-apis-image-e.md#imageformat9)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机）。 |
| capacity | number | 是 | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageReceiver](arkts-apis-image-imagereceiver.md) | 如果操作成功，则返回ImageReceiver实例。 |

**示例：**

```
1. let receiver: image.ImageReceiver = image.createImageReceiver(8192, 8192, image.ImageFormat.JPEG, 8);
```

## image.createImageCreator(deprecated)

PhonePC/2in1TabletTVWearable

createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator

通过宽、高、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-apis-image-imagecreator.md#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

说明

从API version 9开始支持，从API version 11废弃，建议使用[createImageCreator](arkts-apis-image-f.md#imagecreateimagecreator11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 图像的默认宽度。单位：像素。 |
| height | number | 是 | 图像的默认高度。单位：像素。 |
| format | number | 是 | 图像格式，如YCBCR\_422\_SP，JPEG。 |
| capacity | number | 是 | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageCreator](arkts-apis-image-imagecreator.md) | 如果操作成功，则返回ImageCreator实例。 |

**示例：**

```
1. let creator: image.ImageCreator = image.createImageCreator(8192, 8192, image.ImageFormat.JPEG, 8);
```

## SVG标签说明

PhonePC/2in1TabletTVWearable

从API version 10开始支持SVG标签，使用版本为(SVG) 1.1，SVG标签需设置width，height。SVG文件可添加xml声明，应以“<?xml”开头，当前支持的标签列表有：

* a
* circle
* clipPath
* defs
* ellipse
* feBlend
* feColorMatrix
* feComposite
* feDiffuseLighting
* feDisplacementMap
* feDistantLight
* feFlood
* feGaussianBlur
* feImage
* feMorphology
* feOffset
* fePointLight
* feSpecularLighting
* feSpotLight
* feTurbulence
* filter
* g
* image
* line
* linearGradient
* mask
* path
* pattern
* polygon
* polyline
* radialGradient
* rect
* stop
* svg
* text
* textPath
* tspan
* use
