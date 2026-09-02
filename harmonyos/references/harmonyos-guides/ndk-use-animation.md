---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-use-animation
title: 动画概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用动画 > 动画概述
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:52+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:07df78e4c52f3a9195f13bd52c4398991b1ed9ec13850cd2d983cb4a237769e0
---

[ArkUI](arkui-overview.md)开发框架在[NDK](ndk-development-overview.md)接口里提供了动画相关接口，能够在应用中使用C和C++代码实现高效精致的动画效果，其中包括属性动画，组件出现/消失转场，一镜到底转场，关键帧动画，同时支持通过Node-API桥接ArkTS侧帧动画能力，覆盖Native端UI开发中绝大多数动效场景。其核心动画能力主要包括：

* **属性动画**

  [属性动画](arkts-attribute-animation-overview.md)是指部分属性（如尺寸属性、布局属性、位置属性等多种类型）的变化引起的UI的变化，添加属性动画可以让属性值从起点逐渐变化到终点，从而产生连续的动画效果。利用提供的全局[animateTo](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto)显式动画接口可以实现属性动画，通过在闭包函数中设置状态变化，系统就会自动插入过渡动画。对于改变布局类属性（如宽高）的动画，内容通常会直接跳转到最终状态，例如文字。如果希望内容跟随宽高变化，可以使用[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_RENDER\_FIT属性进行配置。具体使用场景可参考示例[使用属性动画](ndk-use-animation-scene.md#使用属性动画)。
* **组件出现/消失转场**

  [组件出现/消失转场](arkts-enter-exit-transition.md)主要用于容器组件中插入和删除子组件时，自动触发入场/出场过渡动效，提升用户体验。支持通过[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_ROTATE\_TRANSITION、NODE\_SCALE\_TRANSITION、NODE\_TRANSLATE\_TRANSITION、NODE\_OPACITY\_TRANSITION、NODE\_MOVE\_TRANSITION属性配置转场参数，分别对应旋转、缩放、位移、透明度、移动五种转场类型，支持独立配置转场动画的时长、动画曲线等，且无需手动控制动画启停，组件上下树时自动触发对应动效。具体使用场景可参考示例[组件出现/消失转场](ndk-use-animation-scene.md#组件出现消失转场)。
* **一镜到底转场**

  [一镜到底转场](arkts-shared-element-transition.md)主要用于界面切换时对相同或者相似的两个元素做的一种位置和大小匹配的过渡动画效果，也称一镜到底动效。一镜到底的效果能够让两个元素的出现消失产生联动，使得内容切换过程灵动自然而不生硬。

  [ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_GEOMETRY\_TRANSITION属性用于组件内隐式共享元素转场，在视图状态切换过程中提供丝滑的上下文继承过渡体验。通过[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_GEOMETRY\_TRANSITION属性为两个组件绑定同一id，这样在移除一个组件并添加另一个组件的时候，系统会对二者切换添加一镜到底动效。通过绑定两个对象的实现方式使得[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_GEOMETRY\_TRANSITION属性区别于其他方法，最适合用于两个不同对象之间完成一镜到底。具体使用场景可参考示例[一镜到底转场](ndk-use-animation-scene.md#一镜到底转场)。
* **关键帧动画**

  关键帧动画通过[keyframeAnimateTo](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#keyframeanimateto)接口来指定若干个关键帧状态，实现分段式、多阶段的复杂动画效果，支持为不同关键帧节点独立设置动画时长，实现非线性、多节奏的动效变化。可以自定义整体动画的循环播放次数、期望帧率范围，支持每个关键帧的状态变更闭包与全局动画结束回调，用于适配更复杂的动效开发场景。具体使用场景可参考示例[使用关键帧动画](ndk-use-animation-scene.md#使用关键帧动画)。
* **帧动画**

  [帧动画](arkts-animator.md)具有逐帧回调的特性，便于开发者在每一帧中调整所需属性。通过提供[OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback](../harmonyos-references/capi-native-animate-h.md#oh_arkui_animatoroption_registeronframecallback)逐帧回调函数，帧动画允许开发者在应用的每一帧设置属性值，从而实现组件属性值变化的自然过渡，营造出流畅的动画效果。帧动画接口可参考[createAnimator](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#createanimator)。

  与属性动画相比，帧动画能让开发者实时感知动画进程，即时调整UI值，并具备事件即时响应和可暂停的优势，但在性能方面略逊于属性动画。当属性动画能满足需求时，建议优先采用属性动画接口实现。[animateTo](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto)接口的使用可参考[使用属性动画](ndk-use-animation-scene.md#使用属性动画)。帧动画具体使用场景可参考示例[使用帧动画](ndk-use-animation-scene.md#使用帧动画)。
