---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-tabtitlebar
title: TabTitleBar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > TabTitleBar
category: harmonyos-references
scraped_at: 2026-04-28T08:02:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:06810423de1346461e687ebd179325ac104efebdf56dfb6f1995de3377260c7b
---

页签型标题栏，用于页面之间的切换。仅一级页面适用。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果TabTitleBar设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到TabTitleBar本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议TabTitleBar设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TabTitleBar } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## TabTitleBar

PhonePC/2in1TabletTVWearable

TabTitleBar({tabItems: Array<TabTitleBarTabItem>, menuItems?: Array<TabTitleBarMenuItem>, swiperContent: () => void})

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| tabItems | Array<[TabTitleBarTabItem](ohos-arkui-advanced-tabtitlebar.md#tabtitlebartabitem)> | 是 | - | 左侧页签项目列表，定义标题栏左侧的页签项目。 |
| menuItems | Array<[TabTitleBarMenuItem](ohos-arkui-advanced-tabtitlebar.md#tabtitlebarmenuitem)> | 否 | - | 右侧菜单项目列表，定义标题栏右侧的菜单项目。若不传，则不显示右侧菜单项。 |
| swiperContent | () => void | 是 | @BuilderParam | 页签列表关联的页面内容构造器。 |

说明

入参对象不可为undefined，即TabTitleBar(undefined)。

## TabTitleBarMenuItem

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图标资源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol图标资源，优先级大于value。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| label13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标标签描述。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| isEnabled | boolean | 否 | 是 | 是否启用。true：启用，false：禁用。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 触发时的动作闭包。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 标题栏右侧自定义按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换'yes'。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：有label默认值为当前项label属性内容，没有设置label时，默认值为“ ”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值为“单指双击即可执行”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## TabTitleBarTabItem

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 文字页签。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图片页签资源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol图片页签资源，优先级大于icon。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（简单的页签型标题栏）

该示例实现了带有左侧页签和右侧菜单列表的页签型标题栏。

```
1. import { TabTitleBar, Prompt, TabTitleBarTabItem, TabTitleBarMenuItem } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @Builder
7. // 定义页签列表关联的页面
8. componentBuilder() {
9. Text("#1ABC9C\nTURQUOISE")
10. .fontWeight(FontWeight.Bold)
11. .fontSize(14)
12. .width("100%")
13. .textAlign(TextAlign.Center)
14. .fontColor("#CCFFFFFF")
15. .backgroundColor("#1ABC9C")
16. Text("#16A085\nGREEN SEA")
17. .fontWeight(FontWeight.Bold)
18. .fontSize(14)
19. .width("100%")
20. .textAlign(TextAlign.Center)
21. .fontColor("#CCFFFFFF")
22. .backgroundColor("#16A085")
23. Text("#2ECC71\nEMERALD")
24. .fontWeight(FontWeight.Bold)
25. .fontSize(14)
26. .width("100%")
27. .textAlign(TextAlign.Center)
28. .fontColor("#CCFFFFFF")
29. .backgroundColor("#2ECC71")
30. Text("#27AE60\nNEPHRITIS")
31. .fontWeight(FontWeight.Bold)
32. .fontSize(14)
33. .width("100%")
34. .textAlign(TextAlign.Center)
35. .fontColor("#CCFFFFFF")
36. .backgroundColor("#27AE60")
37. Text("#3498DB\nPETER RIVER")
38. .fontWeight(FontWeight.Bold)
39. .fontSize(14)
40. .width("100%")
41. .textAlign(TextAlign.Center)
42. .fontColor("#CCFFFFFF")
43. .backgroundColor("#3498DB")
44. }

46. // 定义几个左侧的页签项目
47. private readonly tabItems: Array<TabTitleBarTabItem> =
48. [
49. { title: '页签1' },
50. { title: '页签2' },
51. { title: '页签3' },
52. { title: 'icon', icon: $r('sys.media.ohos_app_icon') },
53. { title: '页签4' },
54. ]
55. // 定义几个右侧的菜单项目
56. private readonly menuItems: Array<TabTitleBarMenuItem> = [
57. {
58. value: $r('sys.media.ohos_save_button_filled'),
59. isEnabled: true,
60. action: () => Prompt.showToast({ message: "on item click! index 0" })
61. },
62. {
63. value: $r('sys.media.ohos_ic_public_copy'),
64. isEnabled: true,
65. action: () => Prompt.showToast({ message: "on item click! index 1" })
66. },
67. {
68. value: $r('sys.media.ohos_ic_public_edit'),
69. isEnabled: true,
70. action: () => Prompt.showToast({ message: "on item click! index 2" })
71. },
72. ]

74. // TabTitleBar效果展示
75. build() {
76. Row() {
77. Column() {
78. TabTitleBar({
79. swiperContent: this.componentBuilder,
80. tabItems: this.tabItems,
81. menuItems: this.menuItems,
82. })
83. }.width('100%')
84. }.height('100%')
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/WrcaL-BoSGyz1APGGi6wwg/zh-cn_image_0000002552960136.png?HW-CC-KV=V1&HW-CC-Date=20260428T000240Z&HW-CC-Expire=86400&HW-CC-Sign=1DDF0D686C653AFB5B6F55A45297CC213DFB171D417AF0FD61759032D0D55A35)

### 示例2（右侧自定义按钮播报）

从API version 18开始，该示例通过设置标题栏右侧自定义按钮属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```
1. import { TabTitleBar, Prompt, TabTitleBarTabItem, TabTitleBarMenuItem } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @Builder
7. // 定义页签列表关联的页面
8. componentBuilder() {
9. Text("#1ABC9C\nTURQUOISE")
10. .fontWeight(FontWeight.Bold)
11. .fontSize(14)
12. .width("100%")
13. .textAlign(TextAlign.Center)
14. .fontColor("#CCFFFFFF")
15. .backgroundColor("#1ABC9C")
16. Text("#16A085\nGREEN SEA")
17. .fontWeight(FontWeight.Bold)
18. .fontSize(14)
19. .width("100%")
20. .textAlign(TextAlign.Center)
21. .fontColor("#CCFFFFFF")
22. .backgroundColor("#16A085")
23. Text("#2ECC71\nEMERALD")
24. .fontWeight(FontWeight.Bold)
25. .fontSize(14)
26. .width("100%")
27. .textAlign(TextAlign.Center)
28. .fontColor("#CCFFFFFF")
29. .backgroundColor("#2ECC71")
30. Text("#27AE60\nNEPHRITIS")
31. .fontWeight(FontWeight.Bold)
32. .fontSize(14)
33. .width("100%")
34. .textAlign(TextAlign.Center)
35. .fontColor("#CCFFFFFF")
36. .backgroundColor("#27AE60")
37. Text("#3498DB\nPETER RIVER")
38. .fontWeight(FontWeight.Bold)
39. .fontSize(14)
40. .width("100%")
41. .textAlign(TextAlign.Center)
42. .fontColor("#CCFFFFFF")
43. .backgroundColor("#3498DB")
44. }

46. // 定义几个左侧的页签项目
47. private readonly tabItems: Array<TabTitleBarTabItem> =
48. [
49. { title: '页签1' },
50. { title: '页签2' },
51. { title: '页签3' },
52. { title: 'icon', icon: $r('sys.media.ohos_app_icon') },
53. { title: '页签4' },
54. ]
55. // 定义几个右侧的菜单项目
56. private readonly menuItems: Array<TabTitleBarMenuItem> = [
57. {
58. value: $r('sys.media.ohos_save_button_filled'),
59. isEnabled: true,
60. action: () => Prompt.showToast({ message: "on item click! index 0" }),
61. accessibilityText: '保存',
62. // 此处为no，屏幕朗读不聚焦
63. accessibilityLevel: 'no',
64. accessibilityDescription: '点击操作保存图标'
65. },
66. {
67. value: $r('sys.media.ohos_ic_public_copy'),
68. isEnabled: true,
69. action: () => Prompt.showToast({ message: "on item click! index 1" }),
70. accessibilityText: '复制',
71. accessibilityLevel: 'yes',
72. accessibilityDescription: '点击操作复制图标'
73. },
74. {
75. value: $r('sys.media.ohos_ic_public_edit'),
76. isEnabled: true,
77. action: () => Prompt.showToast({ message: "on item click! index 2" }),
78. // 屏幕朗读播报文本，优先级比label高
79. accessibilityText: '编辑',
80. // 屏幕朗读是否可以聚焦到
81. accessibilityLevel: 'yes',
82. // 屏幕朗读最后播报的描述文本
83. accessibilityDescription: '点击操作编辑图标'
84. },
85. ]

87. // TabTitleBar效果展示
88. build() {
89. Row() {
90. Column() {
91. TabTitleBar({
92. swiperContent: this.componentBuilder,
93. tabItems: this.tabItems,
94. menuItems: this.menuItems,
95. })
96. }.width('100%')
97. }.height('100%')
98. }
99. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/1uzsh8pJTpa9A_w6iQrq2w/zh-cn_image_0000002583480137.png?HW-CC-KV=V1&HW-CC-Date=20260428T000240Z&HW-CC-Expire=86400&HW-CC-Sign=FC16C9E41721339CDB75F0ECD052239D385E5207FD02A10A33C78324132D6C79)

### 示例3（设置Symbol类型图标）

从API version 18开始，该示例通过设置TabTitleBarTabItem、TabTitleBarMenuItem的属性symbolStyle，展示了自定义Symbol类型图标。

```
1. import { TabTitleBar, Prompt, TabTitleBarTabItem, TabTitleBarMenuItem, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @Builder
7. // 定义页签列表关联的页面
8. componentBuilder() {
9. Text("#1ABC9C\nTURQUOISE")
10. .fontWeight(FontWeight.Bold)
11. .fontSize(14)
12. .width("100%")
13. .textAlign(TextAlign.Center)
14. .fontColor("#CCFFFFFF")
15. .backgroundColor("#1ABC9C")
16. Text("#16A085\nGREEN SEA")
17. .fontWeight(FontWeight.Bold)
18. .fontSize(14)
19. .width("100%")
20. .textAlign(TextAlign.Center)
21. .fontColor("#CCFFFFFF")
22. .backgroundColor("#16A085")
23. Text("#2ECC71\nEMERALD")
24. .fontWeight(FontWeight.Bold)
25. .fontSize(14)
26. .width("100%")
27. .textAlign(TextAlign.Center)
28. .fontColor("#CCFFFFFF")
29. .backgroundColor("#2ECC71")
30. Text("#27AE60\nNEPHRITIS")
31. .fontWeight(FontWeight.Bold)
32. .fontSize(14)
33. .width("100%")
34. .textAlign(TextAlign.Center)
35. .fontColor("#CCFFFFFF")
36. .backgroundColor("#27AE60")
37. Text("#3498DB\nPETER RIVER")
38. .fontWeight(FontWeight.Bold)
39. .fontSize(14)
40. .width("100%")
41. .textAlign(TextAlign.Center)
42. .fontColor("#CCFFFFFF")
43. .backgroundColor("#3498DB")
44. }

46. // 定义几个左侧的页签项目
47. private readonly tabItems: Array<TabTitleBarTabItem> =
48. [
49. { title: '页签1' },
50. { title: '页签2' },
51. { title: '页签3' },
52. {
53. title: 'icon',
54. icon: $r('sys.media.ohos_app_icon'),
55. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.car'))
56. },
57. { title: '页签4' },
58. ]
59. // 定义几个右侧的菜单项目
60. private readonly menuItems: Array<TabTitleBarMenuItem> = [
61. {
62. value: $r('sys.media.ohos_save_button_filled'),
63. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.save')),
64. isEnabled: true,
65. action: () => Prompt.showToast({ message: "on item click! index 0" }),
66. accessibilityText: '保存',
67. // 此处为no，屏幕朗读不聚焦
68. accessibilityLevel: 'no',
69. accessibilityDescription: '点击操作保存图标'
70. },
71. {
72. value: $r('sys.media.ohos_ic_public_copy'),
73. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.car')),
74. isEnabled: true,
75. action: () => Prompt.showToast({ message: "on item click! index 1" }),
76. accessibilityText: '复制',
77. accessibilityLevel: 'yes',
78. accessibilityDescription: '点击操作复制图标'
79. },
80. {
81. value: $r('sys.media.ohos_ic_public_edit'),
82. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.ai_edit')),
83. isEnabled: true,
84. action: () => Prompt.showToast({ message: "on item click! index 2" }),
85. // 屏幕朗读播报文本，优先级比label高
86. accessibilityText: '编辑',
87. // 屏幕朗读是否可以聚焦到
88. accessibilityLevel: 'yes',
89. // 屏幕朗读最后播报的描述文本
90. accessibilityDescription: '点击操作编辑图标'
91. },
92. ]

94. // TabTitleBar效果展示
95. build() {
96. Row() {
97. Column() {
98. TabTitleBar({
99. swiperContent: this.componentBuilder,
100. tabItems: this.tabItems,
101. menuItems: this.menuItems,
102. })
103. }.width('100%')
104. }.height('100%')
105. }
106. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/r3O6mhuiS2yCcK3b4P55EQ/zh-cn_image_0000002552800488.png?HW-CC-KV=V1&HW-CC-Date=20260428T000240Z&HW-CC-Expire=86400&HW-CC-Sign=DC19EEAA9DB00DFCC48355CD14CB421E82E18DD5BF876A560CADE0B0830D98BF)
