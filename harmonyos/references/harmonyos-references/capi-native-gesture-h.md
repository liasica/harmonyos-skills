---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h
title: native_gesture.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_gesture.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa75a8b04352b71ec1843aa2974d52fbd08e266272b0f4c9613e7b7bb95bd202
---

## 概述

提供NativeGesture接口的类型定义，支持手势识别器、手势事件、手势打断、触摸识别器、手势收集干预以及手势参数查询与设置等能力，适用于应用通过Native接口处理手势识别、手势冲突和手势收集干预等场景。

**引用文件：** <arkui/native\_gesture.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NativeGestureAPI\_1](capi-arkui-nativemodule-arkui-nativegestureapi-1.md) | ArkUI\_NativeGestureAPI\_1 | 提供创建敲击、长按、滑动、捏合、旋转、快滑手势及手势组的接口，并支持绑定手势、移除手势、设置手势打断回调和并行内部手势回调，用于配置和管理组件的触控交互识别与事件处理。 使用该模块配置手势时，推荐按以下流程操作：调用[createTapGesture](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#createtapgesture)等接口创建手势识别器，调用[setGestureEventTarget](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setgestureeventtarget)注册手势事件回调，再调用[addGestureToNode](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#addgesturetonode)将手势识别器绑定至组件节点；不再使用该手势时，先调用[removeGestureFromNode](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#removegesturefromnode)解除节点绑定，再调用[dispose](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#dispose)释放手势资源。对于手势竞争场景，可通过手势优先级、屏蔽模式或[setGestureInterrupterToNode](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setgestureinterruptertonode)配置响应策略；对于组件内部手势与外部自定义手势需要并行识别的场景，可调用[setInnerGestureParallelTo](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setinnergestureparallelto)设置并行内部手势事件回调。 |
| [ArkUI\_NativeGestureAPI\_2](capi-arkui-nativemodule-arkui-nativegestureapi-2.md) | - | 定义手势模块接口集合，在[ArkUI\_NativeGestureAPI\_1](capi-arkui-nativemodule-arkui-nativegestureapi-1.md)的基础上扩展提供设置手势打断事件回调的能力，用于在手势处理过程中根据回调结果继续或打断手势。开发者可以通过[gestureApi1](capi-arkui-nativemodule-arkui-nativegestureapi-2.md#成员变量)访问基础手势接口，配合[setGestureInterrupterToNode](capi-arkui-nativemodule-arkui-nativegestureapi-2.md#setgestureinterruptertonode)实现完整的手势打断处理功能。 |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md) | ArkUI\_GestureRecognizer | 提供手势组件实例对象定义，用于在ArkUI手势识别相关接口中表示手势识别器对象，帮助开发者理解和使用组件手势识别能力。 |
| [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md) | ArkUI\_GestureInterruptInfo | 提供手势打断信息类型对象定义，用于在手势打断场景中表示与打断处理相关的信息。关于手势打断信息的相关接口，请参见[native\_gesture.h](capi-native-gesture-h.md)。 |
| [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md) | ArkUI\_GestureEvent | 提供手势事件数据类型对象定义，用于在手势事件处理过程中承载和传递手势事件相关数据，支持获取手势事件类型、坐标、时间戳等关键信息；适用于需要处理触摸手势交互的场景，如点击、长按、拖动、缩放等手势识别与响应；开发者可通过相关手势事件接口获取事件信息。 |
| [ArkUI\_GestureEventTargetInfo](capi-arkui-nativemodule-arkui-gestureeventtargetinfo.md) | ArkUI\_GestureEventTargetInfo | 提供手势事件目标信息类型对象定义，用于表示手势事件关联的目标信息，便于在手势处理过程中获取目标对象的滚动状态等相关信息。 |
| [ArkUI\_ParallelInnerGestureEvent](capi-arkui-nativemodule-arkui-parallelinnergestureevent.md) | ArkUI\_ParallelInnerGestureEvent | 定义并行内部手势事件。该结构体作为[setInnerGestureParallelTo](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setinnergestureparallelto)的回调函数的参数传递，用于将系统内置手势（如Scroll、List等容器组件的内置滑动手势）与响应链上其他组件设置为并行关系的场景。 |
| [ArkUI\_TouchRecognizer](capi-arkui-nativemodule-arkui-touchrecognizer.md) | ArkUI\_TouchRecognizer | 定义触摸识别器。触摸识别器是底层触摸事件的识别单元，负责检测和处理触摸按下、移动、抬起等原始触摸事件。 |
| [ArkUI\_TouchRecognizer\*](capi-arkui-nativemodule-arkui-touchrecognizerhandle.md) | ArkUI\_TouchRecognizerHandle | 定义触摸识别器句柄，用于表示触摸识别器对象，并在触摸识别或手势处理接口中传递和管理该对象。适用于自定义手势识别、多点触控事件处理，以及需要对触摸事件进行精细化拦截和分发控制的场景。 |
| [ArkUI\_TouchRecognizerHandle\*](capi-arkui-nativemodule-arkui-touchrecognizerhandlearray.md) | ArkUI\_TouchRecognizerHandleArray | 定义触摸识别器句柄数组，用于在批量管理多个触摸识别器时使用，例如从手势打断信息中获取多个触摸识别器句柄。 |
| [ArkUI\_GestureRecognizer\*](capi-arkui-nativemodule-arkui-gesturerecognizerhandle.md) | ArkUI\_GestureRecognizerHandle | 提供手势识别器句柄类型定义，用于在ArkUI原生手势相关接口中表示手势识别器对象。 |
| [ArkUI\_GestureRecognizerHandle\*](capi-arkui-nativemodule-arkui-gesturerecognizerhandlearray.md) | ArkUI\_GestureRecognizerHandleArray | 提供手势识别器句柄类型数组对象定义，用于在需要表示或传递多个手势识别器句柄的场景中使用。 |
| [ArkUI\_NativeGestureAPI\_3](capi-arkui-nativemodule-arkui-nativegestureapi-3.md) | ArkUI\_NativeGestureAPI\_3 | 定义手势模块接口集合。包含[ArkUI\_NativeGestureAPI\_1](capi-arkui-nativemodule-arkui-nativegestureapi-1.md)、[ArkUI\_NativeGestureAPI\_2](capi-arkui-nativemodule-arkui-nativegestureapi-2.md)结构体中的手势接口及新增手势接口，支持为ArkUI节点设置并行手势事件回调，适用于需要进行并行手势识别处理的交互场景。 |
| [ArkUI\_ParallelGestureEvent](capi-arkui-nativemodule-arkui-parallelgestureevent.md) | ArkUI\_ParallelGestureEvent | 定义并行手势事件。该结构体作为[setGestureParallelTo](capi-arkui-nativemodule-arkui-nativegestureapi-3.md#setgestureparallelto)回调函数的参数传递，用于在触发触摸测试时，将开发者自定义手势与响应链上其他组件的手势设置为并行关系的场景。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_GestureEventActionType](capi-native-gesture-h.md#arkui_gestureeventactiontype) | ArkUI\_GestureEventActionType | 定义手势事件类型。 |
| [ArkUI\_GesturePriority](capi-native-gesture-h.md#arkui_gesturepriority) | ArkUI\_GesturePriority | 定义手势优先级。 |
| [ArkUI\_GroupGestureMode](capi-native-gesture-h.md#arkui_groupgesturemode) | ArkUI\_GroupGestureMode | 定义手势组事件模式。 |
| [ArkUI\_GestureDirection](capi-native-gesture-h.md#arkui_gesturedirection) | ArkUI\_GestureDirection | 定义滑动手势方向。 |
| [ArkUI\_GestureMask](capi-native-gesture-h.md#arkui_gesturemask) | ArkUI\_GestureMask | 定义手势屏蔽模式。 |
| [ArkUI\_GestureRecognizerType](capi-native-gesture-h.md#arkui_gesturerecognizertype) | ArkUI\_GestureRecognizerType | 定义手势类型。 |
| [ArkUI\_GestureInterruptResult](capi-native-gesture-h.md#arkui_gestureinterruptresult) | ArkUI\_GestureInterruptResult | 定义手势打断结果。 |
| [ArkUI\_GestureRecognizerState](capi-native-gesture-h.md#arkui_gesturerecognizerstate) | ArkUI\_GestureRecognizerState | 定义手势识别器状态。 |
| [OH\_ArkUI\_GestureCollectIntervention](capi-native-gesture-h.md#oh_arkui_gesturecollectintervention) | OH\_ArkUI\_GestureCollectIntervention | 定义手势和事件收集的干预操作类型。  **起始版本：** 26.0.0 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*ArkUI\_GestureRecognizerDisposeNotifyCallback)(ArkUI\_GestureRecognizer\* recognizer, void\* userData)](capi-native-gesture-h.md#arkui_gesturerecognizerdisposenotifycallback) | ArkUI\_GestureRecognizerDisposeNotifyCallback | 定义手势识别器析构通知事件的回调函数类型。 |
| [bool OH\_ArkUI\_GestureInterruptInfo\_GetSystemFlag(const ArkUI\_GestureInterruptInfo\* event)](capi-native-gesture-h.md#oh_arkui_gestureinterruptinfo_getsystemflag) | - | 判断是否为系统内置手势。 |
| [ArkUI\_GestureRecognizer\* OH\_ArkUI\_GestureInterruptInfo\_GetRecognizer(const ArkUI\_GestureInterruptInfo\* event)](capi-native-gesture-h.md#oh_arkui_gestureinterruptinfo_getrecognizer) | - | 返回被打断的手势指针。 |
| [ArkUI\_GestureEvent\* OH\_ArkUI\_GestureInterruptInfo\_GetGestureEvent(const ArkUI\_GestureInterruptInfo\* event)](capi-native-gesture-h.md#oh_arkui_gestureinterruptinfo_getgestureevent) | - | 返回打断的手势事件数据。 |
| [int32\_t OH\_ArkUI\_GestureInterruptInfo\_GetSystemRecognizerType(const ArkUI\_GestureInterruptInfo\* event)](capi-native-gesture-h.md#oh_arkui_gestureinterruptinfo_getsystemrecognizertype) | - | 当要触发的是系统内置手势时，使用该方法可返回该系统内置手势的类型。 |
| [int32\_t OH\_ArkUI\_GestureInterruptInfo\_GetTouchRecognizers(const ArkUI\_GestureInterruptInfo\* info,ArkUI\_TouchRecognizerHandleArray\* recognizers, int32\_t\* size)](capi-native-gesture-h.md#oh_arkui_gestureinterruptinfo_gettouchrecognizers) | - | 从手势打断信息中获取触摸识别器。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_TouchRecognizer\_GetNodeHandle(const ArkUI\_TouchRecognizerHandle recognizer)](capi-native-gesture-h.md#oh_arkui_touchrecognizer_getnodehandle) | - | 获取触摸识别器对应的组件句柄。 |
| [int32\_t OH\_ArkUI\_TouchRecognizer\_CancelTouch(ArkUI\_TouchRecognizerHandle recognizer, ArkUI\_GestureInterruptInfo\* info)](capi-native-gesture-h.md#oh_arkui_touchrecognizer_canceltouch) | - | 在手势打断回调中向指定的触摸识别器发送取消触摸的事件。 |
| [ArkUI\_GestureEventActionType OH\_ArkUI\_GestureEvent\_GetActionType(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_gestureevent_getactiontype) | - | 返回手势事件类型。 |
| [const ArkUI\_UIInputEvent\* OH\_ArkUI\_GestureEvent\_GetRawInputEvent(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_gestureevent_getrawinputevent) | - | 返回手势的原始输入事件。 |
| [int32\_t OH\_ArkUI\_LongPress\_GetRepeatCount(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_longpress_getrepeatcount) | - | 返回是否为重复触发事件。 |
| [float OH\_ArkUI\_PanGesture\_GetVelocity(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pangesture_getvelocity) | - | 滑动手势返回手势主方向速度。 |
| [float OH\_ArkUI\_PanGesture\_GetVelocityX(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pangesture_getvelocityx) | - | 滑动手势返回当前手势的x轴方向速度。 |
| [float OH\_ArkUI\_PanGesture\_GetVelocityY(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pangesture_getvelocityy) | - | 滑动手势返回当前手势的y轴方向速度。 |
| [float OH\_ArkUI\_PanGesture\_GetOffsetX(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pangesture_getoffsetx) | - | 滑动手势返回当前手势事件x轴相对偏移量。 |
| [float OH\_ArkUI\_PanGesture\_GetOffsetY(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pangesture_getoffsety) | - | 滑动手势返回当前手势事件y轴相对偏移量。 |
| [float OH\_ArkUI\_SwipeGesture\_GetAngle(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_swipegesture_getangle) | - | 快滑手势返回当前手势事件角度信息，即手指滑动的瞬时方向与水平正方向的夹角。以水平正方向为基准，滑动方向位于水平正方向顺时针侧时，角度范围为0到180度；位于水平正方向逆时针侧时，角度范围为0到-180度。 |
| [float OH\_ArkUI\_SwipeGesture\_GetVelocity(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_swipegesture_getvelocity) | - | 快滑手势场景中所有手指滑动平均速度。 |
| [float OH\_ArkUI\_RotationGesture\_GetAngle(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_rotationgesture_getangle) | - | 旋转手势返回当前手势事件角度信息。 |
| [float OH\_ArkUI\_PinchGesture\_GetScale(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pinchgesture_getscale) | - | 捏合手势返回当前手势事件缩放信息。 |
| [float OH\_ArkUI\_PinchGesture\_GetCenterX(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pinchgesture_getcenterx) | - | 捏合手势中心点相对于当前组件元素左上角x轴坐标。 |
| [float OH\_ArkUI\_PinchGesture\_GetCenterY(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_pinchgesture_getcentery) | - | 捏合手势中心点相对于当前组件元素左上角y轴坐标。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_GestureEvent\_GetNode(const ArkUI\_GestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_gestureevent_getnode) | - | 获取绑定该手势的ArkUI组件。 |
| [int32\_t OH\_ArkUI\_GetResponseRecognizersFromInterruptInfo(const ArkUI\_GestureInterruptInfo\* event,ArkUI\_GestureRecognizerHandleArray\* responseChain, int32\_t\* count)](capi-native-gesture-h.md#oh_arkui_getresponserecognizersfrominterruptinfo) | - | 获取手势响应链的信息。 |
| [int32\_t OH\_ArkUI\_SetGestureRecognizerEnabled(ArkUI\_GestureRecognizer\* recognizer, bool enabled)](capi-native-gesture-h.md#oh_arkui_setgesturerecognizerenabled) | - | 设置手势识别器的使能状态。适用于需要根据应用交互状态动态启用或禁用手势识别的场景，例如在页面滚动动画期间禁用滑动手势以避免误触，或在编辑模式下禁用拖拽手势。 |
| [int32\_t OH\_ArkUI\_SetGestureRecognizerLimitFingerCount(ArkUI\_GestureRecognizer\* recognizer, bool limitFingerCount)](capi-native-gesture-h.md#oh_arkui_setgesturerecognizerlimitfingercount) | - | 设置是否严格检查触摸手指数量的标志。实际触摸手指数量不等于设置的手指数量的时候，该手势识别不成功。 |
| [bool OH\_ArkUI\_GetGestureRecognizerEnabled(ArkUI\_GestureRecognizer\* recognizer)](capi-native-gesture-h.md#oh_arkui_getgesturerecognizerenabled) | - | 获取手势识别器的使能状态。 |
| [int32\_t OH\_ArkUI\_GetGestureRecognizerState(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureRecognizerState\* state)](capi-native-gesture-h.md#oh_arkui_getgesturerecognizerstate) | - | 获取手势识别器的状态。 |
| [int32\_t OH\_ArkUI\_GetGestureEventTargetInfo(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureEventTargetInfo\*\* info)](capi-native-gesture-h.md#oh_arkui_getgestureeventtargetinfo) | - | 获取手势事件目标信息。 |
| [int32\_t OH\_ArkUI\_GestureEventTargetInfo\_IsScrollBegin(ArkUI\_GestureEventTargetInfo\* info, bool\* ret)](capi-native-gesture-h.md#oh_arkui_gestureeventtargetinfo_isscrollbegin) | - | 当前滚动类容器组件是否在顶部。 |
| [int32\_t OH\_ArkUI\_GestureEventTargetInfo\_IsScrollEnd(ArkUI\_GestureEventTargetInfo\* info, bool\* ret)](capi-native-gesture-h.md#oh_arkui_gestureeventtargetinfo_isscrollend) | - | 当前滚动类容器组件是否在底部。 |
| [int32\_t OH\_ArkUI\_GetPanGestureDirectionMask(ArkUI\_GestureRecognizer\* recognizer,ArkUI\_GestureDirectionMask\* directionMask)](capi-native-gesture-h.md#oh_arkui_getpangesturedirectionmask) | - | 获取滑动手势的滑动方向。 |
| [bool OH\_ArkUI\_IsBuiltInGesture(ArkUI\_GestureRecognizer\* recognizer)](capi-native-gesture-h.md#oh_arkui_isbuiltingesture) | - | 当前手势是否为系统内置手势。 |
| [int32\_t OH\_ArkUI\_GetGestureTag(ArkUI\_GestureRecognizer\* recognizer, char\* buffer, int32\_t bufferSize, int32\_t\* result)](capi-native-gesture-h.md#oh_arkui_getgesturetag) | - | 获取手势识别器的标记。 |
| [int32\_t OH\_ArkUI\_GetGestureBindNodeId(ArkUI\_GestureRecognizer\* recognizer, char\* nodeId, int32\_t size,int32\_t\* result)](capi-native-gesture-h.md#oh_arkui_getgesturebindnodeid) | - | 获取手势识别器绑定的组件的ID。 |
| [bool OH\_ArkUI\_IsGestureRecognizerValid(ArkUI\_GestureRecognizer\* recognizer)](capi-native-gesture-h.md#oh_arkui_isgesturerecognizervalid) | - | 当前手势识别器是否有效。 |
| [void\* OH\_ArkUI\_ParallelInnerGestureEvent\_GetUserData(ArkUI\_ParallelInnerGestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_parallelinnergestureevent_getuserdata) | - | 获取并行内置手势事件中的用户自定义数据。 |
| [ArkUI\_GestureRecognizer\* OH\_ArkUI\_ParallelInnerGestureEvent\_GetCurrentRecognizer(ArkUI\_ParallelInnerGestureEvent\* event)](capi-native-gesture-h.md#oh_arkui_parallelinnergestureevent_getcurrentrecognizer) | - | 获取并行内置手势事件中的当前手势识别器。 |
| [int32\_t OH\_ArkUI\_ParallelInnerGestureEvent\_GetConflictRecognizers(ArkUI\_ParallelInnerGestureEvent\* event,ArkUI\_GestureRecognizerHandleArray\* array, int32\_t\* size)](capi-native-gesture-h.md#oh_arkui_parallelinnergestureevent_getconflictrecognizers) | - | 获取并行内置手势事件中的冲突的手势识别器。 |
| [int32\_t OH\_ArkUI\_SetArkUIGestureRecognizerDisposeNotify(ArkUI\_GestureRecognizer\* recognizer,ArkUI\_GestureRecognizerDisposeNotifyCallback callback, void\* userData)](capi-native-gesture-h.md#oh_arkui_setarkuigesturerecognizerdisposenotify) | - | 设置手势识别器对象析构通知回调函数。适用于需要在手势识别器被销毁时进行资源清理或状态更新的场景，例如释放与手势识别器关联的自定义数据或解除其他对象的引用。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_DirectMask(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureDirectionMask\* directMask)](capi-native-gesture-h.md#oh_arkui_getgestureparam_directmask) | - | 获取手势识别器的滑动方向。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_FingerCount(ArkUI\_GestureRecognizer\* recognizer, int\* finger)](capi-native-gesture-h.md#oh_arkui_getgestureparam_fingercount) | - | 获取手势识别器的手指数。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_limitFingerCount(ArkUI\_GestureRecognizer\* recognizer, bool\* isLimited)](capi-native-gesture-h.md#oh_arkui_getgestureparam_limitfingercount) | - | 获取手势识别器是否有手指数限制。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_repeat(ArkUI\_GestureRecognizer\* recognizer, bool\* isRepeat)](capi-native-gesture-h.md#oh_arkui_getgestureparam_repeat) | - | 获取手势识别器是否连续触发事件回调。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_distance(ArkUI\_GestureRecognizer\* recognizer, double\* distance)](capi-native-gesture-h.md#oh_arkui_getgestureparam_distance) | - | 获取手势识别器的手指允许的移动距离范围。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_speed(ArkUI\_GestureRecognizer\* recognizer, double\* speed)](capi-native-gesture-h.md#oh_arkui_getgestureparam_speed) | - | 获取手势识别器的识别滑动的最小速度。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_duration(ArkUI\_GestureRecognizer\* recognizer, int\* duration)](capi-native-gesture-h.md#oh_arkui_getgestureparam_duration) | - | 获取手势识别器的触发长按的最短时间。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_angle(ArkUI\_GestureRecognizer\* recognizer, double\* angle)](capi-native-gesture-h.md#oh_arkui_getgestureparam_angle) | - | 获取手势识别器的旋转手势的最小改变度数。 |
| [int32\_t OH\_ArkUI\_GetGestureParam\_distanceThreshold(ArkUI\_GestureRecognizer\* recognizer, double\* distanceThreshold)](capi-native-gesture-h.md#oh_arkui_getgestureparam_distancethreshold) | - | 获取手势识别器的手势移动阈值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PanGesture\_SetDistanceMap(ArkUI\_GestureRecognizer\* recognizer, int size, int\* toolTypeArray, double\* distanceArray)](capi-native-gesture-h.md#oh_arkui_pangesture_setdistancemap) | - | 设置手势最小滑动阈值表。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PanGesture\_GetDistanceByToolType(ArkUI\_GestureRecognizer\* recognizer, int toolType, double\* distance)](capi-native-gesture-h.md#oh_arkui_pangesture_getdistancebytooltype) | - | 获取手势识别器的手势移动阈值表。仅支持对通过OH\_ArkUI\_PanGesture\_SetDistanceMap修改过的设备类型的阈值查询。默认滑动阈值可通过查询UI\_INPUT\_EVENT\_TOOL\_TYPE\_UNKNOWN类型获得，其他未设置过的类型不会返回。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SetTouchTestDoneCallback(ArkUI\_NodeHandle node,void\* userData,void (\*touchTestDone)(ArkUI\_GestureEvent\* event,ArkUI\_GestureRecognizerHandleArray recognizers,int32\_t count,void\* userData))](capi-native-gesture-h.md#oh_arkui_settouchtestdonecallback) | - | 注册一个在所有手势识别器收集完成后执行的回调函数。当用户开始触摸屏幕时，系统会进行命中测试并根据触摸位置收集手势识别器。随后，在处理任何移动事件之前，组件可以使用此接口确定将参与识别并相互竞争的手势识别器。 |
| [void\* OH\_ArkUI\_GestureInterrupter\_GetUserData(ArkUI\_GestureInterruptInfo\* event)](capi-native-gesture-h.md#oh_arkui_gestureinterrupter_getuserdata) | - | 获取手势中断事件中的用户自定义数据。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PreventGestureRecognizerBegin(ArkUI\_GestureRecognizer\* recognizer)](capi-native-gesture-h.md#oh_arkui_preventgesturerecognizerbegin) | - | 在手指全部抬起前阻止手势识别器参与当前手势识别，适用于需要在手势竞争过程中动态排除指定手势识别器的场景。如果系统已确定该手势识别器的结果（无论成功与否），调用此接口将无效。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LongPressGesture\_SetAllowableMovement(ArkUI\_GestureRecognizer\* recognizer, double allowableMovement)](capi-native-gesture-h.md#oh_arkui_longpressgesture_setallowablemovement) | - | 设置长按手势识别器识别的手势的最大移动距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LongPressGesture\_GetAllowableMovement(ArkUI\_GestureRecognizer\* recognizer, double\* allowableMovement)](capi-native-gesture-h.md#oh_arkui_longpressgesture_getallowablemovement) | - | 获取长按手势识别器识别的手势的最大移动距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GestureCollectInterceptInfo\_GetResponseRecognizers(const ArkUI\_GestureCollectInterceptInfo\* info, ArkUI\_GestureRecognizerHandleArray\* array, int32\_t\* size)](capi-native-gesture-h.md#oh_arkui_gesturecollectinterceptinfo_getresponserecognizers) | - | 从手势收集拦截信息中获取手势识别器。  **起始版本：** 26.0.0 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GestureCollectInterceptInfo\_GetTouchRecognizers(const ArkUI\_GestureCollectInterceptInfo\* info, ArkUI\_TouchRecognizerHandleArray\* recognizers, int32\_t\* size)](capi-native-gesture-h.md#oh_arkui_gesturecollectinterceptinfo_gettouchrecognizers) | - | 从手势收集拦截信息中获取触摸识别器句柄。  **起始版本：** 26.0.0 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GestureCollectInterceptInfo\_SetGestureCollectIntervention(ArkUI\_GestureCollectInterceptInfo\* info, OH\_ArkUI\_GestureCollectIntervention intervention)](capi-native-gesture-h.md#oh_arkui_gesturecollectinterceptinfo_setgesturecollectintervention) | - | 设置手势收集干预模式。  **起始版本：** 26.0.0 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetGestureBindNodeUniqueId(const ArkUI\_GestureRecognizer\* recognizer, int32\_t\* uniqueId)](capi-native-gesture-h.md#oh_arkui_getgesturebindnodeuniqueid) | - | 获取与手势识别器绑定的组件唯一ID。  **起始版本：** 26.0.0 |
| [bool OH\_ArkUI\_TouchRecognizer\_IsHostBelongsTo(const ArkUI\_TouchRecognizerHandle recognizer, int32\_t uniqueId)](capi-native-gesture-h.md#oh_arkui_touchrecognizer_ishostbelongsto) | - | 检查当前触摸识别器绑定节点是否为传入组件的后代节点。  **起始版本：** 26.0.0 |
| [bool OH\_ArkUI\_GestureRecognizer\_IsHostBelongsTo(const ArkUI\_GestureRecognizer\* recognizer, int32\_t uniqueId)](capi-native-gesture-h.md#oh_arkui_gesturerecognizer_ishostbelongsto) | - | 检查当前手势识别器绑定节点是否为传入组件的后代节点。  **起始版本：** 26.0.0 |

### 变量

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| uint32\_t | ArkUI\_GestureDirectionMask | 定义滑动手势方向集合。  例：ArkUI\_GestureDirectionMask directions = GESTURE\_DIRECTION\_LEFT | GESTURE\_DIRECTION\_RIGHT。  directions 表明支持左右水平方向。 |
| uint32\_t | ArkUI\_GestureEventActionTypeMask | 定义手势事件类型集合。例：ArkUI\_GestureEventActionTypeMask actions = GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE。 |

### 示例

| 名称 | 描述 |
| --- | --- |
| [NdkGestureSetting](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkGestureSetting) | 从API version 20开始，新增手势绑定、手势移除以及自定义手势判断的示例。 |
| [NdkGestureNestScroll](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkGestureNestScroll) | 从API version 20开始，新增手势接口实现嵌套滚动的示例。 |
| [NdkGestureBlocking](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkGestureBlocking) | 从API version 20开始，新增手势拦截的示例。 |

## 枚举类型说明

### ArkUI\_GestureEventActionType

```c
enum ArkUI_GestureEventActionType
```

**描述：**

定义手势事件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| GESTURE\_EVENT\_ACTION\_ACCEPT = 0x01 | 手势事件触发。 |
| GESTURE\_EVENT\_ACTION\_UPDATE = 0x02 | 手势事件更新。 |
| GESTURE\_EVENT\_ACTION\_END = 0x04 | 手势事件结束。 |
| GESTURE\_EVENT\_ACTION\_CANCEL = 0x08 | 手势事件取消。 |

### ArkUI\_GesturePriority

```c
enum ArkUI_GesturePriority
```

**描述：**

定义手势优先级。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NORMAL = 0 | 正常手势。 |
| PRIORITY = 1 | 高优先级手势。 |
| PARALLEL = 2 | 并发手势。 |

### ArkUI\_GroupGestureMode

```c
enum ArkUI_GroupGestureMode
```

**描述：**

定义手势组事件模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SEQUENTIAL\_GROUP = 0 | 顺序手势模式，按照注册顺序识别手势，直到所有手势识别成功。若有识别失败，后续识别均失败。仅有最后一个手势响应结束事件。 |
| PARALLEL\_GROUP = 1 | 并发手势模式，注册的手势同时识别，直到所有手势识别结束，手势识别互相不影响。 |
| EXCLUSIVE\_GROUP = 2 | 互斥手势模式，注册的手势同时识别，若有一个手势识别成功，则结束手势识别。 |

### ArkUI\_GestureDirection

```c
enum ArkUI_GestureDirection
```

**描述：**

定义滑动手势方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| GESTURE\_DIRECTION\_ALL = 0b1111 | 所有方向。 |
| GESTURE\_DIRECTION\_HORIZONTAL = 0b0011 | 水平方向。 |
| GESTURE\_DIRECTION\_VERTICAL = 0b1100 | 竖直方向。 |
| GESTURE\_DIRECTION\_LEFT = 0b0001 | 向左方向。 |
| GESTURE\_DIRECTION\_RIGHT = 0b0010 | 向右方向。 |
| GESTURE\_DIRECTION\_UP = 0b0100 | 向上方向。 |
| GESTURE\_DIRECTION\_DOWN = 0b1000 | 向下方向。 |
| GESTURE\_DIRECTION\_NONE = 0 | 任何方向都不触发手势事件。 |

### ArkUI\_GestureMask

```c
enum ArkUI_GestureMask
```

**描述：**

定义手势屏蔽模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NORMAL\_GESTURE\_MASK = 0 | 不屏蔽子组件的手势，按照默认手势识别顺序进行识别。 |
| IGNORE\_INTERNAL\_GESTURE\_MASK = 1 | 屏蔽子组件的手势，包括子组件上系统内置的手势。 |

### ArkUI\_GestureRecognizerType

```c
enum ArkUI_GestureRecognizerType
```

**描述：**

定义手势类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| TAP\_GESTURE = 0 | 敲击手势。 |
| LONG\_PRESS\_GESTURE = 1 | 长按手势。 |
| PAN\_GESTURE = 2 | 滑动手势。 |
| PINCH\_GESTURE = 3 | 捏合手势。 |
| ROTATION\_GESTURE = 4 | 旋转手势。 |
| SWIPE\_GESTURE = 5 | 快滑手势。 |
| GROUP\_GESTURE = 6 | 手势组合。 |
| CLICK\_GESTURE = 7 | 通过onClick注册的点击手势。  **起始版本：** 20 |
| DRAG\_DROP = 8 | 用于拖放的拖拽手势。  **起始版本：** 20 |

### OH\_ArkUI\_GestureCollectIntervention

```c
enum OH_ArkUI_GestureCollectIntervention
```

**描述：**

定义手势和事件收集的干预操作类型。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARKUI\_GESTURE\_COLLECT\_INTERVENTION\_CONTINUE = 0 | 继续正常的手势和事件收集流程。不进行任何干预。 |
| OH\_ARKUI\_GESTURE\_COLLECT\_INTERVENTION\_DISCARD\_LOWER = 1 | 丢弃所有待收集的低优先级手势和事件。  丢弃的部分包括左侧兄弟节点以及祖先节点（父节点及以上）的手势。  仅保留当前节点和更高优先级节点中已收集的手势。 |
| OH\_ARKUI\_GESTURE\_COLLECT\_INTERVENTION\_DISCARD\_HIGHER = 2 | 丢弃已经收集到的高优先级手势和事件。  会丢弃已收集的右侧兄弟节点和当前节点上的手势。  将继续处理低优先级手势的收集流程（左侧兄弟节点和祖先节点）。 |
| OH\_ARKUI\_GESTURE\_COLLECT\_INTERVENTION\_DISCARD\_SELF = 3 | 丢弃当前节点自身的手势和事件。  当前节点的手势和事件将从手势树中排除。  兄弟节点（左侧和右侧）以及祖先节点的手势仍会继续收集。 |
| OH\_ARKUI\_GESTURE\_COLLECT\_INTERVENTION\_DISCARD\_LOWER\_PRIORITY\_SIBLINGS = 4 | 丢弃左侧兄弟节点中待收集的手势和事件。  当前节点以及已收集的右侧兄弟节点的手势和事件将被保留。  将继续处理父节点以及祖先节点的收集流程。 |

### ArkUI\_GestureInterruptResult

```c
enum ArkUI_GestureInterruptResult
```

**描述：**

定义手势打断结果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| GESTURE\_INTERRUPT\_RESULT\_CONTINUE = 0 | 手势继续。 |
| GESTURE\_INTERRUPT\_RESULT\_REJECT = 1 | 手势打断。 |

### ArkUI\_GestureRecognizerState

```c
enum ArkUI_GestureRecognizerState
```

**描述：**

定义手势识别器状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_READY = 0 | 准备状态。 |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_DETECTING = 1 | 检测状态。 |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_PENDING = 2 | 等待状态。 |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_BLOCKED = 3 | 阻塞状态。 |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_SUCCESSFUL = 4 | 成功状态。 |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_FAILED = 5 | 失败状态。 |

## 函数说明

### ArkUI\_GestureRecognizerDisposeNotifyCallback()

```c
typedef void (*ArkUI_GestureRecognizerDisposeNotifyCallback)(ArkUI_GestureRecognizer* recognizer, void* userData)
```

**描述：**

定义手势识别器析构通知事件的回调函数类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| void\* userData | 用户自定义数据。 |

### OH\_ArkUI\_GestureInterruptInfo\_GetSystemFlag()

```c
bool OH_ArkUI_GestureInterruptInfo_GetSystemFlag(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

判断是否为系统内置手势。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* event | 手势打断回调事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true: 系统内置手势；  false: 非系统内置手势。 |

### OH\_ArkUI\_GestureInterruptInfo\_GetRecognizer()

```c
ArkUI_GestureRecognizer* OH_ArkUI_GestureInterruptInfo_GetRecognizer(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

返回被打断的手势指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* event | 手势打断回调事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 被打断的手势指针。 |

### OH\_ArkUI\_GestureInterruptInfo\_GetGestureEvent()

```c
ArkUI_GestureEvent* OH_ArkUI_GestureInterruptInfo_GetGestureEvent(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

返回打断的手势事件数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* event | 手势打断回调事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* | 打断的手势事件数据。 |

### OH\_ArkUI\_GestureInterruptInfo\_GetSystemRecognizerType()

```c
int32_t OH_ArkUI_GestureInterruptInfo_GetSystemRecognizerType(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

当要触发的是系统内置手势时，使用该方法可返回该系统内置手势的类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* event | 手势打断回调事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 要触发的系统内置手势对应的手势类型，取值由[ArkUI\_GestureRecognizerType](capi-native-gesture-h.md#arkui_gesturerecognizertype)定义。如果当前触发的手势不是系统内置手势，则返回-1。 |

### OH\_ArkUI\_GestureInterruptInfo\_GetTouchRecognizers()

```c
int32_t OH_ArkUI_GestureInterruptInfo_GetTouchRecognizers(const ArkUI_GestureInterruptInfo* info,ArkUI_TouchRecognizerHandleArray* recognizers, int32_t* size)
```

**描述：**

从手势打断信息中获取触摸识别器。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* info | 指向手势打断信息的指针。 |
| [ArkUI\_TouchRecognizerHandleArray](capi-arkui-nativemodule-arkui-touchrecognizerhandlearray.md)\* recognizers | 指向触摸识别器数组的指针。 |
| int32\_t\* size | 触摸识别器数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 表示成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 表示参数错误。 |

### OH\_ArkUI\_TouchRecognizer\_GetNodeHandle()

```c
ArkUI_NodeHandle OH_ArkUI_TouchRecognizer_GetNodeHandle(const ArkUI_TouchRecognizerHandle recognizer)
```

**描述：**

获取触摸识别器对应的组件句柄。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchRecognizerHandle](capi-arkui-nativemodule-arkui-touchrecognizerhandle.md) recognizer | 触摸识别器的句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 触摸识别器对应的组件句柄。 |

### OH\_ArkUI\_TouchRecognizer\_CancelTouch()

```c
int32_t OH_ArkUI_TouchRecognizer_CancelTouch(ArkUI_TouchRecognizerHandle recognizer, ArkUI_GestureInterruptInfo* info)
```

**描述：**

在手势打断回调中向指定的触摸识别器发送取消触摸的事件。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TouchRecognizerHandle](capi-arkui-nativemodule-arkui-touchrecognizerhandle.md) recognizer | 触摸识别器的句柄。 |
| [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* info | 指向手势打断信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_GestureEvent\_GetActionType()

```c
ArkUI_GestureEventActionType OH_ArkUI_GestureEvent_GetActionType(const ArkUI_GestureEvent* event)
```

**描述：**

返回手势事件类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureEventActionType](capi-native-gesture-h.md#arkui_gestureeventactiontype) | 手势事件类型。 |

### OH\_ArkUI\_GestureEvent\_GetRawInputEvent()

```c
const ArkUI_UIInputEvent* OH_ArkUI_GestureEvent_GetRawInputEvent(const ArkUI_GestureEvent* event)
```

**描述：**

返回手势的原始输入事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const [ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* | 手势事件的原始输入事件。 |

### OH\_ArkUI\_LongPress\_GetRepeatCount()

```c
int32_t OH_ArkUI_LongPress_GetRepeatCount(const ArkUI_GestureEvent* event)
```

**描述：**

返回是否为重复触发事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 是否为重复触发事件。1表示为重复触发事件，0表示为非重复触发事件。 |

### OH\_ArkUI\_PanGesture\_GetVelocity()

```c
float OH_ArkUI_PanGesture_GetVelocity(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回手势主方向速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 当前手势主方向速度，为xy轴方向速度的平方和的算术平方根，单位px/s。 |

### OH\_ArkUI\_PanGesture\_GetVelocityX()

```c
float OH_ArkUI_PanGesture_GetVelocityX(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势的x轴方向速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 当前手势的x轴方向速度，单位px/s。 |

### OH\_ArkUI\_PanGesture\_GetVelocityY()

```c
float OH_ArkUI_PanGesture_GetVelocityY(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势的y轴方向速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 当前手势的y轴方向速度，单位px/s。 |

### OH\_ArkUI\_PanGesture\_GetOffsetX()

```c
float OH_ArkUI_PanGesture_GetOffsetX(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势事件x轴相对偏移量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 当前手势事件x轴相对偏移量，单位为px。 |

### OH\_ArkUI\_PanGesture\_GetOffsetY()

```c
float OH_ArkUI_PanGesture_GetOffsetY(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势事件y轴相对偏移量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 当前手势事件y轴相对偏移量，单位为px。 |

### OH\_ArkUI\_SwipeGesture\_GetAngle()

```c
float OH_ArkUI_SwipeGesture_GetAngle(const ArkUI_GestureEvent* event)
```

**描述：**

快滑手势返回当前手势事件角度信息，即手指滑动的瞬时方向与水平正方向的夹角。以水平正方向为基准，滑动方向位于水平正方向顺时针侧时，角度范围为0到180度；位于水平正方向逆时针侧时，角度范围为0到-180度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 快滑手势的角度，即手指滑动的瞬时方向与水平正方向的夹角，单位为deg。 |

### OH\_ArkUI\_SwipeGesture\_GetVelocity()

```c
float OH_ArkUI_SwipeGesture_GetVelocity(const ArkUI_GestureEvent* event)
```

**描述：**

快滑手势场景中所有手指滑动平均速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 快滑手势速度，即所有手指滑动的平均速度，单位为px/s。 |

### OH\_ArkUI\_RotationGesture\_GetAngle()

```c
float OH_ArkUI_RotationGesture_GetAngle(const ArkUI_GestureEvent* event)
```

**描述：**

旋转手势返回当前手势事件角度信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 旋转角度。单位为deg。 |

### OH\_ArkUI\_PinchGesture\_GetScale()

```c
float OH_ArkUI_PinchGesture_GetScale(const ArkUI_GestureEvent* event)
```

**描述：**

捏合手势返回当前手势事件缩放信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 缩放比例。 |

### OH\_ArkUI\_PinchGesture\_GetCenterX()

```c
float OH_ArkUI_PinchGesture_GetCenterX(const ArkUI_GestureEvent* event)
```

**描述：**

捏合手势中心点相对于当前组件元素左上角x轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 捏合手势中心点相对于当前组件元素左上角x轴坐标，单位为px。 |

### OH\_ArkUI\_PinchGesture\_GetCenterY()

```c
float OH_ArkUI_PinchGesture_GetCenterY(const ArkUI_GestureEvent* event)
```

**描述：**

捏合手势中心点相对于当前组件元素左上角y轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 捏合手势中心点相对于当前组件元素左上角y轴坐标，单位为px。 |

### OH\_ArkUI\_GestureEvent\_GetNode()

```c
ArkUI_NodeHandle OH_ArkUI_GestureEvent_GetNode(const ArkUI_GestureEvent* event)
```

**描述：**

获取绑定该手势的ArkUI组件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event | 手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 绑定该手势的ArkUI组件。若返回Null，则表示event是无效值。 |

### OH\_ArkUI\_GetResponseRecognizersFromInterruptInfo()

```c
int32_t OH_ArkUI_GetResponseRecognizersFromInterruptInfo(const ArkUI_GestureInterruptInfo* event,ArkUI_GestureRecognizerHandleArray* responseChain, int32_t* count)
```

**描述：**

获取手势响应链的信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* event | 手势打断回调事件。 |
| [ArkUI\_GestureRecognizerHandleArray](capi-arkui-nativemodule-arkui-gesturerecognizerhandlearray.md)\* responseChain | 响应链组件上的手势识别器。 |
| int32\_t\* count | 响应链组件上的手势识别器的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_SetGestureRecognizerEnabled()

```c
int32_t OH_ArkUI_SetGestureRecognizerEnabled(ArkUI_GestureRecognizer* recognizer, bool enabled)
```

**描述：**

设置手势识别器的使能状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| bool enabled | 使能状态。true表示使能，false表示禁用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_SetGestureRecognizerLimitFingerCount()

```c
int32_t OH_ArkUI_SetGestureRecognizerLimitFingerCount(ArkUI_GestureRecognizer* recognizer, bool limitFingerCount)
```

**描述：**

设置是否严格检查触摸手指数量的标志。实际触摸手指数量不等于设置的手指数量的时候，该手势识别不成功。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| bool limitFingerCount | 表示严格检查触摸手指数量的状态。true表示检查手指数量，false表示不检查手指数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_GetGestureRecognizerEnabled()

```c
bool OH_ArkUI_GetGestureRecognizerEnabled(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

获取手势识别器的使能状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true - 使能。  false - 禁用。 |

### OH\_ArkUI\_GetGestureRecognizerState()

```c
int32_t OH_ArkUI_GetGestureRecognizerState(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureRecognizerState* state)
```

**描述：**

获取手势识别器的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| [ArkUI\_GestureRecognizerState](capi-native-gesture-h.md#arkui_gesturerecognizerstate)\* state | 手势识别器的状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_GetGestureEventTargetInfo()

```c
int32_t OH_ArkUI_GetGestureEventTargetInfo(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureEventTargetInfo** info)
```

**描述：**

获取手势事件目标信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| [ArkUI\_GestureEventTargetInfo](capi-arkui-nativemodule-arkui-gestureeventtargetinfo.md)\*\* info | 手势事件目标信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_GestureEventTargetInfo\_IsScrollBegin()

```c
int32_t OH_ArkUI_GestureEventTargetInfo_IsScrollBegin(ArkUI_GestureEventTargetInfo* info, bool* ret)
```

**描述：**

当前滚动类容器组件是否在顶部。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureEventTargetInfo](capi-arkui-nativemodule-arkui-gestureeventtargetinfo.md)\* info | 手势事件目标信息。 |
| bool\* ret | 当前滚动类容器组件是否在顶部。true表示在顶部，false表示不在顶部。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。  [ARKUI\_ERROR\_CODE\_NON\_SCROLLABLE\_CONTAINER](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 非滚动类容器。 |

### OH\_ArkUI\_GestureEventTargetInfo\_IsScrollEnd()

```c
int32_t OH_ArkUI_GestureEventTargetInfo_IsScrollEnd(ArkUI_GestureEventTargetInfo* info, bool* ret)
```

**描述：**

当前滚动类容器组件是否在底部。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureEventTargetInfo](capi-arkui-nativemodule-arkui-gestureeventtargetinfo.md)\* info | 手势事件目标信息。 |
| bool\* ret | 当前滚动类容器组件是否在底部。true表示在底部，false表示不在底部。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。  [ARKUI\_ERROR\_CODE\_NON\_SCROLLABLE\_CONTAINER](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 非滚动类容器。 |

### OH\_ArkUI\_GetPanGestureDirectionMask()

```c
int32_t OH_ArkUI_GetPanGestureDirectionMask(ArkUI_GestureRecognizer* recognizer,ArkUI_GestureDirectionMask* directionMask)
```

**描述：**

获取滑动手势的滑动方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| [ArkUI\_GestureDirectionMask](capi-native-gesture-h.md#变量)\* directionMask | 滑动手势的滑动方向。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_IsBuiltInGesture()

```c
bool OH_ArkUI_IsBuiltInGesture(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

当前手势是否为系统内置手势。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true - 是系统内置手势。  false - 不是系统内置手势。 |

### OH\_ArkUI\_GetGestureTag()

```c
int32_t OH_ArkUI_GetGestureTag(ArkUI_GestureRecognizer* recognizer, char* buffer, int32_t bufferSize, int32_t* result)
```

**描述：**

获取手势识别器的标记。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| char\* buffer | 存储区。 |
| int32\_t bufferSize | 存储区大小。 |
| int32\_t\* result | 拷贝的字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 存储区大小不足。 |

### OH\_ArkUI\_GetGestureBindNodeId()

```c
int32_t OH_ArkUI_GetGestureBindNodeId(ArkUI_GestureRecognizer* recognizer, char* nodeId, int32_t size,int32_t* result)
```

**描述：**

获取手势识别器绑定的组件的ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| char\* nodeId | 组件的ID。 |
| int32\_t size | 存储区大小。 |
| int32\_t\* result | 拷贝的字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 存储区大小不足。 |

### OH\_ArkUI\_IsGestureRecognizerValid()

```c
bool OH_ArkUI_IsGestureRecognizerValid(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

当前手势识别器是否有效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true - 手势识别器有效。  false - 手势识别器无效。 |

### OH\_ArkUI\_ParallelInnerGestureEvent\_GetUserData()

```c
void* OH_ArkUI_ParallelInnerGestureEvent_GetUserData(ArkUI_ParallelInnerGestureEvent* event)
```

**描述：**

获取并行内置手势事件中的用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ParallelInnerGestureEvent](capi-arkui-nativemodule-arkui-parallelinnergestureevent.md)\* event | 并行内置手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 用户自定义数据的指针。 |

### OH\_ArkUI\_ParallelInnerGestureEvent\_GetCurrentRecognizer()

```c
ArkUI_GestureRecognizer* OH_ArkUI_ParallelInnerGestureEvent_GetCurrentRecognizer(ArkUI_ParallelInnerGestureEvent* event)
```

**描述：**

获取并行内置手势事件中的当前手势识别器。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ParallelInnerGestureEvent](capi-arkui-nativemodule-arkui-parallelinnergestureevent.md)\* event | 并行内置手势事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* | 当前手势识别器的指针。 |

### OH\_ArkUI\_ParallelInnerGestureEvent\_GetConflictRecognizers()

```c
int32_t OH_ArkUI_ParallelInnerGestureEvent_GetConflictRecognizers(ArkUI_ParallelInnerGestureEvent* event,ArkUI_GestureRecognizerHandleArray* array, int32_t* size)
```

**描述：**

获取并行内置手势事件中的冲突的手势识别器。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ParallelInnerGestureEvent](capi-arkui-nativemodule-arkui-parallelinnergestureevent.md)\* event | 并行内置手势事件。 |
| [ArkUI\_GestureRecognizerHandleArray](capi-arkui-nativemodule-arkui-gesturerecognizerhandlearray.md)\* array | 冲突的手势识别器数组。 |
| int32\_t\* size | 冲突的手势识别器数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_SetArkUIGestureRecognizerDisposeNotify()

```c
int32_t OH_ArkUI_SetArkUIGestureRecognizerDisposeNotify(ArkUI_GestureRecognizer* recognizer,ArkUI_GestureRecognizerDisposeNotifyCallback callback, void* userData)
```

**描述：**

设置手势识别器对象析构通知回调函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| [ArkUI\_GestureRecognizerDisposeNotifyCallback](capi-native-gesture-h.md#arkui_gesturerecognizerdisposenotifycallback) callback | 手势识别器对象析构通知回调函数。 |
| void\* userData | 用户自定义数据，会在手势识别器对象析构通知回调callback中透传给调用方。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) - 参数错误。 |

### OH\_ArkUI\_GetGestureParam\_DirectMask()

```c
int32_t OH_ArkUI_GetGestureParam_DirectMask(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureDirectionMask* directMask)
```

**描述：**

获取手势识别器的滑动方向。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| [ArkUI\_GestureDirectionMask](capi-native-gesture-h.md#变量)\* directMask | 手势识别器的滑动方向。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_GetGestureParam\_FingerCount()

```c
int32_t OH_ArkUI_GetGestureParam_FingerCount(ArkUI_GestureRecognizer* recognizer, int* finger)
```

**描述：**

获取手势识别器的手指数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| int\* finger | 手势识别器的手指数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_GetGestureParam\_limitFingerCount()

```c
int32_t OH_ArkUI_GetGestureParam_limitFingerCount(ArkUI_GestureRecognizer* recognizer, bool* isLimited)
```

**描述：**

获取手势识别器是否有手指数限制。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| bool\* isLimited | 手势识别器是否有手指数限制。true表示有手指数限制，false表示没有手指数限制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_GetGestureParam\_repeat()

```c
int32_t OH_ArkUI_GetGestureParam_repeat(ArkUI_GestureRecognizer* recognizer, bool* isRepeat)
```

**描述：**

获取手势识别器是否连续触发事件回调。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| bool\* isRepeat | 手势识别器是否连续触发事件回调。true表示连续触发，false表示不连续触发。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_GetGestureParam\_distance()

```c
int32_t OH_ArkUI_GetGestureParam_distance(ArkUI_GestureRecognizer* recognizer, double* distance)
```

**描述：**

获取手势识别器的手指允许的移动距离范围。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| double\* distance | 手势识别器的手指允许的移动距离范围。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_GetGestureParam\_speed()

```c
int32_t OH_ArkUI_GetGestureParam_speed(ArkUI_GestureRecognizer* recognizer, double* speed)
```

**描述：**

获取手势识别器的识别滑动的最小速度。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| double\* speed | 手势识别器的识别滑动的最小速度。单位为px/s。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_GetGestureParam\_duration()

```c
int32_t OH_ArkUI_GetGestureParam_duration(ArkUI_GestureRecognizer* recognizer, int* duration)
```

**描述：**

获取手势识别器的触发长按的最短时间。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| int\* duration | 手势识别器的触发长按的最短时间。单位为ms。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_GetGestureParam\_angle()

```c
int32_t OH_ArkUI_GetGestureParam_angle(ArkUI_GestureRecognizer* recognizer, double* angle)
```

**描述：**

获取手势识别器的旋转手势的最小改变度数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| double\* angle | 手势识别器的旋转手势的最小改变度数。单位为deg。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_GetGestureParam\_distanceThreshold()

```c
int32_t OH_ArkUI_GetGestureParam_distanceThreshold(ArkUI_GestureRecognizer* recognizer, double* distanceThreshold)
```

**描述：**

获取手势识别器的手势移动阈值。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| double\* distanceThreshold | 手势识别器的手势移动阈值。单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_PanGesture\_SetDistanceMap()

```c
ArkUI_ErrorCode OH_ArkUI_PanGesture_SetDistanceMap(ArkUI_GestureRecognizer* recognizer, int size, int* toolTypeArray, double* distanceArray)
```

**描述：**

设置手势最小滑动阈值表，用于需要根据不同输入工具类型配置滑动手势识别阈值的场景。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| int size | toolTypeArray和distanceArray数组的元素个数。 |
| int\* toolTypeArray | 指向输入事件工具类型数组的指针，元素取值为[UI\_INPUT\_EVENT\_TOOL\_TYPE](capi-ui-input-event-h.md#anonymous2)\_XXX；当设置该范围以外的值时，设置不生效。 |
| double\* distanceArray | 指向最小滑动阈值数组的指针，取值范围为[0, +∞)，单位为px。传入负数时，设置不生效。distanceArray[i]表示toolTypeArray[i]对应工具类型的最小滑动阈值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。  返回 [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_PanGesture\_GetDistanceByToolType()

```c
ArkUI_ErrorCode OH_ArkUI_PanGesture_GetDistanceByToolType(ArkUI_GestureRecognizer* recognizer, int toolType, double* distance)
```

**描述：**

获取手势识别器的手势移动阈值表。仅支持对通过OH\_ArkUI\_PanGesture\_SetDistanceMap修改过的设备类型的阈值查询。默认滑动阈值可通过查询[UI\_INPUT\_EVENT\_TOOL\_TYPE\_UNKNOWN](capi-ui-input-event-h.md#anonymous2)类型获得，其他未设置过的类型不会返回对应的滑动阈值。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| int toolType | 输入事件的工具类型。 |
| double\* distance | 手势识别器的手势移动阈值。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。  返回 [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_SetTouchTestDoneCallback()

```c
ArkUI_ErrorCode OH_ArkUI_SetTouchTestDoneCallback(ArkUI_NodeHandle node, void* userData, void (*touchTestDone)(ArkUI_GestureEvent* event, ArkUI_GestureRecognizerHandleArray recognizers, int32_t count, void* userData))
```

**描述：**

注册一个在所有手势识别器收集完成后执行的回调函数。当用户开始触摸屏幕时，系统会进行命中测试并根据触摸位置收集手势识别器。随后，在处理任何移动事件之前，组件可以使用此接口确定将参与识别并相互竞争的手势识别器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要设置手势收集完成回调的节点句柄。 |
| void\* userData | 用户自定义数据，会在touchTestDone回调中作为userData参数透传给调用方。 |
| void (\*touchTestDone)([ArkUI\_GestureEvent](capi-arkui-nativemodule-arkui-gestureevent.md)\* event, [ArkUI\_GestureRecognizerHandleArray](capi-arkui-nativemodule-arkui-gesturerecognizerhandlearray.md) recognizers, int32\_t count, void\* userData) | 手势收集完成的回调函数。event为手势的基本信息，recognizers为手势识别器数组，count为手势识别器个数，userData为用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_GestureInterrupter\_GetUserData()

```c
void* OH_ArkUI_GestureInterrupter_GetUserData(ArkUI_GestureInterruptInfo* event)
```

**描述：**

获取手势中断事件中的用户自定义数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* event | 是指向手势中断信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 返回指向用户自定义数据的指针。 |

### OH\_ArkUI\_PreventGestureRecognizerBegin()

```c
ArkUI_ErrorCode OH_ArkUI_PreventGestureRecognizerBegin(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

在手指全部抬起前阻止手势识别器参与当前手势识别，适用于需要在手势竞争过程中动态排除指定手势识别器的场景。如果系统已确定该手势识别器的结果（无论成功与否），调用此接口将无效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  返回 [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_LongPressGesture\_SetAllowableMovement()

```c
ArkUI_ErrorCode OH_ArkUI_LongPressGesture_SetAllowableMovement(ArkUI_GestureRecognizer* recognizer, double allowableMovement)
```

**描述：**

设置长按手势识别器识别的手势的最大移动距离。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| double allowableMovement | 长按手势识别器识别的手势的最大移动距离。  单位为px。  取值范围：(0, +∞)，设置小于等于0时，按照默认值15处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_LongPressGesture\_GetAllowableMovement()

```c
ArkUI_ErrorCode OH_ArkUI_LongPressGesture_GetAllowableMovement(ArkUI_GestureRecognizer* recognizer, double* allowableMovement)
```

**描述：**

获取长按手势识别器识别的手势的最大移动距离。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 手势识别器指针。 |
| double\* allowableMovement | 指向长按手势识别器识别的手势的最大移动距离的指针，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。  [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 不支持手势识别器类型。 |

### OH\_ArkUI\_GestureCollectInterceptInfo\_GetResponseRecognizers()

```c
ArkUI_ErrorCode OH_ArkUI_GestureCollectInterceptInfo_GetResponseRecognizers(const ArkUI_GestureCollectInterceptInfo* info, ArkUI_GestureRecognizerHandleArray* array, int32_t* size)
```

**描述：**

从手势收集拦截信息中获取手势识别器。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureCollectInterceptInfo](capi-arkui-nativemodule-arkui-gesturecollectinterceptinfo.md)\* info | 表示指向手势收集拦截信息的指针。 |
| [ArkUI\_GestureRecognizerHandleArray](capi-arkui-nativemodule-arkui-gesturerecognizerhandlearray.md)\* array | 表示响应手势识别器数组的指针。 |
| int32\_t\* size | 表示响应手势识别器数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示成功。  返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示发生参数异常。 |

### OH\_ArkUI\_GestureCollectInterceptInfo\_GetTouchRecognizers()

```c
ArkUI_ErrorCode OH_ArkUI_GestureCollectInterceptInfo_GetTouchRecognizers(const ArkUI_GestureCollectInterceptInfo* info, ArkUI_TouchRecognizerHandleArray* recognizers, int32_t* size)
```

**描述：**

从手势收集拦截信息中获取触摸识别器句柄。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureCollectInterceptInfo](capi-arkui-nativemodule-arkui-gesturecollectinterceptinfo.md)\* info | 表示指向手势收集拦截信息的指针。 |
| [ArkUI\_TouchRecognizerHandleArray](capi-arkui-nativemodule-arkui-touchrecognizerhandlearray.md)\* recognizers | 表示触摸识别器句柄数组的指针。 |
| int32\_t\* size | 表示recognizers数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示成功。  返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示发生参数异常。 |

### OH\_ArkUI\_GestureCollectInterceptInfo\_SetGestureCollectIntervention()

```c
ArkUI_ErrorCode OH_ArkUI_GestureCollectInterceptInfo_SetGestureCollectIntervention(ArkUI_GestureCollectInterceptInfo* info, OH_ArkUI_GestureCollectIntervention intervention)
```

**描述：**

设置手势收集干预模式。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GestureCollectInterceptInfo](capi-arkui-nativemodule-arkui-gesturecollectinterceptinfo.md)\* info | 手势收集拦截信息指针。 |
| [OH\_ArkUI\_GestureCollectIntervention](capi-native-gesture-h.md#oh_arkui_gesturecollectintervention) intervention | 手势收集干预模式，类型为[OH\_ArkUI\_GestureCollectIntervention](capi-native-gesture-h.md#oh_arkui_gesturecollectintervention)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 如果成功，则返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  参数异常返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_GetGestureBindNodeUniqueId()

```c
ArkUI_ErrorCode OH_ArkUI_GetGestureBindNodeUniqueId(const ArkUI_GestureRecognizer* recognizer, int32_t* uniqueId)
```

**描述：**

获取与手势识别器绑定的组件唯一ID。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 表示指向手势识别器的指针。 |
| int32\_t\* uniqueId | 表示与手势识别器绑定的组件唯一ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示成功。  返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示发生参数异常。 |

### OH\_ArkUI\_TouchRecognizer\_IsHostBelongsTo()

```c
bool OH_ArkUI_TouchRecognizer_IsHostBelongsTo(const ArkUI_TouchRecognizerHandle recognizer, int32_t uniqueId)
```

**描述：**

检查当前触摸识别器绑定节点是否为传入组件的后代节点。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TouchRecognizerHandle](capi-arkui-nativemodule-arkui-touchrecognizerhandle.md) recognizer | 表示触摸识别器句柄。 |
| int32\_t uniqueId | 表示组件的唯一ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果当前触摸识别器绑定节点是传入组件的后代，则返回true，否则返回false。 |

### OH\_ArkUI\_GestureRecognizer\_IsHostBelongsTo()

```c
bool OH_ArkUI_GestureRecognizer_IsHostBelongsTo(const ArkUI_GestureRecognizer* recognizer, int32_t uniqueId)
```

**描述：**

检查当前手势识别器绑定节点是否为传入组件的后代节点。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_GestureRecognizer](capi-arkui-nativemodule-arkui-gesturerecognizer.md)\* recognizer | 表示指向手势识别器的指针。 |
| int32\_t uniqueId | 表示组件的唯一ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果当前手势绑定节点是传入组件的后代，则返回true，否则返回false。 |
