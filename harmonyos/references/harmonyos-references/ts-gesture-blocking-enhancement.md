---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement
title: 手势拦截增强
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 手势控制 > 手势拦截增强
category: harmonyos-references
scraped_at: 2026-04-29T13:51:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:53c5b12ffb04f2f1ec3d92d1fc531c2475a347be5da6cdc24f7b0d7de390e1cc
---

为组件提供手势拦截能力。开发者可根据需要，将系统内置手势和比其优先级高的手势做并行化处理，并可以动态控制手势事件的触发。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## shouldBuiltInRecognizerParallelWith

PhonePC/2in1TabletTVWearable

shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T

提供系统内置手势与响应链上其他组件的手势设置并行关系的回调事件。此接口对应的C API接口为[setInnerGestureParallelTo](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setinnergestureparallelto)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ShouldBuiltInRecognizerParallelWithCallback](ts-gesture-blocking-enhancement.md#shouldbuiltinrecognizerparallelwithcallback) | 是 | 系统内置手势与响应链上其他组件的手势设置并行关系的回调事件，当该组件进行触摸碰撞测试时，会触发用户定义的回调来形成手势并行关系。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ShouldBuiltInRecognizerParallelWithCallback

PhonePC/2in1TabletTVWearable

type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer

系统内置手势与响应链上其他组件的手势设置并行关系的回调事件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| current | [GestureRecognizer](ts-gesture-common.md#gesturerecognizer12) | 是 | 当前组件的系统内置手势识别器，当前版本只提供内置的[GestureType](ts-gesture-common.md#gesturetype11).PAN\_GESTURE类型的手势识别器。 |
| others | Array<[GestureRecognizer](ts-gesture-common.md#gesturerecognizer12)> | 是 | 响应链上更高优先级的其他组件相同类别的手势识别器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GestureRecognizer](ts-gesture-common.md#gesturerecognizer12) | 与current识别器绑定并行关系的某个手势识别器。 |

## onGestureRecognizerJudgeBegin13+

PhonePC/2in1TabletTVWearable

onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback, exposeInnerGesture: boolean): T

给组件绑定自定义手势识别器判定回调。

新增exposeInnerGesture参数作为是否将ArkUI系统组合组件的内置组件的手势暴露给开发者的标识。当该标识置为true时，将ArkUI系统组合组件的内置组件的手势暴露给开发者。

对于不需要将ArkUI系统组合组件的内置组件的手势暴露给开发者的场景，建议采用原有[onGestureRecognizerJudgeBegin](ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin)接口。若要求将ArkUI系统组合组件的内置组件的手势暴露给开发者，建议使用该接口并将exposeInnerGesture设置为true。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](ts-gesture-blocking-enhancement.md#gesturerecognizerjudgebegincallback) | 是 | 给组件绑定自定义手势识别器判定回调，当绑定到该组件的手势即将成功时，会触发用户定义的回调来获取结果。 |
| exposeInnerGesture | boolean | 是 | 暴露内部手势标识。  默认值：false  **说明：**  如果是组合组件，此参数设置true，回调中的current参数则会包含组合组件内部的手势识别器。  当前仅支持[Tabs](ts-container-tabs.md)，其他组件请不要设置此参数。  设置为false时，功能与原接口[onGestureRecognizerJudgeBegin](ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin)相同。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onGestureRecognizerJudgeBegin

PhonePC/2in1TabletTVWearable

onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T

给组件绑定自定义手势识别器判定回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](ts-gesture-blocking-enhancement.md#gesturerecognizerjudgebegincallback) | 是 | 自定义手势识别器判定回调。当绑定到该组件的手势即将成功时，会触发用户定义的回调来获取结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## GestureRecognizerJudgeBeginCallback

PhonePC/2in1TabletTVWearable

type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>, touchRecognizers?: Array<TouchRecognizer>) => GestureJudgeResult

自定义手势识别器判定回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [BaseGestureEvent](ts-gesture-common.md#basegestureevent11对象说明) | 是 | 当前基础手势事件信息。 |
| current | [GestureRecognizer](ts-gesture-common.md#gesturerecognizer12) | 是 | 当前即将要响应的识别器对象。 |
| recognizers | Array<[GestureRecognizer](ts-gesture-common.md#gesturerecognizer12)> | 是 | 响应链上的其他手势识别器对象。 |
| touchRecognizers20+ | Array<[TouchRecognizer](ts-gesture-common.md#touchrecognizer20)> | 否 | 响应链上的Touch识别器对象。 默认值为null，表示在当前手势绑定组件及其子孙组件没有可响应的Touch识别器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GestureJudgeResult](ts-gesture-common.md#gesturejudgeresult11) | 手势是否裁决成功的判定结果。 |

## onTouchTestDone20+

PhonePC/2in1TabletTVWearable

onTouchTestDone(callback: TouchTestDoneCallback): T

提供在[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)结束后，指定手势识别器是否参与后续处理的能力。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TouchTestDoneCallback](ts-gesture-blocking-enhancement.md#touchtestdonecallback20) | 是 | 回调函数，用于指定手势识别器是否参与后续处理。在[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)结束后，开始识别用户手势之前，会触发该回调来动态指定手势识别器是否参与后续处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## TouchTestDoneCallback20+

PhonePC/2in1TabletTVWearable

type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void

动态指定手势识别器是否参与手势处理的回调事件类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [BaseGestureEvent](ts-gesture-common.md#basegestureevent11对象说明) | 是 | [触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)结束后的基础手势事件的信息。  **说明：**  仅包含BaseGestureEvent的信息，不包含其子类拓展信息。  axisHorizontal和axisVertical的值为0。 |
| recognizers | Array<[GestureRecognizer](ts-gesture-common.md#gesturerecognizer12)> | 是 | [触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)结束后，所有手势识别器对象。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（嵌套滚动）

该示例通过shouldBuiltInRecognizerParallelWith和onGestureRecognizerJudgeBegin实现了嵌套滚动的功能。内部组件优先响应滑动手势，当内部组件滑动至顶部或底部时，外部组件能够接替滑动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FatherControlChild {
5. scroller: Scroller = new Scroller();
6. scroller2: Scroller = new Scroller();
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
8. private childRecognizer: GestureRecognizer = new GestureRecognizer();
9. private currentRecognizer: GestureRecognizer = new GestureRecognizer();
10. private lastOffset: number = 0;

12. build() {
13. Stack({ alignContent: Alignment.TopStart }) {
14. Scroll(this.scroller) { // 外部滚动容器
15. Column() {
16. Text("Scroll Area")
17. .width('90%')
18. .height(150)
19. .backgroundColor(0xFFFFFF)
20. .borderRadius(15)
21. .fontSize(16)
22. .textAlign(TextAlign.Center)
23. .margin({ top: 10 })
24. Scroll(this.scroller2) { // 内部滚动容器
25. Column() {
26. Text("Scroll Area2")
27. .width('90%')
28. .height(150)
29. .backgroundColor(0xFFFFFF)
30. .borderRadius(15)
31. .fontSize(16)
32. .textAlign(TextAlign.Center)
33. .margin({ top: 10 })
34. Column() {
35. ForEach(this.arr, (item: number) => {
36. Text(item.toString())
37. .width('90%')
38. .height(150)
39. .backgroundColor(0xFFFFFF)
40. .borderRadius(15)
41. .fontSize(16)
42. .textAlign(TextAlign.Center)
43. .margin({ top: 10 })
44. }, (item: string) => item)
45. }.width('100%')
46. }
47. }
48. .id("inner")
49. .width('100%')
50. .height(800)
51. }.width('100%')
52. }
53. .id("outer")
54. .height(600)
55. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
56. .scrollBar(BarState.On) // 滚动条常驻显示
57. .scrollBarColor(Color.Gray) // 滚动条颜色
58. .scrollBarWidth(10) // 滚动条宽度
59. .edgeEffect(EdgeEffect.None)
60. .shouldBuiltInRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
61. for (let i = 0; i < others.length; i++) {
62. let target = others[i].getEventTargetInfo();
63. if (target) {
64. if (target.getId() == "inner" && others[i].isBuiltIn() &&
65. others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
66. this.currentRecognizer = current; // 保存当前组件的识别器
67. this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
68. return others[i]; // 返回将要组成并行手势的识别器
69. }
70. }
71. }
72. return undefined;
73. })
74. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
75. others: Array<GestureRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
76. if (current) {
77. let target = current.getEventTargetInfo();
78. if (target) {
79. if (target.getId() == "outer" && current.isBuiltIn() &&
80. current.getType() == GestureControl.GestureType.PAN_GESTURE) {
81. if (others) {
82. for (let i = 0; i < others.length; i++) {
83. let target = others[i].getEventTargetInfo() as ScrollableTargetInfo;
84. if (target instanceof ScrollableTargetInfo && target.getId() == "inner") { // 找到响应链上对应并行的识别器
85. let panEvent = event as PanGestureEvent;
86. if (target.isEnd()) { // 根据当前组件状态以及移动方向动态控制识别器使能状态
87. if (panEvent && panEvent.offsetY < 0) {
88. this.childRecognizer.setEnabled(false);
89. this.currentRecognizer.setEnabled(true);
90. } else {
91. this.childRecognizer.setEnabled(true);
92. this.currentRecognizer.setEnabled(false);
93. }
94. } else if (target.isBegin()) {
95. if (panEvent.offsetY > 0) {
96. this.childRecognizer.setEnabled(false);
97. this.currentRecognizer.setEnabled(true);
98. } else {
99. this.childRecognizer.setEnabled(true);
100. this.currentRecognizer.setEnabled(false);
101. }
102. } else {
103. this.childRecognizer.setEnabled(true);
104. this.currentRecognizer.setEnabled(false);
105. }
106. }
107. }
108. }
109. }
110. }
111. }
112. return GestureJudgeResult.CONTINUE;
113. })
114. .parallelGesture( // 绑定一个Pan手势作为动态控制器
115. PanGesture()
116. .onActionUpdate((event: GestureEvent) => {
117. if (this.childRecognizer.getState() != GestureRecognizerState.SUCCESSFUL ||
118. this.currentRecognizer.getState() != GestureRecognizerState.SUCCESSFUL) { // 如果识别器状态不是SUCCESSFUL，则不做控制
119. return;
120. }
121. let target = this.childRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
122. let currentTarget = this.currentRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
123. if (target instanceof ScrollableTargetInfo && currentTarget instanceof ScrollableTargetInfo) {
124. if (target.isEnd()) { // 在移动过程中实时根据当前组件状态，控制识别器的开闭状态
125. if ((event.offsetY - this.lastOffset) < 0) {
126. this.childRecognizer.setEnabled(false);
127. if (currentTarget.isEnd()) {
128. this.currentRecognizer.setEnabled(false);
129. } else {
130. this.currentRecognizer.setEnabled(true);
131. }
132. } else {
133. this.childRecognizer.setEnabled(true);
134. this.currentRecognizer.setEnabled(false);
135. }
136. } else if (target.isBegin()) {
137. if ((event.offsetY - this.lastOffset) > 0) {
138. this.childRecognizer.setEnabled(false);
139. if (currentTarget.isBegin()) {
140. this.currentRecognizer.setEnabled(false);
141. } else {
142. this.currentRecognizer.setEnabled(true);
143. }
144. } else {
145. this.childRecognizer.setEnabled(true);
146. this.currentRecognizer.setEnabled(false);
147. }
148. } else {
149. this.childRecognizer.setEnabled(true);
150. this.currentRecognizer.setEnabled(false);
151. }
152. }
153. this.lastOffset = event.offsetY;
154. })
155. )
156. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
157. }
158. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/s7fsOE7vQNuo77ryb_wjBw/zh-cn_image_0000002589245919.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=C6D7FD58C237F830F44A7BB888E5E8E2533D0A398E07C7E6676ACFA75420F080)

### 示例2（嵌套场景下拦截内部容器手势）

本示例通过将参数exposeInnerGesture设置为true，实现了一级Tabs容器在嵌套二级Tabs的场景下，能够屏蔽二级Tabs内置Swiper的滑动手势，从而触发一级Tabs内置Swiper滑动手势的功能。

开发者自行定义变量来记录内层Tabs的索引值，通过该索引值判断当滑动达到内层Tabs的边界处时，触发回调返回屏蔽使外层Tabs产生滑动手势。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State currentIndex: number = 0;
6. @State selectedIndex: number = 0;
7. @State fontColor: string = '#182431';
8. @State selectedFontColor: string = '#007DFF';
9. innerSelectedIndex: number = 0; // 记录内层Tabs的索引
10. controller?: TabsController = new TabsController();

12. @Builder
13. tabBuilder(index: number, name: string) {
14. Column() {
15. Text(name)
16. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
17. .fontSize(16)
18. .fontWeight(this.selectedIndex === index ? 500 : 400)
19. .lineHeight(22)
20. .margin({ top: 17, bottom: 7 })
21. Divider()
22. .strokeWidth(2)
23. .color('#007DFF')
24. .opacity(this.selectedIndex === index ? 1 : 0)
25. }.width('100%')
26. }

28. build() {
29. Column() {
30. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
31. TabContent() {
32. Column().width('100%').height('100%').backgroundColor(Color.Green)
33. }.tabBar(this.tabBuilder(0, 'green'))

35. TabContent() {
36. Tabs() {
37. TabContent() {
38. Column().width('100%').height('100%').backgroundColor(Color.Blue)
39. }.tabBar(new SubTabBarStyle('blue'))

41. TabContent() {
42. Column().width('100%').height('100%').backgroundColor(Color.Pink)
43. }.tabBar(new SubTabBarStyle('pink'))
44. }
45. .onAnimationStart((index: number, targetIndex: number) => {
46. console.info(`ets onGestureRecognizerJudgeBegin child: ${targetIndex}`)
47. this.innerSelectedIndex = targetIndex
48. })
49. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
50. others: Array<GestureRecognizer>): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
51. console.info('ets onGestureRecognizerJudgeBegin child')
52. if (current) {
53. let target = current.getEventTargetInfo();
54. if (target && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
55. console.info('ets onGestureRecognizerJudgeBegin child PAN_GESTURE')
56. let panEvent = event as PanGestureEvent;
57. if (panEvent && panEvent.velocityX < 0 && this.innerSelectedIndex === 1) { // 内层Tabs滑动到尽头
58. console.info('ets onGestureRecognizerJudgeBegin child reject end')
59. return GestureJudgeResult.REJECT;
60. }
61. if (panEvent && panEvent.velocityX > 0 && this.innerSelectedIndex === 0) { // 内层Tabs滑动到开头
62. console.info('ets onGestureRecognizerJudgeBegin child reject begin')
63. return GestureJudgeResult.REJECT;
64. }
65. }
66. }
67. return GestureJudgeResult.CONTINUE;
68. }, true)
69. }.tabBar(this.tabBuilder(1, 'blue and pink'))

71. TabContent() {
72. Column().width('100%').height('100%').backgroundColor(Color.Brown)
73. }.tabBar(this.tabBuilder(2, 'brown'))
74. }
75. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
76. // 切换动画开始时触发该回调。目标页签显示下划线。
77. this.selectedIndex = targetIndex
78. })
79. }
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/7D7KmyolRwK-a-40iZNoLg/zh-cn_image_0000002558766110.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=FBE287C336283B892E376FE747D7E0CCE02D6BFFEAFA3A4218E083E442A2335B)

### 示例3（拦截手势获取属性）

该示例通过配置onGestureRecognizerJudgeBegin判定手势，获取相应属性参数。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'Gesture';

7. build() {
8. Column() {
9. Column() {
10. Row({ space: 20 }) {
11. Text(this.message)
12. .width('100%')
13. .height(80)
14. .fontSize(23)
15. }.margin(25)
16. }
17. .margin(25)
18. .padding(20)
19. .width('90%')
20. .height(250)
21. .borderWidth(2)
22. .gesture(TapGesture())
23. .gesture(LongPressGesture())
24. .gesture(PanGesture({ direction: PanDirection.Vertical }))
25. .gesture(PinchGesture())
26. .gesture(RotationGesture())
27. .gesture(SwipeGesture({ direction: SwipeDirection.Horizontal }))
28. // 给组件绑定自定义手势识别器判定回调
29. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
30. others: Array<GestureRecognizer>) => {
31. if (current) {
32. // 判断是否为滑动手势
33. if (current.getType() === GestureControl.GestureType.PAN_GESTURE) {
34. let target = current as PanRecognizer;
35. this.message = 'PanGesture\ndistance:' + target.getPanGestureOptions().getDistance() + '\nfingers:' +
36. target.getFingerCount() + '\nisFingerCountLimited:' + target.isFingerCountLimit();
37. }
38. // 判断是否为长按手势
39. if (current.getType() === GestureControl.GestureType.LONG_PRESS_GESTURE) {
40. let target = current as LongPressRecognizer;
41. this.message = 'LongPressGesture\nfingers:' + target.getFingerCount() + '\nisFingerCountLimited:' +
42. target.isFingerCountLimit() + '\nrepeat:' + target.isRepeat() + '\nduration:' + target.getDuration();
43. }
44. // 判断是否为捏合手势
45. if (current.getType() === GestureControl.GestureType.PINCH_GESTURE) {
46. let target = current as PinchRecognizer;
47. this.message = 'PinchGesture\ndistance:' + target.getDistance() + '\nfingers:' +
48. target.getFingerCount() + '\nisFingerCountLimited:' + target.isFingerCountLimit();
49. }
50. // 判断是否为点击手势
51. if (current.getType() === GestureControl.GestureType.TAP_GESTURE) {
52. let target = current as TapRecognizer;
53. this.message = 'TapGesture\ncount:' + target.getTapCount() + '\nfingers:' +
54. target.getFingerCount() + '\nisFingerCountLimited:' + target.isFingerCountLimit();
55. }
56. // 判断是否为旋转手势
57. if (current.getType() === GestureControl.GestureType.ROTATION_GESTURE) {
58. let target = current as RotationRecognizer;
59. this.message = 'RotationGesture\nangle:' + target.getAngle() + '\nfingers:' +
60. target.getFingerCount() + '\nisFingerCountLimited:' + target.isFingerCountLimit();
61. }
62. // 判断是否为快滑手势
63. if (current.getType() === GestureControl.GestureType.SWIPE_GESTURE) {
64. let target = current as SwipeRecognizer;
65. this.message = 'SwipeGesture\ndirection:' + target.getDirection() + '\nfingers:' +
66. target.getFingerCount() + '\nisFingerCountLimited:' + target.isFingerCountLimit() + '\nspeed:' +
67. target.getVelocityThreshold();
68. }
69. }
70. return GestureJudgeResult.CONTINUE;
71. })
72. }
73. .padding(15)
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/uaTZxnarTAq3hj4AQJ2EYg/zh-cn_image_0000002558606452.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=622335C792410CB7D2559EE3E866EBEF462C1834D0B6D590047BE730560536EE)

### 示例4（手势触发成功时取消子组件上的Touch事件）

该示例通过配置onGestureRecognizerJudgeBegin判定手势，在父容器手势触发成功时，调用cancelTouch()强制取消子组件上的Touch事件，实现父子组件手势控制的精准切换。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FatherControlChild {
5. scroller: Scroller = new Scroller();
6. scroller2: Scroller = new Scroller()
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
8. private childRecognizer: GestureRecognizer = new GestureRecognizer();
9. private currentRecognizer: GestureRecognizer = new GestureRecognizer();
10. private lastOffset: number = 0;
11. @State outerState: string = "IDLE";
12. @State innerState: string = "IDLE";
13. @State willCancel: boolean = false;

15. build() {
16. Stack({ alignContent: Alignment.TopStart }) {
17. Scroll(this.scroller) { // 外部滚动容器
18. Column() {
19. Text("Scroll Area")
20. .width('90%')
21. .height(150)
22. .backgroundColor(0xFFFFFF)
23. .borderRadius(15)
24. .fontSize(16)
25. .textAlign(TextAlign.Center)
26. .margin({ top: 10 })

28. Scroll(this.scroller2) { // 内部滚动容器
29. Column() {
30. Text("Scroll Area2")
31. .width('90%')
32. .height(150)
33. .backgroundColor(0xFFFFFF)
34. .borderRadius(15)
35. .fontSize(16)
36. .textAlign(TextAlign.Center)
37. .margin({ top: 10 })

39. Column() {
40. ForEach(this.arr, (item: number) => {
41. Text(item.toString())
42. .width('90%')
43. .height(150)
44. .backgroundColor(0xFFFFFF)
45. .borderRadius(15)
46. .fontSize(16)
47. .textAlign(TextAlign.Center)
48. .margin({ top: 10 })
49. }, (item: string) => item)
50. }.width('100%')
51. }
52. }
53. .id("inner")
54. .width('100%')
55. .height(800)
56. .onTouch((event) => {
57. if (event.type === TouchType.Down) {
58. this.innerState = "TOUCHING";
59. this.willCancel = false;
60. } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
61. if (this.willCancel) {
62. this.innerState = "CANCELLED";
63. setTimeout(() => {
64. this.innerState = "IDLE";
65. this.willCancel = false;
66. }, 1000);
67. } else {
68. this.innerState = "IDLE";
69. }
70. }
71. })
72. }.width('100%')
73. }
74. .id("outer")
75. .height('100%')
76. .scrollable(ScrollDirection.Vertical)
77. .scrollBar(BarState.On)
78. .scrollBarColor(Color.Gray)
79. .scrollBarWidth(10)
80. .edgeEffect(EdgeEffect.None)
81. .shouldBuiltInRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
82. for (let i = 0; i < others.length; i++) {
83. let target = others[i].getEventTargetInfo();
84. if (target) {
85. if (target.getId() == "inner" && others[i].isBuiltIn() &&
86. others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
87. this.currentRecognizer = current; // 保存当前组件的识别器
88. this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
89. return others[i]; // 返回将要组成并行手势的识别器
90. }
91. }
92. }
93. return undefined;
94. })
95. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
96. others: Array<GestureRecognizer>,
97. touchRecognizers?: Array<TouchRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
98. if (current && touchRecognizers) {
99. let target = current.getEventTargetInfo();
100. if (target) {
101. if (target.getId() == "outer" && current.isBuiltIn() &&
102. current.getType() == GestureControl.GestureType.PAN_GESTURE) {
103. return GestureJudgeResult.CONTINUE
104. }
105. for (let index = 0; index < touchRecognizers.length; index++) {
106. const element = touchRecognizers![index];
107. let touchTarget = element.getEventTargetInfo()
108. if (touchTarget && touchTarget.getId() == "inner") {
109. this.willCancel = true;
110. element.cancelTouch();
111. }
112. }
113. }
114. }
115. return GestureJudgeResult.CONTINUE;
116. })
117. .onTouch((event) => {
118. if (event.type === TouchType.Down) {
119. this.outerState = "TOUCHING";
120. } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
121. this.outerState = "IDLE";
122. }
123. })
124. .parallelGesture( // 绑定一个Pan手势作为动态控制器
125. PanGesture()
126. .onActionUpdate((event: GestureEvent) => {
127. if (this.childRecognizer.getState() != GestureRecognizerState.SUCCESSFUL ||
128. this.currentRecognizer.getState() != GestureRecognizerState.SUCCESSFUL) { // 如果识别器状态不是SUCCESSFUL，则不做控制
129. return;
130. }
131. let target = this.childRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
132. let currentTarget = this.currentRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
133. if (target instanceof ScrollableTargetInfo && currentTarget instanceof ScrollableTargetInfo) {
134. if (target.isEnd()) { // 在移动过程中实时根据当前组件状态，控制识别器的开闭状态
135. if ((event.offsetY - this.lastOffset) < 0) {
136. this.childRecognizer.setEnabled(false)
137. if (currentTarget.isEnd()) {
138. this.currentRecognizer.setEnabled(false)
139. } else {
140. this.currentRecognizer.setEnabled(true)
141. }
142. } else {
143. this.childRecognizer.setEnabled(true)
144. this.currentRecognizer.setEnabled(false)
145. }
146. } else if (target.isBegin()) {
147. if ((event.offsetY - this.lastOffset) > 0) {
148. this.childRecognizer.setEnabled(false)
149. if (currentTarget.isBegin()) {
150. this.currentRecognizer.setEnabled(false)
151. } else {
152. this.currentRecognizer.setEnabled(true)
153. }
154. } else {
155. this.childRecognizer.setEnabled(true)
156. this.currentRecognizer.setEnabled(false)
157. }
158. } else {
159. this.childRecognizer.setEnabled(true)
160. this.currentRecognizer.setEnabled(false)
161. }
162. }
163. this.lastOffset = event.offsetY
164. })
165. )

167. Column() { // 外层状态显示
168. Text(`outer: ${this.outerState}`)
169. .fontSize(24)
170. .fontColor(this.outerState === "TOUCHING" ? Color.Green : Color.Gray)
171. .margin({ bottom: 10 })
172. // 内层状态显示
173. Text(`inner: ${this.innerState === "TOUCHING" ? "TOUCHING" : this.innerState}`)
174. .fontSize(24)
175. .fontColor(
176. this.innerState === "TOUCHING" ? Color.Blue :
177. this.innerState === "CANCELLED" ? Color.Red : Color.Gray
178. )
179. }
180. .width('90%')
181. .backgroundColor(Color.White)
182. .border({ width: 1, color: Color.Gray })
183. .position({ x: '5%', y: '80%' })
184. .padding(20)
185. }
186. .width('100%')
187. .height('100%')
188. .backgroundColor(0xDCDCDC)
189. }
190. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/R8dK-EqQQ8KBMajf7bddUA/zh-cn_image_0000002589325979.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=1C71C25F168C623A1F4D3997379A3F62DA704331B341C29127FF1304C00AE064)

### 示例5（自定义手势识别器是否参与手势处理）

从API version 20开始，该示例通过配置[onTouchTestDone](ts-gesture-blocking-enhancement.md#ontouchtestdone20)指定手势识别器不参与后续手势处理，触发回调时，调用[preventBegin](ts-gesture-common.md#preventbegin20)阻止手势识别器参与后续处理。点击Tap2和Tap1的重合区域，不调用preventBegin时，触发Tap2对应的手势；调用preventBegin阻止Tap2时，触发Tap1对应的手势。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TouchTestDoneExample {
5. @State tagList: string[] = ['Null', 'Tap1', 'Tap2', 'Tap3', 'Tap4'];
6. @State tagId: number = 0;
7. @State textValue: string = '';

9. // 多层嵌套场景，为每一层的组件绑定一个Tap手势
10. build() {
11. Column() {
12. Column() {
13. Text('Tap1')
14. .margin(20)
15. Column() {
16. Text('Tap2')
17. .margin(20)
18. Column() {
19. Text('Tap3')
20. .margin(20)
21. Column() {
22. Text('Tap4')
23. .margin(20)
24. }
25. .backgroundColor('#D5D5D5')
26. .width('80%')
27. .height('80%')
28. .gesture(TapGesture().tag('Tap4').onAction(() => {
29. this.textValue = 'Tap4';
30. }))
31. }
32. .backgroundColor('#F7F7F7')
33. .width('80%')
34. .height('80%')
35. .gesture(TapGesture().tag('Tap3').onAction(() => {
36. this.textValue = 'Tap3';
37. }))
38. }
39. .backgroundColor('#707070')
40. .width('80%')
41. .height('80%')
42. .gesture(TapGesture().tag('Tap2').onAction(() => {
43. this.textValue = 'Tap2';
44. }))
45. }
46. .backgroundColor('#D5D5D5')
47. .width('80%')
48. .height('80%')
49. .gesture(TapGesture().tag('Tap1').onAction(() => {
50. this.textValue = 'Tap1';
51. }))
52. // 绑定onTouchTestDone，通过调用手势识别器的preventBegin()方法来自定义手势识别器是否参与后续手势处理
53. .onTouchTestDone((event, recognizers) => {
54. console.info(`event is ${JSON.stringify(event)}`);
55. for (let i = 0; i < recognizers.length; i++) {
56. let recognizer = recognizers[i];
57. console.info(`type is ${JSON.stringify(recognizer.getType())}`)
58. // 根据tag的值屏蔽不同的手势识别器
59. if (recognizer.getTag() == this.tagList[this.tagId]) {
60. recognizer.preventBegin();
61. }
62. }
63. })

65. Text('Current Gesture: ' + this.textValue)
66. .margin(5)

68. Button('Click to change preventGesture')
69. .margin(5)
70. .onClick(() => {
71. this.tagId++;
72. this.tagId %= 5;
73. })
74. Text('Current prevent gesture tag: ' + this.tagList[this.tagId])
75. .margin(5)
76. }
77. .width('100%')
78. .height('100%')
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/_qBEEwCdQgCpiO8lb0CZOw/zh-cn_image_0000002589245921.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=B9D9B1227F741852F8718268D94C1076E353B38ED6403A0F661F6A171DED5DD6)
