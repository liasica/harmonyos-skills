---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-bubble
title: Interface (Bubble)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (Bubble)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3057a11fa43b48294844b6d987a17bd8b2d8ac73e5a291dd56a40356bc7c113f
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
import { image } from '@kit.ImageKit';
```

## Bubble

气泡，继承[BasePriorityOverlay](map-map-basepriorityoverlay.md)。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addBubble](map-map-mapcomponentcontroller.md#addbubble)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let bubbleOptions: mapCommon.BubbleParams = {
  positions: [[{
    latitude: 31.98,
    longitude: 118.766
  }]],
  // 图标需存放在resources/rawfile目录下
  icons: [
    'icon.png',
    'icon.png',
    'icon.png',
    'icon.png'
  ],
  forceVisible: true,
  priority: 3,
  minZoom: 2,
  maxZoom: 20,
  visible: true,
  zIndex: 1
};
let bubble: map.Bubble = await this.mapController.addBubble(bubbleOptions);
```

### setIcons

setIcons(icons: Array<string | image.PixelMap | Resource>): Promise<void>

设置气泡的图标。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| icons | Array<string | [image.PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource)> | 是 | 气泡的图标，异常值不处理。  - 必须提供4个方向的图标，传入的图标宽高需要相同。  - 图片格式支持jpg、jpeg、png、gif（只支持显示第一帧）、webp、svg。  - string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。  **说明：**  从5.0.0(12)版本开始，icon属性支持[Resource](ts-types.md#resource)和[image.PixelMap](arkts-apis-image-pixelmap.md)类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
// 图标需存放在resources/rawfile目录下
let icons: Array<string | image.PixelMap | Resource> = [
  'test1.png',
  'test2.png',
  'test3.png',
  'test4.png'
];
await bubble.setIcons(icons);
```

### setPositions

setPositions(positions: Array<Array<mapCommon.LatLng>>): void

设置气泡的候选位置坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| positions | Array<Array<[mapCommon.LatLng](map-common.md#latlng)>> | 是 | 气泡的候选位置坐标，异常值不处理。 |

**示例：**

```typescript
let positions: Array<Array<mapCommon.LatLng>> = [[
  {
    latitude: 31.9844,
    longitude: 118.7112
  }, {
    latitude: 31.9844,
    longitude: 118.7262
  }, {
    latitude: 31.9844,
    longitude: 118.7362
  }, {
    latitude: 31.9844,
    longitude: 118.7462
  }, {
    latitude: 31.9844,
    longitude: 118.7562
  }, {
    latitude: 31.9844,
    longitude: 118.7662
  }, {
    latitude: 31.9844,
    longitude: 118.7762
  }
]];
bubble.setPositions(positions);
```
