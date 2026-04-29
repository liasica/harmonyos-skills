---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-content-modifier
title: 自定义内容
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 自定义内容
category: harmonyos-references
scraped_at: 2026-04-29T13:51:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1f9fda69c943bdca3c975dfa2db50c4239719b9034e26fb029c0cef7515dc99c
---

支持通过样式builder自定义特定组件的内容区。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## ContentModifier<T>

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。

### applyContent

PhonePC/2in1TabletTVWearable

applyContent(): WrappedBuilder<[T]>

定制内容区的Builder。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WrappedBuilder<[T]>](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder) | 组件的属性类，用来区别不同组件自定义内容区后所需要的不同信息，比如Button组件的ButtonConfiguration，Checkbox组件的CheckBoxConfiguration等。 |

**T参数支持范围:**

ButtonConfiguration、CheckBoxConfiguration、DataPanelConfiguration、TextClockConfiguration、ToggleConfiguration、GaugeConfiguration、LoadingProgressConfiguration、RadioConfiguration、ProgressConfiguration、RatingConfiguration、SliderConfiguration

**属性支持范围:**

支持通用属性enabled，contentModifier。

## CommonConfiguration<T>

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 如果该值为true，则contentModifier可用，并且可以响应triggerChange等操作，如果设置为false，则不会响应triggerChange等操作。 |
| contentModifier | [ContentModifier<T>](ts-universal-attributes-content-modifier.md#contentmodifiert) | 否 | 否 | 用于将用户需要的组件信息发送到自定义内容区。 |

## 示例

PhonePC/2in1TabletTVWearable

通过ContentModifier实现自定义复选框样式的功能，用一个五边形复选框替换原本Checkbox的样式。如果选中，内部会出现红色三角图案，标题会显示选中字样；如果取消选中，红色三角图案消失，标题会显示非选中字样。

```
1. // xxx.ets
2. class MyCheckboxStyle implements ContentModifier<CheckBoxConfiguration> {
3. selectedColor: Color = Color.White;

5. constructor(selectedColor: Color) {
6. this.selectedColor = selectedColor;
7. }

9. applyContent(): WrappedBuilder<[CheckBoxConfiguration]> {
10. return wrapBuilder(buildCheckbox);
11. }
12. }

14. @Builder
15. function buildCheckbox(config: CheckBoxConfiguration) {
16. Column({ space: 10 }) {
17. Text(config.name + (config.selected ? "（选中）" : "（非选中）"))
18. Shape() {
19. // 五边形复选框样式
20. Path()
21. .width(200)
22. .height(60)
23. .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
24. .fillOpacity(0)
25. .strokeWidth(3)
26. // 红色三角图案样式
27. Path()
28. .width(10)
29. .height(10)
30. .commands('M50 0 L100 100 L0 100 Z')
31. .visibility(config.selected ? Visibility.Visible : Visibility.Hidden)
32. .fill(config.selected ? (config.contentModifier as MyCheckboxStyle).selectedColor : Color.Black)
33. .stroke((config.contentModifier as MyCheckboxStyle).selectedColor)
34. .margin({ left: 11, top: 10 })
35. }
36. .width(300)
37. .height(200)
38. .viewPort({
39. x: 0,
40. y: 0,
41. width: 310,
42. height: 310
43. })
44. .strokeLineJoin(LineJoinStyle.Miter)
45. .strokeMiterLimit(5)
46. .onClick(() => {
47. // 点击后，触发复选框点击状态变化
48. if (config.selected) {
49. config.triggerChange(false);
50. } else {
51. config.triggerChange(true);
52. }
53. })
54. .margin({ left: 150 })
55. }
56. }

58. @Entry
59. @Component
60. struct Index {
61. build() {
62. Row() {
63. Column() {
64. Checkbox({ name: '复选框状态', group: 'checkboxGroup' })
65. .select(true)
66. .contentModifier(new MyCheckboxStyle(Color.Red))
67. .onChange((value: boolean) => {
68. console.info('Checkbox change is' + value);
69. })
70. }
71. .width('100%')
72. }
73. .height('100%')
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/MG-HwNUTQImMIT_fkE4hsg/zh-cn_image_0000002558766100.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055130Z&HW-CC-Expire=86400&HW-CC-Sign=691E1FB014F4981D983DB00F33657A09647C5A4F6ED107F241EB4E9DBB8A5789)
