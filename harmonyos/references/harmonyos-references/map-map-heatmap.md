---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-heatmap
title: Heatmap
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Heatmap
category: harmonyos-references
scraped_at: 2026-04-28T08:17:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:11c730bdd20deaf33864fda7b380ecb70d20628a6d751aec94470f8a84a5a97d
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## Heatmap

PhonePC/2in1TabletWearable

热力图管理对象。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addHeatmap](map-map-mapcomponentcontroller.md#addheatmap)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**示例：**

```
1. let data: mapCommon.WeightedLatLng[] = [];
2. for (let i = 0; i < 500; i++) {
3. data.push({
4. point: {
5. longitude: 118.000000 + Math.random() * 1 - 0.25,
6. latitude: 31.000000 + Math.random() * 1 - 0.25,
7. },
8. intensity: 1
9. });
10. }
11. let heatMapOptions: mapCommon.HeatmapParams = {
12. id: 'heatmap0001',
13. data: data,
14. radius: 20,
15. intensity: {
16. 2: 1,
17. 5: 5,
18. 8: 10
19. },
20. }
21. let heatMap = await this.mapController.addHeatmap(heatMapOptions)
```

### setData

PhonePC/2in1TabletWearable

setData(data: mapCommon.WeightedLatLng[]): void

更新热力图数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| data | [mapCommon.WeightedLatLng](map-common.md#weightedlatlng)[] | 是 | 热力图数据（建议数据量小于10000条），异常值不处理。 |

**示例：**

```
1. let data: mapCommon.WeightedLatLng[] = [
2. {
3. point: {
4. longitude: -151.5129,
5. latitude: 63.1016
6. },
7. intensity: 2.3
8. }
9. ];
10. heatMap.setData(data);
```

### getData

PhonePC/2in1TabletWearable

getData(): mapCommon.WeightedLatLng[]

获取热力图数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.WeightedLatLng](map-common.md#weightedlatlng)[] | 热力图数据。 |

**示例：**

```
1. let data: mapCommon.WeightedLatLng[] = heatMap.getData();
```

### setColor

PhonePC/2in1TabletWearable

setColor(color: Record<number, number>): void

更新热力图颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | Record<number, number> | 是 | 热力图颜色。  - key：数据密度，取值范围[0, 1]。  - value：颜色渐变值，ARGB格式。  异常值不处理。 |

**示例：**

```
1. let record: Record<number, number> = {
2. 0: 0x26C3999,    // 深蓝色
3. 0.15: 0xFF4D4DFF, // 蓝紫色
4. 0.3: 0xFF9999FF,  // 浅蓝紫色
5. 0.45: 0xFFE6E6FF, // 非常浅的蓝紫色
6. 0.6: 0xFFFFCCFF,  // 浅紫色
7. 0.75: 0xFFFF99FF, // 紫色
8. 0.9: 0xFFFF66FF,  // 深紫色
9. 1: 0xFFFF00FF    // 非常深的紫色
10. };
11. heatMap.setColor(record);
```

### getColor

PhonePC/2in1TabletWearable

getColor(): Record<number, number>

获取热力图颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<number, number> | 热力图颜色。  - key：数据密度，取值范围[0, 1]。  - value：颜色渐变值，ARGB格式。 |

**示例：**

```
1. let record: Record<number, number> = heatMap.getColor();
```

### setIntensity

PhonePC/2in1TabletWearable

setIntensity(intensity: number | Record<number, number>): void

更新热力图强度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| intensity | number | Record<number, number> | 是 | 热力图强度，如果是number类型，所有层级使用同一个强度。  - key：层级，取值范围[2, 20]。  - value：热力图强度，取值范围大于0。  异常值不处理。 |

**示例：**

```
1. let intensity: Record<number, number> | number = {
2. 2:0.1,
3. 3:0.1,
4. 4:0.1
5. };
6. heatMap.setIntensity(intensity);
```

### getIntensity

PhonePC/2in1TabletWearable

getIntensity(): number | Record<number, number>

获取热力图强度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Record<number, number> | 热力图强度，如果是number类型，所有层级使用同一个强度。  - key：层级，取值范围[2, 20]。  - value：热力图强度，取值范围大于0。 |

**示例：**

```
1. let intensity: Record<number, number> | number = heatMap.getIntensity();
```

### setOpacity

PhonePC/2in1TabletWearable

setOpacity(opacity: number | Record<number, number>): void

更新热力图透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| opacity | number | Record<number, number> | 是 | 热力图透明度，如果是number类型，所有层级使用同一个透明度。  - key：层级，取值范围[2, 20]。  - value：热力图透明度，取值范围[0, 1]，0表示完全不透明，1表示完全透明。  异常值不处理。 |

**示例：**

```
1. let opacity: Record<number, number> | number = {
2. 2:0.1,
3. 3:0.1,
4. 4:0.1
5. }
6. heatMap.setOpacity(opacity);
```

### getOpacity

PhonePC/2in1TabletWearable

getOpacity(): number | Record<number, number>

获取热力图透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Record<number, number> | 热力图透明度，如果是number类型，所有层级使用同一个透明度。  - key：热力图颜色渐变层级，取值范围[2, 20]。  - value：热力图透明度，取值范围[0, 1]，0表示完全不透明，1表示完全透明。 |

**示例：**

```
1. let opacity: Record<number, number> | number = heatMap.getOpacity();
```

### setRadius

PhonePC/2in1TabletWearable

setRadius(radius: number | Record<number, number>): void

更新热力图半径。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| radius | number | Record<number, number> | 是 | 热力图半径，如果是number类型，所有层级使用同一个半径。  - key：层级，取值范围[2, 20]。  - value：热力图半径，取值范围：[1, +∞)。  异常值不处理。 |

**示例：**

```
1. heatMap.setRadius(3000);
```

### getRadius

PhonePC/2in1TabletWearable

getRadius(): number | Record<number, number>

获取热力图半径。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Record<number, number> | 热力图半径，如果是number类型，所有层级使用同一个半径。  - key：层级，取值范围[2, 20]。  - value：热力图半径，取值范围：[1, +∞)。 |

**示例：**

```
1. let radius: number | Record<number, number> = heatMap.getRadius();
```

### setRadiusUnit

PhonePC/2in1TabletWearable

setRadiusUnit(radiusUnit: mapCommon.RadiusUnit): void

更新热力图半径的单位。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| radiusUnit | [mapCommon.RadiusUnit](map-common.md#radiusunit) | 是 | 热力图半径单位。异常值不处理。 |

**示例：**

```
1. heatMap.setRadiusUnit(mapCommon.RadiusUnit.PIXEL_UNIT);
```

### getRadiusUnit

PhonePC/2in1TabletWearable

getRadiusUnit(): mapCommon.RadiusUnit

获取热力图半径单位。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.RadiusUnit](map-common.md#radiusunit) | 热力图半径单位。 |

**示例：**

```
1. let radiusUnit: mapCommon.RadiusUnit = heatMap.getRadiusUnit();
```

### setVisible

PhonePC/2in1TabletWearable

setVisible(visible: boolean): void

更新热力图是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| visible | boolean | 是 | 热力图是否可见。  - true：可见。  - false：不可见。  异常值不处理。 |

**示例：**

```
1. heatMap.setVisible(false);
```

### isVisible

PhonePC/2in1TabletWearable

isVisible(): boolean

获取热力图是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 热力图是否可见。  - true：可见。  - false：不可见。 |

**示例：**

```
1. let isVisible: boolean = heatMap.isVisible();
```

### remove

PhonePC/2in1TabletWearable

remove(): void

删除热力图。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**示例：**

```
1. heatMap.remove();
```
