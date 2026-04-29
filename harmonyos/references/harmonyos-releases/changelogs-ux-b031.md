---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-b031
title: UX样式或效果的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta2引入的接口行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-29T13:24:12+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1dd5a5f663c6fe98409cd2e0b248d8e05e85f5624a0ee66c37f249f94440ab6f
---

## TextInput、TextArea 设置TextAlign.Center且显示PlaceHolder文字时，光标位置的变更

**变更原因**

UX规范变更

**变更影响**

变更前：TextAlign.Center，显示PlaceHolder文字时，光标在文字中间，输入文字后光标在末尾

变更后：TextAlign.Center，显示PlaceHolder文字时，光标在文字前面，输入文字后光标在末尾

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**适配指导**

光标显示效果变化，无需适配。

## bindSheet半模态组件横屏支持设置档位与高度

**变更原因**

手机横屏时，bindSheet支持开发者设置档位和高度

**变更影响**

API version 11及以前：bindSheet在手机横屏时不支持设置档位和高度，默认高度距离横屏窗口顶部8vp。

API version 12及以后：bindSheet在手机横屏时支持开发者设置档位和高度，最大高度距离横屏窗口顶部8vp。

**适配指导**

默认效果变更，需应用适配。横竖屏设置档位规则保持一致，参考detents属性的设置请查阅[半模态组件](../harmonyos-references-V5/ts-universal-attributes-sheet-transition-V5.md)文档进行适配。

## bindSheet支持嵌套滚动

**变更原因**

为满足应用诉求，半模态面板嵌套滚动组件，且在滚动组件上设置嵌套模式时，需要实现联动效果。

**变更影响**

此变更涉及应用适配。

单档位模式下半模态仅可设置一档高度。多档位模式下半模态可以设置三档高度，内容位于半模态面板顶部时，通过上下滑动可以自由切换档位。

API version 12之前，半模态面板嵌套滚动组件，且在滚动组件上设置嵌套模式时，无法实现联动。内容位于顶部，多档位时上下滑动无法切换档位，单档位时下滑无法关闭半模态。

API version 12及以后，半模态面板嵌套滚动组件，且在滚动组件上设置嵌套模式时，可以实现联动。内容位于顶部，多档位时上下滑动可以切换档位；单档位时下滑可以关闭半模态。

在滚动组件上设置嵌套的情况下：

| 多档位变更前 | 多档位变更后 |
| --- | --- |
| 无法通过上下滑动切换档位，在最低档下滑无法关闭半模态 | 可以通过上下滑动切换档位，在最低档下滑可以关闭半模态 |

| 单档位变更前 | 单档位变更后 |
| --- | --- |
| 无法通过下滑关闭半模态 | 可以通过下滑关闭半模态 |

**变更的接口/组件**

bindSheet组件

**适配指导**

需要开发者适配。例如，在半模态面板中嵌套List组件场景，@Builder内容可以参考如下示例。

```
1. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
2. @Builder
3. myBuilder() {
4. Column() {
5. List({ space: 20, initialIndex: 0 }) {
6. ForEach(this.arr, (item: number) => {
7. ListItem() {
8. Text('' + item)
9. .width('100%')
10. .height(100)
11. .fontSize(16)
12. .textAlign(TextAlign.Center)
13. .borderRadius(10)
14. .backgroundColor(0xFFFFFF)
15. }
16. }, (item: string) => item)
17. }
18. .listDirection(Axis.Vertical) // 排列方向
19. .edgeEffect(EdgeEffect.None)
20. .nestedScroll({
21. scrollForward: NestedScrollMode.PARENT_FIRST,
22. scrollBackward: NestedScrollMode.SELF_FIRST
23. }) // 嵌套模式
24. .backgroundColor(Color.Gray)
25. .width('90%')
26. .height('100%')
27. }
28. }
```

## ListItem横滑跟手比变更

**变更原因**

ListItem横滑动态跟手比计算公式，需要与其他场景（例如：List拖动过界）的公式一致。

**变更影响**

此变更涉及应用适配。

ListItem横滑动态跟手比按新实现后，手指滑动相同距离，组件滑动距离会变大。

**适配指导**

默认效果变更，无需适配。

## DrawableDescriptor显示效果

**访问级别**

公开接口

**变更原因**

对原来非标准288x288图标的裁切行为做统一变更，提高用户体验。

**变更影响**

对于非288x288尺寸前景图片，当前生成的分层图标按照缩放后裁剪显示，288x288尺寸前景图片保持原规格。

**适配指导**

默认效果变更，无需适配，但应注意变更后的默认效果是否符合开发者预期，如不符合则应自定义修改效果控制变量以达到预期。

## TimePickerDialog、DatePickerDialog支持设置前导零

**变更原因**

修改时间日期选择器的样式规范，给TimePickerDialog、DatePickerDialog设置是否需要前导零。

**变更影响**

此变更涉及应用适配，只影响TimePickerDialog、DatePickerDialog组件的默认样式。

* 变更前： TimePickerDialog、DatePickerDialog组件12小时制小时默认有前置零。
* 变更后： TimePickerDialog、DatePickerDialog组件12小时制小时默认没有前置零。

  如下图所示为变更前后效果对比：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**适配指导**

默认行为变更，应注意时间窗口是否按照设置显示前导零。

## AlphabetIndexer组件popupPosition属性设置为undefined时重置为默认值

**变更原因**

popupPosition属性设置为undefined时应该重置为默认值，但当前实际上会保持现有状态不发生变化，导致开发者不能重置该属性，变更后开发者可通过对该属性设置undefined重置该属性。

**变更影响**

此变更涉及应用适配。

API version 12之前，popupPosition属性设置为undefined时会保持现有状态，提示弹窗位置不发生变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/iw5DsVr-RzqmwQVlxtbQyQ/zh-cn_image_0000001987151785.png?HW-CC-KV=V1&HW-CC-Date=20260429T052410Z&HW-CC-Expire=86400&HW-CC-Sign=57F8ED1A6B5EA4F5D7381180217C323E0487EDC616216E91567D6B46DE6071D6)

API version 12及以后，popupPosition属性设置为undefined时会重置为默认值，提示弹窗位置会发生变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/0zjPVPjrTMatFz54l8CApg/zh-cn_image_0000001953232366.png?HW-CC-KV=V1&HW-CC-Date=20260429T052410Z&HW-CC-Expire=86400&HW-CC-Sign=712E3B0D5F584EF97BF2CA4E25AD7B3B7667B783E897E8F92D01DD7CE1AED660)

**变更的接口/组件**

AlphabetIndexer组件

**适配指导**

开发者需要判断变更后popupPosition属性设置undefined时重置为默认值的效果是否符合预期，如不符合可通过改变[AlphabetIndexer组件](../harmonyos-references-V5/ts-container-alphabet-indexer-V5.md)popupPosition属性传入参数以达到预期。

## bindContentCover动效参数变更

**变更原因**

为满足应用述求和UX规格，全模态动效参数改为与半模态一致。

**变更影响**

变更前，全模态动效参数为interpolatingSpring(velocity:n, mass:1, stiffness:100, damping:20)，动效时长约为1200ms。

变更后，全模态动效参数为interpolatingSpring(velocity:n, mass:1, stiffness:328, damping:36)，动效时长约为800ms。

**变更的接口/组件**

bindContentCover组件

**适配指导**

默认行为变更，应注意变更后的默认效果是否符合开发者预期，如不符合则自定义修改效果控制变量以达到预期，可通过transition接口自定义动效。

## RichEditor长按交互调整

**变更原因**

为满足应用述求和UX规格，RichEditor组件长按交互效果需要进行调整。

**变更影响**

变更前，长按文本内容，直接触发选词，展示选中背板、手柄以及文本选择菜单。

变更后，长按文本内容不松手，触发选词并展示选中背板，继续拖动变更选中区域，松手后展示手柄及文本选择菜单。如果不继续拖动，则松手时直接展示手柄和文本选择菜单。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

RichEditor组件

**适配指导**

默认行为变更，应注意变更后的默认效果是否符合开发者预期，如不符合则自定义修改事件效果以达到预期。

## 滚动类组件（List、Grid、WaterFlow、Scroll）Friction接口默认值变更

**变更原因**

为了优化功耗，将滚动类组件（List、Grid、WaterFlow、Scroll）friction接口默认值改为0.75。

**变更影响**

此变更涉及应用适配。

变更前，滚动类组件（List、Grid、WaterFlow、Scroll）的friction接口默认值为0.7。

变更后，滚动类组件（List、Grid、WaterFlow、Scroll）的friction接口默认值为0.75。相较变更之前，用同样力度抛滑，抛滑时间更短、抛滑距离更近。

**变更的接口/组件**

滚动类组件（List、Grid、WaterFlow、Scroll）的friction接口。

**适配指导**

开发者如果需要使用变更之前的抛滑效果，可以将friction接口的参数设置为0.7。

```
1. @Entry
2. @Component
3. struct FrictionExample {
4. build() {
5. List() {
6. ForEach([1, 2, 3, 4, 5], (item: number) => {
7. ListItem() {
8. Text('' + item)
9. .width('100%').height(200).fontSize(16)
10. .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
11. }
12. }, (item: string) => item)
13. }
14. .height(500)
15. .friction(0.7)
16. }
17. }
```

## ListItem卡片样式行为变更

**变更原因**

原本ListItem在LazyForEach下使用时，ListItem设置卡片样式不生效，需要调整为可以生效。

**变更影响**

此变更涉及应用适配。

变更前：ListItem在LazyForEach下使用时，卡片样式设置不生效。

变更后：ListItem在LazyForEach下使用时，卡片样式设置可以生效。

```
1. // Basic implementation of IDataSource to handle data listener
2. abstract class BasicDataSource<T> implements IDataSource {
3. private listeners: DataChangeListener[] = []

5. public totalCount(): number {
6. return 0
7. }
8. abstract getData(index: number): T;

10. registerDataChangeListener(listener: DataChangeListener): void {
11. if (this.listeners.indexOf(listener) < 0) {
12. this.listeners.push(listener)
13. }
14. }
15. unregisterDataChangeListener(listener: DataChangeListener): void {
16. const pos = this.listeners.indexOf(listener);
17. if (pos >= 0) {
18. this.listeners.splice(pos, 1)
19. }
20. }

22. notifyDataReload(): void {
23. this.listeners.forEach(listener => {
24. listener.onDataReloaded()
25. })
26. }
27. notifyDataAdd(index: number): void {
28. this.listeners.forEach(listener => {
29. listener.onDataAdd(index)
30. })
31. }
32. notifyDataChange(index: number): void {
33. this.listeners.forEach(listener => {
34. listener.onDataChange(index)
35. })
36. }
37. notifyDataDelete(index: number): void {
38. this.listeners.forEach(listener => {
39. listener.onDataDelete(index)
40. })
41. }
42. notifyDataMove(from: number, to: number): void {
43. this.listeners.forEach(listener => {
44. listener.onDataMove(from, to)
45. })
46. }
47. }

49. class MyDataSource<T> extends BasicDataSource<T> {
50. public dataArray: T[] = [];

52. public totalCount(): number {
53. return this.dataArray.length
54. }
55. public getData(index: number): T {
56. return this.dataArray[index]
57. }

59. public addData(index: number, data: T): void {
60. this.dataArray.splice(index, 0, data)
61. this.notifyDataAdd(index)
62. }
63. public popFirstData(): void {
64. this.dataArray.shift()
65. this.notifyDataDelete(0)
66. }
67. public pushData(data: T): void {
68. this.dataArray.push(data)
69. this.notifyDataAdd(this.dataArray.length - 1)
70. }
71. public popData(): void {
72. this.dataArray.pop()
73. this.notifyDataDelete(this.dataArray.length)
74. }
75. }

77. @Entry
78. @Component
79. struct Index {
80. arr:MyDataSource<number> = new MyDataSource<number>();
81. aboutToAppear(): void {
82. for (let i = 0; i < 10; i++) {
83. this.arr.pushData(i)
84. }
85. }

87. build() {
88. List() {
89. ListItemGroup({ style: ListItemGroupStyle.CARD }) {
90. LazyForEach(this.arr, (item: number) => {
91. ListItem({ style: ListItemStyle.CARD }) {
92. Text("item" + item.toString())
93. }
94. })
95. }
96. }.backgroundColor("#DCDCDC")
97. .height("100%")
98. }
99. }
```

| 变更前效果 | 变更后效果 |
| --- | --- |
|  |  |

**变更的接口/组件**

涉及的组件：ListItem组件ListItemStyle接口。

**适配指导**

如果ListItem在LazyForEach下使用，设置了卡片样式没有生效，变更后生效卡片样式导致显示界面变化，可以删除卡片样式的设置。

如下代码变更前设置卡片样式不生效，变更后生效卡片样式导致显示界面变化。

```
1. build() {
2. List() {
3. ListItemGroup({ style: ListItemGroupStyle.CARD }) {
4. LazyForEach(this.arr, (item: number) => {
5. ListItem({ style: ListItemStyle.CARD }) {
6. Text("item" + item.toString())
7. .height(64)
8. }
9. })
10. }
11. }.backgroundColor("#DCDCDC")
12. .height("100%")
13. }
```

删除ListItem卡片样式可以恢复变更前效果。

```
1. build() {
2. List() {
3. ListItemGroup({ style: ListItemGroupStyle.CARD }) {
4. LazyForEach(this.arr, (item: number) => {
5. ListItem() {
6. Text("item" + item.toString())
7. .height(64)
8. }
9. })
10. }
11. }.backgroundColor("#DCDCDC")
12. .height("100%")
13. }
```

## List的constraintSize设置生效

**变更原因**

List的布局行为和当前通用的布局约束优先的规格不一致。

**变更影响**

此变更涉及应用适配。

变更前，List不设置Height时，constraintSize的minHeight设置不生效。

变更后，List不设置Height时，constraintSize的minHeight设置会生效。

```
1. @Entry
2. @Component
3. struct ListExample {
4. build() {
5. List({ space: 5 }) {
6. ForEach([1, 2, 3, 4, 5], (item: number) => {
7. ListItem() {
8. Text('' + item)
9. .width('100%').height(50)
10. .textAlign(TextAlign.Center).backgroundColor(0xFFFFFF)
11. }
12. }, (item: string) => item)
13. }
14. .padding(5)
15. .constraintSize({ minHeight: 500 })
16. .backgroundColor(0xDCDCDC)
17. }
18. }
```

如下是以上示例代码变更前后效果对比：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

List组件的constraintSize接口。

**适配指导**

如果List没有设置height属性，且设置了constraintSize的minHeight属性。变更后minHeight属性生效，导致布局界面变化，如果需要保持之前的布局界面，可以删除constraintSize的minHeight属性。

如下代码，变更前constraintSize的minHeight属性不生效，变更后constraintSize的minHeight属性生效导致显示界面变化。

```
1. @Entry
2. @Component
3. struct ListExample {
4. build() {
5. List({ space: 5 }) {
6. ForEach([1, 2, 3, 4, 5], (item: number) => {
7. ListItem() {
8. Text('' + item)
9. .width('100%').height(50)
10. .textAlign(TextAlign.Center).backgroundColor(0xFFFFFF)
11. }
12. }, (item: string) => item)
13. }
14. .padding(5)
15. .constraintSize({ minHeight: 500, maxHeight: 1000 })
16. .backgroundColor(0xDCDCDC)
17. }
18. }
```

删除constraintSize接口minHeight设置可以恢复之前的效果。

```
1. @Entry
2. @Component
3. struct ListExample {
4. build() {
5. List({ space: 5 }) {
6. ForEach([1, 2, 3, 4, 5], (item: number) => {
7. ListItem() {
8. Text('' + item)
9. .width('100%').height(50)
10. .textAlign(TextAlign.Center).backgroundColor(0xFFFFFF)
11. }
12. }, (item: string) => item)
13. }
14. .padding(5)
15. .constraintSize({ maxHeight: 1000 })
16. .backgroundColor(0xDCDCDC)
17. }
18. }
```

## AlphabetIndexer组件autoCollapse属性默认值由false改为true

**变更原因**

自适应折叠模式使用场景更广，显示效果更加灵活，默认开启自适应折叠模式更符合开发者期望。

**变更影响**

此变更涉及应用适配。

API version 12之前：autoCollapse属性默认值为false，当AlphabetIndexer组件高度不足时，不会折叠显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/gVhJRN-CQAevX9oJlhgsoA/zh-cn_image_0000001987311653.png?HW-CC-KV=V1&HW-CC-Date=20260429T052410Z&HW-CC-Expire=86400&HW-CC-Sign=A6540C46AA9579C73550828F17B683262485AF5562AD9722C5DCA6855B37A707)

API version 12及之后：autoCollapse属性默认值为true，当AlphabetIndexer组件高度不足时，会折叠显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/63yzc1hfQH-At4LMOjsXog/zh-cn_image_0000001987151797.png?HW-CC-KV=V1&HW-CC-Date=20260429T052410Z&HW-CC-Expire=86400&HW-CC-Sign=2373E639E59E961DAEA4C8E756946E1DB3A4727094C1611449E42BE62CD125F3)

**变更的接口/组件**

AlphabetIndexer组件

**适配指导**

默认行为变更，默认开启自适应折叠模式，若要关闭自适应折叠模式，可通过设置[autoCollapse](../harmonyos-references-V5/ts-container-alphabet-indexer-V5.md#autocollapse11)属性进行适配。

## 光标默认样式变更

**变更原因**

默认UX样式变更。

**变更影响**

此变更涉及应用适配。

变更前：光标小圆圈默认直径为20vp。

变更后：光标小圆圈默认直径为16vp。

变更前后对比效果，如下表所示

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

涉及光标的组件：TextInput、TextArea、Search、RichEditor。

**适配指导**

默认UX样式变更，无需适配。

## 高级组件SelectionMenu默认样式变更

**变更原因**

默认UX样式变更。

**变更影响**

此变更涉及应用适配。

变更前：自定义文本选择菜单点击“更多”后展开菜单会显示内置的置灰项分享翻译搜索。

变更后：自定义文本选择菜单点击“更多”后展开菜单去除内置的置灰项分享翻译搜索。

变更前后对比效果，如下表所示：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

高级组件SelectionMenu。

**适配指导**

默认UX样式变更，无需适配。

## SVG根节点视窗外图片内容裁剪

**访问级别**

公开接口

**变更原因**

修正视觉效果以符合SVG标准。

**变更影响**

此变更涉及应用适配。

```
1. <svg width="100" height="100" viewBox="0 0 300 300" version="1.1">
2. <defs>
3. <circle id = "circleId" cx="100" cy="50" r="40"  fill="red"/>
4. </defs>
5. <polygon points="220,100 300,210 170,250 123,234" style="fill:#cccccc;stroke:#000000;stroke-width:1"/>
6. <use href="#circleId" x = "300" y= "150" width="50" height="50"/>
7. </svg>
```

| 变更前 | 变更后 |
| --- | --- |
| 绘制内容超出根节点视窗区域会显示 | 绘制内容超出根节点视窗区域不显示 |
|  |  |

**变更的接口/组件**

涉及的组件：Image、ImageSpan、Canvas。

**适配指导**

默认效果变更，无需适配，但应注意变更后的行为是否对整体应用显示效果产生影响。

## Symbol系统资源变更

**变更原因**

默认UX样式变更。

**变更影响**

此变更涉及应用适配。

```
1. @Extend(SymbolSpan) function style() {
2. .fontWeight(FontWeight.Lighter)
3. .fontSize(96)
4. }
5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Column() {
10. Text() {
11. SymbolSpan($r('sys.symbol.ohos_wifi')).style()
12. SymbolSpan($r('sys.symbol.ohos_trash')).style()
13. SymbolSpan($r('sys.symbol.ohos_trash_circle')).style()
14. SymbolSpan($r('sys.symbol.ohos_photo')).style()
15. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus')).style()
16. SymbolSpan($r('sys.symbol.ohos_lungs')).style()
17. SymbolSpan($r('sys.symbol.ohos_mic')).style()
18. SymbolSpan($r('sys.symbol.ohos_circle')).style()

20. SymbolSpan($r('sys.symbol.ohos_lock')).style()
21. SymbolSpan($r('sys.symbol.ohos_star')).style()
22. SymbolSpan($r('sys.symbol.ohos_arrow_up')).style()
23. }
24. }.width('100%')
25. }
26. }
```

下表例举资源变更前后对比效果：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

涉及Symbol资源的组件：SymbolSpan、SymbolGlyph。

**适配指导**

默认UX样式变更，无需适配。

## 安全控件的背景板变更

**变更原因**

安全控件可设置背景板的属性为不可见或透明，应用可利用此配置将安全控件对用户隐藏，若用户在不知情的情况下触发点击授权，应用就会获取用户的位置、剪切板等敏感信息。

**变更影响**

此变更涉及应用适配。

变更前:

1. 安全控件按钮在构造函数中不设置背景板时，安全控件不展示背景板。
2. 安全控件按钮背景色高八位的α值低于0x1A（例如0x1800ff00）时,安全控件的背景板透明度显示和开发者的设置值一致。

变更后:

1. 安全控件按钮在构造函数中不设置背景板时，安全控件默认展示背景板。
2. 安全控件按钮背景色高八位的α值低于0x1A（例如0x1800ff00）时,安全控件按钮背景色高八位的α值会被系统强制调整为0xff。

**变更的接口/组件**

@internal/component/ets/location\_button.d.ts中 LocationButton接口。

@internal/component/ets/save\_button.d.ts中 SaveButton接口。

@internal/component/ets/paste\_button.d.ts中 PasteButton接口。

**适配指导**

接口使用的示例代码可参考:

[LocationButton接口指导](../harmonyos-references-V5/ts-security-components-locationbutton-V5.md#接口)

[SaveButton接口指导](../harmonyos-references-V5/ts-security-components-savebutton-V5.md#接口)

[PasteButton接口指导](../harmonyos-references-V5/ts-security-components-pastebutton-V5.md#接口)
