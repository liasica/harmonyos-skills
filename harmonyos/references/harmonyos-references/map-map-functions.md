---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-functions
title: Functions
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Functions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cdb852511216d4b5d4b1f566477cac34b6fc25b44e255d4b050092f05df249a4
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## newCameraPosition

newCameraPosition(cameraPosition: mapCommon.CameraPosition): CameraUpdate

创建CameraUpdate对象，更新地图状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| cameraPosition | [mapCommon.CameraPosition](map-common.md#cameraposition) | 是 | 更新后的地图状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化，例如平移、缩放。该对象可用于调用地图更新接口，以实现地图状态变更。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
```

## newLatLng

newLatLng(latLng: mapCommon.LatLng, zoom?: number): CameraUpdate

设置地图的中心点和缩放层级。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| latLng | [mapCommon.LatLng](map-common.md#latlng) | 是 | 经纬度。 |
| zoom | number | 否 | 缩放层级，取值范围：[2, 20]，超出按边界值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let latLng: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraUpdate: map.CameraUpdate = map.newLatLng(latLng);
```

## newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding?: number): CameraUpdate

设置地图经纬度范围、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 地图显示经纬度范围。 |
| padding | number | 否 | 地图区域和边界之间的距离，默认值：0，单位：px，异常值返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 33,
    longitude: 118
  },
  southwest: {
    latitude: 32,
    longitude: 119
  }
};
// 设置地图经纬度范围并指定内边距为5px
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 5);
```

## newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, width: number, height: number, padding: number): CameraUpdate

设置地图经纬度范围、经纬度矩形范围的高和宽、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 地图显示经纬度范围。 |
| width | number | 是 | 经纬度矩形范围的屏幕宽，单位：px，取值范围：大于等于0。 |
| height | number | 是 | 经纬度矩形范围的屏幕高，单位：px，取值范围：大于等于0。 |
| padding | number | 是 | 地图区域和边界之间的距离，单位：px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30.5,
    longitude: 123
  }
};
// 设置地图显示经纬度范围，设置经纬度矩形范围的宽为1000像素，设置经纬度矩形范围的高为1000像素，设置地图区域和边界之间的距离为100像素
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 1000, 1000, 100);
```

## newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding: mapCommon.Padding): CameraUpdate

设置地图经纬度范围和4个方向与边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.1(13)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 地图显示经纬度范围，异常值返回401错误码。 |
| padding | [mapCommon.Padding](map-common.md#padding) | 是 | 地图区域和边界之间的距离，单位：px，异常值返回401错误码。  **说明：**  - 地图组件高度减去padding的top值和bottom值，结果需要大于等于100px。  - 地图组件宽度减去padding的left值和right值，结果需要大于等于100px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30.5,
    longitude: 123
  }
};
// 初始化参数，左边距0，底边距50
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, padding);
```

## scrollBy

scrollBy(x: number, y: number): CameraUpdate

按像素移动地图中心点。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| x | number | 是 | 水平移动的像素数。正值代表可视区域向右移动，负值代表可视区域向左移动。单位：px。 |
| y | number | 是 | 竖直移动的像素数。正值代表可视区域向下移动，负值代表可视区域向上移动。单位：px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let cameraUpdate: map.CameraUpdate = map.scrollBy(100, 200);
```

## zoomBy

zoomBy(amount: number, focus?: mapCommon.MapPoint): CameraUpdate

根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。

以屏幕左顶点为（0, 0）点，focus.positionX正值代表可视区域向右移动，负值代表可视区域向左移动。focus.positionY正值代表可视区域向下移动，负值代表可视区域向上移动。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| amount | number | 是 | 地图缩放级别增量。 |
| focus | [mapCommon.MapPoint](map-common.md#mappoint) | 否 | 地图缩放中心点对应的屏幕坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let focus: mapCommon.MapPoint = {
  positionX: 100,
  positionY: 200
};
let cameraUpdate: map.CameraUpdate = map.zoomBy(10, focus);
```

## zoomIn

zoomIn(): CameraUpdate

放大地图缩放级别，在当前地图显示的级别基础上加1。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**示例：**

```typescript
let cameraUpdate: map.CameraUpdate = map.zoomIn();
```

## zoomOut

zoomOut(): CameraUpdate

缩小地图缩放级别，在当前地图显示的级别基础上减1。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**示例：**

```typescript
let cameraUpdate: map.CameraUpdate = map.zoomOut();
```

## zoomTo

zoomTo(zoom: number): CameraUpdate

设置地图缩放级别。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| zoom | number | 是 | 地图缩放级别，取值范围为[2, 20]，超出按边界值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let cameraUpdate: map.CameraUpdate = map.zoomTo(10);
```

## calculateDistance

calculateDistance(from: mapCommon.LatLng, to: mapCommon.LatLng): number

计算坐标点之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| from | [mapCommon.LatLng](map-common.md#latlng) | 是 | 起点坐标。 |
| to | [mapCommon.LatLng](map-common.md#latlng) | 是 | 终点坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 两个坐标点之间的距离，单位：m。  入参为空返回0。 |

**示例：**

```typescript
let fromLatLng: mapCommon.LatLng = {
  latitude: 38,
  longitude: 118
};
let toLatLng: mapCommon.LatLng = {
  latitude: 39,
  longitude: 119
};

let distance = map.calculateDistance(fromLatLng, toLatLng);
```

## convertCoordinate

convertCoordinate(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): Promise<mapCommon.LatLng>

坐标系转换。当前仅支持WGS84坐标系转GCJ02坐标系。使用Promise异步回调。

同步函数建议使用[convertCoordinateSync](map-map-functions.md#convertcoordinatesync)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 是 | 转换前坐标类型，当前仅支持WGS84。 |
| toType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 是 | 转换后坐标类型，当前仅支持GCJ02。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 是 | 待转换坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[mapCommon.LatLng](map-common.md#latlng)> | Promise对象，返回[mapCommon.LatLng](map-common.md#latlng)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let wgs84Position: mapCommon.LatLng = {
  latitude: 30,
  longitude: 118
};
let gcj02Position: mapCommon.LatLng = await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
```

## convertCoordinateSync

convertCoordinateSync(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): mapCommon.LatLng

坐标系转换。当前仅支持WGS84坐标系转GCJ02坐标系。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 是 | 转换前坐标类型，当前仅支持WGS84。 |
| toType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 是 | 转换后坐标类型，当前仅支持GCJ02。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 是 | 待转换坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 经纬度对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let wgs84Position: mapCommon.LatLng = {
  latitude: 30,
  longitude: 118
};
// 转换经纬度坐标
let gcj02Position: mapCommon.LatLng =
  map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
```

## rectifyCoordinate

rectifyCoordinate(context: common.Context, locations: Array<mapCommon.CoordinateLatLng>): Promise<Array<mapCommon.CoordinateLatLng>>

根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。如果需要修正，则返回修正后的坐标系和坐标。使用Promise异步回调。

**说明** 

* rectifyCoordinate接口仅为解决原始坐标与华为地图展示偏转的问题。
* rectifyCoordinate接口仅支持WGS84坐标系转为GCJ02坐标系。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| locations | Array<[mapCommon.CoordinateLatLng](map-common.md#coordinatelatlng)> | 是 | 输入坐标系和坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[mapCommon.CoordinateLatLng](map-common.md#coordinatelatlng)>> | Promise对象，返回修正后的坐标系和坐标。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600013 | The current routing location is unknown. Try again later. |

**示例：**

```typescript
let locations: Array<mapCommon.CoordinateLatLng> = [
  {
    // 输入香港坐标和WGS84坐标系，若当前地图站点使用GCJ02坐标系，返回GCJ02坐标系和转换后的香港坐标（输入的坐标转换为GCJ02坐标系）
    coordinateType: mapCommon.CoordinateType.WGS84,
    location: { latitude: 22.280556, longitude: 114.984000 }
  }
];
// 包含await的外层方法需要添加async关键字
let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(this.getUIContext().getHostContext(), locations);
```
