---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component
title: 组件内转场 (transition)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 组件内转场 (transition)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:43+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:befbdb301e14511359852dd3b6696a8b42372545f03f098e939b948540e872c7
---

组件内转场主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

当前有两种方式触发组件的transition：

1. 当组件插入或删除时（如if条件改变、ForEach新增删除组件），会递归的触发所有新插入/删除的组件的transition效果。
2. 当组件[visibility](ts-universal-attributes-visibility.md#visibility)属性在可见和不可见（Visibility.Hidden或Visibility.None）之间改变时，只触发该组件的transition效果。在Visibility.Visible与Visibility.None之间切换时，若直接设置为Visibility.None，会导致组件布局大小为0，此时无法观察到transition效果。而当在动画中修改visibility属性为Visibility.None时，组件布局为0是带动画的，将呈现transition与布局动画的叠加效果，形成双动画的复合表现。

## transition

PhonePC/2in1TabletTVWearable

transition(value: TransitionOptions | TransitionEffect): T

组件插入显示和删除隐藏的过渡效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TransitionOptions](ts-transition-animation-component.md#transitionoptionsdeprecated)(deprecated) | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 是 | 设置组件插入显示和删除隐藏的过渡效果。  **说明：**  详细描述见[TransitionOptions](ts-transition-animation-component.md#transitionoptionsdeprecated)和[TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)对象说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## transition12+

PhonePC/2in1TabletTVWearable

transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T

组件插入显示和删除隐藏的过渡效果。同[transition](ts-transition-animation-component.md#transition)相比，增加了转场动画结束的回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 是 | 设置组件插入显示和删除隐藏的过渡效果。 |
| onFinish | Optional<[TransitionFinishCallback](ts-transition-animation-component.md#transitionfinishcallback12)> | 是 | 转场动画结束回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## TransitionEdge10+

PhonePC/2in1TabletTVWearable

转场边缘类型。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 0 | 窗口的上边缘。 |
| BOTTOM | 1 | 窗口的下边缘。 |
| START | 2 | 窗口的起始边缘，LTR时为左边缘，RTL时为右边缘。 |
| END | 3 | 窗口的终止边缘，LTR时为右边缘，RTL时为左边缘。 |

## TransitionEffect10+对象说明

PhonePC/2in1TabletTVWearable

TransitionEffect以函数的形式指定转场效果。提供了以下接口：

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| IDENTITY | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"identity"> | 是 | 否 | 禁用转场效果。 |
| OPACITY | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"opacity"> | 是 | 否 | 为组件添加透明度转场效果，出现时透明度从0到1、消失时透明度从1到0，相当于TransitionEffect.opacity(0)。 |
| SLIDE | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"asymmetric", { appear: [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"move", [TransitionEdge](ts-transition-animation-component.md#transitionedge10)>; disappear: [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"move", [TransitionEdge](ts-transition-animation-component.md#transitionedge10)>; }> | 是 | 否 | 相当于TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.START), TransitionEffect.move(TransitionEdge.END))。从START边滑入，END边滑出。即在LTR模式下，从左侧滑入，右侧滑出；在RTL模式下，从右侧滑入，左侧滑出。 |
| SLIDE\_SWITCH | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"slideSwitch"> | 是 | 否 | 指定出现时从右侧先缩小再放大滑入、消失时从左侧先缩小再放大滑出的转场效果。自带动画参数，也可覆盖动画参数，自带的动画参数时长600ms，指定动画曲线cubicBezierCurve(0.24, 0.0, 0.50, 1.0)，最小缩放比例为0.8。 |

说明

1. TransitionEffect可通过combine函数实现多个转场效果的组合，可以为每个效果分别指定animation参数，且前一效果的animation的参数也可适用于后一效果。例如，TransitionEffect.OPACITY.animation({duration: 1000}).combine(TransitionEffect.translate({x: 100}))，则时长为1000ms的动画参数对OPACITY和translate均生效。
2. 动画参数的生效顺序为：本TransitionEffect指定的animation参数 > 前面的TransitionEffect指定的animation参数 > 触发该组件出现消失的animateTo中的动画参数。
3. 如果未使用animateTo触发转场动画且TransitionEffect中也无animation参数，则该组件直接出现或者消失。
4. TransitionEffect中指定的属性值如与默认值相同，则该属性不会产生转场动画。如TransitionEffect.opacity(1).animation({duration:1000})，由于opacity默认值也为1，未产生透明度动画，该组件直接出现或者消失。
5. 更详细的关于scale、rotate效果的介绍可参考[图形变换](ts-universal-attributes-transformation.md)。
6. 如果在动画范围([animateTo](arkts-apis-uicontext-uicontext.md#animateto)、[animation](ts-animatorproperty.md))内触发组件的上下树或可见性([visibility](ts-universal-attributes-visibility.md#visibility))改变，而根组件没有配置transition，会给该组件加上默认透明度转场，即TransitionEffect.OPACITY，动画参数跟随所处动画环境的参数。如不需要可通过主动配置TransitionEffect.IDENTITY来禁用，使该组件直接出现或消失。
7. 当通过删除整棵子树的方式触发消失转场，如需看到完整的消失转场过程，需要保证被删除子树的根组件的有充足的消失转场时间，见示例3。

### translate10+

PhonePC/2in1TabletTVWearable

translate(options: TranslateOptions): TransitionEffect<"translate">

设置组件转场时的平移效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TranslateOptions](ts-universal-attributes-transformation.md#translateoptions对象说明) | 是 | 组件转场时的平移效果，为插入时起点和删除时终点的值。  -x：横向的平移距离。  -y：纵向的平移距离。  -z：竖向的平移距离。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"translate"> | 当前动画平移效果。 |

### rotate10+

PhonePC/2in1TabletTVWearable

rotate(options: RotateOptions): TransitionEffect<"rotate">

设置组件转场时的旋转效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RotateOptions](ts-universal-attributes-transformation.md#rotateoptions对象说明) | 是 | 组件转场时的旋转效果，为插入时起点和删除时终点的值。  -x：横向的旋转向量分量。  -y：纵向的旋转向量分量。  -z：竖向的旋转向量分量。  - centerX、centerY指旋转中心点，centerX和centerY默认值是"50%"，即默认以组件的中心点为旋转中心点。  - 中心点为(0, 0)代表组件的左上角。  -centerZ指z轴锚点，即3D旋转中心点的z轴分量，centerZ默认值是0。  -perspective指视距，不支持perspective属性做转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"rotate"> | 当前动画旋转效果。 |

### scale10+

PhonePC/2in1TabletTVWearable

scale(options: ScaleOptions): TransitionEffect<"scale">

设置组件转场时的缩放效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ScaleOptions](ts-universal-attributes-transformation.md#scaleoptions对象说明) | 是 | 组件转场时的缩放效果，为插入时起点和删除时终点的值。设置的缩放值在组件当前的scale属性上进行叠加，如组件当前scale值为0.8，当转场缩放值设置为0.5时，组件入场动画的缩放值将从0.4开始执行。  -x：横向放大倍数（或缩小比例）。  -y：纵向放大倍数（或缩小比例）。  -z：当前为二维显示，该参数无效。  - centerX、centerY指缩放中心点，centerX和centerY默认值是"50%"，即默认以组件的中心点为缩放中心点。  - 中心点为(0, 0)代表组件的左上角。  **说明：**  设置centerX、centerY为非法字符串时（例如，"illegalString"），默认值为"0"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"scale"> | 当前动画缩放效果。 |

### opacity10+

PhonePC/2in1TabletTVWearable

opacity(alpha: number): TransitionEffect<"opacity">

设置组件转场时的透明度效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | number | 是 | 组件转场时的透明度效果，为插入时起点和删除时终点的值。  取值范围：[0, 1]  **说明：**  设置小于0的非法值按0处理，大于1的非法值按1处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"opacity"> | 当前动画透明度效果。 |

### move10+

PhonePC/2in1TabletTVWearable

move(edge: TransitionEdge): TransitionEffect<"move">

设置组件转场时从屏幕边缘滑入和滑出的效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edge | [TransitionEdge](ts-transition-animation-component.md#transitionedge10) | 是 | 组件转场时从屏幕边缘滑入和滑出的效果，本质为平移效果，为插入时起点和删除时终点的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"move"> | 当前动画从屏幕边缘滑入和滑出的效果。 |

### asymmetric10+

PhonePC/2in1TabletTVWearable

asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect<"asymmetric">

设置非对称的转场效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appear | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 是 | 指定出现的转场效果。  如不通过asymmetric函数构造TransitionEffect，则表明该效果在组件出现和消失时均生效。 |
| disappear | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 是 | 指定消失的转场效果。  如不通过asymmetric函数构造TransitionEffect，则表明该效果在组件出现和消失时均生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)<"asymmetric"> | 当前动画非对称的转场效果。 |

### constructor10+

PhonePC/2in1TabletTVWearable

constructor(type: Type, effect: Effect)

构造TransitionEffect对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [Type](ts-appendix-enums.md#transitiontype) | 是 | 转场类型。 |
| effect | [Effect](ts-transition-animation-component.md#transitioneffect10对象说明) | 是 | 转场参数。 |

### combine10+

PhonePC/2in1TabletTVWearable

combine(transitionEffect: TransitionEffect): TransitionEffect

对TransitionEffect进行链式组合，以形成包含多种转场效果的TransitionEffect。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transitionEffect | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 是 | 被组合的过渡效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 组合过渡效应。 |

### animation10+

PhonePC/2in1TabletTVWearable

animation(value: AnimateParam): TransitionEffect

指定该TransitionEffect的动画参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 是 | 动画参数。  该参数只用来指定动画参数，其入参AnimateParam的onFinish回调不生效。  如果通过combine进行TransitionEffect的组合，前一TransitionEffect的动画参数也可用于后一TransitionEffect。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 当前动画效果。 |

## TransitionFinishCallback12+

PhonePC/2in1TabletTVWearable

type TransitionFinishCallback = (transitionIn: boolean) => void

组件转场动画的结束回调类型。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transitionIn | boolean | 是 | 该入参表示转场动画的结束回调类型。  该参数为true表示该转场回调是出现动画的结束回调，该参数为false表示该转场回调是消失动画的结束回调。 |

说明

1. 当通过触发一棵子树的上下树，进而递归的触发出现消失转场时，只能保证根组件的消失动画结束回调能被调用。如果子组件的消失动画结束回调时间晚于根组件的消失动画结束回调，由于整棵子树已被销毁，子组件的结束回调不会被调用。
2. 当同一组件的最后一个同类型（即出现或者消失）的动画结束后，才会调用结束回调。即如果反复触发出现消失动画（例如通过Visibility触发），只有最后一次的出现消失的结束回调才会被调用。

## TransitionOptions(deprecated)

PhonePC/2in1TabletTVWearable

TransitionOptions通过指定结构体内的参数来指定转场效果。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TransitionType](ts-appendix-enums.md#transitiontype) | 否 | 是 | 指定该转场样式生效的场景。  默认值：TransitionType.All  **说明：**  不指定type时默认为TransitionType.All，即插入删除都生效。 |
| opacity | number | 否 | 是 | 设置组件转场时的透明度效果，为插入时起点和删除时终点的值。  取值范围： [0, 1]  **说明：**  设置小于0的非法值时，按0处理；设置大于1的非法值时，按1处理。 |
| translate | [TranslateOptions](ts-universal-attributes-transformation.md#translateoptions对象说明) | 否 | 是 | 设置组件转场时的平移效果，为插入时起点和删除时终点的值。  -x：横向的平移距离。  -y：纵向的平移距离。  -z：竖向的平移距离。 |
| scale | [ScaleOptions](ts-universal-attributes-transformation.md#scaleoptions对象说明) | 否 | 是 | 设置组件转场时的缩放效果，为插入时起点和删除时终点的值。  -x：横向放大倍数（或缩小比例）。  -y：纵向放大倍数（或缩小比例）。  -z：当前为二维显示，该参数无效 。  - centerX、centerY指缩放中心点，centerX和centerY默认值是"50%"，即默认以组件的中心点为缩放中心点。  - 中心点为(0, 0)代表组件的左上角。  **说明：**  设置centerX、centerY为非法字符串时（例如，"illegalString"），默认值为"0"。 |
| rotate | [RotateOptions](ts-universal-attributes-transformation.md#rotateoptions对象说明) | 否 | 是 | 设置组件转场时的旋转效果，为插入时起点和删除时终点的值。  -x：横向的旋转向量分量。  -y：纵向的旋转向量分量。  -z：竖向的旋转向量分量。  - centerX、centerY指旋转中心点，centerX和centerY默认值是"50%"，即默认以组件的中心点为旋转中心点。  - 中心点为(0, 0)代表组件的左上角。 |

说明

1. 当使用TransitionOptions类型的入参指定转场效果时，**必须**配合[animateTo](arkts-apis-uicontext-uicontext.md#animateto)使用才有动画效果，动效时长、曲线、延时跟随animateTo中的配置。
2. 当使用TransitionOptions作为入参，且不指定除type外的任何参数时，此时相当于指定了透明度的转场效果。例如，指定{type: TransitionType.Insert}相当于指定了{type: TransitionType.Insert, opacity: 0}的转场效果。而指定了具体效果时，则不会添加默认的透明度转场效果。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用同一接口实现图片出现消失）

该示例主要演示如何通过同一[TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)来实现图片的出现与消失，出现和消失互为逆过程。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransitionEffectExample1 {
5. @State flag: boolean = true;
6. @State show: string = 'show';

8. build() {
9. Column() {
10. Button(this.show).width(80).height(30).margin(30)
11. .onClick(() => {
12. // 点击Button控制Image的显示和消失
13. if (this.flag) {
14. this.show = 'hide';
15. } else {
16. this.show = 'show';
17. }
18. this.flag = !this.flag;
19. })
20. if (this.flag) {
21. // Image的显示和消失配置为相同的过渡效果（出现和消失互为逆过程）
22. // 出现时从指定的透明度为0、绕z轴旋转180°的状态，变为默认的透明度为1、旋转角为0的状态，透明度与旋转动画时长都为2000ms
23. // 消失时从默认的透明度为1、旋转角为0的状态，变为指定的透明度为0、绕z轴旋转180°的状态，透明度与旋转动画时长都为2000ms
24. // $r('app.media.testImg')需要替换为开发者所需的图像资源文件。
25. Image($r('app.media.testImg')).width(200).height(200)
26. .transition(TransitionEffect.OPACITY.animation({ duration: 2000, curve: Curve.Ease }).combine(
27. TransitionEffect.rotate({ z: 1, angle: 180 })
28. ))
29. }
30. }.width('100%')
31. }
32. }
```

示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/3FId8i6IRWqKxgOlZKnMIw/zh-cn_image_0000002558606892.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=6A3579E524C13B1EC11E2356CC118F33528FD3C2CBA7CD8F9ACC69145F75A656)

### 示例2（使用不同接口实现图片出现消失）

该示例主要演示使用不同[TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)来实现图片的出现和消失。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransitionEffectExample2 {
5. @State flag: boolean = true;
6. @State show: string = 'show';

8. build() {
9. Column() {
10. Button(this.show).width(80).height(30).margin(30)
11. .onClick(() => {
12. // 点击Button控制Image的显示和消失
13. if (this.flag) {
14. this.show = 'hide';
15. } else {
16. this.show = 'show';
17. }
18. this.getUIContext().animateTo({ duration: 2000 }, () => {
19. // 第一张图的TransitionEffect包含了animation，transition的动画参数由TransitionEffect指定
20. // 第二张图的TransitionEffect不包含animation，transition的动画参数由animateTo指定
21. this.flag = !this.flag;
22. });
23. })
24. if (this.flag) {
25. // Image的显示和消失配置为不同的过渡效果
26. // 出现时做从指定的透明度为0变为默认的透明度1的动画，该动画时长为1000ms，以及做从指定的绕z轴旋转180°变为默认的旋转角为0的动画，该动画1000ms后播放，时长为1000ms
27. // 消失时做从默认的透明度为1变为指定的透明度0的动画，该动画1000ms后播放，时长为1000ms，以及做从默认的旋转角0变为指定的绕z轴旋转180°的动画，该动画时长为1000ms
28. // $r('app.media.testImg')需要替换为开发者所需的图像资源文件。
29. Image($r('app.media.testImg')).width(200).height(200)
30. .transition(
31. TransitionEffect.asymmetric(
32. TransitionEffect.OPACITY.animation({ duration: 1000 }).combine(
33. TransitionEffect.rotate({ z: 1, angle: 180 }).animation({ delay: 1000, duration: 1000 }))
34. ,
35. TransitionEffect.OPACITY.animation({ delay: 1000, duration: 1000 }).combine(
36. TransitionEffect.rotate({ z: 1, angle: 180 }).animation({ duration: 1000 }))
37. )
38. )
39. // 出现时做从x方向和y方向scale都为0变为默认的x方向和y方向scale都为1的动画，该动画时长为animateTo中指定的2000ms
40. // 消失时无转场效果
41. // $r('app.media.testImg')需要替换为开发者所需的图像资源文件。
42. Image($r('app.media.testImg')).width(200).height(200).margin({ top: 100 })
43. .transition(
44. TransitionEffect.asymmetric(
45. TransitionEffect.scale({ x: 0, y: 0 }),
46. TransitionEffect.IDENTITY
47. )
48. )
49. }
50. }.width('100%')
51. }
52. }
```

示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/H5aKE1tuR3-1Fv2LFmNsbA/zh-cn_image_0000002589326419.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=E407EF541EAB020379E771D9765803745815E4FC40F09DE360331967158DE600)

### 示例3（设置父子组件为transition）

该示例主要演示通过父子组件都配置[transition](ts-transition-animation-component.md#transition)来实现图片的出现和消失。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransitionEffectExample3 {
5. @State flag: boolean = true;
6. @State show: string = 'show';

8. build() {
9. Column() {
10. Button(this.show).width(80).height(30).margin(30)
11. .onClick(() => {
12. // 点击Button控制Image的显示和消失
13. if (this.flag) {
14. this.show = 'hide';
15. } else {
16. this.show = 'show';
17. }
18. this.flag = !this.flag;
19. })
20. if (this.flag) {
21. // 当flag条件改变时，会触发id为"column1"、"image1"、"image2"的transition动画。
22. // id为"column1"的组件是这棵新出现/消失的子树的根节点。
23. Column() {
24. Row() {
25. // $r('app.media.testImg')需要替换为开发者所需的图像资源文件。
26. Image($r('app.media.testImg')).width(150).height(150).id("image1")
27. .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
28. }

30. // $r('app.media.testImg')需要替换为开发者所需的图像资源文件。
31. Image($r('app.media.testImg'))
32. .width(150)
33. .height(150)
34. .margin({ top: 50 })
35. .id("image2")
36. .transition(TransitionEffect.scale({ x: 0, y: 0 }).animation({ duration: 1000 }))
37. Text("view").margin({ top: 50 })
38. }
39. .id("column1")
40. .transition(TransitionEffect.opacity(0.99).animation({ duration: 1000 }),
41. // 结束回调设置在消失的第一层节点上，确保能有消失的结束回调
42. (transitionIn: boolean) => {
43. console.info("transition finish, transitionIn:" + transitionIn);
44. }
45. )
46. }
47. }.width('100%')
48. }
49. }
```

示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_KKyeA5aRJqJFhhAmm3Syg/zh-cn_image_0000002589246361.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=57EF33441E710F49FD1D74D108BC4552C2B7AE7B4CB73DBA61299203F88B71FC)
