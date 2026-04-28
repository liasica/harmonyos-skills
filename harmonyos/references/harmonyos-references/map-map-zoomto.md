---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-zoomto
title: zoomTo
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > zoomTo
category: harmonyos-references
scraped_at: 2026-04-28T08:17:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6bf1d913cdbaa4174bfa9cdc5567eceb1d53a19095d91e8e49eadd6336cadf49
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```

## zoomTo

PhonePC/2in1TabletWearable

zoomTo(zoom: number): CameraUpdate

设置地图缩放级别。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| zoom | number | 是 | 地图缩放级别，取值范围为[2, 20]，超出按边界值处理。 |

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
1. let cameraUpdate: map.CameraUpdate = map.zoomTo(10);
```
