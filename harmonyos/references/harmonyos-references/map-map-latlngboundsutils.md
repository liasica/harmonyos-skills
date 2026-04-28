---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-latlngboundsutils
title: LatLngBoundsUtils
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > LatLngBoundsUtils
category: harmonyos-references
scraped_at: 2026-04-28T08:17:15+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:04735f220d8f8b81dc18334ea5354630b8723804c04b6d2222ebd863023eba10
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## LatLngBoundsUtils

PhonePC/2in1TabletWearable

LatLngBounds工具类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### contains

PhonePC/2in1TabletWearable

static contains(bounds: mapCommon.LatLngBounds, position: mapCommon.LatLng): boolean

判断LatLngBounds是否包含某位置坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | LatLngBounds对象。 |
| position | [mapCommon.LatLng](map-common.md#latlng) | 是 | 用于判断的位置坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：包含该位置点。  false：不包含该位置点。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. southwest: {
3. latitude: 31.98,
4. longitude: 118.766
5. },
6. northeast: {
7. latitude: 32.08,
8. longitude: 118.066
9. }
10. };
11. let result: boolean = map.LatLngBoundsUtils.contains(bounds, {
12. latitude: 15,
13. longitude: 15
14. });
```

### contains

PhonePC/2in1TabletWearable

static contains(src: mapCommon.LatLngBounds, target: mapCommon.LatLngBounds): boolean

判断LatLngBounds是否包含目标区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| src | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | LatLngBounds对象。 |
| target | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 目标区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：包含该区域。  false：不包含该区域。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let src: mapCommon.LatLngBounds = {
2. southwest: {
3. latitude: 31.98,
4. longitude: 118
5. },
6. northeast: {
7. latitude: 31.08,
8. longitude: 119
9. }
10. };
11. let target: mapCommon.LatLngBounds = {
12. southwest: {
13. latitude: 33,
14. longitude: 120
15. },
16. northeast: {
17. latitude: 34,
18. longitude: 121
19. }
20. };

22. let result: boolean = map.LatLngBoundsUtils.contains(src, target);
```

### getCenter

PhonePC/2in1TabletWearable

static getCenter(bounds: mapCommon.LatLngBounds): mapCommon.LatLng

获取LatLngBounds的中心经纬度坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | LatLngBounds对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 中心经纬度坐标。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. southwest: {
3. latitude: 31,
4. longitude: 118
5. },
6. northeast: {
7. latitude: 33,
8. longitude: 119
9. }
10. };
11. let center: mapCommon.LatLng = map.LatLngBoundsUtils.getCenter(bounds);
```

### include

PhonePC/2in1TabletWearable

static include(position: mapCommon.LatLng, bounds?: mapCommon.LatLngBounds): mapCommon.LatLngBounds

获取一个包含指定位置的LatLngBounds对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| position | [mapCommon.LatLng](map-common.md#latlng) | 是 | 位置坐标。 |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 否 | LatLngBounds对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 包含指定位置的LatLngBounds对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let resultBounds: mapCommon.LatLngBounds = map.LatLngBoundsUtils.include({
2. latitude: 31,
3. longitude: 118
4. });
```
