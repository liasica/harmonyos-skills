---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-animation
title: 动视效错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 动视效错误码
category: harmonyos-references
scraped_at: 2026-11-12T09:54:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:66ddcfbbdadffd5cce7e6e804ad49011dc4de9384627a513db0868893f18c569
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 106211 无法获取属性

**错误信息**

The attribute was not found because it was not set before.

**错误描述**

无法获取属性，因为之前未设置该属性。

**可能原因**

调用接口获取属性值时，之前未通过对应的设置接口设置该属性。例如调用[OH\_ArkUI\_NativeModule\_PropertyAnimation\_GetFromValue](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_getfromvalue)时，之前未通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetFromValue](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_setfromvalue)设置属性值。

**处理步骤**

先通过对应的设置接口设置属性值，再调用接口获取属性值。

## 106212 子动画参数无效

**错误信息**

The sub-animation parameter is invalid.

**错误描述**

添加到动画组的子动画参数无效。

**可能原因**

1. 通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddPropertyAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addpropertyanimation)添加属性动画时：属性动画未设置结束值（未调用[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetToValue](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settovalue)）。
2. 通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_AddKeyframeAnimation](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_addkeyframeanimation)添加关键帧动画时：关键帧时间点顺序不正确（存在后续关键帧时间点小于前一个关键帧时间点的情况），或未通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValue](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setvalue)或[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValues](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setvalues)完整设置与创建关键帧动画时传入的[propertyType](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_create)对应的[ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)值。
3. 通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时：子动画未设置目标渲染节点，且动画组也未设置默认目标渲染节点，导致无法解析出目标节点。

**处理步骤**

1. 确保属性动画已通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetToValue](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settovalue)设置结束值。
2. 确保关键帧动画已通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValue](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setvalue)或[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetValues](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setvalues)为每个关键帧设置与propertyType对应的[ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)值；通过[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetKeyTime](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_setkeytime)设置关键帧时间点时，需确保关键帧时间点顺序正确（后续关键帧时间点不小于前一个关键帧时间点）。
3. 通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settargetnode)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settargetnode)或[OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settargetnode)为子动画设置目标渲染节点，或通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置动画组的默认目标渲染节点。

## 106213 在UIContext上未找到指定的动画组

**错误信息**

The animation group is not found on the UIContext.

**错误描述**

在UIContext上未找到指定key标识的动画组。

**可能原因**

1. 使用未通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册的key查找动画组。
2. 动画组已结束播放，动画结束后被系统自动移除。

**处理步骤**

确认key已通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册，且动画组尚未结束。动画组在自然结束、调用[OH\_ArkUI\_NativeModule\_FinishAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_finishanimationgroup)或目标节点销毁后，会触发动画结束回调，回调执行完毕后系统自动移除动画组。必要时通过[OH\_ArkUI\_NativeModule\_HasAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_hasanimationgroup)检查动画组是否存在。

## 106214 检测到同一线程上对动画组接口的重入调用

**错误信息**

A re-entrant call to animation group APIs is detected on the same thread.

**错误描述**

在同一线程上，一个动画组接口调用尚未返回时，该线程嵌套调用了另一个动画组接口。

**可能原因**

在同一线程上，一个动画组接口调用尚未返回时，该线程嵌套调用了另一个动画组接口。

**处理步骤**

确保动画组接口在上一调用完全返回后再进行下一次调用，避免在同一线程上嵌套调用动画组接口。

## 106215 动画组未处于操作所需的状态

**错误信息**

The animation group is not in the required state for the operation.

**错误描述**

动画组当前状态不满足接口调用所需的状态要求。

**可能原因**

1. 调用[OH\_ArkUI\_NativeModule\_PauseAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_pauseanimationgroup)时动画组不处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态。
2. 调用[OH\_ArkUI\_NativeModule\_ResumeAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_resumeanimationgroup)时动画组不处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态。
3. 调用[OH\_ArkUI\_NativeModule\_FinishAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_finishanimationgroup)时动画组不处于[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_RUNNING](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)或[OH\_ARKUI\_ANIMATION\_GROUP\_STATE\_PAUSED](capi-native-type-visual-h.md#oh_arkui_animationgroupstate)状态。

**处理步骤**

通过[OH\_ArkUI\_NativeModule\_GetAnimationGroupState](capi-native-animate-h.md#oh_arkui_nativemodule_getanimationgroupstate)查询动画组当前状态，确保状态正确后再调用对应接口。

## 106216 解析的目标节点不属于注册动画组时传入的context所在的UIContext

**错误信息**

The resolved target node does not belong to the same UIContext as the context parameter.

**错误描述**

解析的目标节点不属于注册动画组时传入的context所在的UIContext。

**可能原因**

通过[OH\_ArkUI\_NativeModule\_AddAnimationGroup](capi-native-animate-h.md#oh_arkui_nativemodule_addanimationgroup)注册动画组时，子动画解析出的目标渲染节点所属的UIContext与传入的context参数所属的UIContext不一致。

**处理步骤**

确保通过[OH\_ArkUI\_NativeModule\_PropertyAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_propertyanimation_settargetnode)、[OH\_ArkUI\_NativeModule\_KeyframeAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_keyframeanimation_settargetnode)或[OH\_ArkUI\_NativeModule\_PathAnimation\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_pathanimation_settargetnode)为子动画设置的目标渲染节点，或通过[OH\_ArkUI\_NativeModule\_AnimationGroup\_SetTargetNode](capi-native-animate-h.md#oh_arkui_nativemodule_animationgroup_settargetnode)设置的动画组默认目标渲染节点，与注册动画组时传入的context属于同一UIContext。
