---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-markerclusterinfo
title: Interface (MarkerClusterInfo)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (MarkerClusterInfo)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dd91e0aa0df71773b0b2bdba99d802d4cc796984872dcc58d863d67267dd1031
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## MarkerClusterInfo

聚合图层的标记的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| marker | [Marker](map-map-marker.md) | 否 | 否 | 聚合图层的标记。 |
| clusterItems | Array<[mapCommon.ClusterItem](map-common.md#clusteritem)> | 否 | 否 | 聚合节点数组。 |

**示例：**

```typescript
let clusterItem1: mapCommon.ClusterItem = {
  position: {
    latitude: 31.984,
    longitude: 118.766
  }
};
let clusterItem2: mapCommon.ClusterItem = {
  position: {
    latitude: 31.974,
    longitude: 118.75
  }
};
let array: Array<mapCommon.ClusterItem> = [
  clusterItem1,
  clusterItem2
];
let clusterOverlayParams: mapCommon.ClusterOverlayParams = {
  distance: 40,
  clusterItems: array
};
let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);
let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback1 markerClusterInfo`);
};
clusterOverlay.on("markerClusterClick", callback1);
```
