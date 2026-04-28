---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-spatialrelationutil
title: SpatialRelationUtil
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > SpatialRelationUtil
category: harmonyos-references
scraped_at: 2026-04-28T08:17:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e387da905de9259ff60a85a7519e31953cf4bbd659022c0241332b701654d28d
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## SpatialRelationUtil

PhonePC/2in1TabletWearable

点面关系计算工具类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

### isPointContainedInPolygon

PhonePC/2in1TabletWearable

static isPointContainedInPolygon(points: Array<mapCommon.LatLng>, point: mapCommon.LatLng): boolean

判断点是否在多边形区域内。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| points | Array<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 多边形区域坐标。 |
| point | [mapCommon.LatLng](map-common.md#latlng) | 是 | 需要判断的点坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 点是否在多边形区域内。  - true：在区域内  - false：不在区域内 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let points: Array<mapCommon.LatLng> = [
2. {
3. latitude: 31.693478,
4. longitude: 118.434595
5. }, {
6. latitude: 31.693478,
7. longitude: 118.534595
8. }, {
9. latitude: 32.993478,
10. longitude: 118.734595
11. }, {
12. latitude: 32.993478,
13. longitude: 118.934595
14. }
15. ];
16. let point: mapCommon.LatLng = {
17. latitude: 31.984,
18. longitude: 118.766
19. };
20. let result: boolean = map.SpatialRelationUtil.isPointContainedInPolygon(points, point);
```
