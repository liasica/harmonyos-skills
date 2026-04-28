---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-t
title: Types
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 窗口管理 > @ohos.window (窗口) > Types
category: harmonyos-references
scraped_at: 2026-04-28T08:00:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a7c6e7712d0006951d2316062eebcb3503dd81e3922a4d1085e3b08045f944b
---

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

## SpecificSystemBar11+

PhonePC/2in1TabletTVWearable

type SpecificSystemBar = 'status' | 'navigation' | 'navigationIndicator'

当前支持显示或隐藏的系统栏类型。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| 'status' | 状态栏。 |
| 'navigation' | HarmonyOS各设备不支持此能力。  三键导航栏。 |
| 'navigationIndicator' | 底部导航。根据用户设置，可表现为导航条或三键导航栏。 |

## WindowAnimationCurveParam20+

PhonePC/2in1TabletTVWearable

type WindowAnimationCurveParam = Array<number>

动画曲线参数。不同曲线类型[WindowAnimationCurve](arkts-apis-window-e.md#windowanimationcurve20)，对应的WindowAnimationCurveParam参数含义不同。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| Array<number> | 表示值类型为数字数组，元素取值范围见对应曲线描述。 |

当曲线类型为LINEAR，动画曲线参数选填，且不生效。

当曲线类型为INTERPOLATION\_SPRING时，动画曲线参数需设置为长度为4的数组：[velocity,mass,stiffness,damping]。

* velocity：表示初始速度，类型为number，必填，取值范围为(-∞, +∞)。

  用于描述外部因素对弹性动效产生的影响参数，目的是保证对象从之前的运动状态平滑地过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。
* mass：表示质量，类型为number。必填，取值范围为(0, +∞)，当取值小于等于0时，按1处理。

  用于描述弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。
* stiffness：表示刚度，类型为number。必填，取值范围为(0, +∞)，当取值小于等于0时，按1处理。

  用于描述物体抵抗施加的力而形变的程度。刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度越快。
* damping：表示阻尼，类型为number。必填，取值范围为(0, +∞)，当取值小于等于0时，按1处理。

  用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。

当曲线类型为CUBIC\_BEZIER时，动画曲线参数需设置为长度为4的数组：[x1, y1, x2, y2]。

* x1: 确定贝塞尔曲线第一点的横坐标，类型为number，必填，取值范围为[0, 1]，值小于0时按0处理，大于1时按1处理。
* y1: 确定贝塞尔曲线第一点的纵坐标，类型为number，必填，取值范围为(-∞, +∞)。
* x2: 确定贝塞尔曲线第二点的横坐标，类型为number，必填，取值范围为[0, 1]，值小于0时按0处理，大于1时按1处理。
* y2: 确定贝塞尔曲线第二点的纵坐标，类型为number，必填，取值范围为(-∞, +∞)。

## RotationChangeCallback19+

PhonePC/2in1TabletTVWearable

type RotationChangeCallback<T, U> = (info: T) => U

旋转事件通知通用回调函数。

开发者在使用时，回调函数参数类型为[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19)，返回值类型为[RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19) | void。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | T | 是 | 回调函数调用时系统传入[RotationChangeInfo](arkts-apis-window-i.md#rotationchangeinfo19)类型的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 回调函数需要返回[RotationChangeResult](arkts-apis-window-i.md#rotationchangeresult19) | void类型的返回值。 |
