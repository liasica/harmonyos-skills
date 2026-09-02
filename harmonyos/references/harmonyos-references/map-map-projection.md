---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-projection
title: Interface (Projection)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (Projection)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a24a376fafaae1a2c225ac70c01e6f3280ac19dbce8eed69539c668c42d3a046
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## Projection

用于在屏幕坐标和经纬度之间进行转换，在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[getProjection](map-map-mapcomponentcontroller.md#getprojection)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let projection: map.Projection = this.mapController?.getProjection();
```

### fromScreenLocation

fromScreenLocation(point: mapCommon.MapPoint): mapCommon.LatLng

将屏幕像素点坐标转换成经纬度。屏幕位置是以相对于地图左上角（而不是整个屏幕的左上角）的屏幕像素（而非显示像素）指定的。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| point | [mapCommon.MapPoint](map-common.md#mappoint) | 是 | 屏幕上的坐标点，异常值不处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 经纬度坐标。 |

**示例：**

```typescript
let point: mapCommon.MapPoint = {
  positionX: 10,
  positionY: 10
};
let latLng: mapCommon.LatLng = projection.fromScreenLocation(point);
```

### fromScreenLocation

fromScreenLocation(point: mapCommon.MapPoint, altitude: number): mapCommon.LatLng

将屏幕像素点坐标转换成经纬度坐标。屏幕位置是以相对于地图界面的左上角的屏幕像素指定的。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| point | [mapCommon.MapPoint](map-common.md#mappoint) | 是 | 屏幕上的坐标点，异常值不处理。 |
| altitude | number | 是 | 相对于地面的高度，单位：m，默认值：0，异常值按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 经纬度坐标。 |

**示例：**

```typescript
let point: mapCommon.MapPoint = {
  positionX: 10,
  positionY: 10
};
let latLng: mapCommon.LatLng = projection.fromScreenLocation(point, 100);
```

### toScreenLocation

toScreenLocation(position: mapCommon.LatLng): mapCommon.MapPoint

将经纬度坐标转换为屏幕上的对应点坐标。该屏幕坐标是相对于地图左上角而非整个屏幕的像素点坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| position | [mapCommon.LatLng](map-common.md#latlng) | 是 | 经纬度坐标，异常值不处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.MapPoint](map-common.md#mappoint) | 屏幕上的坐标点。 |

**示例：**

```typescript
let position: mapCommon.LatLng = {
  latitude: 31.984,
  longitude: 118.766
}
let mapPoint: mapCommon.MapPoint = projection.toScreenLocation(position)
```

### toScreenLocation

toScreenLocation(position: mapCommon.LatLng, altitude: number): mapCommon.MapPoint

将经纬度坐标转换为屏幕上的对应点坐标。该屏幕坐标是相对于地图左上角而非整个屏幕的像素点坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| position | [mapCommon.LatLng](map-common.md#latlng) | 是 | 经纬度坐标，异常值不处理。 |
| altitude | number | 是 | 相对于地面的高度，单位：m，默认值：0，异常值按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.MapPoint](map-common.md#mappoint) | 屏幕上的坐标点。 |

**示例：**

```typescript
let position: mapCommon.LatLng = {
  latitude: 31.984,
  longitude: 118.766
}
let mapPoint: mapCommon.MapPoint = projection.toScreenLocation(position, 100)
```

### getVisibleRegion

getVisibleRegion(): mapCommon.VisibleRegion

获取可视区域的坐标信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.VisibleRegion](map-common.md#visibleregion) | 可见区域。 |

**示例：**

```typescript
let visibleRegion: mapCommon.VisibleRegion = projection.getVisibleRegion();
```

### getMapBounds

getMapBounds(center: mapCommon.LatLng, zoom: number): mapCommon.LatLngBounds

根据中心点和缩放级别获取地图控件对应的目标区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| center | [mapCommon.LatLng](map-common.md#latlng) | 是 | 中心点经纬度坐标，异常值不处理。 |
| zoom | number | 是 | 缩放级别，取值范围：[2, 20]。传入的值大于最大层级，会取最大层级，传入的值小于最小层级，会取最小层级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 目标区域。 |

**示例：**

```typescript
let position: mapCommon.LatLng = {
  latitude: 31.98,
  longitude: 118.766
};
let result: mapCommon.LatLngBounds = projection.getMapBounds(position, 10);
```
