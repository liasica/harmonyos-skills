---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-playimageanimation
title: Class (PlayImageAnimation)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (PlayImageAnimation)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1e7a0c03d32f83e9a064088d719db34b4035f87d629a72b00c1ef77d5143f3df
---

## 导入模块

```typescript
import { map } from '@kit.MapKit';
import { image } from '@kit.ImageKit';
```

## PlayImageAnimation

控制多张图片的帧动画，继承[Animation](map-map-animation.md)。

主要用于在地图应用中实现动态图像展示效果，包括路径追踪、事件标识、状态变化等场景，通过连续播放一组图片帧，可以生动地呈现移动轨迹、动画图标或状态转换过程，增强用户的视觉反馈和交互体验。

帧动画是一种通过快速连续显示一系列静态图像来创建动画效果的技术。每一张图像被称为一帧，当这些帧以快速的顺序播放时，用户会感知到平滑的运动或变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
let images: Array<ResourceStr | image.PixelMap> = [
   // 图片存放在resources/rawfile
   'test1.png',
   'test2.png',
   'test3.png',
   'test4.png'
];
let playImageAnimation: map.PlayImageAnimation = new map.PlayImageAnimation();
await playImageAnimation.addImages(images);
```

### addImages

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

```typescript
let images: Array<ResourceStr | image.PixelMap> = [
   // 图片存放在resources/rawfile
   'test1.png',
   'test2.png',
   'test3.png',
   'test4.png'
];
await playImageAnimation.addImages(images);
```
