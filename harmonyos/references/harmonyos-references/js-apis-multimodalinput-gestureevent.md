---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-multimodalinput-gestureevent
title: "@ohos.multimodalInput.gestureEvent (手势事件)"
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.gestureEvent (手势事件)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a3e7f4f18fc9dde0443ae2494e35bcb05d041412d29de0383abe47e47cccb2ec
---

设备上报的手势事件。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { Rotate, Pinch, ThreeFingersSwipe, FourFingersSwipe, ThreeFingersTap, ActionType } from '@kit.InputKit';
```

## Pinch

捏合手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型，包括手势取消、手势开始、手势更新、手势结束。 |
| scale | number | 否 | 否 | 捏合度，取值范围大于等于0。 |

## Rotate11+

旋转手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| angle | number | 否 | 否 | 旋转角度，单位为度。 |

## ThreeFingersSwipe

三指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x，单位为像素（px）。 |
| y | number | 否 | 否 | 坐标y，单位为像素（px）。 |

## FourFingersSwipe

四指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x，单位为像素（px）。 |
| y | number | 否 | 否 | 坐标y，单位为像素（px）。 |

## ThreeFingersTap11+

三指轻点手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |

## ActionType

手势事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CANCEL | 0 | 手势取消。 |
| BEGIN | 1 | 手势开始。 |
| UPDATE | 2 | 手势更新。 |
| END | 3 | 手势结束。 |
