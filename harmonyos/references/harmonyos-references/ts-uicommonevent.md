---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-uicommonevent
title: 设置事件回调
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 公共定义 > 设置事件回调
category: harmonyos-references
scraped_at: 2026-09-02T15:01:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6c5b122497ef4f4f3743e24e2e116291cc1e67faa8451889da1f65df3f5f27a8
---

**说明** 

* 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## UICommonEvent

用于设置组件基础事件回调，覆盖点击、触摸、显示/消失、按键、焦点、悬浮、鼠标、组件区域变化和可见区域变化等事件；方法入参为undefined时，重置对应的事件回调，适用于集中配置和清理组件基础事件处理逻辑的场景。

### setOnClick

setOnClick(callback: Callback<ClickEvent> | undefined): void

设置[点击事件](ts-universal-events-click.md)的回调。当callback为undefined时，重置点击事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[ClickEvent](ts-universal-events-click.md#clickevent)> | undefined | 是 | 点击事件的回调函数，签名为 (event: ClickEvent) => void，用于在组件触发点击事件时接收点击事件对象。 |

### setOnTouch

setOnTouch(callback: Callback<TouchEvent> | undefined): void

设置[触摸事件](ts-universal-events-touch.md)的回调。当callback为undefined时，重置触摸事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)> | undefined | 是 | 触摸事件的回调函数，签名为 (event: TouchEvent) => void，用于在组件触发触摸事件时接收触摸事件对象。 |

### setOnAppear

setOnAppear(callback: Callback<void> | undefined): void

设置[onAppear](ts-universal-events-show-hide.md#onappear)挂载显示事件的回调。当callback为undefined时，重置挂载显示事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 挂载显示事件的回调函数，签名为 () => void，用于组件挂载显示时触发。 |

### setOnDisappear

setOnDisappear(callback: Callback<void> | undefined): void

设置[onDisappear](ts-universal-events-show-hide.md#ondisappear)卸载消失事件的回调。当callback为undefined时，重置卸载消失事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 卸载消失事件的回调函数，签名为 () => void，用于组件卸载消失时触发。 |

### setOnKeyEvent

setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void

设置[按键事件](ts-universal-events-key.md)的回调。当callback为undefined时，重置按键事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[KeyEvent](ts-universal-events-key.md#keyevent对象说明)> | undefined | 是 | 按键事件的回调函数，签名为 (event: KeyEvent) => void，用于在组件触发按键事件时接收按键事件对象。 |

### setOnFocus

setOnFocus(callback: Callback<void> | undefined): void

设置[onFocus](ts-universal-focus-event.md#onfocus)获焦事件的回调。当callback为undefined时，重置获焦事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 获焦事件的回调函数，签名为 () => void，用于组件获得焦点时触发。 |

### setOnBlur

setOnBlur(callback: Callback<void> | undefined): void

设置[onBlur](ts-universal-focus-event.md#onblur)失焦事件的回调。当callback为undefined时，重置失焦事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | 失焦事件的回调函数，签名为 () => void，用于组件失去焦点时触发。 |

### setOnHover

setOnHover(callback: HoverCallback | undefined): void

设置[onHover](ts-universal-events-hover.md#onhover)悬浮事件的回调。当callback为undefined时，重置悬浮事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [HoverCallback](ts-uicommonevent.md#hovercallback) | undefined | 是 | 悬浮事件的回调函数，签名为 (isHover: boolean, event: HoverEvent) => void，用于组件进入或退出悬浮状态时接收悬浮状态和事件对象。 |

### setOnMouse

setOnMouse(callback: Callback<MouseEvent> | undefined): void

设置[onMouse](ts-universal-mouse-key.md#onmouse)鼠标事件的回调。当callback为undefined时，重置鼠标事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<[MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明)> | undefined | 是 | 鼠标事件的回调函数，签名为 (event: MouseEvent) => void，用于在组件触发鼠标事件时接收鼠标事件对象。 |

### setOnSizeChange

setOnSizeChange(callback: SizeChangeCallback | undefined): void

设置[onSizeChange](ts-universal-component-size-change-event.md#onsizechange)组件区域变化事件的回调。当callback为undefined时，重置组件区域变化事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SizeChangeCallback](ts-universal-component-size-change-event.md#sizechangecallback) | undefined | 是 | 组件区域变化事件的回调函数，签名为 (oldValue: SizeOptions, newValue: SizeOptions) => void，用于在组件区域尺寸发生变化时接收变化前后的尺寸信息。其中 oldValue 表示变化前的尺寸信息，newValue 表示变化后的尺寸信息。 |

### setOnVisibleAreaApproximateChange

setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void

设置限制回调间隔的[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)可见区域变化事件的回调。当event为undefined时，重置可见区域变化事件的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [VisibleAreaEventOptions](ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12) | 是 | 可见区域变化事件的配置参数，用于设置可见面积比例阈值和期望更新间隔；当前接口的可见区域回调阈值默认包含0，当组件可见面积与自身面积的比值接近实际生效的阈值时触发 event 回调。 |
| event | [VisibleAreaChangeCallback](ts-universal-component-visible-area-change-event.md#visibleareachangecallback12) | undefined | 是 | 可见区域变化事件的回调函数，签名为 (isExpanding: boolean, currentRatio: number) => void。当组件可见面积与自身面积的比值接近options中设置的阈值时触发该回调，其中 isExpanding 表示可见区域比例是否正在增大，currentRatio 表示当前可见面积与组件自身面积的比值。为undefined时，重置可见区域变化事件的回调。 |

**说明**

此接口与 [onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange) 接口存在如下差异，onVisibleAreaChange 在每一帧都会进行可见区域比例的计算，注册节点数量增加时，系统功耗可能升高。此接口降低了可见区域比例计算的频度，计算间隔由 [VisibleAreaEventOptions](ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12) 的 expectedUpdateInterval 参数决定。

当前接口的可见区域回调阈值默认包含0。例如，开发者设置回调阈值为[0.5]，实际生效的阈值为[0.0, 0.5]。

## HoverCallback

type HoverCallback = (isHover: boolean, event: HoverEvent)=> void

悬浮事件的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isHover | boolean | 是 | 是否处于悬浮状态，true 表示处于悬浮状态，false 表示不处于悬浮状态。 |
| event | [HoverEvent](ts-universal-events-hover.md#hoverevent10对象说明) | 是 | 鼠标或手写笔悬浮事件对象，用于提供悬浮位置坐标等事件信息。 |
