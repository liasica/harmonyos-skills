---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-playimageanimation
title: PlayImageAnimation
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > PlayImageAnimation
category: harmonyos-references
scraped_at: 2026-04-28T08:17:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:576c38a99f7592a6918e3726afe8f4af110431dcd2221d0966aa04913c5ca301
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
2. import { image } from '@kit.ImageKit';
```

## PlayImageAnimation

PhonePC/2in1TabletWearable

控制多张图片的帧动画，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. let images: Array<ResourceStr | image.PixelMap> = [
2. // 图片存放在resources/rawfile
3. 'test1.png',
4. 'test2.png',
5. 'test3.png',
6. 'test4.png'
7. ];
8. let playImageAnimation: map.PlayImageAnimation = new map.PlayImageAnimation();
9. await playImageAnimation.addImages(images);
```

### addImages

PhonePC/2in1TabletWearable

addImages(images: Array<ResourceStr | image.PixelMap>): Promise<void>

添加动画的图片资源。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| images | Array<[ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 动画的图片资源。  **说明：**  - 建议图片大小相同。  - 图片数量不超过200张。  - 持续时间需要大于33ms。如果不是，它将被更改为33ms。  - string类型入参，图片存放在resources/rawfile。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let images: Array<ResourceStr | image.PixelMap> = [
2. // 图片存放在resources/rawfile
3. 'test1.png',
4. 'test2.png',
5. 'test3.png',
6. 'test4.png'
7. ];
8. await playImageAnimation.addImages(images);
```
