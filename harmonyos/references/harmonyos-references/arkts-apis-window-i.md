---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i
title: Interfaces (其他)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 窗口管理 > @ohos.window (窗口) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d763a37ceeb215a8651f0768f5ecee0ccac36265340c06e684e61c86b0af855
---

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

## Configuration9+

PhonePC/2in1TabletTVWearable

创建子窗口或系统窗口时的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 窗口名称。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| windowType | [WindowType](arkts-apis-window-e.md#windowtype7) | 否 | 否 | 窗口类型。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| ctx | [BaseContext](js-apis-inner-application-basecontext.md) | 否 | 是 | 当前应用上下文信息。不设置，则默认为空。  FA模型下不需要使用该参数，即可创建子窗口，使用该参数时会报错。  Stage模型必须使用该参数，用于创建悬浮窗、模态窗或系统窗口。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| displayId | number | 否 | 是 | 当前屏幕ID。不设置，则默认为父窗口屏幕ID。  该参数应为非负整数，且对应屏幕ID存在。  扩展屏、异源虚拟屏场景下，全局悬浮窗可通过设置屏幕ID显示在指定屏幕上。  模态窗、系统窗设置屏幕ID无效，默认为父窗口屏幕ID。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| parentId | number | 否 | 是 | 父窗口ID。不设置，则默认为-1，默认父窗为当前应用上下文对应主窗。  FA模型下，该参数应为非负整数，且对应父窗口ID存在。  Stage模型下，该参数设置无效。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| decorEnabled12+ | boolean | 否 | 是 | 是否显示窗口装饰，仅在windowType为TYPE\_DIALOG时生效。true表示显示，false表示不显示。此参数默认值为false。  **系统能力：** SystemCapability.Window.SessionManager |
| title12+ | string | 否 | 是 | decorEnabled属性设置为true时，窗口的标题内容。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。不设置，则默认为空字符串。  **系统能力：** SystemCapability.Window.SessionManager |

## SystemBarProperties

PhonePC/2in1TabletTVWearable

状态栏属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| statusBarColor | string | 否 | 是 | 状态栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。默认值：'#66000000'。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isStatusBarLightIcon7+ | boolean | 否 | 是 | 状态栏图标是否为高亮状态。true表示高亮；false表示不高亮。默认值：false。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| statusBarContentColor8+ | string | 否 | 是 | 状态栏文字颜色。当设置此属性后，isStatusBarLightIcon属性设置无效。默认值：'#E5FFFFFF'。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| navigationBarColor | string | 否 | 是 | 三键导航栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。默认值：'#66000000'。  HarmonyOS各设备不支持此能力。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isNavigationBarLightIcon7+ | boolean | 否 | 是 | 三键导航栏图标是否为高亮状态。true表示高亮；false表示不高亮。默认值：false。  HarmonyOS各设备不支持此能力。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| navigationBarContentColor8+ | string | 否 | 是 | 三键导航栏文字颜色。当设置此属性后，isNavigationBarLightIcon属性设置无效。默认值：'#E5FFFFFF'。  HarmonyOS各设备不支持此能力。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| enableStatusBarAnimation12+ | boolean | 否 | 是 | 是否启用状态栏属性变化时的动画效果。true表示启用；false表示不启用。默认值：false。  **系统能力：** SystemCapability.Window.SessionManager |
| enableNavigationBarAnimation12+ | boolean | 否 | 是 | 是否启用三键导航栏属性变化时的动画效果。true表示启用；false表示不启用。默认值：false。  HarmonyOS各设备不支持此能力。  **系统能力：** SystemCapability.Window.SessionManager |

## StatusBarProperty18+

PhonePC/2in1TabletTVWearable

状态栏的属性。在获取状态栏属性信息时返回。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| contentColor | string | 否 | 否 | 状态栏文字颜色，固定为ARGB格式，如：#E5FFFFFF。  **系统能力：** SystemCapability.Window.SessionManager |

## SystemBarStyle12+

PhonePC/2in1TabletTVWearable

状态栏的属性。在设置页面级状态栏属性时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| statusBarContentColor | string | 否 | 是 | 状态栏文字颜色。默认值：'#E5FFFFFF'。 |

## FrameMetrics22+

PhonePC/2in1TabletTVWearable

帧率指标。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| firstDrawFrame | boolean | 否 | 否 | 是否是首帧。true表示首帧，false表示非首帧。 |
| inputHandlingDuration | number | 否 | 否 | 一帧中的手势处理耗时（单位：纳秒）。 |
| layoutMeasureDuration | number | 否 | 否 | 一帧中的布局测量耗时（单位：纳秒）。 |
| vsyncTimestamp | number | 否 | 否 | 当前帧的开始时间戳（单位：纳秒）。 |

## Rect7+

PhonePC/2in1TabletTVWearable

窗口矩形区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 矩形区域的左边界，单位为px，该参数为整数。 |
| top | number | 否 | 否 | 矩形区域的上边界，单位为px，该参数应为整数。 |
| width | number | 否 | 否 | 矩形区域的宽度，单位为px，该参数应为整数。 |
| height | number | 否 | 否 | 矩形区域的高度，单位为px，该参数应为整数。 |

## RectInVP23+

PhonePC/2in1TabletTVWearable

窗口矩形区域，单位为vp。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 矩形区域的左边界值，单位为vp。 |
| top | number | 否 | 否 | 矩形区域的上边界值，单位为vp。 |
| width | number | 否 | 否 | 矩形区域的宽度，单位为vp。 |
| height | number | 否 | 否 | 矩形区域的高度，单位为vp。 |

## AvoidArea7+

PhonePC/2in1TabletTVWearable

窗口内容的避让区域。

窗口内容做[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)适配时，需要按照[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)对应的AvoidArea做窗口内容避让。

在避让区域内，应用窗口内容被遮挡且无法响应用户点击事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| visible9+ | boolean | 否 | 否 | 避让区域是否可见。true表示可见；false表示不可见。 |
| leftRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 中心位于窗口的两条对角线的左侧的矩形区。 |
| topRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 中心位于窗口的两条对角线的顶部的矩形区。 |
| rightRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 中心位于窗口的两条对角线的右侧的矩形区。 |
| bottomRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 中心位于窗口的两条对角线的底部的矩形区。 |

说明

示意图展示了leftRect、topRect、rightRect、bottomRect的含义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/JT7KYqnTT_mPHVJMvprubA/zh-cn_image_0000002552959460.png?HW-CC-KV=V1&HW-CC-Date=20260428T000042Z&HW-CC-Expire=86400&HW-CC-Sign=FBB3FE5D1B8290DCA921C33B076217B97884FE7EE127886D91E59922BC2A0565)

## UIEnvAvoidAreaVP23+

PhonePC/2in1TabletTVWearable

以vp为单位表示的窗口避让区域信息，在进行[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)适配时需关注。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| visible | boolean | 否 | 否 | 避让区域是否可见。true表示可见；false表示不可见。 |
| leftRect | [RectInVP](arkts-apis-window-i.md#rectinvp23) | 否 | 否 | 中心位于窗口的两条对角线的左侧的矩形区，单位为vp。 |
| topRect | [RectInVP](arkts-apis-window-i.md#rectinvp23) | 否 | 否 | 中心位于窗口的两条对角线的顶部的矩形区，单位为vp。 |
| rightRect | [RectInVP](arkts-apis-window-i.md#rectinvp23) | 否 | 否 | 中心位于窗口的两条对角线的右侧的矩形区，单位为vp。 |
| bottomRect | [RectInVP](arkts-apis-window-i.md#rectinvp23) | 否 | 否 | 中心位于窗口的两条对角线的底部的矩形区，单位为vp。 |

## UIEnvWindowAvoidAreaInfoPX23+

PhonePC/2in1TabletTVWearable

窗口不同类型避让区域信息组成的[环境变量](../harmonyos-guides/arkts-env-system-property.md)数据类型，每种类型避让区域单位为px。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| statusBar | [AvoidArea](arkts-apis-window-i.md#avoidarea7) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_SYSTEM类型的避让区域，单位为px。 |
| cutout | [AvoidArea](arkts-apis-window-i.md#avoidarea7) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_CUTOUT类型的避让区域，单位为px。 |
| keyboard | [AvoidArea](arkts-apis-window-i.md#avoidarea7) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_KEYBOARD类型的避让区域，单位为px。 |
| navigationIndicator | [AvoidArea](arkts-apis-window-i.md#avoidarea7) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_NAVIGATION\_INDICATOR类型的避让区域，单位为px。 |

## UIEnvWindowAvoidAreaInfoVP23+

PhonePC/2in1TabletTVWearable

窗口不同类型避让区域信息组成的[环境变量](../harmonyos-guides/arkts-env-system-property.md)数据类型，每种类型避让区域单位为vp。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| statusBar | [UIEnvAvoidAreaVP](arkts-apis-window-i.md#uienvavoidareavp23) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_SYSTEM类型的避让区域，单位为vp。 |
| cutout | [UIEnvAvoidAreaVP](arkts-apis-window-i.md#uienvavoidareavp23) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_CUTOUT类型的避让区域，单位为vp。 |
| keyboard | [UIEnvAvoidAreaVP](arkts-apis-window-i.md#uienvavoidareavp23) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_KEYBOARD类型的避让区域，单位为vp。 |
| navigationIndicator | [UIEnvAvoidAreaVP](arkts-apis-window-i.md#uienvavoidareavp23) | 否 | 否 | 表示[AvoidAreaType](arkts-apis-window-e.md#avoidareatype7)为TYPE\_NAVIGATION\_INDICATOR类型的避让区域，单位为vp。 |

## Size7+

PhonePC/2in1TabletTVWearable

窗口大小，单位为px。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 窗口宽度，单位为px，该参数应为整数。 |
| height | number | 否 | 否 | 窗口高度，单位为px，该参数应为整数。 |

## SizeInVP23+

PhonePC/2in1TabletTVWearable

窗口大小，单位为vp。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 窗口宽度，单位为vp，该参数为浮点数。 |
| height | number | 否 | 否 | 窗口高度，单位为vp，该参数为浮点数。 |

## Position20+

PhonePC/2in1TabletTVWearable

窗口或组件的位置。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x坐标，单位为px，该参数应为整数。 |
| y | number | 否 | 否 | y坐标，单位为px，该参数应为整数。 |

## RectChangeOptions12+

PhonePC/2in1TabletTVWearable

窗口矩形（窗口位置及窗口大小）变化返回的值及变化原因。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 窗口矩形变化后的值。 |
| reason | [RectChangeReason](arkts-apis-window-e.md#rectchangereason12) | 否 | 否 | 窗口矩形变化的原因。 |

## AvoidAreaOptions12+

PhonePC/2in1TabletTVWearable

系统避让区变化后返回当前避让区域以及避让区域类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AvoidAreaType](arkts-apis-window-e.md#avoidareatype7) | 否 | 否 | 系统避让区变化后返回的避让区域类型。 |
| area | [AvoidArea](arkts-apis-window-i.md#avoidarea7) | 否 | 否 | 系统避让区变化后返回的避让区域。 |

## WindowProperties

PhonePC/2in1TabletTVWearable

窗口属性。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowRect7+ | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 窗口尺寸，其中左边界上边界是相对于窗口所在屏幕左上顶点计算，可在页面生命周期[onPageShow](ts-custom-component-lifecycle.md#onpageshow)或应用生命周期[onForeground](js-apis-app-ability-uiability.md#onforeground)阶段获取。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| drawableRect11+ | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 窗口内的可绘制区域尺寸，其中左边界上边界是相对于窗口左上顶点计算。在Stage模型下，需要在调用[loadContent()](arkts-apis-window-window.md#loadcontent9)或[setUIContent()](arkts-apis-window-window.md#setuicontent9)加载页面内容后获取该属性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| type7+ | [WindowType](arkts-apis-window-e.md#windowtype7) | 否 | 否 | 窗口类型。  当前存在主窗使用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)接口返回type不准确的问题，开发者在创建窗口时已指明窗口类型，无需通过getWindowProperties()接口获取窗口类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isFullScreen | boolean | 否 | 否 | 在满足isLayoutFullScreen为true的条件下如果隐藏了状态栏，返回值为true，其他情况下均返回false。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isLayoutFullScreen7+ | boolean | 否 | 否 | 对于子窗，如果设置了[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)，返回值为true。  对于主窗，如果设置了[沉浸式布局](../harmonyos-guides/window-terminology.md#沉浸式布局)且处于全屏模式，返回值为true。  其他情况下均返回false  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| focusable7+ | boolean | 否 | 否 | 窗口是否可获焦。true表示可获焦；false表示不可获焦。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| touchable7+ | boolean | 否 | 否 | 窗口是否可触摸。true表示可触摸；false表示不可触摸。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| brightness | number | 否 | 否 | 窗口亮度。通过[setWindowBrightness()](arkts-apis-window-window.md#setwindowbrightness9)设置窗口的亮度值。该参数为浮点数，可设置的亮度范围为[0.0, 1.0]或-1.0，其取值1.0时表示最大亮度，取值-1.0时，表示亮度跟随系统。如果窗口没有设置亮度值，表示亮度跟随系统，此时获取到的亮度值为-1.0。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| dimBehindValue(deprecated) | number | 否 | 否 | 下层窗口的暗度值。该参数为浮点数，取值范围为[0.0, 1.0]，其取1.0表示最暗。  **说明：** 从API version 7开始支持，从API version 9开始废弃，当前无可替代接口。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isKeepScreenOn | boolean | 否 | 否 | 屏幕是否常亮。true表示常亮；false表示不常亮。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isPrivacyMode7+ | boolean | 否 | 否 | 窗口是否为隐私模式。true表示窗口为隐私模式；false表示窗口为非隐私模式。可通过[setWindowPrivacyMode()](arkts-apis-window-window.md#setwindowprivacymode9)设置窗口的隐私模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isRoundCorner(deprecated) | boolean | 否 | 否 | 窗口是否为圆角。true表示窗口为圆角；false表示窗口为非圆角。  **说明：** 从API version 7开始支持，从API version 9开始废弃，当前无可替代接口。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| isTransparent7+ | boolean | 否 | 否 | 窗口背景是否透明。true表示透明；false表示不透明。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| id9+ | number | 否 | 否 | 窗口ID，该参数为整数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| displayId12+ | number | 否 | 是 | 窗口所在屏幕ID，默认返回主屏幕ID，该参数为整数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| name18+ | string | 否 | 是 | 窗口名称，默认为空字符串。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| globalDisplayRect20+ | [Rect](arkts-apis-window-i.md#rect7) | 否 | 是 | 全局坐标系下的窗口尺寸。扩展屏场景下以主屏左上角为坐标原点，虚拟屏场景下以虚拟屏左上角为坐标原点。默认值：[0, 0, 0, 0]。  **系统能力：** SystemCapability.Window.SessionManager |

## DecorButtonStyle14+

PhonePC/2in1TabletTVWearable

系统装饰栏按钮样式。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorMode | [ConfigurationConstant.ColorMode](js-apis-app-ability-configurationconstant.md#colormode) | 否 | 是 | 颜色模式。深色模式下按钮颜色适配为浅色，浅色模式下按钮颜色适配为深色。未设置则默认跟随系统颜色模式。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| buttonBackgroundSize | number | 否 | 是 | 按钮高亮显示时的大小，取值范围20vp-40vp，默认值28vp。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| spacingBetweenButtons | number | 否 | 是 | 按钮间距，取值范围8vp-24vp，默认值12vp。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| closeButtonRightMargin | number | 否 | 是 | 关闭按钮右侧距窗口边距，取值范围6vp-22vp，默认值20vp。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| buttonIconSize20+ | number | 否 | 是 | 按键icon的大小，取值范围16vp-24vp，默认值20vp。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| buttonBackgroundCornerRadius20+ | number | 否 | 是 | 按键背板圆角半径，取值范围4vp-8vp，默认值4vp。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## WindowLimits11+

PhonePC/2in1TabletTVWearable

窗口尺寸限制参数，应用可以通过[getWindowLimits](arkts-apis-window-window.md#getwindowlimits11)获得当前窗口的尺寸限制（单位为px）；从API version 22开始，还可以通过[getWindowLimitsVP](arkts-apis-window-window.md#getwindowlimitsvp22)获取窗口尺寸限制（单位为vp）。

窗口尺寸限制的最终生效结果由默认系统限制、应用配置和运行时设置的数据取交集得到，优先级从高到低依次为：

1. 应用通过[setWindowLimits](arkts-apis-window-window.md#setwindowlimits11)设置窗口尺寸限制。
2. 应用在[startAbility](js-apis-inner-application-uiabilitycontext.md#startability-2)拉起窗口时通过[StartOptions](js-apis-app-ability-startoptions.md#startoptions)指定窗口尺寸限制（API version 17开始支持）。
3. 应用在[module.json5配置文件中的abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中配置windowLimits。
4. 默认系统限制（基于不同产品和窗口类型，其windowLimits系统默认限制存在差异）。

**系统能力：** SystemCapability.Window.SessionManager

说明

针对maxWidth、maxHeight、minWidth、minHeight属性：

* 默认单位为px，从API version 22开始支持通过pixelUnit设置单位为px或vp。
* 参数为整数，浮点数会向下取整。
* 默认值为0，表示属性不发生变化。
* 可生效范围下限值：系统限定的最小高度/宽度。
* 可生效范围上限值：系统限定的最大高度/宽度。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxWidth | number | 否 | 是 | 窗口的最大宽度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxHeight | number | 否 | 是 | 窗口的最大高度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| minWidth | number | 否 | 是 | 窗口的最小宽度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| minHeight | number | 否 | 是 | 窗口的最小高度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| pixelUnit22+ | [PixelUnit](arkts-apis-window-e.md#pixelunit22) | 否 | 是 | 窗口尺寸限制的单位，默认为px。可显式设置为px或vp。 |

## TitleButtonRect11+

PhonePC/2in1TabletTVWearable

标题栏上的最小化、最大化、关闭按钮矩形区域，该区域位置坐标相对窗口右上角。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| right | number | 否 | 否 | 矩形区域的右边界，单位为vp，该参数为整数。 |
| top | number | 否 | 否 | 矩形区域的上边界，单位为vp，该参数为整数。 |
| width | number | 否 | 否 | 矩形区域的宽度，单位为vp，该参数为整数。 |
| height | number | 否 | 否 | 矩形区域的高度，单位为vp，该参数为整数。 |

## MoveConfiguration15+

PhonePC/2in1TabletTVWearable

窗口移动选项。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| displayId | number | 否 | 是 | 目标屏幕ID，该参数应为整数，输入非整数时将向下取整。默认值为undefined。填入该参数时，将移动到相对于目标屏幕左上角的指定位置。此参数不传、传undefined或传入目标屏幕ID不存在时，将移动到相对于当前屏幕左上角的指定位置。 |

## WindowDensityInfo15+

PhonePC/2in1TabletTVWearable

窗口所在显示设备和窗口自定义的显示密度信息，是与像素单位无关的缩放系数，即显示大小缩放系数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| systemDensity | number | 否 | 否 | 窗口所在屏幕的系统显示大小缩放系数，跟随用户设置变化，该参数变化范围为0.5-4.0。 |
| defaultDensity | number | 否 | 否 | 窗口所在屏幕的系统默认显示大小缩放系数，跟随窗口所在屏幕变化，该参数变化范围为0.5-4.0。 |
| customDensity | number | 否 | 否 | 窗口自定义设置的显示大小缩放系数，该参数取值范围为0.5-4.0。未设置该参数时，将跟随系统显示大小缩放系数变化。该参数仅主窗口生效，在子窗或系统窗口上等于系统显示大小缩放系数(systemDensity)。 |

## WindowLayoutInfo15+

PhonePC/2in1TabletTVWearable

窗口布局信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 窗口尺寸，窗口在屏幕上的实际位置和大小。 |

## KeyboardInfo18+

PhonePC/2in1TabletTVWearable

软键盘窗口信息。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| beginRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 动画开始前软键盘的位置和大小。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| endRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 动画结束后软键盘的位置和大小。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| animated20+ | boolean | 否 | 是 | 当前是否有显示/隐藏动画，true表示有动画，false表示没有。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| config20+ | [WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20) | 否 | 是 | 动画配置信息。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ShowWindowOptions20+

PhonePC/2in1TabletTVWearable

显示子窗口或系统窗口时的参数。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| focusOnShow | boolean | 否 | 是 | 窗口调用[showWindow()](arkts-apis-window-window.md#showwindow20)显示时是否自动获焦，默认为true。该参数对主窗、模态窗、dialog窗口不生效。 |

## WindowAnimationConfig20+

PhonePC/2in1TabletTVWearable

窗口动画参数配置。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| curve | [WindowAnimationCurve](arkts-apis-window-e.md#windowanimationcurve20) | 否 | 否 | 动画曲线类型。 |
| duration | number | 否 | 是 | 动画播放的时长，单位毫秒（ms）。  默认值：0，最大值：3000。  根据动画曲线类型决定是否必填。 |
| param | [WindowAnimationCurveParam](arkts-apis-window-t.md#windowanimationcurveparam20) | 否 | 是 | 动画曲线参数，根据动画曲线类型决定是否必填。 |

## WindowInfo18+

PhonePC/2in1TabletTVWearable

当前窗口的详细信息。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 窗口尺寸。 |
| bundleName | string | 否 | 否 | 应用Bundle的名称。 |
| abilityName | string | 否 | 否 | Ability的名称。 |
| windowId | number | 否 | 否 | 窗口ID。 |
| windowStatusType | [WindowStatusType](arkts-apis-window-e.md#windowstatustype11) | 否 | 否 | 窗口模式枚举。 |
| isFocused | boolean | 否 | 是 | 窗口是否获焦。true表示窗口获焦；false表示窗口未获焦。返回值与[isFocused()](arkts-apis-window-window.md#isfocused12)接口一致。 |
| globalDisplayRect20+ | [Rect](arkts-apis-window-i.md#rect7) | 否 | 是 | 全局坐标系下的窗口尺寸。扩展屏场景下以主屏左上角为坐标原点，虚拟屏场景下以虚拟屏左上角为坐标原点。默认值：[0, 0, 0, 0]。 |

## TransitionAnimation20+

PhonePC/2in1TabletTVWearable

窗口转场动画配置。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| config | [WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20) | 否 | 否 | 本次转场动画配置。 |
| opacity | number | 否 | 是 | 不透明度，转场动画作用的窗口属性，值为0时窗口完全透明，默认值为1.0。当动画类型为WindowTransitionType.DESTROY时，代表动画终点的不透明度。取值范围0~1.0，在动画结束时恢复为1.0。 |

## StartAnimationParams20+

PhonePC/2in1TabletTVWearable

启动动画配置。

仅对同应用的不同ability间跳转生效。

仅对全屏应用生效。

**设备行为差异：** 该接口在Phone设备的非[自由多窗模式](../harmonyos-guides/window-terminology.md#自由多窗模式)、Tablet设备的非[自由多窗模式](../harmonyos-guides/window-terminology.md#自由多窗模式)且非电脑模式下可正常调用，在其他设备、[自由多窗模式](../harmonyos-guides/window-terminology.md#自由多窗模式)或电脑模式下调用不生效也不报错。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AnimationType](arkts-apis-window-e.md#animationtype20) | 否 | 否 | 窗口动画类型。 |

## WindowCreateParams20+

PhonePC/2in1TabletTVWearable

应用启动时的窗口参数配置。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| animationParams | [StartAnimationParams](arkts-apis-window-i.md#startanimationparams20) | 否 | 是 | 启动动画参数配置。默认值为undefined，若不配置将保持系统默认动效。 |
| needAnimation23+ | boolean | 否 | 是 | 是否启用窗口创建动效。  传入true时，跟随系统默认动效。传入false时，表示关闭窗口创建动效，仅在[自由窗口状态](../harmonyos-guides/window-terminology.md#自由窗口)的情况下生效。  此参数不填时，默认为undefined，跟随系统默认动效。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## Callback15+

PhonePC/2in1TabletTVWearable

### (data: T)15+

PhonePC/2in1TabletTVWearable

(data: T): V

通用回调函数。

开发者在使用时，可自定义data的参数类型，回调函数返回对应类型的信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 回调函数调用时需要传入T类型的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 回调函数需要返回V类型的返回值。 |

## RotationChangeInfo19+

PhonePC/2in1TabletTVWearable

窗口旋转变化时的窗口信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [RotationChangeType](arkts-apis-window-e.md#rotationchangetype19) | 否 | 否 | 窗口旋转事件类型。 |
| orientation | number | 否 | 否 | 窗口显示方向。  - 0表示竖屏。  - 1表示反向横屏。  - 2表示反向竖屏。  - 3表示横屏。  开发者在使用时，需要注意该方向与display对象的属性orientation含义不一致。 |
| displayId | number | 否 | 否 | 窗口所在屏幕Id。 |
| displayRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 窗口所在屏幕旋转后的矩形区域大小。 |

## RotationChangeResult19+

PhonePC/2in1TabletTVWearable

应用在窗口旋转变化时返回的信息，系统会根据此信息改变当前窗口矩形区域大小。当返回主窗口旋转变化的信息时，系统不改变主窗口的大小。

应用窗口与系统窗口大小存在限制，具体限制与相关规则可见[resize](arkts-apis-window-window.md#resize9)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rectType | [RectType](arkts-apis-window-e.md#recttype19) | 否 | 否 | 窗口矩形区域坐标系类型。 |
| windowRect | [Rect](arkts-apis-window-i.md#rect7) | 否 | 否 | 相对于屏幕或父窗坐标系的窗口矩形区域信息。 |

## SubWindowOptions11+

PhonePC/2in1TabletTVWearable

子窗口创建参数。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title11+ | string | 否 | 否 | 子窗口标题。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| decorEnabled11+ | boolean | 否 | 否 | 子窗口是否显示装饰。true表示子窗口显示装饰，false表示子窗口不显示装饰。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isModal12+ | boolean | 否 | 是 | 子窗口是否启用模态属性。true表示子窗口启用模态属性，false表示子窗口禁用模态属性。不设置，则默认为false。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| modalityType14+ | [ModalityType](arkts-apis-window-e.md#modalitytype14) | 否 | 是 | 子窗口模态类型，仅当子窗口启用模态属性时生效。不设置，则默认为WINDOW\_MODALITY。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| windowRect18+ | [Rect](arkts-apis-window-i.md#rect7) | 否 | 是 | 子窗口矩形区域，其中子窗口存在大小限制，具体参考[resize()](arkts-apis-window-window.md#resize9)方法。不设置且未调用[showWindow()](arkts-apis-window-window.md#showwindow9)显示前，则默认为{left: 0, top: 0, width: 0, height: 0}。具体参考[设置应用子窗口](../harmonyos-guides/application-window-stage.md#设置应用子窗口)开发指南。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| zLevel18+ | number | 否 | 是 | 子窗口层级级别，仅当子窗口未启用模态属性，即未设置isModal时生效。该参数是整数，取值范围为[-10000, 10000]，浮点数输入将向下取整。不设置，则默认为0。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| maximizeSupported19+ | boolean | 否 | 是 | 子窗口是否支持最大化特性。true表示子窗口支持最大化，false表示子窗口不支持最大化。不设置，则默认为false。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。  **设备行为差异：** 该参数在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上可正常调用；在不支持[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上，作为入参使用时，对应接口不生效不报错；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态的设备上，作为入参使用时，对应接口不生效不报错，切换到[自由窗口](../harmonyos-guides/window-terminology.md#自由窗口)状态后生效。 |
| outlineEnabled20+ | boolean | 否 | 是 | 子窗口是否显示描边。true表示子窗口显示描边，false表示子窗口不显示描边。不设置，则默认为false。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。  **设备行为差异：** 该参数在2in1设备、其他设备的电脑模式中可正常调用，在其他设备和其他模式中作为入参使用时，对应接口不生效不报错。 |

## KeyFramePolicy20+

PhonePC/2in1TabletTVWearable

关键帧的策略配置。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enable | boolean | 否 | 否 | 是否开启关键帧。true表示开启，false表示关闭。 |
| interval | number | 否 | 是 | 设置关键帧布局切换的拖拽时间间隔，单位为毫秒，默认值为1000。取值为正整数，浮点数向下取整。与distance判断为或的关系：满足其一即开始布局切换。 |
| distance | number | 否 | 是 | 设置关键帧布局切换的拖拽距离间隔，单位为px，默认值为1000。取值为0或正整数，浮点数向下取整。设置为0时，忽略拖拽距离因素。与interval判断为或的关系：满足其一即开始布局切换。 |
| animationDuration | number | 否 | 是 | 设置关键帧布局的动效切换时间，单位为毫秒，默认值为100。取值为0或正整数，浮点数向下取整。 |
| animationDelay | number | 否 | 是 | 设置关键帧布局切换动效延迟时间，单位为毫秒，默认值为100。取值为0或正整数，浮点数向下取整。 |

## MainWindowInfo21+

PhonePC/2in1TabletTVWearable

主窗口信息。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| displayId | number | 否 | 否 | 主窗口所在的屏幕ID。 |
| windowId | number | 否 | 否 | 主窗口ID。 |
| showing | boolean | 否 | 否 | 主窗口的前后台状态。true表示主窗口在前台，false表示主窗口不在前台。 |
| label | string | 否 | 否 | 主窗口的任务名称。 |

## WindowSnapshotConfiguration21+

PhonePC/2in1TabletTVWearable

主窗口截图的配置项。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| useCache | boolean | 否 | 是 | 是否使用主窗口的已有截图。默认值为true。 true表示使用主窗口的已有截图，若主窗口无保存的截图，则使用主窗口的最新截图。false表示使用主窗口的最新截图。 |
