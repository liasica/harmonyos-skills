---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdseffect
title: hdsEffect
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS API > hdsEffect
category: harmonyos-references
scraped_at: 2026-04-29T13:57:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07829f2c40eee01a10e8904d5f43a22bab07ffd57fb2e0bab90989ae96203504
---

本模块提供组件的拓展视效能力，包括组件点光源效果、按压光效、动画控制。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { hdsEffect } from '@kit.UIDesignKit';
```

## HdsEffectBuilder

PhonePC/2in1TabletTV

将创建的视效参数添加到VisualEffect对象上，构建VisualEffect对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### constructor

PhonePC/2in1TabletTV

constructor()

HdsEffectBuilder的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### pointLight

PhonePC/2in1TabletTV

pointLight(value: PointLightEffect): HdsEffectBuilder

创建一个组件点光源效果，单个组件最多同时受12个光源照亮。支持点光源效果的组件范围如下：Button、Toggle、Row、Column、Image、Flex、Stack、Select、Menu、MenuItem。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| value | [PointLightEffect](ui-design-hdseffect.md#pointlighteffect) | 是 | 设置组件点光源属性。通过设置光源和被照亮的类型，实现点光源照亮周围组件的UI效果。  **说明**：光源位置初始化为组件正中心，不会跟着组件的位移而变化位置，因此不建议在滚动组件中使用点光源效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HdsEffectBuilder](ui-design-hdseffect.md#hdseffectbuilder) | 返回HdsEffectBuilder对象。 |

**示例：**

```
1. import { hdsEffect } from '@kit.UIDesignKit';

3. @Entry
4. @Component
5. struct Index {
6. @State lightSourceType: hdsEffect.PointLightSourceType = hdsEffect.PointLightSourceType.NONE;

8. build() {
9. Column({ space: 10 }) {
10. Row({ space: 10 }) {
11. Column() {
12. Text('illuminated').padding(10).fontColor(Color.White)
13. Text('illuminated').padding(10).fontColor(Color.White)
14. Text('illuminated').padding(10).fontColor(Color.White)
15. }
16. .visualEffect(new hdsEffect.HdsEffectBuilder()
17. .pointLight({
18. illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
19. })
20. .buildEffect())
21. }

23. Row({ space: 10 }) {
24. Button('lightSource')
25. .visualEffect(new hdsEffect.HdsEffectBuilder()
26. .pointLight({
27. sourceType: this.lightSourceType,
28. illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
29. })
30. .buildEffect())
31. .onTouch((event: TouchEvent) => {
32. if (event.type === TouchType.Down) {
33. this.lightSourceType = hdsEffect.PointLightSourceType.BRIGHT;
34. } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
35. this.lightSourceType = hdsEffect.PointLightSourceType.NONE;
36. }
37. })
38. }

40. Row({ space: 10 }) {
41. Column() {
42. Text('illuminated').padding(10).fontColor(Color.White)
43. Text('illuminated').padding(10).fontColor(Color.White)
44. Text('illuminated').padding(10).fontColor(Color.White)
45. }
46. .visualEffect(new hdsEffect.HdsEffectBuilder()
47. .pointLight({
48. illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
49. })
50. .buildEffect())
51. }
52. }
53. .backgroundColor(Color.Black)
54. .width('100%')
55. .height('100%')
56. .justifyContent(FlexAlign.Center)
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/xZRQGyNnRvqLTLV6Pu2sUA/zh-cn_image_0000002589326913.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=7CB79CCBF426E76B90339044FB5336D81559A8CD83EF5BC81562D36525556D8A)

### pressShadow

PhonePC/2in1TabletTV

pressShadow(type: PressShadowType): HdsEffectBuilder

设置当前组件按压阴影效果，一般用于组件按压后背景色变化。仅在Button组件上生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | [PressShadowType](ui-design-hdseffect.md#pressshadowtype) | 是 | 设置组件按压阴影效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HdsEffectBuilder](ui-design-hdseffect.md#hdseffectbuilder) | 返回HdsEffectBuilder对象。 |

**示例：**

```
1. import { hdsEffect } from '@kit.UIDesignKit';

3. @Entry
4. @Component
5. struct PressShadowExample {
6. @State button_blend_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
7. @State button_gradient_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;

9. build() {
10. NavDestination() {
11. Column({ space: 50 }) {
12. Button("BLEND_WHITE", { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
13. .visualEffect(new hdsEffect.HdsEffectBuilder()
14. .pressShadow(this.button_blend_state)
15. .buildEffect())
16. .onTouch((event: TouchEvent) => {
17. if (event.type === TouchType.Down) {
18. this.button_blend_state = hdsEffect.PressShadowType.BLEND_WHITE;
19. } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
20. this.button_blend_state = hdsEffect.PressShadowType.NONE;
21. }
22. })

24. Button("GRADIENT", { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
25. .visualEffect(new hdsEffect.HdsEffectBuilder()
26. .pressShadow(this.button_gradient_state)
27. .buildEffect())
28. .onTouch((event: TouchEvent) => {
29. if (event.type === TouchType.Down) {
30. this.button_gradient_state = hdsEffect.PressShadowType.BLEND_GRADIENT;
31. } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
32. this.button_gradient_state = hdsEffect.PressShadowType.NONE;
33. }
34. })
35. }
36. .height('70%')
37. .justifyContent(FlexAlign.Center)
38. }
39. .width('100%')
40. .height('100%')
41. .title('Button example')
42. .backgroundColor('#040404')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/sjfZiupWTqud3sRJ9vgTBQ/zh-cn_image_0000002589246853.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=0ADC78D6927E5AF0B99A31D90AF492AC19F5B4BBF049A0B461763DAC0CC36425)

### shaderEffect

PhonePC/2in1TabletTV

shaderEffect(params: ShaderEffectParams): HdsEffectBuilder

创建一个shader视效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [ShaderEffectParams](ui-design-hdseffect.md#shadereffectparams) | 是 | shader视效参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HdsEffectBuilder](ui-design-hdseffect.md#hdseffectbuilder) | 返回HdsEffectBuilder对象。 |

**示例：**

```
1. import { hdsEffect } from '@kit.UIDesignKit';

3. @Entry
4. @Component
5. struct Index {
6. @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();

8. build() {
9. Column() {
10. Stack() {
11. }
12. .visualEffect(new hdsEffect.HdsEffectBuilder()
13. .shaderEffect({
14. effectType: hdsEffect.EffectType.DUAL_EDGE_FLOW_LIGHT,
15. animation: {
16. duration: 4000,
17. iterations: -1,
18. autoPlay: true,
19. onFinish: () => {
20. console.info('Succeeded in finishing');
21. }
22. },
23. controller: this.controller,
24. params: {
25. firstEdgeFlowLight: {
26. startPos: 0,
27. endPos: 1.0,
28. color: '#1AD0F1',
29. },
30. secondEdgeFlowLight: {
31. startPos: 0.5,
32. endPos: 1.5,
33. color: '#FFA4E5',
34. }
35. }
36. })
37. .buildEffect())
38. .width(200)
39. .borderRadius('50%')
40. .clip(true)
41. .height(200)
42. .backgroundColor('#383838')
43. }
44. .justifyContent(FlexAlign.Center)
45. .backgroundColor(Color.Black)
46. .width('100%')
47. .height('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/dULkOq4YRGiLYTBiU5rjUw/zh-cn_image_0000002558767046.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=40F9C458632F02A52DD7B35656916434F10641C0A7998EE54A19947AD9180B8B)

### buildEffect

PhonePC/2in1TabletTV

buildEffect(): VisualEffect

将上文中设置的所有组件视效添加到VisualEffect对象上。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VisualEffect](js-apis-uieffect.md#visualeffect) | 返回带有各种视觉效果的VisualEffect。 |

## ShaderEffectParams

PhonePC/2in1TabletTV

shaderEffect视效配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| effectType | [EffectType](ui-design-hdseffect.md#effecttype) | 否 | 否 | 视效类型。 |
| animation | [AnimationParams](ui-design-hdseffect.md#animationparams) | 否 | 是 | 视效动画参数配置。 |
| params | [EffectParams](ui-design-hdseffect.md#effectparams) | 否 | 是 | shader参数配置。 |
| controller | [ShaderEffectController](ui-design-hdseffect.md#shadereffectcontroller) | 否 | 是 | 视效控制器。 |

## EffectType

PhonePC/2in1TabletTV

视效类型。

**设备行为差异：** 该视效在TV中无效果，在其他设备类型中可正常显示。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DUAL\_EDGE\_FLOW\_LIGHT | 0 | 双边边缘流光。 |
| UV\_BACKGROUND\_FLOW\_LIGHT | 1 | UV背景流光。 |

## AnimationParams

PhonePC/2in1TabletTV

视效动画参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 视效动画播放一次时间，单位为ms(毫秒)。  默认值：1000。  **说明：**  - 设置小于0的值时按0处理。  - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| iterations | number | 否 | 是 | 播放次数，-1为重复执行。  取值范围：[-1,+∞)。  默认值：1。  **说明：**  - 设置超出取值范围的值时按默认值处理。  - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| curve | [Curve](ts-appendix-enums.md#curve) | 否 | 是 | 动画曲线。 |
| delay | number | 否 | 是 | 视觉动画延迟播放时间，单位为ms(毫秒)。  默认值：0。  取值范围：(-∞, +∞)。  **说明：**  - delay>=0为延迟播放，delay<0表示提前播放。对于delay<0的情况：当delay的绝对值小于实际视效动画时长，视效动画将在开始后第一帧直接运动到delay绝对值的时刻的状态；当delay的绝对值大于等于实际视效动画时长，视效动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。  - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| autoPlay | boolean | 否 | 是 | 是否自动执行。true：自动执行；false不自动执行。  默认值：true。 |
| onFinish | [OnFinishCallback](ui-design-hdseffect.md#onfinishcallback) | 否 | 是 | 结束时回调函数。 |
| expectedFrameRateRange | [ExpectedFrameRateRange](ui-design-hdseffect.md#expectedframeraterange) | 否 | 是 | 帧率设置。 |

## OnFinishCallback

PhonePC/2in1TabletTV

type OnFinishCallback = () => void

视效结束回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

## ExpectedFrameRateRange

PhonePC/2in1TabletTV

视效帧率配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| expected | [FrameRateType](ui-design-hdseffect.md#frameratetype) | 否 | 否 | 目标帧率。 |
| min | [FrameRateType](ui-design-hdseffect.md#frameratetype) | 否 | 否 | 最小帧率。 |
| max | [FrameRateType](ui-design-hdseffect.md#frameratetype) | 否 | 否 | 最大帧率。 |

## FrameRateType

PhonePC/2in1TabletTV

视效帧率。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FRAME\_RATE\_15 | 15 | 帧率15FPS。 |
| FRAME\_RATE\_30 | 30 | 帧率30FPS。 |
| FRAME\_RATE\_60 | 60 | 帧率60FPS。 |

## EffectParams

PhonePC/2in1TabletTV

type EffectParams = DualEdgeFlowLightParam | UVFlowLightColorParam

视觉效果参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| [DualEdgeFlowLightParam](ui-design-hdseffect.md#dualedgeflowlightparam) | 双边边缘流光视效参数。 |
| [UVFlowLightColorParam](ui-design-hdseffect.md#uvflowlightcolorparam) | UV流光视效参数。 |

## DualEdgeFlowLightParam

PhonePC/2in1TabletTV

双边边缘流光视效参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| firstEdgeFlowLight | [EdgeFlowLightParam](ui-design-hdseffect.md#edgeflowlightparam) | 否 | 否 | 第一条流光参数配置。 |
| secondEdgeFlowLight | [EdgeFlowLightParam](ui-design-hdseffect.md#edgeflowlightparam) | 否 | 否 | 第二条流光参数配置。 |

## UVFlowLightColorParam

PhonePC/2in1TabletTV

UV流光视效参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| colorSource | Array<[ResourceColor](ts-types.md#resourcecolor)> | 否 | 否 | 背景流光颜色。 |
| colorTarget | Array<[ResourceColor](ts-types.md#resourcecolor)> | 否 | 是 | 目标渐变颜色。默认流光颜色不渐变。 |

## EdgeFlowLightParam

PhonePC/2in1TabletTV

边缘流光视效参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| startPos | number | 否 | 否 | 流光开始位置。以视效容器的上边缘的中点为起始点，取值单位为起始点沿着容器边缘至目标位置的距离与容器周长的比值。沿着容器边缘逆时针为正方向，顺时针为负方向。 |
| endPos | number | 否 | 否 | 流光结束位置。以视效容器的上边缘的中点为起始点，取值单位为起始点沿着容器边缘至目标位置的距离与容器周长的比值。沿着容器边缘逆时针为正方向，顺时针为负方向。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 流光颜色。 |

## ShaderEffectController

PhonePC/2in1TabletTV

视效控制器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### constructor

PhonePC/2in1TabletTV

constructor()

ShaderEffectController的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### play

PhonePC/2in1TabletTV

play(): void

开始执行视效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### pause

PhonePC/2in1TabletTV

pause(): void

暂停视效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### resume

PhonePC/2in1TabletTV

resume(): void

继续执行视效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### reverse

PhonePC/2in1TabletTV

reverse(): void

反转视效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### stop

PhonePC/2in1TabletTV

stop(): void

停止视效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

### setEffectParams

PhonePC/2in1TabletTV

setEffectParams(params: EffectParams): void

设置视效shader参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [EffectParams](ui-design-hdseffect.md#effectparams) | 是 | shaders视效参数。 |

## PointLightEffect

PhonePC/2in1TabletTV

点光源效果属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| sourceType | [PointLightSourceType](ui-design-hdseffect.md#pointlightsourcetype) | 否 | 是 | 组件发光效果类型，发光会影响到周围标记为可以被照亮的组件，并在组件上产生光效。  默认值：NONE，不发光。 |
| illuminatedType | [PointLightIlluminatedType](ui-design-hdseffect.md#pointlightilluminatedtype) | 否 | 是 | 组件受光效果类型，设置当前组件是否可以被光源照亮，以及被照亮的类型。  默认值：NONE，不受光。  **说明**：受光组件如果设置了border的颜色和宽度，会覆盖掉点光源效果。 |
| options | [PointLightOptions](ui-design-hdseffect.md#pointlightoptions) | 否 | 是 | 组件自定义发光参数选项。 |

说明

sourceType的优先级高于options。当同时设置sourceType和options时，options自定义发光参数不会生效。

## PointLightSourceType

PhonePC/2in1TabletTV

组件发光效果类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NONE | 0 | 组件光源类型：点光源不生效，组件无发光效果。 |
| SOFT | 1 | 组件光源类型：柔和点光源，发光强度较弱，周围照亮范围较小。 |
| BRIGHT | 2 | 组件光源类型：明亮点光源，发光强度较高，周围照亮范围较大。 |

## PointLightIlluminatedType

PhonePC/2in1TabletTV

组件受光效果类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NONE | 0 | 组件受光类型：不被照亮。 |
| BORDER | 1 | 组件受光类型：边缘被照亮。 |
| CONTENT | 2 | 组件受光类型：内容被照亮。 |
| BORDER\_CONTENT | 3 | 组件受光类型：边缘和内容被照亮。 |
| DEFAULT\_FEATHERING\_BORDER | 20 | 组件受光类型：边缘被照亮，并且有羽化效果。 |

## PointLightOptions

PhonePC/2in1TabletTV

组件自定义发光参数选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 光源颜色。  默认值：Color.White。 |
| intensity | number | 否 | 是 | 光源强度，建议取值范围0~1。数值越大，光源越强，当光源强度为0时，光源不发光。  默认值：0。 |
| height | [Dimension](ts-types.md#dimension10) | 否 | 是 | 光源高度。光源越高，照射范围越大。  默认值：0。 |
| bloom | number | 否 | 是 | 设置组件的泛光效果强度，建议取值范围为0~1。数值越大，泛光范围越大。  默认值：0。 |

## PressShadowType

PhonePC/2in1TabletTV

组件按压阴影效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | **说明** |
| --- | --- | --- |
| NONE | 0 | 无按压阴影效果。 |
| BLEND\_GRADIENT | 1 | 按压阴影为椭圆形径向渐变的白色，中心为透明度85%的白色，边界为不透明的白色。叠加在组件背景色之上。 |
| BLEND\_WHITE | 2 | 按压阴影为15%透明度的白色。叠加在组件背景色之上。 |
