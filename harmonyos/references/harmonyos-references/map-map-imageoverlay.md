---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-imageoverlay
title: Interface (ImageOverlay)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (ImageOverlay)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:49ae4afecbf664e7e633db0e644938bfe9250f96ea967d764d25ce19c3ec77c3
---

## 导入模块

```typescript
import { mapCommon } from '@kit.MapKit';
```

## ImageOverlay

图片覆盖物。继承[BaseOverlay](map-map-baseoverlay.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
let imageOverlayParams: mapCommon.ImageOverlayParams = {
  bounds: {
    southwest: { latitude: 32, longitude: 118 },
    northeast: { latitude: 32.4, longitude: 118.4 }
  },
  // 图标需存放在resources/rawfile目录下
  image: 'icon.png',
  transparency: 0.3,
  zIndex: 101,
  anchorU: 0.5,
  anchorV: 0.5,
  clickable: true,
  visible: true,
  bearing: 0
};
// 添加图片覆盖物
let imageOverlay = await this.mapController.addImageOverlay(imageOverlayParams);
// 设置覆盖物旋转角度为180度
imageOverlay.setBearing(180);
let bearing: number = imageOverlay.getBearing();
```

### getBearing

getBearing(): number

获取覆盖物的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回覆盖物的旋转角度，单位：度（°）。 |

**示例：**

```typescript
let bearing: number = imageOverlay.getBearing();
```

### getBounds

getBounds(): mapCommon.LatLngBounds

获取覆盖物的矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 获取覆盖物的矩形区域。 |

**示例：**

```typescript
let bounds: mapCommon.LatLngBounds = imageOverlay.getBounds();
```

### getHeight

getHeight(): number

获取覆盖物的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的高度，单位：m。 |

**示例：**

```typescript
let height: number = imageOverlay.getHeight();
```

### getWidth

getWidth(): number

获取覆盖物的宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的宽度，单位：m。 |

**示例：**

```typescript
let width: number = imageOverlay.getWidth();
```

### getPosition

getPosition(): mapCommon.LatLng

获取覆盖物的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 覆盖物的位置。 |

**示例：**

```typescript
let position: mapCommon.LatLng = imageOverlay.getPosition();
```

### getTransparency

getTransparency(): number

获取覆盖物的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。 |

**示例：**

```typescript
let transparency: number = imageOverlay.getTransparency();
```

### isClickable

isClickable(): boolean

获取是否可点击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否可点击。  - true：可点击  - false：不可点击 |

**示例：**

```typescript
let click: boolean = imageOverlay.isClickable();
```

### setBearing

setBearing(bearing: number): void

设置覆盖物的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bearing | number | 是 | 覆盖物的旋转角度，单位：°。  以正北方向为0°、顺时针方向为正的角度，默认值为0°，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361°会被换算成1°，-1°换算为359°。 |

**示例：**

```typescript
imageOverlay.setBearing(180);
```

### setClickable

setClickable(clickable: boolean): void

设置是否开启可点击开关。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 是否开启可点击开关。  - true：开启  - false：不开启 |

**示例：**

```typescript
imageOverlay.setClickable(false);
```

### setDimensions

setDimensions(width: number, height?: number): void

设置覆盖物的宽度和高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| width | number | 是 | 宽度，width为正整数，单位：m，异常值不处理。 |
| height | number | 否 | 高度，height为正整数，单位：m，异常值不处理。若不设置高度，则以覆盖物图片默认宽高比例显示高度。 |

**示例：**

```typescript
imageOverlay.setDimensions(100000, 100000);
```

### setImage

setImage(image: ResourceStr | image.PixelMap): Promise<void>

设置覆盖物的图像。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| image | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 覆盖物的图像。  图片格式支持jpg、jpeg、png、gif（只支持显示第一帧）、webp、svg。  **说明：**  [ResourceStr](ts-types.md#resourcestr)为Resource和string两种格式，其中string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，image参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
// 图标需存放在resources/rawfile目录下
await imageOverlay.setImage("icon.png");
```

### setBounds

setBounds(bounds: mapCommon.LatLngBounds): void

设置覆盖物的矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 覆盖物的矩形区域。 |

**示例：**

```typescript
let bounds: mapCommon.LatLngBounds = {
  southwest: { longitude: 118, latitude: 31 },
  northeast: { longitude: 119, latitude: 32 }
};
imageOverlay.setBounds(bounds);
```

### setPosition

setPosition(position: mapCommon.LatLng): void

设置覆盖物的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| position | [mapCommon.LatLng](map-common.md#latlng) | 是 | 覆盖物的位置。 |

**示例：**

```typescript
let position: mapCommon.LatLng = { longitude: 118, latitude: 31 };
imageOverlay.setPosition(position);
```

### setTransparency

setTransparency(transparency: number): void

设置覆盖物的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| transparency | number | 是 | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。异常值不处理。 |

**示例：**

```typescript
imageOverlay.setTransparency(0.1);
```
