---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepoint
title: @ohos.accessibility.GesturePoint (手势触摸点)
breadcrumb: API参考 > 应用框架 > Accessibility Kit（无障碍服务） > ArkTS API > @ohos.accessibility.GesturePoint (手势触摸点)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dc165627853c2a637754a243aa1eef5e0669bcf304cd0b657d12a51b9c860565
---

GesturePoint表示手势触摸点。

本模块用于创建辅助功能注入手势所需的手势路径的触摸点信息。

说明

* 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { GesturePoint } from '@kit.AccessibilityKit';
```

## GesturePoint

PhonePC/2in1TabletWearable

表示手势触摸点。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| positionX | number | 否 | 否 | 触摸点X坐标。 |
| positionY | number | 否 | 否 | 触摸点Y坐标。 |

### constructor(deprecated)

PhonePC/2in1TabletWearable

constructor(positionX: number, positionY: number);

构造函数。

说明

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionX | number | 是 | 触摸点X坐标。 |
| positionY | number | 是 | 触摸点Y坐标。 |

**示例：**

```
1. import { GesturePoint } from '@kit.AccessibilityKit';

3. let gesturePoint = new GesturePoint(1, 2);
```
