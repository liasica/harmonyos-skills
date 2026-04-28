---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-i
title: Interfaces (其他)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:54b1db5e496aff69f61e1bf897f33a3ca0abfae94c5cff1da6a38c3d4f802093
---

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## TargetInfo18+

PhonePC/2in1TabletTVWearable

指定组件绑定的目标节点。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | number | 否 | 否 | 指定popup或menu绑定的目标节点。  **说明：**  1. 当id是number时，对应组件实例的UniqueID，此id由系统保证唯一性。  2. 当id是string时，对应[通用属性id](ts-universal-attributes-component-id.md#id)所指定的组件，此id的唯一性需由开发者确保，但实际可能会有多个。 |
| componentId | number | 否 | 是 | 目标节点所在的自定义组件的UniqueID。当上述id指定为string类型时，可通过此属性圈定范围。方便开发者在一定范围内保证id: string的唯一性。 |

## PageInfo12+

PhonePC/2in1TabletTVWearable

Router和NavDestination等页面信息，若无对应的Router或NavDestination页面信息，则对应属性为undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| routerPageInfo | observer.[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo) | 否 | 是 | Router信息。 |
| navDestinationInfo | observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo) | 否 | 是 | NavDestination信息。 |

## OverlayManagerOptions15+

PhonePC/2in1TabletTVWearable

初始化[OverlayManager](arkts-apis-uicontext-overlaymanager.md)时所用参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| renderRootOverlay | boolean | 否 | 是 | 是否渲染overlay根节点，true表示渲染overlay根节点，false表示不渲染overlay根节点，默认值为true。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| enableBackPressedEvent19+ | boolean | 否 | 是 | 是否支持通过侧滑手势关闭OverlayManager下的ComponentContent，true表示可以通过侧滑关闭，false表示不可以通过侧滑关闭，默认值为false。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## GestureTriggerInfo20+

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

该参数用于指定需要监听的手势回调阶段（传入空数组将无效），仅当手势触发指定阶段时才会发送通知。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| actionPhases | Array<[GestureActionPhase](arkts-apis-uicontext-e.md#gestureactionphase20)> | 否 | 否 | 手势事件对象。 |

## SwiperContentInfo22+

PhonePC/2in1TabletTVWearable

Swiper组件的内容区信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | Swiper组件的id。 |
| uniqueId | number | 否 | 否 | Swiper组件的唯一标识符。 |
| swiperItemInfos | Array<[SwiperItemInfo](arkts-apis-uicontext-i.md#swiperiteminfo22)> | 否 | 否 | 当前处于显示状态的Swiper子组件的信息。 |

## SwiperItemInfo22+

PhonePC/2in1TabletTVWearable

Swiper子组件的信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniqueId | number | 否 | 否 | Swiper子组件的唯一标识符。 |
| index | number | 否 | 否 | Swiper子组件在Swiper中的索引。 |
