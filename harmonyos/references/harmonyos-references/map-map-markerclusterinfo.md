---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-markerclusterinfo
title: MarkerClusterInfo
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > MarkerClusterInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:17:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:be2d106b7af467c1af1d6404a1a87995fe2291055b6282fdc5721f30217a7ee8
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MarkerClusterInfo

PhonePC/2in1TabletWearable

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

```
1. let clusterItem1: mapCommon.ClusterItem = {
2. position: {
3. latitude: 31.984,
4. longitude: 118.766
5. }
6. };
7. let clusterItem2: mapCommon.ClusterItem = {
8. position: {
9. latitude: 31.974,
10. longitude: 118.75
11. }
12. };
13. let array: Array<mapCommon.ClusterItem> = [
14. clusterItem1,
15. clusterItem2
16. ];
17. let clusterOverlayParams: mapCommon.ClusterOverlayParams = {
18. distance: 40,
19. clusterItems: array
20. };
21. let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);
22. let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
23. console.info("markerClusterClick", `callback1 markerClusterInfo`);
24. };
25. clusterOverlay.on("markerClusterClick", callback1);
```
