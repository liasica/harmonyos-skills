---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitem
title: HdsListItem
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > HdsListItem
category: harmonyos-references
scraped_at: 2026-04-28T08:06:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:375fd895123f5adb71bac5ffb52eb2cafb2d5a7023717fe3bb8146b688d07740
---

该组件可设置ListItem的横滑动效，可以承载HdsListItemCard组件。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { HdsListItem } from '@kit.UIDesignKit';
```

## 接口

PhonePC/2in1TabletTV

HdsListItem({customItemBuilder?: CustomBuilder, hdsListItemCard?: HdsListItemCardOptions, swipeActionOptions?: HdsSwipeActionOptions | SwipeActionOptions, listItemModifier?: ListItemModifier, menuStyle?: MenuStyle, menuBuilder?: CustomBuilder, isSelected?: boolean})

提供了一个列表组件。

**装饰器类型：** @Component

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**设备行为异常：** 该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：** 6.0.0(20)

| 参数名 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| customItemBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | @BuilderParam | 自定义列表卡片项内容。 |
| hdsListItemCard | [HdsListItemCardOptions](ui-design-hdslistitemcard.md#hdslistitemcardoptions) | 否 | - | 列表卡片项内容。 |
| swipeActionOptions | [HdsSwipeActionOptions](ui-design-hdslistitem.md#hdsswipeactionoptions) | [SwipeActionOptions](ts-container-listitem.md#swipeactionoptions9对象说明) | 否 | - | 动效横滑内容展示。  HdsSwipeActionOptions是HdsListItem封装后的横滑动效类型，SwipeActionOptions支持用户自定义使用ListItem的横滑动效类型。 |
| listItemModifier | [ListItemModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | - | ListItem属性样式修改器。  **起始版本：** 6.0.1(21) |
| menuStyle | [MenuStyle](ui-design-hdslistitem.md#menustyle) | 否 | @Prop | ListItem预览菜单样式。  **起始版本：** 6.1.0(23) |
| menuBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | @BuilderParam | 自定义弹出菜单内容。  **起始版本：** 6.1.0(23) |
| isSelected | boolean | 否 | @Prop | ListItem是否被选中。  true：被选中。  false：未选中。  默认值：false。  **起始版本：** 6.1.0(23) |

说明

1. 该接口中customItemBuilder优先级高于hdsListItemCard。当同时设置customItemBuilder和hdsListItemCard时，customItemBuilder生效。
2. 当设置了menuBuilder时，menuStyle生效。
3. 当在listItemModifier中设置了selectable为false时，不要配置isSelected为true。

## HdsSwipeActionOptions

PhonePC/2in1TabletTV

设置横滑按钮的样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icons | Array<[SwipeIconConfigurations](ui-design-hdslistitem.md#swipeiconconfigurations)> | 否 | 是 | 配置除删除按钮之外其他三个按钮样式。 |
| deleteIconOptions | [DeleteIconOptions](ui-design-hdslistitem.md#deleteiconoptions) | 否 | 是 | 配置删除按钮样式。 |
| fullDeleteOptions | [FullDeleteOptions](ui-design-hdslistitem.md#fulldeleteoptions) | 否 | 是 | 配置滑动距离超过划出组件大小后的行为。 |
| deleteTriggerType | [SwipeDeleteTriggerType](ui-design-hdslistitem.md#swipedeletetriggertype) | 否 | 是 | 配置横滑删除的触发类型。  默认值：SwipeDeleteTriggerType.NORMAL\_TRIGGER。  **起始版本：** 6.1.0(23) |
| onStateChange | [OnStateChangeCallback](ui-design-hdslistitem.md#onstatechangecallback) | 否 | 是 | 列表滑出状态变化回调。  **起始版本：** 6.1.0(23) |

## IconOptions

PhonePC/2in1TabletTV

设置图标的可用性和无障碍等属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enable | boolean | 否 | 是 | 图标是否被启用。  true：图标被启用。  false：图标被禁用。  默认值：true。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标的无障碍文本属性。  当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：""。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标的无障碍描述。  此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值：“单指双击即可执行”。 |
| accessibilityLevel | string | 否 | 是 | 图标的无障碍重要性，用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。 |
| accessibilityRole | [AccessibilityRoleType](ts-universal-attributes-accessibility.md#accessibilityroletype18枚举说明) | 否 | 是 | 图标的无障碍组件类型。  可以根据应用诉求，修改组件类型，用于控制无障碍模式下对组件的朗读方式和朗读内容。  默认值：AccessibilityRoleType.ROLE\_NONE。  **起始版本：** 6.1.0(23) |

## SwipeIconConfigurations

PhonePC/2in1TabletTV

设置除删除图标外的横滑图标样式和功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [SwipeIconType](ui-design-hdslistitem.md#swipeicontype) | 否 | 否 | 图标资源，可支持symbol或image类型。 |
| iconOptions | [IconOptions](ui-design-hdslistitem.md#iconoptions) | 否 | 是 | 图标的能力选项。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 图标背景色。 |
| onAction | [SwipeActionCallback](ui-design-hdslistitem.md#swipeactioncallback) | 否 | 是 | 点击回调。 |

## DeleteIconOptions

PhonePC/2in1TabletTV

设置删除图标属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 删除按钮图标背景色。 |
| iconColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 删除按钮图标颜色。 |
| iconOptions | [IconOptions](ui-design-hdslistitem.md#iconoptions) | 否 | 是 | 删除按钮图标的能力选项。 |
| onAction | [SwipeActionCallback](ui-design-hdslistitem.md#swipeactioncallback) | 否 | 是 | 点击回调。 |

## FullDeleteOptions

PhonePC/2in1TabletTV

设置整个列表项的横滑删除属性。

**需要权限：** ohos.permission.VIBRATE（当enableVibration为true时需要申请该权限。若不申请，不会报错，仅无法响应振动）

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isFullDelete | boolean | 否 | 是 | 横滑之后再次滑动是否删除整个列表项。  - true：横滑之后再次滑动删除该列表项。  - false：横滑之后再次滑动不删除该列表项。  默认值：false。 |
| onFullDeleteAction | [SwipeActionCallback](ui-design-hdslistitem.md#swipeactioncallback) | 否 | 是 | 列表项删除的回调。 |
| enableVibration | boolean | 否 | 是 | 横滑删除整个列表项时，是否启用振动。  - true：启用振动。  - false：不启用振动。  默认值：true。  **起始版本：** 6.1.0(23) |

## SwipeIconType

PhonePC/2in1TabletTV

type SwipeIconType = SymbolGlyphModifier | ImageOptions

横滑图标资源类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | symbol资源类型。 |
| [ImageOptions](ui-design-hdslistitemcard.md#accessibilitygroupoptions) | image资源类型。 |

## MenuStyle

PhonePC/2in1TabletTV

设置列表项的预览菜单样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| responseType | [ResponseType](ts-appendix-enums.md#responsetype8) | 否 | 是 | 预览菜单响应类型。 |
| menuOptions | [ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10) | 否 | 是 | 预览菜单选项信息。 |

## SwipeActionCallback

PhonePC/2in1TabletTV

type SwipeActionCallback = () => void

列表滑动事件触发的回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

## OnStateChangeCallback

PhonePC/2in1TabletTV

type OnStateChangeCallback = (state: SwipeActionState) => void

列表滑出状态变化触发的回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [SwipeActionState](ts-container-listitem.md#swipeactionstate11枚举说明) | 是 | 列表项滑动的状态。  - state为SwipeActionState.COLLAPSED时，表示收起状态，此时操作项处于隐藏状态。  - state为SwipeActionState.EXPANDED时，表示展开状态，此时操作项处于显示状态。  - state为SwipeActionState.ACTIONING时，表示长距离状态，当HdsListItem进入长距删除区后，删除HdsListItem的状态。 |

## SwipeDeleteTriggerType

PhonePC/2in1TabletTV

列表横滑删除触发类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL\_TRIGGER | 0 | 列表横滑删除触发类型：正常触发。  正常触发长横滑删除。  触发阈值：图标宽度+50%剩余list宽度。 |
| EASY\_TRIGGER | 1 | 列表横滑删除触发类型：容易触发。  触发删除需要的滑动距离更短，更容易触发长横滑删除。  触发阈值：90%图标宽度+30%剩余list宽度。 |
| NO\_TRIGGER | 2 | 列表横滑删除触发类型：无法触发。  不响应长横滑删除。 |

## 示例

PhonePC/2in1TabletTV

设置一个带横滑效果的列表：

```
1. import { promptAction, SymbolGlyphModifier, TextModifier } from '@kit.ArkUI';
2. import { HdsListItem } from '@kit.UIDesignKit';

4. @Entry
5. @Component
6. struct HdsListItemExample {
7. @State dataSource: LazyDataSource<Item> = new LazyDataSource();
8. @State dataArr: Array<Item> = [];
9. @State EndOffset: number = 0;
10. private scroller: Scroller = new Scroller();

12. build() {
13. Column() {
14. List({ space: 10, scroller: this.scroller }) {
15. LazyForEach(this.dataSource, (item: Item) => {
16. HdsListItem({
17. hdsListItemCard: {
18. textItem: {
19. primaryText: {
20. text: 'Primary Text',
21. modifier: new TextModifier().fontColor(Color.Orange).fontSize(16),
22. }
23. }
24. },
25. swipeActionOptions: {
26. icons: [
27. {
28. icon: new SymbolGlyphModifier($r('sys.symbol.share')).fontColor([Color.Red]).fontSize(16),
29. backgroundColor: Color.Green,
30. onAction: () => {
31. promptAction.openToast({ message: '点击share按钮', duration: 100 });
32. },
33. },
34. {
35. icon: new SymbolGlyphModifier($r('sys.symbol.plus_square_on_square')),
36. backgroundColor: Color.Orange,
37. onAction: () => {
38. promptAction.openToast({ message: '点击copy按钮', duration: 100 });
39. },
40. },
41. {
42. icon: new SymbolGlyphModifier($r('sys.symbol.plus_square_dashed_on_square'))
43. .symbolEffect(new BounceSymbolEffect(), true),
44. onAction: () => {
45. promptAction.openToast({ message: '点击paste按钮', duration: 100 });
46. },
47. },
48. ],
49. deleteIconOptions: {
50. backgroundColor: Color.Red, //  ---修改背景色
51. iconColor: Color.Gray, //  ---- 修改垃圾桶的颜色
52. onAction: () => {
53. promptAction.openToast({ message: '点击删除按钮', duration: 100 });
54. }, //   --点击回调
55. },
56. fullDeleteOptions: {
57. isFullDelete: true, // --- 划动距离超过划出组件大小后自动触发删除，默认是false
58. onFullDeleteAction: () => {
59. promptAction.openToast({ message: '触发自动删除', duration: 100 });
60. this.getUIContext()?.animateTo({
61. duration: 350,
62. }, () => {
63. this.dataSource.deleteItem(item)
64. });
65. }, //   -- 触发删除时的回调
66. },
67. }
68. })
69. }, (item: Item) => item.data)
70. }
71. .scrollBar(BarState.Off)
72. .onDidScroll((scrollOffset: number) => {
73. this.EndOffset = scrollOffset
74. })
75. .margin(10)
76. .width('100%')
77. .height('100%')
78. }
79. .backgroundColor('#0D182431')
80. .width('100%')
81. .height('100%')
82. }

84. aboutToAppear() {
85. for (let i = 0; i < 2; i++) {
86. this.dataSource.pushItem(new Item(i + ''));
87. this.dataArr.push(new Item(i + ''));
88. }
89. }
90. }

92. class Item {
93. constructor(data: string) {
94. this.data = data;
95. }

97. public data: string = '';
98. }

100. export class LazyDataSource<T> implements IDataSource {
101. private elements: T[];
102. private listeners: Set<DataChangeListener>;

104. constructor(elements: T[] = []) {
105. this.elements = elements;
106. this.listeners = new Set();
107. }

109. public totalCount(): number {
110. return this.elements.length;
111. }

113. public getData(index: number): T {
114. return this.elements[index];
115. }

117. public indexOf(item: T): number {
118. return this.elements.indexOf(item);
119. }

121. public pinItem(item: T, index: number): void {
122. this.elements.splice(index, 1);
123. this.elements.unshift(item);
124. this.listeners.forEach(listener => listener.onDataReloaded());
125. }

127. public pushItem(item: T) {
128. this.elements.push(item);
129. this.listeners.forEach(listener => listener.onDataAdd(this.elements.length - 1));
130. }

132. public deleteItem(item: T): void {
133. const index = this.elements.indexOf(item);
134. if (index < 0) {
135. return;
136. }
137. this.elements.splice(index, 1);
138. this.listeners.forEach(listener => listener.onDataDelete(index));
139. }

141. public deleteItemByIndex(index: number): void {
142. this.elements.splice(index, 1);
143. this.listeners.forEach(listener => listener.onDataDelete(index));
144. }

146. public registerDataChangeListener(listener: DataChangeListener): void {
147. this.listeners.add(listener);
148. }

150. public unregisterDataChangeListener(listener: DataChangeListener): void {
151. this.listeners.delete(listener);
152. }
153. }
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/KKsVaV2aRB63q63BGoj6VA/zh-cn_image_0000002583480531.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000641Z&HW-CC-Expire=86400&HW-CC-Sign=C5B5AA45CC6BFB4D0EF913D54FE2095B5859C6CE07BE43C3C943780D79B0FC3C)
