---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-multimodalinput-gestureevent
title: @ohos.multimodalInput.gestureEvent (手势事件)
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.gestureEvent (手势事件)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a2279d1e86f9b7309d7b1719e2e46b9312d0a8ae5380bc16d132440730bdd3d7
---

设备上报的手势事件。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Rotate, Pinch, ThreeFingersSwipe, FourFingersSwipe, ActionType } from '@kit.InputKit';
```

## Pinch

PhonePC/2in1TabletTVWearable

捏合手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| scale | number | 否 | 否 | 捏合度，取值范围大于等于0。 |

## Rotate11+

PhonePC/2in1TabletTVWearable

旋转手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| angle | number | 否 | 否 | 旋转角度。 |

## ThreeFingersSwipe

PhonePC/2in1TabletTVWearable

三指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x。 |
| y | number | 否 | 否 | 坐标y。 |

## FourFingersSwipe

PhonePC/2in1TabletTVWearable

四指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x。 |
| y | number | 否 | 否 | 坐标y。 |

## ThreeFingersTap11+

PhonePC/2in1TabletTVWearable

三指轻点手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ActionType](js-apis-multimodalinput-gestureevent.md#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |

## ActionType

PhonePC/2in1TabletTVWearable

手势事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CANCEL | 0 | 取消。 |
| BEGIN | 1 | 手势开始。 |
| UPDATE | 2 | 手势更新。 |
| END | 3 | 手势结束。 |
