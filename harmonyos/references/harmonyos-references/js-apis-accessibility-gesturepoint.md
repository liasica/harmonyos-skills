---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepoint
title: "@ohos.accessibility.GesturePoint (手势触摸点)"
breadcrumb: API参考 > 应用框架 > Accessibility Kit（无障碍服务） > ArkTS API > @ohos.accessibility.GesturePoint (手势触摸点)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1c29cc86b79763f97cb13549ddd2d4fe948bace0e07310e14b35eb1c940ca02b
---

GesturePoint表示手势触摸点，是构成手势路径GesturePath的基本单元。

本模块用于创建手势路径的触摸点信息，供辅助功能注入手势使用。

**说明** 

* 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { GesturePoint } from '@kit.AccessibilityKit';
```

## GesturePoint

表示手势触摸点，是构成GesturePath路径节点的基本单元，用于定义辅助功能注入手势轨迹中的触摸位置。详细使用方式请参见[GesturePath](js-apis-accessibility-gesturepath.md)。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| positionX | number | 否 | 否 | 触摸点X坐标，单位为像素（px）。 |
| positionY | number | 否 | 否 | 触摸点Y坐标，单位为像素（px）。 |

### constructor(deprecated)

constructor(positionX: number, positionY: number)

根据传入的X坐标和Y坐标创建GesturePoint实例。

**说明** 

从API version 9开始支持，从API version 12开始废弃。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionX | number | 是 | 触摸点X坐标，单位为像素（px）。 |
| positionY | number | 是 | 触摸点Y坐标，单位为像素（px）。 |

**示例：**

```ts
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```
