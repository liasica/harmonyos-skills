---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-alphaanimation
title: Class (AlphaAnimation)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (AlphaAnimation)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:946fc445c15ff0f3abfcd9b46fa1490a57e290e9f190b899ee3e473ff79dc790
---

## 导入模块

```typescript
import { map } from '@kit.MapKit';
```

## AlphaAnimation

控制透明度的动画类，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

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

```typescript
let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
```
