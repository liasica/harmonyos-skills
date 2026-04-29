---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selecttitlebar
title: SelectTitleBar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SelectTitleBar
category: harmonyos-references
scraped_at: 2026-04-29T13:53:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:314f0005ad7f935743f3072eb60fffd2af8e9b1a13412a55bd6009208c01307e
---

下拉菜单标题栏包含一个下拉菜单，可用于页面之间的切换；可用于一级页面、二级及其以上界面（配置返回键）。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果SelectTitleBar设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SelectTitleBar本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SelectTitleBar设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SelectTitleBar } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## SelectTitleBar

PhonePC/2in1TabletTVWearable

SelectTitleBar({selected: number, options: Array<SelectOption>, menuItems?: Array<SelectTitleBarMenuItem>, subtitle?: ResourceStr, badgeValue?: number, hidesBackButton?: boolean, onSelected?: ((index: number) => void)})

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| selected | number | 是 | @Prop | 当前选中项目的索引。  第一项的索引为0。如果不设置该属性，则默认值为0。 |
| options | Array<[SelectOption](ts-basic-components-select.md#selectoption对象说明)> | 是 | - | 下拉菜单中的项目。 |
| menuItems | Array<[SelectTitleBarMenuItem](ohos-arkui-advanced-selecttitlebar.md#selecttitlebarmenuitem)> | 否 | - | 右侧菜单项目列表，定义标题栏右侧的菜单项目。需要在标题栏右侧添加菜单项目列表时传入此参数，缺省时不显示右侧菜单区域。 |
| subtitle | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 子标题。用于显示补充信息，需要显示子标题时传入，缺省时不显示子标题区域。 |
| badgeValue | number | 否 | - | 新事件标记。  取值范围：[-2147483648,2147483647]，超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。  **说明：** 小于等于0时不显示信息标记。  最大消息数99，超过最大消息时仅显示99+。超大数值属于异常值，不显示信息标记。 |
| hidesBackButton | boolean | 否 | - | 是否隐藏左侧的返回箭头。  默认值：false。true：隐藏，false：显示。 |
| onSelected | ((index: number) => void) | 否 | - | 下拉菜单项目选中触发的回调函数，传入选中项的索引。下拉菜单选中后需要处理特定业务逻辑时时传入此参数，无特定业务逻辑时可缺省此参数。 |

说明

入参对象不可为undefined，即SelectTitleBar(undefined)。

## SelectTitleBarMenuItem

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图标资源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol图标资源，优先级大于value。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| label13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标标签描述。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| isEnabled | boolean | 否 | 是 | 是否启用。  默认值：false。true：启用，false：禁用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 触发时的动作闭包。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 标题栏右侧自定义按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换'yes'。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：有label默认值为当前项label属性内容，没有设置label时，默认值为“ ”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值为“单指双击即可执行”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（下拉菜单标题栏）

该示例实现了简单的下拉菜单标题栏，带有返回箭头的下拉菜单标题栏和带有右侧菜单项目列表的下拉菜单标题栏。

```
1. import { SelectTitleBar, Prompt, SelectTitleBarMenuItem } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 定义右侧菜单项目列表
7. private menuItems: Array<SelectTitleBarMenuItem> =
8. [
9. {
10. // 菜单图片资源
11. value: $r('sys.media.ohos_save_button_filled'),
12. // 启用图片
13. isEnabled: true,
14. // 点击菜单时触发事件
15. action: () => Prompt.showToast({ message: 'show toast index 1' }),
16. },
17. {
18. value: $r('sys.media.ohos_ic_public_copy'),
19. isEnabled: true,
20. action: () => Prompt.showToast({ message: 'show toast index 2' }),
21. },
22. {
23. value: $r('sys.media.ohos_ic_public_edit'),
24. isEnabled: true,
25. action: () => Prompt.showToast({ message: 'show toast index 3' }),
26. },
27. {
28. value: $r('sys.media.ohos_ic_public_remove'),
29. isEnabled: true,
30. action: () => Prompt.showToast({ message: 'show toast index 4' }),
31. },
32. ]

34. build() {
35. Row() {
36. Column() {
37. Divider().height(2).color(0xCCCCCC)
38. SelectTitleBar({
39. // 定义下拉列表选项
40. options: [
41. { value: '所有照片' },
42. { value: '本地（设备）' },
43. { value: '本地本地本地本地本地（储存卡）' }
44. ],
45. // 初始选择第一个下拉选项
46. selected: 0,
47. // 选中时触发函数
48. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
49. // 隐藏左侧返回箭头
50. hidesBackButton: true,
51. })
52. Divider().height(2).color(0xCCCCCC)
53. SelectTitleBar({
54. options: [
55. { value: '所有照片' },
56. { value: '本地（设备）' },
57. { value: '本地本地本地本地本地（储存卡）' },
58. ],
59. selected: 0,
60. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
61. hidesBackButton: false,
62. })
63. Divider().height(2).color(0xCCCCCC)
64. SelectTitleBar({
65. options: [
66. { value: '所有照片' },
67. { value: '本地（设备）' },
68. { value: '本地本地本地本地本地（储存卡）' },
69. ],
70. selected: 1,
71. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
72. subtitle: 'example@example.com',
73. })
74. Divider().height(2).color(0xCCCCCC)
75. SelectTitleBar({
76. options: [
77. { value: '所有照片' },
78. { value: '本地（设备）' },
79. { value: '本地本地本地本地本地（储存卡）' },
80. ],
81. selected: 1,
82. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
83. subtitle: 'example@example.com',
84. menuItems: [{ isEnabled: true, value: $r('sys.media.ohos_save_button_filled'),
85. action: () => Prompt.showToast({ message: 'show toast index 1' }),
86. }],
87. })
88. Divider().height(2).color(0xCCCCCC)
89. SelectTitleBar({
90. options: [
91. { value: '所有照片' },
92. { value: '本地（设备）' },
93. { value: '本地本地本地本地本地（储存卡）' },
94. ],
95. selected: 0,
96. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
97. subtitle: 'example@example.com',
98. menuItems: this.menuItems,
99. badgeValue: 99,
100. hidesBackButton: true,
101. })
102. Divider().height(2).color(0xCCCCCC)
103. }.width('100%')
104. }.height('100%')
105. }
106. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/zJ1M2jXIQQOIVz4cCuV09A/zh-cn_image_0000002589326519.png?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=FC44D607EB4210E70FE9AC471A0063309D71F912F57D08EA7DEF88E68EA82903)

### 示例2（右侧自定义按钮播报）

从API version 18开始，该示例通过设置标题栏右侧自定义按钮属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```
1. import { SelectTitleBar, Prompt, SelectTitleBarMenuItem } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 定义右侧菜单项目列表
7. private menuItems: Array<SelectTitleBarMenuItem> =
8. [
9. {
10. // 菜单图片资源
11. value: $r('sys.media.ohos_save_button_filled'),
12. // 启用图片
13. isEnabled: true,
14. // 点击菜单时触发事件
15. action: () => Prompt.showToast({ message: 'show toast index 1' }),
16. // 屏幕朗读播报文本，优先级比label高
17. accessibilityText: '保存',
18. // 屏幕朗读是否可以聚焦到
19. accessibilityLevel: 'yes',
20. // 屏幕朗读最后播报的描述文本
21. accessibilityDescription: '点击操作保存图标',
22. },
23. {
24. value: $r('sys.media.ohos_ic_public_copy'),
25. isEnabled: true,
26. action: () => Prompt.showToast({ message: 'show toast index 2' }),
27. accessibilityText: '复制',
28. // 此处为no，屏幕朗读不聚焦
29. accessibilityLevel: 'no',
30. accessibilityDescription: '点击操作复制图标',
31. },
32. {
33. value: $r('sys.media.ohos_ic_public_edit'),
34. isEnabled: true,
35. action: () => Prompt.showToast({ message: 'show toast index 3' }),
36. accessibilityText: '编辑',
37. accessibilityLevel: 'yes',
38. accessibilityDescription: '点击操作编辑图标',
39. },
40. {
41. value: $r('sys.media.ohos_ic_public_remove'),
42. isEnabled: true,
43. action: () => Prompt.showToast({ message: "show toast index 4" }),
44. accessibilityText: '移除',
45. accessibilityLevel: 'yes',
46. accessibilityDescription: '点击操作移除图标',
47. }
48. ]

50. build() {
51. Row() {
52. Column() {
53. Divider().height(2).color(0xCCCCCC)
54. SelectTitleBar({
55. // 定义下拉列表选项
56. options: [
57. { value: '所有照片' },
58. { value: '本地（设备）' },
59. { value: '本地本地本地本地本地（储存卡）' },
60. ],
61. // 初始选择第一个下拉选项
62. selected: 0,
63. // 选中时触发函数
64. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
65. // 隐藏左侧返回箭头
66. hidesBackButton: true,
67. })
68. Divider().height(2).color(0xCCCCCC)
69. SelectTitleBar({
70. options: [
71. { value: '所有照片' },
72. { value: '本地（设备）' },
73. { value: '本地本地本地本地本地（储存卡）' },
74. ],
75. selected: 0,
76. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
77. hidesBackButton: false,
78. })
79. Divider().height(2).color(0xCCCCCC)
80. SelectTitleBar({
81. options: [
82. { value: '所有照片' },
83. { value: '本地（设备）' },
84. { value: '本地本地本地本地本地（储存卡）' },
85. ],
86. selected: 1,
87. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
88. subtitle: 'example@example.com',
89. })
90. Divider().height(2).color(0xCCCCCC)
91. SelectTitleBar({
92. options: [
93. { value: '所有照片' },
94. { value: '本地（设备）' },
95. { value: '本地本地本地本地本地（储存卡）' },
96. ],
97. selected: 1,
98. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
99. subtitle: 'example@example.com',
100. menuItems: [{ isEnabled: true, value: $r('sys.media.ohos_save_button_filled'),
101. action: () => Prompt.showToast({ message: 'show toast index 1' }),
102. }],
103. })
104. Divider().height(2).color(0xCCCCCC)
105. SelectTitleBar({
106. options: [
107. { value: '所有照片' },
108. { value: '本地（设备）' },
109. { value: '本地本地本地本地本地（储存卡）' },
110. ],
111. selected: 0,
112. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
113. subtitle: 'example@example.com',
114. menuItems: this.menuItems,
115. badgeValue: 99,
116. hidesBackButton: true,
117. })
118. Divider().height(2).color(0xCCCCCC)
119. }.width('100%')
120. }.height('100%')
121. }
122. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/ZGh1fP9OQ4urTuXFNFMfug/zh-cn_image_0000002589246461.png?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=A754FF0516A45A7B39916C118A09B20545638B811C19BB1F1FE50F48F45B6EF8)

### 示例3（设置Symbol类型图标）

从API version 18开始，该示例通过设置SelectTitleBarMenuItem的属性symbolStyle，展示了自定义Symbol类型图标。

```
1. import { SelectTitleBar, Prompt, SelectTitleBarMenuItem, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 定义右侧菜单项目列表
7. private menuItems: Array<SelectTitleBarMenuItem> =
8. [
9. {
10. // 菜单图片资源
11. value: $r('sys.media.ohos_save_button_filled'),
12. // 菜单图片symbol资源
13. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.save')),
14. // 启用图片
15. isEnabled: true,
16. // 点击菜单时触发事件
17. action: () => Prompt.showToast({ message: 'show toast index 1' }),
18. // 屏幕朗读播报文本，优先级比label高
19. accessibilityText: '保存',
20. // 屏幕朗读是否可以聚焦到
21. accessibilityLevel: 'yes',
22. // 屏幕朗读最后播报的描述文本
23. accessibilityDescription: '点击操作保存图标',
24. },
25. {
26. value: $r('sys.media.ohos_ic_public_copy'),
27. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.car')),
28. isEnabled: true,
29. action: () => Prompt.showToast({ message: 'show toast index 2' }),
30. accessibilityText: '复制',
31. // 此处为no，屏幕朗读不聚焦
32. accessibilityLevel: 'no',
33. accessibilityDescription: '点击操作复制图标',
34. },
35. {
36. value: $r('sys.media.ohos_ic_public_edit'),
37. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.ai_edit')),
38. isEnabled: true,
39. action: () => Prompt.showToast({ message: 'show toast index 3' }),
40. accessibilityText: '编辑',
41. accessibilityLevel: 'yes',
42. accessibilityDescription: '点击操作编辑图标',
43. },
44. {
45. value: $r('sys.media.ohos_ic_public_remove'),
46. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.remove_songlist')),
47. isEnabled: true,
48. action: () => Prompt.showToast({ message: "show toast index 4" }),
49. accessibilityText: '移除',
50. accessibilityLevel: 'yes',
51. accessibilityDescription: '点击操作移除图标',
52. }
53. ]

55. build() {
56. Row() {
57. Column() {
58. Divider().height(2).color(0xCCCCCC)
59. SelectTitleBar({
60. // 定义下拉列表选项
61. options: [
62. { value: '所有照片' },
63. { value: '本地（设备）' },
64. { value: '本地本地本地本地本地（储存卡）' },
65. ],
66. // 初始选择第一个下拉选项
67. selected: 0,
68. // 选中时触发函数
69. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
70. // 隐藏左侧返回箭头
71. hidesBackButton: true,
72. })
73. Divider().height(2).color(0xCCCCCC)
74. SelectTitleBar({
75. options: [
76. { value: '所有照片' },
77. { value: '本地（设备）' },
78. { value: '本地本地本地本地本地（储存卡）' },
79. ],
80. selected: 0,
81. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
82. hidesBackButton: false,
83. })
84. Divider().height(2).color(0xCCCCCC)
85. SelectTitleBar({
86. options: [
87. { value: '所有照片' },
88. { value: '本地（设备）' },
89. { value: '本地本地本地本地本地（储存卡）' },
90. ],
91. selected: 1,
92. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
93. subtitle: 'example@example.com',
94. })
95. Divider().height(2).color(0xCCCCCC)
96. SelectTitleBar({
97. options: [
98. { value: '所有照片' },
99. { value: '本地（设备）' },
100. { value: '本地本地本地本地本地（储存卡）' },
101. ],
102. selected: 1,
103. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
104. subtitle: 'example@example.com',
105. menuItems: [{
106. isEnabled: true, value: $r('sys.media.ohos_save_button_filled'),
107. action: () => Prompt.showToast({ message: 'show toast index 1' }),
108. }],
109. })
110. Divider().height(2).color(0xCCCCCC)
111. SelectTitleBar({
112. options: [
113. { value: '所有照片' },
114. { value: '本地（设备）' },
115. { value: '本地本地本地本地本地（储存卡）' },
116. ],
117. selected: 0,
118. onSelected: (index) => Prompt.showToast({ message: 'page index ' + index }),
119. subtitle: 'example@example.com',
120. menuItems: this.menuItems,
121. badgeValue: 99,
122. hidesBackButton: true,
123. })
124. Divider().height(2).color(0xCCCCCC)
125. }.width('100%')
126. }.height('100%')
127. }
128. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/3hqxOsWsT3-GnQ9bk7qt4A/zh-cn_image_0000002558766654.png?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=ECD7EDDEC9FF4B025367309F163BDCFB385FCE35AADDE67F6A84C18BFA4E4890)
