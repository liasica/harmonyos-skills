---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-clusteroverlay
title: ClusterOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > ClusterOverlay
category: harmonyos-references
scraped_at: 2026-04-28T08:17:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2f1efdf57a85729d2aedff19fd6e80b5424a8ce4a40e507908bdd04caa161386
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## ClusterOverlay

PhonePC/2in1TabletWearable

聚合图层类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

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
10. longitude:118.75
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
```

### on('clusterClick')

PhonePC/2in1TabletWearable

on(type: 'clusterClick', callback: Callback<Array<mapCommon.ClusterItem>>): void

监听cluster的点击事件。使用callback异步回调。

建议使用[ClusterOverlay.on(type: 'click')](map-map-clusteroverlay.md#onclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'clusterClick'：聚合图层的聚合点点击监听事件。 |
| callback | Callback<Array<[mapCommon.ClusterItem](map-common.md#clusteritem)>> | 是 | 回调函数，返回Array<[mapCommon.ClusterItem](map-common.md#clusteritem)>。 |

**示例：**

```
1. clusterOverlay.on("clusterClick", (clusterItems) => {
2. console.info(`callback: ${clusterItems.length}`);
3. });
```

### off('clusterClick')

PhonePC/2in1TabletWearable

off(type: 'clusterClick', callback?: Callback<void>): void

取消监听cluster的点击事件。使用callback异步回调。

建议使用[ClusterOverlay.off(type: 'click')](map-map-clusteroverlay.md#offclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'clusterClick'：聚合图层的聚合点点击监听事件。 |
| callback | Callback<void> | 否 | 回调函数。无返回结果的回调函数。 |

**示例：**

```
1. clusterOverlay.off("clusterClick", () => {
2. console.info("callback off");
3. });
```

### on('click')

PhonePC/2in1TabletWearable

on(type: 'click', callback: Callback<Array<mapCommon.ClusterItem>>): void

监听聚合图层的聚合点点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'click'：监听聚合图层的聚合点点击事件。 |
| callback | Callback<Array<[mapCommon.ClusterItem](map-common.md#clusteritem)>> | 是 | 回调函数，返回Array<[mapCommon.ClusterItem](map-common.md#clusteritem)>，监听聚合图层的聚合点点击事件。 |

**示例：**

```
1. let callback1 = (clusterItem: Array<mapCommon.ClusterItem>) => {
2. console.info("click", `callback1 clusterItem length: ${clusterItem.length}`);
3. };
4. let callback2 = (clusterItem: Array<mapCommon.ClusterItem>) => {
5. console.info("click", `callback2 clusterItem length: ${clusterItem.length}`);
6. };
7. let callback3 = (clusterItem: Array<mapCommon.ClusterItem>) => {
8. console.info("click", `callback3 clusterItem length: ${clusterItem.length}`);
9. };
10. clusterOverlay.on("click", callback1);
11. clusterOverlay.on("click", callback2);
12. clusterOverlay.on("click", callback3);
```

### off('click')

PhonePC/2in1TabletWearable

off(type: 'click', callback?: Callback<Array<mapCommon.ClusterItem>>): void

取消监听聚合图层的聚合点点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'click'：监听聚合图层的聚合点点击事件。 |
| callback | Callback<Array<[mapCommon.ClusterItem](map-common.md#clusteritem)>> | 否 | 回调函数，返回Array<[mapCommon.ClusterItem](map-common.md#clusteritem)>，取消监听聚合图层的聚合点点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (clusterItem: Array<mapCommon.ClusterItem>) => {
2. console.info("click", `callback1 clusterItem`);
3. };
4. let callback2 = (clusterItem: Array<mapCommon.ClusterItem>) => {
5. console.info("click", `callback2 clusterItem`);
6. };
7. let callback3 = (clusterItem: Array<mapCommon.ClusterItem>) => {
8. console.info("click", `callback3 clusterItem`);
9. };
10. clusterOverlay.on("click", callback1);
11. clusterOverlay.on("click", callback2);
12. clusterOverlay.on("click", callback3);

14. // 只取消callback1对象的事件响应，当click事件发生时，callback2和callback3会正常被调用
15. clusterOverlay.off('click', callback1);
16. // 取消全部click事件响应
17. clusterOverlay.off('click');
```

### on('markerClusterClick')

PhonePC/2in1TabletWearable

on(type: 'markerClusterClick', callback: Callback<MarkerClusterInfo>): void

监听聚合图层的标记点击事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClusterClick'：聚合图层的标记点击监听事件。 |
| callback | Callback<[MarkerClusterInfo](map-map-markerclusterinfo.md)> | 是 | 回调函数，返回Callback<[MarkerClusterInfo](map-map-markerclusterinfo.md)>，监听聚合图层的标记点击事件。  MarkerClusterInfo包括：  - marker：聚合图层的标记。  - clusterItems：聚合节点数组。 |

**示例：**

```
1. let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
2. console.info("markerClusterClick", `callback1 markerClusterInfo`);
3. };
4. let callback2 = (markerClusterInfo: map.MarkerClusterInfo) => {
5. console.info("markerClusterClick", `callback2 markerClusterInfo`);
6. };
7. let callback3 = (markerClusterInfo: map.MarkerClusterInfo) => {
8. console.info("markerClusterClick", `callback3 markerClusterInfo`);
9. };
10. clusterOverlay.on("markerClusterClick", callback1);
11. clusterOverlay.on("markerClusterClick", callback2);
12. clusterOverlay.on("markerClusterClick", callback3);
```

### off('markerClusterClick')

PhonePC/2in1TabletWearable

off(type: 'markerClusterClick', callback?: Callback<MarkerClusterInfo>): void

取消监听聚合图层的标记点击事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClusterClick'：聚合图层的标记点击监听事件。 |
| callback | Callback<[MarkerClusterInfo](map-map-markerclusterinfo.md)> | 否 | 回调函数，返回Callback<[MarkerClusterInfo](map-map-markerclusterinfo.md)>，取消监听聚合图层的标记点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。  MarkerClusterInfo包括：  - marker：聚合图层的标记。  - clusterItems：聚合节点数组。 |

**示例：**

```
1. let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
2. console.info("markerClusterClick", `callback1 markerClusterInfo`);
3. };
4. let callback2 = (markerClusterInfo: map.MarkerClusterInfo) => {
5. console.info("markerClusterClick", `callback2 markerClusterInfo`);
6. };
7. let callback3 = (markerClusterInfo: map.MarkerClusterInfo) => {
8. console.info("markerClusterClick", `callback3 markerClusterInfo`);
9. };
10. clusterOverlay.on("markerClusterClick", callback1);
11. clusterOverlay.on("markerClusterClick", callback2);
12. clusterOverlay.on("markerClusterClick", callback3);
13. // 只取消callback1对象的事件响应，当markerClusterClick事件发生时，callback2和callback3会正常被调用
14. clusterOverlay.off('markerClusterClick', callback1);
15. // 取消全部markerClusterClick事件响应
16. clusterOverlay.off('markerClusterClick');
```

### addItem

PhonePC/2in1TabletWearable

addItem(item: mapCommon.ClusterItem): Promise<void>

新增聚合节点。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| item | mapCommon.[ClusterItem](map-common.md#clusteritem) | 是 | 待聚合节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. let clusterItem: mapCommon.ClusterItem = {
2. position: {
3. latitude: 31.98,
4. longitude: 118.766
5. }
6. };
7. await clusterOverlay.addItem(clusterItem);
```

### remove

PhonePC/2in1TabletWearable

remove(): Promise<void>

移除聚合图层。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. await clusterOverlay.remove();
```
