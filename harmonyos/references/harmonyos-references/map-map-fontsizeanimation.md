---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-fontsizeanimation
title: FontSizeAnimation
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > FontSizeAnimation
category: harmonyos-references
scraped_at: 2026-04-28T08:17:15+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f88bbfc3a3dbd849c97909a4d2a1e5a32a11eba2874b6d9b2077c434040535d2
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map } from '@kit.MapKit';
```

## FontSizeAnimation

PhonePC/2in1TabletWearable

控制字体大小的动画类，继承[Animation](map-map-animation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### constructor

PhonePC/2in1TabletWearable

constructor(fromSize: number, toSize: number)

构造器，构造控制字体大小的动画实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fromSize | number | 是 | 起始的字体大小。取值范围：[0，100]，单位：px，异常值不处理。 |
| toSize | number | 是 | 目标的字体大小。取值范围：[0，100]，单位：px，异常值不处理。 |

**示例：**

```
1. let animation: map.FontSizeAnimation = new map.FontSizeAnimation(5, 25);
```
