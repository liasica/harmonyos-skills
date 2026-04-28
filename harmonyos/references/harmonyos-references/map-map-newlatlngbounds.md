---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-newlatlngbounds
title: newLatLngBounds
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > newLatLngBounds
category: harmonyos-references
scraped_at: 2026-04-28T08:17:21+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ce55e3be545ad5acc29f051a8221a9d1d04c81662abd4be038279c60954ddcbc
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## newLatLngBounds

PhonePC/2in1TabletWearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding?: number): CameraUpdate

设置地图经纬度范围、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 地图显示经纬度范围。 |
| padding | number | 否 | 地图区域和边界之间的距离，单位：px，异常值返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 33,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 32,
8. longitude: 119
9. }
10. };
11. let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 5);
```

## newLatLngBounds

PhonePC/2in1TabletWearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, width: number, height: number, padding: number): CameraUpdate

设置地图经纬度范围、经纬度矩形范围的高和宽、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 地图显示经纬度范围。 |
| width | number | 是 | 经纬度矩形范围的屏幕宽，单位：px，取值范围：大于等于0，异常值返回401错误码。 |
| height | number | 是 | 经纬度矩形范围的屏幕高，单位：px，取值范围：大于等于0，异常值返回401错误码。 |
| padding | number | 是 | 地图区域和边界之间的距离，单位：px，异常值返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 31,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 30.5,
8. longitude: 123
9. }
10. };
11. // 设置地图显示经纬度范围，设置经纬度矩形范围的宽为1000像素，设置经纬度矩形范围的高为1000像素，设置地图区域和边界之间的距离为100像素
12. let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 1000, 1000, 100);
```

## newLatLngBounds

PhonePC/2in1TabletWearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding: mapCommon.Padding): CameraUpdate

设置地图经纬度范围和4个方向与边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.1(13)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 地图显示经纬度范围，异常值返回401错误码。 |
| padding | [mapCommon.Padding](map-common.md#padding) | 是 | 地图区域和边界之间的距离，单位：px，异常值返回401错误码。  **说明：**  - 地图组件高度减去padding的top值和bottom值，结果需要大于等于100px。  - 地图组件宽度减去padding的left值和right值，结果需要大于等于100px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 31,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 30.5,
8. longitude: 123
9. }
10. };
11. // 初始化参数，左边距0，底边距50
12. let padding: mapCommon.Padding = {
13. left: 0,
14. bottom: 50
15. };
16. let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, padding);
```
