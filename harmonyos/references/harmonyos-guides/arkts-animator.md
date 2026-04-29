---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animator
title: 帧动画（ohos.animator）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 帧动画（ohos.animator）
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f4206feef56fded3c5b1f97508329b636e34d814c70ded9a1231ecd05176ebe0
---

帧动画具备逐帧回调的特性，便于开发者在每一帧中处理需调整的属性。通过向应用提供[AnimatorResult](../harmonyos-references/js-apis-animator.md#animatorresult)的onFrame属性逐帧回调，帧动画使开发者能够在应用的每一帧设置属性值，从而实现组件属性值变化的自然过渡，营造出动画效果。帧动画接口详情可参考[@ohos.animator (动画)](../harmonyos-references/js-apis-animator.md)。

与属性动画相比，帧动画能让开发者实时感知动画进程，即时调整UI值，具备事件即时响应和可暂停的优势，但在性能上略逊于属性动画。当属性动画能满足需求时，建议优先采用属性动画接口实现。属性动画接口可参考[实现属性动画](arkts-attribute-animation-apis.md)。

| 名称 | 实现方式 | 事件响应方式 | 可暂停 | 性能 |
| --- | --- | --- | --- | --- |
| 帧动画（ohos.animator） | 开发者可每帧修改UI侧属性值，UI侧属性实时更新 | 实时响应 | 是 | 较差 |
| 属性动画 | UI侧只计算动画最终状态，动画过程为渲染值在改变，UI侧一直为动画最终状态，不感知实时渲染值 | 按最终状态响应 | 否 | 较好 |

如图所示，帧动画在动画过程中即可实时响应，而属性动画按最终状态响应。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/bTVEPvziTPW40J6KbEeSDQ/zh-cn_image_0000002558764494.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052815Z&HW-CC-Expire=86400&HW-CC-Sign=D374A44ECB75E20E9FADC13869773371A9DACDF9383C5A79868C10D6597E1F8D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/kP640CcuSNmft8r2V-A4IA/zh-cn_image_0000002558604838.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052815Z&HW-CC-Expire=86400&HW-CC-Sign=9F454F1C8F98747A672378ED7A3B950ECCBD2E52FA573FFC7DAB0EE54C551457)

## 使用帧动画实现动画效果

使用如下步骤可以创建一个简单的animator，并且在每个帧回调中打印当前插值。

1. 引入相关依赖。

   ```
   1. import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI';
   ```

   [AnimatorPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/AnimatorPage.ets#L15-L17)
2. 创建执行动画的对象。

   ```
   1. // 创建动画的初始参数
   2. let options: AnimatorOptions = {
   3. duration: 1500,
   4. easing: 'friction',
   5. delay: 0,
   6. fill: 'forwards',
   7. direction: 'normal',
   8. iterations: 2,
   9. // 动画onFrame 插值首帧值
   10. begin: 200.0,
   11. // 动画onFrame 插值尾帧值
   12. end: 400.0
   13. };
   14. let result: AnimatorResult | undefined = this.getUIContext().createAnimator(options);
   15. // 设置接收到帧时回调，动画播放过程中每帧会调用onFrame回调
   16. result.onFrame = (value: number) => {
   17. hilog.info(DOMAIN, TAG, 'current value is :' + value);

   19. }
   ```

   [AnimatorPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/AnimatorPage.ets#L34-L54)
3. 播放动画。

   ```
   1. // 播放动画
   2. result.play();
   ```

   [AnimatorPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/AnimatorPage.ets#L56-L59)
4. 动画执行完成后手动释放AnimatorResult对象。

   ```
   1. // 释放动画对象
   2. result = undefined;
   ```

   [AnimatorPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/AnimatorPage.ets#L61-L64)

## 使用帧动画实现小球抛物运动

1. 引入相关依赖。

   ```
   1. import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/Index.ets#L15-L17)
2. 定义要做动画的组件。

   ```
   1. Button()
   2. .width(60)
   3. .height(60)
   4. .translate({ x: this.translateX, y: this.translateY })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/Index.ets#L109-L114)
3. 在onPageShow中创建AnimatorResult对象。

   ```
   1. onPageShow(): void {
   2. // 创建animatorResult对象
   3. this.animatorResult = this.getUIContext().createAnimator(this.animatorOption);
   4. this.animatorResult.onFrame = (progress: number) => {
   5. this.translateX = progress;
   6. if (progress > this.topWidth && this.translateY < this.bottomHeight) {
   7. this.translateY = Math.pow(progress - this.topWidth, 2) * this.g;
   8. }
   9. }
   10. // 动画取消时执行方法
   11. this.animatorResult.onCancel = () => {
   12. // 请将$r('app.string.cancel')替换为实际资源文件，在本示例中该资源文件的value值为"取消"
   13. this.animatorStatus = $r('app.string.cancel');
   14. }
   15. // 动画完成时执行方法
   16. this.animatorResult.onFinish = () => {
   17. // 请将$r('app.string.complete')替换为实际资源文件，在本示例中该资源文件的value值为"完成"
   18. this.animatorStatus = $r('app.string.complete');
   19. }
   20. // 动画重复播放时执行方法
   21. this.animatorResult.onRepeat = () => {
   22. // 'repeat'资源文件中的value值为'动画重复播放'
   23. hilog.info(DOMAIN, TAG, this.manager.getStringByNameSync('repeat'));
   24. }
   25. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/Index.ets#L50-L76)
4. 定义动画播放，重置，暂停的按钮。

   ```
   1. // 请将$r('app.string.play')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
   2. Button($r('app.string.play')).onClick(() => {
   3. this.animatorResult?.play();
   4. // 请将$r('app.string.playing')替换为实际资源文件，在本示例中该资源文件的value值为"播放中"
   5. this.animatorStatus = $r('app.string.playing');
   6. }).width(80).height(35)
   7. // 请将$r('app.string.reset')替换为实际资源文件，在本示例中该资源文件的value值为"重置"
   8. Button($r('app.string.reset')).onClick(() => {
   9. this.translateX = 0;
   10. this.translateY = 0;
   11. }).width(80).height(35)
   12. // 请将$r('app.string.pause')替换为实际资源文件，在本示例中该资源文件的value值为"暂停"
   13. Button($r('app.string.pause')).onClick(() => {
   14. this.animatorResult?.pause();
   15. // 请将$r('app.string.pause')替换为实际资源文件，在本示例中该资源文件的value值为"暂停"
   16. this.animatorStatus = $r('app.string.pause');
   17. }).width(80).height(35)
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/Index.ets#L87-L105)
5. 在页面隐藏或销毁的生命周期中释放动画对象，避免内存泄漏。

   ```
   1. onPageHide(): void {
   2. this.animatorResult = undefined;
   3. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template4/Index.ets#L78-L82)

完整示例如下。

```
1. import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;
6. const TAG: string = '[AnimatorTest]';

8. @Entry
9. @Component
10. struct Index {
11. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
12. private manager = this.context.resourceManager;
13. @State animatorResult: AnimatorResult | undefined = undefined;
14. // 'create'资源文件中的value值为'创建'
15. @State animatorStatus: string = 'create';
16. begin: number = 0;
17. end: number = 300;
18. topWidth: number = 150;
19. bottomHeight: number = 100;
20. // 自由落体运动的加速度系数
21. g: number = 0.18;
22. animatorOption: AnimatorOptions = {
23. duration: 4000,
24. delay: 0,
25. easing: 'linear',
26. iterations: 1,
27. fill: "forwards",
28. direction: 'normal',
29. begin: this.begin,
30. end: this.end
31. };
32. @State translateX: number = 0;
33. @State translateY: number = 0;

35. onPageShow(): void {
36. this.animatorResult = this.getUIContext().createAnimator(this.animatorOption);
37. this.animatorResult.onFrame = (progress: number) => {
38. this.translateX = progress;
39. if (progress > this.topWidth && this.translateY < this.bottomHeight) {
40. this.translateY = Math.pow(progress - this.topWidth, 2) * this.g;
41. }
42. }
43. this.animatorResult.onCancel = () => {
44. // 'cancel'资源文件中的value值为'取消'
45. this.animatorStatus = 'cancel';
46. }
47. this.animatorResult.onFinish = () => {
48. // 'complete'资源文件中的value值为'完成'
49. this.animatorStatus = 'complete';
50. }
51. this.animatorResult.onRepeat = () => {
52. // 'repeat'资源文件中的value值为'动画重复播放'
53. hilog.info(DOMAIN, TAG, this.manager.getStringByNameSync('repeat'));
54. }
55. }

57. onPageHide(): void {
58. this.animatorResult = undefined;
59. }

61. build() {
62. Column() {
63. Column({ space: 30 }) {
64. // 请将$r('app.string.play')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
65. Button($r('app.string.play')).onClick(() => {
66. this.animatorResult?.play();
67. // 'playing'资源文件中的value值为'播放中'
68. this.animatorStatus = 'playing';
69. }).width(80).height(35)
70. // 请将$r('app.string.reset')替换为实际资源文件，在本示例中该资源文件的value值为"重置"
71. Button($r('app.string.reset')).onClick(() => {
72. this.translateX = 0;
73. this.translateY = 0;
74. }).width(80).height(35)
75. // 请将$r('app.string.pause')替换为实际资源文件，在本示例中该资源文件的value值为"暂停"
76. Button($r('app.string.pause')).onClick(() => {
77. this.animatorResult?.pause();
78. // 'pause'资源文件中的value值为'暂停'
79. this.animatorStatus = 'pause';
80. }).width(80).height(35)
81. }.width('100%').height('25%')

83. Stack() {
84. Button()
85. .width(60)
86. .height(60)
87. .translate({ x: this.translateX, y: this.translateY })
88. }
89. .width('100%')
90. .height('45%')
91. .align(Alignment.Start)
92. // 'animatorStatus'资源文件中的value值为'当前动画状态为:'
93. Text(this.manager.getStringByNameSync('animatorStatus') + this.manager.getStringByNameSync(this.animatorStatus))
94. }.width('100%').height('100%')
95. }
96. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animator/template3/Index.ets#L15-L112)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/tuePB_9DTx619XqIgoikcQ/zh-cn_image_0000002589324363.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052815Z&HW-CC-Expire=86400&HW-CC-Sign=665992176505155217316ABC8E77FEA2264CFCB2DC2BC255994F9B7BF99898E8)
