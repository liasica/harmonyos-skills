---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate
title: Interface (CameraUpdate)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (CameraUpdate)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c5170e61e43651fd7610bd532fd3b5189a47ea2a5dafc23e4fdd5f3f8a9dcacd
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## CameraUpdate

CameraUpdate定义了相机移动参数。CameraUpdate的创建方法参见[newCameraPosition](map-map-functions.md#newcameraposition)、[newLatLng](map-map-functions.md#newlatlng)和[newLatLngBounds](map-map-functions.md#newlatlngbounds)等函数，获取地图的控制器类mapController参见[MapComponentController](map-map-mapcomponentcontroller.md#mapcomponentcontroller)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

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
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// 移动相机
this.mapController.moveCamera(cameraUpdate);
```
