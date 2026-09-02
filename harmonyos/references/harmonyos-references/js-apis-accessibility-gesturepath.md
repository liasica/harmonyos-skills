---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath
title: "@ohos.accessibility.GesturePath (手势路径)"
breadcrumb: API参考 > 应用框架 > Accessibility Kit（无障碍服务） > ArkTS API > @ohos.accessibility.GesturePath (手势路径)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f7e3afe069d90aef635ef30fe1fd15920a5772bba557a54c39bfbfe900ba610
---

GesturePath表示手势路径信息。

本模块用于创建手势路径信息，供辅助功能注入手势使用。

**说明** 

* 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { GesturePath } from '@kit.AccessibilityKit';
```

## GesturePath

表示手势路径信息，用于无障碍服务中模拟用户触摸手势（如点击、滑动等）。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| points | Array<[GesturePoint](js-apis-accessibility-gesturepoint.md#gesturepoint)> | 否 | 否 | 手势路径上的触摸点序列，用于构成手势的移动轨迹。每个触摸点表示路径中的一个坐标位置。数组长度需大于0。 |
| durationTime | number | 否 | 否 | 手势总耗时，单位：ms。取值需大于0。 |

### constructor(deprecated)

constructor(durationTime: number)

通过传入手势总耗时创建手势路径对象。创建GesturePath实例后，还需设置必填属性points。

**说明** 

从API version 9开始支持，从API version 12开始废弃。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| durationTime | number | 是 | 手势总耗时，单位：ms。取值需大于0。 |

**示例：**

```ts
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
let startPoint = new GesturePoint(100, 100);
let endPoint = new GesturePoint(200, 200);
gesturePath.points = [startPoint, endPoint];
```
