---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-uigestureevent
title: 设置组件绑定的手势
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 绑定手势 > 设置组件绑定的手势
category: harmonyos-references
scraped_at: 2026-04-28T08:01:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:04479c316ebe5cd8d7556edb6549964d3e1f7db4f6014e36d3adf0caaf671c76
---

用于设置组件绑定的手势。可以通过UIGestureEvent对象调用其接口添加或删除手势。

说明

本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

## UIGestureEvent

PhonePC/2in1TabletTVWearable

用于设置组件绑定的手势。

### addGesture

PhonePC/2in1TabletTVWearable

addGesture<T>(gesture: GestureHandler<T>, priority?: GesturePriority, mask?: GestureMask): void

添加手势。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gesture | [GestureHandler<T>](ts-gesturehandler.md#gesturehandlert) | 是 | 手势处理器对象。 |
| priority | [GesturePriority](ts-gesturehandler.md#gesturepriority枚举说明) | 否 | 绑定手势的优先级。  默认值：GesturePriority.NORMAL |
| mask | [GestureMask](ts-gesture-common.md#gesturemask枚举说明) | 否 | 事件响应设置。  默认值：GestureMask.Normal |

### addParallelGesture

PhonePC/2in1TabletTVWearable

addParallelGesture<T>(gesture: GestureHandler<T>, mask?: GestureMask): void

绑定可与子组件手势同时触发的手势。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gesture | [GestureHandler<T>](ts-gesturehandler.md#gesturehandlert) | 是 | 手势处理器对象。 |
| mask | [GestureMask](ts-gesture-common.md#gesturemask枚举说明) | 否 | 事件响应设置。  默认值：GestureMask.Normal |

### removeGestureByTag

PhonePC/2in1TabletTVWearable

removeGestureByTag(tag: string): void

移除该组件上通过modifier绑定的设置为指定标志的手势。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string | 是 | 手势处理器标志。 |

### clearGestures

PhonePC/2in1TabletTVWearable

clearGestures(): void

清除该组件上通过modifier绑定的所有手势。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 示例

PhonePC/2in1TabletTVWearable

见[动态手势设置](ts-universal-attributes-gesture-modifier.md)。
