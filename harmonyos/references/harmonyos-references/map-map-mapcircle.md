---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcircle
title: Interface (MapCircle)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (MapCircle)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7197e280b10cefbd4ddad74943e14174db8243def683b90b5a6af60c3192eed3
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## MapCircle

更新和查询圆的接口，继承[BaseOverlay](map-map-baseoverlay.md)。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addCircle](map-map-mapcomponentcontroller.md#addcircle)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let mapCircleOptions: mapCommon.MapCircleOptions = {
  center: {
    latitude: 39.9,
    longitude: 116.4
  },
  radius: 5000,
  fillColor: 0XFF00FFFF,
  strokeColor: 0xFFFF0000,
  strokeWidth: 10,
  zIndex: 15
};
let mapCircle = await this.mapController.addCircle(mapCircleOptions);
```

### getCenter

getCenter(): mapCommon.LatLng

获取圆心经纬度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| mapCommon.[LatLng](map-common.md#latlng) | 获取圆心经纬度。 |

**示例：**

```typescript
let center: mapCommon.LatLng = mapCircle.getCenter();
```

### getFillColor

getFillColor(): number

获取圆的填充色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取圆的填充色。 |

**示例：**

```typescript
let fillColor: number = mapCircle.getFillColor();
```

### getRadius

getRadius(): number

获取圆的半径。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 圆的半径，单位：m。 |

**示例：**

```typescript
let radius: number = mapCircle.getRadius();
```

### getStrokeColor

getStrokeColor(): number

获取圆的边框颜色值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | ARGB格式颜色值。 |

**示例：**

```typescript
let strokeColor: number = mapCircle.getStrokeColor();
```

### getPatterns

getPatterns(): Array<mapCommon.PatternItem>

获取圆的边框样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[mapCommon.PatternItem](map-common.md#patternitem)> | 圆的边框样式。 |

**示例：**

```typescript
let patterns: Array<mapCommon.PatternItem> = mapCircle.getPatterns();
```

### getStrokeWidth

getStrokeWidth(): number

获取圆的边框宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 圆的边框宽度，单位：px。 |

**示例：**

```typescript
let strokeWidth: number = mapCircle.getStrokeWidth();
```

### isClickable

isClickable(): boolean

获取圆的可点击性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 圆的可点击性。  - true：可点击  - false：不可点击 |

**示例：**

```typescript
let clickable: boolean = mapCircle.isClickable();
```

### setCenter

setCenter(center: mapCommon.LatLng): void

给圆心设置经纬度坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| center | [mapCommon.LatLng](map-common.md#latlng) | 是 | 圆心经纬度坐标。  圆的中心点纬度在[-85.051119, 85.051119]范围内才能画出圆。若圆中心点纬度为-85.051119或85.051119时，能画出半径为1米的圆。 |

**示例：**

```typescript
let center: mapCommon.LatLng = {latitude: 31.98, longitude: 116.4};
mapCircle.setCenter(center);
```

### setClickable

setClickable(clickable: boolean): void

设置圆的可点击性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 圆的可点击性，异常值不处理。  - true：可点击  - false：不可点击 |

**示例：**

```typescript
let clickable = true;
mapCircle.setClickable(clickable);
```

### setFillColor

setFillColor(color: number): void

设置圆的填充色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | number | 是 | 圆的填充色，颜色值为ARGB格式，异常值不处理。 |

**示例：**

```typescript
let fillColor = 0xFF00FFFF;
mapCircle.setFillColor(fillColor);
```

### setRadius

setRadius(radius: number): void

设置圆的半径。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| radius | number | 是 | 圆的半径，单位：m，取值范围：大于等于0，异常值不处理。 |

**示例：**

```typescript
let radius = 300;
mapCircle.setRadius(radius);
```

### setStrokeColor

setStrokeColor(color: number): void

设置圆的边框颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | number | 是 | 圆的边框颜色，ARGB格式颜色值，异常值不处理。 |

**示例：**

```typescript
let strokeColor = 0xFFFF0000;
mapCircle.setStrokeColor(strokeColor);
```

### setPatterns

setPatterns(patterns: Array<mapCommon.PatternItem>): void

设置圆的边框样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| patterns | Array<[mapCommon.PatternItem](map-common.md#patternitem)> | 是 | 圆的边框样式。 |

**示例：**

```typescript
let patterns: Array<mapCommon.PatternItem> = [
  { type: 0, length: 100 },
  { type: 1, length: 100 },
  { type: 2, length: 100 }];
mapCircle.setPatterns(patterns);
```

### setStrokeWidth

setStrokeWidth(width: number): void

设置圆的边框宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| width | number | 是 | 圆的边框宽度，单位：px，取值范围：大于等于0。 |

**示例：**

```typescript
let width = 10;
mapCircle.setStrokeWidth(width);
```
