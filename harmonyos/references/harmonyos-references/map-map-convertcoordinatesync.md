---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-convertcoordinatesync
title: convertCoordinateSync
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > convertCoordinateSync
category: harmonyos-references
scraped_at: 2026-04-28T08:17:24+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3be682c2408d714278659ca2461b99f5c56f34b7bde888c02019571b796e4b35
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## convertCoordinateSync

PhonePC/2in1TabletWearable

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

```
1. let wgs84Position: mapCommon.LatLng = {
2. latitude: 30,
3. longitude: 118
4. };
5. // 转换经纬度坐标
6. let gcj02Position: mapCommon.LatLng =
7. map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
```
