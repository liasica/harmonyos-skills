---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagecreator
title: Interface (ImageCreator)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (ImageCreator)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:09+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:b621dc726cb4b9ce373d35068342f106be6928870bd741b61b03a694a39a93cd
---

ImageCreator类，作为图片的生产者，用于将图片写入到Surface中。

在调用以下方法前需要先通过[image.createImageCreator](arkts-apis-image-f.md#imagecreateimagecreator11)创建ImageCreator实例，ImageCreator不支持多线程。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-apis-image-imagecreator.md#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { image } from '@kit.ImageKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| capacity9+ | number | 是 | 否 | 同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |
| format9+ | [ImageFormat](arkts-apis-image-e.md#imageformat9) | 是 | 否 | 图像格式。 |

## dequeueImage9+

PhonePC/2in1TabletTVWearable

dequeueImage(callback: AsyncCallback<Image>): void

从空闲队列中获取buffer图片，用于绘制UI内容。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Image](arkts-apis-image-image.md)> | 是 | 回调函数，当获取最新图片成功，err为undefined，data为获取到的最新图片；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function DequeueImage(creator : image.ImageCreator) {
4. creator.dequeueImage((err: BusinessError, img: image.Image) => {
5. if (err) {
6. console.error(`Failed to dequeue the Image.code ${err.code},message is ${err.message}`);
7. } else {
8. console.info('Succeeded in dequeuing the Image.');
9. }
10. });
11. }
```

## dequeueImage9+

PhonePC/2in1TabletTVWearable

dequeueImage(): Promise<Image>

从空闲队列中获取buffer图片，用于绘制UI内容。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Image](arkts-apis-image-image.md)> | Promise对象，返回最新图片。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function DequeueImage(creator : image.ImageCreator) {
4. creator.dequeueImage().then((img: image.Image) => {
5. console.info('Succeeded in dequeuing the Image.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to dequeue the Image.code ${error.code},message is ${error.message}`);
8. })
9. }
```

## queueImage9+

PhonePC/2in1TabletTVWearable

queueImage(image: Image, callback: AsyncCallback<void>): void

将绘制好的图片放入队列。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [Image](arkts-apis-image-image.md) | 是 | 绘制好的buffer图像。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当将图片放入队列成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function QueueImage(creator : image.ImageCreator) {
4. creator.dequeueImage().then((img: image.Image) => {
5. // 绘制图片。
6. img.getComponent(4).then((component : image.Component) => {
7. let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
8. for (let i = 0; i < bufferArr.length; i += 4) {
9. bufferArr[i] = 0; // B
10. bufferArr[i + 1] = 0; // G
11. bufferArr[i + 2] = 255; // R
12. bufferArr[i + 3] = 255; // A
13. }
14. })
15. creator.queueImage(img, (err: BusinessError) => {
16. if (err) {
17. console.error(`Failed to queue the Image.code ${err.code},message is ${err.message}`);
18. } else {
19. console.info('Succeeded in queuing the Image.');
20. }
21. })
22. })
23. }
```

## queueImage9+

PhonePC/2in1TabletTVWearable

queueImage(image: Image): Promise<void>

将绘制好的图片放入队列。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [Image](arkts-apis-image-image.md) | 是 | 绘制好的buffer图像。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function QueueImage(creator : image.ImageCreator) {
4. creator.dequeueImage().then((img: image.Image) => {
5. // 绘制图片。
6. img.getComponent(4).then((component: image.Component) => {
7. let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
8. for (let i = 0; i < bufferArr.length; i += 4) {
9. bufferArr[i] = 0; // B
10. bufferArr[i + 1] = 0; // G
11. bufferArr[i + 2] = 255; // R
12. bufferArr[i + 3] = 255; // A
13. }
14. })
15. creator.queueImage(img).then(() => {
16. console.info('Succeeded in queuing the Image.');
17. }).catch((error: BusinessError) => {
18. console.error(`Failed to queue the Image.code ${error.code},message is ${error.message}`);
19. })
20. })
21. }
```

## on9+

PhonePC/2in1TabletTVWearable

on(type: 'imageRelease', callback: AsyncCallback<void>): void

监听imageRelease事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，如'imageRelease'。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当监听事件触发成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function On(creator : image.ImageCreator) {
4. creator.on('imageRelease', (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to get the imageRelease callback.code ${err.code},message is ${err.message}`);
7. } else {
8. console.info('Succeeded in getting imageRelease callback.');
9. }
10. })
11. }
```

## off13+

PhonePC/2in1TabletTVWearable

off(type: 'imageRelease', callback?: AsyncCallback<void>): void

释放buffer时，移除注册的回调函数。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件类型，如'imageRelease'。 |
| callback | AsyncCallback<void> | 否 | 回调函数。当移除注册成功时，err返回null，否则为错误对象。 |

**示例：**

```
1. async function Off(creator : image.ImageCreator) {
2. let callbackFunc = ()=>{
3. // 实现回调函数逻辑。
4. }
5. creator.on('imageRelease', callbackFunc)
6. creator.off('imageRelease', callbackFunc)
7. }
```

## release9+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放当前图像。使用callback异步回调。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当图像释放成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release(creator : image.ImageCreator) {
4. creator.release((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to release the creator.code ${err.code},message is ${err.message}`);
7. } else {
8. console.info('Succeeded in releasing creator.');
9. }
10. });
11. }
```

## release9+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放当前图像。使用Promise异步回调。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function Release(creator : image.ImageCreator) {
4. creator.release().then(() => {
5. console.info('Succeeded in releasing creator.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to release the creator.code ${error.code},message is ${error.message}`);
8. })
9. }
```
