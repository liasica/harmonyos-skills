---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-zoomout
title: zoomOut
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > zoomOut
category: harmonyos-references
scraped_at: 2026-04-28T08:17:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68291a544296532f2b5e12c2dc997ad588236f455ddb352e7a1981c22921409a
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```

## zoomOut

PhonePC/2in1TabletWearable

zoomOut(): CameraUpdate

缩小地图缩放级别，在当前地图显示的级别基础上减1。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](map-map-cameraupdate.md) | 描述地图状态将要发生的变化。 |

**示例：**

```
1. let cameraUpdate: map.CameraUpdate = map.zoomOut();
```
