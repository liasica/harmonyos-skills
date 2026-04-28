---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/list-item-combination-scenarios
title: 列表项组合场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 列表项组合场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:36ba95c39b330e6b1e5724775adb23e8fe4d5b31a303fa450262dda4b55a33bd
---

## 设计场景

列表包含一系列相同宽度的列表项，列表项可能由显示文本和可操控组件组合而成。显示文本通常是对可操控组件的功能性描述，类似于可操控组件的标签，因此列表项中的显示文本和可操控组件适合作为一个整体进行聚焦和播报。应用可以在列表项上设置[accessibilityGroup](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitygroup)，并通过[accessibilityOptions](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)指定可操控组件，桥接可操控组件的无障碍状态和无障碍点击事件。

### accessibilityOptions说明

* [accessibilityPreferred](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定是否优先使用无障碍文本进行拼接。若accessibilityPreferred设置为true，则深度遍历每个子节点时优先选择该子节点的无障碍文本accessibilityText。若无障碍文本为空，则选择本身Text文本，最终将拼接完成的文本设置给accessibilityText与Text都为空的父节点。默认值为false，表示不启用此功能。
* [stateControllerRoleType](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定类型的子组件用于控制容器组件的状态播报。配置accessibilityGroup的容器组件进行无障碍聚合后，会将该特定类型的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本，避免需要对子组件单独进行聚焦。如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件作为控制组件。默认值为空，表示不指定任何子组件。
* [stateControllerId](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定唯一标识ID的子组件用于控制容器组件的状态播报。配置accessibilityGroup的容器组件进行无障碍聚合后，会将该ID对应的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本，避免需要对子组件单独进行聚焦。如果聚合组件内有多个相同ID的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。如果与stateControllerRoleType同时配置，则优先匹配ID一致的组件。默认值为空，表示不指定任何子组件。
* [actionControllerRoleType](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定类型的子组件用于控制容器组件的操作执行。配置accessibilityGroup的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定类型的子组件，避免需要对子组件单独进行聚焦。当前只支持无障碍点击操作。如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。默认值为空，表示不指定任何子组件。
* [actionControllerId](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定唯一标识ID的子组件用于控制容器组件的操作执行。配置accessibilityGroup的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该ID对应的子组件，避免需要对子组件单独进行聚焦。当前只支持无障碍点击操作。如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。如果与actionControllerRoleType同时配置，则优先匹配ID一致的组件。默认值为空，表示不指定任何子组件。

## 开发实例

如下示例将开关、单选框、复选框和标签文本组合为一个整体进行聚焦和播报：

```
1. @Entry
2. @Component
3. struct Rule_2_1_13 {
4. scroller: Scroller = new Scroller();
5. @State isToggleSwitch: boolean = false
6. @State isChecked: boolean = false
7. @State isSelected: boolean = false
8. build() {
9. Column() {
10. Scroll(this.scroller) {
11. Column({ space: 30 }) {
12. Column() {
13. Text("按ID接管, state和action接管, 一个 toggle, 样式为开关")
14. // 指定特定唯一标识ID为toggletest1的toggle子组件，样式为开关，桥接其无障碍状态和无障碍点击事件
15. Column() {
16. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
17. Text("是否开启功能")
18. Toggle({ type: ToggleType.Switch, isOn: true })
19. .selectedColor('#007DFF')
20. .switchPointColor('#FFFFFF')
21. .onChange((isOn: boolean) => {
22. console.info('Component status:' + isOn);
23. })
24. .id("toggletest1")
25. }
26. }.width('100%')
27. .accessibilityGroup(true, {
28. stateControllerId: "toggletest1",
29. actionControllerId: "toggletest1"
30. })
31. .border({ color: Color.Black, width: 2 }).padding(10)
32. }

34. Column() {
35. Text("按ID接管, state和action接管, 一个 toggle, 样式为按钮")
36. // 指定特定唯一标识ID为toggletest1的toggle子组件，样式为按钮，桥接其无障碍状态和无障碍点击事件
37. Column() {
38. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
39. Text("是否改变状态")
40. Toggle({ type: ToggleType.Button, isOn: true }) {
41. Text('status button').fontColor('#182431').fontSize(12)
42. }.width(106)
43. .selectedColor('rgba(0,125,255,0.20)')
44. .onChange((isOn: boolean) => {
45. console.info('Component status:' + isOn);
46. })
47. .id("toggletest1")
48. }
49. }.width('100%')
50. .accessibilityGroup(true, {
51. stateControllerId: "toggletest1",
52. actionControllerId: "toggletest1"
53. })
54. .border({ color: Color.Black, width: 2 }).padding(10)
55. }

57. Column() {
58. Text("按ID接管, state和action接管, 一个 toggle, 样式为单选框")
59. // 指定特定唯一标识ID为toggletest1的toggle子组件，样式为单选框，桥接其无障碍状态和无障碍点击事件
60. Column() {
61. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
62. Text("是否选中功能")
63. Toggle({ type: ToggleType.Checkbox, isOn: false })
64. .selectedColor('#007DFF')
65. .switchPointColor('#FFFFFF')
66. .onChange((isOn: boolean) => {
67. console.info('Component status:' + isOn);
68. })
69. .id("toggletest1")
70. }
71. }.width('100%')
72. .accessibilityGroup(true, {
73. stateControllerId: "toggletest1",
74. actionControllerId: "toggletest1"
75. })
76. .border({ color: Color.Black, width: 2 }).padding(10)
77. }

79. Column() {
80. Text("按ID接管, state和action接管, 一个 raido")
81. // 指定特定唯一标识ID为radiotest1的radio子组件，桥接其无障碍状态和无障碍点击事件
82. Column() {
83. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
84. Text("是否改变单选框")
85. Radio({
86. value: 'Radio2.1', group: 'radioGroup2',
87. indicatorType: RadioIndicatorType.TICK
88. })
89. .radioStyle({
90. checkedBackgroundColor: Color.Pink
91. })
92. .checked(false)
93. .height(20)
94. .width(20)
95. .onChange((isChecked: boolean) => {
96. console.info('Radio1 status is ' + isChecked);

98. })
99. .id("radiotest1")
100. }
101. }.width('100%')
102. .accessibilityGroup(true, {
103. stateControllerId: "radiotest1",
104. actionControllerId: "radiotest1"
105. })
106. .border({ color: Color.Black, width: 2 }).padding(10)

108. Radio({ value: 'Radio2.2', group: 'radioGroup2' })
109. .checked(false)
110. .radioStyle({
111. checkedBackgroundColor: Color.Pink
112. })
113. .height(20)
114. .width(20)
115. .onChange((isChecked: boolean) => {
116. console.info('Radio2 status is ' + isChecked);
117. })
118. }

120. Column() {
121. Text("按ID接管, state和action接管, 一个 CheckBox")
122. // 指定特定唯一标识ID为checkboxtest1的checkbox子组件，桥接其无障碍状态和无障碍点击事件
123. Column() {
124. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
125. Text("是否改变复选框")
126. Checkbox({ name: 'checkbox2', group: 'checkboxGroup2' })
127. .select(true)
128. .selectedColor(0xed6f21)
129. .shape(CheckBoxShape.CIRCLE)
130. .onChange((value: boolean) => {
131. console.info('Checkbox2 change is' + value);
132. })
133. .id("checkboxtest1")
134. }
135. }.width('100%')
136. .accessibilityGroup(true, {
137. stateControllerId: "checkboxtest1",
138. actionControllerId: "checkboxtest1"
139. })
140. .border({ color: Color.Black, width: 2 }).padding(10)
141. }
142. }
143. }
144. .scrollable(ScrollDirection.Vertical)
145. .scrollBar(BarState.On)
146. .friction(0.6)
147. .edgeEffect(EdgeEffect.None)
148. .width("100%")
149. }
150. .width("100%")
151. .height("100%")
152. }
153. }
```
