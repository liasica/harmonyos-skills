---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e
title: Enums
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Enums
category: harmonyos-references
scraped_at: 2026-09-02T15:00:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8b0a5410b0fea61c965a952abee72fabf1de17d1f9882df1419586ba397b55c7
---

本章节提供UIContext相关枚举类型，用于配置键盘避让、动态帧率场景、节点渲染状态、手势监听、自定义键盘接续和文本选择清除策略等场景。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## KeyboardAvoidMode11+

配置键盘弹出时页面的避让模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFFSET | 0 | 上抬模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| RESIZE | 1 | 压缩模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| OFFSET\_WITH\_CARET14+ | 2 | 上抬模式，输入框光标位置发生变化时也会触发避让。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| RESIZE\_WITH\_CARET14+ | 3 | 压缩模式，输入框光标位置发生变化时也会触发避让。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| NONE14+ | 4 | 不避让键盘。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## SwiperDynamicSyncSceneType12+

枚举值，表示动态帧率场景的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GESTURE | 0 | 手势操作场景。 |
| ANIMATION | 1 | 动画过渡场景。 |

## MarqueeDynamicSyncSceneType14+

枚举值，表示Marquee的动态帧率场景的类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ANIMATION | 1 | 动画过渡场景。 |

## NodeRenderState20+

节点的渲染状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ABOUT\_TO\_RENDER\_IN | 0 | 该节点已挂载到渲染树上，通常会在下一帧渲染并对用户可见，但节点被渲染不代表一定可见。 |
| ABOUT\_TO\_RENDER\_OUT | 1 | 该节点已从渲染树中删除，一般下一帧不会被渲染，用户将不会看到此节点。 |

## GestureActionPhase20+

此枚举类型表示手势回调触发阶段，对应gesture.d.ts中定义的动作回调，但不同手势类型支持的阶段不同（如SwipeGesture仅包含WILL\_START枚举值）。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WILL\_START | 0 | 手势已被系统成功识别，将立即触发onActionStart或onAction回调。若手势绑定了onActionStart，则在onActionStart处触发；若手势绑定了onAction，则在onAction处触发；若两者同时绑定，则优先在onActionStart处触发；若两者均未绑定，则不会触发任何回调。具有内置手势回调的容器（如滚动类容器）默认支持onActionStart或onAction回调触发机制，无需显式绑定即可触发回调。 |
| WILL\_END | 1 | 表示手势已被判定为结束状态（通常发生在用户抬起手指终止交互时）。onActionEnd回调将立即触发，但手势必须显式绑定onActionEnd。具有内置手势回调的容器（如滚动类容器）默认支持手势结束状态判定，无需显式绑定即可触发onActionEnd回调。 |

## GestureListenerType20+

此枚举类型用于指定需要监控的手势类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TAP | 0 | 点击手势。 |
| LONG\_PRESS | 1 | 长按手势。 |
| PAN | 2 | 平移手势。 |
| PINCH | 3 | 捏合手势。 |
| SWIPE | 4 | 滑动手势。 |
| ROTATION | 5 | 旋转手势。 |

## ResolveStrategy22+

UIContext对象的解析策略。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CALLING\_SCOPE | 0 | 获取调用作用域的UIContext。 |
| LAST\_FOCUS | 1 | 获取最近切换到获焦状态的UIContext。 |
| MAX\_INSTANCE\_ID | 2 | 获取实例ID最大的UIContext。 |
| UNIQUE | 3 | 获取唯一UI实例的UIContext。 |
| LAST\_FOREGROUND | 4 | 获取最近切换到前台状态的UIContext。 |
| UNDEFINED | 5 | 获取未定义调用作用域的UIContext。 |

## CustomKeyboardContinueFeature23+

指定自定义键盘切换时是否接续。

设置为接续，切换输入框时，自定义键盘不会收起和重新拉起。

设置为不接续，切换输入框时，自定义键盘会收起并重新拉起。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENABLED | 0 | 接续。 |
| DISABLED | 1 | 不接续。 |

## TextSelectionClearPolicy

文本选择清除策略枚举。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KEEP\_SELECTED\_TEXT\_ON\_EXTERNAL\_TOUCH | 0 | 触摸到文本组件外部时，保留文本选中和手柄。 |
| CLEAR\_SELECTED\_TEXT\_ON\_EXTERNAL\_TOUCH | 1 | 触摸到文本组件外部时，清除文本选中和手柄。 |
