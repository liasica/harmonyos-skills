---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesturehandler
title: 手势处理器
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 绑定手势 > 手势处理器
category: harmonyos-references
scraped_at: 2026-09-02T15:00:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6be5859eef13e94fb0f82bca6a973be5f8e681bbb44db9848c8c9aa35ac9dc59
---

用于设置组件绑定的手势。支持点击、长按、滑动、快滑、捏合、旋转及手势组等手势处理器，适用于需要为组件动态添加、删除或配置交互手势的场景，可帮助开发者统一管理组件手势交互。可以通过[UIGestureEvent](ts-uigestureevent.md#uigestureevent)对象调用其接口添加或删除手势。

**说明** 

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## GestureHandler<T>

手势处理器的基础类型，用于承载具体手势处理器的通用配置能力，例如设置手势标志和限定支持的事件输入源。

### tag

tag(tag: string): T

设置手势处理器的标志，适用于需要区分或管理多个手势处理器的场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string | 是 | 手势处理器的标志。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前手势处理器对象。 |

### allowedTypes14+

allowedTypes(types: Array<SourceTool>): T

设置手势处理器所支持的事件输入源，适用于需要限定手势仅响应触控、鼠标或手写笔等特定输入源的场景。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array<[SourceTool](ts-gesture-settings.md#sourcetool枚举说明9)> | 是 | 手势处理器所支持的事件输入源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BaseHandlerOptions15+

基础手势处理器配置参数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isFingerCountLimited | boolean | 否 | 是 | 是否检查触摸屏幕的手指数量。true表示检查触摸屏幕的手指数量，false表示不检查触摸屏幕的手指数量。  默认值：false |

## TapGestureHandler

点击手势处理器对象类型，用于识别组件上的点击交互，适用于单击、多击或多指点击等触控场景，并支持配置点击次数、触发手指数等识别条件。

### constructor

constructor(options?: TapGestureHandlerOptions)

点击手势处理器的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TapGestureHandlerOptions](ts-gesturehandler.md#tapgesturehandleroptions) | 否 | 点击手势处理器配置参数。当需要自定义连续点击次数、触发点击的手指数、手指数量校验或点击手势移动阈值时传入；不传入时使用点击手势处理器默认配置，如连续点击次数为1、触发手指数为1、默认不检查触摸屏幕的手指数量。 |

### onAction

onAction(event: Callback<GestureEvent>): TapGestureHandler

设置点击手势处理器识别成功回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 点击手势处理器识别成功回调，回调参数为GestureEvent对象，用于获取点击手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TapGestureHandler](ts-gesturehandler.md#tapgesturehandler) | 返回当前点击手势处理器对象。 |

## TapGestureHandlerOptions

点击手势处理器配置参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 否 | 是 | 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。  默认值：1  取值范围：[0, +∞)  **说明：**  1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。  2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fingers | number | 否 | 是 | 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值。  默认值：1  **说明：**  1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。  2. 未开启isFingerCountLimited时，实际点击手指数超过配置值，手势识别成功；开启isFingerCountLimited时，触摸手指数量需等于配置值，否则手势识别失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isFingerCountLimited15+ | boolean | 否 | 是 | 是否检查触摸屏幕的手指数量。true表示检查触摸屏幕的手指数量，false表示不检查触摸屏幕的手指数量。如果触摸手指的数量不等于设置的触发点击的手指数（即上述fingers参数），那么该手势识别失败。  在多击事件中（上述count参数大于1），需要每一次点击的手指数都等于设置的触发点击的手指数，否则该手势识别失败。  默认值：false  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| distanceThreshold23+ | number | 否 | 是 | 点击手势移动阈值。当设置的值小于等于0或不设置时，会被转化为默认值。  默认值：2^31-1  单位：vp  取值范围：(0, +∞)  **说明：**  当手指的移动距离超出开发者预设的移动阈值时，点击识别失败。如果初始化为默认阈值时，手指移动超过组件热区范围，点击识别失败。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## LongPressGestureHandler

长按手势处理器对象类型，用于识别组件上的长按交互，适用于需要按住后触发操作的场景，并支持配置触发手指数、长按时长、是否连续触发及移动阈值等识别条件。

### constructor

constructor(options?: LongPressGestureHandlerOptions)

长按手势处理器的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LongPressGestureHandlerOptions](ts-gesturehandler.md#longpressgesturehandleroptions) | 否 | 长按手势处理器配置参数。当需要自定义触发长按的最少手指数、是否连续触发、最短触发时间、手指数量校验或最大移动距离时传入；不传入时使用长按手势处理器默认配置，如触发手指数为1、repeat为false、触发长按的最短时间为500ms、最大移动距离为15px。 |

### onAction

onAction(event: Callback<GestureEvent>): LongPressGestureHandler

设置长按手势处理器识别成功回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 长按手势处理器识别成功回调，回调参数为GestureEvent对象，用于获取长按手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LongPressGestureHandler](ts-gesturehandler.md#longpressgesturehandler) | 返回当前长按手势处理器对象。 |

### onActionEnd

onActionEnd(event: Callback<GestureEvent>): LongPressGestureHandler

设置长按手势处理器结束回调。长按手势处理器识别成功后，最后一根手指抬起时触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 长按手势处理器结束回调，回调参数为GestureEvent对象，用于获取长按结束时的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LongPressGestureHandler](ts-gesturehandler.md#longpressgesturehandler) | 返回当前长按手势处理器对象。 |

### onActionCancel

onActionCancel(event: Callback<void>): LongPressGestureHandler

设置长按手势处理器取消回调。长按手势处理器识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<void> | 是 | 长按手势处理器取消回调，该回调无入参，不返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LongPressGestureHandler](ts-gesturehandler.md#longpressgesturehandler) | 返回当前长按手势处理器对象。 |

### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): LongPressGestureHandler

设置长按手势处理器取消回调。长按手势处理器识别成功后，接收到触摸取消事件时触发回调。与[onActionCancel](ts-gesturehandler.md#onactioncancel)接口相比，此接口返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 长按手势处理器取消回调。该回调会返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LongPressGestureHandler](ts-gesturehandler.md#longpressgesturehandler) | 返回当前长按手势处理器对象。 |

## LongPressGestureHandlerOptions

长按手势处理器配置参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fingers | number | 否 | 是 | 触发长按的最少手指数。开启isFingerCountLimited时，触摸屏幕的手指数量需等于fingers参数值，否则手势识别失败。  默认值：1  取值范围：[1, 10]  **说明：**  手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| repeat | boolean | 否 | 是 | 是否连续触发事件回调。true表示为连续触发事件回调，false表示不连续触发事件回调。  默认值：false  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| duration | number | 否 | 是 | 触发长按的最短时间，单位为毫秒（ms）。  默认值：500  **说明：**  取值范围：(0, +∞)，设置小于等于0时，按照默认值500处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isFingerCountLimited15+ | boolean | 否 | 是 | 是否检查触摸屏幕的手指数量。true表示检查触摸屏幕的手指数量，false表示不检查触摸屏幕的手指数量。若触摸屏幕的手指的数量不等于设置的触发长按的最少手指数（即上述fingers参数），手势识别将失败。  对于已成功识别的手势，后续触摸屏幕的手指数变化，将不触发repeat事件（若触摸屏幕的手指数恢复到设置的触发长按的最少手指数时，可以触发[onAction](ts-basic-gestures-longpressgesture.md#onaction)事件），但可以触发[onActionEnd](ts-basic-gestures-longpressgesture.md#onactionend)事件。  默认值：false  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| allowableMovement22+ | number | 否 | 是 | 长按手势识别器识别的手势的最大移动距离，单位为px。  默认值：15  取值范围：(0, +∞)，设置小于等于0时，按照默认值15处理。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## PanGestureHandler

滑动手势处理器对象类型，用于识别组件上的拖动或滑动交互，适用于需要跟随手指移动更新状态的场景，并支持配置触发手指数、滑动方向、最小拖动距离及不同输入源的触发距离。

### constructor

constructor(options?: PanGestureHandlerOptions)

滑动手势处理器的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PanGestureHandlerOptions](ts-gesturehandler.md#pangesturehandleroptions) | 否 | 滑动手势处理器配置参数。当需要自定义触发拖动的最少手指数、触发方向、最小拖动距离、不同输入源的最小拖动距离或手指数量校验时传入；不传入时使用滑动手势处理器默认配置，如触发手指数为1、方向为PanDirection.All，最小拖动距离按输入源使用默认值，默认不检查触摸屏幕的手指数量。 |

### onActionStart

onActionStart(event: Callback<GestureEvent>): PanGestureHandler

设置滑动手势处理器识别成功回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 滑动手势处理器识别成功回调，回调参数为GestureEvent对象，用于获取滑动开始时的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PanGestureHandler](ts-gesturehandler.md#pangesturehandler) | 返回当前滑动手势处理器对象。 |

### onActionUpdate

onActionUpdate(event: Callback<GestureEvent>): PanGestureHandler

设置滑动手势处理器更新回调。滑动手势处理器移动过程中触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 滑动手势处理器更新回调。  fingerList为多根手指时，每次触发该回调只更新一根手指的位置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PanGestureHandler](ts-gesturehandler.md#pangesturehandler) | 返回当前滑动手势处理器对象。 |

### onActionEnd

onActionEnd(event: Callback<GestureEvent>): PanGestureHandler

设置滑动手势处理器结束回调。滑动手势处理器识别成功后，手指抬起时触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 滑动手势处理器结束回调，回调参数为GestureEvent对象，用于获取滑动结束时的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PanGestureHandler](ts-gesturehandler.md#pangesturehandler) | 返回当前滑动手势处理器对象。 |

### onActionCancel

onActionCancel(event: Callback<void>): PanGestureHandler

设置滑动手势处理器取消回调。滑动手势处理器识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<void> | 是 | 滑动手势处理器取消回调，该回调无入参，不返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PanGestureHandler](ts-gesturehandler.md#pangesturehandler) | 返回当前滑动手势处理器对象。 |

### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): PanGestureHandler

设置滑动手势处理器取消回调。滑动手势处理器识别成功后，接收到触摸取消事件时触发回调。与[onActionCancel](ts-gesturehandler.md#onactioncancel-1)接口相比，此接口返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 滑动手势处理器取消回调。返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PanGestureHandler](ts-gesturehandler.md#pangesturehandler) | 返回当前滑动手势处理器对象。 |

## PanGestureHandlerOptions

滑动手势处理器配置参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fingers | number | 否 | 是 | 用于指定触发拖动的最少手指数，最小为1指， 最大取值为10指。  默认值：1  取值范围：[1, 10]  **说明：**  当设置的值小于1或不设置时，会被转化为默认值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction | [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明) | 否 | 是 | 用于指定触发拖动的手势方向，此枚举值支持逻辑与（&）和逻辑或（|）运算。  默认值：PanDirection.All  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| distance | number | 否 | 是 | 用于指定触发滑动手势事件的最小拖动距离，单位为vp。  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs组件](ts-container-tabs.md)滑动与该滑动手势事件同时存在时，可将distance值设为1，使拖动更灵敏，避免造成事件错乱。  取值范围：[0, +∞)，当设定的值小于0时，按默认值处理。  从API version 19开始，手写笔默认值为8，单位为vp。  使用[gestureModifier](ts-universal-attributes-gesture-modifier.md#gesturemodifier)配置该字段时，单位为px。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| distanceMap19+ | Map<[SourceTool](ts-gesture-settings.md#sourcetool枚举说明9), number> | 否 | 是 | 用于指定不同输入源触发滑动手势事件的最小拖动距离，单位为vp。  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs组件](ts-container-tabs.md)滑动与该滑动手势事件同时存在时，可将对应输入源的distanceMap值设为1，使拖动更灵敏，避免造成事件错乱。  取值范围：[0, +∞)，当设定的值小于0时，按默认值处理。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## SwipeGestureHandler

快滑手势处理器对象类型，用于识别组件上的快速滑动交互，适用于需要根据滑动方向或速度触发操作的场景，并支持配置触发手指数、滑动方向和最小速度。

### constructor

constructor(options?: SwipeGestureHandlerOptions)

快滑手势处理器的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SwipeGestureHandlerOptions](ts-gesturehandler.md#swipegesturehandleroptions) | 否 | 快滑手势处理器配置参数。当需要自定义触发快滑的最少手指数、滑动方向、最小识别速度或手指数量校验时传入；不传入时使用快滑手势处理器默认配置，如触发手指数为1、方向为SwipeDirection.All、最小速度为100vp/s、默认不检查触摸屏幕的手指数量。 |

### onAction

onAction(event: Callback<GestureEvent>): SwipeGestureHandler

设置快滑手势处理器识别成功回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 快滑手势处理器识别成功回调，回调参数为GestureEvent对象，用于获取快滑手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SwipeGestureHandler](ts-gesturehandler.md#swipegesturehandler) | 返回当前快滑手势处理器对象。 |

## SwipeGestureHandlerOptions

快滑手势处理器配置参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fingers | number | 否 | 是 | 触发快滑的最少手指数。当单指快滑即可触发操作时设置为1；当需要降低误触、要求多指协同触发快滑时设置为2到10。不传入时默认值为1。  默认值：1  取值范围：[1, 10] |
| direction | [SwipeDirection](ts-basic-gestures-swipegesture.md#swipedirection枚举说明) | 否 | 是 | 触发快滑手势的滑动方向。SwipeDirection.All适用于任意方向快滑均可触发的场景；SwipeDirection.Horizontal适用于只响应水平快滑的场景，如左右翻页或轮播切换；SwipeDirection.Vertical适用于只响应竖直快滑的场景，如上下切换内容；SwipeDirection.None适用于暂不触发快滑手势的场景。不传入时默认值为SwipeDirection.All。  默认值：SwipeDirection.All |
| speed | number | 否 | 是 | 识别快滑的最小速度。需要更灵敏地识别快滑时可设置较小的正数阈值；需要减少普通滑动被误识别为快滑时可设置较大的阈值。推荐先使用默认值，再根据交互灵敏度和误触情况调整。不传入时默认值为100vp/s。  默认值：100vp/s  取值范围：(0, +∞)，单位：vp/s。  **说明：**  当滑动速度的值小于等于0时，会被转化为默认值。 |
| isFingerCountLimited15+ | boolean | 否 | 是 | 是否检查触摸屏幕的手指数量。true表示检查触摸屏幕的手指数量，false表示不检查触摸屏幕的手指数量。如果触摸手指的数量不等于设置的触发快滑的最少手指数（即上述fingers参数），手势识别将失败。  默认值：false  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## PinchGestureHandler

捏合手势处理器对象类型，用于识别组件上的多指捏合交互，适用于缩放类操作场景，并支持配置触发手指数、最小识别距离及手指数限制等识别条件。

### constructor

constructor(options?: PinchGestureHandlerOptions)

捏合手势处理器的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PinchGestureHandlerOptions](ts-gesturehandler.md#pinchgesturehandleroptions) | 否 | 捏合手势处理器配置参数。当需要自定义触发捏合的最少手指数、最小识别距离或手指数量校验时传入；不传入时使用捏合手势处理器默认配置，如触发手指数为2、最小识别距离为5vp、默认不检查触摸屏幕的手指数量。 |

### onActionStart

onActionStart(event: Callback<GestureEvent>): PinchGestureHandler

设置捏合手势处理器识别成功回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 捏合手势处理器识别成功回调，回调参数为GestureEvent对象，用于获取捏合开始时的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PinchGestureHandler](ts-gesturehandler.md#pinchgesturehandler) | 返回当前捏合手势处理器对象。 |

### onActionUpdate

onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler

设置捏合手势处理器更新回调。捏合手势处理器移动过程中触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 捏合手势处理器更新回调，回调参数为GestureEvent对象，用于获取捏合更新过程中的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PinchGestureHandler](ts-gesturehandler.md#pinchgesturehandler) | 返回当前捏合手势处理器对象。 |

### onActionEnd

onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler

设置捏合手势处理器结束回调。捏合手势处理器识别成功后，手指抬起时触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 捏合手势处理器结束回调，回调参数为GestureEvent对象，用于获取捏合结束时的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PinchGestureHandler](ts-gesturehandler.md#pinchgesturehandler) | 返回当前捏合手势处理器对象。 |

### onActionCancel

onActionCancel(event: Callback<void>): PinchGestureHandler

设置捏合手势处理器取消回调。捏合手势处理器识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<void> | 是 | 捏合手势处理器取消回调。不返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PinchGestureHandler](ts-gesturehandler.md#pinchgesturehandler) | 返回当前捏合手势处理器对象。 |

### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler

设置捏合手势处理器取消回调。捏合手势处理器识别成功后，接收到触摸取消事件时触发回调。与[onActionCancel](ts-gesturehandler.md#onactioncancel-2)接口相比，此接口返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 捏合手势处理器取消回调。返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PinchGestureHandler](ts-gesturehandler.md#pinchgesturehandler) | 返回当前捏合手势处理器对象。 |

## PinchGestureHandlerOptions

捏合手势处理器配置参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fingers | number | 否 | 是 | 触发捏合的最少手指数，最小为2指，最大为5指。  默认值：2  取值范围：[2, 5]，包含2和5。设置值小于2或大于5时，按默认值2处理。  未开启isFingerCountLimited时，触发手势手指可以多于fingers数目，但只有先落下的与fingers相同数目的手指参与手势计算；开启isFingerCountLimited时，触摸手指数量需等于fingers数目，否则手势不会被识别。 |
| distance | number | 否 | 是 | 最小识别距离，单位为vp。需要更灵敏地识别捏合手势时可设置较小的正数阈值；需要降低轻微移动或误触触发捏合时可设置较大的阈值。推荐先使用默认值，再根据组件尺寸和交互灵敏度调整。不传入时默认值为5。  默认值：5  取值范围：(0, +∞)。  **说明：**  当识别距离的值小于等于0时，会被转化为默认值。 |
| isFingerCountLimited15+ | boolean | 否 | 是 | 是否检查触摸屏幕的手指数量。true表示检查触摸屏幕的手指数量，false表示不检查触摸屏幕的手指数量。若触摸屏幕的手指数量不等于设置的触发捏合的最少手指数（即上述fingers参数），手势将不会被识别。只有当触摸屏幕的手指数等于设置的触发捏合手势的最小手指数，并且滑动距离满足阈值要求时，手势才能被成功识别（只有先落下的与fingers相同数目的手指参与手势计算，若抬起其中的一个，手势识别失败）。对于已经成功识别的手势，后续改变触摸屏幕的手指数量，将不会触发[onActionUpdate](ts-basic-gestures-pinchgesture.md#onactionupdate)事件，但可以触发[onActionEnd](ts-basic-gestures-pinchgesture.md#onactionend)事件。  默认值：false  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## RotationGestureHandler

旋转手势处理器对象类型，用于识别组件上的多指旋转交互，适用于需要旋转对象或调整角度的场景，并支持配置触发手指数、最小改变角度及手指数限制等识别条件。

### constructor

constructor(options?: RotationGestureHandlerOptions)

旋转手势处理器的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RotationGestureHandlerOptions](ts-gesturehandler.md#rotationgesturehandleroptions) | 否 | 旋转手势处理器配置参数。当需要自定义触发旋转的最少手指数、触发旋转手势的最小改变度数或手指数量校验时传入；不传入时使用旋转手势处理器默认配置，如触发手指数为2、最小改变度数为1deg、默认不检查触摸屏幕的手指数量。 |

### onActionStart

onActionStart(event: Callback<GestureEvent>): RotationGestureHandler

设置旋转手势处理器识别成功回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 旋转手势处理器识别成功回调，回调参数为GestureEvent对象，用于获取旋转开始时的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RotationGestureHandler](ts-gesturehandler.md#rotationgesturehandler) | 返回当前旋转手势处理器对象。 |

### onActionUpdate

onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler

设置旋转手势处理器更新回调。旋转手势处理器移动过程中触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 旋转手势处理器更新回调，回调参数为GestureEvent对象，用于获取旋转更新过程中的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RotationGestureHandler](ts-gesturehandler.md#rotationgesturehandler) | 返回当前旋转手势处理器对象。 |

### onActionEnd

onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler

设置旋转手势处理器结束回调。旋转手势处理器识别成功后，手指抬起时触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 旋转手势处理器结束回调，回调参数为GestureEvent对象，用于获取旋转结束时的手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RotationGestureHandler](ts-gesturehandler.md#rotationgesturehandler) | 返回当前旋转手势处理器对象。 |

### onActionCancel

onActionCancel(event: Callback<void>): RotationGestureHandler

设置旋转手势处理器取消回调。旋转手势处理器识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<void> | 是 | 旋转手势处理器取消回调。不返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RotationGestureHandler](ts-gesturehandler.md#rotationgesturehandler) | 返回当前旋转手势处理器对象。 |

### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler

设置旋转手势处理器取消回调。旋转手势处理器识别成功后，接收到触摸取消事件时触发回调。与[onActionCancel](ts-gesturehandler.md#onactioncancel-3)相比，此接口返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 旋转手势处理器取消回调。返回手势事件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RotationGestureHandler](ts-gesturehandler.md#rotationgesturehandler) | 返回当前旋转手势处理器对象。 |

## RotationGestureHandlerOptions

旋转手势处理器配置参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fingers | number | 否 | 是 | 触发旋转的最少手指数，最小为2指，最大为5指。  默认值：2  取值范围：[2, 5]，包含2和5。设置值小于2或大于5时，按默认值2处理。  未开启isFingerCountLimited时，触发手势时手指数量可以多于fingers参数值，但仅最先落下的两指参与手势计算；开启isFingerCountLimited时，触摸手指数量需等于fingers参数值，否则手势不会被识别。 |
| angle | number | 否 | 是 | 触发旋转手势的最小改变度数，单位为deg。需要更灵敏地识别轻微旋转时可设置较小的正数角度；需要减少误触或只响应明显旋转时可设置较大的角度。推荐先使用默认值，再根据旋转交互精度要求调整。不传入时默认值为1。  默认值：1  取值范围：(0, 360]  **说明：**  当改变度数的值小于等于0或大于360时，会被转化为默认值。 |
| isFingerCountLimited15+ | boolean | 否 | 是 | 是否检查触摸屏幕的手指数量。true表示检查触摸屏幕的手指数量，false表示不检查触摸屏幕的手指数量。若触摸屏幕的手指数量不等于设置的触发旋转的最少手指数（即上述fingers参数），手势将不会被识别。只有当触摸屏幕的手指数等于设置的触发旋转的最少手指数，并且旋转角度变化达到angle阈值时，手势才能被成功识别；若旋转角度变化未达到angle阈值，手势不会被成功识别（只有先落下的两根手指参与手势计算，若抬起其中的一个，手势识别失败）。  对于已成功识别的手势，后续改变触摸屏幕的手指数量，不会触发[onActionUpdate](ts-basic-gestures-rotationgesture.md#onactionupdate)事件，但可以触发[onActionEnd](ts-basic-gestures-rotationgesture.md#onactionend)事件。  默认值：false  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## GestureGroupHandler

手势组处理器对象类型，用于将多个手势组合后统一绑定到组件，适用于需要协调单击、双击、长按等多种手势识别顺序或并发关系的场景。

### constructor

constructor(options?: GestureGroupGestureHandlerOptions)

手势组处理器的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GestureGroupGestureHandlerOptions](ts-gesturehandler.md#gesturegroupgesturehandleroptions) | 否 | 手势组处理器配置参数。当需要设置组合手势识别模式和手势集合时传入；不传入时使用手势组处理器默认配置，组合手势识别模式默认为GestureMode.Sequence，且不会配置手势集合。 |

### onCancel

onCancel(event: Callback<void>): GestureGroupHandler

设置手势组处理器取消回调。顺序组合手势（[GestureMode](ts-combined-gestures.md#gesturemode枚举说明).Sequence）取消后触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<void> | 是 | 手势组处理器取消回调，该回调无入参，用于在顺序组合手势取消后接收通知。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GestureGroupHandler](ts-gesturehandler.md#gesturegrouphandler) | 返回当前手势组处理器对象。 |

## GestureGroupGestureHandlerOptions

手势组处理器配置参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | [GestureMode](ts-combined-gestures.md#gesturemode枚举说明) | 否 | 否 | 设置组合手势识别模式，适用于需要按顺序识别多个手势、并行识别多个手势或在多个手势间互斥识别的场景。  默认值：GestureMode.Sequence |
| gestures | [GestureHandler](ts-gesturehandler.md#gesturehandlert)<[TapGestureHandler](ts-gesturehandler.md#tapgesturehandler) | [LongPressGestureHandler](ts-gesturehandler.md#longpressgesturehandler) | [PanGestureHandler](ts-gesturehandler.md#pangesturehandler) | [SwipeGestureHandler](ts-gesturehandler.md#swipegesturehandler) | [PinchGestureHandler](ts-gesturehandler.md#pinchgesturehandler) | [RotationGestureHandler](ts-gesturehandler.md#rotationgesturehandler) | [GestureGroupHandler](ts-gesturehandler.md#gesturegrouphandler)>[] | 否 | 否 | 设置手势组中需要包含的手势集合。  **说明：**  当需要为一个组件同时添加单击和双击手势时，可在[GestureGroup](ts-combined-gestures.md)中添加两个[TapGesture](ts-basic-gestures-tapgesture.md)，需要双击手势在前，单击手势在后，否则同时添加单击和双击手势的配置不生效。 |

## GesturePriority枚举说明

绑定手势的优先级，适用于多个手势同时绑定时需要控制手势响应先后或处理手势冲突的场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通优先级手势。 |
| PRIORITY | 1 | 高优先级手势。 |
