---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-nested-scrolling
title: Web组件嵌套滚动
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > Web组件嵌套滚动
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c148bb39a244a770671173d62fd95d8f59826d7f2e203cce0033f825daf2553
---

Web组件嵌套滚动的典型应用场景为，在页面中，多个独立区域需进行滚动，当用户滚动Web区域内容时，可联动其他滚动区域，实现上下左右全方位滑动页面的嵌套滚动体验。内嵌于可滚动容器（[Grid](../harmonyos-references/ts-container-grid.md)、[List](../harmonyos-references/ts-container-list.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[Swiper](../harmonyos-references/ts-container-swiper.md)、[Tabs](../harmonyos-references/ts-container-tabs.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)、[Refresh](../harmonyos-references/ts-container-refresh.md)、[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)）中的Web组件，接收到滑动手势事件后，需要设置ArkUI的[NestedScrollMode](../harmonyos-references/ts-appendix-enums.md#nestedscrollmode10)枚举属性，实现Web组件与ArkUI可滚动容器的嵌套滚动。

Web组件嵌套滚动可通过[方案1：使用nestedScroll属性实现嵌套滚动](web-nested-scrolling.md#使用nestedscroll属性实现嵌套滚动)或[方案2：滚动偏移量由滚动父组件统一派发](web-nested-scrolling.md#滚动偏移量由滚动父组件统一派发)两个方案实现，方案的选择应取决于应用嵌套滚动的具体业务场景。如果只是简单的Web组件与其他父组件联动滚动建议通过方案1实现；如果应用需要自定义控制Web组件和其他滚动组件滚动，以及一些复杂场景建议使用方案2。

说明

如果Web组件用到了全量展开的场景（layoutMode为WebLayoutMode.FIT\_CONTENT），需要显式指明渲染模式(RenderMode.SYNC\_RENDER)，详见[layoutMode](../harmonyos-references/arkts-basic-components-web-attributes.md#layoutmode11)。

## 使用nestedScroll属性实现嵌套滚动

使用Web组件[nestedScroll](../harmonyos-references/arkts-basic-components-web-attributes.md#nestedscroll11)属性来设置上下左右四个方向，或者设置向前、向后两个方向的嵌套滚动模式，实现与父组件的滚动联动，同时也允许在过程中动态改变嵌套滚动的模式。

**完整代码**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @ComponentV2
5. struct NestedScroll {
6. private scrollerForScroll: Scroller = new Scroller();
7. private listScroller: Scroller = new Scroller();
8. controller: webview.WebviewController = new webview.WebviewController();
9. @Local arr: Array<number> = [];

11. aboutToAppear(): void {
12. for (let i = 0; i < 10; i++) {
13. this.arr.push(i);
14. }
15. }

17. build() {
18. Scroll(this.scrollerForScroll) {
19. Column() {
20. Web({ src: $rawfile('scroll.html'), controller: this.controller })
21. .nestedScroll({
22. scrollUp: NestedScrollMode.PARENT_FIRST, // 向上滚动父组件优先
23. scrollDown: NestedScrollMode.SELF_FIRST, // 向下滚动子组件优先
24. }).height('100%')
25. Repeat<number>(this.arr)
26. .each((item: RepeatItem<number>) => {
27. Text('Scroll Area')
28. .width('100%')
29. .height('40%')
30. .backgroundColor(0x330000FF)
31. .fontSize(16)
32. .textAlign(TextAlign.Center)
33. })
34. }
35. }
36. }
37. }
```

[ImpNestedScroll.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageInteracts/entry/src/main/ets/pages/ImpNestedScroll.ets#L16-L54)

加载的html文件。

```
1. <!-- scroll.html -->
2. <!DOCTYPE html>
3. <html>

5. <head>
6. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
7. <style>
8. .blue {
9. background-color: lightblue;
10. }

12. .green {
13. background-color: lightgreen;
14. }

16. .blue,
17. .green {
18. font-size: 16px;
19. height: 200px;
20. text-align: center;
21. /* 水平居中 */
22. line-height: 200px;
23. /* 垂直居中（值等于容器高度） */
24. }
25. </style>
26. </head>

28. <body>
29. <div class="blue">webArea</div>
30. <div class="green">webArea</div>
31. <div class="blue">webArea</div>
32. <div class="green">webArea</div>
33. <div class="blue">webArea</div>
34. <div class="green">webArea</div>
35. <div class="blue">webArea</div>
36. </body>

38. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/WT9AgFXLSvuZuODbxAqKAg/zh-cn_image_0000002583478215.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=0593D43E8CE5F31D43472ACE61557A55FF0051955EAB4397224B5C5E04F6EA98)

## 滚动偏移量由滚动父组件统一派发

**实现思路**

1. 手指向上滑动：

   (1) 如果Web页面没有滚动到底部，Scroll组件将滚动偏移量派发给Web，Scroll组件自身不滚动。

   (2) 如果Web页面滚动至底部，而Scroll组件尚未滚动至底部，则仅Scroll组件自身滚动，不向Web组件和List组件派发滚动偏移量。

   (3) 如果Scroll组件滚动到底部，则滚动偏移量派发给List组件，Scroll组件自身不滚动。
2. 手指向下滑动：

   (1) 如果List组件没有滚动到顶部，则Scroll组件将滚动偏移量派发给List组件，Scroll组件自身不滚动。

   (2) 当List组件滚动至顶部，而Scroll组件未到达顶部时，Scroll组件将自行滚动，滚动偏移量不会派发给List组件和Web组件。

   (3) 如果Scroll组件滚动到顶部，则滚动偏移量派发给Web，Scroll组件自身不滚动。

**关键实现**

1. 如何禁用Web组件滚动手势。

   (1) 首先调用Web组件滚动控制器方法，设置Web禁用触摸（[setScrollable](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setscrollable12)）的滚动。

   ```
   1. this.webController.setScrollable(false, webview.ScrollType.EVENT);
   ```

   (2) 再使用[onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13)方法，禁止Web组件自带的滚动手势触发。

   ```
   1. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer, otherArray<GestureRecognizer>) => {
   2. if (current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
   3. return GestureJudgeResult.REJECT;
   4. }
   5. return GestureJudgeResult.CONTINUE;
   6. })
   ```
2. 如何禁用[List](../harmonyos-references/ts-container-list.md)组件的手势。

   ```
   1. .enableScrollInteraction(false)
   ```
3. 如何检测List组件、Scroll组件是否滚动到边界。

   (1) 滚动到上边界：scroller.currentOffset().yOffset <= 0;

   (2) 滚动到下边界：scroller.isAtEnd() == true;
4. 如何检测Web组件是否滚动到边界。

   (1) 获取Web组件自身高度、内容高度和当前滚动偏移量来判定。

   (2) 判断Web组件是否滚动到顶部：webController.getPageOffset().y == 0;

   (3) 判断Web组件是否滚动到底部：webController.getPageOffset().y + this.webHeight >= webController.getPageHeight();

   (4) 获取Web组件自身高度：webController.[getPageHeight()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getpageheight);

   (5) 获取Web组件窗口高度：webController?.[runJavaScriptExt](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)('window.innerHeight');

   (6) 获取Web组件的滚动偏移量：webController.[getPageOffset()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getpageoffset20);
5. 如何让Scroll组件不滚动。

   Scroll组件绑定[onScrollFrameBegin](../harmonyos-references/ts-container-scroll.md#onscrollframebegin9)事件，将剩余滚动偏移量返回0，Scroll组件就不滚动，也不会停止惯性滚动动画。
6. 滚动偏移量如何派发给List组件。

   ```
   1. this.listScroller.scrollBy(0, offset)
   ```
7. 滚动偏移量如何派发给Web组件。

   ```
   1. this.webController.scrollBy(0, offset)
   ```
8. 设置Web组件[bypassVsyncCondition](../harmonyos-references/arkts-basic-components-web-attributes.md#bypassvsynccondition20)为WebBypassVsyncCondition.SCROLLBY\_FROM\_ZERO\_OFFSET，加快Web组件首帧滚动绘制。

   ```
   1. .bypassVsyncCondition(WebBypassVsyncCondition.SCROLLBY_FROM_ZERO_OFFSET)
   ```

**完整代码**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @ComponentV2
5. struct Index {
6. private scroller: Scroller = new Scroller()
7. private listScroller: Scroller = new Scroller()
8. private webController: webview.WebviewController = new webview.WebviewController()
9. private isWebAtEnd: boolean = false
10. private webHeight: number = 0
11. @Local arr: Array<number> = []

13. aboutToAppear(): void {
14. for (let i = 0; i < 10; i++) {
15. this.arr.push(i)
16. }
17. }

19. getWebHeight() {
20. try {
21. this.webController?.runJavaScriptExt('window.innerHeight',
22. (error, result) => {
23. if (error || !result) {
24. return;
25. }
26. if (result.getType() === webview.JsMessageType.NUMBER) {
27. this.webHeight = result.getNumber()
28. }
29. })
30. } catch (error) {
31. }
32. }

34. checkScrollBottom() {
35. this.isWebAtEnd = false;
36. if (this.webController.getPageOffset().y + this.webHeight >= this.webController.getPageHeight()) {
37. this.isWebAtEnd = true;
38. }
39. }

41. build() {
42. Scroll(this.scroller) {
43. Column() {
44. Web({
45. src: $rawfile('scroll.html'),
46. controller: this.webController,
47. }).height('100%')
48. .bypassVsyncCondition(WebBypassVsyncCondition.SCROLLBY_FROM_ZERO_OFFSET)
49. .onPageEnd(() => {
50. this.webController.setScrollable(false, webview.ScrollType.EVENT);
51. this.getWebHeight();
52. })
53. // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
54. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
55. others: Array<GestureRecognizer>) => {
56. if (current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
57. return GestureJudgeResult.REJECT;
58. }
59. return GestureJudgeResult.CONTINUE;
60. })
61. List({ scroller: this.listScroller }) {
62. Repeat<number>(this.arr)
63. .each((item: RepeatItem<number>) => {
64. ListItem() {
65. Text('Scroll Area')
66. .width('100%')
67. .height('40%')
68. .backgroundColor(0x330000FF)
69. .fontSize(16)
70. .textAlign(TextAlign.Center)
71. }
72. })
73. }.height('100%')
74. .maintainVisibleContentPosition(true)
75. .enableScrollInteraction(false)
76. }
77. }
78. .onScrollFrameBegin((offset: number, state: ScrollState) => {
79. this.checkScrollBottom();
80. if (offset > 0) {
81. if (!this.isWebAtEnd) {
82. this.webController.scrollBy(0, offset)
83. return { offsetRemain: 0 }
84. } else if (this.scroller.isAtEnd()) {
85. this.listScroller.scrollBy(0, offset)
86. return { offsetRemain: 0 }
87. }
88. } else if (offset < 0) {
89. if (this.listScroller.currentOffset().yOffset > 0) {
90. this.listScroller.scrollBy(0, offset)
91. return { offsetRemain: 0 }
92. } else if (this.scroller.currentOffset().yOffset <= 0) {
93. this.webController.scrollBy(0, offset)
94. return { offsetRemain: 0 }
95. }
96. }
97. return { offsetRemain: offset }
98. })
99. }
100. }
```

[WebNestedScroll.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageInteracts/entry/src/main/ets/pages/WebNestedScroll.ets#L16-L118)

加载的html文件。

```
1. <!-- scroll.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
6. <style>
7. .blue {
8. background-color: lightblue;
9. }
10. .green {
11. background-color: lightgreen;
12. }
13. .blue, .green {
14. font-size:16px;
15. height:200px;
16. text-align: center;       /* 水平居中 */
17. line-height: 200px;       /* 垂直居中（值等于容器高度） */
18. }
19. </style>
20. </head>
21. <body>
22. <div class="blue" >webArea</div>
23. <div class="green">webArea</div>
24. <div class="blue">webArea</div>
25. <div class="green">webArea</div>
26. <div class="blue">webArea</div>
27. <div class="green">webArea</div>
28. <div class="blue">webArea</div>
29. </body>
30. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/9PGLcZ_-SSONWe20Bhlfqg/zh-cn_image_0000002552798566.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=E09A08F606DAD2F878EDB19F722BCC457A0145A388E93818DBEECC6B557F6D0A)

## 示例代码

* [Web组件嵌套滑动](https://gitcode.com/harmonyos_samples/web-scroller)
