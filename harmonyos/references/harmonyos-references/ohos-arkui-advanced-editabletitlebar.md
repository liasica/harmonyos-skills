---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-editabletitlebar
title: EditableTitleBar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > EditableTitleBar
category: harmonyos-references
scraped_at: 2026-04-28T08:02:35+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:fe8de6d26c3081999d61290c12e0d84c4e741cb64314a8a8f40425e0f8339c7d
---

编辑型标题栏，适用于多选界面或者内容的编辑界面，一般采取左叉右勾的形式。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果EditableTitleBar设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到EditableTitleBar本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议EditableTitleBar设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { EditableTitleBar } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## EditableTitleBar

PhonePC/2in1TabletTVWearable

EditableTitleBar({leftIconStyle: EditableLeftIconType, imageItem?: EditableTitleBarItem, title: ResourceStr, subtitle?: ResourceStr, menuItems?: Array<EditableTitleBarMenuItem>, isSaveIconRequired: boolean, onSave?: () => void, onCancel?: () =>void, options: EditableTitleBarOptions, contentMargin?: LocalizedMargin, leftIconDefaultFocus?: boolean, saveIconDefaultFocus?: boolean})

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| leftIconStyle | [EditableLeftIconType](ohos-arkui-advanced-editabletitlebar.md#editablelefticontype) | 是 | - | 左侧按钮类型。  默认值：EditableLeftIconType.Back，表示返回。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| imageItem12+ | [EditableTitleBarItem](ohos-arkui-advanced-editabletitlebar.md#editabletitlebaritem12) | 否 | - | 用于左侧头像的单个菜单项目。需要在标题栏左侧显示头像时传入此参数，不传入时取默认值，不显示头像。  默认值：undefined。  **说明：** 左侧头像不支持配置无障碍属性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | - | 标题。  默认值：''，表示标题内容为空。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| subtitle12+ | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 副标题。需要在标题下方显示补充说明信息时传入此参数，不传入时取默认值，不显示副标题。  默认值：''，表示副标题内容为空。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| menuItems | Array<[EditableTitleBarMenuItem](ohos-arkui-advanced-editabletitlebar.md#editabletitlebarmenuitem)> | 否 | - | 右侧菜单项目列表。需要在标题栏右侧显示自定义操作按钮时传入此参数，不传入时取默认值，不显示右侧菜单项目列表。  默认值：undefined。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isSaveIconRequired12+ | boolean | 是 | - | 是否需要右侧的保存按钮。  默认值：true，表示需要右侧的保存按钮。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onSave | () => void | 否 | - | 点击保存时的事件。需要自定义保存操作逻辑时传入此参数，缺省时点击按钮无响应。  默认值：() => void。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onCancel | () => void | 否 | - | 当左侧按钮类型为 Cancel，触发取消时的事件。需要自定义返回/取消操作逻辑时传入此参数，缺省时点击左侧按钮无响应。  默认值：() => void。  从API version 12开始，当左侧按钮类型为 Back，触发返回时的事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| options12+ | [EditableTitleBarOptions](ohos-arkui-advanced-editabletitlebar.md#editabletitlebaroptions12) | 是 | - | 标题样式。  默认值：  {  safeAreaTypes: [SafeAreaType.SYSTEM],  safeAreaEdges: [SafeAreaEdge.TOP],  backgroundColor: '#00000000'  }。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| contentMargin12+ | [LocalizedMargin](ts-types.md#localizedmargin12) | 否 | @Prop | 标题栏外边距，不支持设置负数。  默认值：  {start: LengthMetrics.resource($r('sys.float.margin\_left')), end: LengthMetrics.resource($r('sys.float.margin\_right'))}。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| leftIconDefaultFocus18+ | boolean | 否 | - | 左侧图标是否为默认焦点。  默认值：false，表示不是默认焦点。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| saveIconDefaultFocus18+ | boolean | 否 | - | 保存图标是否为默认焦点。  默认值：false，表示不是默认焦点。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

说明

入参对象不可为undefined，即EditableTitleBar(undefined)。

若同时有多个可操作区域设置值默认焦点，则设置过默认焦点的可操作区域中显示顺序的第一个为默认焦点。

## EditableLeftIconType

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Back | 0 | 返回按钮。 |
| Cancel | 1 | 取消按钮。 |

## EditableTitleBarMenuItem

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图标资源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol图标资源，优先级大于value。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| label12+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标标签描述。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isEnabled | boolean | 否 | 是 | 是否启用，默认启用。  isEnabled为true时，表示为启用。  isEnabled为false时，表示为禁用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 标题栏右侧自定义按钮点击事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 标题栏右侧自定义按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：有label默认值为当前项label属性内容，没有设置label时，默认值为“ ”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题栏右侧自定义按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值为“单指双击即可执行”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| defaultFocus18+ | boolean | 否 | 是 | 是否设置为默认获焦。  true: 获焦  false: 不获焦  默认值：false  使用defaultFocus属性时，需提前将isEnabled属性设置为true，否则defaultFocus值会被识别为false。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## EditableTitleBarItem12+

PhonePC/2in1TabletTVWearable

type EditableTitleBarItem = EditableTitleBarMenuItem

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [EditableTitleBarMenuItem](ohos-arkui-advanced-editabletitlebar.md#editabletitlebarmenuitem) | 左侧头像的单个菜单类型。 |

## EditableTitleBarOptions12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 标题栏背景色。  默认值: '#00000000' |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 标题栏背景模糊样式。  默认值: BlurStyle.NONE |
| safeAreaTypes | Array <[SafeAreaType](ts-universal-attributes-expand-safe-area.md#safeareatype)> | 否 | 是 | 非必填，配置扩展安全区域的类型。  默认值: [SafeAreaType.SYSTEM] |
| safeAreaEdges | Array <[SafeAreaEdge](ts-universal-attributes-expand-safe-area.md#safeareaedge)> | 否 | 是 | 非必填，配置扩展安全区域的方向。  默认值: [SafeAreaEdge.TOP] |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（右侧图标自定义标题栏）

该示例主要演示EditableTitleBar设置左侧图标、主标题及自定义右侧图标区的效果。

```
1. import { EditableLeftIconType, EditableTitleBar, Prompt } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. Column() {
9. Divider().height(2).color(0xCCCCCC)
10. // 左侧取消按钮，右侧保存按钮。
11. EditableTitleBar({
12. leftIconStyle: EditableLeftIconType.Cancel,
13. title: '编辑页面',
14. menuItems: [],
15. onCancel: () => {
16. Prompt.showToast({ message: 'on cancel' });
17. },
18. onSave: () => {
19. Prompt.showToast({ message: 'on save' });
20. }
21. })
22. Divider().height(2).color(0xCCCCCC)
23. // 左侧返回按钮，右侧自定义取消按钮（disabled）、保存按钮。
24. EditableTitleBar({
25. leftIconStyle: EditableLeftIconType.Back,
26. title: '编辑页面',
27. menuItems: [
28. {
29. value: $r('sys.media.ohos_ic_public_cancel'),
30. isEnabled: false,
31. action: () => {
32. Prompt.showToast({ message: 'show toast index 2' });
33. }
34. }
35. ],
36. onSave: () => {
37. Prompt.showToast({ message: 'on save' })
38. }
39. })
40. Divider().height(2).color(0xCCCCCC)
41. }.width('100%')
42. }.height('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/lCv5RosXRVKx3f0iWxGB1w/zh-cn_image_0000002552960104.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=9175139E6D304BE0C6605C24915CE3D279EF79CDEB3D008F7DE96D97A693E0D7)

### 示例2（头像与背景模糊标题栏）

该示例主要演示EditableTitleBar设置背景模糊、头像；取消右侧保存图标及自定义标题栏外边距的效果。

```
1. import { EditableLeftIconType, EditableTitleBar, LengthMetrics, Prompt } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State titleBarMargin: LocalizedMargin = {
7. start: LengthMetrics.vp(35),
8. end: LengthMetrics.vp(35),
9. };

11. build() {
12. Row() {
13. Column() {
14. EditableTitleBar({
15. leftIconStyle: EditableLeftIconType.Cancel,
16. title: '主标题',
17. subtitle: '副标题',
18. // 设置背景模糊效果
19. options: {
20. backgroundBlurStyle: BlurStyle.COMPONENT_THICK,
21. },
22. onSave: () => {
23. Prompt.showToast({ message: "on save" });
24. },
25. })
26. Divider().height(2).color(0xCCCCCC);
27. EditableTitleBar({
28. leftIconStyle: EditableLeftIconType.Cancel,
29. title: '主标题',
30. subtitle: '副标题',
31. // 取消右侧保存按钮
32. isSaveIconRequired: false,
33. })
34. Divider().height(2).color(0xCCCCCC);
35. EditableTitleBar({
36. leftIconStyle: EditableLeftIconType.Back,
37. title: '主标题',
38. subtitle: '副标题',
39. isSaveIconRequired: false,
40. onCancel: () => {
41. this.getUIContext()?.getRouter()?.back();
42. },
43. })
44. Divider().height(2).color(0xCCCCCC);
45. EditableTitleBar({
46. leftIconStyle: EditableLeftIconType.Back,
47. title: '主标题',
48. subtitle: '副标题',
49. menuItems: [
50. {
51. value: $r('sys.media.ohos_ic_public_remove'),
52. isEnabled: true,
53. action: () => {
54. Prompt.showToast({ message: "show toast index 1" });
55. }
56. }
57. ],
58. isSaveIconRequired: false,
59. // 点击左侧Back图标，触发的动作。
60. onCancel: () => {
61. this.getUIContext()?.getRouter()?.back();
62. },
63. })
64. Divider().height(2).color(0xCCCCCC);
65. EditableTitleBar({
66. leftIconStyle: EditableLeftIconType.Back,
67. title: '主标题',
68. subtitle: '副标题',
69. // 设置可点击头像
70. imageItem: {
71. value: $r('sys.media.ohos_ic_normal_white_grid_image'),
72. isEnabled: true,
73. action: () => {
74. Prompt.showToast({ message: "show toast index 2" });
75. }
76. },
77. // 设置标题栏外边距
78. contentMargin: this.titleBarMargin,
79. // 右侧图标配置
80. menuItems: [
81. {
82. value: $r('sys.media.ohos_ic_public_remove'),
83. isEnabled: true,
84. action: () => {
85. Prompt.showToast({ message: "show toast index 3" });
86. }
87. }
88. ],
89. onCancel: () => {
90. this.getUIContext()?.getRouter()?.back();
91. },
92. })
93. }
94. }
95. }
96. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/P6Qpo2U-SkanSWOm3vwwxw/zh-cn_image_0000002583480105.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=AF518AA407AD4C4078A551FDA97AABEDFBC83FAC233A25BB1F45F1B6B1DE8528)

### 示例3（右侧自定义按钮播报）

从API version 18开始，该示例通过设置标题栏的右侧自定义按钮属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```
1. import { Prompt, EditableLeftIconType, EditableTitleBar } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index1 {
6. build() {
7. Row() {
8. Column() {
9. Divider().height(2).color(0xCCCCCC)
10. EditableTitleBar({
11. leftIconStyle: EditableLeftIconType.Cancel,
12. title: '编辑页面',
13. menuItems: [],
14. onCancel: () => {
15. Prompt.showToast({ message: 'on cancel' });
16. },
17. onSave: () => {
18. Prompt.showToast({ message: 'on save' });
19. }
20. })
21. Divider().height(2).color(0xCCCCCC)
22. EditableTitleBar({
23. // 头像、自定义按钮不可用
24. leftIconStyle: EditableLeftIconType.Back,
25. title: '主标题',
26. subtitle: '副标题',
27. imageItem: {
28. value: $r('sys.media.ohos_ic_normal_white_grid_image'),
29. isEnabled: true,
30. action: () => {
31. Prompt.showToast({ message: "show toast index 1" });
32. }
33. },
34. menuItems: [
35. {
36. value: $r('sys.media.ohos_ic_public_remove'),
37. label: '取消',
38. isEnabled: false,
39. accessibilityText: '删除',
40. accessibilityDescription: '点击即可删除',
41. action: () => {
42. Prompt.showToast({ message: "show toast index 2" });
43. }
44. }
45. ],
46. onCancel: () => {
47. this.getUIContext()?.getRouter()?.back();
48. },
49. })
50. Divider().height(2).color(0xCCCCCC)
51. }
52. }
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/9qasvt4jQnOYn-nmsayN7A/zh-cn_image_0000002552800456.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=624FFFEB75155FC595EFB231ED84BE795B52286C33881A1FAE70A4145F3C8959)

### 示例4（左侧图标设置为默认焦点）

在获焦状态下，该示例通过设置标题栏属性leftIconDefaultFocus使左侧图标默认获焦。

从API version 18开始，在[EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md#editabletitlebar-1)中新增leftIconDefaultFocus接口。

```
1. import { Prompt, EditableLeftIconType, EditableTitleBar } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column() {
8. EditableTitleBar({
9. leftIconStyle: EditableLeftIconType.Back,
10. leftIconDefaultFocus: true, // 设置左侧图标默认获焦。
11. title: '编辑页面',
12. menuItems: [],
13. onSave: () => {
14. Prompt.showToast({ message: 'on save' });
15. }
16. })
17. }
18. .height('100%')
19. .width('100%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/8z-xhxhRTk2Cvx75ueIFkg/zh-cn_image_0000002583440151.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=11B9ECCAFF795550CBEDB5386D3A9F53B04C7238D5336B6886F4BE8FA60DA64D)

### 示例5（右侧自定义图标设置为默认焦点）

从API version 18开始，该示例通过设置标题栏右侧图标属性defaultFocus使右侧图标默认获焦。

```
1. import { Prompt, EditableLeftIconType, EditableTitleBar } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column() {
8. EditableTitleBar({
9. leftIconStyle: EditableLeftIconType.Back,
10. title: '主标题',
11. subtitle: '副标题',
12. // 右侧图标配置
13. menuItems: [
14. {
15. value: $r('sys.media.ohos_ic_public_remove'),
16. isEnabled: true,
17. action: () => {
18. Prompt.showToast({ message: "show toast index 1" });
19. }
20. },
21. {
22. value: $r('sys.media.ohos_ic_public_remove'),
23. isEnabled: true,
24. defaultFocus: true,
25. action: () => {
26. Prompt.showToast({ message: "show toast index 2" });
27. }
28. }
29. ],
30. onCancel: () => {
31. this.getUIContext()?.getRouter()?.back();
32. },
33. })
34. }
35. .height('100%')
36. .width('100%')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/AdDNCrxlTiiCBzu4rDR-Pw/zh-cn_image_0000002552960106.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=F015C36179081516438C13AA6523BFCBBFEFF05E2C6AD53CC1651687A2B613E0)

### 示例6（设置Symbol类型图标）

从API version 18开始，该示例通过设置EditableTitleBarMenuItem的属性symbolStyle，展示了自定义Symbol类型图标。

```
1. import { EditableLeftIconType, EditableTitleBar, Prompt, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. Column() {
9. Divider().height(2).color(0xCCCCCC)
10. EditableTitleBar({
11. leftIconStyle: EditableLeftIconType.Cancel,
12. title: '主标题',
13. subtitle: '副标题',
14. menuItems: [
15. {
16. value: $r('sys.symbol.house'),
17. isEnabled: true,
18. action: () => {
19. Prompt.showToast({ message: 'show toast index 2' });
20. }
21. },
22. {
23. value: $r('sys.symbol.car'),
24. isEnabled: false,
25. }
26. ],
27. })
28. Divider().height(2).color(0xCCCCCC)
29. EditableTitleBar({
30. leftIconStyle: EditableLeftIconType.Back,
31. title: '主标题',
32. subtitle: '副标题',
33. imageItem: {
34. value: $r('sys.media.ohos_app_icon'),
35. isEnabled: true,
36. action: () => {
37. Prompt.showToast({ message: "show toast index 1" });
38. }
39. },
40. menuItems: [
41. {
42. value: $r('sys.symbol.house'),
43. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor([Color.Red]),
44. isEnabled: true,
45. action: () => {
46. Prompt.showToast({ message: 'show toast index 2' });
47. }
48. },
49. {
50. value: $r('sys.symbol.car'),
51. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor([Color.Blue]),
52. isEnabled: false,
53. }
54. ],
55. })
56. Divider().height(2).color(0xCCCCCC)
57. }.width('100%')
58. }.height('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/8s4VFGQZRWudvpLeeGYVlg/zh-cn_image_0000002583480107.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=54548FD0C273FC3C137DB00D597A5EC8829E6BBA09E9BB0D56B2981E5E153501)
