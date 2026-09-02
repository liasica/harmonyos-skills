---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-latlngboundsutils
title: Class (LatLngBoundsUtils)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (LatLngBoundsUtils)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7d925879b6c7e9d9a931e72e7081f135a8cbdca7f27a7e06db25c16936dbdf90
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## LatLngBoundsUtils

LatLngBounds工具类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### contains

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
| boolean | true：包含该位置点（包括坐标点落在LatLngBounds边界上）。  false：不包含该位置点。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let bounds: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 31.98,
    longitude: 118.766
  },
  northeast: {
    latitude: 32.08,
    longitude: 118.066
  }
};
let result: boolean = map.LatLngBoundsUtils.contains(bounds, {
  latitude: 15,
  longitude: 15
});
```

### contains

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

```typescript
let src: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 31.98,
    longitude: 118
  },
  northeast: {
    latitude: 31.08,
    longitude: 119
  }
};
let target: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 33,
    longitude: 120
  },
  northeast: {
    latitude: 34,
    longitude: 121
  }
};

let result: boolean = map.LatLngBoundsUtils.contains(src, target);
```

### getCenter

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

```typescript
let bounds: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 31,
    longitude: 118
  },
  northeast: {
    latitude: 33,
    longitude: 119
  }
};
let center: mapCommon.LatLng = map.LatLngBoundsUtils.getCenter(bounds);
```

### include

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
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 否 | LatLngBounds对象。若为空则创建的LatLngBounds对象只包含位置坐标。 |

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

```typescript
let resultBounds: mapCommon.LatLngBounds = map.LatLngBoundsUtils.include({
  latitude: 31,
  longitude: 118
});
```
