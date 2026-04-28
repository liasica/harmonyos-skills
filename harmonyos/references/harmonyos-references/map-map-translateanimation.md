---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-translateanimation
title: TranslateAnimation
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > TranslateAnimation
category: harmonyos-references
scraped_at: 2026-04-28T08:17:15+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:df7194bb23e87b43733766b2d25ace6d938de7924ac2bd7fb198360e0ee64044
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## TranslateAnimation

PhonePC/2in1TabletWearable

控制移动的动画类，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

PhonePC/2in1TabletWearable

constructor(target: mapCommon.LatLng)

构造器，构造控制移动的动画实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| target | [mapCommon.LatLng](map-common.md#latlng) | 是 | 需要移动的目标位置，位置类型为经纬度，异常值不处理。 |

**示例：**

```
1. let target: mapCommon.LatLng = {
2. latitude: 31,
3. longitude: 118
4. };
5. let animation: map.TranslateAnimation = new map.TranslateAnimation(target);
```
