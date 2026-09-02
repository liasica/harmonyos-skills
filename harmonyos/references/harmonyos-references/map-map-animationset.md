---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animationset
title: Class (AnimationSet)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (AnimationSet)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:088754fc521f48bffa1e0bd8595abe8ef3f094f86531e242cf788497a9f76b9c
---

## 导入模块

```typescript
import { map } from '@kit.MapKit';
```

## AnimationSet

动画类的集合，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

constructor(shareInterpolator: boolean)

构造器，构造动画类的集合实例。

**说明** 

动画类集合继承[Animation](map-map-animation.md)方法，仅shareInterpolator为true时共享插值器，其余属性不共享且不可设置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| shareInterpolator | boolean | 是 | 定义是否共享插值器。  - true：共享  - false：不共享 |

**示例：**

```typescript
// 创建透明度动画：从完全透明(0.2)到完全不透明(1)
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
// 创建旋转动画：从15度旋转到150度
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
// 创建缩放动画：从原大小(1)缩放到3倍
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
// 创建动画集合，true表示同一时刻仅播放一个动画
let animation: map.AnimationSet = new map.AnimationSet(true);
// 设置动画插值器为线性插值（匀速播放）
animation.setInterpolator(Curve.Linear);
// 向动画集合中添加上述三个动画
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
// 清空动画集合
animation.clearAnimation();
```

### addAnimation

addAnimation(animation: Animation): void

动画类集合增加动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| animation | [Animation](map-map-animation.md) | 是 | 要添加的动画对象。 |

**示例：**

```typescript
// 创建透明度动画：从完全透明(0.2)渐变到完全不透明(1)
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
// 创建旋转动画：从15度旋转到150度
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
// 创建缩放动画：从原大小(1,1)缩放到(3,3)
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
// 创建动画集合，true表示同一时刻仅播放一个动画（取消前一动画再播放下一）
let animation: map.AnimationSet = new map.AnimationSet(true);
// 向动画集合中添加透明度动画
animation.addAnimation(animation1);
// 向动画集合中添加旋转动画
animation.addAnimation(animation2);
// 向动画集合中添加缩放动画
animation.addAnimation(animation3);
```

### clearAnimation

clearAnimation(): void

清空动画类集合。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
// 创建透明度动画：从完全透明(0.2)渐变到完全不透明(1)
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
// 创建旋转动画：从15度旋转到150度
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
// 创建缩放动画：从原大小(1,1)缩放到(3,3)
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
// 创建动画集合，true表示同一时刻仅播放一个动画（取消前一动画再播放下一动画）
let animation: map.AnimationSet = new map.AnimationSet(true);
// 向动画集合中添加透明度动画
animation.addAnimation(animation1);
// 向动画集合中添加旋转动画
animation.addAnimation(animation2);
// 向动画集合中添加缩放动画
animation.addAnimation(animation3);
// 清空动画集合
animation.clearAnimation();
```
