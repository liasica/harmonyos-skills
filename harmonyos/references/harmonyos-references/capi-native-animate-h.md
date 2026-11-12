---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h
title: native_animate.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_animate.h
category: harmonyos-references
scraped_at: 2026-11-12T09:54:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1e81797f17756db53ee3f9229e1002fe2897c8b260721b14676bbf4f35d0f6c6
---

## 概述

提供ArkUI（方舟UI框架）在Native侧的动画接口定义集合。native\_animate.h中的接口需要在主线程上调用。

**引用文件：** <arkui/native\_animate.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [AnimationNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/AnimationNDK)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md) | ArkUI\_ExpectedFrameRateRange | 设置动画的期望帧率。该结构体通过min、max和expected三个字段定义帧率范围，系统尽可能满足期望帧率。 |
| [ArkUI\_AnimateCompleteCallback](capi-arkui-nativemodule-arkui-animatecompletecallback.md) | ArkUI\_AnimateCompleteCallback | 动画播放结束回调类型，用于在动画播放完成时通知开发者动画已结束。开发者可通过type字段指定回调触发方式，通过callback字段设置自定义回调函数，并通过userData字段传递自定义数据至回调函数中。 |
| [ArkUI\_NativeAnimateAPI\_1](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md) | ArkUI\_NativeAnimateAPI\_1 | ArkUI（方舟UI框架）提供的Native侧动画接口集合。 |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md) | ArkUI\_AnimateOption | 定义动画效果的配置参数，用于配置动画的相关属性。 |
| [ArkUI\_Curve](capi-arkui-nativemodule-arkui-curve.md) | ArkUI\_Curve | 提供动画曲线的插值对象定义，用于动画属性值的插值计算。 |
| [ArkUI\_Curve\*](capi-arkui-nativemodule-arkui-curve8h.md) | ArkUI\_CurveHandle | 曲线插值对象的指针类型定义。曲线插值用于控制动画属性值随时间的变化规律，不同类型的插值曲线可实现不同的动画过渡效果。 |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md) | ArkUI\_KeyframeAnimateOption | 定义关键帧动画参数对象，作为关键帧动画接口的输入参数使用。相关接口需要在主线程上调用。 |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md) | ArkUI\_AnimatorOption | 定义animator动画参数对象，用于创建animator动画时配置动画属性参数。 |
| [ArkUI\_Animator\*](capi-arkui-nativemodule-arkui-animator8h.md) | ArkUI\_AnimatorHandle | 定义animator动画对象指针，用于对ArkUI（方舟UI框架）动画对象进行操作和控制。 |
| [ArkUI\_AnimatorEvent](capi-arkui-nativemodule-arkui-animatorevent.md) | ArkUI\_AnimatorEvent | 定义animator回调事件对象，用于在动画状态变化回调中接收事件。 |
| [ArkUI\_AnimatorOnFrameEvent](capi-arkui-nativemodule-arkui-animatoronframeevent.md) | ArkUI\_AnimatorOnFrameEvent | 定义animator动画播放过程中逐帧回调的事件数据对象。 |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md) | ArkUI\_TransitionEffect | 定义transition属性的转场效果参数对象，用于配置组件出现或消失时的过渡动画效果。 |
| [OH\_ArkUI\_PropertyAnimation\*](capi-arkui-nativemodule-arkui-propertyanimation8h.md) | OH\_ArkUI\_PropertyAnimationHandle | 定义属性动画的句柄。 |
| [OH\_ArkUI\_KeyframeAnimation\*](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) | OH\_ArkUI\_KeyframeAnimationHandle | 定义关键帧动画的句柄。 |
| [OH\_ArkUI\_PathAnimation\*](capi-arkui-nativemodule-arkui-pathanimation8h.md) | OH\_ArkUI\_PathAnimationHandle | 定义路径动画的句柄。 |
| [OH\_ArkUI\_AnimationGroup\*](capi-arkui-nativemodule-arkui-animationgroup8h.md) | OH\_ArkUI\_AnimationGroupHandle | 定义动画组的句柄。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption\* OH\_ArkUI\_AnimateOption\_Create()](capi-native-animate-h.md#oh_arkui_animateoption_create) | 创建动画效果参数。 |
| [void OH\_ArkUI\_AnimateOption\_Dispose(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_dispose) | 销毁动画效果参数指针。 |
| [uint32\_t OH\_ArkUI\_AnimateOption\_GetDuration(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_getduration) | 获取动画持续时间，单位为ms（毫秒）。 |
| [float OH\_ArkUI\_AnimateOption\_GetTempo(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_gettempo) | 获取动画播放速率。 |
| [ArkUI\_AnimationCurve OH\_ArkUI\_AnimateOption\_GetCurve(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_getcurve) | 获取动画曲线。 |
| [int32\_t OH\_ArkUI\_AnimateOption\_GetDelay(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_getdelay) | 获取动画延迟播放时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimateOption\_GetIterations(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_getiterations) | 获取动画播放次数。 |
| [ArkUI\_AnimationPlayMode OH\_ArkUI\_AnimateOption\_GetPlayMode(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_getplaymode) | 获取动画播放模式。 |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimateOption\_GetExpectedFrameRateRange(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_getexpectedframeraterange) | 获取动画的期望帧率。 |
| [void OH\_ArkUI\_AnimateOption\_SetDuration(ArkUI\_AnimateOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_animateoption_setduration) | 设置动画持续时间，单位为ms（毫秒）。 |
| [void OH\_ArkUI\_AnimateOption\_SetTempo(ArkUI\_AnimateOption\* option, float value)](capi-native-animate-h.md#oh_arkui_animateoption_settempo) | 设置动画播放速率。 |
| [void OH\_ArkUI\_AnimateOption\_SetCurve(ArkUI\_AnimateOption\* option, ArkUI\_AnimationCurve value)](capi-native-animate-h.md#oh_arkui_animateoption_setcurve) | 设置动画的自定义曲线。 |
| [void OH\_ArkUI\_AnimateOption\_SetDelay(ArkUI\_AnimateOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_animateoption_setdelay) | 设置动画延迟播放时间，单位为ms（毫秒）。 |
| [void OH\_ArkUI\_AnimateOption\_SetIterations(ArkUI\_AnimateOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_animateoption_setiterations) | 设置动画播放次数。 |
| [void OH\_ArkUI\_AnimateOption\_SetPlayMode(ArkUI\_AnimateOption\* option, ArkUI\_AnimationPlayMode value)](capi-native-animate-h.md#oh_arkui_animateoption_setplaymode) | 设置动画播放模式。 |
| [void OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange(ArkUI\_AnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* value)](capi-native-animate-h.md#oh_arkui_animateoption_setexpectedframeraterange) | 设置动画的期望帧率。 |
| [void OH\_ArkUI\_AnimateOption\_SetICurve(ArkUI\_AnimateOption\* option, ArkUI\_CurveHandle value)](capi-native-animate-h.md#oh_arkui_animateoption_seticurve) | 设置动画的插值曲线。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimateOption\_GetICurve(ArkUI\_AnimateOption\* option)](capi-native-animate-h.md#oh_arkui_animateoption_geticurve) | 获取动画的插值曲线。 |
| [ArkUI\_KeyframeAnimateOption\* OH\_ArkUI\_KeyframeAnimateOption\_Create(int32\_t size)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_create) | 创建关键帧动画参数。 |
| [void OH\_ArkUI\_KeyframeAnimateOption\_Dispose(ArkUI\_KeyframeAnimateOption\* option)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_dispose) | 销毁关键帧动画参数。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDelay(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_setdelay) | 设置关键帧动画的整体延迟时间，单位为ms（毫秒），默认不延迟播放。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetIterations(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_setiterations) | 设置关键帧动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*onFinish)(void\* userData))](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_registeronfinishcallback) | 设置关键帧动画播放完成回调。当关键帧动画[ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)所有次数播放完成后调用。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* frameRate)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_setexpectedframerate) | 设置关键帧动画期望帧率。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t value, int32\_t index)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_setduration) | 设置关键帧动画某段关键帧动画的持续时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetCurve(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_CurveHandle value, int32\_t index)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_setcurve) | 设置关键帧动画某段关键帧使用的动画曲线。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*event)(void\* userData), int32\_t index)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_registeroneventcallback) | 设置关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDelay(ArkUI\_KeyframeAnimateOption\* option)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_getdelay) | 获取关键帧整体延迟时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetIterations(ArkUI\_KeyframeAnimateOption\* option)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_getiterations) | 获取关键帧动画播放次数。 |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_getexpectedframerate) | 获取关键帧动画参数的期望帧率。 |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_getduration) | 获取关键帧动画某段状态持续时间，单位为ms（毫秒）。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_KeyframeAnimateOption\_GetCurve(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)](capi-native-animate-h.md#oh_arkui_keyframeanimateoption_getcurve) | 获取关键帧动画某段状态动画曲线。 |
| [ArkUI\_AnimatorOption\* OH\_ArkUI\_AnimatorOption\_Create(int32\_t keyframeSize)](capi-native-animate-h.md#oh_arkui_animatoroption_create) | 创建animator动画对象参数。 |
| [void OH\_ArkUI\_AnimatorOption\_Dispose(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_dispose) | 销毁animator动画对象参数。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDuration(ArkUI\_AnimatorOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_animatoroption_setduration) | 设置animator动画播放的时长，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDelay(ArkUI\_AnimatorOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_animatoroption_setdelay) | 设置animator动画延迟播放的时间，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetIterations(ArkUI\_AnimatorOption\* option, int32\_t value)](capi-native-animate-h.md#oh_arkui_animatoroption_setiterations) | 设置animator动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetFill(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationFillMode value)](capi-native-animate-h.md#oh_arkui_animatoroption_setfill) | 设置组件在动画开始前和结束后保持的状态。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDirection(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationDirection value)](capi-native-animate-h.md#oh_arkui_animatoroption_setdirection) | 设置animator动画播放方向。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value)](capi-native-animate-h.md#oh_arkui_animatoroption_setcurve) | 设置animator动画插值曲线。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetBegin(ArkUI\_AnimatorOption\* option, float value)](capi-native-animate-h.md#oh_arkui_animatoroption_setbegin) | 设置animator动画插值起点。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetEnd(ArkUI\_AnimatorOption\* option, float value)](capi-native-animate-h.md#oh_arkui_animatoroption_setend) | 设置animator动画插值终点。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option, ArkUI\_ExpectedFrameRateRange\* value)](capi-native-animate-h.md#oh_arkui_animatoroption_setexpectedframeraterange) | 设置animator动画期望的帧率范围。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframe(ArkUI\_AnimatorOption\* option, float time, float value, int32\_t index)](capi-native-animate-h.md#oh_arkui_animatoroption_setkeyframe) | 设置animator动画关键帧参数。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value, int32\_t index)](capi-native-animate-h.md#oh_arkui_animatoroption_setkeyframecurve) | 设置animator动画关键帧曲线类型。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetDuration(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getduration) | 获取animator动画播放的时长，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetDelay(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getdelay) | 获取animator动画延迟播放时长，单位为ms（毫秒）。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetIterations(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getiterations) | 获取animator动画播放次数。 |
| [ArkUI\_AnimationFillMode OH\_ArkUI\_AnimatorOption\_GetFill(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getfill) | 获取animator动画执行时组件在动画开始前和结束后的状态。 |
| [ArkUI\_AnimationDirection OH\_ArkUI\_AnimatorOption\_GetDirection(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getdirection) | 获取animator动画播放方向。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetCurve(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getcurve) | 获取animator动画插值曲线。 |
| [float OH\_ArkUI\_AnimatorOption\_GetBegin(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getbegin) | 获取animator动画插值起点。当Animator动画为关键帧动画时，此方法返回的值无实际意义。 |
| [float OH\_ArkUI\_AnimatorOption\_GetEnd(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getend) | 获取animator动画插值终点。当Animator动画为关键帧动画时，此方法返回的值无实际意义。 |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animatoroption_getexpectedframeraterange) | 获取animator动画期望的帧率范围。 |
| [float OH\_ArkUI\_AnimatorOption\_GetKeyframeTime(ArkUI\_AnimatorOption\* option, int32\_t index)](capi-native-animate-h.md#oh_arkui_animatoroption_getkeyframetime) | 获取animator动画关键帧时间，单位为ms（毫秒）。 |
| [float OH\_ArkUI\_AnimatorOption\_GetKeyframeValue(ArkUI\_AnimatorOption\* option, int32\_t index)](capi-native-animate-h.md#oh_arkui_animatoroption_getkeyframevalue) | 获取animator动画在该关键帧位置的插值目标值。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve(ArkUI\_AnimatorOption\* option, int32\_t index)](capi-native-animate-h.md#oh_arkui_animatoroption_getkeyframecurve) | 获取animator动画关键帧动画插值曲线。 |
| [void\* OH\_ArkUI\_AnimatorEvent\_GetUserData(ArkUI\_AnimatorEvent\* event)](capi-native-animate-h.md#oh_arkui_animatorevent_getuserdata) | 获取动画事件对象中的用户自定义对象。 |
| [void\* OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData(ArkUI\_AnimatorOnFrameEvent\* event)](capi-native-animate-h.md#oh_arkui_animatoronframeevent_getuserdata) | 获取动画的帧事件中的用户自定义对象。 |
| [float OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue(ArkUI\_AnimatorOnFrameEvent\* event)](capi-native-animate-h.md#oh_arkui_animatoronframeevent_getvalue) | 获取动画帧回调事件对象中的插值结果。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorOnFrameEvent\* event))](capi-native-animate-h.md#oh_arkui_animatoroption_registeronframecallback) | 设置animator动画接收到帧时回调。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](capi-native-animate-h.md#oh_arkui_animatoroption_registeronfinishcallback) | 设置animator动画完成时回调。当animator动画所有次数播放完成后调用，或调用[OH\_ArkUI\_Animator\_Finish](capi-native-animate-h.md#oh_arkui_animator_finish)结束时也会触发。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](capi-native-animate-h.md#oh_arkui_animatoroption_registeroncancelcallback) | 设置animator动画被取消时回调。 |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](capi-native-animate-h.md#oh_arkui_animatoroption_registeronrepeatcallback) | 设置animator动画重复时回调。 |
| [int32\_t OH\_ArkUI\_Animator\_ResetAnimatorOption(ArkUI\_AnimatorHandle animatorHandle, ArkUI\_AnimatorOption\* option)](capi-native-animate-h.md#oh_arkui_animator_resetanimatoroption) | 重置animator动画的配置参数。 |
| [int32\_t OH\_ArkUI\_Animator\_Play(ArkUI\_AnimatorHandle animatorHandle)](capi-native-animate-h.md#oh_arkui_animator_play) | 启动animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Finish(ArkUI\_AnimatorHandle animatorHandle)](capi-native-animate-h.md#oh_arkui_animator_finish) | 结束animator动画，动画将跳到终点状态。与OH\_ArkUI\_Animator\_Cancel的区别：Finish使动画完成至终点状态，Cancel中断动画并回到初始状态。 |
| [int32\_t OH\_ArkUI\_Animator\_Pause(ArkUI\_AnimatorHandle animatorHandle)](capi-native-animate-h.md#oh_arkui_animator_pause) | 暂停animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Cancel(ArkUI\_AnimatorHandle animatorHandle)](capi-native-animate-h.md#oh_arkui_animator_cancel) | 取消animator动画。 |
| [int32\_t OH\_ArkUI\_Animator\_Reverse(ArkUI\_AnimatorHandle animatorHandle)](capi-native-animate-h.md#oh_arkui_animator_reverse) | 以相反的顺序播放animator动画。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCurveByType(ArkUI\_AnimationCurve curve)](capi-native-animate-h.md#oh_arkui_curve_createcurvebytype) | 插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateStepsCurve(int32\_t count, bool end)](capi-native-animate-h.md#oh_arkui_curve_createstepscurve) | 构造阶梯曲线对象。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)](capi-native-animate-h.md#oh_arkui_curve_createcubicbeziercurve) | 构造三阶贝塞尔曲线对象。动画时长受动画参数中的时长参数控制。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)](capi-native-animate-h.md#oh_arkui_curve_createspringcurve) | 构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受动画参数中的时长参数控制。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)](capi-native-animate-h.md#oh_arkui_curve_createspringmotion) | 构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换前一个动画，并继承之前的速度。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)](capi-native-animate-h.md#oh_arkui_curve_createresponsivespringmotion) | 构造弹性跟手动画曲线对象，是springMotion的一种特例，仅默认参数不同，可与springMotion混合使用。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换前一个动画，并继承之前的速度。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)](capi-native-animate-h.md#oh_arkui_curve_createinterpolatingspring) | 构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。 |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCustomCurve(void\* userData, float (\*interpolate)(float fraction, void\* userdata))](capi-native-animate-h.md#oh_arkui_curve_createcustomcurve) | 构造自定义曲线对象。 |
| [void OH\_ArkUI\_Curve\_DisposeCurve(ArkUI\_CurveHandle curveHandle)](capi-native-animate-h.md#oh_arkui_curve_disposecurve) | 销毁自定义曲线对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateOpacityTransitionEffect(float opacity)](capi-native-animate-h.md#oh_arkui_createopacitytransitioneffect) | 创建组件转场时的透明度效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateTranslationTransitionEffect(ArkUI\_TranslationOptions\* translate)](capi-native-animate-h.md#oh_arkui_createtranslationtransitioneffect) | 创建组件转场时的平移效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateScaleTransitionEffect(ArkUI\_ScaleOptions\* scale)](capi-native-animate-h.md#oh_arkui_createscaletransitioneffect) | 创建组件转场时的缩放效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateRotationTransitionEffect(ArkUI\_RotationOptions\* rotate)](capi-native-animate-h.md#oh_arkui_createrotationtransitioneffect) | 创建组件转场时的旋转效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateMovementTransitionEffect(ArkUI\_TransitionEdge edge)](capi-native-animate-h.md#oh_arkui_createmovementtransitioneffect) | 创建组件平移效果对象，用于组件从指定边缘滑入或滑出的转场效果，适用于仅需指定滑动方向的简单场景。与[OH\_ArkUI\_CreateTranslationTransitionEffect](capi-native-animate-h.md#oh_arkui_createtranslationtransitioneffect)不同：后者支持自定义x/y/z方向的精确平移参数，适用于需要指定具体位移距离的场景。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateAsymmetricTransitionEffect(ArkUI\_TransitionEffect\* appear, ArkUI\_TransitionEffect\* disappear)](capi-native-animate-h.md#oh_arkui_createasymmetrictransitioneffect) | 创建非对称的转场效果对象。 |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateIdentityTransitionEffect(void)](capi-native-animate-h.md#oh_arkui_createidentitytransitioneffect) | 创建无转场效果对象。 |
| [void OH\_ArkUI\_TransitionEffect\_Dispose(ArkUI\_TransitionEffect\* effect)](capi-native-animate-h.md#oh_arkui_transitioneffect_dispose) | 销毁转场效果对象。 |
| [int32\_t OH\_ArkUI\_TransitionEffect\_Combine(ArkUI\_TransitionEffect\* firstEffect, ArkUI\_TransitionEffect\* secondEffect)](capi-native-animate-h.md#oh_arkui_transitioneffect_combine) | 设置转场效果链式组合，以形成包含多种转场效果的TransitionEffect。 |
| [int32\_t OH\_ArkUI\_TransitionEffect\_SetAnimation(ArkUI\_TransitionEffect\* effect, ArkUI\_AnimateOption\* animation)](capi-native-animate-h.md#oh_arkui_transitioneffect_setanimation) | 设置转场效果动画参数。 |
| [OH\_ArkUI\_PropertyAnimationHandle OH\_ArkUI\_NativeModule\_PropertyAnimation\_Create(OH\_ArkUI\_AnimationPropertyType propertyType)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_create) | 为指定的可动画属性创建属性动画。  propertyType必须是有效的[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，否则本接口返回NULL。 |
| [void OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy(OH\_ArkUI\_PropertyAnimationHandle animation)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy) | 销毁属性动画。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetFromValue(OH\_ArkUI\_PropertyAnimationHandle animation, const ArkUI\_NumberValue \*value, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setfromvalue) | 设置属性动画的起始值。  推荐设置起始值，若未设置则默认从当前属性值开始产生动画。如果未设置起始值且对应属性从未被赋值，由于缺少有效的起始状态，属性动画将无法产生。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetFromValue(OH\_ArkUI\_PropertyAnimationHandle animation, ArkUI\_NumberValue \*value, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_getfromvalue) | 获取属性动画的起始值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetToValue(OH\_ArkUI\_PropertyAnimationHandle animation, const ArkUI\_NumberValue \*value, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settovalue) | 设置属性动画的结束值。  必须设置结束值，否则属性动画句柄无实际意义。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetToValue(OH\_ArkUI\_PropertyAnimationHandle animation, ArkUI\_NumberValue \*value, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_gettovalue) | 获取属性动画的结束值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration(OH\_ArkUI\_PropertyAnimationHandle animation, int32\_t duration)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setduration) | 设置属性动画的持续时间。  实际生效的动画持续时间按以下优先级确定：如果通过本接口设置了子动画的持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)在动画组上设置的持续时间；如果两者都未设置，则使用默认值1000毫秒。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetDuration(OH\_ArkUI\_PropertyAnimationHandle animation, int32\_t \*duration)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_getduration) | 获取属性动画的持续时间。  本接口仅返回在本动画上显式设置的持续时间；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时实际生效的动画持续时间按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setduration)设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)设置的动画组持续时间；如果两者都未设置，则使用默认值1000毫秒。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDelay(OH\_ArkUI\_PropertyAnimationHandle animation, int32\_t delay)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setdelay) | 设置属性动画的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetDelay(OH\_ArkUI\_PropertyAnimationHandle animation, int32\_t \*delay)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_getdelay) | 获取属性动画的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetCurve(OH\_ArkUI\_PropertyAnimationHandle animation, ArkUI\_CurveHandle curve)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setcurve) | 设置属性动画的动画曲线。  实际生效的动画曲线按以下优先级确定：如果通过本接口设置了曲线，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)在动画组上设置的曲线；如果两者都未设置，则使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。支持弹簧曲线（springMotion、responsiveSpringMotion和interpolatingSpring）。设置弹簧曲线时，通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setduration)设置的持续时间不生效，动画持续时间由弹簧曲线决定。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetCurve(OH\_ArkUI\_PropertyAnimationHandle animation, ArkUI\_CurveHandle \*outBorrowedCurve)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_getcurve) | 获取属性动画的动画曲线。  本接口仅返回在本动画上显式设置的曲线；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置曲线，则outBorrowedCurve输出为NULL。运行时实际生效的动画曲线按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setcurve)设置了曲线，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)设置的动画组曲线；如果两者都未设置，则使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTempo(OH\_ArkUI\_PropertyAnimationHandle animation, float tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settempo) | 设置属性动画的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetTempo(OH\_ArkUI\_PropertyAnimationHandle animation, float \*tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_gettempo) | 获取属性动画的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetAutoReverse(OH\_ArkUI\_PropertyAnimationHandle animation, bool autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setautoreverse) | 设置属性动画是否自动反转。  启用自动反转后，动画在每轮播放中交替正向播放和反向播放。默认值为false。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetAutoReverse(OH\_ArkUI\_PropertyAnimationHandle animation, bool \*autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_getautoreverse) | 获取属性动画是否启用自动反转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetIterations(OH\_ArkUI\_PropertyAnimationHandle animation, int32\_t iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setiterations) | 设置属性动画的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetIterations(OH\_ArkUI\_PropertyAnimationHandle animation, int32\_t \*iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_getiterations) | 获取属性动画的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode(OH\_ArkUI\_PropertyAnimationHandle animation, ArkUI\_RenderNodeHandle targetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settargetnode) | 设置属性动画的目标渲染节点。  目标节点是被该属性动画驱动的渲染节点。如果为NULL（默认值），则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。非NULL目标必须属于动画组注册的同一UIContext，该检查在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时执行。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetTargetNode(OH\_ArkUI\_PropertyAnimationHandle animation, ArkUI\_RenderNodeHandle \*outBorrowedTargetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_gettargetnode) | 获取属性动画的目标渲染节点。 |
| [OH\_ArkUI\_KeyframeAnimationHandle OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Create(OH\_ArkUI\_AnimationPropertyType propertyType, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create) | 为指定的可动画属性创建关键帧动画。  每个关键帧的关键帧时间点默认按索引在[0, 1]区间均匀分布（例如，当有3个关键帧时，第一帧为0.0，第二帧为0.5，第三帧为1.0）。使用[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTimes](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setkeytimes)或[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTime](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setkeytime)自定义关键帧时间点。  propertyType必须是有效的[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，且size必须大于等于2；否则，本接口返回NULL。 |
| [void OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy(OH\_ArkUI\_KeyframeAnimationHandle animation)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy) | 销毁关键帧动画。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTimes(OH\_ArkUI\_KeyframeAnimationHandle animation, const float \*keyTimes, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setkeytimes) | 设置关键帧的关键帧时间点。  如果不调用本接口，每个关键帧的关键帧时间点默认按索引在[0, 1]区间均匀分布（例如，当有3个关键帧时，第一帧为0.0，第二帧为0.5，第三帧为1.0）。  keyTimes中的元素必须非递减，且size必须等于关键帧动画的关键帧数量（即通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Create](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create)创建动画时指定的size值）。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetKeyTime(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t index, float \*keyTime)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_getkeytime) | 获取指定索引处关键帧的关键帧时间点。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTime(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t index, float keyTime)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setkeytime) | 设置指定索引处关键帧的关键帧时间点。  如果不调用本接口设置某个关键帧，其关键帧时间点默认按索引在[0, 1]区间均匀分布（例如，当有3个关键帧时，第一帧为0.0，第二帧为0.5，第三帧为1.0）。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValue(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t index, const ArkUI\_NumberValue \*value, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setvalue) | 设置指定索引处关键帧的值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValues(OH\_ArkUI\_KeyframeAnimationHandle animation, const ArkUI\_NumberValue \*values, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setvalues) | 一次性设置所有关键帧的值。  值以扁平数组形式提供。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetValue(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t index, ArkUI\_NumberValue \*value, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_getvalue) | 获取指定索引处关键帧的值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurves(OH\_ArkUI\_KeyframeAnimationHandle animation, const ArkUI\_CurveHandle \*value, int32\_t size)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurves) | 设置关键帧的动画曲线。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurve(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t index, ArkUI\_CurveHandle curve)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurve) | 设置指定索引处关键帧的动画曲线。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetCurve(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t index, ArkUI\_CurveHandle \*outBorrowedCurve)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_getcurve) | 获取指定索引处关键帧的动画曲线。  本接口仅返回为关键帧显式设置的曲线；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果关键帧未设置曲线，则outBorrowedCurve输出为NULL。运行时实际生效的动画曲线按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurve)或[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurves](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurves)为关键帧设置了曲线，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)设置的动画组曲线；如果两者都未设置，则使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDuration(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t duration)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setduration) | 设置关键帧动画的持续时间。  实际生效的动画持续时间按以下优先级确定：如果通过本接口设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)在动画组上设置的持续时间；如果两者都未设置，则使用默认值1000毫秒。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetDuration(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t \*duration)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_getduration) | 获取关键帧动画的持续时间。  本接口仅返回在本动画上显式设置的持续时间；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时实际生效的动画持续时间按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setduration)设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)设置的动画组持续时间；如果两者都未设置，则使用默认值1000毫秒。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDelay(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t delay)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setdelay) | 设置关键帧动画的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetDelay(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t \*delay)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_getdelay) | 获取关键帧动画的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTempo(OH\_ArkUI\_KeyframeAnimationHandle animation, float tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settempo) | 设置关键帧动画的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetTempo(OH\_ArkUI\_KeyframeAnimationHandle animation, float \*tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_gettempo) | 获取关键帧动画的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetAutoReverse(OH\_ArkUI\_KeyframeAnimationHandle animation, bool autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setautoreverse) | 设置关键帧动画是否自动反转。  启用自动反转后，动画在每轮播放中交替正向播放和反向播放。默认值为false。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetAutoReverse(OH\_ArkUI\_KeyframeAnimationHandle animation, bool \*autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_getautoreverse) | 获取关键帧动画是否启用自动反转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetIterations(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setiterations) | 设置关键帧动画的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetIterations(OH\_ArkUI\_KeyframeAnimationHandle animation, int32\_t \*iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_getiterations) | 获取关键帧动画的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode(OH\_ArkUI\_KeyframeAnimationHandle animation, ArkUI\_RenderNodeHandle targetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settargetnode) | 设置关键帧动画的目标渲染节点。  目标节点是被该关键帧动画驱动的渲染节点。如果为NULL（默认值），则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。非NULL目标必须属于动画组注册的同一UIContext，该检查在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时执行。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetTargetNode(OH\_ArkUI\_KeyframeAnimationHandle animation, ArkUI\_RenderNodeHandle \*outBorrowedTargetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_gettargetnode) | 获取关键帧动画的目标渲染节点。 |
| [OH\_ArkUI\_PathAnimationHandle OH\_ArkUI\_NativeModule\_PathAnimation\_Create(const char \*path)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_create) | 创建路径动画，使组件沿几何路径移动。  路径动画作用于[OH\_ARKUI\_ANIMATION\_PROPERTY\_TRANSLATION](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)属性。  路径动画不支持设置曲线，运行时固定使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)，不继承动画组曲线。 |
| [void OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy(OH\_ArkUI\_PathAnimationHandle animation)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy) | 销毁路径动画。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_SetDuration(OH\_ArkUI\_PathAnimationHandle animation, int32\_t duration)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setduration) | 设置路径动画的持续时间。  实际生效的动画持续时间按以下优先级确定：如果通过本接口设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)在动画组上设置的持续时间；如果两者都未设置，则使用默认值1000毫秒。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_GetDuration(OH\_ArkUI\_PathAnimationHandle animation, int32\_t \*duration)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_getduration) | 获取路径动画的持续时间。  本接口仅返回在本动画上显式设置的持续时间；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时实际生效的动画持续时间按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_PathAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setduration)设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)设置的动画组持续时间；如果两者都未设置，则使用默认值1000毫秒。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_SetDelay(OH\_ArkUI\_PathAnimationHandle animation, int32\_t delay)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setdelay) | 设置路径动画的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_GetDelay(OH\_ArkUI\_PathAnimationHandle animation, int32\_t \*delay)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_getdelay) | 获取路径动画的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_SetTempo(OH\_ArkUI\_PathAnimationHandle animation, float tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settempo) | 设置路径动画的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_GetTempo(OH\_ArkUI\_PathAnimationHandle animation, float \*tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_gettempo) | 获取路径动画的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_SetAutoReverse(OH\_ArkUI\_PathAnimationHandle animation, bool autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setautoreverse) | 设置路径动画是否自动反转。  启用自动反转后，动画在每轮播放中交替正向播放和反向播放。默认值为false。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_GetAutoReverse(OH\_ArkUI\_PathAnimationHandle animation, bool \*autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_getautoreverse) | 获取路径动画是否启用自动反转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_SetIterations(OH\_ArkUI\_PathAnimationHandle animation, int32\_t iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setiterations) | 设置路径动画的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_GetIterations(OH\_ArkUI\_PathAnimationHandle animation, int32\_t \*iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_getiterations) | 获取路径动画的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_SetAutoRotation(OH\_ArkUI\_PathAnimationHandle animation, bool autoRotation)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setautorotation) | 设置路径动画过程中组件是否沿路径切线方向自动旋转。  启用自动旋转后，组件将旋转使其朝向与当前位置的路径切线对齐。默认值为false。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_GetAutoRotation(OH\_ArkUI\_PathAnimationHandle animation, bool \*autoRotation)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_getautorotation) | 获取路径动画是否启用自动旋转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode(OH\_ArkUI\_PathAnimationHandle animation, ArkUI\_RenderNodeHandle targetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settargetnode) | 设置路径动画的目标渲染节点。  目标节点是被该路径动画驱动的渲染节点。如果为NULL（默认值），则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。非NULL目标必须属于动画组注册的同一UIContext，该检查在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时执行。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PathAnimation\_GetTargetNode(OH\_ArkUI\_PathAnimationHandle animation, ArkUI\_RenderNodeHandle \*outBorrowedTargetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_gettargetnode) | 获取路径动画的目标渲染节点。 |
| [OH\_ArkUI\_AnimationGroupHandle OH\_ArkUI\_NativeModule\_AnimationGroup\_Create()](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_create) | 创建动画组。 |
| [void OH\_ArkUI\_NativeModule\_AnimationGroup\_Destroy(OH\_ArkUI\_AnimationGroupHandle group)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_destroy) | 销毁动画组的前端句柄。  本接口仅释放前端句柄。通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册的动画组的后端（运行时）对象将被单独释放——在finish回调触发时自动释放，或通过[OH\_ArkUI\_NativeModule\_RemoveAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_removeanimationgroup)释放。  添加到动画组的子动画不会被自动销毁。需要分别调用[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy)或[OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration(OH\_ArkUI\_AnimationGroupHandle group, int32\_t duration)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration) | 设置动画组的持续时间。  动画组的持续时间作为未通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setduration)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setduration)或[OH\_ArkUI\_NativeModule\_PathAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setduration)设置自身持续时间的子动画的默认持续时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetDuration(OH\_ArkUI\_AnimationGroupHandle group, int32\_t \*duration)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_getduration) | 获取动画组的持续时间。  本接口仅返回在本动画组上显式设置的持续时间，不受子动画的持续时间影响。如果本动画组未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时，未设置的动画组持续时间默认为1000毫秒。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDelay(OH\_ArkUI\_AnimationGroupHandle group, int32\_t delay)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setdelay) | 设置动画组的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetDelay(OH\_ArkUI\_AnimationGroupHandle group, int32\_t \*delay)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_getdelay) | 获取动画组的延迟时间。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve(OH\_ArkUI\_AnimationGroupHandle group, ArkUI\_CurveHandle curve)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve) | 设置动画组的动画曲线。  动画组的曲线作为未通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setcurve)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurve)设置自身曲线的子动画的默认曲线。不支持springMotion、responsiveSpringMotion和interpolatingSpring曲线，因为这些曲线没有有效的持续时间设置。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetCurve(OH\_ArkUI\_AnimationGroupHandle group, ArkUI\_CurveHandle \*outBorrowedCurve)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_getcurve) | 获取动画组的动画曲线。  本接口仅返回在本动画组上显式设置的曲线，不受子动画的曲线影响。如果本动画组未设置曲线，则outBorrowedCurve输出为NULL。运行时，未设置的动画组曲线默认为[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTempo(OH\_ArkUI\_AnimationGroupHandle group, float tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settempo) | 设置动画组的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetTempo(OH\_ArkUI\_AnimationGroupHandle group, float \*tempo)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_gettempo) | 获取动画组的播放速率。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetAutoReverse(OH\_ArkUI\_AnimationGroupHandle group, bool autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setautoreverse) | 设置动画组是否自动反转。  启用自动反转后，动画组在每轮播放中交替正向播放和反向播放。默认值为false。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetAutoReverse(OH\_ArkUI\_AnimationGroupHandle group, bool \*autoReverse)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_getautoreverse) | 获取动画组是否启用自动反转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetIterations(OH\_ArkUI\_AnimationGroupHandle group, int32\_t iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setiterations) | 设置动画组的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetIterations(OH\_ArkUI\_AnimationGroupHandle group, int32\_t \*iterations)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_getiterations) | 获取动画组的播放次数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetExpectedFrameRateRange(OH\_ArkUI\_AnimationGroupHandle group, const ArkUI\_ExpectedFrameRateRange \*frameRate)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setexpectedframeraterange) | 设置动画组的期望帧率范围。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetExpectedFrameRateRange(OH\_ArkUI\_AnimationGroupHandle group, ArkUI\_ExpectedFrameRateRange \*frameRate)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_getexpectedframeraterange) | 获取动画组的期望帧率范围。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_RegisterOnFinishCallback(OH\_ArkUI\_AnimationGroupHandle group, void \*userData, void (\*callback)(void \*userData))](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_registeronfinishcallback) | 注册动画组播放完成时的回调函数。  动画组只有一个完成回调。注册另一个回调会替换之前的回调和userData对。再次注册相同的回调和userData对会成功，但不会创建额外的注册。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode(OH\_ArkUI\_AnimationGroupHandle group, ArkUI\_RenderNodeHandle targetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode) | 设置动画组的默认目标渲染节点。  默认目标是被未通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settargetnode)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settargetnode)或[OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settargetnode)设置自身目标的子动画驱动的渲染节点。在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时，每个子动画必须解析为非NULL目标（自身的目标或动画组默认目标）；任何解析后的目标必须属于动画组注册的同一UIContext。默认值为NULL。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_GetTargetNode(OH\_ArkUI\_AnimationGroupHandle group, ArkUI\_RenderNodeHandle \*outBorrowedTargetNode)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_gettargetnode) | 获取动画组的默认目标渲染节点。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPropertyAnimation(OH\_ArkUI\_AnimationGroupHandle group, OH\_ArkUI\_PropertyAnimationHandle animation)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addpropertyanimation) | 将属性动画添加到动画组中。  动画的目标节点由[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settargetnode)确定；如果未设置，则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。在注册动画组时，每个子动画必须解析为非NULL目标。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_AddKeyframeAnimation(OH\_ArkUI\_AnimationGroupHandle group, OH\_ArkUI\_KeyframeAnimationHandle animation)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addkeyframeanimation) | 将关键帧动画添加到动画组中。  动画的目标节点由[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settargetnode)确定；如果未设置，则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。在注册动画组时，每个子动画必须解析为非NULL目标。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPathAnimation(OH\_ArkUI\_AnimationGroupHandle group, OH\_ArkUI\_PathAnimationHandle animation)](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addpathanimation) | 将路径动画添加到动画组中。  动画的目标节点由[OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settargetnode)确定；如果未设置，则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。在注册动画组时，每个子动画必须解析为非NULL目标。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_AddAnimationGroup(ArkUI\_ContextHandle context, OH\_ArkUI\_AnimationGroupHandle group, const char \*key)](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup) | 在UIContext上以指定key注册动画组并开始播放。  UIContext通过key拥有动画组：注册后，UIContext持有动画组的后端（运行时）对象，调用者可以在注册后销毁前端动画组句柄（及子动画句柄），因为后端通过(UIContext, key)独立运行。key按UIContext（实例）划分作用域：不同UIContext中的相同key不会冲突。在一个UIContext内，如果已用相同key注册了动画组，系统会先移除前一个动画组（释放其后端对象）再注册新动画组。动画组随后通过相同的(UIContext, key)对进行标识和管理。  通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPropertyAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addpropertyanimation)、[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddKeyframeAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addkeyframeanimation)或[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPathAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addpathanimation)添加的每个子动画，驱动其自身设置的目标节点；如果该目标未设置（或为NULL），则继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。注册时，每个子动画必须解析为非NULL目标节点（自身的或动画组默认的）。如果子动画无可解析的目标节点，则返回[ARKUI\_ERROR\_CODE\_SUB\_ANIMATION\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。每个解析后的目标节点必须属于与context相同的UIContext，否则返回错误码[ARKUI\_ERROR\_CODE\_TARGET\_NODE\_NOT\_IN\_SAME\_CONTEXT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  播放控制和生命周期接口（[OH\_ArkUI\_NativeModule\_RemoveAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_removeanimationgroup)、[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)、[OH\_ArkUI\_NativeModule\_HasAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_hasanimationgroup)、[OH\_ArkUI\_NativeModule\_PauseAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_pauseanimationgroup)、[OH\_ArkUI\_NativeModule\_ResumeAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_resumeanimationgroup)、[OH\_ArkUI\_NativeModule\_FinishAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_finishanimationgroup)）均以(UIContext, key)对为键。  finish回调（见[OH\_ArkUI\_NativeModule\_AnimationGroup\_RegisterOnFinishCallback](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_registeronfinishcallback)）仅触发一次，由停止动画的事件触发——自然结束、[OH\_ArkUI\_NativeModule\_FinishAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_finishanimationgroup)或目标节点销毁。如果[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)返回错误，动画创建失败，finish回调不会被触发。回调返回后，系统自动从UIContext移除动画组并释放动画组及其子动画的后端（运行时）对象；前端句柄（动画组及其子动画）仍需由调用者通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_destroy)、[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy)或[OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy)销毁。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_RemoveAnimationGroup(ArkUI\_ContextHandle context, const char \*key)](capi-native-animate-h.md#oh_arkui_nativemodule_removeanimationgroup) | 从UIContext中移除指定key标识的动画组。  停止动画组（如果仍在运行）并释放动画组及其子动画的后端（运行时）对象。被动画的目标节点将恢复到动画开始时的状态。前端句柄（动画组及其子动画）不会被本调用释放，需要由调用者通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_destroy)、[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy)或[OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy)销毁。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_GetAnimationGroupState(ArkUI\_ContextHandle context, const char \*key, OH\_ArkUI\_AnimationGroupState \*state)](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate) | 获取UIContext上指定key标识的动画组的播放状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_HasAnimationGroup(ArkUI\_ContextHandle context, const char \*key, bool \*exists)](capi-native-animate-h.md#oh_arkui_nativemodule_hasanimationgroup) | 检查UIContext上是否存在指定key的动画组。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_PauseAnimationGroup(ArkUI\_ContextHandle context, const char \*key)](capi-native-animate-h.md#oh_arkui_nativemodule_pauseanimationgroup) | 暂停UIContext上指定key标识的动画组。  调用此接口时动画组必须处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态；否则返回[ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。可通过[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)查询动画组的播放状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ResumeAnimationGroup(ArkUI\_ContextHandle context, const char \*key)](capi-native-animate-h.md#oh_arkui_nativemodule_resumeanimationgroup) | 恢复UIContext上指定key标识的动画组。  调用此接口时动画组必须处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态；否则返回[ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。可通过[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)查询动画组的播放状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_FinishAnimationGroup(ArkUI\_ContextHandle context, const char \*key, OH\_ArkUI\_AnimationFinishMode mode)](capi-native-animate-h.md#oh_arkui_nativemodule_finishanimationgroup) | 结束UIContext上指定key标识的动画组。  根据指定的结束模式结束动画组：跳转到结束状态、跳转到起始状态或保持当前值。动画组必须处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)或[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态；否则返回[ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。可通过[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)查询动画组的播放状态。 |

## 函数说明

### OH\_ArkUI\_AnimateOption\_Create()

```c
ArkUI_AnimateOption* OH_ArkUI_AnimateOption_Create()
```

**描述：**

创建动画效果参数。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* | 新的动画效果参数指针。 |

### OH\_ArkUI\_AnimateOption\_Dispose()

```c
void OH_ArkUI_AnimateOption_Dispose(ArkUI_AnimateOption* option)
```

**描述：**

销毁动画效果参数指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |

### OH\_ArkUI\_AnimateOption\_GetDuration()

```c
uint32_t OH_ArkUI_AnimateOption_GetDuration(ArkUI_AnimateOption* option)
```

**描述：**

获取动画持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 动画持续时间，单位为ms（毫秒）。option异常时返回0。 |

### OH\_ArkUI\_AnimateOption\_GetTempo()

```c
float OH_ArkUI_AnimateOption_GetTempo(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放速率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 动画播放速率。取值范围：[0, +∞)。option异常时返回0.0。 |

### OH\_ArkUI\_AnimateOption\_GetCurve()

```c
ArkUI_AnimationCurve OH_ArkUI_AnimateOption_GetCurve(ArkUI_AnimateOption* option)
```

**描述：**

获取动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimationCurve](capi-native-type-visual-h.md#arkui_animationcurve) | 动画曲线。返回值包括：ARKUI\_CURVE\_LINEAR（0，线性曲线）、ARKUI\_CURVE\_EASE（1，缓动曲线）、ARKUI\_CURVE\_EASE\_IN（2，加速曲线）、ARKUI\_CURVE\_EASE\_OUT（3，减速曲线）、ARKUI\_CURVE\_EASE\_IN\_OUT（4，先加速后减速曲线）、ARKUI\_CURVE\_FAST\_OUT\_SLOW\_IN（5，标准曲线）、ARKUI\_CURVE\_LINEAR\_OUT\_SLOW\_IN（6，减速曲线）、ARKUI\_CURVE\_FAST\_OUT\_LINEAR\_IN（7，加速曲线）、ARKUI\_CURVE\_EXTREME\_DECELERATION（8，急减速曲线）、ARKUI\_CURVE\_SHARP（9，锐利曲线）、ARKUI\_CURVE\_RHYTHM（10，节奏曲线）、ARKUI\_CURVE\_SMOOTH（11，平滑曲线）、ARKUI\_CURVE\_FRICTION（12，阻尼曲线）。option异常时返回-1。 |

### OH\_ArkUI\_AnimateOption\_GetDelay()

```c
int32_t OH_ArkUI_AnimateOption_GetDelay(ArkUI_AnimateOption* option)
```

**描述：**

获取动画延迟播放时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 动画延迟播放时间，单位为ms（毫秒）。option异常时返回0。 |

### OH\_ArkUI\_AnimateOption\_GetIterations()

```c
int32_t OH_ArkUI_AnimateOption_GetIterations(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 动画播放次数。option异常时返回0。 |

### OH\_ArkUI\_AnimateOption\_GetPlayMode()

```c
ArkUI_AnimationPlayMode OH_ArkUI_AnimateOption_GetPlayMode(ArkUI_AnimateOption* option)
```

**描述：**

获取动画播放模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimationPlayMode](capi-native-type-visual-h.md#arkui_animationplaymode) | 动画播放模式。返回值包括：ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL（0，正向播放）、ARKUI\_ANIMATION\_PLAY\_MODE\_REVERSE（1，反向播放）、ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE（2，交替播放）、ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE\_REVERSE（3，反向交替播放）。option异常时返回-1。 |

### OH\_ArkUI\_AnimateOption\_GetExpectedFrameRateRange()

```c
ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimateOption_GetExpectedFrameRateRange(ArkUI_AnimateOption* option)
```

**描述：**

获取动画的期望帧率，单位为帧/秒（fps）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md)\* | 动画的期望帧率，单位为帧/秒（fps）。option异常时返回NULL。 |

### OH\_ArkUI\_AnimateOption\_SetDuration()

```c
void OH_ArkUI_AnimateOption_SetDuration(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| int32\_t value | 动画持续时间，单位为ms（毫秒），默认值1000ms。取值范围：[0, +∞)。  value小于0时，按0处理。 |

### OH\_ArkUI\_AnimateOption\_SetTempo()

```c
void OH_ArkUI_AnimateOption_SetTempo(ArkUI_AnimateOption* option, float value)
```

**描述：**

设置动画播放速率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| float value | 动画播放速率，默认值1.0。取值范围：[0, +∞)。  **说明：**  传入小于0的数值，会默认设置为1。 |

### OH\_ArkUI\_AnimateOption\_SetCurve()

```c
void OH_ArkUI_AnimateOption_SetCurve(ArkUI_AnimateOption* option, ArkUI_AnimationCurve value)
```

**描述：**

设置动画自定义曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| [ArkUI\_AnimationCurve](capi-native-type-visual-h.md#arkui_animationcurve) value | 动画曲线。默认值：[ARKUI\_CURVE\_EASE\_IN\_OUT](capi-native-type-visual-h.md#arkui_animationcurve)，建议使用ARKUI\_CURVE\_EASE\_IN\_OUT获得更平滑的动画效果。  value值异常时，设置无效。  \*\*说明：\*\*若同时设置了[OH\_ArkUI\_AnimateOption\_SetICurve](capi-native-animate-h.md#oh_arkui_animateoption_seticurve)，则SetICurve优先生效，本设置不生效。 |

### OH\_ArkUI\_AnimateOption\_SetDelay()

```c
void OH_ArkUI_AnimateOption_SetDelay(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画延迟播放时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| int32\_t value | 动画延迟播放时间，单位为ms（毫秒）。取值范围：(-∞, +∞)。默认值：0，表示不延迟。value大于0时表示延迟播放，小于0表示提前播放。value小于0时，如果value的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到value绝对值的时刻的状态；如果value的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。 |

### OH\_ArkUI\_AnimateOption\_SetIterations()

```c
void OH_ArkUI_AnimateOption_SetIterations(ArkUI_AnimateOption* option, int32_t value)
```

**描述：**

设置动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| int32\_t value | 动画播放次数。取值范围：[-1, +∞)，其中设置为0时不播放，-1表示无限次播放。默认值：1（播放一次）。  value小于-1时，操作无效。 |

### OH\_ArkUI\_AnimateOption\_SetPlayMode()

```c
void OH_ArkUI_AnimateOption_SetPlayMode(ArkUI_AnimateOption* option, ArkUI_AnimationPlayMode value)
```

**描述：**

设置动画播放模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| [ArkUI\_AnimationPlayMode](capi-native-type-visual-h.md#arkui_animationplaymode) value | 动画播放模式。默认值：[ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL](capi-native-type-visual-h.md#arkui_animationplaymode)。ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL表示正向播放，ARKUI\_ANIMATION\_PLAY\_MODE\_REVERSE表示反向播放，ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE表示交替正反向播放，ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE\_REVERSE表示交替反向和正向播放，奇数次反向，偶数次正向。  value值异常时，操作无效。 |

### OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange()

```c
void OH_ArkUI_AnimateOption_SetExpectedFrameRateRange(ArkUI_AnimateOption* option, ArkUI_ExpectedFrameRateRange* value)
```

**描述：**

设置动画的期望帧率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md)\* value | 动画的期望帧率，单位为帧/秒（fps）。  value为NULL时，操作无效。 |

### OH\_ArkUI\_AnimateOption\_SetICurve()

```c
void OH_ArkUI_AnimateOption_SetICurve(ArkUI_AnimateOption* option, ArkUI_CurveHandle value)
```

**描述：**

设置动画的插值曲线。

**说明** 

此方法优先于[OH\_ArkUI\_AnimateOption\_SetCurve](capi-native-animate-h.md#oh_arkui_animateoption_setcurve)生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，操作无效。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) value | 动画曲线参数。  value为NULL时，操作无效。 |

### OH\_ArkUI\_AnimateOption\_GetICurve()

```c
ArkUI_CurveHandle OH_ArkUI_AnimateOption_GetICurve(ArkUI_AnimateOption* option)
```

**描述：**

获取动画的插值曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果参数。  option为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 动画的插值曲线。参数option异常时返回NULL。 |

### OH\_ArkUI\_KeyframeAnimateOption\_Create()

```c
ArkUI_KeyframeAnimateOption* OH_ArkUI_KeyframeAnimateOption_Create(int32_t size)
```

**描述：**

创建关键帧动画参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t size | 关键帧动画状态数。取值范围：[0, +∞)，需要为正整数才能产生动画效果。  size小于0时返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* | 关键帧动画参数对象。size小于0时返回NULL，option异常时返回NULL。 |

### OH\_ArkUI\_KeyframeAnimateOption\_Dispose()

```c
void OH_ArkUI_KeyframeAnimateOption_Dispose(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

销毁关键帧动画参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数对象。  option为NULL时，操作无效。 |

### OH\_ArkUI\_KeyframeAnimateOption\_SetDelay()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetDelay(ArkUI_KeyframeAnimateOption* option, int32_t value)
```

**描述：**

设置关键帧动画的整体延迟时间，单位为ms（毫秒），默认不延迟播放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t value | 动画延迟播放时间，单位为ms（毫秒）。取值范围：(-∞, +∞)。默认值：0，表示不延迟。value大于0为延迟播放，value小于0表示提前播放。对于value小于0的情况：当value的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到value绝对值的时刻的状态；当value的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。可能原因：option为NULL。解决措施：请确保option为有效的动画参数对象指针。 |

### OH\_ArkUI\_KeyframeAnimateOption\_SetIterations()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetIterations(ArkUI_KeyframeAnimateOption* option, int32_t value)
```

**描述：**

设置关键帧动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t value | 动画播放次数。取值范围：[-1, +∞)，其中设置为0时不播放，-1表示无限次播放。默认值：1，表示播放一次。  value小于-1时，操作无效，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnFinishCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*onFinish)(void* userData))
```

**描述：**

设置关键帧动画播放完成回调。当关键帧动画[ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)所有次数播放完成后调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| void\* userData | 用户自定义对象指针。  不涉及异常值处理。 |
| void (\*onFinish)(void\* userData) | 回调函数。  userData：回调函数的入参，用户自定义对象指针。  onFinish为NULL时，操作无效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option, ArkUI_ExpectedFrameRateRange* frameRate)
```

**描述：**

设置关键帧动画期望帧率。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md)\* frameRate | 关键帧动画的期望帧率。  frameRate为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyframeAnimateOption\_SetDuration()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetDuration(ArkUI_KeyframeAnimateOption* option, int32_t value, int32_t index)
```

**描述：**

设置关键帧动画某段关键帧动画的持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t value | 关键帧动画的持续时间，单位为ms（毫秒），默认值1000ms。取值范围：[0, +∞)。  value小于0时，按0处理。 |
| int32\_t index | 状态索引值。取值范围：[0, size-1]，其中size为关键帧动画状态数。  index超出范围时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyframeAnimateOption\_SetCurve()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_SetCurve(ArkUI_KeyframeAnimateOption* option, ArkUI_CurveHandle value, int32_t index)
```

**描述：**

设置关键帧动画某段关键帧使用的动画曲线。

**说明** 

由于[springMotion](capi-native-animate-h.md#oh_arkui_curve_createspringmotion)、[responsiveSpringMotion](capi-native-animate-h.md#oh_arkui_curve_createresponsivespringmotion)、[interpolatingSpring](capi-native-animate-h.md#oh_arkui_curve_createinterpolatingspring)曲线时长不生效，故不支持这三种曲线。关键帧动画支持[springCurve](capi-native-animate-h.md#oh_arkui_curve_createspringcurve)和[customCurve](capi-native-animate-h.md#oh_arkui_curve_createcustomcurve)曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) value | 该关键帧使用的动画曲线。默认值：[ARKUI\_CURVE\_EASE\_IN\_OUT](capi-native-type-visual-h.md#arkui_animationcurve)。 |
| int32\_t index | 状态索引值。取值范围：[0, size-1]，其中size为关键帧动画状态数。  index小于0或index超出范围时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_RegisterOnEventCallback(ArkUI_KeyframeAnimateOption* option, void* userData, void (*event)(void* userData), int32_t index)
```

**描述：**

设置关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| void\* userData | 用户定义对象指针。  不涉及异常值处理。 |
| void (\*event)(void\* userData) | 闭包函数。  userData：回调函数的入参，用户自定义对象指针。  event为NULL时，操作无效。 |
| int32\_t index | 状态索引值。取值范围：[0, size-1]，其中size为关键帧动画状态数。  index小于0或index超出范围时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyframeAnimateOption\_GetDelay()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_GetDelay(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧整体延迟时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 整体延迟时间，单位为ms（毫秒）。option异常时返回0。 |

### OH\_ArkUI\_KeyframeAnimateOption\_GetIterations()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_GetIterations(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 动画播放次数。option异常时返回0。 |

### OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate()

```c
ArkUI_ExpectedFrameRateRange* OH_ArkUI_KeyframeAnimateOption_GetExpectedFrameRate(ArkUI_KeyframeAnimateOption* option)
```

**描述：**

获取关键帧动画参数的期望帧率。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md)\* | 关键帧动画参数的期望帧率。option异常时返回NULL。 |

### OH\_ArkUI\_KeyframeAnimateOption\_GetDuration()

```c
int32_t OH_ArkUI_KeyframeAnimateOption_GetDuration(ArkUI_KeyframeAnimateOption* option, int32_t index)
```

**描述：**

获取关键帧动画某段状态持续时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回0。 |
| int32\_t index | 状态索引值。取值范围：[0, size-1]，其中size为关键帧动画状态数。  index不在取值范围内时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 持续时间，单位为ms（毫秒）。option异常时返回0。 |

### OH\_ArkUI\_KeyframeAnimateOption\_GetCurve()

```c
ArkUI_CurveHandle OH_ArkUI_KeyframeAnimateOption_GetCurve(ArkUI_KeyframeAnimateOption* option, int32_t index)
```

**描述：**

获取关键帧动画某段状态动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。  option为NULL时，返回NULL。 |
| int32\_t index | 状态索引值。取值范围：[0, size-1]，其中size为关键帧动画状态数。  index不在取值范围内时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 动画曲线。参数异常时返回NULL。 |

### OH\_ArkUI\_AnimatorOption\_Create()

```c
ArkUI_AnimatorOption* OH_ArkUI_AnimatorOption_Create(int32_t keyframeSize)
```

**描述：**

创建animator动画对象参数。

**说明** 

keyframeSize大于0时，动画插值起点默认是0，动画插值终点默认值是1。不支持设置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t keyframeSize | 需要创建的关键帧个数。  keyframeSize小于0时返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* | animator动画对象参数指针。keyframeSize小于0时返回NULL，option异常时返回NULL。 |

### OH\_ArkUI\_AnimatorOption\_Dispose()

```c
void OH_ArkUI_AnimatorOption_Dispose(ArkUI_AnimatorOption* option)
```

**描述：**

销毁animator动画对象参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，操作无效。 |

### OH\_ArkUI\_AnimatorOption\_SetDuration()

```c
int32_t OH_ArkUI_AnimatorOption_SetDuration(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画播放的时长，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t value | 播放的时长，单位为ms（毫秒），默认值0ms。取值范围：[0, +∞)。  value小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetDelay()

```c
int32_t OH_ArkUI_AnimatorOption_SetDelay(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画延迟播放的时间，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t value | 动画延迟播放时间，单位为ms（毫秒）。取值范围：(-∞, +∞)。默认值：0，表示不延迟。value大于0为延迟播放，value小于0表示提前播放。对于value小于0的情况：当value的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到value绝对值的时刻的状态；当value的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetIterations()

```c
int32_t OH_ArkUI_AnimatorOption_SetIterations(ArkUI_AnimatorOption* option, int32_t value)
```

**描述：**

设置animator动画播放次数。默认播放一次，设置为-1时表示无限次播放，设置为0时表示无动画效果。

**说明** 

设置为除-1外其他负数视为无效取值，无效取值动画默认播放1次。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t value | 取值范围：[-1, +∞)，其中设置为0时不播放，-1表示无限次播放。默认值：1（播放一次）。  value小于-1时，操作无效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetFill()

```c
int32_t OH_ArkUI_AnimatorOption_SetFill(ArkUI_AnimatorOption* option, ArkUI_AnimationFillMode value)
```

**描述：**

设置组件在动画开始前和结束后保持的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_AnimationFillMode](capi-native-type-visual-h.md#arkui_animationfillmode) value | 动画执行时组件在动画开始前和结束后的状态。默认值：[ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS](capi-native-type-visual-h.md#arkui_animationfillmode)。  ARKUI\_ANIMATION\_FILL\_MODE\_NONE（0）表示动画前后均恢复初始状态，ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS（1）表示动画结束后保持终点状态，ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS（2）表示动画开始前保持起点状态，ARKUI\_ANIMATION\_FILL\_MODE\_BOTH（3）表示动画前后均保持对应状态。  value小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetDirection()

```c
int32_t OH_ArkUI_AnimatorOption_SetDirection(ArkUI_AnimatorOption* option, ArkUI_AnimationDirection value)
```

**描述：**

设置animator动画播放方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_AnimationDirection](capi-native-type-visual-h.md#arkui_animationdirection) value | 动画播放方向。默认值：[ARKUI\_ANIMATION\_DIRECTION\_NORMAL](capi-native-type-visual-h.md#arkui_animationdirection)。  ARKUI\_ANIMATION\_DIRECTION\_NORMAL（0）表示正向播放，ARKUI\_ANIMATION\_DIRECTION\_REVERSE（1）表示反向播放，ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE（2）表示交替正向和反向播放，奇数次正向，偶数次反向，ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE\_REVERSE（3）表示交替反向和正向播放，奇数次反向，偶数次正向。  value超出取值范围时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetCurve()

```c
int32_t OH_ArkUI_AnimatorOption_SetCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value)
```

**描述：**

设置animator动画插值曲线。

**说明** 

不支持[springCurve](capi-native-animate-h.md#oh_arkui_curve_createspringcurve)、[springMotion](capi-native-animate-h.md#oh_arkui_curve_createspringmotion)、[responsiveSpringMotion](capi-native-animate-h.md#oh_arkui_curve_createresponsivespringmotion)、[interpolatingSpring](capi-native-animate-h.md#oh_arkui_curve_createinterpolatingspring)、[customCurve](capi-native-animate-h.md#oh_arkui_curve_createcustomcurve)动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) value | 动画插值曲线。默认值：[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)，建议使用[ARKUI\_CURVE\_EASE\_IN\_OUT](capi-native-type-visual-h.md#arkui_animationcurve)获得更平滑的动画效果。  value为NULL时，使用默认曲线[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetBegin()

```c
int32_t OH_ArkUI_AnimatorOption_SetBegin(ArkUI_AnimatorOption* option, float value)
```

**描述：**

设置animator动画插值起点。

**说明** 

当animator动画为关键帧动画时，此方法返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| float value | 动画插值起点，默认值0.0。取值范围：(-∞, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetEnd()

```c
int32_t OH_ArkUI_AnimatorOption_SetEnd(ArkUI_AnimatorOption* option, float value)
```

**描述：**

设置animator动画插值终点。

**说明** 

当animator动画为关键帧动画时，此方法返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| float value | 动画插值终点。取值范围：(-∞, +∞)。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange()

```c
int32_t OH_ArkUI_AnimatorOption_SetExpectedFrameRateRange(ArkUI_AnimatorOption* option, ArkUI_ExpectedFrameRateRange* value)
```

**描述：**

设置animator动画期望的帧率范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md)\* value | 期望的帧率范围对象。  value为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetKeyframe()

```c
int32_t OH_ArkUI_AnimatorOption_SetKeyframe(ArkUI_AnimatorOption* option, float time, float value, int32_t index)
```

**描述：**

设置animator动画关键帧参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| float time | 关键帧时间。取值范围：[0, 1], 各关键帧时间必须依次递增，即后一关键帧的time值大于前一关键帧的time值。默认值：按索引均匀分布（如第1帧为0.0，第2帧为0.5，第3帧为1.0）。  time小于0或time大于1时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| float value | 关键帧对应的插值目标值，表示动画在该关键帧时刻要达到的属性值。取值范围：(-∞, +∞)。 |
| int32\_t index | 关键帧的索引值。  index小于0时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve()

```c
int32_t OH_ArkUI_AnimatorOption_SetKeyframeCurve(ArkUI_AnimatorOption* option, ArkUI_CurveHandle value, int32_t index)
```

**描述：**

设置animator动画关键帧曲线类型。

**说明** 

不支持[springCurve](capi-native-animate-h.md#oh_arkui_curve_createspringcurve)、[springMotion](capi-native-animate-h.md#oh_arkui_curve_createspringmotion)、[responsiveSpringMotion](capi-native-animate-h.md#oh_arkui_curve_createresponsivespringmotion)、[interpolatingSpring](capi-native-animate-h.md#oh_arkui_curve_createinterpolatingspring)、[customCurve](capi-native-animate-h.md#oh_arkui_curve_createcustomcurve)动画曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) value | 动画插值曲线。默认值：NULL，表示线性插值。 |
| int32\_t index | 关键帧的索引值。取值范围：[0, keyframeSize-1]，其中keyframeSize为关键帧个数。  index超出取值范围时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_GetDuration()

```c
int32_t OH_ArkUI_AnimatorOption_GetDuration(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放的时长，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。  option为NULL时，返回-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 动画播放的时长，单位为ms（毫秒）。option异常时返回0。 |

### OH\_ArkUI\_AnimatorOption\_GetDelay()

```c
int32_t OH_ArkUI_AnimatorOption_GetDelay(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画延迟播放时长，单位为ms（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 动画延迟播放时长，单位为ms（毫秒）。option异常时返回0。 |

### OH\_ArkUI\_AnimatorOption\_GetIterations()

```c
int32_t OH_ArkUI_AnimatorOption_GetIterations(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放次数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 动画播放次数。option异常时返回0。 |

### OH\_ArkUI\_AnimatorOption\_GetFill()

```c
ArkUI_AnimationFillMode OH_ArkUI_AnimatorOption_GetFill(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画执行时组件在动画开始前和结束后的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。option为NULL时，返回-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimationFillMode](capi-native-type-visual-h.md#arkui_animationfillmode) | 动画执行时组件在动画开始前和结束后的状态。返回值包括：ARKUI\_ANIMATION\_FILL\_MODE\_NONE（0，播放完成后恢复初始状态）、ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS（1，播放完成后保持终点状态）、ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS（2，延时播放时保持起点状态）、ARKUI\_ANIMATION\_FILL\_MODE\_BOTH（3，同时应用FORWARDS和BACKWARDS效果）。option异常时返回-1。 |

### OH\_ArkUI\_AnimatorOption\_GetDirection()

```c
ArkUI_AnimationDirection OH_ArkUI_AnimatorOption_GetDirection(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画播放方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimationDirection](capi-native-type-visual-h.md#arkui_animationdirection) | 动画播放方向。返回值包括：ARKUI\_ANIMATION\_DIRECTION\_NORMAL（0，正向播放）、ARKUI\_ANIMATION\_DIRECTION\_REVERSE（1，反向播放）、ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE（2，交替正向和反向播放，奇数次正向，偶数次反向）、ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE\_REVERSE（3，交替反向和正向播放，奇数次反向，偶数次正向）。option异常时返回-1。 |

### OH\_ArkUI\_AnimatorOption\_GetCurve()

```c
ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetCurve(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 动画插值曲线。option异常时返回NULL。 |

### OH\_ArkUI\_AnimatorOption\_GetBegin()

```c
float OH_ArkUI_AnimatorOption_GetBegin(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值起点。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 动画插值起点。option异常时返回0.0。 |

### OH\_ArkUI\_AnimatorOption\_GetEnd()

```c
float OH_ArkUI_AnimatorOption_GetEnd(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画插值终点。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 动画插值终点。option异常时返回0.0。 |

### OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange()

```c
ArkUI_ExpectedFrameRateRange* OH_ArkUI_AnimatorOption_GetExpectedFrameRateRange(ArkUI_AnimatorOption* option)
```

**描述：**

获取animator动画期望的帧率范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md)\* | 期望的帧率范围对象指针。函数参数异常时返回NULL。 |

### OH\_ArkUI\_AnimatorOption\_GetKeyframeTime()

```c
float OH_ArkUI_AnimatorOption_GetKeyframeTime(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧时间，取值范围[0, 1]，为归一化时间比例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。 |
| int32\_t index | 关键帧的索引值。取值范围：[0, keyframeSize-1]，其中keyframeSize为关键帧个数。  index超出范围时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 关键帧时间，取值范围[0, 1]，为归一化时间比例。 |

### OH\_ArkUI\_AnimatorOption\_GetKeyframeValue()

```c
float OH_ArkUI_AnimatorOption_GetKeyframeValue(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧数值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回0.0。 |
| int32\_t index | 关键帧的索引值。取值范围：[0, keyframeSize-1]，其中keyframeSize为关键帧个数。  index超出范围时，返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 关键帧数值。 |

### OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve()

```c
ArkUI_CurveHandle OH_ArkUI_AnimatorOption_GetKeyframeCurve(ArkUI_AnimatorOption* option, int32_t index)
```

**描述：**

获取animator动画关键帧动画插值曲线。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回空指针。 |
| int32\_t index | 关键帧的索引值。取值范围：[0, keyframeSize-1]，其中keyframeSize为关键帧个数。  index超出范围时，返回空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 动画插值曲线。函数参数异常时返回NULL。 |

### OH\_ArkUI\_AnimatorEvent\_GetUserData()

```c
void* OH_ArkUI_AnimatorEvent_GetUserData(ArkUI_AnimatorEvent* event)
```

**描述：**

获取动画事件对象中的用户自定义对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorEvent](capi-arkui-nativemodule-arkui-animatorevent.md)\* event | 动画事件对象。event为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 用户自定义对象。 |

### OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData()

```c
void* OH_ArkUI_AnimatorOnFrameEvent_GetUserData(ArkUI_AnimatorOnFrameEvent* event)
```

**描述：**

获取动画的帧事件中的用户自定义对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOnFrameEvent](capi-arkui-nativemodule-arkui-animatoronframeevent.md)\* event | 动画事件对象。event为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 用户自定义对象。 |

### OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue()

```c
float OH_ArkUI_AnimatorOnFrameEvent_GetValue(ArkUI_AnimatorOnFrameEvent* event)
```

**描述：**

获取动画帧回调事件对象中的插值结果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOnFrameEvent](capi-arkui-nativemodule-arkui-animatoronframeevent.md)\* event | 动画事件对象。event为NULL时，返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 动画插值结果。  **说明：**  在动画过程中，插值结果根据动画参数在插值起点[OH\_ArkUI\_AnimatorOption\_SetBegin](capi-native-animate-h.md#oh_arkui_animatoroption_setbegin)和插值终点[OH\_ArkUI\_AnimatorOption\_SetEnd](capi-native-animate-h.md#oh_arkui_animatoroption_setend)间变化。 |

### OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnFrameCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorOnFrameEvent* event))
```

**描述：**

设置animator动画接收到帧时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorOnFrameEvent\* event) | 回调函数。  - event：回调函数的入参，动画事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnFinishCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画完成时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 回调函数。  - event：回调函数的入参，动画事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnCancelCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画被取消时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回 [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 回调函数。  - event：回调函数的入参，动画事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback()

```c
int32_t OH_ArkUI_AnimatorOption_RegisterOnRepeatCallback(ArkUI_AnimatorOption* option, void* userData, void (*callback)(ArkUI_AnimatorEvent* event))
```

**描述：**

设置animator动画重复时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画对象参数。option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| void\* userData | 用户自定义参数。 |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 回调函数。  - event：回调函数的入参，动画事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Animator\_ResetAnimatorOption()

```c
int32_t OH_ArkUI_Animator_ResetAnimatorOption(ArkUI_AnimatorHandle animatorHandle, ArkUI_AnimatorOption* option)
```

**描述：**

重置animator动画的配置参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象。  animatorHandle为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。  option为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Animator\_Play()

```c
int32_t OH_ArkUI_Animator_Play(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

启动animator动画。需要在主线程上调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象。animatorHandle为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Animator\_Finish()

```c
int32_t OH_ArkUI_Animator_Finish(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

结束animator动画，动画将跳到终点状态后停止。与[OH\_ArkUI\_Animator\_Cancel](capi-native-animate-h.md#oh_arkui_animator_cancel)的区别：Cancel会立即中断动画并回到初始状态，Finish会让动画直接跳到终点状态后停止。需要在主线程上调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象。animatorHandle为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Animator\_Pause()

```c
int32_t OH_ArkUI_Animator_Pause(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

暂停animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象。animatorHandle为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Animator\_Cancel()

```c
int32_t OH_ArkUI_Animator_Cancel(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

取消animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象。animatorHandle为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Animator\_Reverse()

```c
int32_t OH_ArkUI_Animator_Reverse(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

以相反的顺序播放animator动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象。animatorHandle为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Curve\_CreateCurveByType()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCurveByType(ArkUI_AnimationCurve curve)
```

**描述：**

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimationCurve](capi-native-type-visual-h.md#arkui_animationcurve) curve | 曲线类型。curve值异常时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 插值曲线对象指针，用于动画属性值的插值计算。curve值异常时返回NULL。 |

### OH\_ArkUI\_Curve\_CreateStepsCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateStepsCurve(int32_t count, bool end)
```

**描述：**

构造阶梯曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t count | 阶梯的数量，需要为正整数，取值范围：[1, +∞)。  count值异常时，操作无效。 |
| bool end | 在每个间隔的起点或是终点发生阶跃变化。true：在终点发生阶跃变化。false：在起点发生阶跃变化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 阶梯曲线对象指针。如果参数异常返回NULL。 |

### OH\_ArkUI\_Curve\_CreateCubicBezierCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)
```

**描述：**

构造三阶贝塞尔曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float x1 | 确定贝塞尔曲线第一点横坐标，取值范围：[0, 1]。设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| float y1 | 确定贝塞尔曲线第一点纵坐标。取值范围：(-∞, +∞)。 |
| float x2 | 确定贝塞尔曲线第二点横坐标，取值范围：[0, 1]。设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| float y2 | 确定贝塞尔曲线第二点纵坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 三阶贝塞尔曲线对象指针。 |

### OH\_ArkUI\_Curve\_CreateSpringCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)
```

**描述：**

构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受动画参数中的时长参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float velocity | 初始速度。是由外部因素对弹性动效产生的影响参数，其目的是保证对象从之前的运动状态平滑地过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。 |
| float mass | 质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，振荡的幅度越大，恢复到平衡位置的速度越慢。取值范围：[0, +∞)。  value小于等于0时，按1处理。 |
| float stiffness | 刚度。是物体抵抗施加的力而形变的程度。在弹性系统中，刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度就越快。取值范围：[0, +∞)。  value小于等于0时，按1处理。 |
| float damping | 阻尼。用于描述系统在受到扰动后振荡及衰减的情形。阻尼越大，弹性运动的振荡次数越少、振荡幅度越小。取值范围：[0, +∞)。  value小于等于0时，按1处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 插值器弹簧曲线的插值对象指针，用于基于弹簧物理模型进行插值计算，生成从0到1的动画曲线。如果参数异常返回NULL。 |

### OH\_ArkUI\_Curve\_CreateSpringMotion()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)
```

**描述：**

构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换前一个动画，并继承之前的速度。

**说明** 

动画时间由曲线参数决定，不受[animation](capi-native-animate-h.md#oh_arkui_transitioneffect_setanimation)、[animateTo](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto)中的duration参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float response | 弹簧自然振动周期，决定弹簧复位的速度，单位为s（秒）。取值范围：(0, +∞)。  参数小于等于0时，按0.55处理。 |
| float dampingFraction | 阻尼系数。大于0小于1的值为欠阻尼，运动过程中会超出目标值；等于1为临界阻尼；大于1为过阻尼，运动过程中逐渐趋于目标值。取值范围：(0, +∞)。  参数小于等于0时，按0.825处理。 |
| float overlapDuration | 弹性动画衔接时长，单位为s（秒）。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。取值范围：[0, +∞)。  参数小于0时，按0处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 弹性动画曲线的插值对象指针，使用响应式参数构造曲线，支持动画间的速度继承。如果参数异常返回NULL。 |

### OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)
```

**描述：**

构造弹性跟手动画曲线对象，是springMotion的一种特例，仅默认参数不同，可与springMotion混合使用。

**说明** 

动画时间由曲线参数决定，不受[animation](capi-native-animate-h.md#oh_arkui_transitioneffect_setanimation)、[animateTo](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto)中的duration参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float response | 弹簧自然振动周期，决定弹簧复位的速度，单位为s（秒）。取值范围：(0, +∞)。  参数小于等于0时，按0.15处理。 |
| float dampingFraction | 阻尼系数。大于0小于1的值为欠阻尼，运动过程中会超出目标值；等于1为临界阻尼；大于1为过阻尼，运动过程中逐渐趋于目标值。取值范围：[0, +∞)。  参数小于0时，按0.86处理。 |
| float overlapDuration | 弹性动画衔接时长，单位为s（秒）。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。取值范围：[0, +∞)。  参数小于0时，按0.25处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 响应式弹簧动画曲线的插值对象指针，是springMotion的一种特例，仅默认参数不同。如果参数异常返回NULL。 |

### OH\_ArkUI\_Curve\_CreateInterpolatingSpring()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)
```

**描述：**

构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。

**说明** 

动画时间由曲线参数决定，不受[animation](capi-native-animate-h.md#oh_arkui_transitioneffect_setanimation)、[animateTo](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto)中的duration参数控制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float velocity | 初始速度。外部因素对弹性动效产生的影响参数，目的是保证对象从之前的运动状态平滑地过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。取值范围：(-∞, +∞)。 |
| float mass | 质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，振荡的幅度越大，恢复到平衡位置的速度越慢。取值范围：[0, +∞)。  value小于等于0时，按1处理。 |
| float stiffness | 刚度。表示物体抵抗施加的力而形变的程度。刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度越快。取值范围：[0, +∞)。  value小于等于0时，按1处理。 |
| float damping | 阻尼。用于描述系统在受到扰动后振荡及衰减的情形。阻尼越大，弹性运动的振荡次数越少、振荡幅度越小。取值范围：[0, +∞)。  value小于等于0时，按1处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 曲线的插值对象指针。如果参数异常返回NULL。 |

### OH\_ArkUI\_Curve\_CreateCustomCurve()

```c
ArkUI_CurveHandle OH_ArkUI_Curve_CreateCustomCurve(void* userData, float (*interpolate)(float fraction, void* userdata))
```

**描述：**

构造自定义曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* userData | 用户自定义数据。 |
| float (\*interpolate)(float fraction, void\* userdata) | 用户自定义的插值回调函数。fraction为动画开始时的插值输入x值。取值范围：[0,1]。返回值为曲线的y值。取值范围：[0,1]。fraction等于0时，返回值为0对应动画起点，返回不为0，动画在起点处有跳变效果。fraction等于1时，返回值为1对应动画终点，返回值不为1将导致动画的终值不是状态变量的值，出现大于或者小于状态变量值，再跳变到状态变量值的效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) | 曲线的插值对象指针。如果参数异常返回NULL。 |

### OH\_ArkUI\_Curve\_DisposeCurve()

```c
void OH_ArkUI_Curve_DisposeCurve(ArkUI_CurveHandle curveHandle)
```

**描述：**

销毁自定义曲线对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) curveHandle | 曲线的插值对象指针。  curveHandle为NULL时，操作无效。 |

### OH\_ArkUI\_CreateOpacityTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateOpacityTransitionEffect(float opacity)
```

**描述：**

创建组件转场时的透明度效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float opacity | 透明度，取值范围为[0, 1]。默认值为1。设置小于0的非法值按0处理，大于1的非法值按1处理，1表示不透明，0表示完全透明。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* | 组件转场时的透明度效果对象。 |

### OH\_ArkUI\_CreateTranslationTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateTranslationTransitionEffect(ArkUI_TranslationOptions* translate)
```

**描述：**

创建组件转场时的平移效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TranslationOptions](capi-arkui-nativemodule-arkui-translationoptions.md)\* translate | 组件转场时的平移参数对象。  translate为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* | 组件转场时的平移效果对象。如果参数异常返回NULL。 |

### OH\_ArkUI\_CreateScaleTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateScaleTransitionEffect(ArkUI_ScaleOptions* scale)
```

**描述：**

创建组件转场时的缩放效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ScaleOptions](capi-arkui-nativemodule-arkui-scaleoptions.md)\* scale | 组件转场时的缩放参数对象。scale为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* | 组件转场时的缩放效果对象。如果参数异常返回NULL。 |

### OH\_ArkUI\_CreateRotationTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateRotationTransitionEffect(ArkUI_RotationOptions* rotate)
```

**描述：**

创建组件转场时的旋转效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_RotationOptions](capi-arkui-nativemodule-arkui-rotationoptions.md)\* rotate | 组件转场时的旋转参数对象。rotate为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* | 组件转场时的旋转效果对象。如果参数异常返回NULL。 |

### OH\_ArkUI\_CreateMovementTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateMovementTransitionEffect(ArkUI_TransitionEdge edge)
```

**描述：**

创建组件平移效果对象，通过指定边缘方向（上、下、左、右）控制组件的滑入滑出方向，适用于仅需指定滑动方向的简单场景。与OH\_ArkUI\_CreateTranslationTransitionEffect不同：后者支持自定义x/y/z方向的精确平移参数，适用于需要指定具体位移距离的场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TransitionEdge](capi-native-type-visual-h.md#arkui_transitionedge) edge | 组件平移的方向类型，决定组件出现和消失时的平移方向。edge值异常时，按[ARKUI\_TRANSITION\_EDGE\_START](capi-native-type-visual-h.md#arkui_transitionedge)处理。  ARKUI\_TRANSITION\_EDGE\_TOP（0）表示从上方滑入/滑出，ARKUI\_TRANSITION\_EDGE\_BOTTOM（1）表示从下方滑入/滑出，ARKUI\_TRANSITION\_EDGE\_START（2）表示从左侧滑入/滑出，ARKUI\_TRANSITION\_EDGE\_END（3）表示从右侧滑入/滑出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* | 组件转场时的平移效果对象。如果参数异常返回NULL。 |

### OH\_ArkUI\_CreateAsymmetricTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateAsymmetricTransitionEffect(ArkUI_TransitionEffect* appear, ArkUI_TransitionEffect* disappear)
```

**描述：**

创建非对称的转场效果对象。

**说明** 

如果不通过该函数构造[ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)，则表明该效果在组件出现和消失时均生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* appear | 组件出现时的转场效果。appear为NULL时，返回NULL。 |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* disappear | 组件消失时的转场效果。disappear为NULL时，返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* | 非对称的转场效果对象。如果参数异常返回NULL。 |

### OH\_ArkUI\_CreateIdentityTransitionEffect()

```c
ArkUI_TransitionEffect* OH_ArkUI_CreateIdentityTransitionEffect(void)
```

**描述：**

创建无转场效果对象。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* | 创建的无转场效果对象指针。调用者需要调用[OH\_ArkUI\_TransitionEffect\_Dispose](capi-native-animate-h.md#oh_arkui_transitioneffect_dispose)释放该对象。 |

### OH\_ArkUI\_TransitionEffect\_Dispose()

```c
void OH_ArkUI_TransitionEffect_Dispose(ArkUI_TransitionEffect* effect)
```

**描述：**

销毁转场效果对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* effect | 转场效果对象。  effect为NULL时，操作无效。 |

### OH\_ArkUI\_TransitionEffect\_Combine()

```c
int32_t OH_ArkUI_TransitionEffect_Combine(ArkUI_TransitionEffect* firstEffect, ArkUI_TransitionEffect* secondEffect)
```

**描述：**

设置转场效果链式组合，以形成包含多种转场效果的TransitionEffect。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* firstEffect | 链式组合的前一个转场效果，将与secondEffect组合形成包含多种转场效果的TransitionEffect。  firstEffect为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* secondEffect | 需要组合的后一个转场效果，将与firstEffect链式组合形成包含多种转场效果的TransitionEffect。  secondEffect为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TransitionEffect\_SetAnimation()

```c
int32_t OH_ArkUI_TransitionEffect_SetAnimation(ArkUI_TransitionEffect* effect, ArkUI_AnimateOption* animation)
```

**描述：**

设置转场效果动画参数。

**说明** 

如果通过[OH\_ArkUI\_TransitionEffect\_Combine](capi-native-animate-h.md#oh_arkui_transitioneffect_combine)进行转场效果的组合，前一转场效果的动画参数也可用于后一转场效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)\* effect | 要设置动画参数的转场效果对象。  effect为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* animation | 属性显示动画效果相关参数。  animation为NULL时，设置动画参数为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_Create()

```c
OH_ArkUI_PropertyAnimationHandle OH_ArkUI_NativeModule_PropertyAnimation_Create(OH_ArkUI_AnimationPropertyType propertyType)
```

**描述：**

为指定的可动画属性创建属性动画。

propertyType必须是有效的[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，否则本接口返回NULL。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype) propertyType | [入参] 表示要动画的属性类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) | 返回属性动画的句柄。调用者拥有返回的句柄，不再使用时需要调用[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy)释放该句柄。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy()

```c
void OH_ArkUI_NativeModule_PropertyAnimation_Destroy(OH_ArkUI_PropertyAnimationHandle animation)
```

**描述：**

销毁属性动画。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示由[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Create](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_create)返回的属性动画句柄。传入NULL无效果。该函数对非NULL句柄返回后，句柄即失效，不得再次使用或销毁。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetFromValue()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetFromValue(OH_ArkUI_PropertyAnimationHandle animation, const ArkUI_NumberValue *value, int32_t size)
```

**描述：**

设置属性动画的起始值。

推荐设置起始值，若未设置则默认从当前属性值开始产生动画。如果属性动画未设置属性的起始值且对应属性从未被赋值，由于缺少有效的起始状态，属性动画将无法产生。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| const [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) \*value | [入参] 表示起始值。value中元素的数量和类型取决于创建属性动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_create)的取值，具体请参考[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)的枚举描述。例如，如果取值为[OH\_ARKUI\_ANIMATION\_PROPERTY\_OPACITY](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，则value需要传入1个f32值。 |
| int32\_t size | [入参] 表示value数组中的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetFromValue()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetFromValue(OH_ArkUI_PropertyAnimationHandle animation, ArkUI_NumberValue *value, int32_t size)
```

**描述：**

获取属性动画的起始值。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) \*value | [出参] 表示用于接收[ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)起始值数组的指针。  value中元素的数量和类型取决于创建属性动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_create)的取值，具体请参考[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)的枚举描述。例如，如果取值为[OH\_ARKUI\_ANIMATION\_PROPERTY\_OPACITY](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，则value需要传入1个f32值。值将写入该指针指向的内存。  该指针不能为NULL。如果value设置为NULL，则返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t size | [入参] 表示输出数组的大小。必须等于[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)所需的元素个数，否则返回错误码[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 未设置起始值。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 数组大小与所需大小不一致。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetToValue()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetToValue(OH_ArkUI_PropertyAnimationHandle animation, const ArkUI_NumberValue *value, int32_t size)
```

**描述：**

设置属性动画的结束值。

必须设置结束值，否则属性动画句柄无实际意义。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| const [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) \*value | [入参] 表示结束值。value中元素的数量和类型取决于创建属性动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_create)的取值，具体请参考[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)的枚举描述。例如，如果取值为[OH\_ARKUI\_ANIMATION\_PROPERTY\_OPACITY](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，则value需要传入1个f32值。 |
| int32\_t size | [入参] 表示value数组中的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetToValue()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetToValue(OH_ArkUI_PropertyAnimationHandle animation, ArkUI_NumberValue *value, int32_t size)
```

**描述：**

获取属性动画的结束值。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) \*value | [出参] 表示用于接收[ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)结束值数组的指针。  value中元素的数量和类型取决于创建属性动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_create)的取值，具体请参考[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)的枚举描述。例如，如果取值为[OH\_ARKUI\_ANIMATION\_PROPERTY\_OPACITY](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，则value需要传入1个f32值。值将写入该指针指向的内存。  该指针不能为NULL。如果value设置为NULL，则返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t size | [入参] 表示输出数组的大小。必须等于[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)所需的元素个数；否则返回错误码[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 未设置结束值。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 数组大小与所需大小不一致。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetDuration(OH_ArkUI_PropertyAnimationHandle animation, int32_t duration)
```

**描述：**

设置属性动画的持续时间。

实际生效的动画持续时间按以下优先级确定：如果通过本接口设置了子动画的持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)在动画组上设置的持续时间；如果两者都未设置，则使用默认值1000毫秒。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| int32\_t duration | [入参] 表示持续时间，单位为毫秒。该值必须大于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetDuration(OH_ArkUI_PropertyAnimationHandle animation, int32_t *duration)
```

**描述：**

获取属性动画的持续时间。

本接口仅返回在本动画上显式设置的持续时间；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时实际生效的动画持续时间按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setduration)设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)设置的动画组持续时间；如果两者都未设置，则使用默认值1000毫秒。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| int32\_t \*duration | [出参] 表示用于接收持续时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 未设置持续时间。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetDelay(OH_ArkUI_PropertyAnimationHandle animation, int32_t delay)
```

**描述：**

设置属性动画的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| int32\_t delay | [入参] 表示延迟时间，单位为毫秒。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetDelay(OH_ArkUI_PropertyAnimationHandle animation, int32_t *delay)
```

**描述：**

获取属性动画的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| int32\_t \*delay | [出参] 表示用于接收延迟时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetCurve()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetCurve(OH_ArkUI_PropertyAnimationHandle animation, ArkUI_CurveHandle curve)
```

**描述：**

设置属性动画的动画曲线。

实际生效的动画曲线按以下优先级确定：如果通过本接口设置了曲线，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)在动画组上设置的曲线；如果两者都未设置，则使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。支持弹簧曲线（springMotion、responsiveSpringMotion和interpolatingSpring）。设置弹簧曲线时，通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setduration)设置的持续时间不生效，动画持续时间由弹簧曲线决定。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) curve | [入参] 表示动画曲线。NULL表示继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)设置的动画组曲线。本接口不接管曲线句柄的所有权；调用者必须确保在使用该动画句柄期间，曲线保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetCurve()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetCurve(OH_ArkUI_PropertyAnimationHandle animation, ArkUI_CurveHandle *outBorrowedCurve)
```

**描述：**

获取属性动画的动画曲线。

本接口仅返回在本动画上显式设置的曲线；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置曲线，则outBorrowedCurve输出为NULL。运行时实际生效的动画曲线按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setcurve)设置了曲线，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)设置的动画组曲线；如果两者都未设置，则使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) \*outBorrowedCurve | [出参] 表示用于接收动画曲线的指针。调用者不得销毁该句柄。NULL表示本动画未设置曲线，运行时将继承动画组的曲线。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetTempo(OH_ArkUI_PropertyAnimationHandle animation, float tempo)
```

**描述：**

设置属性动画的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| float tempo | [入参] 表示动画播放速率。取值范围：(0, +∞)。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetTempo(OH_ArkUI_PropertyAnimationHandle animation, float *tempo)
```

**描述：**

获取属性动画的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| float \*tempo | [出参] 表示用于接收动画播放速率的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetAutoReverse(OH_ArkUI_PropertyAnimationHandle animation, bool autoReverse)
```

**描述：**

设置属性动画是否自动反转。

启用自动反转后，动画在每轮播放中交替正向播放和反向播放。默认值为false。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| bool autoReverse | [入参] 表示是否启用自动反转。true表示启用自动反转，动画在每轮播放中交替正向播放和反向播放；false表示不启用，动画仅正向播放。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetAutoReverse(OH_ArkUI_PropertyAnimationHandle animation, bool *autoReverse)
```

**描述：**

获取属性动画是否启用自动反转。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| bool \*autoReverse | [出参] 表示用于接收该值的指针。如果启用自动反转则为true；否则为false。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetIterations(OH_ArkUI_PropertyAnimationHandle animation, int32_t iterations)
```

**描述：**

设置属性动画的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| int32\_t iterations | [入参] 表示播放次数。该值必须为-1或大于等于1；值为0时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。值-1表示无限次播放。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetIterations(OH_ArkUI_PropertyAnimationHandle animation, int32_t *iterations)
```

**描述：**

获取属性动画的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| int32\_t \*iterations | [出参] 表示用于接收播放次数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_SetTargetNode(OH_ArkUI_PropertyAnimationHandle animation, ArkUI_RenderNodeHandle targetNode)
```

**描述：**

设置属性动画的目标渲染节点。

目标节点是被该属性动画驱动的渲染节点。如果为NULL（默认值），则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。非NULL目标必须属于动画组注册的同一UIContext，该检查在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时执行。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) targetNode | [入参] 表示要动画的渲染节点。NULL表示继承动画组的默认目标。默认值为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PropertyAnimation_GetTargetNode(OH_ArkUI_PropertyAnimationHandle animation, ArkUI_RenderNodeHandle *outBorrowedTargetNode)
```

**描述：**

获取属性动画的目标渲染节点。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示属性动画句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) \*outBorrowedTargetNode | [出参] 表示用于接收目标渲染节点的指针；调用者不得销毁该句柄。NULL表示继承动画组的默认目标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Create()

```c
OH_ArkUI_KeyframeAnimationHandle OH_ArkUI_NativeModule_KeyframeAnimation_Create(OH_ArkUI_AnimationPropertyType propertyType, int32_t size)
```

**描述：**

为指定的可动画属性创建关键帧动画。

每个关键帧的关键帧时间点默认按索引在[0, 1]区间均匀分布（例如，当有3个关键帧时，第一帧为0.0，第二帧为0.5，第三帧为1.0）。使用[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTimes](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setkeytimes)或[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTime](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setkeytime)自定义关键帧时间点。

propertyType必须是有效的[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，且size必须大于等于2；否则，本接口返回NULL。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype) propertyType | [入参] 表示要动画的属性类型。 |
| int32\_t size | [入参] 表示关键帧数量。该值必须大于等于2。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) | 返回关键帧动画的句柄。调用者拥有返回的句柄，不再使用时需要调用[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy)释放该句柄。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy()

```c
void OH_ArkUI_NativeModule_KeyframeAnimation_Destroy(OH_ArkUI_KeyframeAnimationHandle animation)
```

**描述：**

销毁关键帧动画。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示由[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Create](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create)返回的关键帧动画句柄。  传入NULL无效果。该函数对非NULL句柄返回后，句柄即失效，不得再次使用或销毁。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTimes()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetKeyTimes(OH_ArkUI_KeyframeAnimationHandle animation, const float *keyTimes, int32_t size)
```

**描述：**

设置关键帧的关键帧时间点。

如果不调用本接口，每个关键帧的关键帧时间点默认按索引在[0, 1]区间均匀分布（例如，当有3个关键帧时，第一帧为0.0，第二帧为0.5，第三帧为1.0）。

keyTimes中的元素必须非递减，且size必须等于关键帧动画的关键帧数量（即通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Create](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create)创建动画时指定的size值）。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| const float \*keyTimes | [入参] 表示关键帧时间点数组，为归一化时间比例，取值范围[0, 1]。 |
| int32\_t size | [入参] 表示关键帧时间点的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetKeyTime()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetKeyTime(OH_ArkUI_KeyframeAnimationHandle animation, int32_t index, float *keyTime)
```

**描述：**

获取指定索引处关键帧的关键帧时间点。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t index | [入参] 表示关键帧索引。 |
| float \*keyTime | [出参] 表示用于接收关键帧时间点的指针，为归一化时间比例，取值范围[0, 1]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTime()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetKeyTime(OH_ArkUI_KeyframeAnimationHandle animation, int32_t index, float keyTime)
```

**描述：**

设置指定索引处关键帧的关键帧时间点。

如果不调用本接口设置某个关键帧，其关键帧时间点默认按索引在[0, 1]区间均匀分布（例如，当有3个关键帧时，第一帧为0.0，第二帧为0.5，第三帧为1.0）。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t index | [入参] 表示关键帧索引。 |
| float keyTime | [入参] 表示关键帧时间点，为归一化时间比例，取值范围[0, 1]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValue()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetValue(OH_ArkUI_KeyframeAnimationHandle animation, int32_t index, const ArkUI_NumberValue *value, int32_t size)
```

**描述：**

设置指定索引处关键帧的值。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t index | [入参] 表示关键帧索引。 |
| const [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) \*value | [入参] 表示[ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)数组。  value中元素的数量和类型取决于创建关键帧动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create)的取值，具体请参考[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)的枚举描述。例如，如果取值为[OH\_ARKUI\_ANIMATION\_PROPERTY\_OPACITY](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，则value需要传入1个f32值。 |
| int32\_t size | [入参] 表示value数组中的元素个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValues()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetValues(OH_ArkUI_KeyframeAnimationHandle animation, const ArkUI_NumberValue *values, int32_t size)
```

**描述：**

一次性设置所有关键帧的值。

值以扁平数组形式提供。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| const [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) \*values | [入参] 表示所有关键帧的[ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)扁平数组。每个关键帧的元素数量取决于创建关键帧动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create)的取值。例如，[OH\_ARKUI\_ANIMATION\_PROPERTY\_OPACITY](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)每个关键帧需要1个值，[OH\_ARKUI\_ANIMATION\_PROPERTY\_TRANSLATION](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)每个关键帧需要2个值。元素总数必须等于关键帧数量乘以每个关键帧的值数量。 |
| int32\_t size | [入参] 表示values数组中的元素总数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetValue()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetValue(OH_ArkUI_KeyframeAnimationHandle animation, int32_t index, ArkUI_NumberValue *value, int32_t size)
```

**描述：**

获取指定索引处关键帧的值。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t index | [入参] 表示关键帧索引。 |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) \*value | [出参] 表示用于接收[ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)值数组的指针。  value中元素的数量和类型取决于创建关键帧动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create)的取值，具体请参考[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)的枚举描述。例如，如果取值为[OH\_ARKUI\_ANIMATION\_PROPERTY\_OPACITY](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)，则value需要传入1个f32值。值将写入该指针指向的内存。  该指针不能为NULL。如果value设置为NULL，则返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t size | [入参] 表示输出数组的大小。必须等于[OH\_ArkUI\_AnimationPropertyType](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)所需的元素个数；否则返回错误码[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 关键帧的值未设置。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 数组大小与所需大小不一致。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurves()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetCurves(OH_ArkUI_KeyframeAnimationHandle animation, const ArkUI_CurveHandle *value, int32_t size)
```

**描述：**

设置关键帧的动画曲线。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| const [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) \*value | [入参] 表示曲线句柄数组。本接口不接管曲线句柄的所有权；调用者必须确保在使用该动画句柄期间，所有曲线保持有效。不支持springMotion、responsiveSpringMotion和interpolatingSpring曲线，因为这些曲线没有有效的持续时间设置。 |
| int32\_t size | [入参] 表示曲线数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurve()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetCurve(OH_ArkUI_KeyframeAnimationHandle animation, int32_t index, ArkUI_CurveHandle curve)
```

**描述：**

设置指定索引处关键帧的动画曲线。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t index | [入参] 表示关键帧索引。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) curve | [入参] 表示动画曲线。NULL表示继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)设置的动画组曲线。本接口不接管曲线句柄的所有权；调用者必须确保在使用该动画句柄期间，曲线保持有效。不支持springMotion、responsiveSpringMotion和interpolatingSpring曲线，因为这些曲线没有有效的持续时间设置。实际生效的动画曲线按以下优先级确定：如果通过本接口或[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurves](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurves)为关键帧设置了曲线，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)在动画组上设置的曲线；如果两者都未设置，则使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetCurve()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetCurve(OH_ArkUI_KeyframeAnimationHandle animation, int32_t index, ArkUI_CurveHandle *outBorrowedCurve)
```

**描述：**

获取指定索引处关键帧的动画曲线。

本接口仅返回为关键帧显式设置的曲线；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果关键帧未设置曲线，则outBorrowedCurve输出为NULL。运行时实际生效的动画曲线按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurve)或[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurves](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurves)为关键帧设置了曲线，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setcurve)设置的动画组曲线；如果两者都未设置，则使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t index | [入参] 表示关键帧索引。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) \*outBorrowedCurve | [出参] 表示用于接收动画曲线的指针。调用者不得销毁该句柄。NULL表示该关键帧未设置曲线，运行时将继承动画组的曲线。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetDuration(OH_ArkUI_KeyframeAnimationHandle animation, int32_t duration)
```

**描述：**

设置关键帧动画的持续时间。

实际生效的动画持续时间按以下优先级确定：如果通过本接口设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)在动画组上设置的持续时间；如果两者都未设置，则使用默认值1000毫秒。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t duration | [入参] 表示持续时间，单位为毫秒。该值必须大于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetDuration(OH_ArkUI_KeyframeAnimationHandle animation, int32_t *duration)
```

**描述：**

获取关键帧动画的持续时间。

本接口仅返回在本动画上显式设置的持续时间；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时实际生效的动画持续时间按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setduration)设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)设置的动画组持续时间；如果两者都未设置，则使用默认值1000毫秒。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t \*duration | [出参] 表示用于接收持续时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 未设置持续时间。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetDelay(OH_ArkUI_KeyframeAnimationHandle animation, int32_t delay)
```

**描述：**

设置关键帧动画的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t delay | [入参] 表示延迟时间，单位为毫秒。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetDelay(OH_ArkUI_KeyframeAnimationHandle animation, int32_t *delay)
```

**描述：**

获取关键帧动画的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t \*delay | [出参] 表示用于接收延迟时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetTempo(OH_ArkUI_KeyframeAnimationHandle animation, float tempo)
```

**描述：**

设置关键帧动画的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| float tempo | [入参] 表示动画播放速率。取值范围：(0, +∞)。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetTempo(OH_ArkUI_KeyframeAnimationHandle animation, float *tempo)
```

**描述：**

获取关键帧动画的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| float \*tempo | [出参] 表示用于接收动画播放速率的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetAutoReverse(OH_ArkUI_KeyframeAnimationHandle animation, bool autoReverse)
```

**描述：**

设置关键帧动画是否自动反转。

启用自动反转后，动画在每轮播放中交替正向播放和反向播放。默认值为false。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| bool autoReverse | [入参] 表示是否启用自动反转。true表示启用自动反转，动画在每轮播放中交替正向播放和反向播放；false表示不启用，动画仅正向播放。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetAutoReverse(OH_ArkUI_KeyframeAnimationHandle animation, bool *autoReverse)
```

**描述：**

获取关键帧动画是否启用自动反转。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| bool \*autoReverse | [出参] 表示用于接收该值的指针。如果启用自动反转则为true；否则为false。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetIterations(OH_ArkUI_KeyframeAnimationHandle animation, int32_t iterations)
```

**描述：**

设置关键帧动画的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t iterations | [入参] 表示播放次数。该值必须为-1或大于等于1；值为0时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。值-1表示无限次播放。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetIterations(OH_ArkUI_KeyframeAnimationHandle animation, int32_t *iterations)
```

**描述：**

获取关键帧动画的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| int32\_t \*iterations | [出参] 表示用于接收播放次数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_SetTargetNode(OH_ArkUI_KeyframeAnimationHandle animation, ArkUI_RenderNodeHandle targetNode)
```

**描述：**

设置关键帧动画的目标渲染节点。

目标节点是被该关键帧动画驱动的渲染节点。如果为NULL（默认值），则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。非NULL目标必须属于动画组注册的同一UIContext，该检查在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时执行。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) targetNode | [入参] 表示要动画的渲染节点。NULL表示继承动画组的默认目标。默认值为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_KeyframeAnimation\_GetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_KeyframeAnimation_GetTargetNode(OH_ArkUI_KeyframeAnimationHandle animation, ArkUI_RenderNodeHandle *outBorrowedTargetNode)
```

**描述：**

获取关键帧动画的目标渲染节点。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示关键帧动画句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) \*outBorrowedTargetNode | [出参] 表示用于接收目标渲染节点的指针；调用者不得销毁该句柄。NULL表示继承动画组的默认目标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_Create()

```c
OH_ArkUI_PathAnimationHandle OH_ArkUI_NativeModule_PathAnimation_Create(const char *path)
```

**描述：**

创建路径动画，使组件沿几何路径移动。

路径动画作用于[OH\_ARKUI\_ANIMATION\_PROPERTY\_TRANSLATION](capi-native-type-visual-h.md#oh_arkui_animationpropertytype)属性。

路径动画不支持设置曲线，运行时固定使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)，不继承动画组曲线。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*path | [入参] 表示SVG路径语法的路径字符串。不支持"start"和"end"关键字作为位置值。如果path为NULL、空字符串或包含不支持的值，则返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) | 返回路径动画的句柄。输入无效时返回NULL。调用者拥有返回的句柄，不再使用时需要调用[OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy)释放该句柄。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy()

```c
void OH_ArkUI_NativeModule_PathAnimation_Destroy(OH_ArkUI_PathAnimationHandle animation)
```

**描述：**

销毁路径动画。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示由[OH\_ArkUI\_NativeModule\_PathAnimation\_Create](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_create)返回的路径动画句柄。传入NULL无效果。该函数对非NULL句柄返回后，句柄即失效，不得再次使用或销毁。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_SetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_SetDuration(OH_ArkUI_PathAnimationHandle animation, int32_t duration)
```

**描述：**

设置路径动画的持续时间。

实际生效的动画持续时间按以下优先级确定：如果通过本接口设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)在动画组上设置的持续时间；如果两者都未设置，则使用默认值1000毫秒。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| int32\_t duration | [入参] 表示持续时间，单位为毫秒。该值必须大于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_GetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_GetDuration(OH_ArkUI_PathAnimationHandle animation, int32_t *duration)
```

**描述：**

获取路径动画的持续时间。

本接口仅返回在本动画上显式设置的持续时间；从动画组继承的值或默认值在运行时解析，不存储在本对象上。如果本动画未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时实际生效的动画持续时间按以下优先级确定：如果通过[OH\_ArkUI\_NativeModule\_PathAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setduration)设置了持续时间，则使用该值；否则，使用通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_setduration)设置的动画组持续时间；如果两者都未设置，则使用默认值1000毫秒。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| int32\_t \*duration | [出参] 表示用于接收持续时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 未设置持续时间。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_SetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_SetDelay(OH_ArkUI_PathAnimationHandle animation, int32_t delay)
```

**描述：**

设置路径动画的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| int32\_t delay | [入参] 表示延迟时间，单位为毫秒。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_GetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_GetDelay(OH_ArkUI_PathAnimationHandle animation, int32_t *delay)
```

**描述：**

获取路径动画的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| int32\_t \*delay | [出参] 表示用于接收延迟时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_SetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_SetTempo(OH_ArkUI_PathAnimationHandle animation, float tempo)
```

**描述：**

设置路径动画的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| float tempo | [入参] 表示动画播放速率。取值范围：(0, +∞)。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_GetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_GetTempo(OH_ArkUI_PathAnimationHandle animation, float *tempo)
```

**描述：**

获取路径动画的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| float \*tempo | [出参] 表示用于接收动画播放速率的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_SetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_SetAutoReverse(OH_ArkUI_PathAnimationHandle animation, bool autoReverse)
```

**描述：**

设置路径动画是否自动反转。

启用自动反转后，动画在每轮播放中交替正向播放和反向播放。默认值为false。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| bool autoReverse | [入参] 表示是否启用自动反转。true表示启用自动反转，动画在每轮播放中交替正向播放和反向播放；false表示不启用，动画仅正向播放。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_GetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_GetAutoReverse(OH_ArkUI_PathAnimationHandle animation, bool *autoReverse)
```

**描述：**

获取路径动画是否启用自动反转。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| bool \*autoReverse | [出参] 表示用于接收该值的指针。如果启用自动反转则为true；否则为false。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_SetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_SetIterations(OH_ArkUI_PathAnimationHandle animation, int32_t iterations)
```

**描述：**

设置路径动画的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| int32\_t iterations | [入参] 表示播放次数。该值必须为-1或大于等于1；值为0时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。值-1表示无限次播放。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_GetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_GetIterations(OH_ArkUI_PathAnimationHandle animation, int32_t *iterations)
```

**描述：**

获取路径动画的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| int32\_t \*iterations | [出参] 表示用于接收播放次数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_SetAutoRotation()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_SetAutoRotation(OH_ArkUI_PathAnimationHandle animation, bool autoRotation)
```

**描述：**

设置路径动画过程中组件是否沿路径切线方向自动旋转。

启用自动旋转后，组件将旋转使其朝向与当前位置的路径切线对齐。默认值为false。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| bool autoRotation | [入参] 表示是否启用自动旋转。true表示启用自动旋转，组件将旋转使其朝向与当前位置的路径切线对齐；false表示不启用，组件不随路径切线旋转。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_GetAutoRotation()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_GetAutoRotation(OH_ArkUI_PathAnimationHandle animation, bool *autoRotation)
```

**描述：**

获取路径动画是否启用自动旋转。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| bool \*autoRotation | [出参] 表示用于接收该值的指针。如果启用自动旋转则为true；否则为false。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_SetTargetNode(OH_ArkUI_PathAnimationHandle animation, ArkUI_RenderNodeHandle targetNode)
```

**描述：**

设置路径动画的目标渲染节点。

目标节点是被该路径动画驱动的渲染节点。如果为NULL（默认值），则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。非NULL目标必须属于动画组注册的同一UIContext，该检查在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时执行。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) targetNode | [入参] 表示要动画的渲染节点。NULL表示继承动画组的默认目标。默认值为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_PathAnimation\_GetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PathAnimation_GetTargetNode(OH_ArkUI_PathAnimationHandle animation, ArkUI_RenderNodeHandle *outBorrowedTargetNode)
```

**描述：**

获取路径动画的目标渲染节点。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示路径动画句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) \*outBorrowedTargetNode | [出参] 表示用于接收目标渲染节点的指针；调用者不得销毁该句柄。NULL表示继承动画组的默认目标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_Create()

```c
OH_ArkUI_AnimationGroupHandle OH_ArkUI_NativeModule_AnimationGroup_Create(void)
```

**描述：**

创建动画组。

**起始版本：** 26.0.1

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) | 返回动画组的句柄。调用者拥有返回的句柄，不再使用时需要调用[OH\_ArkUI\_NativeModule\_AnimationGroup\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_destroy)释放该句柄。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_Destroy()

```c
void OH_ArkUI_NativeModule_AnimationGroup_Destroy(OH_ArkUI_AnimationGroupHandle group)
```

**描述：**

销毁动画组的前端句柄。

本接口仅释放前端句柄。通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册的动画组的后端（运行时）对象将被单独释放——在finish回调触发时自动释放，或通过[OH\_ArkUI\_NativeModule\_RemoveAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_removeanimationgroup)释放。

添加到动画组的子动画不会被自动销毁。需要分别调用[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy)或[OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy)。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示由[OH\_ArkUI\_NativeModule\_AnimationGroup\_Create](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_create)返回的动画组句柄。  传入NULL无效果。该函数对非NULL句柄返回后，句柄即失效，不得再次使用或销毁。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetDuration(OH_ArkUI_AnimationGroupHandle group, int32_t duration)
```

**描述：**

设置动画组的持续时间。

动画组的持续时间作为未通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setduration)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setduration)或[OH\_ArkUI\_NativeModule\_PathAnimation\_SetDuration](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_setduration)设置自身持续时间的子动画的默认持续时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| int32\_t duration | [入参] 表示持续时间，单位为毫秒。该值必须大于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetDuration()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetDuration(OH_ArkUI_AnimationGroupHandle group, int32_t *duration)
```

**描述：**

获取动画组的持续时间。

本接口仅返回在本动画组上显式设置的持续时间，不受子动画的持续时间影响。如果本动画组未设置持续时间，则返回[ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。运行时，未设置的动画组持续时间默认为1000毫秒。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| int32\_t \*duration | [出参] 表示用于接收持续时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NO\_ATTRIBUTE\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 未设置持续时间。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetDelay(OH_ArkUI_AnimationGroupHandle group, int32_t delay)
```

**描述：**

设置动画组的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| int32\_t delay | [入参] 表示延迟时间，单位为毫秒。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetDelay()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetDelay(OH_ArkUI_AnimationGroupHandle group, int32_t *delay)
```

**描述：**

获取动画组的延迟时间。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| int32\_t \*delay | [出参] 表示用于接收延迟时间值的指针，单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetCurve()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetCurve(OH_ArkUI_AnimationGroupHandle group, ArkUI_CurveHandle curve)
```

**描述：**

设置动画组的动画曲线。

动画组的曲线作为未通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setcurve)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetCurve](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setcurve)设置自身曲线的子动画的默认曲线。不支持springMotion、responsiveSpringMotion和interpolatingSpring曲线，因为这些曲线没有有效的持续时间设置。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) curve | [入参] 表示动画曲线。NULL表示动画组在运行时使用默认值[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。本接口不接管曲线句柄的所有权；调用者必须确保在使用该动画句柄期间，曲线保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetCurve()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetCurve(OH_ArkUI_AnimationGroupHandle group, ArkUI_CurveHandle *outBorrowedCurve)
```

**描述：**

获取动画组的动画曲线。

本接口仅返回在本动画组上显式设置的曲线，不受子动画的曲线影响。如果本动画组未设置曲线，则outBorrowedCurve输出为NULL。运行时，未设置的动画组曲线默认为[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [ArkUI\_CurveHandle](capi-arkui-nativemodule-arkui-curve8h.md) \*outBorrowedCurve | [出参] 表示用于接收动画曲线的指针。调用者不得销毁该句柄。NULL表示本动画组未设置曲线，运行时默认使用[ARKUI\_CURVE\_LINEAR](capi-native-type-visual-h.md#arkui_animationcurve)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetTempo(OH_ArkUI_AnimationGroupHandle group, float tempo)
```

**描述：**

设置动画组的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| float tempo | [入参] 表示动画播放速率。取值范围：(0, +∞)。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetTempo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetTempo(OH_ArkUI_AnimationGroupHandle group, float *tempo)
```

**描述：**

获取动画组的播放速率。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| float \*tempo | [出参] 表示用于接收动画播放速率的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetAutoReverse(OH_ArkUI_AnimationGroupHandle group, bool autoReverse)
```

**描述：**

设置动画组是否自动反转。

启用自动反转后，动画组在每轮播放中交替正向播放和反向播放。默认值为false。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| bool autoReverse | [入参] 表示是否启用自动反转。true表示启用自动反转，动画在每轮播放中交替正向播放和反向播放；false表示不启用，动画仅正向播放。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetAutoReverse()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetAutoReverse(OH_ArkUI_AnimationGroupHandle group, bool *autoReverse)
```

**描述：**

获取动画组是否启用自动反转。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| bool \*autoReverse | [出参] 表示用于接收该值的指针。如果启用自动反转则为true；否则为false。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetIterations(OH_ArkUI_AnimationGroupHandle group, int32_t iterations)
```

**描述：**

设置动画组的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| int32\_t iterations | [入参] 表示播放次数。该值必须为-1或大于等于1；值为0时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。值-1表示无限次播放。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetIterations()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetIterations(OH_ArkUI_AnimationGroupHandle group, int32_t *iterations)
```

**描述：**

获取动画组的播放次数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| int32\_t \*iterations | [出参] 表示用于接收播放次数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetExpectedFrameRateRange()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetExpectedFrameRateRange(OH_ArkUI_AnimationGroupHandle group, const ArkUI_ExpectedFrameRateRange *frameRate)
```

**描述：**

设置动画组的期望帧率范围。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| const [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md) \*frameRate | [入参] 表示期望帧率范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetExpectedFrameRateRange()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetExpectedFrameRateRange(OH_ArkUI_AnimationGroupHandle group, ArkUI_ExpectedFrameRateRange *frameRate)
```

**描述：**

获取动画组的期望帧率范围。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md) \*frameRate | [出参] 表示用于接收期望帧率范围的指针。  [ArkUI\_ExpectedFrameRateRange](capi-arkui-nativemodule-arkui-expectedframeraterange.md)对象的值将写入该指针指向的内存。  该指针不能为NULL。如果frameRate设置为NULL，则返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_RegisterOnFinishCallback()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_RegisterOnFinishCallback(OH_ArkUI_AnimationGroupHandle group, void *userData, void (*callback)(void *userData))
```

**描述：**

注册动画组播放完成时的回调函数。

动画组只有一个完成回调。注册另一个回调会替换之前的回调和userData对。再次注册相同的回调和userData对会成功，但不会创建额外的注册。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| void \*userData | [入参] 表示调用者拥有的自定义数据，原样传递给回调。可以为NULL，必须保持有效直到回调返回，本接口不负责释放该数据。 |
| void (\*callback)(void \*userData) | [入参] 表示完成回调函数。不能为NULL，在UI主线程上串行调用一次。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_SetTargetNode(OH_ArkUI_AnimationGroupHandle group, ArkUI_RenderNodeHandle targetNode)
```

**描述：**

设置动画组的默认目标渲染节点。

默认目标是被未通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settargetnode)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settargetnode)或[OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settargetnode)设置自身目标的子动画驱动的渲染节点。在通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时，每个子动画必须解析为非NULL目标（自身的目标或动画组默认目标）；任何解析后的目标必须属于动画组注册的同一UIContext。默认值为NULL。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) targetNode | [入参] 表示默认的要动画的渲染节点。NULL表示没有动画组级别的默认值。默认值为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_GetTargetNode()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_GetTargetNode(OH_ArkUI_AnimationGroupHandle group, ArkUI_RenderNodeHandle *outBorrowedTargetNode)
```

**描述：**

获取动画组的默认目标渲染节点。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [ArkUI\_RenderNodeHandle](capi-arkui-nativemodule-arkui-rendernodehandle.md) \*outBorrowedTargetNode | [出参] 表示用于接收默认目标节点的指针；调用者不得销毁该句柄。NULL表示未设置动画组级别的默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPropertyAnimation()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_AddPropertyAnimation(OH_ArkUI_AnimationGroupHandle group, OH_ArkUI_PropertyAnimationHandle animation)
```

**描述：**

将属性动画添加到动画组中。

动画的目标节点由[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settargetnode)确定；如果未设置，则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。在注册动画组时，每个子动画必须解析为非NULL目标。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [OH\_ArkUI\_PropertyAnimationHandle](capi-arkui-nativemodule-arkui-propertyanimation8h.md) animation | [入参] 表示要添加的属性动画。本接口不接管该动画句柄的所有权；调用者必须确保在使用动画组句柄期间，该动画保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_SUB\_ANIMATION\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) OH\_ArkUI\_PropertyAnimationHandle参数无效。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_AddKeyframeAnimation()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_AddKeyframeAnimation(OH_ArkUI_AnimationGroupHandle group, OH_ArkUI_KeyframeAnimationHandle animation)
```

**描述：**

将关键帧动画添加到动画组中。

动画的目标节点由[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settargetnode)确定；如果未设置，则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。在注册动画组时，每个子动画必须解析为非NULL目标。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [OH\_ArkUI\_KeyframeAnimationHandle](capi-arkui-nativemodule-arkui-keyframeanimation8h.md) animation | [入参] 表示要添加的关键帧动画。本接口不接管该动画句柄的所有权；调用者必须确保在使用动画组句柄期间，该动画保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_SUB\_ANIMATION\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) OH\_ArkUI\_KeyframeAnimationHandle参数无效。 |

### OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPathAnimation()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AnimationGroup_AddPathAnimation(OH_ArkUI_AnimationGroupHandle group, OH_ArkUI_PathAnimationHandle animation)
```

**描述：**

将路径动画添加到动画组中。

动画的目标节点由[OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settargetnode)确定；如果未设置，则动画继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。在注册动画组时，每个子动画必须解析为非NULL目标。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| [OH\_ArkUI\_PathAnimationHandle](capi-arkui-nativemodule-arkui-pathanimation8h.md) animation | [入参] 表示要添加的路径动画。本接口不接管该动画句柄的所有权；调用者必须确保在使用动画组句柄期间，该动画保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_SUB\_ANIMATION\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) OH\_ArkUI\_PathAnimationHandle参数无效。 |

### OH\_ArkUI\_NativeModule\_AddAnimationGroup()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_AddAnimationGroup(ArkUI_ContextHandle context, OH_ArkUI_AnimationGroupHandle group, const char *key)
```

**描述：**

在UIContext上以指定key注册动画组并开始播放。

UIContext通过key拥有动画组：注册后，UIContext持有动画组的后端（运行时）对象，调用者可以在注册后销毁前端动画组句柄（及子动画句柄），因为后端通过(UIContext, key)独立运行。key按UIContext（实例）划分作用域：不同UIContext中的相同key不会冲突。在一个UIContext内，如果已用相同key注册了动画组，系统会先移除前一个动画组（释放其后端对象）再注册新动画组。动画组随后通过相同的(UIContext, key)对进行标识和管理。

通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPropertyAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addpropertyanimation)、[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddKeyframeAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addkeyframeanimation)或[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPathAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addpathanimation)添加的每个子动画，驱动其自身设置的目标节点；如果该目标未设置（或为NULL），则继承通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标。注册时，每个子动画必须解析为非NULL目标节点（自身的或动画组默认的）。如果子动画无可解析的目标节点，则返回[ARKUI\_ERROR\_CODE\_SUB\_ANIMATION\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。每个解析后的目标节点必须属于与context相同的UIContext，否则返回错误码[ARKUI\_ERROR\_CODE\_TARGET\_NODE\_NOT\_IN\_SAME\_CONTEXT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

播放控制和生命周期接口（[OH\_ArkUI\_NativeModule\_RemoveAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_removeanimationgroup)、[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)、[OH\_ArkUI\_NativeModule\_HasAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_hasanimationgroup)、[OH\_ArkUI\_NativeModule\_PauseAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_pauseanimationgroup)、[OH\_ArkUI\_NativeModule\_ResumeAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_resumeanimationgroup)、[OH\_ArkUI\_NativeModule\_FinishAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_finishanimationgroup)）均以(UIContext, key)对为键。

finish回调（见[OH\_ArkUI\_NativeModule\_AnimationGroup\_RegisterOnFinishCallback](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_registeronfinishcallback)）仅触发一次，由停止动画的事件触发——自然结束、[OH\_ArkUI\_NativeModule\_FinishAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_finishanimationgroup)或目标节点销毁。如果[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)返回错误，动画创建失败，finish回调不会被触发。回调返回后，系统自动从UIContext移除动画组并释放动画组及其子动画的后端（运行时）对象；前端句柄（动画组及其子动画）仍需由调用者通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_destroy)、[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy)或[OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy)销毁。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | [入参] 表示注册并播放动画组的[ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md)（UIContext）。 |
| [OH\_ArkUI\_AnimationGroupHandle](capi-arkui-nativemodule-arkui-animationgroup8h.md) group | [入参] 表示动画组句柄。 |
| const char \*key | [入参] 表示用于在UIContext上标识动画组的key。key为用户自定义的字符串，在同一UIContext内需唯一。如果已用相同key注册了动画组，系统会先移除前一个动画组再注册新动画组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_TARGET\_NODE\_NOT\_IN\_SAME\_CONTEXT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 解析后的目标节点不属于与context相同的UIContext。  [ARKUI\_ERROR\_CODE\_SUB\_ANIMATION\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 子动画无可解析的目标节点或子动画参数非法。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_REENTRANT\_CALL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 检测到同线程重入调用。 |

### OH\_ArkUI\_NativeModule\_RemoveAnimationGroup()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_RemoveAnimationGroup(ArkUI_ContextHandle context, const char *key)
```

**描述：**

从UIContext中移除指定key标识的动画组。

停止动画组（如果仍在运行）并释放动画组及其子动画的后端（运行时）对象。被动画的目标节点将恢复到动画开始时的状态。前端句柄（动画组及其子动画）不会被本调用释放，需要由调用者通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_destroy)、[OH\_ArkUI\_NativeModule\_PropertyAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_destroy)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_destroy)或[OH\_ArkUI\_NativeModule\_PathAnimation\_Destroy](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_destroy)销毁。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | [入参] 表示注册动画组的UIContext。 |
| const char \*key | [入参] 表示要移除的动画组的key。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_NOT\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 在UIContext上未找到key标识的动画组。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_REENTRANT\_CALL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 检测到同线程重入调用。 |

### OH\_ArkUI\_NativeModule\_GetAnimationGroupState()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_GetAnimationGroupState(ArkUI_ContextHandle context, const char *key, OH_ArkUI_AnimationGroupState *state)
```

**描述：**

获取UIContext上指定key标识的动画组的播放状态。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | [入参] 表示UIContext。 |
| const char \*key | [入参] 表示动画组的key。 |
| [OH\_ArkUI\_AnimationGroupState](capi-native-type-visual-h.md#oh_arkui_animationgroupstate) \*state | [出参] 表示用于接收状态值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_NOT\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 在UIContext上未找到key标识的动画组。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_REENTRANT\_CALL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 检测到同线程重入调用。 |

### OH\_ArkUI\_NativeModule\_HasAnimationGroup()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_HasAnimationGroup(ArkUI_ContextHandle context, const char *key, bool *exists)
```

**描述：**

检查UIContext上是否存在指定key的动画组。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | [入参] 表示UIContext。 |
| const char \*key | [入参] 表示动画组的key。 |
| bool \*exists | [入参] 表示用于接收该值的指针。如果动画组存在则为true；否则为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_REENTRANT\_CALL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 检测到同线程重入调用。 |

### OH\_ArkUI\_NativeModule\_PauseAnimationGroup()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_PauseAnimationGroup(ArkUI_ContextHandle context, const char *key)
```

**描述：**

暂停UIContext上指定key标识的动画组。

调用此接口时动画组必须处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态；否则返回[ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。可通过[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)查询动画组的播放状态。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | [入参] 表示UIContext。 |
| const char \*key | [入参] 表示动画组的key。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_NOT\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 在UIContext上未找到key标识的动画组。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 动画组不处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_REENTRANT\_CALL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 检测到同线程重入调用。 |

### OH\_ArkUI\_NativeModule\_ResumeAnimationGroup()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ResumeAnimationGroup(ArkUI_ContextHandle context, const char *key)
```

**描述：**

恢复UIContext上指定key标识的动画组。

调用此接口时动画组必须处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态；否则返回[ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。可通过[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)查询动画组的播放状态。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | [入参] 表示UIContext。 |
| const char \*key | [入参] 表示动画组的key。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_NOT\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 在UIContext上未找到key标识的动画组。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 动画组不处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_REENTRANT\_CALL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 检测到同线程重入调用。 |

### OH\_ArkUI\_NativeModule\_FinishAnimationGroup()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_FinishAnimationGroup(ArkUI_ContextHandle context, const char *key, OH_ArkUI_AnimationFinishMode mode)
```

**描述：**

结束UIContext上指定key标识的动画组。

根据指定的结束模式结束动画组：跳转到结束状态、跳转到起始状态或保持当前值。动画组必须处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)或[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态；否则返回[ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。可通过[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)查询动画组的播放状态。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | [入参] 表示UIContext。 |
| const char \*key | [入参] 表示动画组的key。 |
| [OH\_ArkUI\_AnimationFinishMode](capi-native-type-visual-h.md#oh_arkui_animationfinishmode) mode | [入参] 表示结束模式。该值为[OH\_ArkUI\_AnimationFinishMode](capi-native-type-visual-h.md#oh_arkui_animationfinishmode)的枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，例如context或key无效，或mode不是OH\_ArkUI\_AnimationFinishMode的有效值。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_NOT\_FOUND](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 在UIContext上未找到key标识的动画组。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_INVALID\_STATE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 动画组不处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)或[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态。  [ARKUI\_ERROR\_CODE\_ANIMATION\_GROUP\_REENTRANT\_CALL](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 检测到同线程重入调用。 |
