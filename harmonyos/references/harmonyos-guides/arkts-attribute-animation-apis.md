---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-animation-apis
title: 实现属性动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 属性动画 > 实现属性动画
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e3fcd6059328f361d891e5c7efab954f13042ba0c77b6877b0e08a7828ab556
---

通过可动画属性改变引起UI上产生的连续视觉效果，即为属性动画。属性动画是最基础易懂的动画，ArkUI提供三种动画接口[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)、[animation](../harmonyos-references/ts-animatorproperty.md)和[keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)驱动组件属性按照动画曲线等动画参数进行连续的变化，产生属性动画。

说明

本章节讨论的属性动画不是狭义的[属性动画接口](../harmonyos-references/ts-animatorproperty.md)，而是通过给定新的可动画属性终值，对属性产生动画的方式。

| 动画接口 | 作用域 | 原理 | 使用场景 |
| --- | --- | --- | --- |
| animateTo | 闭包内改变属性引起的界面变化。 | 通用函数，对闭包前界面和闭包中的状态变量引起的界面之间的差异做动画。  支持多次调用，支持嵌套。 | 适用对多个可动画属性配置相同动画参数的动画。  需要嵌套使用动画的场景。  如果需要实现多段动画循环的效果，建议通过设置[AnimateParam](../harmonyos-references/ts-explicit-animation.md#animateparam对象说明)的playMode和iterations属性实现，或使用keyframeAnimateTo实现。 |
| animation | 组件通过属性接口绑定的属性变化引起的界面变化。 | 识别组件的可动画属性变化，自动添加动画。  组件的接口调用是从下往上执行，animation只会作用于在其之上的属性调用。  组件可以根据调用顺序对多个属性设置不同的animation。 | 适用于对多个可动画属性配置不同参数动画的场景。 |
| keyframeAnimateTo | 多个闭包内改变属性引起的分段属性动画。 | 通用函数，每一段闭包中的状态变量与前一次的差异做动画。  支持多次调用，不推荐嵌套。 | 适用于同一属性需要做连续多个动画的场景。 |

## 使用animateTo产生属性动画

```
1. animateTo(value: AnimateParam, event: () => void): void
```

[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口参数中，value指定[AnimateParam对象](../harmonyos-references/ts-explicit-animation.md#animateparam对象说明)（包括时长、曲线等）event为动画的闭包函数，闭包内变量改变产生的属性动画将遵循相同的动画参数。

说明

直接使用animateTo可能导致[UI上下文不明确](arkts-global-interface.md)的问题，建议使用[getUIContext()](../harmonyos-references/ts-custom-component-api.md#getuicontext)获取[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)实例，并使用[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)调用绑定实例的animateTo。

```
1. import { curves } from '@kit.ArkUI';
2. @Entry
3. @Component
4. struct attrAnimateToDemo2 {
5. @State animate: boolean = false;
6. // 第一步: 声明相关状态变量
7. @State rotateValue: number = 0; // 组件一旋转角度
8. @State translateX: number = 0; // 组件二偏移量
9. @State opacityValue: number = 1; // 组件二透明度

11. // 第二步：将状态变量设置到相关可动画属性接口
12. build() {
13. Row() {
14. // 组件一
15. Column() {
16. }
17. .rotate({ angle: this.rotateValue })
18. .backgroundColor('#317AF7')
19. .justifyContent(FlexAlign.Center)
20. .width(100)
21. .height(100)
22. .borderRadius(30)
23. .onClick(() => {
24. this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
25. this.animate = !this.animate;
26. // 第三步：闭包内通过状态变量改变UI界面
27. // 这里可以写任何能改变UI的逻辑比如数组添加，显隐控制，系统会检测改变后的UI界面与之前的UI界面的差异，对有差异的部分添加动画
28. // 组件一的rotate属性发生变化，所以会给组件一添加rotate旋转动画
29. this.rotateValue = this.animate ? 90 : 0;
30. // 组件二的透明度发生变化，所以会给组件二添加透明度的动画
31. this.opacityValue = this.animate ? 0.6 : 1;
32. // 组件二的translate属性发生变化，所以会给组件二添加translate偏移动画
33. this.translateX = this.animate ? 50 : 0;
34. })
35. })

37. // 组件二
38. Column() {
39. }
40. .justifyContent(FlexAlign.Center)
41. .width(100)
42. .height(100)
43. .backgroundColor('#D94838')
44. .borderRadius(30)
45. .opacity(this.opacityValue)
46. .translate({ x: this.translateX })
47. }
48. .width('100%')
49. .height('100%')
50. .justifyContent(FlexAlign.Center)
51. }
52. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animation/template2/Index.ets#L15-L68)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/MGpWbcArS36IyG4PoBhdPQ/zh-cn_image_0000002552957980.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233955Z&HW-CC-Expire=86400&HW-CC-Sign=189C96CF2B030376DB26F7C3FAC9693587BDB297DB81AC935C05BC0290DFA351)

## 使用animation产生属性动画

相比于animateTo接口需要将属性修改封装在闭包中执行，[animation](../harmonyos-references/ts-animatorproperty.md)接口无需使用闭包，只需将其加在要做动画的可动画属性后即可。animation只要检测到其绑定的可动画属性发生变化，就会自动添加属性动画，animateTo则必须在动画闭包内改变可动画属性的值从而生成动画。

```
1. import { curves } from '@kit.ArkUI';
2. @Entry
3. @Component
4. struct attrAnimationDemo3 {
5. @State animate: boolean = false;
6. // 第一步: 声明相关状态变量
7. @State rotateValue: number = 0; // 组件一旋转角度
8. @State translateX: number = 0; // 组件二偏移量
9. @State opacityValue: number = 1; // 组件二透明度

11. // 第二步：将状态变量设置到相关可动画属性接口
12. build() {
13. Row() {
14. // 组件一
15. Column() {
16. }
17. .opacity(this.opacityValue)
18. .rotate({ angle: this.rotateValue })
19. // 第三步：通过属性动画接口开启属性动画
20. .animation({ curve: curves.springMotion() })
21. .backgroundColor('#317AF7')
22. .justifyContent(FlexAlign.Center)
23. .width(100)
24. .height(100)
25. .borderRadius(30)
26. .onClick(() => {
27. this.animate = !this.animate;
28. // 第四步：闭包内通过状态变量改变UI界面
29. // 这里可以写任何能改变UI的逻辑比如数组添加，显隐控制，系统会检测改变后的UI界面与之前的UI界面的差异，对有差异的部分添加动画
30. // 组件一的rotate属性发生变化，所以会给组件一添加rotate旋转动画
31. this.rotateValue = this.animate ? 90 : 0;
32. // 组件二的translate属性发生变化，所以会给组件二添加translate偏移动画
33. this.translateX = this.animate ? 50 : 0;
34. // 父组件column的opacity属性有变化，会导致其子节点的透明度也变化，所以这里会给column和其子节点的透明度属性都添加动画
35. this.opacityValue = this.animate ? 0.6 : 1;
36. })

38. // 组件二
39. Column() {
40. }
41. .justifyContent(FlexAlign.Center)
42. .width(100)
43. .height(100)
44. .backgroundColor('#D94838')
45. .borderRadius(30)
46. .opacity(this.opacityValue)
47. .translate({ x: this.translateX })
48. .animation({ curve: curves.springMotion() })
49. }
50. .width('100%')
51. .height('100%')
52. .justifyContent(FlexAlign.Center)
53. }
54. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animation/template3/Index.ets#L15-L70)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/_TLXoY2zT9SrlZ6Zzbs9Zg/zh-cn_image_0000002583477981.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233955Z&HW-CC-Expire=86400&HW-CC-Sign=C9726965A67F87FDD99046608E6370D9FE0B7C8A037859C9F02A033594C2CC90)

## 使用keyframeAnimateTo产生属性动画

```
1. keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void
```

[keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)接口参数中，第一个参数[KeyframeAnimateParam](../harmonyos-references/ts-keyframeanimateto.md#keyframeanimateparam对象说明)为关键帧动画的整体参数（包括延时、播放次数、结束回调、期望帧率），第二个参数是一个数组，每一项表示一个关键帧内的动画行为；每一段动画可单独控制动画参数（包括时长、曲线等）。

在同一属性存在多段动画过程的场景，可通过在结束回调中再创建新动画实现，但写法更复杂，且每次创建新动画需要耗时，会有衔接卡顿现象。此场景更适宜用关键帧动画实现。

以下示例主要演示如何通过keyframeAnimateTo来设置关键帧动画。

```
1. @Entry
2. @Component
3. struct KeyframeAnimateToDemo {
4. // 第一步: 声明相关状态变量
5. @State rotateValue: number = 0; // 组件一旋转角度
6. @State translateX: number = 0; // 组件二偏移量
7. @State opacityValue: number = 1; // 组件二透明度
8. // 第二步：将状态变量设置到相关可动画属性接口
9. build() {
10. Row() {
11. // 组件一
12. Column() {
13. }
14. .rotate({ angle: this.rotateValue })
15. .backgroundColor('#317AF7')
16. .justifyContent(FlexAlign.Center)
17. .width(100)
18. .height(100)
19. .borderRadius(30)
20. .onClick(() => {
21. // 第三步：调用keyframeAnimateTo接口
22. this.getUIContext()?.keyframeAnimateTo({
23. iterations: 1
24. }, [
25. {
26. // 第一段关键帧动画时长为800ms，组件一顺时针旋转90度，组件二的透明度变从1变为0.6，组件二的translate从0位移到50
27. duration: 800,
28. event: () => {
29. this.rotateValue = 90;
30. this.opacityValue = 0.6;
31. this.translateX = 50;
32. }
33. },
34. {
35. // 第二段关键帧动画时长为500ms，组件一逆时针旋转90度恢复至0度，组件二的透明度变从0.6变为1，组件二的translate从50位移到0
36. duration: 500,
37. event: () => {
38. this.rotateValue = 0;
39. this.opacityValue = 1;
40. this.translateX = 0;
41. }
42. }
43. ]);
44. })
45. // 组件二
46. Column() {
47. }
48. .justifyContent(FlexAlign.Center)
49. .width(100)
50. .height(100)
51. .backgroundColor('#D94838')
52. .borderRadius(30)
53. .opacity(this.opacityValue)
54. .translate({ x: this.translateX })
55. }
56. .width('100%')
57. .height('100%')
58. .justifyContent(FlexAlign.Center)
59. }
60. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animation/template4/Index.ets#L16-L77)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/J12CXrvPSxCPAnFpBsmArw/zh-cn_image_0000002552798332.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233955Z&HW-CC-Expire=86400&HW-CC-Sign=D4D6693FC5CAAB25F14AFA9254F5D34C612EDAF9FCFD16CE60BD0DF298212789)

说明

* 在对组件位置大小变化做动画的时候，由于布局属性的改变会触发测量布局，性能开销大。而[scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)属性的改变不会触发测量布局，性能开销小。因此，在组件位置大小持续发生变化的场景，如跟手触发组件大小变化的场景，推荐使用scale。
* 属性动画应该作用于始终存在的组件，对于将要出现或者将要消失的组件的动画应该使用[转场动画](arkts-transition-overview.md)。
* 尽量不要使用动画结束回调。属性动画是对已经发生的状态进行的动画，不需要开发者去处理结束的逻辑。如果要使用结束回调，一定要正确处理连续操作的数据管理。
* 在设置的开发者选项中关闭过渡动画，或UIAbility从前台切换至后台，会立即执行动画结束回调。建议对此类场景进行一定的验证并避免在动画结束回调中加入时序相关的功能逻辑。
