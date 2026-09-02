---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h
title: ui_input_event.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > ui_input_event.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:318e042e3dbac2c3430a1b4820efdbefb6e3667cd1683cc3c8fa13fbd345ca63
---

## 概述

提供ArkUI在Native侧的输入事件定义，支持触摸、鼠标、轴和按键事件，以及事件属性获取、事件冒泡控制和事件克隆处理，用于Native组件识别和处理用户输入。

**引用文件：** <arkui/ui\_input\_event.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_EventModule](capi-arkui-eventmodule.md)

**相关示例：** [NdkInputEvent](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkInputEvent)、[CoastingAxisEventNDK](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/CoastingAxisEventNDK)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md) | ArkUI\_UIInputEvent | ArkUI\_UIInputEvent用于表示ArkUI中的UI输入事件，供ArkUI\_EventModule模块中的事件接口传递和处理输入事件信息，适用于需要识别、分发或响应用户输入事件的场景。 |
| [ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md) | ArkUI\_CoastingAxisEvent | 定义惯性滚动轴事件。当用户在触控板上用双指滑动时，系统会根据手指抬起时的速度，按照系统预设的衰减曲线构造滑动事件。可以监听此类事件，以便在常规轴事件之后立即处理惯性滚动效果。 仅当用户在触控板上双指抛滑，且指针位置下存在通过[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册了[NODE\_ON\_COASTING\_AXIS\_EVENT](capi-native-node-h.md#arkui_nodeeventtype)事件的组件时，才能接收到此事件。不再需要监听此事件时，应通过[unregisterNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodeevent)注销事件监听，避免回调持续触发。 |
| [ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md) | ArkUI\_TouchTestInfo | 定义触摸测试信息，用于在命中测试过程中获取触摸测试策略、参与命中测试的子组件ID及触摸测试信息项列表，适用于需要在子组件触摸事件中获取命中测试详细信息以自定义命中测试逻辑、优化触摸事件分发与响应的场景。 当用户通过[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册了[NODE\_ON\_CHILD\_TOUCH\_TEST](capi-native-node-h.md#arkui_nodeeventtype)事件时，才能接收到此事件。触摸测试信息包含触摸测试策略、命中测试过程中需要参与命中测试的子组件ID和触摸测试信息项的列表。 |
| [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md) | ArkUI\_TouchTestInfoItem | 定义触摸测试信息项。触摸测试信息项包含触摸测试中子组件的信息，适用于触摸测试过程中获取和识别子组件相关信息的场景，可以通过[OH\_ArkUI\_TouchTestInfoItem\_GetX](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getx)、[OH\_ArkUI\_TouchTestInfoItem\_GetY](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_gety)等接口获取子组件信息，帮助开发者处理触摸测试结果。 |
| [ArkUI\_TouchTestInfoItem\*](capi-arkui-nativemodule-arkui-touchtestinfoitemhandle.md) | ArkUI\_TouchTestInfoItemHandle | 定义触摸测试信息项句柄，用于表示触摸测试流程中的触摸测试信息项；触摸测试接口请参见[ui\_input\_event.h](capi-ui-input-event-h.md)。 |
| [ArkUI\_TouchTestInfoItemHandle\*](capi-arkui-nativemodule-arkui-touchtestinfoitemhandlearray.md) | ArkUI\_TouchTestInfoItemArray | 定义触摸测试信息项句柄数组，用于表示多个触摸测试信息项句柄。在触摸事件分发与测试过程中，可通过此数组类型统一管理和访问多个触摸测试结果，适用于需要同时处理多个触点测试信息的场景。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_UIInputEvent\_Type](capi-ui-input-event-h.md#arkui_uiinputevent_type) | ArkUI\_UIInputEvent\_Type | UI输入事件类型定义。 |
| [anonymous1](capi-ui-input-event-h.md#anonymous1) | - | 定义输入事件的行为类型。 |
| [anonymous2](capi-ui-input-event-h.md#anonymous2) | - | 产生输入事件的工具类型定义。 |
| [anonymous3](capi-ui-input-event-h.md#anonymous3) | - | 产生输入事件的来源类型定义。 |
| [HitTestMode](capi-ui-input-event-h.md#hittestmode) | HitTestMode | 定义触摸测试类型的枚举值。 |
| [anonymous4](capi-ui-input-event-h.md#anonymous4) | - | 定义鼠标事件的行为类型。 |
| [anonymous5](capi-ui-input-event-h.md#anonymous5) | - | 定义鼠标事件的按键类型。 |
| [ArkUI\_ModifierKeyName](capi-ui-input-event-h.md#arkui_modifierkeyname) | ArkUI\_ModifierKeyName | 定义修饰键。 |
| [anonymous6](capi-ui-input-event-h.md#anonymous6) | - | 定义焦点轴事件的轴类型。 |
| [ArkUI\_InteractionHand](capi-ui-input-event-h.md#arkui_interactionhand) | ArkUI\_InteractionHand | 定义触摸事件是左手还是右手。 |
| [anonymous7](capi-ui-input-event-h.md#anonymous7) | - | 定义轴事件的操作类型。 |
| [anonymous8](capi-ui-input-event-h.md#anonymous8) | - | 定义轴事件的轴类型。 |
| [ArkUI\_CoastingAxisEventPhase](capi-ui-input-event-h.md#arkui_coastingaxiseventphase) | ArkUI\_CoastingAxisEventPhase | 定义惯性滚动轴事件的阶段。 |
| [ArkUI\_CompetitionStrategy](capi-ui-input-event-h.md#arkui_competitionstrategy) | ArkUI\_CompetitionStrategy | 事件的注入方和被注入方间手势识别结果是否为竞争场景的策略。该策略决定了事件的注入方如何与被注入方的手势处理逻辑交互，非竞争场景会同时触发手势，竞争场景只触发其中一个。 |
| [ArkUI\_TouchTestStrategy](capi-ui-input-event-h.md#arkui_touchteststrategy) | ArkUI\_TouchTestStrategy | 定义触摸测试策略。 |
| [ArkUI\_CrownEvent\_Action](capi-ui-input-event-h.md#arkui_crownevent_action) | ArkUI\_CrownEvent\_Action | 定义表冠事件的阶段。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetType(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_gettype) | 获取UI输入事件的类型。在访问一个ArkUI\_UIInputEvent指针对象之前，推荐使用该方法判断该输入事件的类型，该接口会返回[ArkUI\_UIInputEvent\_Type](capi-ui-input-event-h.md#arkui_uiinputevent_type)枚举中的一种。比如，当事件是一个触控类型时，由于触控类型是指向性事件，那么使用OH\_ArkUI\_UIInputEvent\_GetXXX及OH\_ArkUI\_PointerEvent\_GetXXX系列接口，均可以正常访问；而如果使用OH\_ArkUI\_KeyEvent\_GetXXX相关接口去访问它，则会有无法预期的结果。对于还未支持的事件类型，接口返回默认值0。 |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetAction(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getaction) | 获取输入事件的action类型。action类型为基础事件在不同阶段的类型定义，通常代表事件的特点，并表征事件的开始与结束，如touch down、touch up。触控事件的action类型为UI\_TOUCH\_EVENT\_ACTION\_XXX，鼠标事件的action类型为UI\_MOUSE\_EVENT\_ACTION\_XXX。 |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetSourceType(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getsourcetype) | 获取UI输入事件的触发源类型。输入源为产生输入事件的真实物理设备，如触摸屏、鼠标等，由[UI\_INPUT\_EVENT\_SOURCE\_TYPE](capi-ui-input-event-h.md#anonymous3)定义，而输入工具为操作输入源设备来产生事件的工具，如手指、触控笔。在某些情况下两者可能容易发生混淆，比如当用户在操作鼠标时，鼠标既是输入源，也是输入工具。对于按键事件，并不支持获取输入源类型，返回unknown。 |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetToolType(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_gettooltype) | 获取UI输入事件的工具类型。输入工具是操作输入源设备以产生事件的工具，如手指、触控笔。它们自身不直接产生事件，但可以驱动输入源设备不断产生事件。返回的类型由UI\_INPUT\_EVENT\_TOOL\_TYPE\_XXX枚举值定义。 |
| [int64\_t OH\_ArkUI\_UIInputEvent\_GetEventTime(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtime) | 获取UI输入事件发生的时间。单位为ns。 |
| [uint32\_t OH\_ArkUI\_PointerEvent\_GetPointerCount(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpointercount) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点数量。指向性事件一般是附带有事件发生位置信息的事件，如触摸事件，用户操作时，可以感知事件在什么位置发生。而非指向性事件，如按键事件，一般没有位置信息，没有触点的说法，该接口对按键事件调用时永远返回0。对于触摸事件，该接口多用于处理多指触控，判断用户有几根手指在操作当前控件。而对于鼠标和轴事件，可认为触点只有1个，该接口永远返回1。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpointerid) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点标识。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetChangedPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t\* pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getchangedpointerid) | 获取触发当前事件的手指ID。 |
| [float OH\_ArkUI\_PointerEvent\_GetCurrentLocalX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getcurrentlocalx) | 从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取相对于当前组件左上角的X坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetCurrentLocalXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getcurrentlocalxbyindex) | 从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取特定接触点相对于当前组件左上角的X坐标。所有类型事件，pointerIndex为uint32\_t，不存在小于0的取值。对于鼠标和轴事件，pointerIndex必须为0。对于触摸事件，pointerIndex必须小于当前事件的触点数量，根据给定的索引获取特定接触点相对于当前组件左上角的X坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetCurrentLocalY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getcurrentlocaly) | 从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取相对于当前组件左上角的Y坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetCurrentLocalYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getcurrentlocalybyindex) | 从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取特定接触点相对于当前组件左上角的Y坐标。所有类型事件，若传入的索引值小于0时为非法值。对于鼠标和轴事件，当索引值非0时为非法值。对于触摸事件，根据给定的索引获取特定接触点相对于当前组件左上角的Y坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getx) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的X坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getxbyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gety) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的Y坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getybyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetWindowX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getwindowx) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的X坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetWindowXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getwindowxbyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetWindowY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getwindowy) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的Y坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetWindowYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getwindowybyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayx) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的X坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayxbyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayy) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的Y坐标。 |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getdisplayybyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getglobaldisplayx) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)事件中获取位置信息。 |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getglobaldisplayxbyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从指向性输入事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getglobaldisplayy) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)事件中获取位置信息。 |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getglobaldisplayybyindex) | 从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从指向性输入事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。 |
| [float OH\_ArkUI\_PointerEvent\_GetPressure(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpressure) | 从指向性输入事件（如触摸事件）中获取触屏压力。 |
| [float OH\_ArkUI\_PointerEvent\_GetTiltX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gettiltx) | 从指向性输入事件（如触摸事件）中获取相对YZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向右倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetTiltY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gettilty) | 从指向性输入事件（如触摸事件）中获取相对XZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向下倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetRollAngle(const ArkUI\_UIInputEvent\* event, double\* rollAngle)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getrollangle) | 获取触控笔绕Z轴旋转的角度。 |
| [float OH\_ArkUI\_PointerEvent\_GetTouchAreaWidth(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gettouchareawidth) | 从指向性输入事件（如触摸事件）中获取触屏区域的宽度。仅适用于手指操作产生的触控事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetTouchAreaHeight(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gettouchareaheight) | 从指向性输入事件（如触摸事件）中获取触屏区域的高度。仅适用于手指操作产生的触控事件。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetInteractionHand(const ArkUI\_UIInputEvent \*event, ArkUI\_InteractionHand \*hand)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getinteractionhand) | 获取当前触摸事件是左手点击触发还是右手点击触发。仅在部分触控产品上有效。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetInteractionHandByIndex(const ArkUI\_UIInputEvent \*event, int32\_t pointerIndex, ArkUI\_InteractionHand \*hand)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getinteractionhandbyindex) | 获取当前触摸事件是左手点击触发还是右手点击触发。仅在部分触控产品上有效。 |
| [uint32\_t OH\_ArkUI\_PointerEvent\_GetHistorySize(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize) | [从指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)中获取历史事件数量。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。历史事件为此次事件与上一次事件之间发生的原始事件，仅在指向性输入事件的移动阶段（即触摸移动或鼠标移动）中适用，在其他状态中调用返回默认值0。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [int64\_t OH\_ArkUI\_PointerEvent\_GetHistoryEventTime(const ArkUI\_UIInputEvent\* event, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistoryeventtime) | 从指向性输入事件中获取历史事件发生的时间。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [uint32\_t OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(const ArkUI\_UIInputEvent\* event, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorypointercount) | 从指向性输入事件中获取特定历史事件中多点触控的接触点数量。本接口支持的指向性输入事件仅包含触摸事件。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetHistoryPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorypointerid) | 从指向性输入事件的历史点中获取多点触控的接触点标识。本接口支持的指向性输入事件仅包含触摸事件。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistoryx) | 从指向性输入事件中获取特定历史事件中特定接触点相对于当前组件左上角的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistoryy) | 从指向性输入事件中获取特定历史事件中特定接触点相对于当前组件左上角的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryWindowX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorywindowx) | 从指向性输入事件中获取特定历史事件中特定接触点相对于当前应用窗口左上角的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryWindowY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorywindowy) | 从指向性输入事件中获取特定历史事件中特定接触点相对于当前应用窗口左上角的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryDisplayX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorydisplayx) | 从指向性输入事件中获取特定历史事件中特定接触点相对于当前屏幕左上角的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryDisplayY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorydisplayy) | 从指向性输入事件中获取特定历史事件中特定接触点相对于当前屏幕左上角的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistoryglobaldisplayx) | 从给定指针索引和历史记录索引的指向性输入事件中获取历史事件中相对于全局显示的特定触摸点的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。只能从指针事件中获取位置信息，对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 20开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistoryglobaldisplayy) | 从给定指针索引和历史记录索引的指向性输入事件中获取历史事件中相对于全局显示的特定触摸点的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。只能从指针事件中获取位置信息，对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 20开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryPressure(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorypressure) | 从指向性输入事件（如触摸事件）中获取特定历史事件中的触屏压力。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTiltX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorytiltx) | 从指向性输入事件（如触摸事件）中获取特定历史事件中的相对YZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向右倾斜。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTiltY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorytilty) | 从指向性输入事件（如触摸事件）中获取特定历史事件中的相对XZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向下倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaWidth(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorytouchareawidth) | 从指向性输入事件（如触摸事件）中获取特定历史事件中的触屏区域的宽度。 |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaHeight(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorytouchareaheight) | 从指向性输入事件（如触摸事件）中获取特定历史事件中的触屏区域的高度。 |
| [double OH\_ArkUI\_AxisEvent\_GetVerticalAxisValue(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_axisevent_getverticalaxisvalue) | 获取当前轴事件的垂直滚动轴的值。该值通常由鼠标滚轮或用户在触控板上双指竖向滑动产生。 当通过鼠标滚轮触发时： 1. 上报的数值单位为角度，表示单次滚动角度增量，非滚动总量。 2. 上报的数值已与用户配置的放大系数[OH\_ArkUI\_AxisEvent\_GetScrollStep](capi-ui-input-event-h.md#oh_arkui_axisevent_getscrollstep)叠加运算。 3. 数值的正负代表方向，向前滚动鼠标滚轮时上报数值为负数，向后滚动鼠标滚轮时上报数值为正数。 当通过触控板双指竖向滑动触发时： 1. 上报的数值单位为px，表示单次滚动增量，非滚动总量。 2. 上报的数值不受用户配置的放大系数[OH\_ArkUI\_AxisEvent\_GetScrollStep](capi-ui-input-event-h.md#oh_arkui_axisevent_getscrollstep)影响。 3. 数值的正负代表方向，双指从上往下滑动时上报数值为负数，双指从下往上滑动时上报数值为正数。 4. 方向会受系统设置中“自然滚动”配置的影响。 通常情况下，垂直滚动轴事件只能驱动竖向的滑动手势响应。但当鼠标指针下命中的可滑动手势里可响应方向一致时，垂直滚动轴事件可以驱动这些滑动手势得到响应，即使这些手势所定义的方向是横向的。 |
| [double OH\_ArkUI\_AxisEvent\_GetHorizontalAxisValue(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_axisevent_gethorizontalaxisvalue) | 获取当前轴事件的水平滚动轴的值，该值通过在触控板上双指横向滑动产生。 1. 上报的数值单位为px，表示单次滚动增量，非滚动总量。 2. 上报的数值不受用户配置的放大系数[OH\_ArkUI\_AxisEvent\_GetScrollStep](capi-ui-input-event-h.md#oh_arkui_axisevent_getscrollstep)影响。 3. 数值的正负代表方向，双指从左往右滑动时上报数值为负数，双指从右往左滑动时上报数值为正数。 4. 方向会受系统设置中“自然滚动”配置的影响。 |
| [double OH\_ArkUI\_AxisEvent\_GetPinchAxisScaleValue(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_axisevent_getpinchaxisscalevalue) | 获取当前轴事件的捏合轴缩放的值。通过触控板双指缩放/捏合操作产生。上报的scale数值，为相对于初始状态时的当前scale值。初始状态为系统识别到用户通过触控板发生了捏合操作时的两指位置状态，此时的scale数值为1.0。在手指抬起前的本次捏合操作过程中，所上报的scale数值均将初始状态作为参考系，从初始状态往中心捏合，则上报的scale会从1.0逐步往0.0缩小；当从初始状态往外扩大双指距离时，会从1.0逐步变大。 |
| [int32\_t OH\_ArkUI\_AxisEvent\_GetAxisAction(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_axisevent_getaxisaction) | 获取当前轴事件的操作类型。 |
| [int32\_t OH\_ArkUI\_AxisEvent\_HasAxis(const ArkUI\_UIInputEvent\* event, int32\_t axis)](capi-ui-input-event-h.md#oh_arkui_axisevent_hasaxis) | 检测此轴事件是否包含指定的轴类型。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetInterceptHitTestMode(const ArkUI\_UIInputEvent\* event, HitTestMode mode)](capi-ui-input-event-h.md#oh_arkui_pointerevent_setintercepthittestmode) | 配置触摸测试模式。仅适用于接收基础事件的场景，如使用NODE\_ON\_TOUCH接收触摸事件场景。对于通过[OH\_ArkUI\_GestureEvent\_GetRawInputEvent](capi-native-gesture-h.md#oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI\_UIInputEvent对象，无法使用该接口。 |
| [int32\_t OH\_ArkUI\_MouseEvent\_GetMouseButton(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_mouseevent_getmousebutton) | 获取鼠标事件的按键类型的值。 |
| [int32\_t OH\_ArkUI\_MouseEvent\_GetMouseAction(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_mouseevent_getmouseaction) | 获取鼠标事件的鼠标动作类型的值。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetStopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)](capi-ui-input-event-h.md#oh_arkui_pointerevent_setstoppropagation) | 设置是否阻止事件冒泡。仅适用于接收基础事件的场景，如使用NODE\_ON\_TOUCH接收触摸事件场景，不适用于轴事件。对于通过[OH\_ArkUI\_GestureEvent\_GetRawInputEvent](capi-native-gesture-h.md#oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI\_UIInputEvent对象，无法使用该接口。 |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetDeviceId(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getdeviceid) | 获取当前UI输入事件的设备ID。 |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetPressedKeys(const ArkUI\_UIInputEvent\* event, int32\_t\* pressedKeyCodes, int32\_t\* length)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getpressedkeys) | 获取所有按下的按键，当前只支持按键事件。 |
| [double OH\_ArkUI\_FocusAxisEvent\_GetAxisValue(const ArkUI\_UIInputEvent\* event, int32\_t axis)](capi-ui-input-event-h.md#oh_arkui_focusaxisevent_getaxisvalue) | 获取焦点轴事件的轴值。 |
| [int32\_t OH\_ArkUI\_FocusAxisEvent\_SetStopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)](capi-ui-input-event-h.md#oh_arkui_focusaxisevent_setstoppropagation) | 设置是否阻止焦点轴事件冒泡。 |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetModifierKeyStates(const ArkUI\_UIInputEvent\* event, uint64\_t\* keys)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getmodifierkeystates) | 获取UI输入事件的修饰键状态。该接口会通过keys传出当前事件发生时所有修饰键的状态，应用可将keys与[ArkUI\_ModifierKeyName](capi-ui-input-event-h.md#arkui_modifierkeyname)中定义的修饰键类型进行位运算，以获取处于按下状态的修饰键。 |
| [int32\_t OH\_ArkUI\_AxisEvent\_SetPropagation(const ArkUI\_UIInputEvent\* event, bool propagation)](capi-ui-input-event-h.md#oh_arkui_axisevent_setpropagation) | 设置是否启用轴事件冒泡。默认不会进行冒泡传递，仅发送给第一个可响应轴事件的控件。可在接收到轴事件时，主动启用冒泡传递，以便当前事件可以继续传递给响应链上的下一个可响应轴事件的祖先组件处理。不支持对从手势事件中获取到的轴事件进行设置。 |
| [int32\_t OH\_ArkUI\_AxisEvent\_GetScrollStep(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_axisevent_getscrollstep) | 获取滚动轴事件的滚动步长系数，适用于鼠标滚轮产生的轴事件。该值表示用户配置的滚动放大系数。 |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetWidth(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtargetwidth) | 获取事件命中的组件的宽度。 |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetHeight(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtargetheight) | 获取事件命中的组件的高度。 |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtargetpositionx) | 获取事件命中的组件的X坐标。 |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtargetpositiony) | 获取事件命中的组件的Y坐标。 |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtargetglobalpositionx) | 获取事件命中的组件的全局X坐标。 |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtargetglobalpositiony) | 获取事件命中的组件的全局Y坐标。 |
| [int64\_t OH\_ArkUI\_PointerEvent\_GetPressedTimeByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpressedtimebyindex) | 获取指定触点的按下时间。仅对触摸事件有效。 |
| [float OH\_ArkUI\_MouseEvent\_GetRawDeltaX(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_mouseevent_getrawdeltax) | 获取鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。 |
| [float OH\_ArkUI\_MouseEvent\_GetRawDeltaY(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_mouseevent_getrawdeltay) | 获取鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。 |
| [int32\_t OH\_ArkUI\_MouseEvent\_GetPressedButtons(const ArkUI\_UIInputEvent\* event, int32\_t\* pressedButtons, int32\_t\* length)](capi-ui-input-event-h.md#oh_arkui_mouseevent_getpressedbuttons) | 从鼠标事件中获取按下的按键。 |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetTargetDisplayId(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_gettargetdisplayid) | 获取发生UI输入事件的屏幕ID。 |
| [bool OH\_ArkUI\_HoverEvent\_IsHovered(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_hoverevent_ishovered) | 获取鼠标是否悬浮在当前组件上 |
| [int32\_t OH\_ArkUI\_PointerEvent\_CreateClonedEvent(const ArkUI\_UIInputEvent\* event, ArkUI\_UIInputEvent\*\* clonedEvent)](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedevent) | 基于原始事件指针创建克隆事件指针。仅对触摸事件有效。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_DestroyClonedEvent(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_destroyclonedevent) | 销毁由OH\_ArkUI\_PointerEvent\_CreateClonedEvent()创建的克隆事件指针。克隆事件使用完毕后应调用该接口释放资源。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPosition(const ArkUI\_UIInputEvent\* event, float x, float y)](capi-ui-input-event-h.md#oh_arkui_pointerevent_setclonedeventlocalposition) | 设置指向性克隆事件相对于当前组件左上角的X坐标和Y坐标。该接口应在调用OH\_ArkUI\_PointerEvent\_CreateClonedEvent()创建克隆事件后使用；同系列SetClonedEvent接口均仅适用于克隆事件。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPositionByIndex(const ArkUI\_UIInputEvent\* event, float x, float y, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_setclonedeventlocalpositionbyindex) | 设置克隆指向性事件特定接触点相对于当前组件左上角的X坐标和Y坐标。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedevent)接口创建的ArkUI\_UIInputEvent克隆事件指针才能使用此接口。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventActionType(const ArkUI\_UIInputEvent\* event, int32\_t actionType)](capi-ui-input-event-h.md#oh_arkui_pointerevent_setclonedeventactiontype) | 设置当前带有指向性的克隆输入事件的动作类型。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventChangedFingerId(const ArkUI\_UIInputEvent\* event, int32\_t fingerId)](capi-ui-input-event-h.md#oh_arkui_pointerevent_setclonedeventchangedfingerid) | 设置当前带有指向性的克隆输入事件的触摸点ID。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventFingerIdByIndex(const ArkUI\_UIInputEvent\* event, int32\_t fingerId, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_pointerevent_setclonedeventfingeridbyindex) | 设置带有指向性的克隆输入事件特定接触点的触摸点ID。 |
| [int32\_t OH\_ArkUI\_PointerEvent\_PostClonedEvent(ArkUI\_NodeHandle node, const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_postclonedevent) | 转发克隆事件到特定节点。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent(const ArkUI\_UIInputEvent\* event, ArkUI\_UIInputEvent\*\* clonedEvent)](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent) | 创建指定事件的克隆事件。该接口适用于触摸事件、鼠标事件和轴事件。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PointerEvent\_CreatePointerEvent(ArkUI\_UIInputEvent\*\* event, ArkUI\_UIInputEvent\_Type type)](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent) | 创建新事件，不克隆现有事件。该接口适用于触摸事件、鼠标事件和轴事件。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PointerEvent\_DestroyClonedPointerEvent(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_pointerevent_destroyclonedpointerevent) | 销毁克隆事件指针。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetActionType(const ArkUI\_UIInputEvent\* event, int32\_t type)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setactiontype) | 设置克隆事件的动作类型。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetSourceType(const ArkUI\_UIInputEvent\* event, int32\_t sourceType)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setsourcetype) | 设置克隆事件的源类型。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetToolType(const ArkUI\_UIInputEvent\* event, int32\_t toolType)](capi-ui-input-event-h.md#oh_arkui_clonedevent_settooltype) | 设置克隆事件的工具类型。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetPressure(const ArkUI\_UIInputEvent\* event, float pressure)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setpressure) | 设置克隆事件应用于触摸屏的压力。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetPressureByIndex(const ArkUI\_UIInputEvent\* event, float pressure, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setpressurebyindex) | 设置克隆事件指定触摸点应用于触摸屏的压力。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetEventTime(const ArkUI\_UIInputEvent\* event, int64\_t timestamp)](capi-ui-input-event-h.md#oh_arkui_clonedevent_seteventtime) | 设置克隆UI输入事件发生的时间。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetDeviceId(const ArkUI\_UIInputEvent\* event, int32\_t deviceId)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setdeviceid) | 设置触发克隆UI输入事件的设备ID。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetTargetDisplayId(const ArkUI\_UIInputEvent\* event, int32\_t targetDisplayId)](capi-ui-input-event-h.md#oh_arkui_clonedevent_settargetdisplayid) | 设置克隆UI输入事件发生的屏幕ID。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetChangedFingerId(const ArkUI\_UIInputEvent\* event, int32\_t fingerId)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setchangedfingerid) | 设置克隆指针事件的触摸点ID。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetFingerIdByIndex(const ArkUI\_UIInputEvent\* event, int32\_t fingerId, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setfingeridbyindex) | 设置克隆事件特定接触点的触摸点ID。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetChangedWindowPosition(const ArkUI\_UIInputEvent\* event, float x, float y)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setchangedwindowposition) | 设置克隆事件相对于当前窗口左上角的X坐标和Y坐标。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetWindowPositionByIndex(const ArkUI\_UIInputEvent\* event, float x, float y, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setwindowpositionbyindex) | 设置克隆事件特定接触点相对于当前窗口左上角的X坐标和Y坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetChangedScreenPosition(const ArkUI\_UIInputEvent\* event, float x, float y)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setchangedscreenposition) | 设置克隆事件相对于当前屏幕左上角的X坐标和Y坐标。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetScreenPositionByIndex(const ArkUI\_UIInputEvent\* event, float x, float y, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setscreenpositionbyindex) | 设置克隆事件特定接触点相对于当前屏幕左上角的X坐标和Y坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetChangedGlobalDisplayPosition(const ArkUI\_UIInputEvent\* event, float x, float y)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setchangedglobaldisplayposition) | 设置克隆事件在[全局坐标系](../harmonyos-guides/window-terminology.md#global-coordinate-system全局坐标系)的坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetGlobalDisplayPositionByIndex(const ArkUI\_UIInputEvent\* event, float x, float y, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setglobaldisplaypositionbyindex) | 设置克隆事件在[全局坐标系](../harmonyos-guides/window-terminology.md#global-coordinate-system全局坐标系)的坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetHandleId(const ArkUI\_UIInputEvent\* event, int32\_t eventHandleId)](capi-ui-input-event-h.md#oh_arkui_clonedevent_sethandleid) | 设置事件处理会话的唯一句柄。该句柄必须用于对该事件的任何进一步操作。对于给定的手指，同一时间只有一个具有此句柄的事件处于活动状态。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetTiltAngle(const ArkUI\_UIInputEvent\* event, float tiltX, float tiltY)](capi-ui-input-event-h.md#oh_arkui_clonedevent_settiltangle) | 设置克隆事件相对于YZ平面和XZ平面的倾斜角度。tiltX取值范围为[-90, 90]，其中正值表示向右倾斜；tiltY取值范围为[-90, 90]，其中正值表示向下倾斜。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetRollAngle(const ArkUI\_UIInputEvent\* event, float rollAngle)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setrollangle) | 设置克隆事件触控笔绕Z轴的旋转角度。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetPressedKeys(const ArkUI\_UIInputEvent\* event, int32\_t\* pressedKeyCodes, int32\_t length)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setpressedkeys) | 设置克隆事件中所有按下的按键。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetChangedTouchArea(const ArkUI\_UIInputEvent\* event, float width, float height)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setchangedtoucharea) | 设置克隆事件的手指接触区域的宽度和高度，该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetTouchAreaByIndex(const ArkUI\_UIInputEvent\* event, float width, float height, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_settouchareabyindex) | 设置克隆事件特定接触点的手指接触区域的宽度和高度，该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetChangedInteractionHand(const ArkUI\_UIInputEvent\* event, int32\_t hand)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setchangedinteractionhand) | 设置克隆事件是左手或右手触发。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetInteractionHandByIndex(const ArkUI\_UIInputEvent\* event, int32\_t hand, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setinteractionhandbyindex) | 设置克隆事件特定接触点由左手或右手触发。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetPressedTimeByIndex(const ArkUI\_UIInputEvent\* event, int64\_t pressedTime, int32\_t pointerIndex)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setpressedtimebyindex) | 设置克隆事件指定触摸点的按下时间。该接口仅适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetPinchAxisScaleValue(const ArkUI\_UIInputEvent\* event, double pinchAxisScaleValue)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setpinchaxisscalevalue) | 设置克隆事件的捏合轴缩放值。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetHorizontalAxisScaleValue(const ArkUI\_UIInputEvent\* event, double horizontalAxisScaleValue)](capi-ui-input-event-h.md#oh_arkui_clonedevent_sethorizontalaxisscalevalue) | 设置克隆事件水平滚动轴的值。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetVerticalAxisScaleValue(const ArkUI\_UIInputEvent\* event, double verticalAxisScaleValue)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setverticalaxisscalevalue) | 设置克隆事件垂直滚动轴的值。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetScrollStep(const ArkUI\_UIInputEvent\* event, int32\_t scrollStep)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setscrollstep) | 设置克隆事件的滚动步长系数。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetMouseButton(const ArkUI\_UIInputEvent\* event, int32\_t button)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setmousebutton) | 设置克隆事件的按键类型值。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetRawDeltaX(const ArkUI\_UIInputEvent\* event, float rawDeltaX)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setrawdeltax) | 设置鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetRawDeltaY(const ArkUI\_UIInputEvent\* event, float rawDeltaY)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setrawdeltay) | 设置鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ClonedEvent\_SetPressedButtons(const ArkUI\_UIInputEvent\* event, const int32\_t\* pressedButtons, int32\_t length)](capi-ui-input-event-h.md#oh_arkui_clonedevent_setpressedbuttons) | 设置克隆事件的按下的按键。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PointerEvent\_PostClonedEventWithStrategy(ArkUI\_NodeHandle node, const ArkUI\_UIInputEvent\* event, ArkUI\_CompetitionStrategy strategy)](capi-ui-input-event-h.md#oh_arkui_pointerevent_postclonedeventwithstrategy) | 使用指定的竞争策略将克隆事件发送到特定节点，适用于向目标节点注入克隆事件并需要控制注入事件与目标节点已有手势之间是否竞争的场景。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_UIInputEvent\_GetLatestStatus()](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getlateststatus) | 调用该方法获取最近一次UIInput相关方法的执行情况。通常情况下不需要使用该方法，仅在调用UIInput相关方法后需要确认最近一次调用是否执行异常时使用。 |
| [ArkUI\_CoastingAxisEvent\* OH\_ArkUI\_UIInputEvent\_GetCoastingAxisEvent(ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getcoastingaxisevent) | 从组件事件中获取惯性滚动轴事件，仅当用户在触控板上使用双指执行满足系统惯性滚动判定条件的抛滑操作，且指针位置下存在注册了[NODE\_ON\_COASTING\_AXIS\_EVENT](capi-native-node-h.md#arkui_nodeeventtype)事件的组件时，才能获取到有效事件。在从[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象获取到[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)对象后调用此方法。惯性滚动轴事件仅在双指抛滑并离开触控板时触发，因此仅支持触控板。惯性滚动轴事件会在手指离开触控板后，根据抛滑速度产生轴值逐渐衰减的事件。由于刷新频率和性能的影响，当前事件轴值可能高于或低于上一个事件值。在惯性滚动轴事件期间，以下四种行为会中断事件，并立即收到[ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_END](capi-ui-input-event-h.md#arkui_coastingaxiseventphase)。1. 手指触摸触控板。2. 滚动鼠标滚轮。3. 手指或鼠标点击注册了惯性滚动轴事件的节点。需要注意的是，点击未注册此事件的节点不会产生任何效果。例如，A节点注册了惯性滚动轴事件，当事件发生时，让B节点滚动，但点击B节点不会中断此事件。点击事件的中断行为受[OH\_ArkUI\_PointerEvent\_SetInterceptHitTestMode](capi-ui-input-event-h.md#oh_arkui_pointerevent_setintercepthittestmode)的影响。此外，如果用户点击区域存在已收集的可响应惯性滚动轴事件的节点，本次惯性滚动轴事件会被强制终止。4. 应用休眠（例如最小化、锁屏）。 |
| [int64\_t OH\_ArkUI\_CoastingAxisEvent\_GetEventTime(ArkUI\_CoastingAxisEvent\* event)](capi-ui-input-event-h.md#oh_arkui_coastingaxisevent_geteventtime) | 获取惯性滚动轴事件发生的时间。 |
| [ArkUI\_CoastingAxisEventPhase OH\_ArkUI\_CoastingAxisEvent\_GetPhase(ArkUI\_CoastingAxisEvent\* event)](capi-ui-input-event-h.md#oh_arkui_coastingaxisevent_getphase) | 获取惯性滚动轴事件发生时的滚动阶段。 |
| [float OH\_ArkUI\_CoastingAxisEvent\_GetDeltaY(ArkUI\_CoastingAxisEvent\* event)](capi-ui-input-event-h.md#oh_arkui_coastingaxisevent_getdeltay) | 获取惯性滚动轴事件垂直方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从上往下滑动时为负数，双指从下往上滑动时为正数。 |
| [float OH\_ArkUI\_CoastingAxisEvent\_GetDeltaX(ArkUI\_CoastingAxisEvent\* event)](capi-ui-input-event-h.md#oh_arkui_coastingaxisevent_getdeltax) | 获取惯性滚动轴事件水平方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从左往右滑动时为负数，双指从右往左滑动时为正数。 |
| [int32\_t OH\_ArkUI\_CoastingAxisEvent\_SetPropagation(ArkUI\_CoastingAxisEvent\* event, bool propagation)](capi-ui-input-event-h.md#oh_arkui_coastingaxisevent_setpropagation) | 设置惯性滚动轴事件是否启用冒泡，默认禁止冒泡。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_GetTouchTestInfoList(ArkUI\_TouchTestInfo\* info, ArkUI\_TouchTestInfoItemArray\* array, int32\_t\* size)](capi-ui-input-event-h.md#oh_arkui_touchtestinfo_gettouchtestinfolist) | 获取触摸测试信息中的触摸测试信息项数组。 |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetX(const ArkUI\_TouchTestInfoItem\* info)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getx) | 从触摸测试信息项中获取相对于子组件左上角的X坐标，单位为px。 |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetY(const ArkUI\_TouchTestInfoItem\* info)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_gety) | 从触摸测试信息项中获取相对于子组件左上角的Y坐标，单位为px。 |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetWindowX(const ArkUI\_TouchTestInfoItem\* info)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getwindowx) | 从触摸测试信息项中获取相对于当前应用窗口左上角的X坐标，单位为px。 |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetWindowY(const ArkUI\_TouchTestInfoItem\* info)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getwindowy) | 从触摸测试信息项中获取相对于当前应用窗口左上角的Y坐标，单位为px。 |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetXRelativeToParent(const ArkUI\_TouchTestInfoItem\* info)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getxrelativetoparent) | 从触摸测试信息项中获取相对于父组件左上角的X坐标，单位为px。 |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetYRelativeToParent(const ArkUI\_TouchTestInfoItem\* info)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getyrelativetoparent) | 从触摸测试信息项中获取相对于父组件左上角的Y坐标，单位为px。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfoItem\_GetChildRect(const ArkUI\_TouchTestInfoItem\* info, ArkUI\_Rect\* childRect)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getchildrect) | 从触摸测试信息项中获取子组件的边界矩形信息。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfoItem\_GetChildId(const ArkUI\_TouchTestInfoItem\* info, char\* buffer, int32\_t bufferSize)](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getchildid) | 从触摸测试信息项中获取子组件的ID。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_SetTouchResultStrategy(ArkUI\_TouchTestInfo\* info, ArkUI\_TouchTestStrategy strategy)](capi-ui-input-event-h.md#oh_arkui_touchtestinfo_settouchresultstrategy) | 设置触摸测试策略，即组件及其子组件在命中测试过程中的行为方式，适用于自定义触摸命中结果、将触摸事件分发给指定子组件或控制兄弟节点是否继续参与命中测试的场景。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_SetTouchResultId(ArkUI\_TouchTestInfo\* info, const char\* id)](capi-ui-input-event-h.md#oh_arkui_touchtestinfo_settouchresultid) | 设置命中测试过程中需要作用的子组件ID，适用于自定义触摸测试结果并希望将触摸事件分发到指定子组件的场景。 |
| [int64\_t OH\_ArkUI\_DigitalCrownEvent\_GetEventTime(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_digitalcrownevent_geteventtime) | 获取表冠事件发生的时间。单位为ns。仅适用于入参event里存储的是表冠事件对象的场景。 |
| [double OH\_ArkUI\_DigitalCrownEvent\_GetAngularVelocity(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_digitalcrownevent_getangularvelocity) | 获取表冠事件发生的角速度。单位为°/s。仅适用于入参event里存储的是表冠事件对象的场景。 |
| [double OH\_ArkUI\_DigitalCrownEvent\_GetDegree(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_digitalcrownevent_getdegree) | 获取表冠事件发生的旋转角度。单位为°。仅适用于入参event里存储的是表冠事件对象的场景。 |
| [ArkUI\_CrownEvent\_Action OH\_ArkUI\_DigitalCrownEvent\_GetAction(const ArkUI\_UIInputEvent\* event)](capi-ui-input-event-h.md#oh_arkui_digitalcrownevent_getaction) | 获取表冠事件发生的阶段。仅适用于入参event里存储的是表冠事件对象的场景。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DigitalCrownEvent\_SetStopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)](capi-ui-input-event-h.md#oh_arkui_digitalcrownevent_setstoppropagation) | 设置是否阻止事件冒泡，适用于当前组件已处理表冠事件且不希望该事件继续传递给父组件或其他祖先组件的场景。仅适用于入参event里存储的是表冠事件对象的场景。 |

## 枚举类型说明

### ArkUI\_UIInputEvent\_Type

```c
enum ArkUI_UIInputEvent_Type
```

**描述：**

UI输入事件类型定义。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_UIINPUTEVENT\_TYPE\_UNKNOWN = 0 | 未知。 |
| ARKUI\_UIINPUTEVENT\_TYPE\_TOUCH = 1 | 触摸事件。 |
| ARKUI\_UIINPUTEVENT\_TYPE\_AXIS = 2 | 轴事件。 |
| ARKUI\_UIINPUTEVENT\_TYPE\_MOUSE = 3 | 鼠标事件。 |
| ARKUI\_UIINPUTEVENT\_TYPE\_KEY = 4 | 按键事件。  **起始版本：** 20 |
| ARKUI\_UIINPUTEVENT\_TYPE\_DIGITAL\_CROWN = 5 | 表冠事件。  **起始版本：** 24 |

### anonymous1

```c
enum anonymous1
```

**描述：**

定义输入事件的行为类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| UI\_TOUCH\_EVENT\_ACTION\_CANCEL = 0 | 触摸取消。 |
| UI\_TOUCH\_EVENT\_ACTION\_DOWN = 1 | 触摸按下。 |
| UI\_TOUCH\_EVENT\_ACTION\_MOVE = 2 | 触摸移动。 |
| UI\_TOUCH\_EVENT\_ACTION\_UP = 3 | 触摸抬起。 |

### anonymous2

```c
enum anonymous2
```

**描述：**

产生输入事件的工具类型定义。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_UNKNOWN = 0 | 不支持的工具类型。 |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_FINGER = 1 | 手指。 |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_PEN = 2 | 触控笔。 |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_MOUSE = 3 | 鼠标。 |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_TOUCHPAD = 4 | 触控板。 |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_JOYSTICK = 5 | 操纵杆。 |

### anonymous3

```c
enum anonymous3
```

**描述：**

产生输入事件的来源类型定义。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_UNKNOWN = 0 | 未知输入源。 |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_MOUSE = 1 | 鼠标。 |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_TOUCH\_SCREEN = 2 | 触摸屏。 |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_KEY = 4 | 按键。  **起始版本：** 22 |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_JOYSTICK = 5 | 手柄。  **起始版本：** 22 |

### HitTestMode

```c
enum HitTestMode
```

**描述：**

定义触摸测试类型的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HTM\_DEFAULT = 0 | 默认触摸测试效果。自身及子节点响应触摸测试，但阻塞兄弟节点的触摸测试，不影响祖先节点的触摸测试。 |
| HTM\_BLOCK = 1 | 自身响应触摸测试，阻塞子节点、兄弟节点和祖先节点的触摸测试。 |
| HTM\_TRANSPARENT = 2 | 自身和子节点都响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。 |
| HTM\_NONE = 3 | 自身不响应触摸测试，不会阻塞子节点、兄弟节点和祖先节点的触摸测试。 |
| HTM\_BLOCK\_HIERARCHY = 4 | 自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试。  **起始版本：** 20 |
| HTM\_BLOCK\_DESCENDANTS = 5 | 自身不响应触摸测试，并且所有的后代（孩子、孙子等）也不响应触摸测试，不会影响祖先节点的触摸测试。  **起始版本：** 20 |

### anonymous4

```c
enum anonymous4
```

**描述：**

定义鼠标事件的行为类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| UI\_MOUSE\_EVENT\_ACTION\_UNKNOWN = 0 | 无效行为。  **说明：** 此行为由系统侧处理，开发者无需关注。 |
| UI\_MOUSE\_EVENT\_ACTION\_PRESS = 1 | 鼠标按键按下。 |
| UI\_MOUSE\_EVENT\_ACTION\_RELEASE = 2 | 鼠标按键松开。 |
| UI\_MOUSE\_EVENT\_ACTION\_MOVE = 3 | 鼠标移动。 |
| UI\_MOUSE\_EVENT\_ACTION\_CANCEL = 13 | 鼠标按键被取消。  **起始版本：** 18 |

### anonymous5

```c
enum anonymous5
```

**描述：**

定义鼠标事件的按键类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| UI\_MOUSE\_EVENT\_BUTTON\_NONE = 0 | 无按键。 |
| UI\_MOUSE\_EVENT\_BUTTON\_LEFT = 1 | 鼠标左键。 |
| UI\_MOUSE\_EVENT\_BUTTON\_RIGHT = 2 | 鼠标右键。 |
| UI\_MOUSE\_EVENT\_BUTTON\_MIDDLE = 3 | 鼠标中键。 |
| UI\_MOUSE\_EVENT\_BUTTON\_BACK = 4 | 鼠标左侧后退键。 |
| UI\_MOUSE\_EVENT\_BUTTON\_FORWARD = 5 | 鼠标左侧前进键。 |

### ArkUI\_ModifierKeyName

```c
enum ArkUI_ModifierKeyName
```

**描述：**

定义修饰键。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MODIFIER\_KEY\_CTRL = 1 << 0 | Ctrl. |
| ARKUI\_MODIFIER\_KEY\_SHIFT = 1 << 1 | Shift. |
| ARKUI\_MODIFIER\_KEY\_ALT = 1 << 2 | Alt. |
| ARKUI\_MODIFIER\_KEY\_FN = 1 << 3 | Fn（仅调试使用，通常不上报Fn状态）。 |

### anonymous6

```c
enum anonymous6
```

**描述：**

定义[焦点轴事件](ts-universal-events-focus_axis.md)的轴类型。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_X = 0 | 游戏手柄X轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_Y = 1 | 游戏手柄Y轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_Z = 2 | 游戏手柄Z轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_RZ = 3 | 游戏手柄RZ轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_GAS = 4 | 游戏手柄GAS轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_BRAKE = 5 | 游戏手柄BRAKE轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT0X = 6 | 游戏手柄HAT0X轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT0Y = 7 | 游戏手柄HAT0Y轴。 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_RX = 8 | 游戏手柄RX轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_RY = 9 | 游戏手柄RY轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_THROTTLE = 10 | 游戏手柄THROTTLE轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_RUDDER = 11 | 游戏手柄RUDDER轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_WHEEL = 12 | 游戏手柄WHEEL轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT1X = 13 | 游戏手柄HAT1X轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT1Y = 14 | 游戏手柄HAT1Y轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT2X = 15 | 游戏手柄HAT2X轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT2Y = 16 | 游戏手柄HAT2Y轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT3X = 17 | 游戏手柄HAT3X轴。  **起始版本：** 23 |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT3Y = 18 | 游戏手柄HAT3Y轴。  **起始版本：** 23 |

### ArkUI\_InteractionHand

```c
enum ArkUI_InteractionHand
```

**描述：**

定义触摸事件是左手还是右手。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_EVENT\_HAND\_NONE = 0 | 未知。 |
| ARKUI\_EVENT\_HAND\_LEFT = 1 | 左手。 |
| ARKUI\_EVENT\_HAND\_RIGHT = 2 | 右手。 |

### anonymous7

```c
enum anonymous7
```

**描述：**

定义[轴事件](ts-universal-events-axis.md)的操作类型。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| UI\_AXIS\_EVENT\_ACTION\_NONE = 0 | 轴事件异常。 |
| UI\_AXIS\_EVENT\_ACTION\_BEGIN = 1 | 轴事件开始。 |
| UI\_AXIS\_EVENT\_ACTION\_UPDATE = 2 | 轴事件更新。 |
| UI\_AXIS\_EVENT\_ACTION\_END = 3 | 轴事件结束。 |
| UI\_AXIS\_EVENT\_ACTION\_CANCEL = 4 | 轴事件取消。 |

### anonymous8

```c
enum anonymous8
```

**描述：**

定义轴事件的轴类型。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| UI\_AXIS\_TYPE\_VERTICAL\_AXIS = 0 | 垂直滚动轴。 |
| UI\_AXIS\_TYPE\_HORIZONTAL\_AXIS = 1 | 水平滚动轴。 |
| UI\_AXIS\_TYPE\_PINCH\_AXIS = 2 | 捏合轴。 |

### ArkUI\_CoastingAxisEventPhase

```c
enum ArkUI_CoastingAxisEventPhase
```

**描述：**

定义惯性滚动轴事件的阶段。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_NONE = 0 | 非惯性轴事件阶段，异常默认值，可以通过检查惯性轴阶段值不为该值来判断当前惯性轴事件是有效的。 |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_BEGIN = 1 | 惯性滚动轴事件开始，此为惯性阶段的第一个事件。 |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_UPDATE = 2 | 惯性滚动轴事件更新，此阶段可以获取惯性轴值增量来处理滚动偏移。 |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_END = 3 | 惯性滚动轴事件结束，此值在惯性被刹停（惯性滚动阶段用户重新触摸触控板或通过鼠标及触屏与组件产生交互等）或惯性衰减至自然停止时发送，到达此阶段时，应立即停止惯性滚动效果。 |

### ArkUI\_TouchTestStrategy

```c
enum ArkUI_TouchTestStrategy
```

**描述：**

定义触摸测试策略。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TOUCH\_TEST\_STRATEGY\_DEFAULT = 0 | 自定义分发不产生影响，系统按当前节点命中状态分发事件。 |
| ARKUI\_TOUCH\_TEST\_STRATEGY\_FORWARD\_COMPETITION = 1 | 应用指定分发事件到某个子节点，其他兄弟节点是否分发事件交由系统决定。 |
| ARKUI\_TOUCH\_TEST\_STRATEGY\_FORWARD = 2 | 应用指定分发事件到某个子节点，系统不再分发事件到其他兄弟节点。 |

### ArkUI\_CompetitionStrategy

```c
enum ArkUI_CompetitionStrategy
```

**描述：**

事件的注入方和被注入方间手势识别结果是否为竞争场景的策略。该策略决定了事件的注入方如何与被注入方的手势处理逻辑交互，非竞争场景会同时触发手势，竞争场景只触发其中一个。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_COMPETITION\_STRATEGY\_DEFAULT = 0 | 无竞争策略。注入的事件不与任何现有手势竞争。注入的事件和现有手势可以独立并行处理。 |
| ARKUI\_COMPETITION\_STRATEGY\_COMPETITION = 1 | 竞争策略。事件注入方和被注入方间的手势为竞争关系，只能处理其中一方的手势。 |

### ArkUI\_CrownEvent\_Action

```c
enum ArkUI_CrownEvent_Action
```

**描述：**

定义表冠事件的阶段。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CROWNEVENT\_ACTION\_UNKNOWN = 0 | 未知的表冠事件阶段。 |
| ARKUI\_CROWNEVENT\_ACTION\_UPDATE = 1 | 表冠事件更新。 |
| ARKUI\_CROWNEVENT\_ACTION\_END = 2 | 表冠事件结束。 |

## 函数说明

### OH\_ArkUI\_UIInputEvent\_GetType()

```c
int32_t OH_ArkUI_UIInputEvent_GetType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件的类型。在访问一个ArkUI\_UIInputEvent指针对象之前，推荐使用该方法判断该输入事件的类型，该接口会返回[ArkUI\_UIInputEvent\_Type](capi-ui-input-event-h.md#arkui_uiinputevent_type)枚举中的一种。比如，当事件是一个触控类型时，由于触控类型是指向性事件，那么使用OH\_ArkUI\_UIInputEvent\_GetXXX及OH\_ArkUI\_PointerEvent\_GetXXX系列接口，均可以正常访问；而如果使用OH\_ArkUI\_KeyEvent\_GetXXX相关接口访问该触控事件，则接口返回值不保证有效。对于还未支持的事件类型，接口返回默认值0。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回当前UI输入事件的类型，如果参数异常则返回0。 |

### OH\_ArkUI\_UIInputEvent\_GetAction()

```c
int32_t OH_ArkUI_UIInputEvent_GetAction(const ArkUI_UIInputEvent* event)
```

**描述：**

获取输入事件的 action 类型。action 类型为基础事件在不同阶段的类型定义，通常代表事件的特点，并表征事件的开始与结束，如touch down、touch up。触控事件的action类型为[UI\_TOUCH\_EVENT\_ACTION](capi-ui-input-event-h.md#anonymous1)，鼠标事件的action类型为[UI\_MOUSE\_EVENT\_ACTION](capi-ui-input-event-h.md#anonymous4)。轴事件的action类型获取请使用[OH\_ArkUI\_AxisEvent\_GetAxisAction](capi-ui-input-event-h.md#oh_arkui_axisevent_getaxisaction)接口，返回值类型为[UI\_AXIS\_EVENT\_ACTION](capi-ui-input-event-h.md#anonymous7)；按键事件的action类型获取请使用[OH\_ArkUI\_KeyEvent\_GetType](capi-native-key-event-h.md#oh_arkui_keyevent_gettype)接口，返回值类型为[ArkUI\_KeyEventType](capi-native-key-event-h.md#arkui_keyeventtype)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回当前UI输入事件的操作类型，如果参数异常则返回-1。 |

### OH\_ArkUI\_UIInputEvent\_GetSourceType()

```c
int32_t OH_ArkUI_UIInputEvent_GetSourceType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件的触发源类型。输入源为产生输入事件的真实物理设备，如触摸屏、鼠标等，由[UI\_INPUT\_EVENT\_SOURCE\_TYPE](capi-ui-input-event-h.md#anonymous3)定义，而输入工具为操作输入源设备来产生事件的工具，如手指、触控笔。当用户操作鼠标时，鼠标既是输入源，也是输入工具。对于按键事件，并不支持获取输入源类型，返回unknown。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回产生当前UI输入事件的来源类型。 |

### OH\_ArkUI\_UIInputEvent\_GetToolType()

```c
int32_t OH_ArkUI_UIInputEvent_GetToolType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件的工具类型。输入工具是操作输入源设备以产生事件的工具，如手指、触控笔。它们自身不直接产生事件，但可以驱动输入源设备不断产生事件。返回类型由[UI\_INPUT\_EVENT\_TOOL\_TYPE](capi-ui-input-event-h.md#anonymous2)枚举定义。对于按键事件，不支持获取输入工具类型，返回 unknown。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回产生当前UI输入事件的工具类型。 |

### OH\_ArkUI\_UIInputEvent\_GetEventTime()

```c
int64_t OH_ArkUI_UIInputEvent_GetEventTime(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件发生的时间。单位为ns。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回UI输入事件发生的时间，如果参数异常则返回0。 |

### OH\_ArkUI\_PointerEvent\_GetPointerCount()

```c
uint32_t OH_ArkUI_PointerEvent_GetPointerCount(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点数量。指向性事件一般是附带有事件发生位置信息的事件，如触摸事件，用户操作时，可以感知事件在什么位置发生。而非指向性事件，如按键事件，一般没有位置信息，没有触点的说法，该接口永远返回0。对于触摸事件，该接口多用于处理多指触控，判断用户有几根手指在操作当前控件。而对于鼠标和轴事件，可认为触点只有1个，该接口永远返回1。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回当前指向性输入事件的接触点数量。 |

### OH\_ArkUI\_PointerEvent\_GetPointerId()

```c
int32_t OH_ArkUI_PointerEvent_GetPointerId(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点标识。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效取值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event)-1]。超出范围时返回参数异常结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回特定接触点标识。 |

### OH\_ArkUI\_PointerEvent\_GetChangedPointerId()

```c
int32_t OH_ArkUI_PointerEvent_GetChangedPointerId(const ArkUI_UIInputEvent* event, uint32_t* pointerIndex)
```

**描述：**

获取触发当前事件的手指ID。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t\* pointerIndex | 输出参数，用于接收触发当前事件的触点在多点触控数据列表中的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_PointerEvent\_GetX()

```c
float OH_ArkUI_PointerEvent_GetX(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的X坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前组件左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetXByIndex()

```c
float OH_ArkUI_PointerEvent_GetXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号；对于鼠标和轴事件，该参数大于0时返回默认值0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回指向性输入事件中特定接触点相对于当前组件左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetY()

```c
float OH_ArkUI_PointerEvent_GetY(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的Y坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前组件左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetYByIndex()

```c
float OH_ArkUI_PointerEvent_GetYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号；对于鼠标和轴事件，仅支持索引0，传入大于0的索引时返回0.0f；对于触摸事件，传入超出有效范围的索引时返回0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回指向性输入事件中特定接触点相对于当前组件左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetCurrentLocalX()

```c
float OH_ArkUI_PointerEvent_GetCurrentLocalX(const ArkUI_UIInputEvent* event)
```

**描述：**

从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取相对于当前组件左上角的X坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前组件左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetCurrentLocalXByIndex()

```c
float OH_ArkUI_PointerEvent_GetCurrentLocalXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取特定接触点相对于当前组件左上角的X坐标。

pointerIndex为uint32\_t，不存在小于0的取值；当索引超出当前事件支持的触点范围时为非法值。

对于鼠标和轴事件，当索引值非0时为非法值。

对于触摸事件，根据给定的索引获取特定接触点相对于当前组件左上角的X坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引。对于鼠标和轴事件，该参数必须为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回特定接触点相对于当前组件左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetCurrentLocalY()

```c
float OH_ArkUI_PointerEvent_GetCurrentLocalY(const ArkUI_UIInputEvent* event)
```

**描述：**

从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取相对于当前组件左上角的Y坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前组件左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetCurrentLocalYByIndex()

```c
float OH_ArkUI_PointerEvent_GetCurrentLocalYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)（如触摸事件、鼠标事件、轴事件）中根据实时位置获取特定接触点相对于当前组件左上角的Y坐标。

pointerIndex为uint32\_t，不存在小于0的取值；当索引超出当前事件支持的触点范围时为非法值。

对于鼠标和轴事件，当索引值非0时为非法值。

对于触摸事件，根据给定的索引获取特定接触点相对于当前组件左上角的Y坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引。对于鼠标和轴事件，该参数必须为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回特定接触点相对于当前组件左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetWindowX()

```c
float OH_ArkUI_PointerEvent_GetWindowX(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的X坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前应用窗口左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetWindowXByIndex()

```c
float OH_ArkUI_PointerEvent_GetWindowXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号；对于鼠标和轴事件，仅支持索引0，传入大于0的索引时返回0.0f；对于触摸事件，传入超出有效范围的索引时返回0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回指向性输入事件中特定接触点相对于当前应用窗口左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetWindowY()

```c
float OH_ArkUI_PointerEvent_GetWindowY(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的Y坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前应用窗口左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetWindowYByIndex()

```c
float OH_ArkUI_PointerEvent_GetWindowYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号；对于鼠标和轴事件，仅支持索引0，传入大于0的索引时返回0.0f；对于触摸事件，传入超出有效范围的索引时返回0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回指向性输入事件中特定接触点相对于当前应用窗口左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetDisplayX()

```c
float OH_ArkUI_PointerEvent_GetDisplayX(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的X坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前屏幕左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex()

```c
float OH_ArkUI_PointerEvent_GetDisplayXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号；对于鼠标和轴事件，仅支持索引0，传入大于0的索引时返回0.0f；对于触摸事件，传入超出有效范围的索引时返回0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回指向性输入事件中特定接触点相对于当前屏幕左上角的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetDisplayY()

```c
float OH_ArkUI_PointerEvent_GetDisplayY(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的Y坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件相对于当前屏幕左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex()

```c
float OH_ArkUI_PointerEvent_GetDisplayYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号；对于鼠标和轴事件，仅支持索引0，传入大于0的索引时返回0.0f；对于触摸事件，传入超出有效范围的索引时返回0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回指向性输入事件中特定接触点相对于当前屏幕左上角的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetGlobalDisplayX()

```c
float OH_ArkUI_PointerEvent_GetGlobalDisplayX(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)事件中获取位置信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回相对于全局显示的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果发生任何参数错误，例如传递的一个事件没有位置信息，则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetGlobalDisplayXByIndex()

```c
float OH_ArkUI_PointerEvent_GetGlobalDisplayXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从指向性输入事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引。有效值范围[0, [OH\_ArkUI\_PointerEvent\_GetPointerCount()](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpointercount) - 1]；对于鼠标和轴事件，该参数必须为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回指向性输入事件中特定接触点相对于全局显示的X坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果发生任何参数错误，则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetGlobalDisplayY()

```c
float OH_ArkUI_PointerEvent_GetGlobalDisplayY(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)事件中获取位置信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回相对于全局显示的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果发生任何参数错误，例如传递的一个事件没有位置信息，则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetGlobalDisplayYByIndex()

```c
float OH_ArkUI_PointerEvent_GetGlobalDisplayYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从指向性输入事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引。有效值范围[0, [OH\_ArkUI\_PointerEvent\_GetPointerCount()](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpointercount) - 1]；对于鼠标和轴事件，该参数必须为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回相对于全局显示的Y坐标。默认单位为vp，单位可跟随[setLengthMetricUnit](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlengthmetricunit)的设置而变化。如果发生任何参数错误，则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetPressure()

```c
float OH_ArkUI_PointerEvent_GetPressure(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取触屏压力，适用于绘图、书写等需要根据触控压力调整笔刷粗细或交互效果的场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]。超出范围时返回默认值0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件产生的触屏压力。取值范围为[0, 1]，压感大小与数值正相关。如果参数异常则返回默认值0.0f。不同设备的硬件参数配置可能存在差异，部分设备可能返回大于1的值。 |

### OH\_ArkUI\_PointerEvent\_GetTiltX()

```c
float OH_ArkUI_PointerEvent_GetTiltX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取相对YZ平面的角度，适用于绘图、书写等需要根据触控笔倾斜方向调整笔刷效果的场景。取值的范围[-90, 90]，单位为deg，其中正值是向右倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]。超出范围时返回参数异常结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中相对YZ平面的角度。 |

### OH\_ArkUI\_PointerEvent\_GetTiltY()

```c
float OH_ArkUI_PointerEvent_GetTiltY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取相对XZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向下倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效取值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event)-1]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中相对XZ平面的角度。 |

### OH\_ArkUI\_PointerEvent\_GetRollAngle()

```c
int32_t OH_ArkUI_PointerEvent_GetRollAngle(const ArkUI_UIInputEvent* event, double* rollAngle)
```

**描述：**

获取触控笔绕Z轴旋转的角度，适用于绘图、书写等需要根据触控笔旋转方向调整笔刷方向或交互效果的场景。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向当前UI输入事件的指针。 |
| double\* rollAngle | 触控笔绕Z轴旋转的角度，单位为deg。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，可能是事件指针或rollAngle输出参数无效；请检查并传入有效参数。 |

### OH\_ArkUI\_PointerEvent\_GetTouchAreaWidth()

```c
float OH_ArkUI_PointerEvent_GetTouchAreaWidth(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取触屏区域的宽度。仅适用于手指操作产生的触控事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]。超出范围时返回默认值0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中触屏区域的宽度，单位为px。 |

### OH\_ArkUI\_PointerEvent\_GetTouchAreaHeight()

```c
float OH_ArkUI_PointerEvent_GetTouchAreaHeight(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取触屏区域的高度。仅适用于手指操作产生的触控事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]。超出范围时返回默认值0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中触屏区域的高度，单位为px。 |

### OH\_ArkUI\_PointerEvent\_GetInteractionHand()

```c
int32_t OH_ArkUI_PointerEvent_GetInteractionHand(const ArkUI_UIInputEvent *event, ArkUI_InteractionHand *hand)
```

**描述：**

获取当前触摸事件是左手点击触发还是右手点击触发。仅在支持触控交互手别识别的产品上有效，请通过设备能力查询接口判断当前设备是否支持该功能。该值并非在按下时就能实时获取，在系统完成结果推断之前，皆默认返回NONE，因此请不要将按下阶段的返回值作为最终识别结果。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md) \*event | 表示指向当前UI输入事件的指针。 |
| [ArkUI\_InteractionHand](capi-ui-input-event-h.md#arkui_interactionhand) \*hand | 输出参数，用于接收触摸点的交互手信息，返回值为ARKUI\_EVENT\_HAND\_LEFT、ARKUI\_EVENT\_HAND\_RIGHT或ARKUI\_EVENT\_HAND\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，例如事件指针、hand输出参数或pointerIndex无效，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)；请检查并传入有效参数。 |

### OH\_ArkUI\_PointerEvent\_GetInteractionHandByIndex()

```c
int32_t OH_ArkUI_PointerEvent_GetInteractionHandByIndex(const ArkUI_UIInputEvent *event, int32_t pointerIndex, ArkUI_InteractionHand *hand)
```

**描述：**

获取当前触摸事件是左手点击触发还是右手点击触发。仅在支持触控交互手别识别的产品上有效。该值并非在按下时就能实时获取，在系统完成结果推断之前，皆默认返回NONE，因此请不要将按下阶段的返回值作为最终识别结果。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md) \*event | 表示指向当前UI输入事件的指针。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_InteractionHand](capi-ui-input-event-h.md#arkui_interactionhand) \*hand | 表示触摸点是左手还是右手。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，例如事件指针、hand输出参数或pointerIndex无效，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)；请检查并传入有效参数。 |

### OH\_ArkUI\_PointerEvent\_GetHistorySize()

```c
uint32_t OH_ArkUI_PointerEvent_GetHistorySize(const ArkUI_UIInputEvent* event)
```

**描述：**

从[指向性输入事件](../harmonyos-guides/arkts-interaction-capability-overview.md#指向性事件)中获取历史事件数量。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。历史事件为此次事件与上一次事件之间发生的原始事件，仅在指向性输入事件的移动阶段（即触摸移动或鼠标移动）中适用，在其他状态中调用返回默认值0。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回当前历史事件数量。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryEventTime()

```c
int64_t OH_ArkUI_PointerEvent_GetHistoryEventTime(const ArkUI_UIInputEvent* event, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取历史事件发生的时间。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回UI输入事件发生的时间，单位为ns。如果参数异常则返回0。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount()

```c
uint32_t OH_ArkUI_PointerEvent_GetHistoryPointerCount(const ArkUI_UIInputEvent* event, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取特定历史事件中多点触控的接触点数量。本接口支持的指向性输入事件仅包含触摸事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 特定历史事件中多点触控的接触点数量。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryPointerId()

```c
int32_t OH_ArkUI_PointerEvent_GetHistoryPointerId(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件的历史点中获取多点触控的接触点标识。本接口支持的指向性输入事件仅包含触摸事件。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示特定历史事件中多点触控数据列表的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。超出范围时返回参数异常结果。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回特定历史事件中的特定接触点标识。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryX()

```c
float OH_ArkUI_PointerEvent_GetHistoryX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取特定历史事件中特定接触点相对于当前组件左上角的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于当前组件左上角的X坐标，单位为px。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryY()

```c
float OH_ArkUI_PointerEvent_GetHistoryY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取特定历史事件中特定接触点相对于当前组件左上角的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于当前组件左上角的Y坐标，单位为px。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryWindowX()

```c
float OH_ArkUI_PointerEvent_GetHistoryWindowX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取特定历史事件中特定接触点相对于当前应用窗口左上角的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于当前应用窗口左上角的X坐标，单位为px。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryWindowY()

```c
float OH_ArkUI_PointerEvent_GetHistoryWindowY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取特定历史事件中特定接触点相对于当前应用窗口左上角的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于当前应用窗口左上角的Y坐标，单位为px。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryDisplayX()

```c
float OH_ArkUI_PointerEvent_GetHistoryDisplayX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取特定历史事件中特定接触点相对于当前屏幕左上角的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于当前屏幕左上角的X坐标，单位为px。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryDisplayY()

```c
float OH_ArkUI_PointerEvent_GetHistoryDisplayY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件中获取特定历史事件中特定接触点相对于当前屏幕左上角的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 12开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于当前屏幕左上角的Y坐标，单位为px。如果参数异常则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayX()

```c
float OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从给定指针索引和历史记录索引的指向性输入事件中获取历史事件中相对于全局显示的特定触摸点的X坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。只能从指向性输入事件中获取位置信息，对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 20开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示要返回的历史值，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于全局显示的X坐标，单位为px。如果发生任何参数错误，则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayY()

```c
float OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从给定指针索引和历史记录索引的指向性输入事件中获取历史事件中相对于全局显示的特定触摸点的Y坐标。本接口支持的指向性输入事件仅包含触摸事件、鼠标事件。只能从指向性输入事件中获取位置信息，对于鼠标事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。从API version 20开始支持触摸事件，从API version 26.0.0开始支持鼠标事件。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示要返回的历史值，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回在指向性输入事件中，特定历史事件内特定接触点相对于全局显示的Y坐标，单位为px。如果发生任何参数错误，则返回0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryPressure()

```c
float OH_ArkUI_PointerEvent_GetHistoryPressure(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取特定历史事件中的触屏压力。本接口支持的指向性输入事件仅包含触摸事件，historyIndex必须小于OH\_ArkUI\_PointerEvent\_GetHistorySize返回的历史事件数量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示特定历史事件中多点触控数据列表的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。对于鼠标事件，该参数大于0时始终返回默认值0.0f。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件产生的触屏压力。取值范围为[0, 1]，压感大小与数值正相关。如果参数异常则返回默认值0.0f。在部分设备中，由于设备的硬件参数配置不同，可能会返回大于1的值。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryTiltX()

```c
float OH_ArkUI_PointerEvent_GetHistoryTiltX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取特定历史事件中的相对YZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向右倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件，且historyIndex必须小于OH\_ArkUI\_PointerEvent\_GetHistorySize返回的历史事件数量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示特定历史事件中多点触控数据列表的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。超出范围时返回参数异常结果。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中相对YZ平面的角度。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryTiltY()

```c
float OH_ArkUI_PointerEvent_GetHistoryTiltY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取特定历史事件中的相对XZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向下倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件，且historyIndex必须小于OH\_ArkUI\_PointerEvent\_GetHistorySize返回的历史事件数量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示特定历史事件中多点触控数据列表的序号，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(event, historyIndex) - 1]。超出范围时返回参数异常结果。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中相对XZ平面的角度。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaWidth()

```c
float OH_ArkUI_PointerEvent_GetHistoryTouchAreaWidth(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取特定历史事件中的触屏区域的宽度。仅适用于手指操作产生的触控事件，且historyIndex必须小于OH\_ArkUI\_PointerEvent\_GetHistorySize返回的历史事件数量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中触屏区域的宽度，单位为px。 |

### OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaHeight()

```c
float OH_ArkUI_PointerEvent_GetHistoryTouchAreaHeight(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取特定历史事件中的触屏区域的高度。仅适用于手指操作产生的触控事件，且historyIndex必须小于OH\_ArkUI\_PointerEvent\_GetHistorySize返回的历史事件数量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| uint32\_t pointerIndex | 表示多点触控数据列表中的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |
| uint32\_t historyIndex | 表示历史事件数据列表的序号，必须小于[OH\_ArkUI\_PointerEvent\_GetHistorySize](capi-ui-input-event-h.md#oh_arkui_pointerevent_gethistorysize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回当前指向性输入事件中触屏区域的高度，单位为px。 |

### OH\_ArkUI\_AxisEvent\_GetVerticalAxisValue()

```c
double OH_ArkUI_AxisEvent_GetVerticalAxisValue(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的垂直滚动轴的值。该值通常由鼠标滚轮或用户在触控板上双指竖向滑动产生。

当通过鼠标滚轮触发时：

1. 上报的数值单位为角度，表示单次滚动角度增量，非滚动总量。
2. 上报的数值已与用户配置的放大系数[OH\_ArkUI\_AxisEvent\_GetScrollStep](capi-ui-input-event-h.md#oh_arkui_axisevent_getscrollstep)叠加运算。
3. 数值的正负代表方向，向前滚动鼠标滚轮时上报数值为负数，向后滚动鼠标滚轮时上报数值为正数。

当通过触控板双指竖向滑动触发时：

1. 上报的数值单位为px，表示单次滚动增量，非滚动总量。
2. 上报的数值不受用户配置的放大系数[OH\_ArkUI\_AxisEvent\_GetScrollStep](capi-ui-input-event-h.md#oh_arkui_axisevent_getscrollstep)影响。
3. 数值的正负代表方向，双指从上往下滑动时上报数值为负数，双指从下往上滑动时上报数值为正数。
4. 方向会受系统设置中“自然滚动”配置的影响。

通常情况下，垂直滚动轴事件只能驱动竖向的滑动手势响应。但当鼠标指针下命中的可滑动手势的可响应方向与垂直滚动轴事件的方向一致时，垂直滚动轴事件可以驱动这些滑动手势得到响应，即使这些手势定义的滑动方向是横向的。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回当前轴事件的垂直滚动轴的值，如果参数异常则返回0.0。 |

### OH\_ArkUI\_AxisEvent\_GetHorizontalAxisValue()

```c
double OH_ArkUI_AxisEvent_GetHorizontalAxisValue(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的水平滚动轴的值，该值通过在触控板上双指横向滑动产生。

1. 上报的数值单位为px，表示单次滚动增量，非滚动总量。
2. 上报的数值不受用户配置的放大系数[OH\_ArkUI\_AxisEvent\_GetScrollStep](capi-ui-input-event-h.md#oh_arkui_axisevent_getscrollstep)影响。
3. 数值的正负代表方向，双指从左往右滑动时上报数值为负数，双指从右往左滑动时上报数值为正数。
4. 方向会受系统设置中“自然滚动”配置的影响。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回当前轴事件的水平滚动轴的值，如果参数异常则返回0.0。 |

### OH\_ArkUI\_AxisEvent\_GetPinchAxisScaleValue()

```c
double OH_ArkUI_AxisEvent_GetPinchAxisScaleValue(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的捏合轴缩放的值。该值由触控板双指缩放或捏合操作产生。系统识别到捏合操作时，将两指位置作为初始状态，scale值为1.0。在手指抬起前的本次捏合操作过程中，所上报的scale数值均将初始状态作为参考系，从初始状态往中心捏合，则上报的scale会从1.0逐步往0.0缩小；当从初始状态往外扩大双指距离时，会从1.0逐步变大。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回当前轴事件的捏合轴缩放的值，如果参数异常则返回0.0。 |

### OH\_ArkUI\_AxisEvent\_GetAxisAction()

```c
int32_t OH_ArkUI_AxisEvent_GetAxisAction(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的操作类型。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回当前轴事件的操作类型，取值可参考[anonymous7](capi-ui-input-event-h.md#anonymous7)。当输入非轴事件时，默认返回0。 |

### OH\_ArkUI\_AxisEvent\_HasAxis()

```c
int32_t OH_ArkUI_AxisEvent_HasAxis(const ArkUI_UIInputEvent* event, int32_t axis)
```

**描述：**

检测此轴事件是否包含指定的轴类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| int32\_t axis | 表示轴事件的轴类型[UI\_AXIS\_TYPE](capi-ui-input-event-h.md#anonymous8)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回此轴事件是否包含指定的轴类型。返回true表示包含指定的轴类型，返回false表示不包含指定的轴类型。 |

### OH\_ArkUI\_PointerEvent\_SetInterceptHitTestMode()

```c
int32_t OH_ArkUI_PointerEvent_SetInterceptHitTestMode(const ArkUI_UIInputEvent* event, HitTestMode mode)
```

**描述：**

配置触摸测试模式，用于在接收基础触摸事件时控制组件自身、子组件、兄弟组件和祖先组件是否参与触摸命中测试，例如在需要调整触摸事件分发范围的场景中使用。仅适用于接收基础事件的场景，如使用NODE\_ON\_TOUCH接收触摸事件场景。对于通过[OH\_ArkUI\_GestureEvent\_GetRawInputEvent](capi-native-gesture-h.md#oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI\_UIInputEvent对象，无法使用该接口。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| [HitTestMode](capi-ui-input-event-h.md#hittestmode) mode | 指定触摸测试模式。HTM\_DEFAULT适用于自身及子节点响应触摸测试且阻塞兄弟节点的场景；HTM\_BLOCK适用于仅自身响应并阻塞子节点、兄弟节点和祖先节点的场景；HTM\_TRANSPARENT适用于自身和子节点响应且不阻塞兄弟节点和祖先节点的场景；HTM\_NONE适用于自身不响应触摸测试且不影响其他节点的场景；HTM\_BLOCK\_HIERARCHY适用于自身和子节点响应并阻止低优先级兄弟节点及父节点参与触摸测试的场景；HTM\_BLOCK\_DESCENDANTS适用于自身及所有后代均不响应触摸测试且不影响祖先节点的场景。根据所需的节点响应范围和阻塞关系选择对应模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回触摸测试模式配置结果的状态代码。返回0表示配置成功，返回非0表示配置失败。 |

### OH\_ArkUI\_MouseEvent\_GetMouseButton()

```c
int32_t OH_ArkUI_MouseEvent_GetMouseButton(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标事件的按键类型的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回鼠标按键类型，取值由[anonymous5](capi-ui-input-event-h.md#anonymous5)枚举定义，但在非鼠标事件中调用时返回值为-1。 |

### OH\_ArkUI\_MouseEvent\_GetMouseAction()

```c
int32_t OH_ArkUI_MouseEvent_GetMouseAction(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标事件的鼠标动作类型的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回鼠标动作类型，取值由[anonymous4](capi-ui-input-event-h.md#anonymous4)枚举定义，但在非鼠标事件中调用时返回值为-1。 |

### OH\_ArkUI\_PointerEvent\_SetStopPropagation()

```c
int32_t OH_ArkUI_PointerEvent_SetStopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

**描述：**

设置是否阻止事件冒泡，适用于当前组件已处理基础触摸事件且不希望事件继续传递给父组件或其他祖先组件的场景。仅适用于接收基础事件的场景，如使用NODE\_ON\_TOUCH接收触摸事件场景，不适用于轴事件。对于通过[OH\_ArkUI\_GestureEvent\_GetRawInputEvent](capi-native-gesture-h.md#oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI\_UIInputEvent对象，无法使用该接口。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| bool stopPropagation | 表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。返回0表示设置成功，如果返回401，表示返回失败，可能的原因是参数异常，例如event是一个空指针，请检查event是否为空并传入有效的UI输入事件指针。 |

### OH\_ArkUI\_UIInputEvent\_GetDeviceId()

```c
int32_t OH_ArkUI_UIInputEvent_GetDeviceId(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前UI输入事件的设备ID。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 当前UI输入事件的设备ID。 |

### OH\_ArkUI\_UIInputEvent\_GetPressedKeys()

```c
int32_t OH_ArkUI_UIInputEvent_GetPressedKeys(const ArkUI_UIInputEvent* event, int32_t* pressedKeyCodes, int32_t* length)
```

**描述：**

获取所有按下的按键，当前只支持按键事件。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t\* pressedKeyCodes | 输出参数，指向由调用者分配的按键编码数组，用于接收所有按下按键的键值；数组容量由输入参数length指定，实际按键数量通过length输出。 |
| int32\_t\* length | 作为输入参数表示传入的pressedKeyCodes数组长度，作为输出参数表示实际按下按键的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 内存分配不足，请检查并增大pressedKeyCodes缓冲区容量。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，可能是事件指针、pressedKeyCodes或length无效；请检查参数并重试。 |

### OH\_ArkUI\_FocusAxisEvent\_GetAxisValue()

```c
double OH_ArkUI_FocusAxisEvent_GetAxisValue(const ArkUI_UIInputEvent* event, int32_t axis)
```

**描述：**

获取焦点轴事件的轴值。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t axis | 焦点轴事件的轴类型。需要读取游戏手柄横向、纵向或深度控制量时分别选择UI\_FOCUS\_AXIS\_EVENT\_ABS\_X、UI\_FOCUS\_AXIS\_EVENT\_ABS\_Y或UI\_FOCUS\_AXIS\_EVENT\_ABS\_Z；需要读取旋转控制量时选择UI\_FOCUS\_AXIS\_EVENT\_ABS\_RZ、UI\_FOCUS\_AXIS\_EVENT\_ABS\_RX或UI\_FOCUS\_AXIS\_EVENT\_ABS\_RY；需要读取油门、刹车、方向舵或方向盘控制量时分别选择UI\_FOCUS\_AXIS\_EVENT\_ABS\_GAS、UI\_FOCUS\_AXIS\_EVENT\_ABS\_BRAKE、UI\_FOCUS\_AXIS\_EVENT\_ABS\_RUDDER或UI\_FOCUS\_AXIS\_EVENT\_ABS\_WHEEL；需要读取方向帽控制量时选择UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT0X、UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT0Y、UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT1X、UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT1Y、UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT2X、UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT2Y、UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT3X或UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT3Y。根据要读取的游戏手柄控制轴选择对应枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 焦点轴事件的轴值，如果参数异常则返回0.0。 |

### OH\_ArkUI\_FocusAxisEvent\_SetStopPropagation()

```c
int32_t OH_ArkUI_FocusAxisEvent_SetStopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

**描述：**

设置是否阻止焦点轴事件冒泡，适用于组件已处理焦点轴事件后，不希望该事件继续传递给父组件或其他祖先组件的场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前UI输入事件的指针。 |
| bool stopPropagation | 表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常。 |

### OH\_ArkUI\_UIInputEvent\_GetModifierKeyStates()

```c
int32_t OH_ArkUI_UIInputEvent_GetModifierKeyStates(const ArkUI_UIInputEvent* event, uint64_t* keys)
```

**描述：**

获取UI输入事件的修饰键状态。该接口会通过keys传出当前事件发生时所有修饰键的状态，应用可将keys与[ArkUI\_ModifierKeyName](capi-ui-input-event-h.md#arkui_modifierkeyname)中定义的修饰键类型进行位运算，以获取处于按下状态的修饰键。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| uint64\_t\* keys | 返回当前处于按下状态的修饰键组合，应用可通过位运算进行判断。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，可能是事件指针或输出参数无效；请检查并传入有效参数。 |

### OH\_ArkUI\_AxisEvent\_SetPropagation()

```c
int32_t OH_ArkUI_AxisEvent_SetPropagation(const ArkUI_UIInputEvent* event, bool propagation)
```

**描述：**

设置是否启用轴事件冒泡。默认不会进行冒泡传递，仅发送给第一个可响应轴事件的控件。可在接收到轴事件时，主动启用冒泡传递，以便当前事件可以继续传递给响应链上的下一个可响应轴事件的祖先组件处理。不支持对从手势事件中获取到的轴事件进行设置。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 表示指向当前 UI 输入事件的指针。 |
| bool propagation | 表示是否激活事件冒泡。true表示激活事件冒泡，false表示不激活事件冒泡。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常。 |

### OH\_ArkUI\_AxisEvent\_GetScrollStep()

```c
int32_t OH_ArkUI_AxisEvent_GetScrollStep(const ArkUI_UIInputEvent* event)
```

**描述：**

获取滚动轴事件的滚动步长系数，适用于鼠标滚轮产生的轴事件。该值表示用户配置的滚动放大系数。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向 ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回鼠标滚轮轴滚动步长配置。在非鼠标事件返回默认值0。 |

### OH\_ArkUI\_UIInputEvent\_GetEventTargetWidth()

```c
float OH_ArkUI_UIInputEvent_GetEventTargetWidth(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的宽度。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向ArkUI\_UIInputEvent对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回事件命中的组件的宽度，单位为px；如果发生任何参数错误，则返回 0.0f。 |

### OH\_ArkUI\_UIInputEvent\_GetEventTargetHeight()

```c
float OH_ArkUI_UIInputEvent_GetEventTargetHeight(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的高度。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向ArkUI\_UIInputEvent对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回事件命中的组件的高度，单位为px；如果发生任何参数错误，则返回 0.0f。 |

### OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionX()

```c
float OH_ArkUI_UIInputEvent_GetEventTargetPositionX(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的X坐标。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向ArkUI\_UIInputEvent对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回事件命中的组件的X坐标，单位为px；如果发生任何参数错误，则返回 0.0f。 |

### OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionY()

```c
float OH_ArkUI_UIInputEvent_GetEventTargetPositionY(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的Y坐标。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向ArkUI\_UIInputEvent对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回事件命中的组件的Y坐标，单位为px；如果发生任何参数错误，则返回 0.0f。 |

### OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionX()

```c
float OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionX(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的全局X坐标。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向ArkUI\_UIInputEvent对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回事件命中的组件的全局X坐标，单位为px；如果发生任何参数错误，则返回 0.0f。 |

### OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionY()

```c
float OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionY(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的全局Y坐标。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | 指向ArkUI\_UIInputEvent对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回事件命中的组件的全局Y坐标，单位为px；如果发生任何参数错误，则返回 0.0f。 |

### OH\_ArkUI\_PointerEvent\_GetPressedTimeByIndex()

```c
int64_t OH_ArkUI_PointerEvent_GetPressedTimeByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

获取指定触点的按下时间。仅对触摸事件有效。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| uint32\_t pointerIndex | 指示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]。超出范围时返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回特定触摸点的按下时间，单位为ns；如果发生任何参数错误，则返回0。 |

### OH\_ArkUI\_MouseEvent\_GetRawDeltaX()

```c
float OH_ArkUI_MouseEvent_GetRawDeltaX(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回鼠标设备在二维平面X轴的移动增量，使用物理世界中鼠标移动的距离单位进行表示；如果发生任何参数错误，则返回0.0f。  **说明：** API版本26.0.0之前，返回值并非鼠标硬件的原始移动数据，而是原始数据缩小了X倍，X为系统的显示大小比例。API版本26.0.0开始，返回值为鼠标硬件的原始移动数据。 |

### OH\_ArkUI\_MouseEvent\_GetRawDeltaY()

```c
float OH_ArkUI_MouseEvent_GetRawDeltaY(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回鼠标设备在二维平面Y轴的移动增量，使用物理世界中鼠标移动的距离单位进行表示；如果发生任何参数错误，则返回0.0f。  **说明：** API版本26.0.0之前，返回值并非鼠标硬件的原始移动数据，而是原始数据缩小了Y倍，Y为系统的显示大小比例。API版本26.0.0开始，返回值为鼠标硬件的原始移动数据。 |

### OH\_ArkUI\_MouseEvent\_GetPressedButtons()

```c
int32_t OH_ArkUI_MouseEvent_GetPressedButtons(const ArkUI_UIInputEvent* event, int32_t* pressedButtons, int32_t* length)
```

**描述：**

从鼠标事件中获取按下的按键。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t\* pressedButtons | 指示按下按键的列表。需要先创建一个int数组，用来储存按下的按键，按键的值请参考[anonymous5](capi-ui-input-event-h.md#anonymous5)。 |
| int32\_t\* length | 作为输入参数表示传入的pressedButtons数组长度，作为输出参数表示实际按下按键的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果传入的缓冲区大小异常，则返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_UIInputEvent\_GetTargetDisplayId()

```c
int32_t OH_ArkUI_UIInputEvent_GetTargetDisplayId(const ArkUI_UIInputEvent* event)
```

**描述：**

获取发生UI输入事件的屏幕ID。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回屏幕ID；如果发生任何参数错误，则返回0。 |

### OH\_ArkUI\_HoverEvent\_IsHovered()

```c
bool OH_ArkUI_HoverEvent_IsHovered(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标是否悬浮在当前组件上。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果鼠标悬浮在当前组件上则返回true。  如果鼠标没有悬浮在当前组件上，返回false |

### OH\_ArkUI\_PointerEvent\_CreateClonedEvent()

```c
int32_t OH_ArkUI_PointerEvent_CreateClonedEvent(const ArkUI_UIInputEvent* event, ArkUI_UIInputEvent** clonedEvent)
```

**描述：**

基于原始事件指针创建克隆事件指针。仅对触摸事件有效。调用成功后，应在克隆事件使用完毕后调用OH\_ArkUI\_PointerEvent\_DestroyClonedEvent()销毁该克隆事件指针，避免资源未释放。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\*\* clonedEvent | 输出参数，由接口写入新创建的克隆ArkUI\_UIInputEvent对象指针；使用完毕后应调用OH\_ArkUI\_PointerEvent\_DestroyClonedEvent释放资源。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_DestroyClonedEvent()

```c
int32_t OH_ArkUI_PointerEvent_DestroyClonedEvent(const ArkUI_UIInputEvent* event)
```

**描述：**

销毁由OH\_ArkUI\_PointerEvent\_CreateClonedEvent()创建的克隆事件指针。克隆事件使用完毕后应调用该接口释放资源。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPosition()

```c
int32_t OH_ArkUI_PointerEvent_SetClonedEventLocalPosition(const ArkUI_UIInputEvent* event, float x, float y)
```

**描述：**

设置指向性克隆事件相对于当前组件左上角的X坐标和Y坐标。该接口应在调用OH\_ArkUI\_PointerEvent\_CreateClonedEvent()创建克隆事件后使用；同系列SetClonedEvent接口均仅适用于克隆事件。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 当前指向性输入事件相对于当前组件左上角的X坐标，单位为px。 |
| float y | 当前指向性输入事件相对于当前组件左上角的Y坐标，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPositionByIndex()

```c
int32_t OH_ArkUI_PointerEvent_SetClonedEventLocalPositionByIndex(const ArkUI_UIInputEvent* event, float x, float y, int32_t pointerIndex)
```

**描述：**

设置克隆指向性事件特定接触点相对于当前组件左上角的X坐标和Y坐标。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedevent)接口创建的ArkUI\_UIInputEvent克隆事件指针才能使用此接口。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 当前指向性输入事件相对于当前组件左上角的X坐标，单位为px。 |
| float y | 当前指向性输入事件相对于当前组件左上角的Y坐标，单位为px。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_SetClonedEventActionType()

```c
int32_t OH_ArkUI_PointerEvent_SetClonedEventActionType(const ArkUI_UIInputEvent* event, int32_t actionType)
```

**描述：**

设置当前带有指向性的克隆输入事件的动作类型。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedevent)接口创建的ArkUI\_UIInputEvent克隆事件指针才能使用此接口。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t actionType | ArkUI\_UIInputEvent克隆事件的动作类型。触摸事件根据按下、移动、抬起或取消场景选择UI\_TOUCH\_EVENT\_ACTION\_DOWN、UI\_TOUCH\_EVENT\_ACTION\_MOVE、UI\_TOUCH\_EVENT\_ACTION\_UP或UI\_TOUCH\_EVENT\_ACTION\_CANCEL；鼠标事件根据按下、松开、移动或取消场景选择UI\_MOUSE\_EVENT\_ACTION\_PRESS、UI\_MOUSE\_EVENT\_ACTION\_RELEASE、UI\_MOUSE\_EVENT\_ACTION\_MOVE或UI\_MOUSE\_EVENT\_ACTION\_CANCEL；轴事件根据开始、更新、结束或取消场景选择UI\_AXIS\_EVENT\_ACTION\_BEGIN、UI\_AXIS\_EVENT\_ACTION\_UPDATE、UI\_AXIS\_EVENT\_ACTION\_END或UI\_AXIS\_EVENT\_ACTION\_CANCEL。根据克隆事件的事件类型和动作阶段选择对应取值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_SetClonedEventChangedFingerId()

```c
int32_t OH_ArkUI_PointerEvent_SetClonedEventChangedFingerId(const ArkUI_UIInputEvent* event, int32_t fingerId)
```

**描述：**

设置当前带有指向性的克隆输入事件的触摸点ID。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedevent)接口创建的ArkUI\_UIInputEvent克隆事件指针才能使用此接口。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t fingerId | 触发当前事件指针的触摸点ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_SetClonedEventFingerIdByIndex()

```c
int32_t OH_ArkUI_PointerEvent_SetClonedEventFingerIdByIndex(const ArkUI_UIInputEvent* event, int32_t fingerId, int32_t pointerIndex)
```

**描述：**

设置带有指向性的克隆输入事件特定接触点的触摸点ID。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedevent)接口创建的ArkUI\_UIInputEvent克隆事件指针才能使用此接口。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t fingerId | 指向性的输入事件特定接触点的触摸点ID。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_PostClonedEvent()

```c
int32_t OH_ArkUI_PointerEvent_PostClonedEvent(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event)
```

**描述：**

转发克隆事件到特定节点。使用该接口前应先调用OH\_ArkUI\_PointerEvent\_CreateClonedEvent()创建克隆事件，并可按需调用OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPosition()等接口设置事件属性；克隆事件使用完毕后应调用OH\_ArkUI\_PointerEvent\_DestroyClonedEvent()销毁。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果组件状态异常，则返回[ARKUI\_ERROR\_CODE\_POST\_CLONED\_COMPONENT\_STATUS\_ABNORMAL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果未命中可响应事件的组件，则返回[ARKUI\_ERROR\_CODE\_POST\_CLONED\_NO\_COMPONENT\_HIT\_TO\_RESPOND\_TO\_THE\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent()

```c
ArkUI_ErrorCode OH_ArkUI_PointerEvent_CreateClonedPointerEvent(const ArkUI_UIInputEvent* event, ArkUI_UIInputEvent** clonedEvent)
```

**描述：**

创建指定事件的克隆事件。该接口适用于触摸事件、鼠标事件和轴事件。调用成功后，可使用OH\_ArkUI\_ClonedEvent\_SetXXX系列接口设置克隆事件属性，使用完毕后应调用OH\_ArkUI\_PointerEvent\_DestroyClonedPointerEvent()销毁该克隆事件，避免资源未释放。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\*\* clonedEvent | 输出参数，用于接收创建成功后的ArkUI\_UIInputEvent克隆事件指针；使用完毕后需调用OH\_ArkUI\_PointerEvent\_DestroyClonedPointerEvent()释放该事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_CreatePointerEvent()

```c
ArkUI_ErrorCode OH_ArkUI_PointerEvent_CreatePointerEvent(ArkUI_UIInputEvent** event, ArkUI_UIInputEvent_Type type)
```

**描述：**

创建新事件，不克隆现有事件。该接口适用于触摸事件、鼠标事件和轴事件。调用成功后，请使用OH\_ArkUI\_ClonedEvent\_SetXXX系列接口设置事件属性。事件使用完毕后，请调用OH\_ArkUI\_PointerEvent\_DestroyClonedPointerEvent()销毁事件，避免资源未释放。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\*\* event | 输出参数，用于接收新创建的ArkUI\_UIInputEvent对象；使用完毕后需调用OH\_ArkUI\_PointerEvent\_DestroyClonedPointerEvent()释放该事件。 |
| [ArkUI\_UIInputEvent\_Type](capi-ui-input-event-h.md#arkui_uiinputevent_type) type | ArkUI\_UIInputEvent的事件类型。创建触摸事件时选择ARKUI\_UIINPUTEVENT\_TYPE\_TOUCH，适用于模拟或处理触摸输入；创建轴事件时选择ARKUI\_UIINPUTEVENT\_TYPE\_AXIS，适用于模拟或处理鼠标滚轮、触控板滚动或捏合输入；创建鼠标事件时选择ARKUI\_UIINPUTEVENT\_TYPE\_MOUSE，适用于模拟或处理鼠标按键或移动输入；根据需要创建的输入设备事件类型选择对应取值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_DestroyClonedPointerEvent()

```c
ArkUI_ErrorCode OH_ArkUI_PointerEvent_DestroyClonedPointerEvent(const ArkUI_UIInputEvent* event)
```

**描述：**

销毁克隆事件指针。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，例如event无效或type不属于对应事件类型支持的动作类型，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)；请检查事件指针和动作类型参数。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetActionType()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetActionType(const ArkUI_UIInputEvent* event, int32_t type)
```

**描述：**

设置克隆事件的动作类型。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t type | 克隆事件的动作类型，包括触摸事件的[UI\_TOUCH\_EVENT\_ACTION](capi-ui-input-event-h.md#anonymous1)，鼠标事件的[UI\_MOUSE\_EVENT\_ACTION](capi-ui-input-event-h.md#anonymous4)，轴事件的[UI\_AXIS\_EVENT\_ACTION](capi-ui-input-event-h.md#anonymous7)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetSourceType()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetSourceType(const ArkUI_UIInputEvent* event, int32_t sourceType)
```

**描述：**

设置克隆事件的源类型。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t sourceType | 克隆事件的源类型。取值为0、1、2、4或5，其中0表示未知，1表示鼠标，2表示触屏，4表示键盘，5表示手柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetToolType()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetToolType(const ArkUI_UIInputEvent* event, int32_t toolType)
```

**描述：**

设置克隆事件的工具类型。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t toolType | 克隆事件的工具类型。手指操作选择UI\_INPUT\_EVENT\_TOOL\_TYPE\_FINGER，触控笔操作选择UI\_INPUT\_EVENT\_TOOL\_TYPE\_PEN，鼠标操作选择UI\_INPUT\_EVENT\_TOOL\_TYPE\_MOUSE，触控板操作选择UI\_INPUT\_EVENT\_TOOL\_TYPE\_TOUCHPAD，操纵杆操作选择UI\_INPUT\_EVENT\_TOOL\_TYPE\_JOYSTICK，无法确定工具类型时选择UI\_INPUT\_EVENT\_TOOL\_TYPE\_UNKNOWN。应根据实际产生事件的操作工具选择对应取值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetPressure()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetPressure(const ArkUI_UIInputEvent* event, float pressure)
```

**描述：**

设置克隆事件应用于触摸屏的压力。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float pressure | 应用于触摸屏的压力，通常取值范围为[0, 1]，包含0和1；部分设备可能支持大于1的值，具体范围以设备能力为准。传入不支持的值时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，例如event无效或pressure参数不符合要求，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)；请检查事件指针和压力参数。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，可能是传入了非触摸事件；请传入触摸事件后重试。 |

### OH\_ArkUI\_ClonedEvent\_SetPressureByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetPressureByIndex(const ArkUI_UIInputEvent* event, float pressure, int32_t pointerIndex)
```

**描述：**

设置克隆事件指定触摸点应用于触摸屏的压力。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float pressure | 应用于触摸屏的压力，通常取值范围为[0, 1]，包含0和1；部分设备可能支持大于1的值，具体范围以设备能力为准。传入不支持的值时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetEventTime()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetEventTime(const ArkUI_UIInputEvent* event, int64_t timestamp)
```

**描述：**

设置克隆UI输入事件发生的时间。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int64\_t timestamp | 克隆UI输入事件发生的时间，单位为ns。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetDeviceId()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetDeviceId(const ArkUI_UIInputEvent* event, int32_t deviceId)
```

**描述：**

设置触发克隆UI输入事件的设备ID。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t deviceId | 触发克隆UI输入事件的设备ID，可用[OH\_ArkUI\_UIInputEvent\_GetDeviceId](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getdeviceid)接口获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetTargetDisplayId()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetTargetDisplayId(const ArkUI_UIInputEvent* event, int32_t targetDisplayId)
```

**描述：**

设置克隆UI输入事件发生的屏幕ID。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t targetDisplayId | 克隆UI输入事件发生的屏幕ID，可用[OH\_ArkUI\_UIInputEvent\_GetTargetDisplayId](capi-ui-input-event-h.md#oh_arkui_uiinputevent_gettargetdisplayid)接口获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetChangedFingerId()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetChangedFingerId(const ArkUI_UIInputEvent* event, int32_t fingerId)
```

**描述：**

设置克隆指针事件的触摸点ID。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t fingerId | 触发事件的触摸点ID，可以通过[OH\_ArkUI\_PointerEvent\_GetPointerId](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpointerid)接口获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，例如event无效或pointerIndex超出有效范围，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)；请检查事件指针和触摸点索引。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，可能是传入了非触摸事件；请传入触摸事件后重试。 |

### OH\_ArkUI\_ClonedEvent\_SetFingerIdByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetFingerIdByIndex(const ArkUI_UIInputEvent* event, int32_t fingerId, int32_t pointerIndex)
```

**描述：**

设置克隆事件特定接触点的触摸点ID。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t fingerId | 特定接触点的触摸点ID，可以通过[OH\_ArkUI\_PointerEvent\_GetPointerId](capi-ui-input-event-h.md#oh_arkui_pointerevent_getpointerid)接口获取。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetChangedWindowPosition()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetChangedWindowPosition(const ArkUI_UIInputEvent* event, float x, float y)
```

**描述：**

设置克隆事件相对于当前窗口左上角的X坐标和Y坐标。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 事件相对于当前窗口左上角的X坐标，单位为px。 |
| float y | 事件相对于当前窗口左上角的Y坐标，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetWindowPositionByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetWindowPositionByIndex(const ArkUI_UIInputEvent* event, float x, float y, int32_t pointerIndex)
```

**描述：**

设置克隆事件特定接触点相对于当前窗口左上角的X坐标和Y坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 事件相对于当前窗口左上角的X坐标，单位为px。 |
| float y | 事件相对于当前窗口左上角的Y坐标，单位为px。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetChangedScreenPosition()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetChangedScreenPosition(const ArkUI_UIInputEvent* event, float x, float y)
```

**描述：**

设置克隆事件相对于当前屏幕左上角的X坐标和Y坐标。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 事件相对于当前屏幕左上角的X坐标，单位为px。 |
| float y | 事件相对于当前屏幕左上角的Y坐标，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetScreenPositionByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetScreenPositionByIndex(const ArkUI_UIInputEvent* event, float x, float y, int32_t pointerIndex)
```

**描述：**

设置克隆事件特定接触点相对于当前屏幕左上角的X坐标和Y坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 事件相对于当前屏幕左上角的X坐标，单位为px。 |
| float y | 事件相对于当前屏幕左上角的Y坐标，单位为px。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，例如event无效、pointerIndex超出有效范围或坐标参数不符合要求，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)；请检查事件指针、触摸点索引和坐标参数。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，可能是传入了非触摸事件；请传入触摸事件后重试。 |

### OH\_ArkUI\_ClonedEvent\_SetChangedGlobalDisplayPosition()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetChangedGlobalDisplayPosition(const ArkUI_UIInputEvent* event, float x, float y)
```

**描述：**

设置克隆事件在[全局坐标系](../harmonyos-guides/window-terminology.md#global-coordinate-system全局坐标系)的坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 事件相对于全局显示的X坐标，单位为px。 |
| float y | 事件相对于全局显示的Y坐标，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetGlobalDisplayPositionByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetGlobalDisplayPositionByIndex(const ArkUI_UIInputEvent* event, float x, float y, int32_t pointerIndex)
```

**描述：**

设置克隆事件在[全局坐标系](../harmonyos-guides/window-terminology.md#global-coordinate-system全局坐标系)的坐标。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float x | 事件相对于全局显示的X坐标，单位为px。 |
| float y | 事件相对于全局显示的Y坐标，单位为px。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetHandleId()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetHandleId(const ArkUI_UIInputEvent* event, int32_t eventHandleId)
```

**描述：**

设置事件处理会话的唯一句柄。该句柄必须用于对该事件的任何进一步操作。对于给定的手指，同一时间只有一个具有此句柄的事件处于活动状态。该接口适用于触摸事件、鼠标事件和轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t eventHandleId | 事件处理会话的唯一句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetTiltAngle()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetTiltAngle(const ArkUI_UIInputEvent* event, float tiltX, float tiltY)
```

**描述：**

设置克隆事件相对于YZ平面和XZ平面的倾斜角度。tiltX和tiltY的取值范围均为[-90, 90]，包含-90和90；其中tiltX正值表示向右倾斜，tiltY正值表示向下倾斜。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float tiltX | 克隆事件相对于YZ平面的倾斜角度，单位为deg。 |
| float tiltY | 克隆事件相对于XZ平面的倾斜角度，单位为deg。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetRollAngle()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetRollAngle(const ArkUI_UIInputEvent* event, float rollAngle)
```

**描述：**

设置克隆事件触控笔绕Z轴的旋转角度。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float rollAngle | 克隆事件触控笔绕Z轴的旋转角度，单位为deg。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetPressedKeys()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetPressedKeys(const ArkUI_UIInputEvent* event, int32_t* pressedKeyCodes, int32_t length)
```

**描述：**

设置克隆事件中所有按下的按键。该接口适用于按键事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t\* pressedKeyCodes | 所有按下按键的键值数组，键值取值为[ArkUI\_KeyCode](capi-native-key-event-h.md#arkui_keycode)。 |
| int32\_t length | 按下的按键数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetChangedTouchArea()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetChangedTouchArea(const ArkUI_UIInputEvent* event, float width, float height)
```

**描述：**

设置克隆事件的手指接触区域的宽度和高度，该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float width | 克隆事件的接触区域的宽度，单位为px。 |
| float height | 克隆事件的接触区域的高度，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetTouchAreaByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetTouchAreaByIndex(const ArkUI_UIInputEvent* event, float width, float height, int32_t pointerIndex)
```

**描述：**

设置克隆事件特定接触点的手指接触区域的宽度和高度，该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float width | 克隆事件的接触区域的宽度，单位为px。 |
| float height | 克隆事件的接触区域的高度，单位为px。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetChangedInteractionHand()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetChangedInteractionHand(const ArkUI_UIInputEvent* event, int32_t hand)
```

**描述：**

设置克隆事件是左手或右手触发。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t hand | 触摸点的交互手类型。系统识别为左手触摸时选择ARKUI\_EVENT\_HAND\_LEFT，系统识别为右手触摸时选择ARKUI\_EVENT\_HAND\_RIGHT，无法确定交互手时选择ARKUI\_EVENT\_HAND\_NONE；仅在需要模拟或修正克隆触摸事件的左右手属性时设置对应取值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetInteractionHandByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetInteractionHandByIndex(const ArkUI_UIInputEvent* event, int32_t hand, int32_t pointerIndex)
```

**描述：**

设置克隆事件特定接触点由左手或右手触发。该接口适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t hand | 触摸点是左手还是右手，[ARKUI\_EVENT\_HAND\_LEFT](capi-ui-input-event-h.md#arkui_interactionhand)为左手，[ARKUI\_EVENT\_HAND\_RIGHT](capi-ui-input-event-h.md#arkui_interactionhand)为右手。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetPressedTimeByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetPressedTimeByIndex(const ArkUI_UIInputEvent* event, int64_t pressedTime, int32_t pointerIndex)
```

**描述：**

设置克隆事件指定触摸点的按下时间。该接口仅适用于触摸事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int64\_t pressedTime | 指定触摸点的按下时间，单位为ns。 |
| int32\_t pointerIndex | 表示多点触控数据列表中目标触控点的索引，有效值范围为[0, OH\_ArkUI\_PointerEvent\_GetPointerCount(event) - 1]，不支持负索引；超出范围时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetPinchAxisScaleValue()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetPinchAxisScaleValue(const ArkUI_UIInputEvent* event, double pinchAxisScaleValue)
```

**描述：**

设置克隆事件的捏合轴缩放值。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| double pinchAxisScaleValue | 设置克隆轴事件的捏合轴缩放值，用于控制该事件对应的捏合缩放状态；取值范围为[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetHorizontalAxisScaleValue()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetHorizontalAxisScaleValue(const ArkUI_UIInputEvent* event, double horizontalAxisScaleValue)
```

**描述：**

设置克隆事件水平滚动轴的缩放值。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| double horizontalAxisScaleValue | 水平滚动轴的值，用于控制该事件的水平滚动行为，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetVerticalAxisScaleValue()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetVerticalAxisScaleValue(const ArkUI_UIInputEvent* event, double verticalAxisScaleValue)
```

**描述：**

设置克隆事件垂直滚动轴的缩放值。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| double verticalAxisScaleValue | 垂直滚动轴的值，用于控制该事件的垂直滚动行为。单位根据事件来源确定：触控板双指滑动为px，鼠标滚轮为角度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetScrollStep()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetScrollStep(const ArkUI_UIInputEvent* event, int32_t scrollStep)
```

**描述：**

设置克隆事件的滚动步长系数。该接口仅适用于轴事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t scrollStep | 克隆事件的滚动步长系数，用于控制鼠标滚轮轴事件的滚动放大效果，取值为[0, 65535]的整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetMouseButton()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetMouseButton(const ArkUI_UIInputEvent* event, int32_t button)
```

**描述：**

设置克隆事件的按钮类型值。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| int32\_t button | 克隆事件的鼠标按钮类型。模拟左键点击时选择UI\_MOUSE\_EVENT\_BUTTON\_LEFT，模拟右键菜单操作时选择UI\_MOUSE\_EVENT\_BUTTON\_RIGHT，模拟中键操作时选择UI\_MOUSE\_EVENT\_BUTTON\_MIDDLE，模拟鼠标后退或前进操作时分别选择UI\_MOUSE\_EVENT\_BUTTON\_BACK或UI\_MOUSE\_EVENT\_BUTTON\_FORWARD，无按钮操作时选择UI\_MOUSE\_EVENT\_BUTTON\_NONE；根据需要模拟的鼠标操作选择对应取值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetRawDeltaX()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetRawDeltaX(const ArkUI_UIInputEvent* event, float rawDeltaX)
```

**描述：**

设置鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float rawDeltaX | 鼠标位置相对于之前上报的鼠标事件中位置的X轴偏移量，单位为鼠标硬件上报的距离单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetRawDeltaY()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetRawDeltaY(const ArkUI_UIInputEvent* event, float rawDeltaY)
```

**描述：**

设置鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| float rawDeltaY | 鼠标位置相对于之前上报的鼠标事件中位置的Y轴偏移量，单位为鼠标硬件上报的距离单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ClonedEvent\_SetPressedButtons()

```c
ArkUI_ErrorCode OH_ArkUI_ClonedEvent_SetPressedButtons(const ArkUI_UIInputEvent* event, const int32_t* pressedButtons, int32_t length)
```

**描述：**

设置克隆事件的按下的按键。该接口仅适用于鼠标事件。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| const int32\_t\* pressedButtons | 按下的按键数组，按键的值请参考[anonymous5](capi-ui-input-event-h.md#anonymous5) |
| int32\_t length | 按下的按键数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果事件类型不支持，则返回[ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_PointerEvent\_PostClonedEventWithStrategy()

```c
ArkUI_ErrorCode OH_ArkUI_PointerEvent_PostClonedEventWithStrategy(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event, ArkUI_CompetitionStrategy strategy)
```

**描述：**

使用指定的竞争策略将克隆事件发送到特定节点，适用于向目标节点注入克隆事件并需要控制注入事件与目标节点已有手势之间是否竞争的场景。只有通过[OH\_ArkUI\_PointerEvent\_CreateClonedPointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createclonedpointerevent)和[OH\_ArkUI\_PointerEvent\_CreatePointerEvent](capi-ui-input-event-h.md#oh_arkui_pointerevent_createpointerevent)接口创建的ArkUI\_UIInputEvent对象才能使用此接口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| [ArkUI\_CompetitionStrategy](capi-ui-input-event-h.md#arkui_competitionstrategy) strategy | 竞争策略。注入事件需要与目标节点已有手势独立并行处理时选择ARKUI\_COMPETITION\_STRATEGY\_DEFAULT；需要让注入方和被注入方手势互相竞争且只处理其中一方时选择ARKUI\_COMPETITION\_STRATEGY\_COMPETITION；根据是否需要手势竞争选择对应策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，例如node、event或strategy无效，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)；请检查并传入有效节点、事件指针和竞争策略。  如果输入的事件指针不是克隆事件指针，则返回[ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果组件状态异常，则返回[ARKUI\_ERROR\_CODE\_POST\_CLONED\_COMPONENT\_STATUS\_ABNORMAL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果未命中可响应事件的组件，则返回[ARKUI\_ERROR\_CODE\_POST\_CLONED\_NO\_COMPONENT\_HIT\_TO\_RESPOND\_TO\_THE\_EVENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_UIInputEvent\_GetLatestStatus()

```c
ArkUI_ErrorCode OH_ArkUI_UIInputEvent_GetLatestStatus()
```

**描述：**

调用该方法获取最近一次UIInput相关方法的执行情况。仅在调用UIInput相关方法后需要确认该次调用是否执行异常时使用。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回最近一次调用UIInput方法产生的结果代码。 |

### OH\_ArkUI\_UIInputEvent\_GetCoastingAxisEvent()

```c
ArkUI_CoastingAxisEvent* OH_ArkUI_UIInputEvent_GetCoastingAxisEvent(ArkUI_UIInputEvent* event)
```

**描述：**

请在从[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象获取[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)对象后调用此方法，以获取惯性滚动轴事件。仅当用户在触控板上使用双指执行满足系统惯性滚动判定条件的抛滑操作，且指针位置下存在注册了[NODE\_ON\_COASTING\_AXIS\_EVENT](capi-native-node-h.md#arkui_nodeeventtype)事件的组件时，才能获取有效事件。

惯性滚动轴事件仅在双指抛滑并离开触控板时触发，因此仅支持触控板。惯性滚动轴事件会在手指离开触控板后，根据抛滑速度产生轴值逐渐衰减的事件。由于刷新频率和性能的影响，当前事件轴值可能高于或低于上一个事件值。在惯性滚动轴事件期间，以下四种行为会中断事件，并立即收到[ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_END](capi-ui-input-event-h.md#arkui_coastingaxiseventphase)。

1. 手指触摸触控板。
2. 滚动鼠标滚轮。
3. 手指或鼠标点击注册了惯性滚动轴事件的节点。需要注意的是，点击未注册此事件的节点不会中断当前惯性滚动轴事件。例如，A节点注册了惯性滚动轴事件，当事件发生时，让B节点滚动，但点击B节点不会中断此事件。点击事件的中断行为受[OH\_ArkUI\_PointerEvent\_SetInterceptHitTestMode](capi-ui-input-event-h.md#oh_arkui_pointerevent_setintercepthittestmode)的影响。此外，如果用户点击区域存在已收集的可响应惯性滚动轴事件的节点，本次惯性滚动轴事件会被强制终止。
4. 应用休眠（例如最小化、锁屏）。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md)\* | 返回指向惯性滚动轴事件的指针，如果未发生任何惯性滚动轴事件或发生任何参数错误，则返回空指针。 |

### OH\_ArkUI\_CoastingAxisEvent\_GetEventTime()

```c
int64_t OH_ArkUI_CoastingAxisEvent_GetEventTime(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件发生的时间。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md)\* event | ArkUI\_CoastingAxisEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回惯性滚动轴事件发生的时间，单位为ns；如果发生任何参数错误，则返回0。 |

### OH\_ArkUI\_CoastingAxisEvent\_GetPhase()

```c
ArkUI_CoastingAxisEventPhase OH_ArkUI_CoastingAxisEvent_GetPhase(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件发生时的滚动阶段。当返回[ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_END](capi-ui-input-event-h.md#arkui_coastingaxiseventphase)时，应立即停止惯性滚动效果。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md)\* event | ArkUI\_CoastingAxisEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CoastingAxisEventPhase](capi-ui-input-event-h.md#arkui_coastingaxiseventphase) | 返回事件阶段，参见[ArkUI\_CoastingAxisEventPhase](capi-ui-input-event-h.md#arkui_coastingaxiseventphase)。  如果发生任何参数错误则返回ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_NONE。 |

### OH\_ArkUI\_CoastingAxisEvent\_GetDeltaY()

```c
float OH_ArkUI_CoastingAxisEvent_GetDeltaY(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件垂直方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从上往下滑动时为负数，双指从下往上滑动时为正数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md)\* event | ArkUI\_CoastingAxisEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回Y轴增量值，以px为单位；如果发生任何参数错误则返回0.0f。 |

### OH\_ArkUI\_CoastingAxisEvent\_GetDeltaX()

```c
float OH_ArkUI_CoastingAxisEvent_GetDeltaX(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件水平方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从左往右滑动时为负数，双指从右往左滑动时为正数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md)\* event | ArkUI\_CoastingAxisEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回X轴增量值，以px为单位；如果发生任何参数错误则返回0.0f。 |

### OH\_ArkUI\_CoastingAxisEvent\_SetPropagation()

```c
int32_t OH_ArkUI_CoastingAxisEvent_SetPropagation(ArkUI_CoastingAxisEvent* event, bool propagation)
```

**描述：**

设置惯性滚动轴事件是否启用冒泡，默认禁止冒泡；适用于当前组件处理惯性滚动轴事件后，还需要将事件继续传递给祖先组件协同处理滚动效果的场景。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md)\* event | ArkUI\_CoastingAxisEvent事件指针。 |
| bool propagation | 是否启用事件冒泡。true表示启用，false表示禁用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_TouchTestInfo\_GetTouchTestInfoList()

```c
ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_GetTouchTestInfoList(ArkUI_TouchTestInfo* info,
    ArkUI_TouchTestInfoItemArray* array, int32_t* size);
```

**描述：**

获取触摸测试信息中的触摸测试信息项数组。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md)\* info | 指向触摸测试信息的指针。 |
| [ArkUI\_TouchTestInfoItemArray](capi-arkui-nativemodule-arkui-touchtestinfoitemhandlearray.md)\* array | 输出参数，指向用于接收触摸测试信息项数组的指针，数组元素为触摸测试信息项，数组大小通过size参数返回。 |
| int32\_t\* size | 输出参数，表示array中返回的触摸测试信息项数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI\_ErrorCode | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetX()

```c
float OH_ArkUI_TouchTestInfoItem_GetX(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于子组件左上角的X坐标，单位为px。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 相对于子组件左上角的X坐标，单位为px。若参数错误，返回0.0f。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetY()

```c
float OH_ArkUI_TouchTestInfoItem_GetY(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于子组件左上角的Y坐标，单位为px。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 相对于子组件左上角的Y坐标，单位为px。若参数错误，返回0.0f。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetWindowX()

```c
float OH_ArkUI_TouchTestInfoItem_GetWindowX(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于当前应用窗口左上角的X坐标，单位为px。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 相对于当前应用窗口左上角的X坐标，单位为px。若参数错误，返回0.0f。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetWindowY()

```c
float OH_ArkUI_TouchTestInfoItem_GetWindowY(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于当前应用窗口左上角的Y坐标，单位为px。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 相对于当前应用窗口左上角的Y坐标，单位为px。若参数错误，返回0.0f。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetXRelativeToParent()

```c
float OH_ArkUI_TouchTestInfoItem_GetXRelativeToParent(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于父组件左上角的X坐标，单位为px。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 相对于父组件左上角的X坐标，单位为px。若参数错误，返回0.0f。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetYRelativeToParent()

```c
float OH_ArkUI_TouchTestInfoItem_GetYRelativeToParent(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于父组件左上角的Y坐标，单位为px。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 相对于父组件左上角的Y坐标，单位为px。若参数错误，返回0.0f。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetChildRect()

```c
ArkUI_ErrorCode OH_ArkUI_TouchTestInfoItem_GetChildRect(const ArkUI_TouchTestInfoItem* info, ArkUI_Rect* childRect);
```

**描述：**

从触摸测试信息项中获取子组件的边界矩形信息。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |
| [ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md)\* childRect | 指向子组件边界矩形的指针，用于存储获取到的边界矩形信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI\_ErrorCode | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_TouchTestInfoItem\_GetChildId()

```c
ArkUI_ErrorCode OH_ArkUI_TouchTestInfoItem_GetChildId(const ArkUI_TouchTestInfoItem* info, char* buffer,
    int32_t bufferSize);
```

**描述：**

从触摸测试信息项中获取子组件的ID。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchTestInfoItem](capi-arkui-nativemodule-arkui-touchtestinfoitem.md)\* info | 指向触摸测试信息项的指针。 |
| char\* buffer | 调用者提供的缓冲区，用于接收获取到的子组件ID字符串。 |
| int32\_t bufferSize | 缓冲区的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI\_ErrorCode | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果缓冲区空间不足，则返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_TouchTestInfo\_SetTouchResultStrategy()

```c
ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_SetTouchResultStrategy(ArkUI_TouchTestInfo* info, ArkUI_TouchTestStrategy strategy);
```

**描述：**

设置触摸测试策略，即组件及其子组件在命中测试过程中的行为方式，适用于自定义触摸命中结果、将触摸事件分发给指定子组件或控制兄弟节点是否继续参与命中测试的场景。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md)\* info | 指向触摸测试信息的指针。 |
| [ArkUI\_TouchTestStrategy](capi-ui-input-event-h.md#arkui_touchteststrategy) strategy | 触摸测试策略。无需自定义分发、由系统按当前节点命中状态分发事件时选择ARKUI\_TOUCH\_TEST\_STRATEGY\_DEFAULT；需要将事件指定分发给某个子节点且允许系统决定其他兄弟节点是否分发时选择ARKUI\_TOUCH\_TEST\_STRATEGY\_FORWARD\_COMPETITION；需要将事件指定分发给某个子节点并禁止分发给其他兄弟节点时选择ARKUI\_TOUCH\_TEST\_STRATEGY\_FORWARD；根据是否需要自定义分发及是否允许兄弟节点继续参与选择对应策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI\_ErrorCode | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_TouchTestInfo\_SetTouchResultId()

```c
ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_SetTouchResultId(ArkUI_TouchTestInfo* info, const char* id);
```

**描述：**

设置命中测试过程中需要作用的子组件ID，适用于自定义触摸测试结果并希望将触摸事件分发到指定子组件的场景。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md)\* info | 指向触摸测试信息的指针。 |
| const char\* id | 子组件的ID，指定命中测试中需要作用的目标子组件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI\_ErrorCode | 返回结果代码。  如果操作成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果入参错误，则返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_DigitalCrownEvent\_GetEventTime()

```c
int64_t OH_ArkUI_DigitalCrownEvent_GetEventTime(const ArkUI_UIInputEvent* event)
```

**描述：**

获取表冠事件发生的时间。单位为ns。仅适用于入参event里存储的是表冠事件对象的场景。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent\*](capi-arkui-eventmodule-arkui-uiinputevent.md) event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回UI输入事件发生的时间，如果参数有误，则返回**0**。 |

### OH\_ArkUI\_DigitalCrownEvent\_GetAngularVelocity()

```c
double OH_ArkUI_DigitalCrownEvent_GetAngularVelocity(const ArkUI_UIInputEvent* event)
```

**描述：**

获取表冠事件发生的角速度。单位为°/s。仅适用于入参event里存储的是表冠事件对象的场景。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent\*](capi-arkui-eventmodule-arkui-uiinputevent.md) event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回UI输入事件发生的角速度，如果参数有误，则返回**0.0**。 |

### OH\_ArkUI\_DigitalCrownEvent\_GetDegree()

```c
double OH_ArkUI_DigitalCrownEvent_GetDegree(const ArkUI_UIInputEvent* event)
```

**描述：**

获取表冠事件发生的旋转角度。单位为°。仅适用于入参event里存储的是表冠事件对象的场景。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent\*](capi-arkui-eventmodule-arkui-uiinputevent.md) event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回UI输入事件发生的旋转角度，如果参数有误，则返回**0.0**。 |

### OH\_ArkUI\_DigitalCrownEvent\_GetAction()

```c
ArkUI_CrownEvent_Action OH_ArkUI_DigitalCrownEvent_GetAction(const ArkUI_UIInputEvent* event)
```

**描述：**

获取表冠事件发生的阶段。仅适用于入参event里存储的是表冠事件对象的场景。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent\*](capi-arkui-eventmodule-arkui-uiinputevent.md) event | 表示指向当前UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CrownEvent\_Action](capi-ui-input-event-h.md#arkui_crownevent_action) | 返回UI输入事件发生时旋转表冠的行为。如果入参错误，则返回**[ARKUI\_CROWNEVENT\_ACTION\_UNKNOWN](capi-ui-input-event-h.md#arkui_crownevent_action)**。 |

### OH\_ArkUI\_DigitalCrownEvent\_SetStopPropagation()

```c
ArkUI_ErrorCode OH_ArkUI_DigitalCrownEvent_SetStopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

**描述：**

设置是否阻止事件冒泡，适用于当前组件已处理表冠事件且不希望该事件继续传递给父组件或其他祖先组件的场景。仅适用于入参event里存储的是表冠事件对象的场景。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_UIInputEvent\*](capi-arkui-eventmodule-arkui-uiinputevent.md) event | 表示指向当前UI输入事件的指针。 |
| bool stopPropagation | 表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常，可能是事件指针、pressedKeyCodes或length无效；请检查参数并重试。 |
