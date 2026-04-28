---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-mouse
title: 支持鼠标输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件 > 支持鼠标输入事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:49512602f704161efe70f728bc67ab1a3aff740f175f026e293b778521dfb009
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/CbYGN2-rRfeHtbZBBcChJQ/zh-cn_image_0000002583477945.png?HW-CC-KV=V1&HW-CC-Date=20260427T233950Z&HW-CC-Expire=86400&HW-CC-Sign=547D54233D83D5EC346C7BD94C593B39876998AA965B19E864B40A2F441B01C8)

鼠标设备是2in1类型设备必不可少的输入设备，其特点是可以通过按键达成点击或滑动操作，也可以通过滚轮触发滑动，另外还有一些按键，这些分别通过MouseEvent及AxisEvent上报给应用。

说明

所有单指可响应的触摸事件/手势事件，均可通过鼠标左键来操作和响应。

* 例如当我们需要开发单击Button跳转页面的功能、且需要支持手指点击和鼠标左键点击，那么只绑定一个点击事件（onClick）就可以实现该效果；
* 若需要针对手指和鼠标左键的点击实现不一样的效果，可以在onClick回调中，使用回调参数中的source字段判断当前触发事件的来源是手指还是鼠标。

## 处理鼠标移动

鼠标事件通过[onMouse](../harmonyos-references/ts-universal-mouse-key.md#onmouse)接口注册一个回调来接收，当鼠标事件发生时，会按照鼠标光标所在位置下的组件进行派发，派发过程同样遵循事件冒泡机制。

### onMouse

```
1. onMouse(event: (event?: MouseEvent) => void)
```

鼠标事件回调。每当鼠标指针在绑定该API的组件内产生行为（MouseAction）时，触发事件回调，参数为[MouseEvent](../harmonyos-references/ts-universal-mouse-key.md#mouseevent对象说明)对象，表示触发此次的鼠标事件。该事件支持自定义冒泡设置，默认父子冒泡。常用于开发者自定义的鼠标行为逻辑处理。

开发者可以通过回调中的MouseEvent对象获取触发事件的坐标（displayX/displayY/windowX/windowY/x/y）、按键（[MouseButton](../harmonyos-references/ts-appendix-enums.md#mousebutton8)）、行为（[MouseAction](../harmonyos-references/ts-appendix-enums.md#mouseaction8)）、时间戳（[timestamp](../harmonyos-references/ts-gesture-customize-judge.md#baseevent8)）、交互组件的区域（[EventTarget](../harmonyos-references/ts-universal-events-click.md#eventtarget8)）、事件来源（[SourceType](../harmonyos-references/ts-gesture-settings.md#sourcetype枚举说明8)）等。MouseEvent的回调函数stopPropagation用于设置当前事件是否阻止冒泡。

说明

按键（MouseButton）的值：Left/Right/Middle/Back/Forward均对应鼠标上的实体按键，当这些按键被按下或松开时触发这些按键的事件。None表示没有鼠标按键按下或松开的状态下，仅移动鼠标所触发的事件。

```
1. @Entry
2. @Component
3. struct MouseMove {
4. @State buttonText: string = '';
5. @State columnText: string = '';
6. @State text: string = 'OnMouse Sample Button';
7. @State color: Color = Color.Gray;

9. build() {
10. Column() {
11. Button(this.text, { type: ButtonType.Capsule })
12. .width(200)
13. .height(100)
14. .backgroundColor(this.color)
15. .onMouse((event?: MouseEvent) => { // 设置Button的onMouse回调
16. if (event) {
17. this.buttonText = 'Button onMouse:\n' + '' +
18. 'button = ' + event.button + '\n' +
19. 'action = ' + event.action + '\n' +
20. 'x,y = ' + '\n' + '(' + event.x + ',' + event.y + ')' + '\n' +
21. 'windowXY=' + '\n' + '(' + event.windowX + ',' + event.windowY + ')';
22. }
23. })
24. Column() {
25. Divider()
26. Text(this.buttonText).fontColor(Color.Green).padding(5)
27. Divider()
28. Text(this.columnText).fontColor(Color.Red).padding(5)
29. }
30. .width('100%')
31. .alignItems(HorizontalAlign.Start)
32. }
33. .width('100%')
34. .height('100%')
35. .justifyContent(FlexAlign.Center)
36. .borderWidth(2)
37. .borderColor(Color.Red)
38. .onMouse((event?: MouseEvent) => { // Set the onMouse callback for the column.
39. if (event) {
40. this.columnText = 'Column onMouse:\n' + '' +
41. 'button = ' + event.button + '\n' +
42. 'action = ' + event.action + '\n' +
43. 'x,y = ' + '\n' + '(' + event.x + ',' + event.y + ')' + '\n' +
44. 'windowXY=' + '\n' + '(' + event.windowX + ',' + event.windowY + ')';
45. }
46. })
47. }
48. }
```

[MouseMove.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/mouseMove/MouseMove.ets#L16-L65)

上面的示例中给Button绑定onMouse接口。在回调中，打印出鼠标事件的button/action等回调参数值。同时，在外层的Column容器上，也做相同的设置。整个过程可以分为以下两个动作：

1. 移动鼠标：在鼠标从Button外部移入Button内部前，仅触发了Column的onMouse回调；当鼠标移入到Button内部后，由于onMouse事件默认是冒泡的，所以此时会同时响应Column的onMouse回调和Button的onMouse回调。此过程中，由于鼠标仅有移动动作而没有点击动作，因此打印信息中的button均为0（MouseButton.None的枚举值）、action均为3（MouseAction.Move的枚举值）。
2. 点击鼠标：鼠标进入Button后进行了2次点击，分别是左键点击和右键点击。

   左键点击时：button = 1（MouseButton.Left的枚举值），按下时：action = 1（MouseAction.Press的枚举值），抬起时：action = 2（MouseAction.Release的枚举值）。

   右键点击时：button = 2（MouseButton.Right的枚举值），按下时：action = 1（MouseAction.Press的枚举值），抬起时：action = 2（MouseAction.Release的枚举值）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/s14bH37vTsuXfNVNyHf4Pg/zh-cn_image_0000002552798296.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233950Z&HW-CC-Expire=86400&HW-CC-Sign=C3806B3337C6C45025D1D6C8B91700DFD05BB9B1ABBD5E6C0644A663B1A3F89C)

如果需要阻止鼠标事件冒泡，可以通过调用stopPropagation方法进行设置。

```
1. @Entry
2. @Component
3. struct StopPropagation {
4. @State buttonText: string = '';
5. @State columnText: string = '';
6. @State text: string = 'OnMouse Sample Button';
7. @State color: Color = Color.Gray;

9. build() {
10. Column() {
11. Button(this.text, { type: ButtonType.Capsule })
12. .width(200)
13. .height(100)
14. .backgroundColor(this.color)
15. .onMouse((event?: MouseEvent) => { // 设置Button的onMouse回调
16. if (event) {
17. event.stopPropagation(); // 在Button的onMouse事件中设置阻止冒泡
18. this.buttonText = 'Button onMouse:\n' + '' +
19. 'button = ' + event.button + '\n' +
20. 'action = ' + event.action + '\n' +
21. 'x,y = ' + '\n' + '(' + event.x + ',' + event.y + ')' + '\n' +
22. 'windowXY=' + '\n' + '(' + event.windowX + ',' + event.windowY + ')';
23. }
24. })
25. Column() {
26. Divider()
27. Text(this.buttonText).fontColor(Color.Green).padding(5)
28. Divider()
29. Text(this.columnText).fontColor(Color.Red).padding(5)
30. }
31. .width('100%')
32. .alignItems(HorizontalAlign.Start)
33. }
34. .width('100%')
35. .height('100%')
36. .justifyContent(FlexAlign.Center)
37. .borderWidth(2)
38. .borderColor(Color.Red)
39. .onMouse((event?: MouseEvent) => { // 设置Column的onMouse回调
40. if (event) {
41. this.columnText = 'Column onMouse:\n' + '' +
42. 'button = ' + event.button + '\n' +
43. 'action = ' + event.action + '\n' +
44. 'x,y = ' + '\n' + '(' + event.x + ',' + event.y + ')' + '\n' +
45. 'windowXY=' + '\n' + '(' + event.windowX + ',' + event.windowY + ')';
46. }
47. })
48. }
49. }
```

[StopPropagation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/stopPropagation/StopPropagation.ets#L16-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/goAcJWvsQVq-JWwuKevDaw/zh-cn_image_0000002583437991.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233950Z&HW-CC-Expire=86400&HW-CC-Sign=0A05B1EAADFDCA13DD3CF9BC87F0BF4DC4DB8A3B5FDF838BE07B05ED4A97AC53)

在子组件（Button）的onMouse中，通过回调参数event调用stopPropagation回调方法（如上）即可阻止Button子组件的鼠标事件冒泡到父组件Column上。

### onHover

如果需要感知鼠标移入或移出控件范围，建议直接使用高级事件[onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)，建议避免直接处理鼠标move事件，以保持代码简洁。

```
1. onHover(event: (isHover: boolean) => void)
```

悬浮事件回调。参数isHover类型为boolean，表示鼠标进入组件或离开组件。该事件支持自定义冒泡设置，默认父子冒泡。

若组件绑定了该接口，当鼠标指针从组件外部进入到该组件的瞬间会触发事件回调，参数isHover等于true；鼠标指针离开组件的瞬间也会触发该事件回调，参数isHover等于false。

```
1. @Entry
2. @Component
3. struct OnHover {
4. @State hoverText: string = 'Not Hover';
5. @State color: Color = Color.Gray;

7. build() {
8. Column() {
9. Button(this.hoverText)
10. .width(200).height(100)
11. .backgroundColor(this.color)
12. .onHover((isHover?: boolean) => { // 使用onHover接口监听鼠标是否悬浮在Button组件上
13. if (isHover) {
14. this.hoverText = 'Hovered!';
15. this.color = Color.Green;
16. } else {
17. this.hoverText = 'Not Hover';
18. this.color = Color.Gray;
19. }
20. })
21. }.width('100%').height('100%').justifyContent(FlexAlign.Center)
22. }
23. }
```

[OnHover.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/onHover/OnHover.ets#L16-L40)

该示例创建了一个Button组件，初始背景色为灰色，内容为“Not Hover”。示例中的Button组件绑定了onHover回调，在该回调中将this.isHovered变量置为回调参数：isHover。

当鼠标从Button外移动到Button内的瞬间，回调响应，isHover值等于true，isHovered的值变为true，将组件的背景色改成Color.Green，内容变为“Hovered!”。

当鼠标从Button内移动到Button外的瞬间，回调响应，isHover值等于false，又将组件变成了初始的样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/_wo61B5sRp2gAHmdz7z5EQ/zh-cn_image_0000002552957946.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233950Z&HW-CC-Expire=86400&HW-CC-Sign=E49F277A7DF1368024C4E50C53AAC7F612A8695DC3FE2868940DB0B0D79E7FFA)

## 处理鼠标按键

当用户按下鼠标上的按键时，会产生鼠标按下事件，可以通过[MouseEvent](../harmonyos-references/ts-universal-mouse-key.md#mouseevent对象说明)访问事件的一些重要信息，如发生时间，鼠标按键(MouseButton: 左键/右键等)，也可以通过[**getModifierKeyState**](../harmonyos-references/ts-gesture-customize-judge.md#getmodifierkeystate12)接口获取到用户在使用鼠标时，物理键盘上的**ctrl/alt/shift**这几个修饰键的按下状态，可以通过组合判断它们的状态来实现一些便捷操作。

以下是一个通过处理鼠标按键实现快速多选的示例：

```
1. class ListDataSource implements IDataSource {
2. private list: number[] = [];
3. private listeners: DataChangeListener[] = [];

5. constructor(list: number[]) {
6. this.list = list;
7. }

9. totalCount(): number {
10. return this.list.length;
11. }

13. getData(index: number): number {
14. return this.list[index];
15. }

17. registerDataChangeListener(listener: DataChangeListener): void {
18. if (this.listeners.indexOf(listener) < 0) {
19. this.listeners.push(listener);
20. }
21. }

23. unregisterDataChangeListener(listener: DataChangeListener): void {
24. const pos = this.listeners.indexOf(listener);
25. if (pos >= 0) {
26. this.listeners.splice(pos, 1);
27. }
28. }

30. // 通知控制器数据删除
31. notifyDataDelete(index: number): void {
32. this.listeners.forEach(listener => {
33. listener.onDataDelete(index);
34. });
35. }

37. // 在指定索引位置删除一个元素
38. public deleteItem(index: number): void {
39. this.list.splice(index, 1);
40. this.notifyDataDelete(index);
41. }
42. }

44. @Entry
45. @Component
46. struct ListExample {
47. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
48. private allSelectedItems: Array<number> = [];
49. @State isSelected: boolean[] = [];

51. @Styles
52. selectedStyle(): void {
53. .backgroundColor(Color.Blue);
54. }

56. isItemSelected(item: number): boolean {
57. for (let i = 0; i < this.allSelectedItems.length; i++) {
58. if (this.allSelectedItems[i] === item) {
59. this.isSelected[item] = true;
60. return true;
61. }
62. }
63. this.isSelected[item] = false;
64. return false;
65. }

67. build() {
68. Column() {
69. List({ space: 10, initialIndex: 0 }) {
70. LazyForEach(this.arr, (index: number) => {
71. ListItem() {
72. Text('' + index)
73. .width('100%')
74. .height(100)
75. .fontSize(16)
76. .fontColor(this.isSelected[index] ? Color.White : Color.Black)
77. .textAlign(TextAlign.Center)
78. }
79. .backgroundColor(Color.White)
80. .selectable(true)
81. .selected(this.isSelected[index])
82. .stateStyles({
83. selected: this.selectedStyle
84. })
85. .onMouse((event: MouseEvent) => {
86. // 判断是否按下鼠标左键
87. if (event.button === MouseButton.Left && event.action === MouseAction.Press) {
88. // 判断之前是否已经是选中状态
89. let isSelected: boolean = this.isItemSelected(index);
90. // 判断修饰键状态
91. let isCtrlPressing: boolean = false;
92. if (event.getModifierKeyState) {
93. isCtrlPressing = event.getModifierKeyState(['Ctrl']);
94. }
95. // 如果没有按着ctrl键点鼠标，则强制清理掉其他选中的条目并只让当前条目选中
96. if (!isCtrlPressing) {
97. this.allSelectedItems = [];
98. for (let i = 0; i < this.isSelected.length; i++) {
99. this.isSelected[i] = false;
100. }
101. }
102. if (isSelected) {
103. this.allSelectedItems.filter(item => item !== index);
104. this.isSelected[index] = false;
105. } else {
106. this.allSelectedItems.push(index);
107. this.isSelected[index] = true;
108. }
109. }
110. })
111. }, (item: string) => item)
112. }
113. .listDirection(Axis.Vertical)
114. .scrollBar(BarState.Off)
115. .friction(0.6)
116. .edgeEffect(EdgeEffect.Spring)
117. .width('90%')
118. }
119. .width('100%')
120. .height('100%')
121. .backgroundColor(0xDCDCDC)
122. .padding({ top: 5 })
123. }
124. }
```

[MouseButton.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/MouseButton/MouseButton.ets#L16-L142)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/e208rXOMSjmAcHsKqdSnNA/zh-cn_image_0000002583477947.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233950Z&HW-CC-Expire=86400&HW-CC-Sign=69D25F6D32714EA54CF7FD26E15CB2E78D91C540EACAFC32C0C6DB1105D28CCB)

## 处理滚轮

鼠标的滚轮是一种可以产生纵向滚动量的输入设备，当用户滚动鼠标滚轮时，系统会产生纵向[轴事件](../harmonyos-references/ts-universal-events-axis.md)上报，应用可在组件上通过[onAxisEvent](../harmonyos-references/ts-universal-events-axis.md#onaxisevent)接口接收轴事件，轴事件中上报的坐标，为鼠标光标所在的位置，而滚轮上报的角度变化可从[BaseEvent](../harmonyos-references/ts-gesture-customize-judge.md#baseevent8)的axisVertical获得。

鼠标滚轮轴事件的上报，每次都以[AxisAction](../harmonyos-references/ts-appendix-enums.md#axisaction17).BEGIN类型开始，当停止滚动时以[AxisAction](../harmonyos-references/ts-appendix-enums.md#axisaction17).End结束，慢速滚动时，会产生多段的BEGIN、END上报。当你处理axisVertical时，应确保理解它的数值含义与单位，其有以下特点：

* 上报的数值单位为角度，为单次变化量，非总量。
* 上报数值大小受系统设置中对滚轮放大倍数设置的影响。
* 系统设置中的放大倍数通过AxisEvent中的scrollStep告知。
* 向前滚动，上报数值为负，向后滚动，上报数值为正。

如果使用滚动类组件，对于滚轮的响应，系统内部已实现，不需要额外处理。

如果使用[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)，对于滚轮的响应，此时向前滚动，offsetY的上报数值为正，向后滚动，offsetY的上报数值为负。

说明

1. 滚轮产生的纵向轴值，一般情况下只能触发纵向滚动手势，无法触发横向滚动。
2. 系统会在发现鼠标指针下只有能够响应横向滚动的组件时，也可以触发横向滚动。
3. 但只要指针下有一个可以响应纵向滚动，则会优先处理纵向，不再处理横向。

以下是纵向和横向的List响应滚轮的示例：

```
1. export class ListDataSource implements IDataSource {
2. private list: number[] = [];
3. private listeners: DataChangeListener[] = [];

5. constructor(list: number[]) {
6. this.list = list;
7. }

9. totalCount(): number {
10. return this.list.length;
11. }

13. getData(index: number): number {
14. return this.list[index];
15. }

17. registerDataChangeListener(listener: DataChangeListener): void {
18. if (this.listeners.indexOf(listener) < 0) {
19. this.listeners.push(listener);
20. }
21. }

23. unregisterDataChangeListener(listener: DataChangeListener): void {
24. const pos = this.listeners.indexOf(listener);
25. if (pos >= 0) {
26. this.listeners.splice(pos, 1);
27. }
28. }

30. // 通知控制器数据删除
31. notifyDataDelete(index: number): void {
32. this.listeners.forEach(listener => {
33. listener.onDataDelete(index);
34. });
35. }

37. // 通知控制器添加数据
38. notifyDataAdd(index: number): void {
39. this.listeners.forEach(listener => {
40. listener.onDataAdd(index);
41. });
42. }

44. // 在指定索引位置删除一个元素
45. public deleteItem(index: number): void {
46. this.list.splice(index, 1);
47. this.notifyDataDelete(index);
48. }

50. // 在指定索引位置插入一个元素
51. public insertItem(index: number, data: number): void {
52. this.list.splice(index, 0, data);
53. this.notifyDataAdd(index);
54. }
55. }
```

[ListDataSource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/MouseWheel/ListDataSource.ets#L16-L72)

```
1. import { ListDataSource } from './ListDataSource';

3. @Entry
4. @Component
5. struct MouseWheel {
6. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
7. @State dir1: Axis = Axis.Vertical;

9. build() {
10. Column() {
11. Button('Click to Change ListDirection')
12. .margin(20)
13. .onClick(() => {
14. if (this.dir1 === Axis.Vertical) {
15. this.dir1 = Axis.Horizontal
16. } else {
17. this.dir1 = Axis.Vertical
18. }
19. })
20. List({ space: 20, initialIndex: 0 }) {
21. LazyForEach(this.arr, (item: number) => {
22. ListItem() {
23. Text('' + item)
24. .width('100%')
25. .height(100)
26. .fontSize(16)
27. .textAlign(TextAlign.Center)
28. .borderRadius(10)
29. .backgroundColor(0xFFFFFF)
30. }
31. .margin(20)
32. // 为ListItem绑定滑动手势，当在ListItem上滚动鼠标滚轮时，会优先触发ListItem的滑动手势
33. .gesture(PanGesture({ direction: PanDirection.Vertical })
34. .onActionStart(() => {
35. })
36. .onActionUpdate(() => {
37. }))
38. }, (item: number) => item.toString())
39. }
40. .borderWidth(1)
41. .listDirection(this.dir1) // 排列方向
42. .scrollBar(BarState.Off)
43. .friction(0.6)
44. .divider({
45. strokeWidth: 2,
46. color: 0xFFFFFF,
47. startMargin: 20,
48. endMargin: 20
49. }) // 每行之间的分界线
50. .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
51. .width('90%')
52. }
53. .width('100%')
54. .height('100%')
55. .backgroundColor(0xDCDCDC)
56. .padding(20)
57. }
58. }
```

[MouseWheel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/MouseWheel/MouseWheel.ets#L16-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/S6mulMUdT6eVDTtNSZ4PYQ/zh-cn_image_0000002552798298.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233950Z&HW-CC-Expire=86400&HW-CC-Sign=67EC27FE93AC31BA49580E5375E2BB0FAF5C33991660BE2C0F2DA0D84A8B9D2D)
