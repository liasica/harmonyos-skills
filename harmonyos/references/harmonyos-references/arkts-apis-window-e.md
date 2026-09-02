---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-e
title: Enums
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 窗口管理 > @ohos.window (窗口) > Enums
category: harmonyos-references
scraped_at: 2026-09-02T15:00:52+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e1eda88fc91b32635fa8000734be40425c6654818d5911ad6160f70162aececa
---

**说明** 

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

## WindowType7+

窗口类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_APP | 0 | 表示应用子窗口。  **模型约束：** 此接口仅可在FA模型下使用。 |
| TYPE\_SYSTEM\_ALERT(deprecated) | 1 | 表示系统告警窗口。  **说明：** 从API version 11开始废弃。  从API version 7开始支持。 |
| TYPE\_FLOAT9+ | 8 | 表示全局悬浮窗。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE\_DIALOG10+ | 16 | 表示模态窗口。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE\_MAIN18+ | 32 | 表示应用主窗口。  此窗口类型不支持在创建窗口时使用。 |

## WindowPostureMode

窗口姿态模式枚举。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DESKTOP\_MODE | 0 | 桌面模式。当满足以下条件时处于桌面模式：  1. 当前设备折叠状态为半折叠状态（[FoldStatus.FOLD\_STATUS\_HALF\_FOLDED](js-apis-display.md#foldstatus10)）；  2. 窗口所在屏幕通过[getLiveCreaseRegion()](js-apis-display.md#getlivecreaseregion20)获取的creaseRects宽度大于高度；  3. 窗口模式为全屏模式（[WindowStatusType.FULL\_SCREEN](arkts-apis-window-e.md#windowstatustype11)）或最大化模式（[WindowStatusType.MAXIMIZE](arkts-apis-window-e.md#windowstatustype11)）。  4. 屏幕折痕区域位于窗口显示区域内。 |

## AvoidAreaType7+

窗口内容的避让区域的类型枚举。

窗口内容做[沉浸式布局](../harmonyos-guides/immersive-window-feature.md#沉浸式布局)适配时，需要按照AvoidAreaType对应的[AvoidArea](arkts-apis-window-i.md#avoidarea7)做窗口内容避让。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_SYSTEM | 0 | 表示系统默认区域。通常表示状态栏区域，悬浮窗状态下的应用主窗中表示三点控制栏区域。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TYPE\_CUTOUT | 1 | 表示挖孔区域。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TYPE\_SYSTEM\_GESTURE9+ | 2 | 表示侧边返回手势区域。当前所有设备均无此类型避让区域。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TYPE\_KEYBOARD9+ | 3 | 表示固定态软键盘区域。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TYPE\_NAVIGATION\_INDICATOR11+ | 4 | 表示底部导航区域。当三键导航显示时，底部导航避让区域始终存在。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TYPE\_FLOAT\_NAVIGATION | 5 | 表示三键导航区域。需要调用[setFloatNavigationAvoidAreaEnabled()](arkts-apis-window-window.md#setfloatnavigationavoidareaenabled)接口使能后，才能获取到三键导航的避让区域，否则直接返回空的三键导航避让区域。  **系统能力：** SystemCapability.Window.SessionManager  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## SplitRatioPreference

窗口分屏比例的类型枚举。

该枚举应用于[应用内分屏场景](../harmonyos-guides/multi-window-support.md#应用内分屏)，不支持直板机拉起分屏。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EQUAL | 0 | 表示系统为主分屏和次分屏窗口分配同样大小的窗口比例。  未指定字段值时该字段为默认值。 |
| PRIMARY\_DOMINANT | 1 | 表示系统为主分屏窗口分配当前设备所允许的较大可用比例。 |
| SECONDARY\_DOMINANT | 2 | 表示系统为次分屏窗口分配当前设备所允许的较大可用比例。 |

**说明** 

* 底部导航与三键导航是两种不同的系统导航模式，用户可以通过**设置>系统>系统导航>更多设置**进行三键导航的自定义切换。
* 默认情况下，底部导航表现为导航条，三键导航为关闭状态，此时三键导航区域不存在。
* 当用户切换为三键导航栏模式时，三键导航区域存在，导航条会隐藏，但底部导航区域仍然存在。

## Orientation9+

窗口显示方向类型枚举。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 表示未定义方向模式，由系统判定。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| PORTRAIT | 1 | 表示竖屏显示模式。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LANDSCAPE | 2 | 表示横屏显示模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| PORTRAIT\_INVERTED | 3 | 表示反向竖屏显示模式。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LANDSCAPE\_INVERTED | 4 | 表示反向横屏显示模式。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION | 5 | 跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且不受控制中心的旋转开关控制。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_PORTRAIT | 6 | 跟随传感器自动竖向旋转，可以旋转到竖屏、反向竖屏，无法旋转到横屏、反向横屏，且不受控制中心的旋转开关控制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| AUTO\_ROTATION\_LANDSCAPE | 7 | 跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且不受控制中心的旋转开关控制。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_RESTRICTED | 8 | 跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且受控制中心的旋转开关控制。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 9 | 跟随传感器自动竖向旋转，可以旋转到竖屏、反向竖屏，无法旋转到横屏、反向横屏，且受控制中心的旋转开关控制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 | 跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且受控制中心的旋转开关控制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| LOCKED | 11 | 表示锁定模式，窗口显示方向与屏幕当前方向一致。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| AUTO\_ROTATION\_UNSPECIFIED12+ | 12 | 跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在某种设备，可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Window.SessionManager |
| USER\_ROTATION\_PORTRAIT12+ | 13 | 调用时临时旋转到竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在某种设备，可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Window.SessionManager |
| USER\_ROTATION\_LANDSCAPE12+ | 14 | 调用时临时旋转到横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在某种设备，可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Window.SessionManager |
| USER\_ROTATION\_PORTRAIT\_INVERTED12+ | 15 | 调用时临时旋转到反向竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在某种设备，可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Window.SessionManager |
| USER\_ROTATION\_LANDSCAPE\_INVERTED12+ | 16 | 调用时临时旋转到反向横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在某种设备，可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Window.SessionManager |
| FOLLOW\_DESKTOP12+ | 17 | 表示跟随桌面的旋转模式，如果桌面可以旋转则可旋转，桌面不可旋转则不可旋转。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Window.SessionManager |

## RectChangeReason12+

窗口矩形（窗口位置及窗口大小）变化的原因。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 默认值，表示窗口矩形变化的原因未定义。 |
| MAXIMIZE | 1 | 窗口进入最大化或全屏模式。 |
| RECOVER | 2 | 窗口从最大化模式、全屏模式或分屏模式恢复到自由悬浮窗口模式。 |
| MOVE | 3 | 窗口拖拽移动。 |
| DRAG | 4 | 窗口拖拽缩放。 |
| DRAG\_START | 5 | 窗口开始拖拽缩放。 |
| DRAG\_END | 6 | 窗口结束拖拽缩放。 |

## ColorSpace8+

色域模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认SRGB色域模式。 |
| WIDE\_GAMUT | 1 | 广色域模式。 |

## WindowEventType10+

窗口生命周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_SHOWN | 1 | 切到前台。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| WINDOW\_ACTIVE | 2 | 获焦状态。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| WINDOW\_INACTIVE | 3 | 失焦状态。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| WINDOW\_HIDDEN | 4 | 切到后台。  **系统能力：** SystemCapability.WindowManager.WindowManager.Core |
| WINDOW\_DESTROYED11+ | 7 | 窗口销毁。  **系统能力：** SystemCapability.Window.SessionManager |

## WindowStatusType11+

窗口模式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 表示应用未定义窗口模式。 |
| FULL\_SCREEN | 1 | 表示应用全屏模式。  [自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态下，窗口铺满整个屏幕，默认无dock栏、标题栏和状态栏显示。  可通过[maximize()](arkts-apis-window-window.md#maximize12)和[setTitleAndDockHoverShown()](arkts-apis-window-window.md#settitleanddockhovershown14)配置，当悬停到热区时是否显示标题栏和dock栏。  当maximize()和setTitleAndDockHoverShown()接口都调用时，以最后调用设置的效果为准。  非[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态下，窗口铺满整个屏幕，无标题栏和dock栏显示。可通过[setSpecificSystemBarEnabled()](arkts-apis-window-window.md#setspecificsystembarenabled11)配置是否显示状态栏。 |
| MAXIMIZE | 2 | 表示应用窗口最大化模式，[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态下，窗口铺满整个屏幕，不需要悬停就可以显示dock栏、状态栏和标题栏。非[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态下，不存在该状态。 |
| MINIMIZE | 3 | 表示应用窗口最小化模式。 |
| FLOATING | 4 | 表示应用自由悬浮窗口模式，窗口可以自由移动和缩放，适用于需要多窗口同时使用的场景。 |
| SPLIT\_SCREEN | 5 | 表示应用分屏模式，屏幕同时显示两个应用窗口，每个窗口占据屏幕的一半空间，适用于多任务并行处理的场景。 |

## PixelUnit22+

像素单位枚举。

物理像素单位和虚拟像素单位换算可使用[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)和[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PX | 0 | 物理像素单位（px）。 |
| VP | 1 | 虚拟像素单位（vp）。 |

## MaximizePresentation12+

窗口最大化时的布局枚举。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLLOW\_APP\_IMMERSIVE\_SETTING | 0 | 最大化时，跟随应用当前设置的全屏模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| EXIT\_IMMERSIVE | 1 | 最大化时，如果当前窗口设置了全屏模式会退出全屏模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ENTER\_IMMERSIVE | 2 | 最大化时，进入全屏模式，鼠标悬停在热区上显示窗口标题栏和dock栏。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ENTER\_IMMERSIVE\_DISABLE\_TITLE\_AND\_DOCK\_HOVER14+ | 3 | 最大化时，进入全屏模式，鼠标悬停在热区上不显示窗口标题栏和dock栏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## AcrossDisplayPresentation

折叠屏的跨屏策略枚举，用于控制折叠2in1设备在悬停态下主窗口最大化时的瀑布流模式行为。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLLOW\_ACROSS\_DISPLAY\_SETTING | 0 | 跟随当前跨屏策略设置。若未设置过跨屏策略，则使用系统默认策略：设备悬停态下，窗口进入单屏最大化（即窗口最大化时只在上半屏或下半屏显示）；展开态下，窗口最大化并在折回悬停态时保持瀑布流模式（即窗口跨上下两半屏显示）。 |
| ENTER\_ACROSS\_DISPLAY\_MODE | 1 | 设备悬停态下，窗口直接进入瀑布流模式；展开态下，窗口最大化并在折回悬停态时保持瀑布流模式。 |
| EXIT\_ACROSS\_DISPLAY\_MODE | 2 | 设备悬停态下，窗口退出瀑布流模式，进入单屏最大化；展开态下，窗口最大化并在折回悬停态时退出瀑布流模式。 |

## WindowAnimationCurve20+

窗口动画曲线类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINEAR | 0 | 表示动画从头到尾的速度都是相同的。  使用该曲线类型时[WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20)中duration必填。  使用该曲线类型时[WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20)中param选填，且不生效。 |
| INTERPOLATION\_SPRING | 1 | 表示插值器弹簧曲线，一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。动画时间由曲线参数决定，不受[WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20)中的duration参数控制。  使用该曲线类型时[WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20)中duration选填，且不生效。  使用该曲线类型时[WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20)中param必填。 |
| CUBIC\_BEZIER | 2 | 表示贝塞尔曲线。  使用该曲线类型时[WindowAnimationConfig](arkts-apis-window-i.md#windowanimationconfig20)中的param和duration为必填项。 |

## WindowTransitionType20+

窗口转场动画类型枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DESTROY | 0 | 表示窗口销毁时的转场动画。 |

## AnimationType20+

窗口动画类型枚举。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FADE\_IN\_OUT | 0 | 表示窗口动画类型为淡入淡出。淡入动画在窗口显示过程中生效，淡出动画在窗口隐藏过程中生效。 |

## WindowAnchor20+

窗口锚点枚举。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP\_START | 0 | 窗口左上角。 |
| TOP | 1 | 窗口上边界横向居中点。 |
| TOP\_END | 2 | 窗口右上角。 |
| START | 3 | 窗口左边界纵向居中点。 |
| CENTER | 4 | 窗口横向和纵向居中点。 |
| END | 5 | 窗口右边界纵向居中点。 |
| BOTTOM\_START | 6 | 窗口左下角。 |
| BOTTOM | 7 | 窗口下边界横向居中点。 |
| BOTTOM\_END | 8 | 窗口右下角。 |

## RotationChangeType19+

窗口旋转事件类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_WILL\_ROTATE | 0 | 窗口即将旋转。 |
| WINDOW\_DID\_ROTATE | 1 | 窗口旋转结束。 |

## RectType19+

窗口矩形区域坐标系类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RELATIVE\_TO\_SCREEN | 0 | 窗口矩形区域相对于屏幕坐标系。 |
| RELATIVE\_TO\_PARENT\_WINDOW | 1 | 窗口矩形区域相对于父窗口坐标系。 |

## GlobalWindowMode20+

窗口模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FULLSCREEN | 1 | 全屏窗口，二进制从右往左，第一个二进制位为1。 |
| SPLIT | 1 << 1 | 分屏窗口，二进制从右往左，第二个二进制位为1。 |
| FLOAT | 1 << 2 | 自由悬浮窗口，二进制从右往左，第三个二进制位为1。 |
| PIP | 1 << 3 | 画中画，二进制从右往左，第四个二进制位为1。 |

## OcclusionState22+

窗口可见性状态枚举。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_OCCLUSION | 0 | 窗口完全可见（没有任何部分被其他非透明窗口遮挡）。 |
| PARTIAL\_OCCLUSION | 1 | 窗口部分可见（部分被其他非透明窗口遮挡）。 |
| FULL\_OCCLUSION | 2 | 窗口完全不可见（完全被其他非透明窗口遮挡，或窗口最小化，或窗口隐藏）。 |

## WindowStageEventType9+

WindowStage生命周期状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOWN | 1 | 前台状态，例如点击应用图标启动，无论是首次启动还是从后台启动均会触发。 |
| ACTIVE | 2 | 获焦状态，例如应用窗口处理点击事件后的状态、应用启动后的状态。 |
| INACTIVE | 3 | 失焦状态，例如打开新应用或点击其他窗口后，原获焦窗口的状态。 |
| HIDDEN | 4 | 后台状态，例如应用上滑退出、应用窗口关闭。 |
| RESUMED11+ | 5 | 前台可交互状态，例如打开应用后，应用处于前台，且可以与用户交互的状态。 |
| PAUSED11+ | 6 | 前台不可交互状态，例如应用在前台时，进入多任务界面，应用依然处于前台但不可以与用户交互的状态。 |

## WindowStageLifecycleEventType20+

WindowStage生命周期的状态类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOWN | 1 | 切到前台，例如点击应用图标启动，无论是首次启动还是从后台启动均会触发。 |
| RESUMED | 2 | 前台可交互状态，例如打开应用后，应用处于前台，且可以与用户交互的状态。 |
| PAUSED | 3 | 前台不可交互状态，例如应用在前台时，进入多任务界面，应用依然处于前台但不可以与用户交互的状态。 |
| HIDDEN | 4 | 切到后台，例如应用上滑退出、应用窗口关闭。 |

## ModalityType14+

子窗口模态类型枚举。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_MODALITY | 0 | 当仅需要其父级窗口不响应用户操作时，可选此参数。 |
| APPLICATION\_MODALITY | 1 | 除其父级窗口外还需要该应用其他实例的窗口不响应用户操作时，可选此参数。  **设备行为差异：** 该枚举在支持并处于[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态的设备及不支持[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态的设备上调用返回801错误码。 |

## ScreenshotEventType20+

截屏事件类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM\_SCREENSHOT | 0 | 系统截屏成功。 |
| SYSTEM\_SCREENSHOT\_ABORT | 1 | 系统截屏中止。 |
| SCROLL\_SHOT\_START | 2 | 滚动截屏开始。 |
| SCROLL\_SHOT\_END | 3 | 滚动截屏结束。 |
| SCROLL\_SHOT\_ABORT | 4 | 滚动截屏中止。 |

## OrientationExecutionResult

窗口显示方向的执行结果枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORIENTATION\_APPLIED | 0 | 设置的方向已生效。 |
| ORIENTATION\_IGNORED | 1 | 设置的方向不生效。 |
| ORIENTATION\_PENDING | 2 | 设置的方向被挂起，等系统动画结束后，将生效。 |

## RotationInfoType23+

旋转信息类型枚举。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_ORIENTATION | 0 | 窗口所在屏幕的显示方向，以窗口模块对横竖屏的定义方式表示。  开发者在使用时，需要注意该方向表示[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19)中的orientation参数。 |
| DISPLAY\_ORIENTATION | 1 | 屏幕显示方向，以屏幕模块对横竖屏的定义方式表示。  开发者在使用时，需要注意该方向表示[display](js-apis-display.md#display)对象的orientation属性。 |
| DISPLAY\_ROTATION | 2 | 设备的屏幕顺时针旋转角度。  开发者在使用时，需要注意该方向表示[display](js-apis-display.md#display)对象的rotation属性。 |
