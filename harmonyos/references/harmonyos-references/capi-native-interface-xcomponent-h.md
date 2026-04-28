---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h
title: native_interface_xcomponent.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_interface_xcomponent.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:49+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:70af5691f0d9443e8c0605e12f037d6eb0c64b8ec5dfeb818e8cc0814a76fe00
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于访问Native XComponent的API。

**引用文件：** <ace/xcomponent/native\_interface\_xcomponent.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 8

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**相关示例：** [NativeXComponentSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeXComponentSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeXComponent\_HistoricalPoint](ive-xcomponent-oh-nativexcomponent-historicalpoint.md) | OH\_NativeXComponent\_HistoricalPoint | 历史接触点。 |
| [OH\_NativeXComponent\_TouchPoint](t-native-xcomponent-oh-nativexcomponent-touchpoint.md) | OH\_NativeXComponent\_TouchPoint | 触摸事件中触摸点的信息。 |
| [OH\_NativeXComponent\_TouchEvent](t-native-xcomponent-oh-nativexcomponent-touchevent.md) | OH\_NativeXComponent\_TouchEvent | 触摸事件。 |
| [OH\_NativeXComponent\_MouseEvent](t-native-xcomponent-oh-nativexcomponent-mouseevent.md) | OH\_NativeXComponent\_MouseEvent | 鼠标事件。 |
| [OH\_NativeXComponent\_Callback](ent-native-xcomponent-oh-nativexcomponent-callback.md) | OH\_NativeXComponent\_Callback | 注册Surface生命周期和触摸事件回调。 |
| [OH\_NativeXComponent\_MouseEvent\_Callback](xcomponent-oh-nativexcomponent-mouseevent-callback.md) | OH\_NativeXComponent\_MouseEvent\_Callback | 注册鼠标事件的回调。 |
| [OH\_NativeXComponent\_ExpectedRateRange](e-xcomponent-oh-nativexcomponent-expectedraterange.md) | OH\_NativeXComponent\_ExpectedRateRange | 定义期望帧率范围。 |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md) | OH\_NativeXComponent | 提供封装的OH\_NativeXComponent实例。 |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md) | OH\_NativeXComponent\_KeyEvent | 提供封装按键事件信息的OH\_NativeXComponent\_KeyEvent实例。 |
| [OH\_NativeXComponent\_ExtraMouseEventInfo](xcomponent-oh-nativexcomponent-extramouseeventinfo.md) | OH\_NativeXComponent\_ExtraMouseEventInfo | 提供封装的扩展的鼠标事件信息实例。 |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md) | OH\_ArkUI\_SurfaceHolder | 提供封装的OH\_ArkUI\_SurfaceHolder实例。 |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md) | OH\_ArkUI\_SurfaceCallback | 定义Surface生命周期回调函数。 |
| [NativeWindow](oh-nativexcomponent-native-xcomponent-nativewindow.md) | OHNativeWindow | 提供封装的NativeWindow实例。 |
| [ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md) | ArkUI\_XComponentSurfaceConfig | 定义XComponent组件持有的Surface选项，用于设置XComponent组件持有的Surface在渲染时是否被视为不透明。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [anonymous](capi-native-interface-xcomponent-h.md#anonymous) | - | 枚举API访问状态。 |
| [ArkUI\_XComponent\_ImageAnalyzerState](capi-native-interface-xcomponent-h.md#arkui_xcomponent_imageanalyzerstate) | ArkUI\_XComponent\_ImageAnalyzerState | XComponent图像AI分析状态码. |
| [OH\_NativeXComponent\_TouchEventType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_toucheventtype) | OH\_NativeXComponent\_TouchEventType | 触摸事件类型。 |
| [OH\_NativeXComponent\_TouchPointToolType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_touchpointtooltype) | OH\_NativeXComponent\_TouchPointToolType | 触摸点工具类型。 |
| [OH\_NativeXComponent\_EventSourceType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_eventsourcetype) | OH\_NativeXComponent\_EventSourceType | 触摸事件源类型。 |
| [OH\_NativeXComponent\_MouseEventAction](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventaction) | OH\_NativeXComponent\_MouseEventAction | 鼠标事件动作。 |
| [OH\_NativeXComponent\_MouseEventButton](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventbutton) | OH\_NativeXComponent\_MouseEventButton | 鼠标事件按键。 |
| [OH\_NativeXComponent\_TouchEvent\_SourceTool](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_touchevent_sourcetool) | OH\_NativeXComponent\_TouchEvent\_SourceTool | 表示触摸事件的源工具类型。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_NATIVE\_XCOMPONENT\_OBJ ("\_\_NATIVE\_XCOMPONENT\_OBJ\_\_") | 代表Native XComponent实例。 |
| OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER 10 | 触摸事件中的可识别的触摸点个数最大值。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_NativeXComponent\_GetXComponentId(OH\_NativeXComponent\* component, char\* id, uint64\_t\* size)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getxcomponentid) | 获取ArkUI XComponent的id。 |
| [int32\_t OH\_NativeXComponent\_GetXComponentSize(OH\_NativeXComponent\* component, const void\* window, uint64\_t\* width, uint64\_t\* height)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getxcomponentsize) | 获取ArkUI XComponent持有的Surface的大小。 |
| [int32\_t OH\_NativeXComponent\_GetXComponentOffset(OH\_NativeXComponent\* component, const void\* window, double\* x, double\* y)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getxcomponentoffset) | 获取ArkUI XComponent持有的Surface相对其父组件左顶点的偏移量。 |
| [int32\_t OH\_NativeXComponent\_GetTouchEvent(OH\_NativeXComponent\* component, const void\* window, OH\_NativeXComponent\_TouchEvent\* touchEvent)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchevent) | 获取ArkUI XComponent调度的触摸事件。 |
| [int32\_t OH\_NativeXComponent\_GetTouchPointToolType(OH\_NativeXComponent\* component, uint32\_t pointIndex, OH\_NativeXComponent\_TouchPointToolType\* toolType)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchpointtooltype) | 获取ArkUI XComponent触摸点工具类型。 |
| [int32\_t OH\_NativeXComponent\_GetTouchPointTiltX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* tiltX)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchpointtiltx) | 获取ArkUI XComponent触摸点倾斜与X轴角度。 |
| [int32\_t OH\_NativeXComponent\_GetTouchPointTiltY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* tiltY)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchpointtilty) | 获取ArkUI XComponent触摸点倾斜与Y轴角度。 |
| [int32\_t OH\_NativeXComponent\_GetTouchPointWindowX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* windowX)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchpointwindowx) | 获取ArkUI XComponent触摸点相对于应用窗口左上角的X坐标。 |
| [int32\_t OH\_NativeXComponent\_GetTouchPointWindowY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* windowY)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchpointwindowy) | 获取ArkUI XComponent触摸点相对于应用窗口左上角的Y坐标。 |
| [int32\_t OH\_NativeXComponent\_GetTouchPointDisplayX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* displayX)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchpointdisplayx) | 获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的X坐标。 |
| [int32\_t OH\_NativeXComponent\_GetTouchPointDisplayY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* displayY)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettouchpointdisplayy) | 获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的Y坐标。 |
| [int32\_t OH\_NativeXComponent\_GetHistoricalPoints(OH\_NativeXComponent\* component, const void\* window, int32\_t\* size, OH\_NativeXComponent\_HistoricalPoint\*\* historicalPoints)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gethistoricalpoints) | 获取当前XComponent触摸事件的历史点信息。由于部分输入设备上报触点的频率非常高（最高可达每1 ms上报一次），而对输入事件的响应通常是为了使UI界面发生变化以响应用户操作，如果将触摸事件按照上报触点的频率如此高频率上报给应用，大多会造成冗余，因此触摸事件在一帧内只会上报一次给应用。在当前帧内上报的触点均作为历史点保存，如果应用需要直接处理这些数据，可调用该接口获取历史点信息。 |
| [int32\_t OH\_NativeXComponent\_GetMouseEvent(OH\_NativeXComponent\* component, const void\* window, OH\_NativeXComponent\_MouseEvent\* mouseEvent)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getmouseevent) | 获取ArkUI XComponent调度的鼠标事件。 |
| [int32\_t OH\_NativeXComponent\_RegisterCallback(OH\_NativeXComponent\* component, OH\_NativeXComponent\_Callback\* callback)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registercallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册回调。 |
| [int32\_t OH\_NativeXComponent\_RegisterMouseEventCallback(OH\_NativeXComponent\* component, OH\_NativeXComponent\_MouseEvent\_Callback\* callback)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registermouseeventcallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册鼠标事件回调。 |
| [int32\_t OH\_NativeXComponent\_GetExtraMouseEventInfo(OH\_NativeXComponent\* component, OH\_NativeXComponent\_ExtraMouseEventInfo\*\* extraMouseEventInfo)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getextramouseeventinfo) | 从此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例中获取扩展的鼠标事件信息。 |
| [int32\_t OH\_NativeXComponent\_GetMouseEventModifierKeyStates (OH\_NativeXComponent\_ExtraMouseEventInfo\* extraMouseEventInfo, uint64\_t\* keys)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getmouseeventmodifierkeystates) | 从[OH\_NativeXComponent\_ExtraMouseEventInfo](xcomponent-oh-nativexcomponent-extramouseeventinfo.md)实例中获取功能键按压状态信息。 |
| [int32\_t OH\_NativeXComponent\_RegisterFocusEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registerfocuseventcallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册获焦事件回调。 |
| [int32\_t OH\_NativeXComponent\_RegisterKeyEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registerkeyeventcallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册按键事件回调。 |
| [int32\_t OH\_NativeXComponent\_RegisterBlurEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registerblureventcallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册失焦事件回调。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEvent(OH\_NativeXComponent\* component, OH\_NativeXComponent\_KeyEvent\*\* keyEvent)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyevent) | 获取ArkUI XComponent调度的按键事件。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventAction(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_KeyAction\* action)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventaction) | 获取传入按键事件的动作。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventCode(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_KeyCode\* code)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventcode) | 获取传入按键事件的按键码。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventSourceType(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_EventSourceType\* sourceType)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventsourcetype) | 获取传入按键事件的事件源类型。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventDeviceId(OH\_NativeXComponent\_KeyEvent\* keyEvent, int64\_t\* deviceId)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventdeviceid) | 获取传入按键事件的设备id。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventTimestamp(OH\_NativeXComponent\_KeyEvent\* keyEvent, int64\_t\* timestamp)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventtimestamp) | 获取传入按键事件的时间戳。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventModifierKeyStates(OH\_NativeXComponent\_KeyEvent\* keyEvent, uint64\_t\* keys)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventmodifierkeystates) | 从按键事件中获取功能键按压状态信息。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventNumLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isNumLockOn)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventnumlockstate) | 从按键事件中获取NumLock（小键盘锁定）键的状态信息。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventCapsLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isCapsLockOn)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventcapslockstate) | 从按键事件中获取CapsLock（大写锁定）键的状态信息。 |
| [int32\_t OH\_NativeXComponent\_GetKeyEventScrollLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isScrollLockOn)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getkeyeventscrolllockstate) | 从按键事件中获取ScrollLock（滚动锁定）键的状态信息。 |
| [int32\_t OH\_NativeXComponent\_SetExpectedFrameRateRange(OH\_NativeXComponent\* component, OH\_NativeXComponent\_ExpectedRateRange\* range)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_setexpectedframeraterange) | 设置期望帧率范围。 |
| [int32\_t OH\_NativeXComponent\_RegisterOnFrameCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, uint64\_t timestamp, uint64\_t targetTimestamp))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registeronframecallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册显示更新回调，并使能每帧回调此函数。 |
| [int32\_t OH\_NativeXComponent\_UnregisterOnFrameCallback(OH\_NativeXComponent\* component)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_unregisteronframecallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例取消注册回调函数，并关闭每帧回调此函数。 |
| [int32\_t OH\_NativeXComponent\_AttachNativeRootNode(OH\_NativeXComponent\* component, ArkUI\_NodeHandle root)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_attachnativerootnode) | 将通过ArkUI的Native接口创建出来的UI组件挂载到当前XComponent上。 |
| [int32\_t OH\_NativeXComponent\_DetachNativeRootNode(OH\_NativeXComponent\* component, ArkUI\_NodeHandle root)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_detachnativerootnode) | 将ArkUI的Native组件从当前XComponent上卸载。 |
| [int32\_t OH\_NativeXComponent\_RegisterUIInputEventCallback(OH\_NativeXComponent \*component, void (\*callback)(OH\_NativeXComponent \*component, ArkUI\_UIInputEvent \*event,ArkUI\_UIInputEvent\_Type type),ArkUI\_UIInputEvent\_Type type)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registeruiinputeventcallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册UI输入事件回调，并使能收到UI输入事件时回调此函数。当前仅支持轴事件。 |
| [int32\_t OH\_NativeXComponent\_RegisterOnTouchInterceptCallback(OH\_NativeXComponent\* component, HitTestMode (\*callback)(OH\_NativeXComponent\* component, ArkUI\_UIInputEvent\* event))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registerontouchinterceptcallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册自定义事件拦截回调，并使能在做触摸测试时回调此函数。通过该回调获取到的事件对象不支持UIInput相关信息操作接口，建议切换为通过注册native node上的[NODE\_ON\_TOUCH\_INTERCEPT](capi-native-node-h.md#arkui_nodeeventtype)通用事件来支持。 |
| [int32\_t OH\_NativeXComponent\_SetNeedSoftKeyboard(OH\_NativeXComponent\* component, bool needSoftKeyboard)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_setneedsoftkeyboard) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例设置是否需要软键盘。 |
| [int32\_t OH\_NativeXComponent\_RegisterSurfaceShowCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registersurfaceshowcallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。 |
| [int32\_t OH\_NativeXComponent\_RegisterSurfaceHideCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registersurfacehidecallback) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。 |
| [int32\_t OH\_NativeXComponent\_GetTouchEventSourceType(OH\_NativeXComponent\* component, int32\_t pointId, OH\_NativeXComponent\_EventSourceType\* sourceType)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_gettoucheventsourcetype) | 获取ArkUI XComponent触摸事件的输入设备类型。 |
| [OH\_NativeXComponent\* OH\_NativeXComponent\_GetNativeXComponent(ArkUI\_NodeHandle node)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getnativexcomponent) | 基于Native接口创建的组件实例获取[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)类型的指针。 |
| [int32\_t OH\_NativeXComponent\_GetNativeAccessibilityProvider(OH\_NativeXComponent\* component, ArkUI\_AccessibilityProvider\*\* handle)](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getnativeaccessibilityprovider) | 获取ArkUI XComponent无障碍接入句柄指针。 |
| [int32\_t OH\_NativeXComponent\_RegisterKeyEventCallbackWithResult(OH\_NativeXComponent\* component, bool (\*callback)(OH\_NativeXComponent\* component, void\* window))](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registerkeyeventcallbackwithresult) | 为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册带有返回值的按键事件回调。通过此接口注册的按键事件回调都必须返回一个结果，即true或false。当返回值为true时，该事件将不会继续分发；当返回值为false时，该事件将按照事件处理流程继续分发。 |
| [int32\_t OH\_ArkUI\_XComponent\_StartImageAnalyzer(ArkUI\_NodeHandle node, void\* userData, void (\*callback)(ArkUI\_NodeHandle node, ArkUI\_XComponent\_ImageAnalyzerState statusCode, void\* userData))](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_startimageanalyzer) | 为此XComponent组件实例开始图像AI分析，使用前需先使能图像AI分析能力。 |
| [int32\_t OH\_ArkUI\_XComponent\_StopImageAnalyzer(ArkUI\_NodeHandle node)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_stopimageanalyzer) | 为此XComponent组件实例停止图像AI分析。 |
| [OH\_ArkUI\_SurfaceHolder\* OH\_ArkUI\_SurfaceHolder\_Create(ArkUI\_NodeHandle node)](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_create) | 创建XComponent组件的[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)对象。 |
| [void OH\_ArkUI\_SurfaceHolder\_Dispose(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_dispose) | 销毁[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)对象。 |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_SetUserData(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, void\* userData)](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_setuserdata) | 向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例存储自定义数据。 |
| [void\* OH\_ArkUI\_SurfaceHolder\_GetUserData(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_getuserdata) | 获取[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例存储的自定义数据。 |
| [OH\_ArkUI\_SurfaceCallback\* OH\_ArkUI\_SurfaceCallback\_Create()](capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_create) | 创建[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)对象。 |
| [void OH\_ArkUI\_SurfaceCallback\_Dispose(OH\_ArkUI\_SurfaceCallback\* callback)](capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_dispose) | 销毁[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)对象。 |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceCreatedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceCreated)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_setsurfacecreatedevent) | 设置Surface生命周期回调中的创建回调事件。 |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceChangedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceChanged)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, uint64\_t width, uint64\_t height))](capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_setsurfacechangedevent) | 设置Surface生命周期回调中的大小改变回调事件。 |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceDestroyedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceDestroyed)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_setsurfacedestroyedevent) | 设置Surface生命周期回调中的销毁回调事件。 |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_AddSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder,OH\_ArkUI\_SurfaceCallback\* callback)](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_addsurfacecallback) | 添加Surface生命周期回调到[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例。 |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_RemoveSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder,OH\_ArkUI\_SurfaceCallback\* callback)](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_removesurfacecallback) | 删除[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的先前添加的Surface生命周期回调。 |
| [OHNativeWindow\* OH\_ArkUI\_XComponent\_GetNativeWindow(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_getnativewindow) | 获取[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例关联的NativeWindow。 |
| [int32\_t OH\_ArkUI\_XComponent\_SetAutoInitialize(ArkUI\_NodeHandle node, bool autoInitialize)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_setautoinitialize) | 设置XComponent组件是否需要自动初始化Surface的标志位。 |
| [int32\_t OH\_ArkUI\_XComponent\_Initialize(ArkUI\_NodeHandle node)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_initialize) | 初始化XComponent组件持有的Surface。 |
| [int32\_t OH\_ArkUI\_XComponent\_Finalize(ArkUI\_NodeHandle node)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_finalize) | 销毁XComponent组件持有的Surface。 |
| [int32\_t OH\_ArkUI\_XComponent\_IsInitialized(ArkUI\_NodeHandle node, bool\* isInitialized)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_isinitialized) | 获取XComponent组件是否已经初始化的标志位。 |
| [int32\_t OH\_ArkUI\_XComponent\_SetExpectedFrameRateRange(ArkUI\_NodeHandle node, OH\_NativeXComponent\_ExpectedRateRange range)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_setexpectedframeraterange) | 为此XComponent组件实例设置期望帧率。 |
| [int32\_t OH\_ArkUI\_XComponent\_RegisterOnFrameCallback(ArkUI\_NodeHandle node,void (\*callback)(ArkUI\_NodeHandle node, uint64\_t timestamp, uint64\_t targetTimestamp))](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_registeronframecallback) | 为此XComponent组件实例注册帧回调函数。 |
| [int32\_t OH\_ArkUI\_XComponent\_UnregisterOnFrameCallback(ArkUI\_NodeHandle node)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_unregisteronframecallback) | 为此XComponent组件实例取消注册帧回调函数。 |
| [int32\_t OH\_ArkUI\_XComponent\_SetNeedSoftKeyboard(ArkUI\_NodeHandle node, bool needSoftKeyboard)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_setneedsoftkeyboard) | 为此XComponent组件实例设置是否需要软键盘。 |
| [ArkUI\_AccessibilityProvider\* OH\_ArkUI\_AccessibilityProvider\_Create(ArkUI\_NodeHandle node)](capi-native-interface-xcomponent-h.md#oh_arkui_accessibilityprovider_create) | 基于此XComponent实例创建[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)实例。 |
| [void OH\_ArkUI\_AccessibilityProvider\_Dispose(ArkUI\_AccessibilityProvider\* provider)](capi-native-interface-xcomponent-h.md#oh_arkui_accessibilityprovider_dispose) | 销毁由Native接口[OH\_ArkUI\_AccessibilityProvider\_Create](capi-native-interface-xcomponent-h.md#oh_arkui_accessibilityprovider_create)创建的[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)实例。 |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceShowEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceShow)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_setsurfaceshowevent) | 为此[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)实例设置Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。 |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceHideEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceHide)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_setsurfacehideevent) | 为此[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)实例设置Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。 |
| [ArkUI\_XComponentSurfaceConfig\* OH\_ArkUI\_XComponentSurfaceConfig\_Create()](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponentsurfaceconfig_create) | 创建XComponent组件的[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)对象。 |
| [void OH\_ArkUI\_XComponentSurfaceConfig\_Dispose(ArkUI\_XComponentSurfaceConfig\* config)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponentsurfaceconfig_dispose) | 销毁[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)对象。 |
| [void OH\_ArkUI\_XComponentSurfaceConfig\_SetIsOpaque(ArkUI\_XComponentSurfaceConfig\* config, bool isOpaque)](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponentsurfaceconfig_setisopaque) | 设置XComponent组件持有的Surface在渲染时是否被视为不透明，无论该Surface是否存在半透明像素。 |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_SetSurfaceConfig(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, ArkUI\_XComponentSurfaceConfig \*config)](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_setsurfaceconfig) | 为[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例设置Surface选项。 |

### 变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const uint32\_t OH\_XCOMPONENT\_ID\_LEN\_MAX = 128 | ArkUI XComponent的id最大长度。  **起始版本：** 8 |
| const uint32\_t OH\_MAX\_TOUCH\_POINTS\_NUMBER = 10 | 触摸事件中的可识别的触摸点个数最大值。  **起始版本：** 8 |
| OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER 10 | 最大支持10个触摸点。  **起始版本：** 8 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### anonymous

PhonePC/2in1TabletTVWearable

```
1. enum anonymous
```

**描述：**

枚举API访问状态。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS = 0 | 成功结果。 |
| OH\_NATIVEXCOMPONENT\_RESULT\_FAILED = -1 | 失败结果。 |
| OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER = -2 | 无效参数。 |

### ArkUI\_XComponent\_ImageAnalyzerState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_XComponent_ImageAnalyzerState
```

**描述：**

XComponent图像AI分析状态码.

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_FINISHED = 0 | 图像AI分析完成。 |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_DISABLED = 110000 | 图像AI分析已禁用。 |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_UNSUPPORTED = 110001 | 设备不支持图像AI分析。 |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_ONGOING = 110002 | 图像AI分析进行中。 |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_STOPPED = 110003 | 图像AI分析停止。 |

### OH\_NativeXComponent\_TouchEventType

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_TouchEventType
```

**描述：**

触摸事件类型。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_DOWN = 0 | 手指按下时触发触摸事件。 |
| OH\_NATIVEXCOMPONENT\_UP = 1 | 手指抬起时触发触摸事件。 |
| OH\_NATIVEXCOMPONENT\_MOVE = 2 | 手指按下状态下在屏幕上移动时触发触摸事件。 |
| OH\_NATIVEXCOMPONENT\_CANCEL = 3 | 触摸事件取消时触发事件。 |
| OH\_NATIVEXCOMPONENT\_UNKNOWN = 4 | 无效的触摸类型。 |

### OH\_NativeXComponent\_TouchPointToolType

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_TouchPointToolType
```

**描述：**

触摸点工具类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_UNKNOWN = 0 | 未识别工具类型。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_FINGER = 1 | 表示用手指。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_PEN = 2 | 表示用触笔。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_RUBBER = 3 | 表示用橡皮擦。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_BRUSH = 4 | 表示用画笔。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_PENCIL = 5 | 表示用铅笔。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_AIRBRUSH = 6 | 表示用气笔。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_MOUSE = 7 | 表示用鼠标。 |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_LENS = 8 | 表示用晶状体。 |

### OH\_NativeXComponent\_EventSourceType

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_EventSourceType
```

**描述：**

触摸事件源类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_UNKNOWN = 0 | 未知的输入源类型。 |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_MOUSE = 1 | 表示输入源生成鼠标多点触摸事件。 |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_TOUCHSCREEN = 2 | 表示输入源生成一个触摸屏多点触摸事件。 |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_TOUCHPAD = 3 | 表示输入源生成一个触摸板多点触摸事件。 |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_JOYSTICK = 4 | 表示输入源生成一个操纵杆多点触摸事件。 |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_KEYBOARD = 5 | 表示输入源生成一个键盘事件。  **起始版本：** 10 |

### OH\_NativeXComponent\_MouseEventAction

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_MouseEventAction
```

**描述：**

鼠标事件动作。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_MOUSE\_NONE = 0 | 无效鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_MOUSE\_PRESS = 1 | 鼠标按键按下时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_MOUSE\_RELEASE = 2 | 鼠标按键松开时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_MOUSE\_MOVE = 3 | 鼠标在屏幕上移动时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_MOUSE\_CANCEL = 4 | 鼠标按键被取消时触发鼠标事件。  **起始版本：** 18  **说明：** OH\_NATIVEXCOMPONENT\_MOUSE\_CANCEL表示鼠标事件被取消，通常在以下场景被触发：  1.组件失去焦点：当前持有焦点的XComponent因系统事件（如弹窗打断、应用切换）失去焦点时，会触发该动作。  2.事件中断：鼠标操作过程中发生更高优先级事件（如系统级手势或强制回收事件流），导致当前鼠标操作被强制终止。  3.异常状态退出：如组件销毁、渲染环境异常等场景下，未完成的鼠标事件会被标记为取消。 |

### OH\_NativeXComponent\_MouseEventButton

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_MouseEventButton
```

**描述：**

鼠标事件按键。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_NONE\_BUTTON = 0 | 鼠标无按键操作时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_LEFT\_BUTTON = 0x01 | 按下鼠标左键时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_RIGHT\_BUTTON = 0x02 | 按下鼠标右键时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_MIDDLE\_BUTTON = 0x04 | 按下鼠标中键时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_BACK\_BUTTON = 0x08 | 按下鼠标左侧后退键时触发鼠标事件。 |
| OH\_NATIVEXCOMPONENT\_FORWARD\_BUTTON = 0x10 | 按下鼠标左侧前进键时触发鼠标事件。 |

### OH\_NativeXComponent\_TouchEvent\_SourceTool

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_TouchEvent_SourceTool
```

**描述：**

表示触摸事件的源工具类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_UNKNOWN = 0 | 未知的触摸事件的源工具。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_FINGER = 1 | 表示触摸事件的源工具是手指。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_PEN = 2 | 表示触摸事件的源工具是钢笔。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_RUBBER = 3 | 表示触摸事件的源工具是橡皮。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_BRUSH = 4 | 表示触摸事件的源工具是笔刷。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_PENCIL = 5 | 表示触摸事件的源工具是铅笔。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_AIRBRUSH = 6 | 表示触摸事件的源工具是喷枪。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_MOUSE = 7 | 表示触摸事件的源工具是鼠标。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_LENS = 8 | 表示触摸事件的源工具是透镜。 |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_TOUCHPAD = 9 | 表示触摸事件的源工具是触摸板。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeXComponent\_GetXComponentId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetXComponentId(OH_NativeXComponent* component, char* id, uint64_t* size)
```

**描述：**

获取ArkUI XComponent的id。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| char\* id | 表示用于保存此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的ID的字符缓冲区。请注意，空终止符将附加到字符缓冲区，因此字符缓冲区的大小应至少比真实id长度大一个单位。建议字符缓冲区的大小为[[OH\_XCOMPONENT\_ID\_LEN\_MAX](capi-native-interface-xcomponent-h.md#变量) + 1]。 |
| uint64\_t\* size | 表示指向id长度的指针，用于接收id的长度信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetXComponentSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetXComponentSize(OH_NativeXComponent* component, const void* window, uint64_t* width, uint64_t* height)
```

**描述：**

获取ArkUI XComponent持有的Surface的大小。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| const void\* window | 表示NativeWindow句柄。 |
| uint64\_t\* width | 表示指向当前Surface宽度的指针。单位：vp。 |
| uint64\_t\* height | 表示指向当前Surface高度的指针。单位：vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetXComponentOffset()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetXComponentOffset(OH_NativeXComponent* component, const void* window, double* x, double* y)
```

**描述：**

获取ArkUI XComponent持有的Surface相对其父组件左顶点的偏移量。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| const void\* window | 表示NativeWindow句柄。 |
| double\* x | 表示指向当前Surface相对于XComponent父组件左顶点x坐标的指针。单位：vp。 |
| double\* y | 表示指向当前Surface相对于XComponent父组件左顶点y坐标的指针。单位：vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetTouchEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchEvent(OH_NativeXComponent* component, const void* window, OH_NativeXComponent_TouchEvent* touchEvent)
```

**描述：**

获取ArkUI XComponent调度的触摸事件。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| const void\* window | 表示NativeWindow句柄。 |
| [OH\_NativeXComponent\_TouchEvent](t-native-xcomponent-oh-nativexcomponent-touchevent.md)\* touchEvent | 表示指向当前触摸事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetTouchPointToolType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchPointToolType(OH_NativeXComponent* component, uint32_t pointIndex,OH_NativeXComponent_TouchPointToolType* toolType)
```

**描述：**

获取ArkUI XComponent触摸点工具类型。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| uint32\_t pointIndex | 表示触摸点的指针索引。 |
| [OH\_NativeXComponent\_TouchPointToolType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_touchpointtooltype)\* toolType | 表示指向工具类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetTouchPointTiltX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchPointTiltX(OH_NativeXComponent* component, uint32_t pointIndex, float* tiltX)
```

**描述：**

获取ArkUI XComponent触摸点倾斜与X轴角度。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| uint32\_t pointIndex | 表示触摸点的指针索引。 |
| float\* tiltX | 表示指向X倾斜度的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetTouchPointTiltY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchPointTiltY(OH_NativeXComponent* component, uint32_t pointIndex, float* tiltY)
```

**描述：**

获取ArkUI XComponent触摸点倾斜与Y轴角度。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| uint32\_t pointIndex | 表示触摸点的指针索引。 |
| float\* tiltY | 表示指向Y倾斜度的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetTouchPointWindowX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchPointWindowX(OH_NativeXComponent* component, uint32_t pointIndex, float* windowX)
```

**描述：**

获取ArkUI XComponent触摸点相对于应用窗口左上角的X坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| uint32\_t pointIndex | 表示触摸点的指针索引。 |
| float\* windowX | 表示指向触摸点相对于应用窗口左上角的X坐标的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) 获取windowX成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) component是空指针、windowX是空指针或者native XComponent是空指针。 |

### OH\_NativeXComponent\_GetTouchPointWindowY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchPointWindowY(OH_NativeXComponent* component, uint32_t pointIndex, float* windowY)
```

**描述：**

获取ArkUI XComponent触摸点相对于应用窗口左上角的Y坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| uint32\_t pointIndex | 表示触摸点的指针索引。 |
| float\* windowY | 表示指向触摸点相对于应用窗口左上角的Y坐标的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) 获取windowY成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) component是空指针、windowY是空指针或者native XComponent是空指针。 |

### OH\_NativeXComponent\_GetTouchPointDisplayX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchPointDisplayX(OH_NativeXComponent* component, uint32_t pointIndex, float* displayX)
```

**描述：**

获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的X坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| uint32\_t pointIndex | 表示触摸点的指针索引。 |
| float\* displayX | 表示指向触摸点相对于应用所在屏幕左上角的X坐标的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) 获取displayX成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) component是空指针、displayX是空指针或者native XComponent是空指针。 |

### OH\_NativeXComponent\_GetTouchPointDisplayY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchPointDisplayY(OH_NativeXComponent* component, uint32_t pointIndex, float* displayY)
```

**描述：**

获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的Y坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| uint32\_t pointIndex | 表示触摸点的指针索引。 |
| float\* displayY | 表示指向触摸点相对于应用所在屏幕左上角的Y坐标的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) 获取displayY成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) component是空指针、displayY是空指针或者native XComponent是空指针。 |

### OH\_NativeXComponent\_GetHistoricalPoints()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetHistoricalPoints(OH_NativeXComponent* component, const void* window,int32_t* size, OH_NativeXComponent_HistoricalPoint** historicalPoints)
```

**描述：**

获取当前XComponent触摸事件的历史点信息。由于部分输入设备上报触点的频率非常高（最高可达每1 ms上报一次），而对输入事件的响应通常是为了使UI界面发生变化以响应用户操作，如果将触摸事件按照上报触点的频率如此高频率上报给应用，大多会造成冗余，因此触摸事件在一帧内只会上报一次给应用。在当前帧内上报的触点均作为历史点保存，如果应用需要直接处理这些数据，可调用该接口获取历史点信息。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| const void\* window | 表示NativeWindow句柄。 |
| int32\_t\* size | 表示当前历史接触点数组的长度。 |
| [OH\_NativeXComponent\_HistoricalPoint](ive-xcomponent-oh-nativexcomponent-historicalpoint.md)\*\* historicalPoints | 表示指向当前历史接触点数组的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetMouseEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetMouseEvent(OH_NativeXComponent* component, const void* window, OH_NativeXComponent_MouseEvent* mouseEvent)
```

**描述：**

获取ArkUI XComponent调度的鼠标事件。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| const void\* window | 表示NativeWindow句柄。 |
| [OH\_NativeXComponent\_MouseEvent](t-native-xcomponent-oh-nativexcomponent-mouseevent.md)\* mouseEvent | 表示指向当前鼠标事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterCallback(OH_NativeXComponent* component, OH_NativeXComponent_Callback* callback)
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册回调。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [OH\_NativeXComponent\_Callback](ent-native-xcomponent-oh-nativexcomponent-callback.md)\* callback | 表示指向Surface生命周期和触摸事件回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterMouseEventCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterMouseEventCallback(OH_NativeXComponent* component, OH_NativeXComponent_MouseEvent_Callback* callback)
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册鼠标事件回调。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [OH\_NativeXComponent\_MouseEvent\_Callback](xcomponent-oh-nativexcomponent-mouseevent-callback.md)\* callback | 表示指向鼠标事件回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetExtraMouseEventInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetExtraMouseEventInfo(OH_NativeXComponent* component, OH_NativeXComponent_ExtraMouseEventInfo** extraMouseEventInfo)
```

**描述：**

从此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例中获取扩展的鼠标事件信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [OH\_NativeXComponent\_ExtraMouseEventInfo](xcomponent-oh-nativexcomponent-extramouseeventinfo.md)\*\* extraMouseEventInfo | 表示指向[OH\_NativeXComponent\_ExtraMouseEventInfo](xcomponent-oh-nativexcomponent-extramouseeventinfo.md)类型指针的地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_NativeXComponent\_GetMouseEventModifierKeyStates()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetMouseEventModifierKeyStates(OH_NativeXComponent_ExtraMouseEventInfo* extraMouseEventInfo, uint64_t* keys)
```

**描述：**

从[OH\_NativeXComponent\_ExtraMouseEventInfo](xcomponent-oh-nativexcomponent-extramouseeventinfo.md)实例中获取功能键按压状态信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_ExtraMouseEventInfo](xcomponent-oh-nativexcomponent-extramouseeventinfo.md)\* extraMouseEventInfo | 表示指向扩展的鼠标事件信息实例的指针。 |
| uint64\_t\* keys | 表示用于接收功能键按压状态信息的64位无符号整数的地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterFocusEventCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterFocusEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册获焦事件回调。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | 表示指向获焦事件回调的指针。- window: 表示NativeWindow句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterKeyEventCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterKeyEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册按键事件回调。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | 表示指向按键事件回调的指针。- window: 表示NativeWindow句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterBlurEventCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterBlurEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册失焦事件回调。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | 表示指向失焦事件回调的指针。- window: 表示NativeWindow句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEvent(OH_NativeXComponent* component, OH_NativeXComponent_KeyEvent** keyEvent)
```

**描述：**

获取ArkUI XComponent调度的按键事件。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\*\* keyEvent | 表示指向当前按键事件指针的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventAction()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventAction(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_KeyAction* action)
```

**描述：**

获取传入按键事件的动作。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向[OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)实例的指针。 |
| [OH\_NativeXComponent\_KeyAction](capi-native-xcomponent-key-event-h.md#oh_nativexcomponent_keyaction)\* action | 表示指向按键事件动作的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventCode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventCode(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_KeyCode* code)
```

**描述：**

获取传入按键事件的按键码。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向[OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)实例的指针。 |
| [OH\_NativeXComponent\_KeyCode](capi-native-xcomponent-key-event-h.md#oh_nativexcomponent_keycode)\* code | 表示指向按键事件按键码的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventSourceType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventSourceType(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_EventSourceType* sourceType)
```

**描述：**

获取传入按键事件的事件源类型。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向[OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)实例的指针。 |
| [OH\_NativeXComponent\_EventSourceType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_eventsourcetype)\* sourceType | 表示指向按键事件事件源类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventDeviceId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventDeviceId(OH_NativeXComponent_KeyEvent* keyEvent, int64_t* deviceId)
```

**描述：**

获取传入按键事件的设备id。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向[OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)实例的指针。 |
| int64\_t\* deviceId | 表示指向按键事件设备id的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventTimestamp()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventTimestamp(OH_NativeXComponent_KeyEvent* keyEvent, int64_t* timestamp)
```

**描述：**

获取传入按键事件的时间戳。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向[OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)实例的指针。 |
| int64\_t\* timestamp | 表示指向按键事件时间戳的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventModifierKeyStates()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventModifierKeyStates(OH_NativeXComponent_KeyEvent* keyEvent, uint64_t* keys)
```

**描述：**

从按键事件中获取功能键按压状态信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向按键事件的指针。 |
| uint64\_t\* keys | 表示用于接收功能键按压状态信息的64位无符号整数的地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventNumLockState()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventNumLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isNumLockOn)
```

**描述：**

从按键事件中获取NumLock（小键盘锁定）键的状态信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向按键事件的指针。 |
| bool\* isNumLockOn | 表示用于接收NumLock（小键盘锁定）键状态的bool类型变量的地址。true表示小键盘锁定，false表示小键盘解锁。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventCapsLockState()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventCapsLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isCapsLockOn)
```

**描述：**

从按键事件中获取CapsLock（大写锁定）键的状态信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向按键事件的指针。 |
| bool\* isCapsLockOn | 表示用于接收CapsLock（大写锁定）键状态的bool类型变量的地址。true表示大写处于锁定，false表示大写处于解锁。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_NativeXComponent\_GetKeyEventScrollLockState()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetKeyEventScrollLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isScrollLockOn)
```

**描述：**

从按键事件中获取ScrollLock（滚动锁定）键的状态信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent\_KeyEvent](ent-native-xcomponent-oh-nativexcomponent-keyevent.md)\* keyEvent | 表示指向按键事件的指针。 |
| bool\* isScrollLockOn | 表示用于接收ScrollLock（滚动锁定）键状态的bool类型变量的地址。true表示滚动处于锁定，false表示滚动处于解锁。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_NativeXComponent\_SetExpectedFrameRateRange()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_SetExpectedFrameRateRange(OH_NativeXComponent* component, OH_NativeXComponent_ExpectedRateRange* range)
```

**描述：**

设置期望帧率范围。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [OH\_NativeXComponent\_ExpectedRateRange](e-xcomponent-oh-nativexcomponent-expectedraterange.md)\* range | 表示指向[OH\_NativeXComponent\_ExpectedRateRange](e-xcomponent-oh-nativexcomponent-expectedraterange.md)类型的期望帧率信息对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterOnFrameCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterOnFrameCallback(OH_NativeXComponent* component,void (*callback)(OH_NativeXComponent* component, uint64_t timestamp, uint64_t targetTimestamp))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册显示更新回调，并使能每帧回调此函数。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void (\*callback)(OH\_NativeXComponent\* component, uint64\_t timestamp, uint64\_t targetTimestamp) | 表示指向显示更新回调的指针。- timestamp: 当前帧到达的时间（单位：纳秒）。- targetTimestamp: 下一帧预期到达的时间（单位：纳秒）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_UnregisterOnFrameCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_UnregisterOnFrameCallback(OH_NativeXComponent* component)
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例取消注册回调函数，并关闭每帧回调此函数。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_AttachNativeRootNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_AttachNativeRootNode(OH_NativeXComponent* component, ArkUI_NodeHandle root)
```

**描述：**

将通过ArkUI的Native接口创建出来的UI组件挂载到当前XComponent上。

**起始版本：** 12

**废弃版本：** 20

**替代接口：** [OH\_ArkUI\_NodeContent\_AddNode](capi-native-node-h.md#oh_arkui_nodecontent_addnode)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) root | 表示指向Native接口创建的组件实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 成功。  返回 [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 参数异常。 |

### OH\_NativeXComponent\_DetachNativeRootNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_DetachNativeRootNode(OH_NativeXComponent* component, ArkUI_NodeHandle root)
```

**描述：**

将ArkUI的Native组件从当前XComponent上卸载。

**起始版本：** 12

**废弃版本：** 20

**替代接口：** [OH\_ArkUI\_NodeContent\_RemoveNode](capi-native-node-h.md#oh_arkui_nodecontent_removenode)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) root | 表示指向Native接口创建的组件实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 成功。  返回 [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 参数异常。 |

### OH\_NativeXComponent\_RegisterUIInputEventCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterUIInputEventCallback(OH_NativeXComponent *component,void (*callback)(OH_NativeXComponent *component, ArkUI_UIInputEvent *event,ArkUI_UIInputEvent_Type type),ArkUI_UIInputEvent_Type type)
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册UI输入事件回调，并使能收到UI输入事件时回调此函数。当前仅支持轴事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md) \*component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void (\*callback)(OH\_NativeXComponent \*component, ArkUI\_UIInputEvent \*event,ArkUI\_UIInputEvent\_Type type) | 表示指向UI输入事件回调的指针。- event: 表示指向UI输入事件的指针。 |
| [ArkUI\_UIInputEvent\_Type](capi-ui-input-event-h.md#arkui_uiinputevent_type) type | 表示当前UI输入事件的类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 参数异常。 |

### OH\_NativeXComponent\_RegisterOnTouchInterceptCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterOnTouchInterceptCallback(OH_NativeXComponent* component, HitTestMode (*callback)(OH_NativeXComponent* component, ArkUI_UIInputEvent* event))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册自定义事件拦截回调，并使能在做触摸测试时回调此函数。通过该回调获取到的事件对象不支持UIInput相关信息操作接口，建议切换为通过注册native node上的[NODE\_ON\_TOUCH\_INTERCEPT](capi-native-node-h.md#arkui_nodeeventtype)通用事件来支持。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| HitTestMode (\*callback)(OH\_NativeXComponent\* component, ArkUI\_UIInputEvent\* event) | 表示指向自定义事件拦截回调的指针。- event: 表示指向UI输入事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 参数异常。 |

### OH\_NativeXComponent\_SetNeedSoftKeyboard()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_SetNeedSoftKeyboard(OH_NativeXComponent* component, bool needSoftKeyboard)
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例设置是否需要软键盘。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| bool needSoftKeyboard | 表示此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例是否需要软键盘。需要时为true，不需要时为false，默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterSurfaceShowCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterSurfaceShowCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | 表示指向Surface显示回调的指针。- window: 表示NativeWindow句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_RegisterSurfaceHideCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterSurfaceHideCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | 表示指向Surface隐藏回调的指针。- window: 表示NativeWindow句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 执行成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_NativeXComponent\_GetTouchEventSourceType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetTouchEventSourceType(OH_NativeXComponent* component, int32_t pointId, OH_NativeXComponent_EventSourceType* sourceType)
```

**描述：**

获取ArkUI XComponent触摸事件的输入设备类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| int32\_t pointId | 表示触摸点的id。仅当传入的id为触发该touch事件的触点id时，可正确返回输入设备类型，否则返回OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER。 |
| [OH\_NativeXComponent\_EventSourceType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_eventsourcetype)\* sourceType | 表示指向返回设备类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 参数异常。  [OH\_NATIVEXCOMPONENT\_RESULT\_FAILED](capi-native-interface-xcomponent-h.md#anonymous) - 其他错误。 |

### OH\_NativeXComponent\_GetNativeXComponent()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeXComponent* OH_NativeXComponent_GetNativeXComponent(ArkUI_NodeHandle node)
```

**描述：**

基于Native接口创建的组件实例获取[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)类型的指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指向Native接口创建的组件实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |

### OH\_NativeXComponent\_GetNativeAccessibilityProvider()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_GetNativeAccessibilityProvider(OH_NativeXComponent* component, ArkUI_AccessibilityProvider** handle)
```

**描述：**

获取ArkUI XComponent无障碍接入句柄指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)\*\* handle | 表示指向[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 参数异常。  [OH\_NATIVEXCOMPONENT\_RESULT\_FAILED](capi-native-interface-xcomponent-h.md#anonymous) - 其他错误。 |

### OH\_NativeXComponent\_RegisterKeyEventCallbackWithResult()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeXComponent_RegisterKeyEventCallbackWithResult(OH_NativeXComponent* component, bool (*callback)(OH_NativeXComponent* component, void* window))
```

**描述：**

为此[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例注册带有返回值的按键事件回调。通过此接口注册的按键事件回调都必须返回一个结果，即true或false。当返回值为true时，该事件将不会继续分发；当返回值为false时，该事件将按照事件处理流程继续分发。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| bool (\*callback)(OH\_NativeXComponent\* component, void\* window) | 表示指向按键事件回调的指针。- window: 表示NativeWindow句柄。当回调返回值为true时，该事件将不会继续分发；当回调返回值为false时，该事件将按照事件处理流程继续分发。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](capi-native-interface-xcomponent-h.md#anonymous) - 回调函数注册成功。  [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](capi-native-interface-xcomponent-h.md#anonymous) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_StartImageAnalyzer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_StartImageAnalyzer(ArkUI_NodeHandle node, void* userData,void (*callback)(ArkUI_NodeHandle node, ArkUI_XComponent_ImageAnalyzerState statusCode, void* userData))
```

**描述：**

为此XComponent组件实例开始图像AI分析，使用前需先使能图像AI分析能力。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示XComponent组件实例。 |
| void\* userData | 表示开发者需要在回调函数执行时获取的数据的指针。 |
| void (\*callback)(ArkUI\_NodeHandle node, ArkUI\_XComponent\_ImageAnalyzerState statusCode, void\* userData) | 表示图像AI分析状态刷新时触发的回调函数。- statusCode: 回调函数的入参之一，表示当前的图像分析状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_StopImageAnalyzer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_StopImageAnalyzer(ArkUI_NodeHandle node)
```

**描述：**

为此XComponent组件实例停止图像AI分析。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示XComponent组件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_SurfaceHolder\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_ArkUI_SurfaceHolder* OH_ArkUI_SurfaceHolder_Create(ArkUI_NodeHandle node)
```

**描述：**

创建XComponent组件的[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)对象。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示指向Native接口创建的XComponent组件实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* | 返回被创建的[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)对象的指针。 |

### OH\_ArkUI\_SurfaceHolder\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SurfaceHolder_Dispose(OH_ArkUI_SurfaceHolder* surfaceHolder)
```

**描述：**

销毁[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)对象。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* surfaceHolder | 表示指向需要销毁的[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |

### OH\_ArkUI\_SurfaceHolder\_SetUserData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SurfaceHolder_SetUserData(OH_ArkUI_SurfaceHolder* surfaceHolder, void* userData)
```

**描述：**

向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例存储自定义数据。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* surfaceHolder | 表示指向存储自定义数据的[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |
| void\* userData | 表示指向要存储的自定义数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_SurfaceHolder\_GetUserData()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_SurfaceHolder_GetUserData(OH_ArkUI_SurfaceHolder* surfaceHolder)
```

**描述：**

获取[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例存储的自定义数据。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* surfaceHolder | 表示指向存储自定义数据的[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 返回自定义数据。 |

### OH\_ArkUI\_SurfaceCallback\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_ArkUI_SurfaceCallback* OH_ArkUI_SurfaceCallback_Create()
```

**描述：**

创建[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)对象。

**起始版本：** 19

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* | 返回创建的[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)对象的指针。 |

### OH\_ArkUI\_SurfaceCallback\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SurfaceCallback_Dispose(OH_ArkUI_SurfaceCallback* callback)
```

**描述：**

销毁[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)对象。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向需要销毁的[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)对象的指针。 |

### OH\_ArkUI\_SurfaceCallback\_SetSurfaceCreatedEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceCreated)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

**描述：**

设置Surface生命周期回调中的创建回调事件。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向Surface生命周期回调的指针。 |
| void (\*onSurfaceCreated)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder) | 表示声明Surface创建时会触发的回调事件。- surfaceHolder: 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |

### OH\_ArkUI\_SurfaceCallback\_SetSurfaceChangedEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceChanged)(OH_ArkUI_SurfaceHolder* surfaceHolder, uint64_t width, uint64_t height))
```

**描述：**

设置Surface生命周期回调中的大小改变回调事件。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向Surface生命周期回调的指针。 |
| void (\*onSurfaceChanged)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, uint64\_t width, uint64\_t height) | 表示声明Surface大小改变时会触发的回调事件。- surfaceHolder: 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。- width: 表示Surface大小变化后的宽度。单位：vp。- height: 表示Surface大小变化后的高度。单位：vp。 |

### OH\_ArkUI\_SurfaceCallback\_SetSurfaceDestroyedEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceDestroyed)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

**描述：**

设置Surface生命周期回调中的销毁回调事件。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向Surface生命周期回调的指针。 |
| void (\*onSurfaceDestroyed)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder) | 表示声明Surface销毁时会触发的回调事件。- surfaceHolder: 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |

### OH\_ArkUI\_SurfaceHolder\_AddSurfaceCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SurfaceHolder_AddSurfaceCallback(OH_ArkUI_SurfaceHolder* surfaceHolder,OH_ArkUI_SurfaceCallback* callback)
```

**描述：**

添加Surface生命周期回调到[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* surfaceHolder | 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向新回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_SurfaceHolder\_RemoveSurfaceCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SurfaceHolder_RemoveSurfaceCallback(OH_ArkUI_SurfaceHolder* surfaceHolder,OH_ArkUI_SurfaceCallback* callback)
```

**描述：**

删除[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的先前添加的Surface生命周期回调。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* surfaceHolder | 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向需要删除的回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_GetNativeWindow()

PhonePC/2in1TabletTVWearable

```
1. OHNativeWindow* OH_ArkUI_XComponent_GetNativeWindow(OH_ArkUI_SurfaceHolder* surfaceHolder)
```

**描述：**

获取[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例关联的NativeWindow。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* surfaceHolder | 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativeWindow](oh-nativexcomponent-native-xcomponent-nativewindow.md)\* | 返回[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例关联的NativeWindow。 |

### OH\_ArkUI\_XComponent\_SetAutoInitialize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_SetAutoInitialize(ArkUI_NodeHandle node, bool autoInitialize)
```

**描述：**

设置XComponent组件是否需要自动初始化Surface的标志位。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示指向XComponent组件实例的指针。 |
| bool autoInitialize | 表示XComponent组件是否需要自动初始化Surface。如果autoInitialize值是true，OnSurfaceCreated回调会在挂树时被触发，OnSurfaceDestroyed回调会在下树时被触发。false表示组件不需要自动初始化Surface。  autoInitialize默认值是true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_Initialize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_Initialize(ArkUI_NodeHandle node)
```

**描述：**

初始化XComponent组件持有的Surface。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示指向XComponent组件实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。  返回 [ARKUI\_ERROR\_CODE\_XCOMPONENT\_STATE\_INVALID](capi-native-type-h.md#arkui_errorcode) - XComponent持有的Surface已经被初始化。 |

### OH\_ArkUI\_XComponent\_Finalize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_Finalize(ArkUI_NodeHandle node)
```

**描述：**

销毁XComponent组件持有的Surface。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示指向XComponent组件实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。  返回 [ARKUI\_ERROR\_CODE\_XCOMPONENT\_STATE\_INVALID](capi-native-type-h.md#arkui_errorcode) - XComponent持有的Surface已经被销毁。 |

### OH\_ArkUI\_XComponent\_IsInitialized()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_IsInitialized(ArkUI_NodeHandle node, bool* isInitialized)
```

**描述：**

获取XComponent组件是否已经初始化的标志位。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示指向XComponent组件实例的指针。 |
| bool\* isInitialized | 表示XComponent组件是否已经初始化Surface。true表示组件已初始化Surface，false表示组件未初始化Surface。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_SetExpectedFrameRateRange()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_SetExpectedFrameRateRange(ArkUI_NodeHandle node, OH_NativeXComponent_ExpectedRateRange range)
```

**描述：**

为此XComponent组件实例设置期望帧率。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示XComponent组件实例。 |
| [OH\_NativeXComponent\_ExpectedRateRange](e-xcomponent-oh-nativexcomponent-expectedraterange.md) range | 表示[OH\_NativeXComponent\_ExpectedRateRange](e-xcomponent-oh-nativexcomponent-expectedraterange.md)类型的期望帧率信息对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_RegisterOnFrameCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_RegisterOnFrameCallback(ArkUI_NodeHandle node,void (*callback)(ArkUI_NodeHandle node, uint64_t timestamp, uint64_t targetTimestamp))
```

**描述：**

为此XComponent组件实例注册帧回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示XComponent组件实例。 |
| void (\*callback)(ArkUI\_NodeHandle node, uint64\_t timestamp, uint64\_t targetTimestamp) | 表示执行帧回调函数的指针。- timestamp: 当前帧到达的时间（单位：纳秒）。- targetTimestamp: 下一帧预期到达的时间（单位：纳秒）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_UnregisterOnFrameCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_UnregisterOnFrameCallback(ArkUI_NodeHandle node)
```

**描述：**

为此XComponent组件实例取消注册帧回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示XComponent组件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_XComponent\_SetNeedSoftKeyboard()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_XComponent_SetNeedSoftKeyboard(ArkUI_NodeHandle node, bool needSoftKeyboard)
```

**描述：**

为此XComponent组件实例设置是否需要软键盘。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示XComponent组件实例。 |
| bool needSoftKeyboard | 表示是否需要软键盘。需要时为true，不需要时为false，默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行的状态代码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |

### OH\_ArkUI\_AccessibilityProvider\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AccessibilityProvider* OH_ArkUI_AccessibilityProvider_Create(ArkUI_NodeHandle node)
```

**描述：**

基于此XComponent实例创建[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 表示XComponent组件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)\* | [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)类型的指针。 |

### OH\_ArkUI\_AccessibilityProvider\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityProvider_Dispose(ArkUI_AccessibilityProvider* provider)
```

**描述：**

销毁由Native接口[OH\_ArkUI\_AccessibilityProvider\_Create](capi-native-interface-xcomponent-h.md#oh_arkui_accessibilityprovider_create)创建的[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)\* provider | 表示由Native接口[OH\_ArkUI\_AccessibilityProvider\_Create](capi-native-interface-xcomponent-h.md#oh_arkui_accessibilityprovider_create)创建的[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)实例。 |

### OH\_ArkUI\_SurfaceCallback\_SetSurfaceShowEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SurfaceCallback_SetSurfaceShowEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceShow)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

**描述：**

为此[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)实例设置Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)实例的指针。 |
| onSurfaceShow | 表示Surface显示回调函数指针。- surfaceHolder: 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |

### OH\_ArkUI\_SurfaceCallback\_SetSurfaceHideEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SurfaceCallback_SetSurfaceHideEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceHide)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

**描述：**

为此[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)实例设置Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)\* callback | 表示指向[OH\_ArkUI\_SurfaceCallback](mponent-native-xcomponent-oh-arkui-surfacecallback.md)实例的指针。 |
| onSurfaceHide | 表示Surface隐藏回调函数指针。- surfaceHolder: 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |

### OH\_ArkUI\_XComponentSurfaceConfig\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_XComponentSurfaceConfig* OH_ArkUI_XComponentSurfaceConfig_Create()
```

**描述：**

创建XComponent组件的[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)对象。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)\* | 返回创建的[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)对象的指针。 |

### OH\_ArkUI\_XComponentSurfaceConfig\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_XComponentSurfaceConfig_Dispose(ArkUI_XComponentSurfaceConfig* config)
```

**描述：**

销毁[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)\* config | 表示指向需要销毁的[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)对象的指针。 |

### OH\_ArkUI\_XComponentSurfaceConfig\_SetIsOpaque()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_XComponentSurfaceConfig_SetIsOpaque(ArkUI_XComponentSurfaceConfig* config, bool isOpaque)
```

**描述：**

设置XComponent组件持有的Surface在渲染时是否被视为不透明，无论该Surface是否存在半透明像素。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)\* config | 表示指向[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)实例的指针。 |
| bool isOpaque | 表示设置XComponent组件持有的Surface在渲染时是否需要被视为不透明。true表示需要被视为不透明，false表示不需要被视为不透明，默认值为false，即在渲染时会应用Surface中绘制内容像素的透明度。 |

### OH\_ArkUI\_SurfaceHolder\_SetSurfaceConfig()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SurfaceHolder_SetSurfaceConfig(OH_ArkUI_SurfaceHolder* surfaceHolder, ArkUI_XComponentSurfaceConfig *config)
```

**描述：**

为[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例设置Surface选项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)\* surfaceHolder | 表示指向[OH\_ArkUI\_SurfaceHolder](component-native-xcomponent-oh-arkui-surfaceholder.md)实例的指针。 |
| [ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md) \*config | 表示指向[ArkUI\_XComponentSurfaceConfig](nt-native-xcomponent-arkui-xcomponentsurfaceconfig.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回执行结果。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) - 执行成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) - 传入参数异常。 |
