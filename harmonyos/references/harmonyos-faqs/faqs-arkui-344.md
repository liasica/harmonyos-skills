---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-344
title: 如何在Tabs的tabBar中添加其他组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在Tabs的tabBar中添加其他组件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:aeb6845098c6505d50c14f9f9ee5f7f891c15614db83de75ada0a5c01bec0dec
---

标准Tabs组件不支持在tabBar中添加其他组件，但通过自定义Tabs可实现该需求。

示例代码如下：

```
1. import { componentUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TabsDemo {
6. @State tabArray: Array<number> = [0, 1, 2];
7. @State lastTabIndex: number = this.tabArray.length - 1;
8. @State currentIndex: number = 0;
9. @State animationDuration: number = 300;
10. @State indicatorLeftMargin: number = 0;
11. @State indicatorWidth: number = 0;
12. private controller: TabsController = new TabsController();
13. private tabsWidth: number = 0;

15. // Single tab
16. @Builder
17. tab(tabName: string, tabItem: number, tabIndex: number) {
18. Row({ space: 20 }) {
19. Text(tabName).fontSize(18)
20. .fontColor(tabItem === this.currentIndex ? Color.Red : Color.Black)
21. .id(tabIndex.toString())
22. .onAreaChange((oldValue: Area, newValue: Area) => {
23. if (this.currentIndex === tabIndex && (this.indicatorLeftMargin === 0 || this.indicatorWidth === 0)) {
24. if (newValue.position.x !== undefined) {
25. let positionX = Number.parseFloat(newValue.position.x.toString());
26. this.indicatorLeftMargin = Number.isNaN(positionX) ? 0 : positionX;
27. }
28. let width = Number.parseFloat(newValue.width.toString());
29. this.indicatorWidth = Number.isNaN(width) ? 0 : width;
30. }
31. })
32. }
33. .justifyContent(FlexAlign.Center)
34. .constraintSize({ minWidth: 35 })
35. .width(80)
36. .height(35)
37. .borderRadius({
38. topLeft: 10,
39. topRight: 10
40. })
41. .onClick(() => {
42. this.controller.changeIndex(tabIndex);
43. this.currentIndex = tabIndex;
44. })
45. }

47. build() {
48. Column() {
49. // Tab bar
50. Stack({ alignContent: Alignment.TopStart }) {
51. Scroll() {
52. Row() {
53. ForEach(this.tabArray, (item: number, index: number) => {
54. this.tab('Tab' + item, item, index);
55. })
56. Text('+')
57. .width(36)
58. .height(50)
59. .fontSize(28)
60. .borderRadius(5)
61. .padding({
62. left: 5,
63. bottom: 2
64. })
65. .onClick(() => {
66. if (this.tabArray.length < 1000) {
67. this.tabArray.push(++this.lastTabIndex);
68. }
69. })
70. }
71. .justifyContent(FlexAlign.SpaceBetween)
72. }
73. .align(Alignment.Start)
74. .scrollable(ScrollDirection.Horizontal)
75. .scrollBar(BarState.Off)
76. .width('100%')

78. Column()
79. .width(this.indicatorWidth)
80. .height(2)
81. .backgroundColor(Color.Red)
82. .borderRadius(2)
83. .margin({
84. left: this.indicatorLeftMargin,
85. top: 38
86. })
87. }
88. .width('100%')

90. Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
91. ForEach(this.tabArray, (item: number, index: number) => {
92. TabContent() {
93. Text('I am the content of page ' + item)
94. .height(300)
95. .width('100%')
96. .fontSize(30)
97. .textAlign(TextAlign.Center)
98. }
99. .backgroundColor(Color.Pink)
100. })
101. }
102. .onAreaChange((oldValue: Area, newValue: Area) => {
103. let width = Number.parseFloat(newValue.width.toString());
104. this.tabsWidth = Number.isNaN(width) ? 0 : width;
105. })
106. .barWidth('100%')
107. .barHeight(0)
108. .width('100%')
109. .height('100%')
110. .backgroundColor('#F1F3F5')
111. .animationDuration(this.animationDuration)
112. .onChange((index: number) => {
113. this.currentIndex = index; // Listen for index changes to switch tab content.
114. })
115. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
116. // Callback when the switching animation starts. The underline slides with the page and the width changes.
117. this.currentIndex = targetIndex;
118. let targetIndexInfo = this.getTextInfo(targetIndex);
119. this.startAnimateTo(this.animationDuration, targetIndexInfo.left, targetIndexInfo.width);
120. })
121. .onAnimationEnd((index: number, event: TabsAnimationEvent) => {
122. // Callback when the switching animation ends. The underline animation stops.
123. let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
124. this.startAnimateTo(0, currentIndicatorInfo.left, currentIndicatorInfo.width);
125. })
126. .onGestureSwipe((index: number, event: TabsAnimationEvent) => {
127. // Callback triggered frame by frame during page swipe.
128. let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
129. this.currentIndex = currentIndicatorInfo.index;
130. this.indicatorLeftMargin = currentIndicatorInfo.left;
131. this.indicatorWidth = currentIndicatorInfo.width;
132. })
133. }
134. .height('100%')
135. }

137. // Get component size, position, translation, scaling, rotation, and affine matrix attribute information.
138. private getTextInfo(index: number): Record<string, number> {
139. let modePosition: componentUtils.ComponentInfo =
140. this.getUIContext().getComponentUtils().getRectangleById(index.toString());
141. return {
142. 'left': this.getUIContext().px2vp(modePosition?.windowOffset?.x ?? 0),
143. 'width': this.getUIContext().px2vp(modePosition.size.width)
144. };
145. }

147. /*
148. * Calculate indicator dynamic position information
149. * @param index Current page index
150. * @param event Swipe event object
151. * @returns {left: Indicator left shift, width: Indicator width, index: Target page index}
152. */
153. private getCurrentIndicatorInfo(index: number, event: TabsAnimationEvent): Record<string, number> {
154. let nextIndex = index;
155. if (index > 0 && event.currentOffset > 0) {
156. nextIndex--;
157. } else if (index < 3 && event.currentOffset < 0) {
158. nextIndex++;
159. }
160. let indexInfo = this.getTextInfo(index);
161. let nextIndexInfo = this.getTextInfo(nextIndex);
162. let swipeRatio = Math.abs(event.currentOffset / this.tabsWidth);
163. // When page sliding exceeds half, tabBar switches to the next page.
164. let currentIndex = swipeRatio > 0.5 ? nextIndex : index;
165. let currentLeft = indexInfo.left + (nextIndexInfo.left - indexInfo.left) * swipeRatio;
166. let currentWidth = indexInfo.width + (nextIndexInfo.width - indexInfo.width) * swipeRatio;
167. return { 'index': currentIndex, 'left': currentLeft, 'width': currentWidth };
168. }

170. private startAnimateTo(duration: number, leftMargin: number, width: number) {
171. this.getUIContext().animateTo({
172. // Animation duration
173. duration: duration,
174. // Animation curve
175. curve: Curve.Linear,
176. // Number of iterations
177. iterations: 1,
178. // Animation mode
179. playMode: PlayMode.Normal,
180. onFinish: () => {
181. console.info('play end');
182. }
183. }, () => {
184. this.indicatorLeftMargin = leftMargin;
185. this.indicatorWidth = width;
186. })
187. }
188. }
```

[AddComponentInTabbar.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/AddComponentInTabbar.ets#L21-L209)
