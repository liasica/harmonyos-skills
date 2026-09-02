---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolygon
title: Interface (MapPolygon)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (MapPolygon)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:de5076aeddeb6b9f828cd0acfbc838b644d457d496c25ac348f7b11cdd496d2c
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## MapPolygon

多边形，继承[BaseOverlay](map-map-baseoverlay.md)。多边形可以是凸面或凹面，它可以跨越180子午线并且可以具有未填充的孔。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addPolygon](map-map-mapcomponentcontroller.md#addpolygon)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let polygonOptions: mapCommon.MapPolygonOptions = {
  // 定义多边形的四个顶点坐标
  points: [
    { latitude: 31.9844102, longitude: 118.7662 },
    { latitude: 31.9844102, longitude: 123.7662 },
    { latitude: 36.9844102, longitude: 123.7662 },
    { latitude: 36.9844102, longitude: 118.7662 }
  ],
  // 设置多边形填充颜色为红色
  fillColor: 0xffff4500
};
// 地图添加多边形
let mapPolygon = await this.mapController.addPolygon(polygonOptions);
```

### getFillColor

getFillColor(): number

获取ARGB格式的多边形的填充色值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | ARGB格式的颜色值。 |

**示例：**

```typescript
let fillColor: number = mapPolygon.getFillColor();
```

### getHoles

getHoles(): Array<Array<mapCommon.LatLng>>

获取多边形的空心洞。

**说明** 

多边形的空心洞：多边形可能包含一个或多个内部空洞，形成“空心”效果。这些区域不被填充，使得多边形的内部结构更加复杂和多样化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Array<[mapCommon.LatLng](map-common.md#latlng)>> | 多边形的空心洞数组，其中空心洞是[LatLng](map-common.md#latlng)数组。 |

**示例：**

```typescript
let holes: Array<Array<mapCommon.LatLng>> = mapPolygon.getHoles();
```

### getPoints

getPoints(): Array<mapCommon.LatLng>

获取多边形的顶点坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[mapCommon.LatLng](map-common.md#latlng)> | 多边形的顶点坐标。 |

**示例：**

```typescript
let points: Array<mapCommon.LatLng> = mapPolygon.getPoints();
```

### getStrokeColor

getStrokeColor(): number

获取多边形的边框颜色。

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
let strokeColor: number = mapPolygon.getStrokeColor();
```

### getJointType

getJointType(): mapCommon.JointType

获取多边形的顶点样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.JointType](map-common.md#jointtype) | 多边形的顶点样式。 |

**示例：**

```typescript
let jointType: mapCommon.JointType = mapPolygon.getJointType();
```

### getPatterns

getPatterns(): Array<mapCommon.PatternItem>

获取多边形的边框样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[mapCommon.PatternItem](map-common.md#patternitem)> | 多边形的边框样式。 |

**示例：**

```typescript
let patterns: Array<mapCommon.PatternItem> = mapPolygon.getPatterns();
```

### getStrokeWidth

getStrokeWidth(): number

获取多边形的边框宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 多边形的边框宽度，单位：px。 |

**示例：**

```typescript
let strokeWidth: number = mapPolygon.getStrokeWidth();
```

### isClickable

isClickable(): boolean

获取多边形的可点击性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 多边形的可点击性。  - true：可点击  - false：不可点击 |

**示例：**

```typescript
let clickable: boolean = mapPolygon.isClickable();
```

### isGeodesic

isGeodesic(): boolean

获取多边形的每个线段是否为大地线。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 多边形的每个线段是否为大地线。  - true：大地线  - false：非大地线 |

**示例：**

```typescript
let geodesic: boolean = mapPolygon.isGeodesic();
```

### setClickable

setClickable(clickable: boolean): void

设置多边形的可点击性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 多边形的可点击性，异常值不处理。  - true：可点击  - false：不可点击 |

**示例：**

```typescript
mapPolygon.setClickable(true);
```

### setFillColor

setFillColor(color: number): void

设置多边形的填充色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | number | 是 | 多边形的填充色，ARGB格式颜色值，异常值不处理。 |

**示例：**

```typescript
mapPolygon.setFillColor(0xff000FFF);
```

### setGeodesic

setGeodesic(geodesic: boolean): void

设置是否将多边形的每个线段绘制为大地线。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| geodesic | boolean | 是 | 将多边形的每个线段绘制为大地线，异常值不处理。  - true：每段绘制为大地线  - false：不是大地线 |

**示例：**

```typescript
mapPolygon.setGeodesic(true);
```

### setHoles

setHoles(holes: Array<Array<mapCommon.LatLng>>): void

设置多边形的空心洞。

**说明** 

多边形的空心洞：多边形可能包含一个或多个内部空洞，形成“空心”效果。这些区域不被填充，使得多边形的内部结构更加复杂和多样化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| holes | Array<Array<[mapCommon.LatLng](map-common.md#latlng)>> | 是 | 空心洞数组，其中空心洞是[LatLng](map-common.md#latlng)数组。异常值不处理。 |

**示例：**

```typescript
let holes: Array<Array<mapCommon.LatLng>> = [
  [
    {
      latitude: 32.98,
      longitude: 121.76
    },
    {
      latitude: 32.98,
      longitude: 119.76
    },
    {
      latitude: 35.98,
      longitude: 119.76
    },
    {
      latitude: 35.98,
      longitude: 121.76
    }
  ]
];
mapPolygon.setHoles(holes);
```

**说明** 

当空心洞的坐标贴合多边形边缘时，会导致渲染出现异常，渲染多余的空心区域。

### setPoints

setPoints(points: Array<mapCommon.LatLng>): void

重新设置多边形的顶点坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| points | Array<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 顶点坐标数组。异常值不处理。 |

**示例：**

```typescript
let points: Array<mapCommon.LatLng> = [
  {
    latitude: 31.98,
    longitude: 115.76
  },
  {
    latitude: 31.98,
    longitude: 118.76
  },
  {
    latitude: 35.98,
    longitude: 118.76
  },
  {
    latitude: 35.98,
    longitude: 118.76
  }
];
mapPolygon.setPoints(points);
```

### setStrokeColor

setStrokeColor(color: number): void

设置多边形的边框颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | number | 是 | 多边形的边框颜色，ARGB格式颜色值，异常值不处理。 |

**示例：**

```typescript
mapPolygon.setStrokeColor(0xff00DB93);
```

### setJointType

setJointType(jointType: mapCommon.JointType): void

设置多边形的顶点样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| jointType | [mapCommon.JointType](map-common.md#jointtype) | 是 | 顶点样式，异常值不处理。 |

**示例：**

```typescript
mapPolygon.setJointType(mapCommon.JointType.ROUND);
```

### setPatterns

setPatterns(patterns: Array<mapCommon.PatternItem>): void

设置多边形的边框样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| patterns | Array<[mapCommon.PatternItem](map-common.md#patternitem)> | 是 | [PatternItem](map-common.md#patternitem)对象的数组，异常值不处理。 |

**示例：**

```typescript
let linePatterns: Array<mapCommon.PatternItem> = [
  {
    type: mapCommon.PatternItemType.DASH,
    length: 100
  },
  {
    type: mapCommon.PatternItemType.DOT,
    length: 100
  },
  {
    type: mapCommon.PatternItemType.GAP,
    length: 100
  }
];
mapPolygon.setPatterns(linePatterns);
```

### setStrokeWidth

setStrokeWidth(width: number): void

设置多边形的边框宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| width | number | 是 | 边框的宽度，单位：px，取值范围：大于等于0，异常值不处理。 |

**示例：**

```typescript
mapPolygon.setStrokeWidth(30);
```
