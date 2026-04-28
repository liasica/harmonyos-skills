---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-alphaanimation
title: AlphaAnimation
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > AlphaAnimation
category: harmonyos-references
scraped_at: 2026-04-28T08:17:15+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:949d3bc640428a5b786a998e4310f8b9fae6f19b5e7f70a3b6e022b4c4c4cc52
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```

## AlphaAnimation

PhonePC/2in1TabletWearable

控制透明度的动画类，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

PhonePC/2in1TabletWearable

constructor(fromAlpha: number, toAlpha: number)

构造器，构造控制透明度的动画实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromAlpha | number | 是 | 起始透明度。透明度范围为[0, 1]，1为不透明，0为完全透明，异常值不处理。 |
| toAlpha | number | 是 | 目标透明度。透明度范围为[0, 1]，1为不透明，0为完全透明，异常值不处理。 |

**示例：**

```
1. let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
```
