---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper
title: ArcSwiper
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ArcSwiper
category: harmonyos-references
scraped_at: 2026-04-29T13:51:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0385790b0fae535cbbfe8e2c9bde191e895a5d229dfa86d06e53089c8ab0ba41
---

弧形滑块视图容器，提供子组件滑动轮播显示的能力。

说明

该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

说明

* ArcSwiperAttribute是用于配置ArcSwiper组件属性的关键接口。API version 21及之前版本，导入ArcSwiper组件后需要开发者手动导入ArcSwiperAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcSwiper组件后，会自动导入ArcSwiperAttribute，无需开发者手动导入ArcSwiperAttribute。
* 如果开发者手动导入ArcSwiperAttribute，DevEco Studio会显示置灰，API version 21及之前版本删除会编译报错，从API version 22开始，删除对功能无影响。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

API version 21及之前版本：

```
1. import {
2. ArcSwiper,
3. ArcSwiperAttribute,
4. ArcDotIndicator,
5. ArcDirection,
6. ArcSwiperController
7. } from '@kit.ArkUI';
```

API version 22及之后版本：

```
1. import {
2. ArcSwiper,
3. ArcDotIndicator,
4. ArcDirection,
5. ArcSwiperController
6. } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

说明

* 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。
* 不建议在执行翻页动画过程中增加或减少子组件，会导致未进行动画的子组件提前进入视窗，引起显示异常。

## 接口

PhonePC/2in1TabletTVWearable

ArcSwiper(controller?: ArcSwiperController)

创建弧形滑块视图容器。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [ArcSwiperController](ts-container-arcswiper.md#arcswipercontroller) | 否 | 给组件绑定一个控制器，用来控制组件翻页。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性。

### index

PhonePC/2in1TabletTVWearable

index(index: Optional<number>)

设置当前在容器中显示的子组件的索引值。设置小于0或大于等于子组件数量时，按照默认值0处理。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | Optional<number> | 是 | 当前在容器中显示的子组件的索引值。  当index值为undefined时，按取值为0处理。 |

### indicator

PhonePC/2in1TabletTVWearable

indicator(style: Optional<ArcDotIndicator | boolean>)

设置弧形圆点指示器样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional<[ArcDotIndicator](ts-container-arcswiper.md#arcdotindicator) | boolean> | 是 | 弧形圆点指示器样式。  - ArcDotIndicator：弧形圆点指示器属性及功能。  - boolean：是否启用弧形圆点指示器。设置为true启用，false不启用。  默认值：true  默认类型：ArcDotIndicator |

### duration

PhonePC/2in1TabletTVWearable

duration(duration: Optional<number>)

设置子组件切换的动画时长。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | Optional<number> | 是 | 子组件切换的动画时长。  默认值：400  单位：毫秒 |

### vertical

PhonePC/2in1TabletTVWearable

vertical(isVertical: Optional<boolean>)

设置是否为纵向滑动。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isVertical | Optional<boolean> | 是 | 是否为纵向滑动。  true: 纵向滑动；false: 横向滑动。  默认值：false |

### disableSwipe

PhonePC/2in1TabletTVWearable

disableSwipe(disabled: Optional<boolean>)

设置禁用组件滑动切换功能。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disabled | Optional<boolean> | 是 | 禁用组件滑动切换功能。设置为true禁用，false不禁用。  默认值：false |

### digitalCrownSensitivity

PhonePC/2in1TabletTVWearable

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置旋转表冠的灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | Optional<[CrownSensitivity](ts-appendix-enums.md#crownsensitivity18)> | 是 | 旋转表冠的灵敏度。  默认值：CrownSensitivity.MEDIUM |

### effectMode

PhonePC/2in1TabletTVWearable

effectMode(edgeEffect: Optional<EdgeEffect>)

设置边缘滑动效果。 目前支持的滑动效果参见[EdgeEffect](ts-appendix-enums.md#edgeeffect)的枚举说明。调用控制器接口时回弹不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edgeEffect | Optional<[EdgeEffect](ts-appendix-enums.md#edgeeffect)> | 是 | 边缘滑动效果。  默认值：EdgeEffect.Spring |

### disableTransitionAnimation

PhonePC/2in1TabletTVWearable

disableTransitionAnimation(disabled: Optional<boolean>)

是否关闭特殊动效效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disabled | Optional<boolean> | 是 | 是否关闭特殊动效效果。  true：关闭特殊动效效果；false：不关闭特殊动效效果。  传入参数非法时，按false处理。 |

## ArcSwiperController

PhonePC/2in1TabletTVWearable

ArcSwiper容器组件的控制器，可以将此对象绑定至ArcSwiper组件，可以通过它控制翻页。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### constructor

PhonePC/2in1TabletTVWearable

constructor()

ArcSwiperController的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### showNext

PhonePC/2in1TabletTVWearable

showNext()

翻至下一页。翻页带动效切换过程，时长通过[duration](ts-container-arcswiper.md#duration)指定。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### showPrevious

PhonePC/2in1TabletTVWearable

showPrevious()

翻至上一页。翻页带动效切换过程，时长通过[duration](ts-container-arcswiper.md#duration)指定。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### finishAnimation

PhonePC/2in1TabletTVWearable

finishAnimation(handler?: FinishAnimationHandler)

停止播放动画。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [FinishAnimationHandler](ts-container-arcswiper.md#finishanimationhandler) | 否 | 动画结束的回调。  默认值：不传入的情况，无回调 |

## ArcDotIndicator

PhonePC/2in1TabletTVWearable

提供弧形圆点指示器属性及功能。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### constructor

PhonePC/2in1TabletTVWearable

constructor()

ArcDotIndicator的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### arcDirection

PhonePC/2in1TabletTVWearable

arcDirection(direction: Optional<ArcDirection>): ArcDotIndicator

设置弧形指示器的方向。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | Optional<[ArcDirection](ts-container-arcswiper.md#arcdirection-1)> | 是 | 设置弧形指示器的方向。  默认值：ArcDirection.SIX\_CLOCK\_DIRECTION，6点钟方向。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArcDotIndicator](ts-container-arcswiper.md#arcdotindicator) | 提供弧形圆点指示器属性及功能。 |

### itemColor

PhonePC/2in1TabletTVWearable

itemColor(color: Optional<ResourceColor>): ArcDotIndicator

设置弧形指示器中，未选中导航点的颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 设置弧形指示器中，未选中导航点的颜色。  默认值：'#A9FFFFFF' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArcDotIndicator](ts-container-arcswiper.md#arcdotindicator) | 提供弧形圆点指示器属性及功能。 |

### selectedItemColor

PhonePC/2in1TabletTVWearable

selectedItemColor(color: Optional<ResourceColor>): ArcDotIndicator

设置弧形指示器中，选中导航点的颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 设置弧形指示器中，选中导航点的颜色。  默认值：'#FF5EA1FF' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArcDotIndicator](ts-container-arcswiper.md#arcdotindicator) | 提供弧形圆点指示器属性及功能。 |

### backgroundColor

PhonePC/2in1TabletTVWearable

backgroundColor(color: Optional<ResourceColor>): ArcDotIndicator

设置弧形指示器被长按时，弧形指示器的颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 设置弧形指示器被长按时，弧形指示器的颜色。  默认值：'#FF404040' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArcDotIndicator](ts-container-arcswiper.md#arcdotindicator) | 提供弧形圆点指示器属性及功能。 |

### maskColor

PhonePC/2in1TabletTVWearable

maskColor(color: Optional<LinearGradient>): ArcDotIndicator

设置弧形指示器的遮罩渐变色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional<[LinearGradient](ts-basic-components-datapanel.md#lineargradient10)> | 是 | 设置弧形指示器的遮罩渐变色。  起始颜色默认值：'#00000000'  结束颜色默认值：'#FF000000' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArcDotIndicator](ts-container-arcswiper.md#arcdotindicator) | 提供弧形圆点指示器属性及功能。 |

### ArcDirection

PhonePC/2in1TabletTVWearable

弧形方向。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 值 | 说明 |
| --- | --- | --- |
| THREE\_CLOCK\_DIRECTION | 0 | 3点钟方向。 |
| SIX\_CLOCK\_DIRECTION | 1 | 6点钟方向。 |
| NINE\_CLOCK\_DIRECTION | 2 | 9点钟方向。 |

## FinishAnimationHandler

PhonePC/2in1TabletTVWearable

type FinishAnimationHandler = () => void

停止播放动画时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## IndexChangedHandler

PhonePC/2in1TabletTVWearable

type IndexChangedHandler = (index: number) => void

当前显示元素的索引变化时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。index序列从0开始。 |

## AnimationStartHandler

PhonePC/2in1TabletTVWearable

type AnimationStartHandler = (index: number, targetIndex: number, event: SwiperAnimationEvent) => void

切换动画开始时的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引，动画开始前的index值（不是最终结束动画的index值）。 |
| targetIndex | number | 是 | 切换动画目标元素的索引。 |
| event | [SwiperAnimationEvent](ts-container-swiper.md#swiperanimationevent10对象说明) | 是 | 动画相关信息，包括主轴方向上当前显示元素和目标元素相对ArcSwiper起始位置的位移，以及离手速度。 |

## AnimationEndHandler

PhonePC/2in1TabletTVWearable

type AnimationEndHandler = (index: number, event: SwiperAnimationEvent) => void

切换动画结束时的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。 |
| event | [SwiperAnimationEvent](ts-container-swiper.md#swiperanimationevent10对象说明) | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于ArcSwiper起始位置的位移。 |

## GestureSwipeHandler

PhonePC/2in1TabletTVWearable

type GestureSwipeHandler = (index: number, event: SwiperAnimationEvent) => void

在页面跟手滑动过程中，逐帧触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。 |
| event | [SwiperAnimationEvent](ts-container-swiper.md#swiperanimationevent10对象说明) | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于ArcSwiper起始位置的位移。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(handler: Optional<IndexChangedHandler>)

当前显示子组件的索引变化时触发该事件，返回值为当前显示子组件的索引值。

ArcSwiper组件结合[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)使用时，不能在onChange事件里触发子页面UI的刷新。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional<[IndexChangedHandler](ts-container-arcswiper.md#indexchangedhandler)> | 是 | 当前显示元素的索引回调。 |

### onAnimationStart

PhonePC/2in1TabletTVWearable

onAnimationStart(handler: Optional<AnimationStartHandler>)

切换动画开始时触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional<[AnimationStartHandler](ts-container-arcswiper.md#animationstarthandler)> | 是 | 切换动画开始时的回调。 |

### onAnimationEnd

PhonePC/2in1TabletTVWearable

onAnimationEnd(handler: Optional<AnimationEndHandler>)

切换动画结束时触发该回调。

当ArcSwiper切换动效结束时触发，包括动画过程中手势中断，通过[SwiperController](ts-container-swiper.md#swipercontroller)调用finishAnimation。参数为动画结束后的index值，多列ArcSwiper时，index为最左侧组件的索引。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional<[AnimationEndHandler](ts-container-arcswiper.md#animationendhandler)> | 是 | 切换动画结束时触发该回调。 |

### onGestureSwipe

PhonePC/2in1TabletTVWearable

onGestureSwipe(handler: Optional<GestureSwipeHandler>)

在页面跟手滑动过程中，逐帧触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional<[GestureSwipeHandler](ts-container-arcswiper.md#gestureswipehandler)> | 是 | 在页面跟手滑动过程中，逐帧触发该回调。 |

### customContentTransition

PhonePC/2in1TabletTVWearable

customContentTransition(transition: Optional<SwiperContentAnimatedTransition>)

自定义ArcSwiper页面切换动画。在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发回调。开发者可以在回调中设置透明度、缩放比例、位移等属性来自定义切换动画。

在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发[SwiperContentTransitionProxy](ts-container-arcswiper.md#swipercontenttransitionproxy)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | Optional<[SwiperContentAnimatedTransition](ts-container-arcswiper.md#swipercontentanimatedtransition)> | 是 | ArcSwiper自定义切换动画相关信息。 |

## SwiperContentAnimatedTransition

PhonePC/2in1TabletTVWearable

ArcSwiper自定义切换动画相关信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | ArcSwiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用[SwiperContentTransitionProxy](ts-container-arcswiper.md#swipercontenttransitionproxy)的[finishTransition](ts-container-arcswiper.md#finishtransition)接口通知ArcSwiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即在该页面节点下渲染树。单位ms，默认值为0。 |
| transition | Callback<[SwiperContentTransitionProxy](ts-container-arcswiper.md#swipercontenttransitionproxy)> | 否 | 否 | 自定义切换动画具体内容。 |

## SwiperContentTransitionProxy

PhonePC/2in1TabletTVWearable

ArcSwiper自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画视窗内的页面信息，同时，也可以通过调用该对象的finishTransition接口通知ArcSwiper组件页面自定义动画已结束。

说明

* 假设当前选中的子组件的索引为0，从第0页切换到第1页的动画过程中，每帧都会对视窗内所有页面触发回调，当视窗内有第0页和第1页两页时，每帧会触发两次回调。其中第一次回调的selectedIndex为0，index为0，position为当前帧第0页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第0页的长度；第二次回调的selectedIndex仍为0，index为1，position为当前帧第1页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第1页的长度。
* 若动画曲线为弹簧插值曲线，从第0页切换到第1页的动画过程中，可能会因为离手时的位置和速度，先过滑到第2页，再回弹到第1页，该过程中每帧会对视窗内第1页和第2页触发回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### **属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selectedIndex | number | 否 | 否 | 当前选中页面的索引。 |
| index | number | 否 | 否 | 视窗内页面的索引。 |
| position | number | 否 | 否 | index页面相对于ArcSwiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。 |
| mainAxisLength | number | 否 | 否 | index对应页面在主轴方向上的长度。 |

### finishTransition

PhonePC/2in1TabletTVWearable

finishTransition(): void

通知ArcSwiper组件，此页面的自定义动画已结束。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置arcSwiper基本属性）

该示例通过设置arcSwiper的基本属性，展示了组件的基本功能。

```
1. // xxx.ets
2. import {
3. CircleShape,
4. ArcSwiper,
5. ArcSwiperAttribute,
6. ArcDotIndicator,
7. ArcDirection,
8. ArcSwiperController
9. } from '@kit.ArkUI';
10. // 从API version 22开始，无需手动导入ArcSwiperAttribute。具体请参考ArcSwiper的导入模块说明

12. class MyDataSource implements IDataSource {
13. private list: Color[] = [];

15. constructor(list: Color[]) {
16. this.list = list;
17. }

19. totalCount(): number {
20. return this.list.length;
21. }

23. getData(index: number): Color {
24. return this.list[index];
25. }

27. registerDataChangeListener(listener: DataChangeListener): void {
28. }

30. unregisterDataChangeListener() {
31. }
32. }

34. @Entry
35. @Component
36. struct TestNewInterface {
37. @State itemSimpleColor: Color | number | string = '';
38. @State selectedItemSimpleColor: Color | number | string = '';
39. private wearableSwiperController: ArcSwiperController = new ArcSwiperController();
40. private arcDotIndicator: ArcDotIndicator = new ArcDotIndicator();
41. private data: MyDataSource = new MyDataSource([]);
42. @State backgroundColors: Color[] =
43. [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.White, Color.Gray, Color.Orange, Color.Transparent];
44. innerSelectedIndex: number = 0;

46. aboutToAppear(): void {
47. let list: Color[] = [];
48. for (let i = 1; i <= 6; i++) {
49. list.push(i);
50. }
51. this.data = new MyDataSource(this.backgroundColors);
52. }

54. build() {
55. Column() {
56. Row() {
57. ArcSwiper(this.wearableSwiperController) {
58. LazyForEach(this.data, (backgroundColor: Color, index: number) => {
59. Text(index.toString())
60. .width(233)
61. .height(233)
62. .backgroundColor(backgroundColor)
63. .textAlign(TextAlign.Center)
64. .fontSize(30)
65. })
66. }
67. .clipShape(new CircleShape({ width: 233, height: 233 }))
68. .effectMode(EdgeEffect.None)
69. .backgroundColor(Color.Transparent)
70. .index(0)
71. .duration(400)
72. .vertical(false)
73. .indicator(this.arcDotIndicator
74. .arcDirection(ArcDirection.SIX_CLOCK_DIRECTION)
75. .itemColor(this.itemSimpleColor)
76. .selectedItemColor(this.selectedItemSimpleColor)
77. )
78. .disableSwipe(false)
79. .digitalCrownSensitivity(CrownSensitivity.MEDIUM)
80. .onChange((index: number) => {
81. console.info("onChange:" + index.toString());
82. })
83. .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
84. this.innerSelectedIndex = targetIndex;
85. console.info("index: " + index);
86. console.info("targetIndex: " + targetIndex);
87. console.info("current offset: " + extraInfo.currentOffset);
88. console.info("target offset: " + extraInfo.targetOffset);
89. console.info("velocity: " + extraInfo.velocity);
90. })
91. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
92. others: Array<GestureRecognizer>): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
93. if (current) {
94. let target = current.getEventTargetInfo();
95. if (target && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
96. // 此处判断swiperTarget.isBegin()或innerSelectedIndex === 0，表明ArcSwiper滑动到开头
97. let swiperTarget = target as ScrollableTargetInfo
98. if (swiperTarget instanceof ScrollableTargetInfo &&
99. (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) {
100. let panEvent = event as PanGestureEvent;
101. if (panEvent && panEvent.offsetX > 0 && (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) {
102. return GestureJudgeResult.REJECT;
103. }
104. }
105. }
106. }
107. return GestureJudgeResult.CONTINUE;
108. })
109. .onAnimationEnd((index: number, extraInfo: SwiperAnimationEvent) => {
110. console.info("index: " + index);
111. console.info("current offset: " + extraInfo.currentOffset);
112. })
113. .disableTransitionAnimation(false)
114. }.height('100%')
115. }.width('100%')
116. }
117. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/T_MZCXk3S4u0NyT-n1gSkA/zh-cn_image_0000002558606508.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055145Z&HW-CC-Expire=86400&HW-CC-Sign=8BAE3E9394FC3FE70D9654B74CCB224CEDE4482344D46DD7437F90880ED77491)

### 示例2（设置ArcSwiper自定义页面切换动画）

该示例通过[customContentTransition](ts-container-arcswiper.md#customcontenttransition)接口，实现了自定义ArcSwiper页面切换动画。

```
1. import { Decimal } from '@kit.ArkTS';
2. import { CircleShape, ArcSwiper, ArcSwiperAttribute } from '@kit.ArkUI';

4. // 从API version 22开始，无需手动导入ArcSwiperAttribute。具体请参考ArcSwiper的导入模块说明
5. @Entry
6. @Component
7. struct TestNewInterface {
8. private backgroundColors: Color[] =
9. [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.White, Color.Gray, Color.Orange];
10. @State scaleList: number[] = [];

12. aboutToAppear(): void {
13. for (let i = 0; i < this.backgroundColors.length; i++) {
14. this.scaleList.push(1.0);
15. }
16. }

18. build() {
19. Column() {
20. Row() {
21. ArcSwiper() {
22. ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
23. Text(index.toString())
24. .width(233)
25. .height(233)
26. .backgroundColor(backgroundColor)
27. .textAlign(TextAlign.Center)
28. .fontSize(30)
29. .scale({ x: this.scaleList[index], y: this.scaleList[index] })
30. })
31. }
32. .clipShape(new CircleShape({ width: 233, height: 233 }))
33. .effectMode(EdgeEffect.None)
34. .onChange((index: number) => {
35. console.info('onChange:' + index.toString());
36. })
37. .customContentTransition({
38. // 页面移除视窗时超时1000ms下渲染树
39. timeout: 1000,
40. // 对视窗内所有页面逐帧回调transition，在回调中修改opacity属性值，实现自定义动画
41. transition: (proxy: SwiperContentTransitionProxy) => {
42. if (proxy.position <= -1 || proxy.position >= 1) {
43. // 页面完全滑出视窗外时，重置属性值
44. this.scaleList[proxy.index] = 1.0;
45. } else {
46. let position: number = Decimal.abs(proxy.position).toNumber();
47. this.scaleList[proxy.index] = 1 - position;
48. }
49. }
50. })
51. .disableTransitionAnimation(false)
52. }.height('100%')
53. }.width('100%')
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/bSY2C3I5R6qUZ28PnlJ4wA/zh-cn_image_0000002589326035.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055145Z&HW-CC-Expire=86400&HW-CC-Sign=9EDB1DA436B88FD6C5D542F127AC580D991B81598548E6139E531AB64FA7DF75)
