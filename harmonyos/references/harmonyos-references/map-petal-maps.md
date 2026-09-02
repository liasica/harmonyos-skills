---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-petal-maps
title: petalMaps（拉起地图应用）
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > petalMaps（拉起地图应用）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1491854b8516853ac7a6a84eb8ddb734be92d5513d3012f18c870b30f1fd315e
---

本模块提供拉起地图应用功能。

**起始版本：** 5.0.3(15)

## 导入模块

```typescript
import { petalMaps } from '@kit.MapKit';
```

## openMapHomePage

openMapHomePage(context: common.Context): Promise<void>

打开地图应用首页。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600014 | Failed to start the map app. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities.  适用版本：5.1.0(18)+ |

**示例：**

```typescript
await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
```

## openMapPoiDetail

openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>

应用的POI详情页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| poiDetailParams | [PoiDetailParams](map-petal-maps.md#poidetailparams) | 是 | POI详情的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600014 | Failed to start the map app. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities.  适用版本：5.1.0(18)+ |

**示例：**

```typescript
let params: petalMaps.PoiDetailParams = {
  destinationPosition: {
    latitude: 30.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
```

## openMapTextSearch

openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>

打开地图应用的文本搜索页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| textSearchParams | [TextSearchParams](map-petal-maps.md#textsearchparams) | 是 | 文本搜索的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600014 | Failed to start the map app. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities.  适用版本：5.1.0(18)+ |

**示例：**

```typescript
let params: petalMaps.TextSearchParams = {
  destinationName: '云谷'
};
await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
```

## openMapRoutePlan

openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>

打开地图应用的路线规划页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| routePlanParams | [RoutePlanParams](map-petal-maps.md#routeplanparams) | 是 | 路线规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600014 | Failed to start the map app. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities.  适用版本：5.1.0(18)+ |

**示例：**

```typescript
let params: petalMaps.RoutePlanParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
```

## openMapNavi

openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>

打开地图应用的导航页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| naviParams | [NaviParams](map-petal-maps.md#naviparams) | 是 | 导航的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600014 | Failed to start the map app. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities.  适用版本：5.1.0(18)+ |

**示例：**

```typescript
let params: petalMaps.NaviParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
```

## openMapTaxi

openMapTaxi(context: common.Context, taxiParams: TaxiParams): Promise<void>

打开地图应用的打车页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在6.0.1(21)及之后版本该接口在phone和tablet均可正常使用，在其他设备中返回801错误码。

**起始版本：** 6.0.1(21)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| taxiParams | [TaxiParams](map-petal-maps.md#taxiparams) | 是 | 打车的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002600014 | Failed to start the map app. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```typescript
let params: petalMaps.TaxiParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
```

## openMapOfflineDataManagement

openMapOfflineDataManagement(context: common.Context, offlineDataParams: OfflineDataParams): Promise<void>

打开地图应用的离线地图管理页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在6.1.1(24)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 6.1.1(24)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| offlineDataParams | [OfflineDataParams](map-petal-maps.md#offlinedataparams) | 是 | 离线地图管理参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002600014 | Failed to start the map app. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```typescript
let params: petalMaps.OfflineDataParams = {
  scenarios: 'PHONE'
};
await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
```

## PoiDetailParams

POI详情的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | POI的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | POI的名称，名称超出单行时，以省略号"..."截断显示。 |
| destinationPoiId | string | 否 | 是 | POI ID。  POI ID和经纬度都作为入参时，POI ID具有更高优先级。 |
| zoom | number | 否 | 是 | 地图缩放级别。取值范围：[3, 20]，默认值：17，异常值按照默认值处理。  **说明：**  当传入destinationPoiId时zoom层级不支持自定义。  **起始版本：** 6.0.1(21) |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。  **起始版本：** 6.0.1(21) |
| destinationAddress | string | 否 | 是 | POI的描述，默认值和异常值会通过逆地理自动获取对应的描述。  **起始版本：** 6.1.1(24) |

**示例：**

```typescript
let params: petalMaps.PoiDetailParams = {
  destinationPosition: {
    latitude: 31.968789,
    longitude: 118.798537
  },
  destinationName: '标记点',
  zoom: 17,
  coordinateType: mapCommon.CoordinateType.GCJ02,
  destinationAddress: '这是我选择的演示名称'
};
```

## TextSearchParams

文本搜索的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationName | string | 否 | 是 | 终点的名称，名称超出单行时，以省略号"..."截断显示。 |

**示例：**

```typescript
let params: petalMaps.TextSearchParams = {
  destinationName: '云谷'
};
```

## RoutePlanParams

路线规划的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| originPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 起点的坐标。默认值为用户当前坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| originName | string | 否 | 是 | 起点的名称，名称超出单行时，以省略号"..."截断显示。 |
| originPoiId | string | 否 | 是 | 起点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 终点的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | 终点的名称，名称超出单行时，以省略号"..."截断显示。 |
| destinationPoiId | string | 否 | 是 | 终点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| vehicleType | [VehicleType](map-petal-maps.md#vehicletype) | 否 | 是 | 出行方式。  默认值为[VehicleType](map-petal-maps.md#vehicletype).DRIVING，异常值按默认值处理。 |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。  **起始版本：** 6.0.1(21) |

**示例：**

```typescript
let params: petalMaps.RoutePlanParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
```

## NaviParams

导航的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 终点的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | 终点名称，名称超出单行时，以省略号"..."截断显示。 |
| destinationPoiId | string | 否 | 是 | 终点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| vehicleType | [VehicleType](map-petal-maps.md#vehicletype) | 否 | 是 | 出行方式。  默认值为[VehicleType](map-petal-maps.md#vehicletype).DRIVING，异常值按默认值处理。 |
| originPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 起点的坐标。默认值为用户当前坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。  **起始版本：** 6.0.1(21) |
| originName | string | 否 | 是 | 起点的名称，名称超出单行时，以省略号"..."截断显示。  **起始版本：** 6.0.1(21) |
| originPoiId | string | 否 | 是 | 起点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。  **起始版本：** 6.0.1(21) |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。  **起始版本：** 6.0.1(21) |

**示例：**

```typescript
let params: petalMaps.NaviParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
```

## OfflineDataParams

离线地图管理参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在6.1.1(24)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 6.1.1(24)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| scenarios | string | 否 | 否 | 场景描述。  **说明：**  目前场景仅支持'WATCH'、'PHONE'、'TABLET'、'PC'、'VOICE'，且可适配大写及小写字符串。  WATCH：打开手表离线地图管理页，管理手表离线地图。  PHONE：打开地图资源管理页，管理设备本地离线地图。  TABLET：打开地图资源管理页，管理设备本地离线地图。  PC：打开地图资源管理页，管理设备本地离线地图。  VOICE：打开导航语音页，管理设备本地离线导航语音。 |
| recommendedRegionIds | string[] | 否 | 是 | 推荐下载离线地图的地区集合，最大长度为20，异常值返回401。 |

**示例：**

```typescript
let params: petalMaps.OfflineDataParams = {
  scenarios: 'PHONE'
};
```

## VehicleType

出行方式。地图应用侧目前出行方式暂时仅支持驾车、步行、骑行、公交。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于5.1.1(19)及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误码。在6.0.0(20)及之后版本该接口在phone、tablet、PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.3(15)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DRIVING | 0 | 驾车。 |
| WALKING | 1 | 步行。 |
| CYCLING | 2 | 骑行。 |
| TRANSIT | 3 | 公交。  **起始版本：** 6.0.1(21) |

## TaxiParams

打车的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在6.0.1(21)及之后版本该接口在phone、tablet均可正常使用，在其他设备中返回801错误码。

**起始版本：** 6.0.1(21)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 终点的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | 终点名称，名称超出单行时，以省略号"..."截断显示。 |
| destinationPoiId | string | 否 | 是 | 终点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| originPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 起点的坐标。默认值为用户当前坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| originName | string | 否 | 是 | 起点的名称，名称超出单行时，以省略号"..."截断显示。 |
| originPoiId | string | 否 | 是 | 起点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。 |

**示例：**

```typescript
let params: petalMaps.TaxiParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
```
