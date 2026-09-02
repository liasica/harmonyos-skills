---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-i
title: Interfaces (其他)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:840201642538e59870c300d87e9c26015f950e59832e3ed2bfa2ed321d29157c
---

本文汇总ArkUI UIContext相关的其他接口，用于描述组件目标节点、页面信息、OverlayManager初始化参数、手势触发信息及Swiper内容区信息等。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## TargetInfo18+

指定组件绑定的目标节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | number | 否 | 否 | 指定popup或menu绑定的目标节点。  **说明：**  1. 当id是number时，对应组件实例的UniqueID，此id由系统保证唯一性。  2. 当id是string时，对应[通用属性id](ts-universal-attributes-component-id.md#id)所指定的组件，此id的唯一性需由开发者确保，但实际会有存在多个相同id的组件的可能性。 |
| componentId | number | 否 | 是 | 目标节点所在的自定义组件的UniqueID。当上述id指定为string类型且需要在指定自定义组件范围内查找目标节点时，可通过此属性圈定范围，方便开发者在一定范围内保证id: string的唯一性。默认不指定自定义组件范围。 |

## PageInfo12+

Router和NavDestination等页面信息，若无对应的Router或NavDestination页面信息，则对应属性为undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| routerPageInfo | observer.[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo) | 否 | 是 | Router信息。 |
| navDestinationInfo | observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo) | 否 | 是 | NavDestination信息。 |

## OverlayManagerOptions15+

初始化[OverlayManager](arkts-apis-uicontext-overlaymanager.md)时所用参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| renderRootOverlay | boolean | 否 | 是 | 是否渲染overlay根节点，true表示渲染overlay根节点，false表示不渲染overlay根节点，默认值为true。通过将该参数设置为false，可以解决[OverlayManager](arkts-apis-uicontext-overlaymanager.md)显示在[PhotoPickerComponent](ohos-file-photopickercomponent.md)上层时，PhotoPickerComponent无法选中照片的问题。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| enableBackPressedEvent19+ | boolean | 否 | 是 | 是否支持通过侧滑手势关闭OverlayManager下的ComponentContent，true表示可以通过侧滑关闭，false表示不可以通过侧滑关闭，默认值为false。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onBackPress | [OnOverlayBackPressCallback](arkts-apis-uicontext-t.md#onoverlaybackpresscallback) | 否 | 是 | 拦截Overlay侧滑返回事件的回调。  **说明：**  1. 注册该回调且**enableBackPressedEvent**设置为true时，侧滑返回事件不会自动关闭Overlay，而是调用该回调决定事件是否向下层组件传递。  2. 返回true表示拦截该事件（事件被消费，不会向下层传递）；返回false表示不拦截，事件将向下层组件透传。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## GestureTriggerInfo20+

特定手势回调函数触发时的信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | [GestureEvent](ts-gesture-common.md#gestureevent对象说明) | 否 | 否 | 手势事件对象。 |
| current | [GestureRecognizer](ts-gesture-common.md#gesturerecognizer12) | 否 | 否 | 手势识别器对象。可从中获取手势的详细信息，但请勿在本地保留此对象，因为当节点释放后该对象可能失效。 |
| currentPhase | [GestureActionPhase](arkts-apis-uicontext-e.md#gestureactionphase20) | 否 | 否 | 手势动作回调阶段。 |
| node | [FrameNode](js-apis-arkui-framenode.md) | 否 | 是 | 触发手势的节点。默认值为null，表示没有触发手势的节点。 |

## GestureObserverConfigs20+

该参数用于指定需要监听的手势回调阶段（传入空数组时不监听任何手势回调阶段），仅当手势触发指定阶段时才会发送通知。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| actionPhases | Array<[GestureActionPhase](arkts-apis-uicontext-e.md#gestureactionphase20)> | 否 | 否 | 需要监听的手势回调阶段。传入空数组将无效，仅当手势触发指定阶段时才会发送通知。 |

## SwiperContentInfo22+

Swiper组件的内容区信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | Swiper组件的id。 |
| uniqueId | number | 否 | 否 | Swiper组件的唯一标识符。 |
| swiperItemInfos | Array<[SwiperItemInfo](arkts-apis-uicontext-i.md#swiperiteminfo22)> | 否 | 否 | 当前处于显示状态的Swiper子组件的信息。 |

## SwiperItemInfo22+

Swiper子组件的信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniqueId | number | 否 | 否 | Swiper子组件的唯一标识符。 |
| index | number | 否 | 否 | Swiper子组件在Swiper中的索引。 |
