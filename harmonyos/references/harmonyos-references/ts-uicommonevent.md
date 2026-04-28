---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-uicommonevent
title: 设置事件回调
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 公共定义 > 设置事件回调
category: harmonyos-references
scraped_at: 2026-04-28T08:02:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5ee038128b512c157c8bae3410aca4d6f775b6e977a9a4065360e2f3e8d41355
---

说明

本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## UICommonEvent

PhonePC/2in1TabletTVWearable

用于设置基础事件回调。方法入参为undefined的时候，重置对应的事件回调。

### setOnClick

PhonePC/2in1TabletTVWearable

setOnClick(callback: Callback<ClickEvent> | undefined): void

设置[点击事件](ts-universal-events-click.md)的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[ClickEvent](ts-universal-events-click.md#clickevent)> | undefined | 是 | 点击事件的回调函数。 |

### setOnTouch

PhonePC/2in1TabletTVWearable

setOnTouch(callback: Callback<TouchEvent> | undefined): void

设置[触摸事件](ts-universal-events-touch.md)的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)> | undefined | 是 | 触摸事件的回调函数。 |

### setOnAppear

PhonePC/2in1TabletTVWearable

setOnAppear(callback: Callback<void> | undefined): void

设置[onAppear](ts-universal-events-show-hide.md#onappear)挂载显示事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 挂载显示事件的回调函数。 |

### setOnDisappear

PhonePC/2in1TabletTVWearable

setOnDisappear(callback: Callback<void> | undefined): void

设置[onDisAppear](ts-universal-events-show-hide.md#ondisappear)卸载消失事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 卸载消失事件的回调。 |

### setOnKeyEvent

PhonePC/2in1TabletTVWearable

setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void

设置[按键事件](ts-universal-events-key.md)的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[KeyEvent](ts-universal-events-key.md#keyevent对象说明)> | undefined | 是 | 按键事件的回调函数。 |

### setOnFocus

PhonePC/2in1TabletTVWearable

setOnFocus(callback: Callback<void> | undefined): void

设置[onFocus](ts-universal-focus-event.md#onfocus)获焦事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 获焦事件的回调。 |

### setOnBlur

PhonePC/2in1TabletTVWearable

setOnBlur(callback: Callback<void> | undefined): void

设置[onBlur](ts-universal-focus-event.md#onblur)失焦事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 失焦事件的回调。 |

### setOnHover

PhonePC/2in1TabletTVWearable

setOnHover(callback: HoverCallback | undefined): void

设置[onHover](ts-universal-events-hover.md#onhover)悬浮事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [HoverCallback](ts-uicommonevent.md#hovercallback) | undefined | 是 | 悬浮事件的回调函数。 |

### setOnMouse

PhonePC/2in1TabletTVWearable

setOnMouse(callback: Callback<MouseEvent> | undefined): void

设置[onMouse](ts-universal-mouse-key.md#onmouse)鼠标事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明)> | undefined | 是 | 鼠标事件的回调函数。 |

### setOnSizeChange

PhonePC/2in1TabletTVWearable

setOnSizeChange(callback: SizeChangeCallback | undefined): void

设置[onSizeChange](ts-universal-component-size-change-event.md#onsizechange)组件区域变化事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SizeChangeCallback](ts-universal-component-size-change-event.md#sizechangecallback) | undefined | 是 | 组件区域变化事件的回调函数。 |

### setOnVisibleAreaApproximateChange

PhonePC/2in1TabletTVWearable

setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void

设置限制回调间隔的[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)可见区域变化事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [VisibleAreaEventOptions](ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12) | 是 | 可见区域变化相关的参数。 |
| event | [VisibleAreaChangeCallback](ts-universal-component-visible-area-change-event.md#visibleareachangecallback12) | undefined | 是 | 可见区域变化事件的回调函数。当组件可见面积与自身面积的比值接近options中设置的阈值时触发该回调。 |

说明

此接口与[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)接口存在如下差异，onVisibleAreaChange在每一帧都会进行可见区域比例的计算，如果注册节点太多，系统功耗存在劣化。此接口降低了可见区域比例计算的频度，计算间隔由[VisibleAreaEventOptions](ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12)的expectedUpdateInterval参数决定。

当前接口的可见区域回调阈值默认包含0。例如，开发者设置回调阈值为[0.5]，实际生效的阈值为[0.0, 0.5]。

## HoverCallback

PhonePC/2in1TabletTVWearable

type HoverCallback = (isHover: boolean, event: HoverEvent)=> void

hover事件的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isHover | boolean | 是 | 是否处于hover状态，true表示处于hover状态，false表示不在hover状态。 |
| event | [HoverEvent](ts-universal-events-hover.md#hoverevent10对象说明) | 是 | 获取鼠标或手写笔悬浮的位置坐标。 |
