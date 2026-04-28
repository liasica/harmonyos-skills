---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto
title: 关键帧动画 (keyframeAnimateTo)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 关键帧动画 (keyframeAnimateTo)
category: harmonyos-references
scraped_at: 2026-04-28T08:02:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:76cca39e3a9d8193f39d22e7604a1b5d13f0b2dabca3f92d099f290f5c280661
---

在[UIContext](arkts-apis-uicontext-uicontext.md)中提供keyframeAnimateTo接口来指定若干个关键帧状态，实现分段的动画。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态，例如文字、[Canvas](ts-components-canvas-canvas.md)的内容等，如果要内容跟随宽高变化，可以使用[renderFit](ts-universal-attributes-renderfit.md)属性配置。

说明

从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该接口为[UIContext](arkts-apis-uicontext-uicontext.md)类的成员函数，需要通过UIContext实例对象调用。

keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void

设置关键帧动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [KeyframeAnimateParam](ts-keyframeanimateto.md#keyframeanimateparam对象说明) | 是 | 关键帧动画的整体动画参数。 |
| keyframes | Array<[KeyframeState](ts-keyframeanimateto.md#keyframestate对象说明)> | 是 | 所有的关键帧状态。 |

## KeyframeAnimateParam对象说明

PhonePC/2in1TabletTVWearable

动画选项设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| delay | number | 否 | 是 | 动画的整体延时时间，单位为ms（毫秒），默认不延时播放。  默认值：0  **说明：**  delay>=0为延迟播放，delay<0表示提前播放。对于delay<0的情况：当delay的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到delay绝对值的时刻的状态；当delay的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iterations | number | 否 | 是 | 动画播放次数。默认播放一次，设置为-1时表示无限次播放。设置为0时表示无动画效果。  默认值：1  **取值范围：**[-1, +∞)  **说明：**  - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onFinish | () => void | 否 | 是 | 动画播放完成回调。当keyframe动画所有次数播放完成后调用。在设置的开发者选项中关闭过渡动画，或UIAbility从前台切换至后台时会立即结束仍在播放中的有限循环keyframe动画，触发播放完成回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| expectedFrameRateRange19+ | [ExpectedFrameRateRange](ts-explicit-animation.md#expectedframeraterange11) | 否 | 是 | 设置动画的期望帧率。  **默认值：**{min:0, max:0, expected:0}，即跟随应用帧率。  **说明：**  开发者通过设置有效的期望帧率后，系统会收集设置的请求帧率，进行决策和分发，在渲染管线上进行分频，尽量能够满足开发者的期望帧率。开发者设置的期望帧率值不能代表最终实际效果，会受限于系统能力和屏幕刷新率。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## KeyframeState对象说明

PhonePC/2in1TabletTVWearable

设置关键帧选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 否 | 该段关键帧动画的持续时间，单位为毫秒。  取值范围：[0, +∞)  **说明：**  - 设置小于0的值时按0处理。  - 设置浮点型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| curve | [Curve](ts-appendix-enums.md#curve)| string | [ICurve](ts-explicit-animation.md#icurve9) | 否 | 是 | 该关键帧使用的动画曲线。  推荐以Curve或ICurve形式指定。  当类型为string时，为动画插值曲线，取值参考[AnimateParam](ts-explicit-animation.md#animateparam对象说明)的curve参数。  默认值：Curve.EaseInOut  **说明：**  由于[springMotion](js-apis-curve.md#curvesspringmotion9)、[responsiveSpringMotion](js-apis-curve.md#curvesresponsivespringmotion9)、[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)曲线时长不生效，故不支持这三种曲线。 |
| event | () => void | 否 | 否 | 指定在该关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要演示如何通过keyframeAnimateTo来设置关键帧动画。

```
1. // xxx.ets
2. import { UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct KeyframeDemo {
7. @State myScale: number = 1.0;
8. uiContext: UIContext | undefined = undefined;

10. aboutToAppear() {
11. this.uiContext = this.getUIContext?.();
12. }

14. build() {
15. Column() {
16. Circle()
17. .width(100)
18. .height(100)
19. .fill("#46B1E3")
20. .margin(100)
21. .scale({ x: this.myScale, y: this.myScale })
22. .onClick(() => {
23. if (!this.uiContext) {
24. console.info("no uiContext, keyframe failed");
25. return;
26. }
27. this.myScale = 1;
28. // 设置关键帧动画整体播放3次
29. this.uiContext.keyframeAnimateTo({
30. iterations: 3,
31. expectedFrameRateRange: {
32. min: 10,
33. max: 120,
34. expected: 60,
35. }
36. }, [
37. {
38. // 第一段关键帧动画时长为800ms，scale属性做从1到1.5的动画
39. duration: 800,
40. event: () => {
41. this.myScale = 1.5;
42. }
43. },
44. {
45. // 第二段关键帧动画时长为500ms，scale属性做从1.5到1的动画
46. duration: 500,
47. event: () => {
48. this.myScale = 1;
49. }
50. }
51. ]);
52. })
53. }.width('100%').margin({ top: 5 })
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/tcaEJw0FSw-iRFynPiY7cA/zh-cn_image_0000002552960024.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=1B71B357C2B049A5F1C2E39E9766B2F7EFF8706ED8C9BAA4728A2809785CB618)
