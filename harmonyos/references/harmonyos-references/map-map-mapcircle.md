---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcircle
title: MapCircle
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > MapCircle
category: harmonyos-references
scraped_at: 2026-04-28T08:17:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f4a95603f4f5dc976b6ae74e446dbc88661d5b3b03abe69ace3e748aa280ad8d
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MapCircle

PhonePC/2in1TabletWearable

更新和查询圆的接口，继承[BaseOverlay](map-map-baseoverlay.md)。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addCircle](map-map-mapcomponentcontroller.md#addcircle)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. let mapCircleOptions: mapCommon.MapCircleOptions = {
2. center: {
3. latitude: 39.9,
4. longitude: 116.4
5. },
6. radius: 5000,
7. fillColor: 0XFF00FFFF,
8. strokeColor: 0xFFFF0000,
9. strokeWidth: 10,
10. zIndex: 15
11. };
12. let mapCircle = await this.mapController.addCircle(mapCircleOptions);
```

### getCenter

PhonePC/2in1TabletWearable

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

```
1. let center: mapCommon.LatLng = mapCircle.getCenter();
```

### getFillColor

PhonePC/2in1TabletWearable

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

```
1. let fillColor: number = mapCircle.getFillColor();
```

### getRadius

PhonePC/2in1TabletWearable

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

```
1. let radius: number = mapCircle.getRadius();
```

### getStrokeColor

PhonePC/2in1TabletWearable

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

```
1. let strokeColor: number = mapCircle.getStrokeColor();
```

### getPatterns

PhonePC/2in1TabletWearable

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

```
1. let patterns: Array<mapCommon.PatternItem> = mapCircle.getPatterns();
```

### getStrokeWidth

PhonePC/2in1TabletWearable

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

```
1. let strokeWidth: number = mapCircle.getStrokeWidth();
```

### isClickable

PhonePC/2in1TabletWearable

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

```
1. let clickable: boolean = mapCircle.isClickable();
```

### setCenter

PhonePC/2in1TabletWearable

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

```
1. let center: mapCommon.LatLng = {latitude: 31.98, longitude: 116.4};
2. mapCircle.setCenter(center);
```

### setClickable

PhonePC/2in1TabletWearable

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

```
1. let clickable = true;
2. mapCircle.setClickable(clickable);
```

### setFillColor

PhonePC/2in1TabletWearable

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

```
1. let fillColor = 0xFF00FFFF;
2. mapCircle.setFillColor(fillColor);
```

### setRadius

PhonePC/2in1TabletWearable

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

```
1. let radius = 300;
2. mapCircle.setRadius(radius);
```

### setStrokeColor

PhonePC/2in1TabletWearable

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

```
1. let strokeColor = 0xFFFF0000;
2. mapCircle.setStrokeColor(strokeColor);
```

### setPatterns

PhonePC/2in1TabletWearable

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

```
1. let patterns: Array<mapCommon.PatternItem> = [
2. { type: 0, length: 100 },
3. { type: 1, length: 100 },
4. { type: 2, length: 100 }];
5. mapCircle.setPatterns(patterns);
```

### setStrokeWidth

PhonePC/2in1TabletWearable

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

```
1. let width = 10;
2. mapCircle.setStrokeWidth(width);
```
