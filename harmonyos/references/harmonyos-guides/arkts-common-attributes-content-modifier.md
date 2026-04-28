---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-attributes-content-modifier
title: 内容修改器 (ContentModifier)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > Modifier机制 > 内容修改器 (ContentModifier)
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b28069ddea5ef499dbbce470a0222e68016f4a131405935b946ffab24b875d80
---

当开发者期望自定义组件的内容区时，比如Checkbox的内部显示一个五角星等场景时，可以使用此功能。

仅[Button](../harmonyos-references/ts-basic-components-button.md)、[Checkbox](../harmonyos-references/ts-basic-components-checkbox.md)、[DataPanel](../harmonyos-references/ts-basic-components-datapanel.md)、[TextTimer](../harmonyos-references/ts-basic-components-texttimer.md)、[Slider](../harmonyos-references/ts-basic-components-slider.md)、[Select](../harmonyos-references/ts-basic-components-select.md)、[Rating](../harmonyos-references/ts-basic-components-rating.md)、[Radio](../harmonyos-references/ts-basic-components-radio.md)、[Gauge](../harmonyos-references/ts-basic-components-gauge.md)、[Toggle](../harmonyos-references/ts-basic-components-toggle.md)、[TextClock](../harmonyos-references/ts-basic-components-textclock.md)组件支持该能力。

使用ContentModifier自定义Checkbox样式，用五边形Checkbox替换默认Checkbox。选中时，五边形内部显示红色三角图案，标题显示“选中”；取消选中时，红色三角图案消失，标题显示“非选中”。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { resourceManager } from '@kit.LocalizationKit';

4. const DOMAIN = 0x0000;
5. // xxx.ets
6. class MyCheckboxStyle implements ContentModifier<CheckBoxConfiguration> {
7. public selectedColor: Color = Color.White;

9. constructor(selectedColor: Color) {
10. this.selectedColor = selectedColor;
11. }

13. applyContent(): WrappedBuilder<[CheckBoxConfiguration]> {
14. return wrapBuilder(buildCheckbox);
15. }
16. }

18. @Builder
19. function buildCheckbox(config: CheckBoxConfiguration) {
20. Column({ space: 10 }) {
21. Text() {
22. Span(config.name)
23. // 请将$r('app.string.checked_context')替换为实际资源文件，在本示例中该资源文件的value值为"（选中）"
24. // 请将$r('app.string.unchecked_context')替换为实际资源文件，在本示例中该资源文件的value值为"（非选中）"
25. Span(config.selected ? $r('app.string.checked_context') : $r('app.string.unchecked_context'))
26. }
27. Shape() {
28. // 五边形复选框样式
29. Path()
30. .width(200)
31. .height(60)
32. .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
33. .fillOpacity(0)
34. .strokeWidth(3)
35. // 红色三角图案样式
36. Path()
37. .width(10)
38. .height(10)
39. .commands('M50 0 L100 100 L0 100 Z')
40. .visibility(config.selected ? Visibility.Visible : Visibility.Hidden)
41. .fill(config.selected ? (config.contentModifier as MyCheckboxStyle).selectedColor : Color.Black)
42. .stroke((config.contentModifier as MyCheckboxStyle).selectedColor)
43. .margin({ left: 11, top: 10 })
44. }
45. .width(300)
46. .height(200)
47. .viewPort({
48. x: 0,
49. y: 0,
50. width: 310,
51. height: 310
52. })
53. .strokeLineJoin(LineJoinStyle.Miter)
54. .strokeMiterLimit(5)
55. .onClick(() => {
56. // 点击后，触发复选框点击状态变化
57. if (config.selected) {
58. config.triggerChange(false);
59. } else {
60. config.triggerChange(true);
61. }
62. })
63. .margin({ left: 150 })
64. }
65. }

67. @Entry
68. @Component
69. struct Index {
70. private resmg: resourceManager.ResourceManager | undefined = this.getUIContext().getHostContext()?.resourceManager
71. build() {
72. Row() {
73. Column() {
74. //选中和不选中按钮
75. // 请将$r('app.string.checkbox_status')替换为实际资源文件，在本示例中该资源文件的value值为"复选框状态"
76. Checkbox({ name: this.resmg?.getStringSync($r('app.string.checkbox_status').id), group: 'checkboxGroup' })
77. .select(true)
78. .contentModifier(new MyCheckboxStyle(Color.Red))
79. .onChange((value: boolean) => {
80. hilog.info(DOMAIN, 'testTag', 'Checkbox change is' + value);
81. })
82. }
83. .width('100%')
84. }
85. .height('100%')
86. }
87. }
```

[MyCheckboxStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Modifier/entry/src/main/ets/pages/MyCheckboxStyle.ets#L16-L104)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/jNByBszITyiAWTkCObVRww/zh-cn_image_0000002552798378.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234004Z&HW-CC-Expire=86400&HW-CC-Sign=4E3610C98D3AC6654792D0F2D00A6ACDD3801BD2562B8014F642C979805CFC04)
