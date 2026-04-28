---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-convertcoordinate
title: convertCoordinate
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > convertCoordinate
category: harmonyos-references
scraped_at: 2026-04-28T08:17:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ec6d239cad3b22fc237f3a2364befc54bd4902c533b3ab16544a7ede88d20951
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## convertCoordinate

PhonePC/2in1TabletWearable

convertCoordinate(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): Promise<mapCommon.LatLng>

坐标系转换。当前仅支持WGS84坐标系转GCJ02坐标系。使用Promise异步回调。

建议使用[convertCoordinateSync](map-map-convertcoordinatesync.md)。

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

```
1. let wgs84Position: mapCommon.LatLng = {
2. latitude: 30,
3. longitude: 118
4. };
5. let gcj02Position: mapCommon.LatLng = await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02,wgs84Position);
```
