---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapeventmanager
title: MapEventManager
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > MapEventManager
category: harmonyos-references
scraped_at: 2026-04-28T08:17:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8b9a32aad6b3f2b4dfa47fe28b63799d69f18db64aa2de619e89bdf9a7a6ae16
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MapEventManager

PhonePC/2in1TabletWearable

地图监听事件管理器。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. let mapEventManager: map.MapEventManager = this.mapController.getEventManager();
```

### on('cameraChange')

PhonePC/2in1TabletWearable

on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void

监听地图相机状态变化。支持传递多个callback异步回调。此回调不会在动画过程中触发，而是在动画结束时触发。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraChange'：监听地图相机状态变化事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，监听地图相机状态变化事件。该回调不会在动画过程中触发，而是在动画结束时触发。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("cameraChange", `callback1 position = ${position.longitude}`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("cameraChange", `callback2 position = ${position.longitude}`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("cameraChange", `callback3 position = ${position.longitude}`);
9. };
10. mapEventManager.on("cameraChange", callback1);
11. mapEventManager.on("cameraChange", callback2);
12. mapEventManager.on("cameraChange", callback3);
```

### off('cameraChange')

PhonePC/2in1TabletWearable

off(type: 'cameraChange', callback?: Callback<mapCommon.LatLng>): void

取消监听地图相机状态变化事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraChange'：监听地图相机状态变化事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 否 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，取消监听地图相机状态变化事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("cameraChange", `callback1 position`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("cameraChange", `callback2 position`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("cameraChange", `callback3 position`);
9. };
10. mapEventManager.on("cameraChange", callback1);
11. mapEventManager.on("cameraChange", callback2);
12. mapEventManager.on("cameraChange", callback3);
13. // 只取消callback1对象的事件响应，当cameraChange事件发生时，callback2和callback3会正常被调用
14. mapEventManager.off('cameraChange', callback1);
15. // 取消所有cameraChange事件响应
16. mapEventManager.off('cameraChange');
```

### on('cameraIdle')

PhonePC/2in1TabletWearable

on(type: 'cameraIdle', callback: Callback<void>): void

监听相机移动结束事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraIdle'：监听相机移动结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数，监听相机移动结束事件。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("cameraIdle", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("cameraIdle", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("cameraIdle", `callback3`);
9. };
10. mapEventManager.on("cameraIdle", callback1);
11. mapEventManager.on("cameraIdle", callback2);
12. mapEventManager.on("cameraIdle", callback3);
```

### off('cameraIdle')

PhonePC/2in1TabletWearable

off(type: 'cameraIdle', callback?: Callback<void>): void

取消监听相机移动结束事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraIdle'：监听相机移动结束事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果的回调函数，取消监听相机移动结束事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("cameraIdle", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("cameraIdle", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("cameraIdle", `callback3`);
9. };
10. mapEventManager.on("cameraIdle", callback1);
11. mapEventManager.on("cameraIdle", callback2);
12. mapEventManager.on("cameraIdle", callback3);
13. // 只取消callback1对象的事件响应，当cameraIdle事件发生时，callback2和callback3会正常被调用
14. mapEventManager.off('cameraIdle', callback1);
15. // 取消全部cameraIdle事件响应
16. mapEventManager.off('cameraIdle');
```

### on('cameraMoveCancel')

PhonePC/2in1TabletWearable

on(type: 'cameraMoveCancel', callback: Callback<void>): void

监听相机移动取消事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveCancel'：监听地图相机移动取消事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数，监听地图相机移动取消事件。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("cameraMoveCancel", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("cameraMoveCancel", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("cameraMoveCancel", `callback3`);
9. };
10. mapEventManager.on("cameraMoveCancel", callback1);
11. mapEventManager.on("cameraMoveCancel", callback2);
12. mapEventManager.on("cameraMoveCancel", callback3);
```

### off('cameraMoveCancel')

PhonePC/2in1TabletWearable

off(type: 'cameraMoveCancel', callback?: Callback<void>): void

取消监听相机移动取消事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveCancel'：监听地图相机移动取消事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果的回调函数，取消监听地图相机移动取消事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("cameraMoveCancel", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("cameraMoveCancel", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("cameraMoveCancel", `callback3`);
9. };
10. mapEventManager.on("cameraMoveCancel", callback1);
11. mapEventManager.on("cameraMoveCancel", callback2);
12. mapEventManager.on("cameraMoveCancel", callback3);
13. // 只取消callback1对象的事件响应，当cameraMoveCancel事件发生时，callback2和callback3会正常被调用
14. mapEventManager.off('cameraMoveCancel', callback1);
15. // 取消全部cameraMoveCancel事件响应
16. mapEventManager.off('cameraMoveCancel');
```

### on('cameraMove')

PhonePC/2in1TabletWearable

on(type: 'cameraMove', callback: Callback<void>): void

监听相机移动事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMove'：监听相机移动事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数，监听相机移动事件。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("cameraMove", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("cameraMove", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("cameraMove", `callback3`);
9. };
10. mapEventManager.on("cameraMove", callback1);
11. mapEventManager.on("cameraMove", callback2);
12. mapEventManager.on("cameraMove", callback3);
```

### off('cameraMove')

PhonePC/2in1TabletWearable

off(type: 'cameraMove', callback?: Callback<void>): void

取消监听相机移动事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMove'：监听相机移动事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果的回调函数，取消监听相机移动事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("cameraMove", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("cameraMove", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("cameraMove", `callback3`);
9. };
10. mapEventManager.on("cameraMove", callback1);
11. mapEventManager.on("cameraMove", callback2);
12. mapEventManager.on("cameraMove", callback3);
13. // 只取消callback1对象的事件响应，当cameraMove事件发生时，callback2和callback3会正常被调用
14. mapEventManager.off('cameraMove', callback1);
15. // 取消全部cameraMove事件响应
16. mapEventManager.off('cameraMove');
```

### on('cameraMoveStart')

PhonePC/2in1TabletWearable

on(type: 'cameraMoveStart', callback: Callback<number>): void

监听相机移动开始事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveStart'：监听相机移动开始事件。 |
| callback | Callback<number> | 是 | 回调函数，返回number，监听相机移动开始事件。  number表示相机改变的原因：  1：地图上的用户手势  2：用户交互产生的默认动画  3：开发人员启动的动画 |

**示例：**

```
1. let callback1 = (reason: number) => {
2. console.info("cameraMoveStart", `callback1 reason = ${reason}`);
3. };
4. let callback2 = (reason: number) => {
5. console.info("cameraMoveStart", `callback2 reason = ${reason}`);
6. };
7. let callback3 = (reason: number) => {
8. console.info("cameraMoveStart", `callback3 reason = ${reason}`);
9. };
10. mapEventManager.on("cameraMoveStart", callback1);
11. mapEventManager.on("cameraMoveStart", callback2);
12. mapEventManager.on("cameraMoveStart", callback3);
```

### off('cameraMoveStart')

PhonePC/2in1TabletWearable

off(type: 'cameraMoveStart', callback?: Callback<number>): void

取消监听相机移动开始事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveStart'：监听相机移动开始事件。 |
| callback | Callback<number> | 否 | 回调函数，取消监听相机移动开始事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。  number表示相机改变的原因：  1：地图上的用户手势  2：用户交互产生的默认动画  3：开发人员启动的动画 |

**示例：**

```
1. let callback1 = (reason: number) => {
2. console.info("cameraMoveStart", `callback1`);
3. };
4. let callback2 = (reason: number) => {
5. console.info("cameraMoveStart", `callback2`);
6. };
7. let callback3 = (reason: number) => {
8. console.info("cameraMoveStart", `callback3`);
9. };
10. mapEventManager.on("cameraMoveStart", callback1);
11. mapEventManager.on("cameraMoveStart", callback2);
12. mapEventManager.on("cameraMoveStart", callback3);

14. // 只取消callback1对象的事件响应，当cameraMoveStart事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('cameraMoveStart', callback1);
16. // 取消全部cameraMoveStart事件响应
17. mapEventManager.off('cameraMoveStart');
```

### on('mapClick')

PhonePC/2in1TabletWearable

on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void

监听地图点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapClick'：监听地图点击事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，监听地图点击事件。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("mapClick", `callback1 position = ${position.longitude}`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("mapClick", `callback2 position = ${position.longitude}`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("mapClick", `callback3 position = ${position.longitude}`);
9. };
10. mapEventManager.on("mapClick", callback1);
11. mapEventManager.on("mapClick", callback2);
12. mapEventManager.on("mapClick", callback3);
```

### off('mapClick')

PhonePC/2in1TabletWearable

off(type: 'mapClick', callback?: Callback<[mapCommon.LatLng](map-common.md#latlng)>): void

取消监听地图点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapClick'：监听地图点击事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 否 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，取消监听地图点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("mapClick", `callback1 position`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("mapClick", `callback2 position`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("mapClick", `callback3 position`);
9. };
10. mapEventManager.on("mapClick", callback1);
11. mapEventManager.on("mapClick", callback2);
12. mapEventManager.on("mapClick", callback3);

14. // 只取消callback1对象的事件响应，当mapClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('mapClick', callback1);
16. // 取消全部mapClick事件响应
17. mapEventManager.off('mapClick');
```

### on('mapLoad')

PhonePC/2in1TabletWearable

on(type: 'mapLoad', callback: Callback<void>): void

监听地图加载事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLoad'：监听地图加载事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数，监听地图加载事件。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("mapLoad", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("mapLoad", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("mapLoad", `callback3`);
9. };
10. mapEventManager.on("mapLoad", callback1);
11. mapEventManager.on("mapLoad", callback2);
12. mapEventManager.on("mapLoad", callback3);
```

### off('mapLoad')

PhonePC/2in1TabletWearable

off(type: 'mapLoad', callback?: Callback<void>): void

取消监听地图加载事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLoad'：监听地图加载事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果的回调函数，取消监听地图加载事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("mapLoad", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("mapLoad", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("mapLoad", `callback3`);
9. };
10. mapEventManager.on("mapLoad", callback1);
11. mapEventManager.on("mapLoad", callback2);
12. mapEventManager.on("mapLoad", callback3);

14. // 只取消callback1对象的事件响应，当mapLoad事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('mapLoad', callback1);
16. // 取消全部mapLoad事件响应
17. mapEventManager.off('mapLoad');
```

### on('mapLongClick')

PhonePC/2in1TabletWearable

on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void

监听地图长按事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLongClick'：监听地图长按事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，监听地图长按事件。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("mapLongClick", `callback1 position = ${position.longitude}`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("mapLongClick", `callback2 position = ${position.longitude}`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("mapLongClick", `callback3 position = ${position.longitude}`);
9. };
10. mapEventManager.on("mapLongClick", callback1);
11. mapEventManager.on("mapLongClick", callback2);
12. mapEventManager.on("mapLongClick", callback3);
```

### off('mapLongClick')

PhonePC/2in1TabletWearable

off(type: 'mapLongClick', callback?: Callback<mapCommon.LatLng>): void

取消监听地图长按事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLongClick'：监听地图长按事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 否 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，取消监听地图长按事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("mapLongClick", `callback1 position`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("mapLongClick", `callback2 position`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("mapLongClick", `callback3 position`);
9. };
10. mapEventManager.on("mapLongClick", callback1);
11. mapEventManager.on("mapLongClick", callback2);
12. mapEventManager.on("mapLongClick", callback3);

14. // 只取消callback1对象的事件响应，当mapLongClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('mapLongClick', callback1);
16. // 取消全部mapLongClick事件响应
17. mapEventManager.off('mapLongClick');
```

### on('myLocationButtonClick')

PhonePC/2in1TabletWearable

on(type: 'myLocationButtonClick', callback: Callback<void>): void

监听我的位置按钮点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationButtonClick'：监听我的位置按钮点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数，监听我的位置按钮点击事件。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("myLocationButtonClick", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("myLocationButtonClick", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("myLocationButtonClick", `callback3`);
9. };
10. mapEventManager.on("myLocationButtonClick", callback1);
11. mapEventManager.on("myLocationButtonClick", callback2);
12. mapEventManager.on("myLocationButtonClick", callback3);
```

### off('myLocationButtonClick')

PhonePC/2in1TabletWearable

off(type: 'myLocationButtonClick', callback?: Callback<void>): void

取消监听我的位置按钮点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationButtonClick'：监听我的位置按钮点击事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果的回调函数，取消监听我的位置按钮点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = () => {
2. console.info("myLocationButtonClick", `callback1`);
3. };
4. let callback2 = () => {
5. console.info("myLocationButtonClick", `callback2`);
6. };
7. let callback3 = () => {
8. console.info("myLocationButtonClick", `callback3`);
9. };
10. mapEventManager.on("myLocationButtonClick", callback1);
11. mapEventManager.on("myLocationButtonClick", callback2);
12. mapEventManager.on("myLocationButtonClick", callback3);

14. // 只取消callback1对象的事件响应，当myLocationButtonClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('myLocationButtonClick', callback1);
16. // 取消全部myLocationButtonClick事件响应
17. mapEventManager.off('myLocationButtonClick');
```

### on('myLocationClick')

PhonePC/2in1TabletWearable

on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void

监听我的位置点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationClick'：监听我的位置点击事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，监听我的位置点击事件。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("myLocationClick", `callback1 position = ${position.longitude}`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("myLocationClick", `callback2 position = ${position.longitude}`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("myLocationClick", `callback3 position = ${position.longitude}`);
9. };
10. mapEventManager.on("myLocationClick", callback1);
11. mapEventManager.on("myLocationClick", callback2);
12. mapEventManager.on("myLocationClick", callback3);
```

### off('myLocationClick')

PhonePC/2in1TabletWearable

off(type: 'myLocationClick', callback?: Callback<mapCommon.LatLng>): void

取消监听我的位置点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationClick'：监听我的位置点击事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 否 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，取消监听我的位置点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (position: mapCommon.LatLng) => {
2. console.info("myLocationClick", `callback1 position`);
3. };
4. let callback2 = (position: mapCommon.LatLng) => {
5. console.info("myLocationClick", `callback2 position`);
6. };
7. let callback3 = (position: mapCommon.LatLng) => {
8. console.info("myLocationClick", `callback3 position`);
9. };
10. mapEventManager.on("myLocationClick", callback1);
11. mapEventManager.on("myLocationClick", callback2);
12. mapEventManager.on("myLocationClick", callback3);

14. // 只取消callback1对象的事件响应，当myLocationClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('myLocationClick', callback1);
16. // 取消全部myLocationClick事件响应
17. mapEventManager.off('myLocationClick');
```

### on('poiClick')

PhonePC/2in1TabletWearable

on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void

监听POI点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'poiClick'：监听POI点击事件。 |
| callback | Callback<[mapCommon.Poi](map-common.md#poi)> | 是 | 回调函数，返回[mapCommon.Poi](map-common.md#poi)，监听POI点击事件。 |

**示例：**

```
1. let callback1 = (poi: mapCommon.Poi) => {
2. console.info("poiClick", `callback1 poi = ${poi.id}`);
3. };
4. let callback2 = (poi: mapCommon.Poi) => {
5. console.info("poiClick", `callback2 poi = ${poi.id}`);
6. };
7. let callback3 = (poi: mapCommon.Poi) => {
8. console.info("poiClick", `callback3 poi = ${poi.id}`);
9. };
10. mapEventManager.on("poiClick", callback1);
11. mapEventManager.on("poiClick", callback2);
12. mapEventManager.on("poiClick", callback3);
```

### off('poiClick')

PhonePC/2in1TabletWearable

off(type: 'poiClick', callback?: Callback<mapCommon.Poi>): void

取消监听POI点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'poiClick'：监听POI点击事件。 |
| callback | Callback<[mapCommon.Poi](map-common.md#poi)> | 否 | 回调函数，返回[mapCommon.Poi](map-common.md#poi)，取消监听POI点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (poi: mapCommon.Poi) => {
2. console.info("poiClick", `callback1 poi`);
3. };
4. let callback2 = (poi: mapCommon.Poi) => {
5. console.info("poiClick", `callback2 poi`);
6. };
7. let callback3 = (poi: mapCommon.Poi) => {
8. console.info("poiClick", `callback3 poi`);
9. };
10. mapEventManager.on("poiClick", callback1);
11. mapEventManager.on("poiClick", callback2);
12. mapEventManager.on("poiClick", callback3);

14. // 只取消callback1对象的事件响应，当poiClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('poiClick', callback1);
16. // 取消全部poiClick事件响应
17. mapEventManager.off('poiClick');
```

### on('markerClick')

PhonePC/2in1TabletWearable

on(type: 'markerClick', callback: Callback<Marker>): void

监听标记点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClick'：监听标记点击事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)，监听标记点击事件。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerClick", `callback1 marker = ${marker.getId()}`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerClick", `callback2 marker = ${marker.getId()}`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerClick", `callback3 marker = ${marker.getId()}`);
9. };
10. mapEventManager.on("markerClick", callback1);
11. mapEventManager.on("markerClick", callback2);
12. mapEventManager.on("markerClick", callback3);
```

### off('markerClick')

PhonePC/2in1TabletWearable

off(type: 'markerClick', callback?: Callback<Marker>): void

取消监听标记点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClick'：监听标记点击事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 否 | 回调函数，返回[Marker](map-map-marker.md)，取消监听标记点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerClick", `callback1 marker`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerClick", `callback2 marker`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerClick", `callback3 marker`);
9. };
10. mapEventManager.on("markerClick", callback1);
11. mapEventManager.on("markerClick", callback2);
12. mapEventManager.on("markerClick", callback3);

14. // 只取消callback1对象的事件响应，当markerClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('markerClick', callback1);
16. // 取消全部markerClick事件响应
17. mapEventManager.off('markerClick');
```

### on('markerDragStart')

PhonePC/2in1TabletWearable

on(type: 'markerDragStart', callback: Callback<Marker>): void

监听标记开始拖拽事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragStart'：监听标记开始拖拽事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)，监听标记开始拖拽事件。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerDragStart", `callback1 marker = ${marker.getId()}`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerDragStart", `callback2 marker = ${marker.getId()}`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerDragStart", `callback3 marker = ${marker.getId()}`);
9. };
10. mapEventManager.on("markerDragStart", callback1);
11. mapEventManager.on("markerDragStart", callback2);
12. mapEventManager.on("markerDragStart", callback3);
```

### off('markerDragStart')

PhonePC/2in1TabletWearable

off(type: 'markerDragStart', callback?: Callback<Marker>): void

取消监听标记开始拖拽事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragStart'：监听标记开始拖拽事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 否 | 回调函数，返回[Marker](map-map-marker.md)，取消监听标记开始拖拽事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerDragStart", `callback1 marker`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerDragStart", `callback2 marker`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerDragStart", `callback3 marker`);
9. };
10. mapEventManager.on("markerDragStart", callback1);
11. mapEventManager.on("markerDragStart", callback2);
12. mapEventManager.on("markerDragStart", callback3);

14. // 只取消callback1对象的事件响应，当markerDragStart事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('markerDragStart', callback1);
16. // 取消全部markerDragStart事件响应
17. mapEventManager.off('markerDragStart');
```

### on('markerDrag')

PhonePC/2in1TabletWearable

on(type: 'markerDrag', callback: Callback<Marker>): void

监听标记拖拽事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDrag'：监听标记拖拽事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)，监听标记拖拽事件。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerDrag", `callback1 marker = ${marker.getId()}`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerDrag", `callback2 marker = ${marker.getId()}`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerDrag", `callback3 marker = ${marker.getId()}`);
9. };
10. mapEventManager.on("markerDrag", callback1);
11. mapEventManager.on("markerDrag", callback2);
12. mapEventManager.on("markerDrag", callback3);
```

### off('markerDrag')

PhonePC/2in1TabletWearable

off(type: 'markerDrag', callback?: Callback<Marker>): void

取消监听标记拖拽事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDrag'：监听标记拖拽事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 否 | 回调函数，返回[Marker](map-map-marker.md)，取消监听标记拖拽事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerDrag", `callback1 marker`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerDrag", `callback2 marker`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerDrag", `callback3 marker`);
9. };
10. mapEventManager.on("markerDrag", callback1);
11. mapEventManager.on("markerDrag", callback2);
12. mapEventManager.on("markerDrag", callback3);

14. // 只取消callback1对象的事件响应，当markerDrag事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('markerDrag', callback1);
16. // 取消全部markerDrag事件响应
17. mapEventManager.off('markerDrag');
```

### on('markerDragEnd')

PhonePC/2in1TabletWearable

on(type: 'markerDragEnd', callback: Callback<Marker>): void

监听标记拖拽结束事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragEnd'：监听标记拖拽结束事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)，监听标记拖拽结束事件。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerDragEnd", `callback1 marker = ${marker.getId()}`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerDragEnd", `callback2 marker = ${marker.getId()}`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerDragEnd", `callback3 marker = ${marker.getId()}`);
9. };
10. mapEventManager.on("markerDragEnd", callback1);
11. mapEventManager.on("markerDragEnd", callback2);
12. mapEventManager.on("markerDragEnd", callback3);
```

### off('markerDragEnd')

PhonePC/2in1TabletWearable

off(type: 'markerDragEnd', callback?: Callback<Marker>): void

取消监听标记拖动结束事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragEnd'：监听标记拖动结束事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 否 | 回调函数，返回[Marker](map-map-marker.md)，取消监听标记拖拽结束事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (marker: map.Marker) => {
2. console.info("markerDragEnd", `callback1 marker`);
3. };
4. let callback2 = (marker: map.Marker) => {
5. console.info("markerDragEnd", `callback2 marker`);
6. };
7. let callback3 = (marker: map.Marker) => {
8. console.info("markerDragEnd", `callback3 marker`);
9. };
10. mapEventManager.on("markerDragEnd", callback1);
11. mapEventManager.on("markerDragEnd", callback2);
12. mapEventManager.on("markerDragEnd", callback3);

14. // 只取消callback1对象的事件响应，当markerDragEnd事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('markerDragEnd', callback1);
16. // 取消全部markerDragEnd事件响应
17. mapEventManager.off('markerDragEnd');
```

### on('circleClick')

PhonePC/2in1TabletWearable

on(type: 'circleClick', callback: Callback<MapCircle>): void

监听圆点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'circleClick'：监听圆点击事件。 |
| callback | Callback<[MapCircle](map-map-mapcircle.md)> | 是 | 回调函数，返回[MapCircle](map-map-mapcircle.md)，监听圆点击事件。 |

**示例：**

```
1. let callback1 = (circle: map.MapCircle) => {
2. console.info("circleClick", `callback1 circle = ${circle.getId()}`);
3. };
4. let callback2 = (circle: map.MapCircle) => {
5. console.info("circleClick", `callback2 circle = ${circle.getId()}`);
6. };
7. let callback3 = (circle: map.MapCircle) => {
8. console.info("circleClick", `callback3 circle = ${circle.getId()}`);
9. };
10. mapEventManager.on("circleClick", callback1);
11. mapEventManager.on("circleClick", callback2);
12. mapEventManager.on("circleClick", callback3);
```

### off('circleClick')

PhonePC/2in1TabletWearable

off(type: 'circleClick', callback?: Callback<MapCircle>): void

取消监听圆点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'circleClick'：监听圆点击事件。 |
| callback | Callback<[MapCircle](map-map-mapcircle.md)> | 否 | 回调函数，返回[MapCircle](map-map-mapcircle.md)，取消监听圆点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (circle: map.MapCircle) => {
2. console.info("circleClick", `callback1 circle`);
3. };
4. let callback2 = (circle: map.MapCircle) => {
5. console.info("circleClick", `callback2 circle`);
6. };
7. let callback3 = (circle: map.MapCircle) => {
8. console.info("circleClick", `callback3 circle`);
9. };
10. mapEventManager.on("circleClick", callback1);
11. mapEventManager.on("circleClick", callback2);
12. mapEventManager.on("circleClick", callback3);

14. // 只取消callback1对象的事件响应，当circleClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('circleClick', callback1);
16. // 取消全部circleClick事件响应
17. mapEventManager.off('circleClick');
```

### on('polylineClick')

PhonePC/2in1TabletWearable

on(type: 'polylineClick', callback: Callback<MapPolyline>): void

监听折线点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polylineClick'：监听折线点击事件。 |
| callback | Callback<[MapPolyline](map-map-mappolyline.md)> | 是 | 回调函数，返回[MapPolyline](map-map-mappolyline.md)，监听折线点击事件。 |

**示例：**

```
1. let callback1 = (polyline: map.MapPolyline) => {
2. console.info("polylineClick", `callback1 polyline = ${polyline.getId()}`);
3. };
4. let callback2 = (polyline: map.MapPolyline) => {
5. console.info("polylineClick", `callback2 polyline = ${polyline.getId()}`);
6. };
7. let callback3 = (polyline: map.MapPolyline) => {
8. console.info("polylineClick", `callback3 polyline = ${polyline.getId()}`);
9. };
10. mapEventManager.on("polylineClick", callback1);
11. mapEventManager.on("polylineClick", callback2);
12. mapEventManager.on("polylineClick", callback3);
```

### off('polylineClick')

PhonePC/2in1TabletWearable

off(type: 'polylineClick', callback?: Callback<MapPolyline>): void

取消监听折线点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polylineClick'：监听折线点击事件。 |
| callback | Callback<[MapPolyline](map-map-mappolyline.md)> | 否 | 回调函数，返回[MapPolyline](map-map-mappolyline.md)，取消监听折线点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (polyline: map.MapPolyline) => {
2. console.info("polylineClick", `callback1 polyline`);
3. };
4. let callback2 = (polyline: map.MapPolyline) => {
5. console.info("polylineClick", `callback2 polyline`);
6. };
7. let callback3 = (polyline: map.MapPolyline) => {
8. console.info("polylineClick", `callback3 polyline`);
9. };
10. mapEventManager.on("polylineClick", callback1);
11. mapEventManager.on("polylineClick", callback2);
12. mapEventManager.on("polylineClick", callback3);

14. // 只取消callback1对象的事件响应，当polylineClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('polylineClick', callback1);
16. // 取消全部polylineClick事件响应
17. mapEventManager.off('polylineClick');
```

### on('polygonClick')

PhonePC/2in1TabletWearable

on(type: 'polygonClick', callback: Callback<MapPolygon>): void

监听多边形点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polygonClick'：监听多边形点击事件。 |
| callback | Callback<[MapPolygon](map-map-mappolygon.md)> | 是 | 回调函数，返回[MapPolygon](map-map-mappolygon.md)，监听多边形点击事件。 |

**示例：**

```
1. let callback1 = (polygon: map.MapPolygon) => {
2. console.info("polygonClick", `callback1 polygon = ${polygon.getId()}`);
3. };
4. let callback2 = (polygon: map.MapPolygon) => {
5. console.info("polygonClick", `callback2 polygon = ${polygon.getId()}`);
6. };
7. let callback3 = (polygon: map.MapPolygon) => {
8. console.info("polygonClick", `callback3 polygon = ${polygon.getId()}`);
9. };
10. mapEventManager.on("polygonClick", callback1);
11. mapEventManager.on("polygonClick", callback2);
12. mapEventManager.on("polygonClick", callback3);
```

### off('polygonClick')

PhonePC/2in1TabletWearable

off(type: 'polygonClick', callback?: Callback<MapPolygon>): void

取消监听多边形点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polygonClick'：监听多边形点击事件。 |
| callback | Callback<[MapPolygon](map-map-mappolygon.md)> | 否 | 回调函数，返回[MapPolygon](map-map-mappolygon.md)，取消监听多边形点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (polygon: map.MapPolygon) => {
2. console.info("polygonClick", `callback1 polygon`);
3. };
4. let callback2 = (polygon: map.MapPolygon) => {
5. console.info("polygonClick", `callback2 polygon`);
6. };
7. let callback3 = (polygon: map.MapPolygon) => {
8. console.info("polygonClick", `callback3 polygon`);
9. };
10. mapEventManager.on("polygonClick", callback1);
11. mapEventManager.on("polygonClick", callback2);
12. mapEventManager.on("polygonClick", callback3);

14. // 只取消callback1对象的事件响应，当polygonClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('polygonClick', callback1);
16. // 取消全部polygonClick事件响应
17. mapEventManager.off('polygonClick');
```

### on('infoWindowClick')

PhonePC/2in1TabletWearable

on(type: 'infoWindowClick', callback: Callback<Marker>): void

监听信息窗点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClick'：监听信息窗点击事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)，监听信息窗点击事件。 |

**示例：**

```
1. let callback1 = (infoWindow: map.Marker) => {
2. console.info("infoWindowClick", `callback1 infoWindow = ${infoWindow.getId()}`);
3. };
4. let callback2 = (infoWindow: map.Marker) => {
5. console.info("infoWindowClick", `callback2 infoWindow = ${infoWindow.getId()}`);
6. };
7. let callback3 = (infoWindow: map.Marker) => {
8. console.info("infoWindowClick", `callback3 infoWindow = ${infoWindow.getId()}`);
9. };
10. mapEventManager.on("infoWindowClick", callback1);
11. mapEventManager.on("infoWindowClick", callback2);
12. mapEventManager.on("infoWindowClick", callback3);
```

### off('infoWindowClick')

PhonePC/2in1TabletWearable

off(type: 'infoWindowClick', callback?: Callback<[Marker](map-map-marker.md)>): void

取消监听信息窗点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClick'：监听信息窗点击事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 否 | 回调函数，返回[Marker](map-map-marker.md)，取消监听信息窗点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (infoWindow: map.Marker) => {
2. console.info("infoWindowClick", `callback1 infoWindow`);
3. };
4. let callback2 = (infoWindow: map.Marker) => {
5. console.info("infoWindowClick", `callback2 infoWindow`);
6. };
7. let callback3 = (infoWindow: map.Marker) => {
8. console.info("infoWindowClick", `callback3 infoWindow`);
9. };
10. mapEventManager.on("infoWindowClick", callback1);
11. mapEventManager.on("infoWindowClick", callback2);
12. mapEventManager.on("infoWindowClick", callback3);

14. // 只取消callback1对象的事件响应，当infoWindowClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('infoWindowClick', callback1);
16. // 取消全部infoWindowClick事件响应
17. mapEventManager.off('infoWindowClick');
```

### on('infoWindowClose')

PhonePC/2in1TabletWearable

on(type: 'infoWindowClose', callback: Callback<Marker>): void

监听信息窗关闭事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClose'：监听信息窗关闭事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)，监听信息窗关闭事件。 |

**示例：**

```
1. let callback1 = (infoWindow: map.Marker) => {
2. console.info("infoWindowClose", `callback1 infoWindowClose = ${infoWindow.getId()}`);
3. };
4. let callback2 = (infoWindow: map.Marker) => {
5. console.info("infoWindowClose", `callback2 infoWindowClose = ${infoWindow.getId()}`);
6. };
7. let callback3 = (infoWindow: map.Marker) => {
8. console.info("infoWindowClose", `callback3 infoWindowClose = ${infoWindow.getId()}`);
9. };
10. mapEventManager.on("infoWindowClose", callback1);
11. mapEventManager.on("infoWindowClose", callback2);
12. mapEventManager.on("infoWindowClose", callback3);
```

### off('infoWindowClose')

PhonePC/2in1TabletWearable

off(type: 'infoWindowClose', callback?: Callback<Marker>): void

取消监听信息窗关闭事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClose'：监听信息窗关闭事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 否 | 回调函数，返回[Marker](map-map-marker.md)，取消监听信息窗关闭事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (infoWindow: map.Marker) => {
2. console.info("infoWindowClose", `callback1 infoWindowClose`);
3. };
4. let callback2 = (infoWindow: map.Marker) => {
5. console.info("infoWindowClose", `callback2 infoWindowClose`);
6. };
7. let callback3 = (infoWindow: map.Marker) => {
8. console.info("infoWindowClose", `callback3 infoWindowClose`);
9. };
10. mapEventManager.on("infoWindowClose", callback1);
11. mapEventManager.on("infoWindowClose", callback2);
12. mapEventManager.on("infoWindowClose", callback3);

14. // 只取消callback1对象的事件响应，当infoWindowClose事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('infoWindowClose', callback1);
16. // 取消全部infoWindowClose事件响应
17. mapEventManager.off('infoWindowClose');
```

### on('pointAnnotationClick')

PhonePC/2in1TabletWearable

on(type: 'pointAnnotationClick', callback: Callback<PointAnnotation>): void

监听点注释点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'pointAnnotationClick'：监听点注释点击事件。 |
| callback | Callback<[PointAnnotation](map-map-pointannotation.md)> | 是 | 回调函数，返回[PointAnnotation](map-map-pointannotation.md)，监听点注释点击事件。 |

**示例：**

```
1. let callback1 = (pointAnnotation: map.PointAnnotation) => {
2. console.info("pointAnnotationClick", `callback1 pointAnnotation = ${pointAnnotation.getId()}`);
3. };
4. let callback2 = (pointAnnotation: map.PointAnnotation) => {
5. console.info("pointAnnotationClick", `callback2 pointAnnotation = ${pointAnnotation.getId()}`);
6. };
7. let callback3 = (pointAnnotation: map.PointAnnotation) => {
8. console.info("pointAnnotationClick", `callback3 pointAnnotation = ${pointAnnotation.getId()}`);
9. };
10. mapEventManager.on("pointAnnotationClick", callback1);
11. mapEventManager.on("pointAnnotationClick", callback2);
12. mapEventManager.on("pointAnnotationClick", callback3);
```

### off('pointAnnotationClick')

PhonePC/2in1TabletWearable

off(type: 'pointAnnotationClick', callback?: Callback<PointAnnotation>): void

取消监听点注释点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'pointAnnotationClick'：监听点注释点击事件。 |
| callback | Callback<[PointAnnotation](map-map-pointannotation.md)> | 否 | 回调函数，返回[PointAnnotation](map-map-pointannotation.md)，取消监听点注释点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (pointAnnotation: map.PointAnnotation) => {
2. console.info("pointAnnotationClick", `callback1 pointAnnotation`);
3. };
4. let callback2 = (pointAnnotation: map.PointAnnotation) => {
5. console.info("pointAnnotationClick", `callback2 pointAnnotation`);
6. };
7. let callback3 = (pointAnnotation: map.PointAnnotation) => {
8. console.info("pointAnnotationClick", `callback3 pointAnnotation`);
9. };
10. mapEventManager.on("pointAnnotationClick", callback1);
11. mapEventManager.on("pointAnnotationClick", callback2);
12. mapEventManager.on("pointAnnotationClick", callback3);

14. // 只取消callback1对象的事件响应，当pointAnnotationClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('pointAnnotationClick', callback1);
16. // 取消全部pointAnnotationClick事件响应
17. mapEventManager.off('pointAnnotationClick');
```

### on('bubbleClick')

PhonePC/2in1TabletWearable

on(type: 'bubbleClick', callback: Callback<Bubble>): void

监听气泡点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'bubbleClick'：监听气泡点击事件。 |
| callback | Callback<[Bubble](map-map-bubble.md)> | 是 | 回调函数，返回[Bubble](map-map-bubble.md)，监听气泡点击事件。 |

**示例：**

```
1. let callback1 = (bubble: map.Bubble) => {
2. console.info("bubbleClick", `callback1 bubble = ${bubble.getId()}`);
3. };
4. let callback2 = (bubble: map.Bubble) => {
5. console.info("bubbleClick", `callback2 bubble = ${bubble.getId()}`);
6. };
7. let callback3 = (bubble: map.Bubble) => {
8. console.info("bubbleClick", `callback3 bubble = ${bubble.getId()}`);
9. };
10. mapEventManager.on("bubbleClick", callback1);
11. mapEventManager.on("bubbleClick", callback2);
12. mapEventManager.on("bubbleClick", callback3);
```

### off('bubbleClick')

PhonePC/2in1TabletWearable

off(type: 'bubbleClick', callback?: Callback<Bubble>): void

取消监听气泡点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'bubbleClick'：监听气泡点击事件。 |
| callback | Callback<[Bubble](map-map-bubble.md)> | 否 | 回调函数，返回[Bubble](map-map-bubble.md)，取消监听气泡点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (bubble: map.Bubble) => {
2. console.info("bubbleClick", `callback1 bubble`);
3. };
4. let callback2 = (bubble: map.Bubble) => {
5. console.info("bubbleClick", `callback2 bubble`);
6. };
7. let callback3 = (bubble: map.Bubble) => {
8. console.info("bubbleClick", `callback3 bubble`);
9. };
10. mapEventManager.on("bubbleClick", callback1);
11. mapEventManager.on("bubbleClick", callback2);
12. mapEventManager.on("bubbleClick", callback3);

14. // 只取消callback1对象的事件响应，当bubbleClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('bubbleClick', callback1);
16. // 取消全部bubbleClick事件响应
17. mapEventManager.off('bubbleClick');
```

### on('imageOverlayClick')

PhonePC/2in1TabletWearable

on(type: 'imageOverlayClick', callback: Callback<ImageOverlay>): void

监听覆盖物点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'imageOverlayClick'：监听覆盖物点击事件。 |
| callback | Callback<[ImageOverlay](map-map-imageoverlay.md)> | 是 | 回调函数，返回[ImageOverlay](map-map-imageoverlay.md)，监听覆盖物点击事件。 |

**示例：**

```
1. let callback1 = (imageOverlay: map.ImageOverlay) => {
2. console.info("imageOverlayClick", `callback1 imageOverlay = ${imageOverlay.getId()}`);
3. };
4. let callback2 = (imageOverlay: map.ImageOverlay) => {
5. console.info("imageOverlayClick", `callback2 imageOverlay = ${imageOverlay.getId()}`);
6. };
7. let callback3 = (imageOverlay: map.ImageOverlay) => {
8. console.info("imageOverlayClick", `callback3 imageOverlay = ${imageOverlay.getId()}`);
9. };
10. mapEventManager.on("imageOverlayClick", callback1);
11. mapEventManager.on("imageOverlayClick", callback2);
12. mapEventManager.on("imageOverlayClick", callback3);
```

### off('imageOverlayClick')

PhonePC/2in1TabletWearable

off(type: 'imageOverlayClick', callback?: Callback<ImageOverlay>): void

取消监听覆盖物点击事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'imageOverlayClick'：监听覆盖物点击事件。 |
| callback | Callback<[ImageOverlay](map-map-imageoverlay.md)> | 否 | 回调函数，返回[ImageOverlay](map-map-imageoverlay.md)，取消监听覆盖物点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. let callback1 = (imageOverlay: map.ImageOverlay) => {
2. console.info("imageOverlayClick", `callback1 imageOverlay`);
3. };
4. let callback2 = (imageOverlay: map.ImageOverlay) => {
5. console.info("imageOverlayClick", `callback2 imageOverlay`);
6. };
7. let callback3 = (imageOverlay: map.ImageOverlay) => {
8. console.info("imageOverlayClick", `callback3 imageOverlay`);
9. };
10. mapEventManager.on("imageOverlayClick", callback1);
11. mapEventManager.on("imageOverlayClick", callback2);
12. mapEventManager.on("imageOverlayClick", callback3);

14. // 只取消callback1对象的事件响应，当imageOverlayClick事件发生时，callback2和callback3会正常被调用
15. mapEventManager.off('imageOverlayClick', callback1);
16. // 取消全部imageOverlayClick事件响应
17. mapEventManager.off('imageOverlayClick');
```

### on('error')

PhonePC/2in1TabletWearable

on(type: 'error', callback: ErrorCallback): void

监听异常事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'error'：监听异常事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，返回[ErrorCallback](js-apis-base.md#errorcallback)，监听异常事件。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let callback1 = (error: BusinessError) => {
4. console.error("error", `callback1 code: ${error.code}, message: ${error.message}`);
5. };
6. let callback2 = (error: BusinessError) => {
7. console.error("error", `callback2 code: ${error.code}, message: ${error.message}`);
8. };
9. let callback3 = (error: BusinessError) => {
10. console.error("error", `callback3 code: ${error.code}, message: ${error.message}`);
11. };
12. mapEventManager.on("error", callback1);
13. mapEventManager.on("error", callback2);
14. mapEventManager.on("error", callback3);
```

### off('error')

PhonePC/2in1TabletWearable

off(type: 'error', callback?: ErrorCallback): void

取消监听异常事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'error'：监听异常事件。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，返回[ErrorCallback](js-apis-base.md#errorcallback)，取消监听异常事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let callback1 = (error: BusinessError) => {
4. console.info("error", `callback1`);
5. };
6. let callback2 = (error: BusinessError) => {
7. console.info("error", `callback2`);
8. };
9. let callback3 = (error: BusinessError) => {
10. console.info("error", `callback3`);
11. };
12. mapEventManager.on("error", callback1);
13. mapEventManager.on("error", callback2);
14. mapEventManager.on("error", callback3);

16. // 只取消callback1对象的事件响应，当error事件发生时，callback2和callback3会正常被调用
17. mapEventManager.off('error', callback1);
18. // 取消全部error事件响应
19. mapEventManager.off('error');
```

### on('indoorMapEnter')

PhonePC/2in1TabletWearable

on(type: 'indoorMapEnter', callback: Callback<IndoorMapInfo>): void

监听室内图进入事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.1.1(19)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'indoorMapEnter'：监听室内图进入事件。 |
| callback | Callback<[IndoorMapInfo](map-map-indoormapinfo.md)> | 是 | 回调函数，返回[IndoorMapInfo](map-map-indoormapinfo.md)，监听室内图进入事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let callback = (indoorMapInfo: map.IndoorMapInfo) => {
2. console.info("indoorMapEnter", `callback indoorMapInfo`);
3. };
4. mapEventManager.on("indoorMapEnter", callback);
```

### off('indoorMapEnter')

PhonePC/2in1TabletWearable

off(type: 'indoorMapEnter', callback?: Callback<IndoorMapInfo>): void

取消监听室内图进入事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.1.1(19)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'indoorMapEnter'：监听室内图进入事件。 |
| callback | Callback<[IndoorMapInfo](map-map-indoormapinfo.md)> | 否 | 回调函数，返回[IndoorMapInfo](map-map-indoormapinfo.md)，取消监听室内图进入事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let callback = (indoorMapInfo: map.IndoorMapInfo) => {
2. console.info("indoorMapEnter", `callback`);
3. };
4. mapEventManager.on("indoorMapEnter", callback);

6. // 取消callback对象的事件响应
7. mapEventManager.off('indoorMapEnter', callback);
```

### on('indoorMapExit')

PhonePC/2in1TabletWearable

on(type: 'indoorMapExit', callback: Callback<void>): void

监听室内图退出事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.1.1(19)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'indoorMapExit'：监听室内图退出事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数，监听室内图退出事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let callback = () => {
2. console.info("indoorMapExit", `callback`);
3. };
4. mapEventManager.on("indoorMapExit", callback);
```

### off('indoorMapExit')

PhonePC/2in1TabletWearable

off(type: 'indoorMapExit', callback?: Callback<void>): void

取消监听室内图退出事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.1.1(19)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'indoorMapExit'：监听室内图退出事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果的回调函数，取消监听室内图退出事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let callback = () => {
2. console.info("indoorMapExit", `callback`);
3. };
4. mapEventManager.on("indoorMapExit", callback);

6. // 取消callback对象的事件响应
7. mapEventManager.off('indoorMapExit', callback);
```

### on('massPointOverlayClick')

PhonePC/2in1TabletWearable

on(type: 'massPointOverlayClick', callback: MassPointOverlayCallback): void

监听海量点图层点击事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'massPointOverlayClick'：用于监听海量点图层的点击事件。 |
| callback | [MassPointOverlayCallback](map-map-masspointoverlaycallback.md) | 是 | 回调函数，无返回结果的回调函数，监听海量点图层点击事件。 |

**示例：**

```
1. // 初始化地图组件的监听事件管理接口
2. let mapEventManager = this.mapController.getEventManager();
3. let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
4. console.info(`overlayId:${overlay.getId()},item :${JSON.stringify(item)}`);
5. }
6. // 启动海量点点击事件监听
7. mapEventManager.on('massPointOverlayClick', massCallback);
```

### off('massPointOverlayClick')

PhonePC/2in1TabletWearable

off(type: 'massPointOverlayClick', callback?: MassPointOverlayCallback): void

取消监听海量点图层点击事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'massPointOverlayClick'：监听海量点图层点击退出事件。 |
| callback | [MassPointOverlayCallback](map-map-masspointoverlaycallback.md) | 否 | 回调函数，无返回结果的回调函数，取消监听海量点图层点击事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```
1. // 初始化地图组件的监听事件管理接口
2. let mapEventManager = this.mapController.getEventManager();
3. let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
4. console.info(`overlayId:${overlay.getId()},item :${JSON.stringify(item)}`);
5. }
6. // 启动海量点点击事件监听
7. mapEventManager.on('massPointOverlayClick', massCallback);
8. // 停止海量点点击事件监听,传入指定callback
9. mapEventManager.off('massPointOverlayClick', massCallback);
10. // 停止所有海量点点击事件监听，无需传入callback
11. mapEventManager.off('massPointOverlayClick');
```
