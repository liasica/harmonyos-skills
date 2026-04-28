---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style
title: 多态样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 多态样式
category: harmonyos-references
scraped_at: 2026-04-28T08:01:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a3b155501add8394d54d4edbf3eff7c09e260a32d34a55d5ea0150367338c52f
---

设置组件不同状态下的样式。

说明

* 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 从API version 11开始支持另一种写法[attributeModifier](ts-universal-attributes-attribute-modifier.md)，可根据开发者需要动态设置属性。
* 多态样式仅支持[通用属性](ts-component-general-attributes.md)。如果多态样式不生效，则该属性可能为组件的私有属性，例如：fontColor、[TextInput](ts-basic-components-textinput.md)组件的[backgroundColor](ts-universal-attributes-background.md#backgroundcolor18)等。此时，可以通过attributeModifier动态设置组件属性来解决此问题。
* 当前多态样式实现依赖于组件自定义节点的刷新机制。因Builder不具备独立的自定义父节点，无法直接触发刷新，致使多态样式无法直接在Builder中生效。解决方法是将多态样式封装至自定义组件内部，再将此组件置于@Builder中，以此来间接实现多态样式。示例代码可参考[示例3设置Builder多态样式](ts-universal-attributes-polymorphic-style.md#示例3设置builder多态样式)。
* 多态样式的焦点态只有在[焦点激活态](../harmonyos-guides/arkts-common-events-focus-event.md#基础概念)开启时生效。

## stateStyles

PhonePC/2in1TabletTVWearable

stateStyles(value: StateStyles): T

设置组件不同状态的样式。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [StateStyles](ts-universal-attributes-polymorphic-style.md#statestyles-1) | 是 | 设置组件不同状态的样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## StateStyles

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | any | 否 | 是 | 组件无状态时的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| pressed | any | 否 | 是 | 组件按下状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| disabled | any | 否 | 是 | 组件禁用状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| focused | any | 否 | 是 | 组件获焦状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| clicked | any | 否 | 是 | 组件点击状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| selected10+ | object | 否 | 是 | 组件选中状态的样式。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |

**selected选中状态说明**

* 当前多态样式的选中状态样式依赖组件选中属性值，可以使用[点击事件](ts-universal-events-click.md)修改属性值，或使用属性自带[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定功能。
* 当前支持selected的组件及其参数/属性值：

  | 组件 | 支持的参数/属性 | 起始API版本 |
  | --- | --- | --- |
  | [Checkbox](ts-basic-components-checkbox.md) | select | 10 |
  | [CheckboxGroup](ts-basic-components-checkboxgroup.md) | selectAll | 10 |
  | [Radio](ts-basic-components-radio.md) | checked | 10 |
  | [Toggle](ts-basic-components-toggle.md) | isOn | 10 |
  | [ListItem](ts-container-listitem.md) | selected | 10 |
  | [GridItem](ts-container-griditem.md) | selected | 10 |
  | [MenuItem](ts-basic-components-menuitem.md) | selected | 10 |

**pressed和clicked状态说明**

* 当clicked和pressed同时在一个组件上使用时，只有后注册的状态才能生效。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置Text多态样式）

该示例展示了状态为pressed和disabled时Text组件的样式变化。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StyleExample {
5. @State isEnable: boolean = true

7. @Styles
8. pressedStyles(): void {
9. .backgroundColor("#ED6F21")
10. .borderRadius(10)
11. .borderStyle(BorderStyle.Dashed)
12. .borderWidth(2)
13. .borderColor("#33000000")
14. .width(120)
15. .height(30)
16. .opacity(1)
17. }

19. @Styles
20. disabledStyles(): void {
21. .backgroundColor("#E5E5E5")
22. .borderRadius(10)
23. .borderStyle(BorderStyle.Solid)
24. .borderWidth(2)
25. .borderColor("#2a4c1919")
26. .width(90)
27. .height(25)
28. .opacity(1)
29. }

31. @Styles
32. normalStyles(): void {
33. .backgroundColor("#0A59F7")
34. .borderRadius(10)
35. .borderStyle(BorderStyle.Solid)
36. .borderWidth(2)
37. .borderColor("#33000000")
38. .width(100)
39. .height(25)
40. .opacity(1)
41. }

43. build() {
44. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
45. Text("normal")
46. .fontSize(14)
47. .fontColor(Color.White)
48. .opacity(0.5)
49. // stateStyles设置组件无状态时的样式
50. .stateStyles({
51. normal: this.normalStyles,
52. })
53. .margin({ bottom: 20 })
54. .textAlign(TextAlign.Center)
55. Text("pressed")
56. .backgroundColor("#0A59F7")
57. .borderRadius(20)
58. .borderStyle(BorderStyle.Dotted)
59. .borderWidth(2)
60. .borderColor(Color.Red)
61. .width(100)
62. .height(25)
63. .opacity(1)
64. .fontSize(14)
65. .fontColor(Color.White)
66. // stateStyles设置组件按下状态时的样式
67. .stateStyles({
68. pressed: this.pressedStyles,
69. })
70. .margin({ bottom: 20 })
71. .textAlign(TextAlign.Center)
72. Text(this.isEnable == true ? "effective" : "disabled")
73. .backgroundColor("#0A59F7")
74. .borderRadius(20)
75. .borderStyle(BorderStyle.Solid)
76. .borderWidth(2)
77. .borderColor(Color.Gray)
78. .width(100)
79. .height(25)
80. .opacity(1)
81. .fontSize(14)
82. .fontColor(Color.White)
83. .enabled(this.isEnable)
84. // stateStyles设置组件禁用状态时的样式
85. .stateStyles({
86. disabled: this.disabledStyles,
87. })
88. .textAlign(TextAlign.Center)
89. Text("control disabled")
90. .onClick(() => {
91. this.isEnable = !this.isEnable
92. console.info(`${this.isEnable}`)
93. })
94. }
95. .width(350).height(300)
96. }
97. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/-0-s1RW2Q4mo8lZJETcY4Q/zh-cn_image_0000002583439591.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=74AF230EF105B87766DDAF8C8A7C26084E0F8DDD21E8CA84764EFF776E6EA129)

### 示例2（设置Radio多态样式）

该示例展示了状态为selected时Radio组件的样式变化。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State value: boolean = false
6. @State value2: boolean = false

8. @Styles
9. normalStyles(): void{
10. .backgroundColor("#E5E5E1")
11. }

13. @Styles
14. selectStyles(): void{
15. .backgroundColor("#ED6F21")
16. .borderWidth(2)
17. }

19. build() {
20. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
21. Column() {
22. Text('Radio1')
23. .fontSize(25)
24. Radio({ value: 'Radio1', group: 'radioGroup1' })
25. .checked(this.value)
26. .height(50)
27. .width(50)
28. .borderWidth(0)
29. .borderRadius(30)
30. .onClick(() => {
31. this.value = !this.value
32. })
33. .stateStyles({
34. normal: this.normalStyles,
35. selected: this.selectStyles,
36. })
37. }
38. .margin(30)

40. Column() {
41. Text('Radio2')
42. .fontSize(25)
43. Radio({ value: 'Radio2', group: 'radioGroup2' })
44. .checked($$this.value2)
45. .height(50)
46. .width(50)
47. .borderWidth(0)
48. .borderRadius(30)
49. .stateStyles({
50. normal: this.normalStyles,
51. selected: this.selectStyles,
52. })
53. }
54. .margin(30)
55. }.padding({ top: 30 })
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/B1stT4vkTzq--rt8bVFblg/zh-cn_image_0000002552959546.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=E7F501F0C95754EA5BDE2402F01283F7F9E530ED9C18169ABAECFF4C35747B01)

### 示例3（设置Builder多态样式）

该示例展示了状态为pressed时Builder组件的样式变化。

```
1. import { ComponentContent } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Component
5. struct Child {
6. build() {
7. Row()
8. .zIndex(10)
9. .width(200)
10. .height(200)
11. .stateStyles({
12. normal: {
13. .backgroundColor(Color.Blue)
14. },
15. pressed: {
16. .backgroundColor(Color.Black)
17. }
18. })
19. }
20. }

22. @Builder
23. function buildText() {
24. Child()
25. }

27. @Entry
28. @Component
29. struct Index {
30. private contentNode: ComponentContent<Object> =
31. new ComponentContent(this.getUIContext(), wrapBuilder(buildText));

33. build() {
34. Column() {
35. Button().margin({ top: 200 }).onClick((event: ClickEvent) => {
36. this.getUIContext()
37. .getPromptAction()
38. .openCustomDialog(this.contentNode)
39. .then(() => {
40. console.info('OpenCustomDialog complete.')
41. })
42. .catch((error: BusinessError) => {
43. let message = (error as BusinessError).message;
44. let code = (error as BusinessError).code;
45. console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
46. })
47. })
48. }
49. .width('100%')
50. .height('100%')
51. }
52. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/QRxWAdZoTHu-AW4m0pkDXw/zh-cn_image_0000002583479547.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=E62C5904B0012B01502D4B0778ABAF00E1A850F9E2EDA55D529E863554AA75B7)
