---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-spring-curve
title: 弹簧曲线
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画曲线 > 弹簧曲线
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4bc09d7f05d4c43839cd66356f3f9255574c18fbd23e0f32804a420e947618b9
---

阻尼弹簧曲线（以下简称弹簧曲线）对应的阻尼弹簧系统中，偏离平衡位置的物体一方面受到弹簧形变产生的反向作用力，被迫发生振动。另一方面，阻尼的存在为物体振动提供阻力。除阻尼为0的特殊情况，物体在振动过程中振幅不断减小，且最终趋于0，其轨迹对应的动画曲线自然连续。

采用弹簧曲线的动画在达终点时动画速度为0，不会产生动画“戛然而止”的观感，以避免影响用户体验。

ArkUI提供了四种阻尼弹簧曲线接口。

* [curves.springMotion](../harmonyos-references/js-apis-curve.md#curvesspringmotion9)：创建弹性动画，动画时长由曲线参数、属性变化值大小和弹簧初速度自动计算，开发者指定的动画时长不生效。

  springMotion不提供速度设置接口，速度通过继承获得，无需开发者指定。对于某个属性，如果当前存在正在运行的springMotion或者[responsiveSpringMotion](../harmonyos-references/js-apis-curve.md#curvesresponsivespringmotion9)类型动画，新创建的弹簧动画将停止正在运行的动画，并继承其当前时刻的动画属性值和速度作为新建动画的初始状态。此外，接口提供默认参数，便于开发者直接使用。

  ```
  1. function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve;
  ```
* [curves.responsiveSpringMotion](../harmonyos-references/js-apis-curve.md#curvesresponsivespringmotion9)：是springMotion动画的一种特例，仅默认参数不同。一般用于跟手做成动画的场景，离手时可用springMotion创建动画，此时离手阶段动画将自动继承跟手阶段动画速度，完成动画衔接。

  当新动画的overlapDuration参数不为0，且当前属性的上一个springMotion动画还未结束时，response和dampingFraction将在overlapDuration指定的时间内，从旧动画的参数值过渡到新动画的参数值。

  ```
  1. function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve;
  ```
* [curves.interpolatingSpring](../harmonyos-references/js-apis-curve.md#curvesinterpolatingspring10)：适合于需要指定初速度的动效场景，动画时长同样由接口参数自动计算，开发者在动画接口中指定的时长不生效。

  曲线接口提供速度入参，且由于接口对应一条从0到1的阻尼弹簧曲线，实际动画值根据曲线进行插值计算。所以速度也应该为归一化速度，其值等于动画属性改变的绝对速度除以动画属性改变量。因此不适合于动画起点属性值和终点属性值相同的场景，此时动画属性改变量为0，归一化速度不存在。

  ```
  1. function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve;
  ```
* [curves.springCurve](../harmonyos-references/js-apis-curve.md#curvesspringcurve9)：适合于需要直接指定动画时长的场景。springCurve接口与interpolatingSpring接口几乎一致，但是对于采用springCurve的动画，会将曲线的物理时长映射到指定的时长，相当于在时间轴上拉伸或压缩曲线，破坏曲线原本的物理规律，因此不建议开发者使用。

  ```
  1. function springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve;
  ```

关于弹簧曲线完整的使用示例和参考效果如下，开发者也可参考[动画衔接](arkts-animation-smoothing.md)，掌握使用responsiveSpringMotion和springMotion进行手势和动画之间的衔接。

弹簧曲线的示例代码和效果如下。

```
1. import { curves } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. class Spring {
5. public title: string;
6. public subTitle: ResourceStr;
7. public iCurve: ICurve;

9. constructor(title: string, subTitle: ResourceStr, iCurve: ICurve) {
10. this.title = title;
11. this.iCurve = iCurve;
12. this.subTitle = subTitle;
13. }
14. }

16. // 弹簧组件
17. @Component
18. struct Motion {
19. @Prop dRotate: number = 0;
20. private title: string = '';
21. private subTitle: ResourceStr = '';
22. private iCurve: ICurve | undefined = undefined;

24. build() {
25. Column() {
26. Circle()
27. .translate({ y: this.dRotate })
28. .animation({ curve: this.iCurve, iterations: -1 })
29. .foregroundColor('#317AF7')
30. .width(30)
31. .height(30)

33. Column() {
34. Text(this.title)
35. .fontColor(Color.Black)
36. .fontSize(10).height(30)
37. Text(this.subTitle)
38. .fontColor(0xcccccc)
39. .fontSize(10).width(50)
40. }
41. .borderWidth({ top: 1 })
42. .borderColor(0xf5f5f5)
43. .width(80)
44. .alignItems(HorizontalAlign.Center)
45. .height(100)

47. }
48. .height(110)
49. .margin({ bottom: 5 })
50. .alignItems(HorizontalAlign.Center)
51. }
52. }

54. @Entry
55. @Component
56. export struct SpringCurve {
57. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
58. @State dRotate: number = 0;
59. private springs: Spring[] = [
60. // 请将$r('app.string.springCurve_text1')替换为实际资源文件，在本示例中该资源文件的value值为"周期1, 阻尼0.25"
61. new Spring('springMotion', $r('app.string.springCurve_text1'), curves.springMotion(1, 0.25)),
62. // 请将$r('app.string.springCurve_text2')替换为实际资源文件，在本示例中该资源文件的value值为"弹性跟手曲线"
63. new Spring('responsive' + '\n' + 'SpringMotion', $r('app.string.springCurve_text2'),
64. curves.responsiveSpringMotion(1, 0.25)),
65. // 请将$r('app.string.springCurve_text3')替换为实际资源文件，在本示例中该资源文件的value值为"初始速度10， 质量1， 刚度228， 阻尼30"
66. new Spring('interpolating' + '\n' + 'Spring', $r('app.string.springCurve_text3'),
67. curves.interpolatingSpring(10, 1, 228, 30)),
68. // 请将$r('app.string.springCurve_text1')替换为实际资源文件，在本示例中该资源文件的value值为"周期1, 阻尼0.25"
69. new Spring('springCurve', $r('app.string.springCurve_text1'),
70. curves.springCurve(10, 1, 228, 30))
71. ];

73. build() {
74. Row() {
75. ForEach(this.springs, (item: Spring) => {
76. Motion({
77. title: item.title,
78. subTitle: item.subTitle,
79. iCurve: item.iCurve,
80. dRotate: this.dRotate
81. })
82. })
83. }
84. .justifyContent(FlexAlign.Center)
85. .alignItems(VerticalAlign.Bottom)
86. .width('100%')
87. .height(437)
88. .margin({ top: 20 })
89. .onClick(() => {
90. this.dRotate = -50;
91. })
92. }
93. }
```

[SpringCurve.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/springCurve/template1/SpringCurve.ets#L16-L111)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/kR5yZW9pTvOBaj22wfI1rg/zh-cn_image_0000002552798348.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233957Z&HW-CC-Expire=86400&HW-CC-Sign=935445D522902EFCBA800B472204898D728B89F0E3A271FB367E4B88368EF4B7)
