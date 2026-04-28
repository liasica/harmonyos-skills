---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-newcameraposition
title: newCameraPosition
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > newCameraPosition
category: harmonyos-references
scraped_at: 2026-04-28T08:17:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f238a0d60a9812224f05dae807deef89b7be12c3f030fcbd100a58ebf318d503
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## newCameraPosition

PhonePC/2in1TabletWearable

newCameraPosition(cameraPosition: mapCommon.CameraPosition): CameraUpdate

创建CameraUpdate对象，更新地图状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| cameraPosition | [mapCommon.CameraPosition](map-common.md#cameraposition) | 是 | 新的地图状态。 |

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
1. let target: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraPosition: mapCommon.CameraPosition = {
6. target: target,
7. zoom: 10
8. };
9. let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
```
