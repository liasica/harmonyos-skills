---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-composetitlebar
title: ComposeTitleBar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ComposeTitleBar
category: harmonyos-references
scraped_at: 2026-04-28T08:02:35+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c269918d445981e13336cfe3cf24959d2d75a29cfc1691ab33f78e03dbe6f76d
---

一种普通标题栏，支持设置标题、头像（可选）和副标题（可选），可用于一级页面、二级及其以上界面配置返回键。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果ComposeTitleBar设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到ComposeTitleBar本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ComposeTitleBar设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ComposeTitleBar } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## ComposeTitleBar

PhonePC/2in1TabletTVWearable

ComposeTitleBar({item?: ComposeTitleBarMenuItem, title: ResourceStr, subtitle?: ResourceStr, menuItems?: Array<ComposeTitleBarMenuItem>})

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | [ComposeTitleBarMenuItem](ohos-arkui-advanced-composetitlebar.md#composetitlebarmenuitem) | 否 | 用于左侧头像的单个菜单项目。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | 标题。 |
| subtitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 副标题。 |
| menuItems | Array<[ComposeTitleBarMenuItem](ohos-arkui-advanced-composetitlebar.md#composetitlebarmenuitem)> | 否 | 右侧菜单项目列表。 |

说明

入参对象不可为undefined，即ComposeTitleBar(undefined)。

## ComposeTitleBarMenuItem

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图标资源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol图标资源，优先级大于value，item左侧头像不支持设置该属性。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| label13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标标签描述。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| isEnabled | boolean | 否 | 是 | 是否启用，默认禁用。  isEnabled为true时，表示为启用。  isEnabled为false时，表示为禁用。  item属性不支持触发isEnabled属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 触发时的动作闭包，item属性不支持触发action事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 标题栏右侧自定义按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换'yes'。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：有label默认值为当前项label属性内容，没有设置label时，默认值为“ ”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值为“单指双击即可执行”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（简单的标题栏）

该示例实现了简单的标题栏，带有返回箭头的标题栏及带有右侧菜单项目列表的标题栏。

```
1. import { ComposeTitleBar, Prompt, ComposeTitleBarMenuItem } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 定义右侧菜单项目列表
7. private menuItems: Array<ComposeTitleBarMenuItem> = [
8. {
9. // 菜单图片资源
10. value: $r('sys.media.ohos_save_button_filled'),
11. // 启用图标
12. isEnabled: true,
13. // 点击菜单时触发事件
14. action: () => Prompt.showToast({ message: 'icon 1' }),
15. },
16. {
17. value: $r('sys.media.ohos_ic_public_copy'),
18. isEnabled: true,
19. action: () => Prompt.showToast({ message: 'icon 2' }),
20. },
21. {
22. value: $r('sys.media.ohos_ic_public_edit'),
23. isEnabled: true,
24. action: () => Prompt.showToast({ message: 'icon 3' }),
25. },
26. {
27. value: $r('sys.media.ohos_ic_public_remove'),
28. isEnabled: true,
29. action: () => Prompt.showToast({ message: 'icon 4' }),
30. },
31. ]

33. build() {
34. Row() {
35. Column() {
36. // 分割线
37. Divider().height(2).color(0xCCCCCC)
38. ComposeTitleBar({
39. title: '标题',
40. subtitle: '副标题',
41. menuItems: this.menuItems.slice(0, 1),
42. })
43. Divider().height(2).color(0xCCCCCC)
44. ComposeTitleBar({
45. title: '标题',
46. subtitle: '副标题',
47. menuItems: this.menuItems.slice(0, 2),
48. })
49. Divider().height(2).color(0xCCCCCC)
50. ComposeTitleBar({
51. title: '标题',
52. subtitle: '副标题',
53. menuItems: this.menuItems,
54. })
55. Divider().height(2).color(0xCCCCCC)
56. // 定义带头像的标题栏
57. ComposeTitleBar({
58. menuItems: [{
59. isEnabled: true, value: $r('sys.media.ohos_save_button_filled'),
60. action: () => Prompt.showToast({ message: 'icon' }),
61. }],
62. title: '标题',
63. subtitle: '副标题',
64. item: { isEnabled: true, value: $r('sys.media.ohos_app_icon') }
65. })
66. Divider().height(2).color(0xCCCCCC)
67. }
68. }.height('100%')
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/CcH4ZnOvQ4uR-QottP1Rmg/zh-cn_image_0000002552960100.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=39DCEABA2D73AC82F92AD3F848859BFB8E1F31894461EDEB7E03D5BEB188F60E)

### 示例2（右侧自定义按钮播报）

从API version 18开始，该示例通过设置标题栏右侧自定义按钮属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```
1. import { ComposeTitleBar, Prompt, ComposeTitleBarMenuItem } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 定义右侧菜单项目列表
7. private menuItems: Array<ComposeTitleBarMenuItem> = [
8. {
9. // 菜单图片资源
10. value: $r('sys.media.ohos_save_button_filled'),
11. // 启用图标
12. isEnabled: true,
13. // 点击菜单时触发事件
14. action: () => Prompt.showToast({ message: 'icon 1' }),
15. // 屏幕朗读播报文本，优先级比label高
16. accessibilityText: '保存',
17. // 屏幕朗读是否可以聚焦到
18. accessibilityLevel: 'yes',
19. // 屏幕朗读最后播报的描述文本
20. accessibilityDescription: '点击操作保存图标',
21. },
22. {
23. value: $r('sys.media.ohos_ic_public_copy'),
24. isEnabled: true,
25. action: () => Prompt.showToast({ message: 'icon 2' }),
26. accessibilityText: '复制',
27. // 此处为no，屏幕朗读不聚焦
28. accessibilityLevel: 'no',
29. accessibilityDescription: '点击操作复制图标',
30. },
31. {
32. value: $r('sys.media.ohos_ic_public_edit'),
33. isEnabled: true,
34. action: () => Prompt.showToast({ message: 'icon 3' }),
35. accessibilityText: '编辑',
36. accessibilityLevel: 'yes',
37. accessibilityDescription: '点击操作编辑图标',
38. },
39. {
40. value: $r('sys.media.ohos_ic_public_remove'),
41. isEnabled: true,
42. action: () => Prompt.showToast({ message: 'icon 4' }),
43. accessibilityText: '移除',
44. accessibilityLevel: 'yes',
45. accessibilityDescription: '点击操作移除图标',
46. },
47. ]

49. build() {
50. Row() {
51. Column() {
52. // 分割线
53. Divider().height(2).color(0xCCCCCC)
54. ComposeTitleBar({
55. title: '标题',
56. subtitle: '副标题',
57. menuItems: this.menuItems.slice(0, 1),
58. })
59. Divider().height(2).color(0xCCCCCC)
60. ComposeTitleBar({
61. title: '标题',
62. subtitle: '副标题',
63. menuItems: this.menuItems.slice(0, 2),
64. })
65. Divider().height(2).color(0xCCCCCC)
66. ComposeTitleBar({
67. title: '标题',
68. subtitle: '副标题',
69. menuItems: this.menuItems,
70. })
71. Divider().height(2).color(0xCCCCCC)
72. // 定义带头像的标题栏
73. ComposeTitleBar({
74. menuItems: [{
75. isEnabled: true, value: $r('sys.media.ohos_save_button_filled'),
76. action: () => Prompt.showToast({ message: 'icon' }),
77. }],
78. title: '标题',
79. subtitle: '副标题',
80. item: { isEnabled: true, value: $r('sys.media.ohos_app_icon') },
81. })
82. Divider().height(2).color(0xCCCCCC)
83. }
84. }.height('100%')
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/LYOu2MsKSJ-gVJO6CjDMKA/zh-cn_image_0000002583480101.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=0B99938F0213BCED9CF8D2E1A3795C83F97A67CC49006B8002ED1816FBB60762)

### 示例3（设置Symbol类型图标）

从API version 18开始，该示例通过设置ComposeTitleBarMenuItem的属性symbolStyle，展示了自定义Symbol类型图标。

```
1. import { ComposeTitleBar, Prompt, ComposeTitleBarMenuItem, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 定义右侧菜单项目列表
7. private menuItems: Array<ComposeTitleBarMenuItem> = [
8. {
9. // 菜单图片资源
10. value: $r('sys.symbol.house'),
11. // 菜单symbol图标
12. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor([Color.Red]),
13. // 启用图标
14. isEnabled: true,
15. // 点击菜单时触发事件
16. action: () => Prompt.showToast({ message: 'symbol icon 1' }),
17. },
18. {
19. value: $r('sys.symbol.house'),
20. isEnabled: true,
21. action: () => Prompt.showToast({ message: 'symbol icon 2' }),
22. },
23. {
24. value: $r('sys.symbol.car'),
25. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor([Color.Pink]),
26. isEnabled: true,
27. action: () => Prompt.showToast({ message: 'symbol icon 3' }),
28. },
29. {
30. value: $r('sys.symbol.car'),
31. isEnabled: true,
32. action: () => Prompt.showToast({ message: 'symbol icon 4' }),
33. },
34. ]

36. build() {
37. Row() {
38. Column() {
39. // 分割线
40. Divider().height(2).color(0xCCCCCC)
41. ComposeTitleBar({
42. title: '标题',
43. subtitle: '副标题',
44. menuItems: this.menuItems.slice(0, 1),
45. })
46. Divider().height(2).color(0xCCCCCC)
47. ComposeTitleBar({
48. title: '标题',
49. subtitle: '副标题',
50. menuItems: this.menuItems.slice(0, 2),
51. })
52. Divider().height(2).color(0xCCCCCC)
53. ComposeTitleBar({
54. title: '标题',
55. subtitle: '副标题',
56. menuItems: this.menuItems,
57. })
58. Divider().height(2).color(0xCCCCCC)
59. // 定义带头像的标题栏
60. ComposeTitleBar({
61. menuItems: [{
62. isEnabled: true, value: $r('sys.symbol.heart'),
63. action: () => Prompt.showToast({ message: 'symbol icon 1' }),
64. }],
65. title: '标题',
66. subtitle: '副标题',
67. item: { isEnabled: true, value: $r('sys.media.ohos_app_icon') },
68. })
69. Divider().height(2).color(0xCCCCCC)
70. }
71. }.height('100%')
72. }
73. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/nWx4jDkCQoCmOB75zdRhTg/zh-cn_image_0000002552800452.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=5BA9CB884EC5F35601B495874063AEB6DD652FCAF6E932CA1C8CBC6A4F5714D5)
