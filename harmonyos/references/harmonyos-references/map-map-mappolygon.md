---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolygon
title: MapPolygon
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > MapPolygon
category: harmonyos-references
scraped_at: 2026-04-28T08:17:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5701748b7cfd1a4e8d76a5b28aa81dde94c689e6b875932927d14ab694391943
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MapPolygon

PhonePC/2in1TabletWearable

多边形，继承[BaseOverlay](map-map-baseoverlay.md)。多边形可以是凸面或凹面，它可以跨越180子午线并且可以具有未填充的孔。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addPolygon](map-map-mapcomponentcontroller.md#addpolygon)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. let polygonOptions: mapCommon.MapPolygonOptions = {
2. points: [
3. { latitude: 31.9844102, longitude: 118.7662 },
4. { latitude: 31.9844102, longitude: 123.7662 },
5. { latitude: 36.9844102, longitude: 123.7662 },
6. { latitude: 36.9844102, longitude: 118.7662 }
7. ],
8. fillColor: 0xffff4500
9. };
10. let mapPolygon = await this.mapController.addPolygon(polygonOptions);
```

### getFillColor

PhonePC/2in1TabletWearable

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

```
1. let fillColor: number = mapPolygon.getFillColor();
```

### getHoles

PhonePC/2in1TabletWearable

getHoles(): Array<Array<mapCommon.LatLng>>

获取多边形的空心洞。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Array<[mapCommon.LatLng](map-common.md#latlng)>> | 多边形的空心洞数组，其中空心洞是[LatLng](map-common.md#latlng)数组。 |

**示例：**

```
1. let holes: Array<Array<mapCommon.LatLng>> = mapPolygon.getHoles();
```

### getPoints

PhonePC/2in1TabletWearable

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

```
1. let points: Array<mapCommon.LatLng> = mapPolygon.getPoints();
```

### getStrokeColor

PhonePC/2in1TabletWearable

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

```
1. let strokeColor: number = mapPolygon.getStrokeColor();
```

### getJointType

PhonePC/2in1TabletWearable

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

```
1. let jointType: mapCommon.JointType = mapPolygon.getJointType();
```

### getPatterns

PhonePC/2in1TabletWearable

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

```
1. let patterns: Array<mapCommon.PatternItem> = mapPolygon.getPatterns();
```

### getStrokeWidth

PhonePC/2in1TabletWearable

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

```
1. let strokeWidth: number = mapPolygon.getStrokeWidth();
```

### isClickable

PhonePC/2in1TabletWearable

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

```
1. let clickable: boolean = mapPolygon.isClickable();
```

### isGeodesic

PhonePC/2in1TabletWearable

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

```
1. let geodesic: boolean = mapPolygon.isGeodesic();
```

### setClickable

PhonePC/2in1TabletWearable

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

```
1. mapPolygon.setClickable(true);
```

### setFillColor

PhonePC/2in1TabletWearable

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

```
1. mapPolygon.setFillColor(0xff000FFF);
```

### setGeodesic

PhonePC/2in1TabletWearable

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

```
1. mapPolygon.setGeodesic(true);
```

### setHoles

PhonePC/2in1TabletWearable

setHoles(holes: Array<Array<mapCommon.LatLng>>): void

设置多边形的空心洞。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| holes | Array<Array<[mapCommon.LatLng](map-common.md#latlng)>> | 是 | 空心洞数组，其中空心洞是[LatLng](map-common.md#latlng)数组。异常值不处理。 |

**示例：**

```
1. let holes: Array<Array<mapCommon.LatLng>> = [
2. [
3. {
4. latitude: 32.98,
5. longitude: 121.76
6. },
7. {
8. latitude: 32.98,
9. longitude: 119.76
10. },
11. {
12. latitude: 35.98,
13. longitude: 119.76
14. },
15. {
16. latitude: 35.98,
17. longitude: 121.76
18. }
19. ]
20. ];
21. mapPolygon.setHoles(holes);
```

说明

当空心洞的坐标贴合多边形边缘时，会导致渲染出现异常，渲染多余的空心区域。

### setPoints

PhonePC/2in1TabletWearable

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

```
1. let points: Array<mapCommon.LatLng> = [
2. {
3. latitude: 31.98,
4. longitude: 115.76
5. },
6. {
7. latitude: 31.98,
8. longitude: 118.76
9. },
10. {
11. latitude: 35.98,
12. longitude: 118.76
13. },
14. {
15. latitude: 35.98,
16. longitude: 118.76
17. }
18. ];
19. mapPolygon.setPoints(points);
```

### setStrokeColor

PhonePC/2in1TabletWearable

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

```
1. mapPolygon.setStrokeColor(0xff00DB93);
```

### setJointType

PhonePC/2in1TabletWearable

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

```
1. mapPolygon.setJointType(mapCommon.JointType.ROUND);
```

### setPatterns

PhonePC/2in1TabletWearable

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

```
1. let linePatterns: Array<mapCommon.PatternItem> = [
2. {
3. type: mapCommon.PatternItemType.DASH,
4. length: 100
5. },
6. {
7. type: mapCommon.PatternItemType.DOT,
8. length: 100
9. },
10. {
11. type: mapCommon.PatternItemType.GAP,
12. length: 100
13. }
14. ];
15. mapPolygon.setPatterns(linePatterns);
```

### setStrokeWidth

PhonePC/2in1TabletWearable

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

```
1. mapPolygon.setStrokeWidth(30);
```
