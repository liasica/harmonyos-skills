---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-calculatedistance
title: calculateDistance
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > calculateDistance
category: harmonyos-references
scraped_at: 2026-04-28T08:17:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fbb46ebd1ee4ba3d378f94bf9eb192b8770b91a887940408181e5430db9ac3f2
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## calculateDistance

PhonePC/2in1TabletWearable

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
| number | 两个坐标点之间的距离，单位：米。  入参为空返回0。 |

**示例：**

```
1. let fromLatLng: mapCommon.LatLng = {
2. latitude: 38,
3. longitude: 118
4. };
5. let toLatLng: mapCommon.LatLng = {
6. latitude: 39,
7. longitude: 119
8. };

10. let distance = map.calculateDistance(fromLatLng, toLatLng);
```
