---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbar
title: ToolBar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ToolBar
category: harmonyos-references
scraped_at: 2026-04-29T13:53:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:63f3b287d476cbd6c208b4cdf749a19e7ad4e8f94d7c275fe32a9982cea92ca9
---

工具栏组件，用于展示针对当前界面内容的操作选项，在界面底部显示。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果ToolBar设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到ToolBar本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ToolBar设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SymbolGlyphModifier, DividerModifier, ToolBar, ToolBarOptions, ToolBarModifier, ItemState, LengthMetrics } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## ToolBar

PhonePC/2in1TabletTVWearable

ToolBar({toolBarList: ToolBarOptions, activateIndex?: number, controller: TabsController, dividerModifier?: DividerModifier, toolBarModifier?: ToolBarModifier})

工具栏组件，用于展示针对当前界面内容的操作选项，在界面底部显示。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| toolBarList | [ToolBarOptions](ohos-arkui-advanced-toolbar.md#toolbaroptions) | 是 | @ObjectLink | 工具栏列表。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| activateIndex | number | 否 | @Prop | 激活态的子项。  取值范围：大于等于-1。  默认值：-1，没有激活态的子项。若设置数值小于-1，按没有激活项处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| controller | [TabsController](ts-container-tabs.md#tabscontroller) | 是 | - | 工具栏控制器，不支持控制工具栏子项。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| dividerModifier13+ | [DividerModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | @Prop | 工具栏头部分割线属性，可设置分割线高度、颜色等。  默认值：系统默认值。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| toolBarModifier13+ | [ToolBarModifier](ohos-arkui-advanced-toolbar.md#toolbarmodifier13) | 否 | @Prop | 工具栏属性，可设置工具栏高度、背景色、内边距（仅在工具栏子项数量小于5时生效）、是否显示按压态。  默认值：  工具栏高度：56vp  背景色：ohos\_id\_toolbar\_bg  内边距：24vp  显示按压态。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

## ToolBarOptions

PhonePC/2in1TabletTVWearable

继承于 Array<[ToolBarOption](ohos-arkui-advanced-toolbar.md#toolbaroption)>。

**装饰器类型：**@Observed

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

## ToolBarOption

PhonePC/2in1TabletTVWearable

定义工具栏的列表内容和属性。

**装饰器类型：**@Observed

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 工具栏子项的文本。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 工具栏子项点击事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | [Resource](ts-types.md#resource) | 否 | 是 | 工具栏子项的图标。  默认不设置或者设置为undefined，图标不显示。  toolBarSymbolOptions有传入参数时，icon不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| state | [ItemState](ohos-arkui-advanced-toolbar.md#itemstate) | 否 | 是 | 工具栏子项的状态。  默认为ItemState.ENABLE。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| iconColor13+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 工具栏子项的图标填充颜色。  默认值为$r('sys.color.icon\_primary')。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| activatedIconColor13+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 工具栏子项激活态的图标填充颜色。  默认值为$r('sys.color.icon\_emphasize')。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| textColor13+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 工具栏子项的文本颜色。  默认值为$r('sys.color.font\_primary')。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| activatedTextColor13+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 工具栏子项激活态的文本颜色。  默认值为$r('sys.color.font\_emphasize')。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| toolBarSymbolOptions13+ | [ToolBarSymbolGlyphOptions](ohos-arkui-advanced-toolbar.md#toolbarsymbolglyphoptions13) | 否 | 是 | 工具栏子项的图标属性，symbol类型。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 工具栏子项的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值为当前项content属性内容。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 工具栏子项的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值为“单指双击即可执行”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 工具栏子项无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## ToolBarModifier13+

PhonePC/2in1TabletTVWearable

ToolBarModifier提供设置工具栏高度(height)、背景色(backgroundColor)、左右内边距（padding，仅在item小于5个时生效）、是否显示按压态（stateEffect）的方法。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

### backgroundColor13+

PhonePC/2in1TabletTVWearable

backgroundColor(backgroundColor: ResourceColor): ToolBarModifier

自定义绘制工具栏背景色的接口，若重载该方法则可进行工具栏背景色的自定义绘制。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 是 | 工具栏背景色。  默认背景色为$r('sys.color.ohos\_id\_color\_toolbar\_bg')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarModifier](ohos-arkui-advanced-toolbar.md#toolbarmodifier13) | 设置backgroundColor后的ToolBarModifier对象。 |

### padding13+

PhonePC/2in1TabletTVWearable

padding(padding: LengthMetrics): ToolBarModifier

自定义绘制工具栏左右内边距的接口，若重载该方法则可进行工具栏左右内边距的自定义绘制。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 工具栏左右内边距，仅在item小于5个时生效。  工具栏默认在item小于5个时padding为24vp，大于等于5个时为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarModifier](ohos-arkui-advanced-toolbar.md#toolbarmodifier13) | 设置padding后的ToolBarModifier对象。 |

### height13+

PhonePC/2in1TabletTVWearable

height(height: LengthMetrics): ToolBarModifier

自定义绘制工具栏高度的接口，若重载该方法则可进行工具栏高度的自定义绘制，此高度不包含分割线高度。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 工具栏高度。  工具栏高度默认为56vp（不包含分割线）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarModifier](ohos-arkui-advanced-toolbar.md#toolbarmodifier13) | 设置height后的ToolBarModifier对象。 |

### stateEffect13+

PhonePC/2in1TabletTVWearable

stateEffect(stateEffect: boolean): ToolBarModifier

设置是否显示按压态效果的接口。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateEffect | boolean | 是 | 工具栏是否显示按压态效果。  true为显示按压态效果，false为移除按压态效果，默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarModifier](ohos-arkui-advanced-toolbar.md#toolbarmodifier13) | 设置stateEffect后的ToolBarModifier对象。 |

## ItemState

PhonePC/2in1TabletTVWearable

定义工具栏子项的当前状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENABLE | 1 | 工具栏子项为正常可点击状态。 |
| DISABLE | 2 | 工具栏子项为不可点击状态。 |
| ACTIVATE | 3 | 工具栏子项为激活状态，可点击。 |

## ToolBarSymbolGlyphOptions13+

PhonePC/2in1TabletTVWearable

ToolBarSymbolGlyphOptions定义图标的属性。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 工具栏symbol图标普通态样式。  默认值：fontColor：$r('sys.color.icon\_primary')，fontSize：24vp。 |
| activated | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 工具栏symbol图标激活态样式。  默认值：fontColor：$r('sys.color.icon\_emphasize')，fontSize：24vp。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（工具栏不同状态的默认效果）

该示例展示了工具栏子项state属性分别设置ENABLE、DISABLE、ACTIVATE状态的不同显示效果。

```
1. import { ToolBar, ToolBarOptions, ItemState } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State toolbarList: ToolBarOptions = new ToolBarOptions();

8. aboutToAppear() {
9. this.toolbarList.push({
10. content: '剪贴我是超超超超超超超超超长样式',
11. icon: $r('sys.media.ohos_ic_public_share'),
12. action: () => {
13. },
14. })
15. this.toolbarList.push({
16. content: '拷贝',
17. icon: $r('sys.media.ohos_ic_public_copy'),
18. action: () => {
19. },
20. state: ItemState.DISABLE
21. })
22. this.toolbarList.push({
23. content: '粘贴',
24. icon: $r('sys.media.ohos_ic_public_paste'),
25. action: () => {
26. },
27. state: ItemState.ACTIVATE
28. })
29. this.toolbarList.push({
30. content: '全选',
31. icon: $r('sys.media.ohos_ic_public_select_all'),
32. action: () => {
33. },
34. })
35. this.toolbarList.push({
36. content: '分享',
37. icon: $r('sys.media.ohos_ic_public_share'),
38. action: () => {
39. },
40. })
41. this.toolbarList.push({
42. content: '分享',
43. icon: $r('sys.media.ohos_ic_public_share'),
44. action: () => {
45. },
46. })
47. }

49. build() {
50. Row() {
51. Stack() {
52. Column() {
53. ToolBar({
54. activateIndex: 2,
55. toolBarList: this.toolbarList,
56. })
57. }
58. }
59. .align(Alignment.Bottom)
60. .width('100%')
61. .height('100%')
62. }
63. }
64. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/j8iDQiCdQAiBIOdxyr9GsA/zh-cn_image_0000002558766664.png?HW-CC-KV=V1&HW-CC-Date=20260429T055305Z&HW-CC-Expire=86400&HW-CC-Sign=9ECF161846F524EB38665E953EAB363250AD91C52177F5109868A7A1EDE2D24D)

### 示例2（设置工具栏自定义样式）

从API version 13开始，该示例通过设置属性ToolBarModifier自定义工具栏高度、背景色、按压效果等样式。

```
1. import {
2. SymbolGlyphModifier,
3. DividerModifier,
4. ToolBar,
5. ToolBarOptions,
6. ToolBarModifier,
7. ItemState,
8. LengthMetrics,
9. } from '@kit.ArkUI';

11. @Entry
12. @Component
13. struct Index {
14. @State toolbarList: ToolBarOptions = new ToolBarOptions();
15. // 自定义工具栏样式
16. private toolBarModifier: ToolBarModifier =
17. new ToolBarModifier().height(LengthMetrics.vp(52)).backgroundColor(Color.Transparent).stateEffect(false);
18. @State dividerModifier: DividerModifier = new DividerModifier().height(0);

20. aboutToAppear() {
21. // 添加工具栏子项
22. this.toolbarList.push({
23. content: 'Long long long long long long long long text',
24. icon: $r('sys.media.ohos_ic_public_share'),
25. action: () => {
26. },
27. state: ItemState.ACTIVATE,
28. toolBarSymbolOptions: {
29. normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Green]), // 普通态symbol图标
30. activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]), // 激活态symbol图标
31. },
32. activatedTextColor: $r('sys.color.font_primary'),
33. })
34. this.toolbarList.push({
35. content: 'Copy',
36. icon: $r('sys.media.ohos_ic_public_copy'),
37. action: () => {
38. },
39. state: ItemState.DISABLE,
40. iconColor: '#ff18cb53',
41. activatedIconColor: '#ffec5d5d', // 激活态icon颜色
42. activatedTextColor: '#ffec5d5d', // 激活态文本颜色
43. })
44. this.toolbarList.push({
45. content: 'Paste',
46. icon: $r('sys.media.ohos_ic_public_paste'),
47. action: () => {
48. },
49. state: ItemState.ACTIVATE,
50. textColor: '#ff18cb53',
51. })
52. this.toolbarList.push({
53. content: 'All',
54. icon: $r('sys.media.ohos_ic_public_select_all'),
55. action: () => {
56. },
57. state: ItemState.ACTIVATE,
58. })
59. this.toolbarList.push({
60. content: '分享',
61. icon: $r('sys.media.ohos_ic_public_share'),
62. action: () => {
63. },
64. })
65. this.toolbarList.push({
66. content: '分享',
67. icon: $r('sys.media.ohos_ic_public_share'),
68. action: () => {
69. },
70. })
71. }

73. build() {
74. Row() {
75. Stack() {
76. Column() {
77. ToolBar({
78. toolBarModifier: this.toolBarModifier,
79. dividerModifier: this.dividerModifier,
80. activateIndex: 0,
81. toolBarList: this.toolbarList,
82. })
83. .height(52)
84. }
85. }
86. .align(Alignment.Bottom)
87. .width('100%')
88. .height('100%')
89. }
90. }
91. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/8H6TPwKxS7CJlyTubD-tMA/zh-cn_image_0000002558607004.png?HW-CC-KV=V1&HW-CC-Date=20260429T055305Z&HW-CC-Expire=86400&HW-CC-Sign=4C5CA7C5D54CB9680486F95276DB1D8979BCC6F4CA9D16565BABDDEF120B4813)

### 示例3（设置工具栏自定义播报）

从API version 18开始，该示例通过设置工具栏子项属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```
1. import { ToolBar, ToolBarOptions, ItemState } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State toolbarList: ToolBarOptions = new ToolBarOptions();

8. aboutToAppear() {
9. // 添加工具栏子项
10. this.toolbarList.push({
11. content: '剪贴我是超超超超超超超超超长样式',
12. icon: $r('sys.media.ohos_ic_public_share'),
13. action: () => {
14. },
15. accessibilityText: '剪贴', // 该项屏幕朗读播报文本为‘剪贴’
16. accessibilityDescription: '单指双击即可剪贴', // 该项屏幕朗读播报描述为'单指双击即可剪贴'
17. accessibilityLevel: 'yes' // 该项可被无障碍屏幕朗读聚焦
18. })
19. this.toolbarList.push({
20. content: '拷贝',
21. icon: $r('sys.media.ohos_ic_public_copy'),
22. action: () => {
23. },
24. state: ItemState.DISABLE,
25. accessibilityLevel: 'no' // 该项将无法被屏幕朗读服务所识别，屏幕朗读不可聚焦
26. })
27. this.toolbarList.push({
28. content: '粘贴',
29. icon: $r('sys.media.ohos_ic_public_paste'),
30. action: () => {
31. },
32. state: ItemState.ACTIVATE
33. })
34. this.toolbarList.push({
35. content: '全选',
36. icon: $r('sys.media.ohos_ic_public_select_all'),
37. action: () => {
38. },
39. })
40. this.toolbarList.push({
41. content: '分享',
42. icon: $r('sys.media.ohos_ic_public_share'),
43. action: () => {
44. },
45. })
46. this.toolbarList.push({
47. content: '分享',
48. icon: $r('sys.media.ohos_ic_public_share'),
49. action: () => {
50. },
51. })
52. }

54. build() {
55. Row() {
56. Stack() {
57. Column() {
58. ToolBar({
59. activateIndex: 2,
60. toolBarList: this.toolbarList,
61. })
62. }
63. }
64. .align(Alignment.Bottom)
65. .width('100%')
66. .height('100%')
67. }
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/N5OKb6gQT76GD4jW5aoPrg/zh-cn_image_0000002558766664.png?HW-CC-KV=V1&HW-CC-Date=20260429T055305Z&HW-CC-Expire=86400&HW-CC-Sign=01890BA5B69DE6EE2653DDE2D55C1AD9391BE2BF2881710C534E458CB25F2A4A)
