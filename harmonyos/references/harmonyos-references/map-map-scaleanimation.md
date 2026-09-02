---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-scaleanimation
title: Class (ScaleAnimation)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (ScaleAnimation)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d64aa70cabafb476ef032e7b62d747c611731e1e2317fae42f17d7f517d812f
---

## 导入模块

```typescript
import { map } from '@kit.MapKit';
```

## ScaleAnimation

控制缩放的动画类，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

constructor(fromX: number, toX: number, fromY: number, toY: number)

构造器，构造控制缩放的动画实例。

**说明** 

0表示动画缩小消失。

1表示动画不缩放。

小于1的值表示动画缩小。

大于1的值表示动画放大。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromX | number | 是 | 指动画开始时应用的水平缩放倍数，负数按0处理，异常值不处理。 |
| toX | number | 是 | 指动画结束时应用的水平缩放倍数，负数按0处理，异常值不处理。 |
| fromY | number | 是 | 指动画开始时应用的垂直缩放倍数，负数按0处理，异常值不处理。 |
| toY | number | 是 | 指动画结束时应用的垂直缩放倍数，负数按0处理，异常值不处理。 |

**示例：**

```typescript
let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
```
