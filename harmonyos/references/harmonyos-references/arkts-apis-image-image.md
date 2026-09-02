---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image
title: Interface (Image)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Interface (Image)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9a4a6c53747725c23c1811b03de42a059e2aa9d62f119297addcc1101692eb5f
---

Image类，供ImageReceiver和ImageCreator使用，用于传输图片对象，其实际内容由生产者决定。如相机预览流提供的Image对象存储了YUV数据、相机拍照提供的Image对象存储了JPEG文件。

调用[readNextImage](arkts-apis-image-imagereceiver.md#readnextimage9)和[readLatestImage](arkts-apis-image-imagereceiver.md#readlatestimage9)接口时会返回Image实例。

Image的属性仅支持在创建时初始化，后续无法再修改，且其属性不对图片内容产生实际影响，请以图片生产者写入的属性为准，即以向[ImageReceiver](arkts-apis-image-imagereceiver.md)发送图片数据的发送方实际写入的内容为准。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用[release](arkts-apis-image-image.md#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**说明** 

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

```ts
import { image } from '@kit.ImageKit';
```

## 属性

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clipRect9+ | [Region](arkts-apis-image-i.md#region8) | 否 | 否 | 要裁剪的图像区域。恒等于整个图像，不支持修改。 |
| size9+ | [Size](arkts-apis-image-i.md#size) | 是 | 否 | 图像大小。  如果Image对象所存储的是相机预览流数据（YUV图像数据），那么获取到的size中的宽和高分别对应YUV图像的宽和高。  如果Image对象所存储的是相机拍照流数据（JPEG图像数据），由于已是编码后的文件，size中的宽等于JPEG文件大小，高等于1。  Image对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId通过[createPreviewOutput](arkts-apis-camera-cameramanager.md#createpreviewoutput)接口还是[createPhotoOutput](arkts-apis-camera-cameramanager.md#createphotooutputdeprecated)接口传给相机。  相机预览与拍照最佳实践请参考[双路预览(ArkTS)](../harmonyos-guides/camera-dual-channel-preview.md)与[拍照实践(ArkTS)](../harmonyos-guides/camera-shooting-case.md)。 |
| format9+ | number | 是 | 否 | 图像格式，参考[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)。 |
| timestamp12+ | number | 是 | 否 | 图像时间戳。时间戳以纳秒为单位，通常是单调递增的。时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。如果要获取某张照片的生成时间，可以通过[getImageProperty](arkts-apis-image-imagesource.md#getimageproperty11)接口读取EXIF时间戳信息。 |
| colorSpace23+ | [colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace) | 是 | 否 | 图像色彩空间，色域枚举类型。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## getComponent9+

getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void

根据图像的组件类型从图像中获取组件缓存。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| componentType | [ComponentType](arkts-apis-image-e.md#componenttype9) | 是 | 图像的组件类型（目前仅支持ComponentType:JPEG，实际返回格式由生产者决定，如相机）。 |
| callback | AsyncCallback<[Component](arkts-apis-image-i.md#component9)> | 是 | 回调函数，当返回组件缓冲区成功，err为undefined，data为获取到的组件缓冲区；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG, (err: BusinessError, component: image.Component) => {
    if (err) {
      console.error(`Failed to get the component.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting component.');
    }
  })
}
```

## getComponent9+

getComponent(componentType: ComponentType): Promise<Component>

根据图像的组件类型从图像中获取组件缓存。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| componentType | [ComponentType](arkts-apis-image-e.md#componenttype9) | 是 | 图像的组件类型（目前仅支持ComponentType:JPEG，实际返回格式由生产者决定，如相机）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Component](arkts-apis-image-i.md#component9)> | Promise对象，返回组件缓冲区。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
    console.info('Succeeded in getting component.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get the component.code ${error.code},message is ${error.message}`);
  })
}
```

## release9+

release(callback: AsyncCallback<void>): void

释放当前图像。使用callback异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当图像释放成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}
```

## release9+

release(): Promise<void>

释放当前图像。使用Promise异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image instance.code ${error.code},message is ${error.message}`);
  })
}
```

## getBufferData23+

getBufferData(): ImageBufferData | null

从图像中获取ImageBufferData。

**注意** 

ImageBufferData中的byteBuffer是对内部缓存的浅拷贝，当Image的生命周期结束时，便不能对byteBuffer做任何操作，否则会导致未定义行为。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageBufferData](arkts-apis-image-i.md#imagebufferdata23) | null | 获取封装图像数据缓冲区的结构体，获取不到时返回空值。 |

**示例：**

```ts
function GetBufferData(img: image.Image) {
  const bufferData = img.getBufferData();
  if (bufferData == null) {
    console.error('Failed to get the bufferData: bufferData is null.');
    return;
  }
  console.info('Succeeded in getting bufferData.');
}
```

## getMetadata23+

getMetadata(key: HdrMetadataKey): HdrMetadataValue | null

根据HDR元数据的类型从图像中获取HDR元数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12) | 是 | HDR元数据的关键字，可用于查询对应值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HdrMetadataValue](arkts-apis-image-t.md#hdrmetadatavalue12) | null | 返回关键字对应的HDR元数据的值。如果图像没有HDR元数据，返回空值。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid parameter. |
| 7600302 | Memory copy failed. |

**示例：**

```ts
async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    console.info(`getMetadata:${staticMetadata}`);
  } catch (err) {
    console.error('Failed to getMetadata.' + err);
  }
}
```
