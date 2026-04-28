---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animationset
title: AnimationSet
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > AnimationSet
category: harmonyos-references
scraped_at: 2026-04-28T08:17:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:053ca4706ef9cb39a3484d1da7fdbea464c6711ca58140cb00121f5ecf4e12b8
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```

## AnimationSet

PhonePC/2in1TabletWearable

动画类的集合，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

PhonePC/2in1TabletWearable

constructor(shareInterpolator: boolean)

构造器，构造动画类的集合实例。

说明

动画类集合继承[Animation](map-map-animation.md)方法，仅shareInterpolator为true时共享插值器，其他属性不共享，不支持设置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| shareInterpolator | boolean | 是 | 定义是否共享插值器。  - true：共享  - false：不共享 |

**示例：**

```
1. let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
2. let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
3. let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
4. let animation = new map.AnimationSet(true);
5. animation.setInterpolator(Curve.Linear);
6. animation.addAnimation(animation1);
7. animation.addAnimation(animation2);
8. animation.addAnimation(animation3);
9. animation.clearAnimation();
```

### addAnimation

PhonePC/2in1TabletWearable

addAnimation(animation: Animation): void

动画类集合增加动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| animation | [Animation](map-map-animation.md) | 是 | 动画类集合增加动画。 |

**示例：**

```
1. let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
2. let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
3. let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
4. let animation = new map.AnimationSet(true);
5. animation.addAnimation(animation1);
6. animation.addAnimation(animation2);
7. animation.addAnimation(animation3);
```

### clearAnimation

PhonePC/2in1TabletWearable

clearAnimation(): void

清空动画类集合。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
2. let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
3. let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
4. let animation = new map.AnimationSet(true);
5. animation.addAnimation(animation1);
6. animation.addAnimation(animation2);
7. animation.addAnimation(animation3);
8. animation.clearAnimation();
```
