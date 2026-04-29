---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-petal-maps
title: petalMaps（拉起地图应用）
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > petalMaps（拉起地图应用）
category: harmonyos-references
scraped_at: 2026-04-29T14:08:09+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:52479c32e7a7e334a9cd4a6cf82654c0b35c35fcbf35f1a856bc1bde7c51c1dc
---

本模块提供拉起地图应用功能。

**起始版本：** 5.0.3(15)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { petalMaps } from '@kit.MapKit';
```

## openMapHomePage

PhonePC/2in1TabletWearable

openMapHomePage(context: common.Context): Promise<void>

根据提供的参数打开地图应用首页。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

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
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
```

## openMapPoiDetail

PhonePC/2in1TabletWearable

openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>

根据提供的参数打开地图应用的POI详情页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

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
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let params: petalMaps.PoiDetailParams = {
2. destinationPosition: {
3. latitude: 30.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
7. await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
```

## openMapTextSearch

PhonePC/2in1TabletWearable

openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>

根据提供的参数打开地图应用的文本搜索页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

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
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let params: petalMaps.TextSearchParams = {
2. destinationName: '云谷'
3. };
4. await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
```

## openMapRoutePlan

PhonePC/2in1TabletWearable

openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>

根据提供的参数打开地图应用的路线规划页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

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
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let params: petalMaps.RoutePlanParams = {
2. destinationPosition: {
3. latitude: 31.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
7. await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
```

## openMapNavi

PhonePC/2in1TabletWearable

openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>

根据提供的参数打开地图应用的导航页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

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
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let params: petalMaps.NaviParams = {
2. destinationPosition: {
3. latitude: 31.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
7. await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
```

## openMapTaxi

PhonePC/2in1TabletWearable

openMapTaxi(context: common.Context, taxiParams: TaxiParams): Promise<void>

根据提供的参数打开地图应用的打车页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API21及之后版本该接口在phone和tablet均可正常使用，在其他设备中返回801错误。

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

```
1. let params: petalMaps.TaxiParams = {
2. destinationPosition: {
3. latitude: 31.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
7. await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
```

## PoiDetailParams

PhonePC/2in1TabletWearable

POI详情的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | POI的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | POI的名称，超长名称超出部分用省略号“...”表示。 |
| destinationPoiId | string | 否 | 是 | POI ID。  POI ID和经纬度都作为入参时，POI ID具有更高优先级。 |
| zoom | number | 否 | 是 | 地图缩放级别。取值范围：[3, 20]，默认值：17，异常值按照默认值处理。  **说明：**  当传入destinationPoiId时zoom层级不支持自定义。  **起始版本：** 6.0.1(21) |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。  **起始版本：** 6.0.1(21) |

**示例：**

```
1. let params: petalMaps.PoiDetailParams = {
2. destinationPosition: {
3. latitude: 30.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
```

## TextSearchParams

PhonePC/2in1TabletWearable

文本搜索的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationName | string | 否 | 是 | 终点的名称，超长名称超出部分用省略号“...”表示。 |

**示例：**

```
1. let params: petalMaps.TextSearchParams = {
2. destinationName: '云谷'
3. };
```

## RoutePlanParams

PhonePC/2in1TabletWearable

路线规划的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| originPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 起点的坐标。默认值为用户当前坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| originName | string | 否 | 是 | 起点的名称，超长名称超出部分用省略号“...”表示。 |
| originPoiId | string | 否 | 是 | 起点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 终点的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | 终点的名称，超长名称超出部分用省略号“...”表示。 |
| destinationPoiId | string | 否 | 是 | 终点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| vehicleType | [VehicleType](map-petal-maps.md#vehicletype) | 否 | 是 | 出行方式。  默认值为[VehicleType](map-petal-maps.md#vehicletype).DRIVING，异常值按默认值处理。 |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。  **起始版本：** 6.0.1(21) |

**示例：**

```
1. let params: petalMaps.RoutePlanParams = {
2. destinationPosition: {
3. latitude: 31.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
```

## NaviParams

PhonePC/2in1TabletWearable

导航的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 终点的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | 终点名称，超长名称超出部分用省略号“...”表示。 |
| destinationPoiId | string | 否 | 是 | 终点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| vehicleType | [VehicleType](map-petal-maps.md#vehicletype) | 否 | 是 | 出行方式。  默认值为[VehicleType](map-petal-maps.md#vehicletype).DRIVING，异常值按默认值处理。 |
| originPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 起点的坐标。默认值为用户当前坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。  **起始版本：** 6.0.1(21) |
| originName | string | 否 | 是 | 起点的名称，超长名称超出部分用省略号“...”表示。  **起始版本：** 6.0.1(21) |
| originPoiId | string | 否 | 是 | 起点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。  **起始版本：** 6.0.1(21) |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。  **起始版本：** 6.0.1(21) |

**示例：**

```
1. let params: petalMaps.NaviParams = {
2. destinationPosition: {
3. latitude: 31.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
```

## VehicleType

PhonePC/2in1TabletWearable

出行方式。地图应用侧目前出行方式暂时仅支持驾车、步行、骑行、公交。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.0.3(15)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DRIVING | 0 | 驾车。 |
| WALKING | 1 | 步行。 |
| CYCLING | 2 | 骑行。 |
| TRANSIT | 3 | 公交。  **起始版本：** 6.0.1(21) |

## TaxiParams

PhonePC/2in1TabletWearable

打车的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API21及之后版本该接口在phone、tablet均可正常使用，在其他设备中返回801错误。

**起始版本：** 6.0.1(21)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| destinationPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 终点的坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| destinationName | string | 否 | 是 | 终点名称，超长名称超出部分用省略号“...”表示。 |
| destinationPoiId | string | 否 | 是 | 终点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| originPosition | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 起点的坐标。默认值为用户当前坐标。  取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。 |
| originName | string | 否 | 是 | 起点的名称，超长名称超出部分用省略号“...”表示。 |
| originPoiId | string | 否 | 是 | 起点的POI ID。  POI ID和经纬度都入参时，POI ID具有更高优先级。 |
| coordinateType | [mapCommon.CoordinateType](map-common.md#coordinatetype) | 否 | 是 | 地图坐标系类型。默认值[mapCommon.CoordinateType](map-common.md#coordinatetype).GCJ02，异常值按照默认值处理。 |

**示例：**

```
1. let params: petalMaps.TaxiParams = {
2. destinationPosition: {
3. latitude: 31.983015468224288,
4. longitude: 118.78058590757131
5. }
6. };
```
