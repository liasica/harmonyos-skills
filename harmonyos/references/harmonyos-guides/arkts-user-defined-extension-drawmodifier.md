---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-drawmodifier
title: 自定义绘制修改器 (DrawModifier)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义绘制 > 自定义绘制修改器 (DrawModifier)
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2d04c8979181b768abd8c97c1acb575ff6bfdee58c1343eb5dc42c8bb0273529
---

## 概述

当某些组件本身的绘制内容不满足需求时，可使用组件自定义绘制功能，在原有组件基础上部分绘制、或者全部自行绘制，以达到预期效果。例如：独特的按钮形状、文字和图像混合的图标等。组件自定义绘制提供了自定义绘制修改器DrawModifier，来实现更自由的组件绘制。

## 使用DrawModifier接口

```
1. declare class DrawModifier {

3. drawBehind?(drawContext: DrawContext): void;

5. drawContent?(drawContext: DrawContext): void;

7. drawFront?(drawContext: DrawContext): void;

9. drawForeground?(drawContext: DrawContext): void;

11. drawOverlay(drawContext: DrawContext): void;

13. invalidate(): void;
14. }
```

DrawModifier可设置遮罩层前景（drawOverlay）、前景（drawForeground）、内容前景（drawFront）、内容（drawContent）和内容背景（drawBehind）的绘制方法，开发者需要重载这些方法，并通过[Canvas](arkts-drawing-customization-on-canvas.md)的接口进行自定义绘制。自定义绘制层级图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/8xFdZRh5TUy3F_vZQadQ1A/zh-cn_image_0000002558764516.png?HW-CC-KV=V1&HW-CC-Date=20260429T052818Z&HW-CC-Expire=86400&HW-CC-Sign=2ADDF0E9708F6223555D6B7E75DD74AA9A2C8774CC882C1AF318BA40297C664C)

DrawModifier还提供主动触发重绘的方法invalidate，该接口开发者无需也无法重载，调用会触发所绑定组件的重绘。

说明

* 每个DrawModifier实例只能设置到一个组件上，禁止进行重复设置。
* drawContent方法会替换组件原本的内容绘制函数。
* drawForeground方法从API version 20开始支持。
* drawOverlay方法从API version 23开始支持。
* NDK的自定义绘制能力和示例请参考[自定义绘制](arkts-user-defined-draw.md)。

## 通过drawFront、drawContent、drawBehind进行自定义绘制

通过drawFront、drawContent、drawBehind接口，在内容前景、内容和内容背景三个层级上对Text组件进行了自定义绘制，从而按需改变组件的绘制效果。

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. import { AnimatorResult } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const LOG_PRINT_DOMAIN: number = 0xFF00;
6. const PREFIX: string = '[Sample]'

8. class MyFullDrawModifier extends DrawModifier {
9. public scaleX: number = 1;
10. public scaleY: number = 1;
11. public uiContext: UIContext;

13. constructor(uiContext: UIContext) {
14. super();
15. this.uiContext = uiContext;
16. }

18. // 重载drawBehind方法，实现自定义绘制内容背景。
19. drawBehind(context: DrawContext): void {
20. const brush = new drawing.Brush();
21. brush.setColor({
22. alpha: 255,
23. red: 161,
24. green: 10,
25. blue: 33
26. });
27. context.canvas.attachBrush(brush);
28. const halfWidth = context.size.width / 2;
29. const halfHeight = context.size.height / 2;
30. context.canvas.drawRect({
31. left: this.uiContext.vp2px(halfWidth - 50 * this.scaleX),
32. top: this.uiContext.vp2px(halfHeight - 50 * this.scaleY),
33. right: this.uiContext.vp2px(halfWidth + 50 * this.scaleX),
34. bottom: this.uiContext.vp2px(halfHeight + 50 * this.scaleY)
35. });
36. }

38. // 重载drawContent方法，实现自定义绘制内容。
39. drawContent(context: DrawContext): void {
40. const brush = new drawing.Brush();
41. brush.setColor({
42. alpha: 255,
43. red: 23,
44. green: 169,
45. blue: 141
46. });
47. context.canvas.attachBrush(brush);
48. const halfWidth = context.size.width / 2;
49. const halfHeight = context.size.height / 2;
50. context.canvas.drawRect({
51. left: this.uiContext.vp2px(halfWidth - 30 * this.scaleX),
52. top: this.uiContext.vp2px(halfHeight - 30 * this.scaleY),
53. right: this.uiContext.vp2px(halfWidth + 30 * this.scaleX),
54. bottom: this.uiContext.vp2px(halfHeight + 30 * this.scaleY)
55. });
56. }

58. // 重载drawFront方法，实现自定义绘制内容前景。
59. drawFront(context: DrawContext): void {
60. const brush = new drawing.Brush();
61. brush.setColor({
62. alpha: 255,
63. red: 39,
64. green: 135,
65. blue: 217
66. });
67. context.canvas.attachBrush(brush);
68. const halfWidth = context.size.width / 2;
69. const halfHeight = context.size.height / 2;
70. const radiusScale = (this.scaleX + this.scaleY) / 2;
71. context.canvas.drawCircle(this.uiContext.vp2px(halfWidth), this.uiContext.vp2px(halfHeight),
72. this.uiContext.vp2px(20 * radiusScale));
73. }
74. }

76. class MyFrontDrawModifier extends DrawModifier {
77. public scaleX: number = 1;
78. public scaleY: number = 1;
79. public uiContext: UIContext;

81. constructor(uiContext: UIContext) {
82. super();
83. this.uiContext = uiContext;
84. }

86. // 重载drawFront方法，实现自定义绘制内容前景。
87. drawFront(context: DrawContext): void {
88. const brush = new drawing.Brush();
89. brush.setColor({
90. alpha: 255,
91. red: 39,
92. green: 135,
93. blue: 217
94. });
95. context.canvas.attachBrush(brush);
96. const halfWidth = context.size.width / 2;
97. const halfHeight = context.size.height / 2;
98. const radiusScale = (this.scaleX + this.scaleY) / 2;
99. context.canvas.drawCircle(this.uiContext.vp2px(halfWidth), this.uiContext.vp2px(halfHeight),
100. this.uiContext.vp2px(20 * radiusScale));
101. }
102. }

104. @Entry
105. @Component
106. struct DrawModifierExample {
107. // 将自定义绘制前景的类实例化，传入UIContext实例。
108. private fullModifier: MyFullDrawModifier = new MyFullDrawModifier(this.getUIContext());
109. private frontModifier: MyFrontDrawModifier = new MyFrontDrawModifier(this.getUIContext());
110. private drawAnimator: AnimatorResult | undefined = undefined;
111. @State modifier: DrawModifier = new MyFrontDrawModifier(this.getUIContext());
112. private count = 0;

114. create() {
115. // 设置绘制动画
116. let self = this;
117. this.drawAnimator = this.getUIContext().createAnimator({
118. duration: 1000,
119. easing: 'ease',
120. delay: 0,
121. fill: 'forwards',
122. direction: 'normal',
123. iterations: 1,
124. begin: 0,
125. end: 2
126. });
127. this.drawAnimator.onFrame = (value: number) => {
128. hilog.info(LOG_PRINT_DOMAIN, PREFIX, 'frame value = %{public}', value);
129. const tempModifier = self.modifier as MyFullDrawModifier | MyFrontDrawModifier;
130. tempModifier.scaleX = Math.abs(value - 1);
131. tempModifier.scaleY = Math.abs(value - 1);
132. self.modifier.invalidate();
133. };
134. }

136. build() {
137. Column() {
138. Row() {
139. // $r('app.string.Modifier')需要替换为开发者所需的资源文件
140. Text($r('app.string.Modifier'))
141. .width(100)
142. .height(100)
143. .margin(10)
144. .backgroundColor(Color.Gray)
145. .onClick(() => {
146. // 修改当前绘制大小
147. const tempModifier = this.modifier as MyFullDrawModifier | MyFrontDrawModifier;
148. tempModifier.scaleX -= 0.1;
149. tempModifier.scaleY -= 0.1;
150. })
151. // 调用此接口并传入自定义绘制的类实例，即可实现自定义绘制。
152. .drawModifier(this.modifier)
153. }

155. Row() {
156. Button('create')
157. .width(100)
158. .height(100)
159. .margin(10)
160. .backgroundColor(0xFF2787D9)
161. .onClick(() => {
162. // 创建动画
163. this.create();
164. })
165. Button('play')
166. .id('play')
167. .width(100)
168. .height(100)
169. .margin(10)
170. .backgroundColor(0xFF2787D9)
171. .onClick(() => {
172. // 播放动画
173. if (this.drawAnimator) {
174. this.drawAnimator.play();
175. }
176. })
177. Button('changeModifier')
178. .width(100)
179. .height(100)
180. .margin(10)
181. .backgroundColor(0xFF2787D9)
182. .onClick(() => {
183. // 切换modifier
184. this.count += 1;
185. if (this.count % 2 === 1) {
186. hilog.info(LOG_PRINT_DOMAIN, PREFIX, 'change to full modifier');
187. this.modifier = this.fullModifier;
188. } else {
189. hilog.info(LOG_PRINT_DOMAIN, PREFIX, 'change to front modifier');
190. this.modifier = this.frontModifier;
191. }
192. })
193. }
194. }
195. .width('100%')
196. .height('100%')
197. }
198. }
```

[DrawFrontDrawContentDrawBehind.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DrawModifier/entry/src/main/ets/pages/DrawFrontDrawContentDrawBehind.ets#L16-L215)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/BYk-DpDdQSepBc67zCrW2g/zh-cn_image_0000002558604860.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052818Z&HW-CC-Expire=86400&HW-CC-Sign=A2F38AF04B5CF230B2D2166B8325BB0C35FC3E73668B343CD5BEB0FC203B477B)

## 通过drawForeground进行自定义绘制

通过drawForeground接口，在组件前景层级上对Column组件进行了自定义绘制，从而改变组件前景的绘制效果。

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. class MyForegroundDrawModifier extends DrawModifier {
4. public scaleX: number = 3;
5. public scaleY: number = 3;
6. public uiContext: UIContext;

8. constructor(uiContext: UIContext) {
9. super();
10. this.uiContext = uiContext;
11. }

13. // 重载drawForeground方法，实现自定义绘制前景。
14. drawForeground(context: DrawContext): void {
15. const brush = new drawing.Brush();
16. brush.setColor({
17. alpha: 255,
18. red: 0,
19. green: 50,
20. blue: 100
21. });
22. context.canvas.attachBrush(brush);
23. const halfWidth = context.size.width / 2;
24. const halfHeight = context.size.height / 2;
25. context.canvas.drawRect({
26. left: this.uiContext.vp2px(halfWidth - 30 * this.scaleX),
27. top: this.uiContext.vp2px(halfHeight - 30 * this.scaleY),
28. right: this.uiContext.vp2px(halfWidth + 30 * this.scaleX),
29. bottom: this.uiContext.vp2px(halfHeight + 30 * this.scaleY)
30. });
31. }
32. }

34. @Entry
35. @Component
36. struct DrawModifierExample {
37. // 将自定义绘制前景的类实例化，传入UIContext实例。
38. private foregroundModifier: MyForegroundDrawModifier = new MyForegroundDrawModifier(this.getUIContext());

40. build() {
41. Column() {
42. // $r('app.string.TestNode')需要替换为开发者所需的资源文件。
43. Text($r('app.string.TestNode'))
44. .fontSize(36)
45. .width('100%')
46. .height('100%')
47. .textAlign(TextAlign.Center)
48. }
49. .margin(50)
50. .width(280)
51. .height(300)
52. .backgroundColor(0x87CEEB)
53. // 调用此接口并传入自定义绘制前景的类实例，即可实现自定义绘制前景。
54. .drawModifier(this.foregroundModifier)
55. }
56. }
```

[DrawForeground.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DrawModifier/entry/src/main/ets/pages/DrawForeground.ets#L16-L73)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/CvVAWmxiTqyzqf39eOZ_qQ/zh-cn_image_0000002589324385.png?HW-CC-KV=V1&HW-CC-Date=20260429T052818Z&HW-CC-Expire=86400&HW-CC-Sign=5FA1CB6BA08D7854D77AB3FF3096BFA4DD1E8774F4FA769C1F88A9B40A28E1CC)

## 调整自定义绘制Canvas的变换矩阵

从API version 12开始，通过重写DrawModifier中的[drawContent](../harmonyos-references/ts-universal-attributes-draw-modifier.md#drawcontent)方法，可以替换组件原本的内容绘制函数。

通过[concatMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#concatmatrix12)可以调整自定义绘制画布的变换矩阵。

说明

* [getTotalMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#gettotalmatrix12)获取的是用来记录绘制指令的临时canvas的变换矩阵。
* 如果开发者希望这个画布进行一个预期的变换，应该使用[concatMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#concatmatrix12)而不是[setMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#setmatrix12)，因为setMatrix会覆盖原本真实canvas上存在的变换矩阵。

**ArkTS接口调用示例：**

```
1. import { DrawContext } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. function drawImage(canvas: DrawingCanvas) {
5. let matrix = new drawing.Matrix();
6. matrix.setTranslation(100, 100);
7. canvas.concatMatrix(matrix);
8. const pen = new drawing.Pen();
9. pen.setStrokeWidth(5);
10. pen.setColor({
11. alpha: 255,
12. red: 0,
13. green: 0,
14. blue: 255
15. });
16. canvas.attachPen(pen);
17. const brush = new drawing.Brush();
18. brush.setColor({
19. alpha: 255,
20. red: 0,
21. green: 0,
22. blue: 255
23. });
24. canvas.attachBrush(brush);
25. canvas.drawRect({
26. left: 10,
27. top: 10,
28. right: 110,
29. bottom: 60
30. });
31. canvas.detachPen();
32. }

34. function drawImage1(canvas: DrawingCanvas) {
35. let matrix = new drawing.Matrix();
36. matrix.setTranslation(100, 100);

38. // 1. getTotalMatrix获取的是用来记录绘制指令的临时canvas的变换矩阵
39. // 2. 如果开发者希望这个画布进行一个预期的变换，应该使用concatMatrix而不是setMatrix，因为setMatrix会覆盖原本真实canvas上存在的变换矩阵
40. canvas.getTotalMatrix();
41. canvas.setMatrix(matrix);
42. const pen = new drawing.Pen();
43. pen.setStrokeWidth(5);
44. pen.setColor({
45. alpha: 255,
46. red: 0,
47. green: 0,
48. blue: 255
49. });
50. canvas.attachPen(pen);
51. const brush = new drawing.Brush();
52. brush.setColor({
53. alpha: 255,
54. red: 0,
55. green: 0,
56. blue: 255
57. });
58. canvas.attachBrush(brush);
59. canvas.drawRect({
60. left: 10,
61. top: 10,
62. right: 110,
63. bottom: 60
64. });
65. canvas.detachPen();
66. }

68. class MyDrawModifier1 extends DrawModifier {
69. drawContent(drawContext: DrawContext): void {
70. drawImage1(drawContext.canvas)
71. }
72. }

74. class MyDrawModifier extends DrawModifier {
75. drawContent(drawContext: DrawContext): void {
76. drawImage(drawContext.canvas)
77. }
78. }

80. @Entry
81. @Component
82. struct Index {
83. myDrawModifier: MyDrawModifier = new MyDrawModifier();
84. myDrawModifier1: MyDrawModifier = new MyDrawModifier1();

86. build() {
87. Row() {
88. Column() {
89. Stack().width(300).height(300).drawModifier(this.myDrawModifier).position({ x: 10, y: 10 })
90. }
91. .borderWidth(1)
92. .height(200)
93. .width('45%')

95. Column() {
96. Stack().width(300).height(300).drawModifier(this.myDrawModifier1).position({ x: 10, y: 10 })
97. }
98. .borderWidth(1)
99. .height(200)
100. .width('45%')
101. }.height('100%')
102. .width('100%').position({ x: 10, y: 10 })

104. }
105. }
```

[Canvas.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DrawModifier/entry/src/main/ets/pages/Canvas.ets#L16-L122)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/1TEvykwRSf6tazUzek-xtg/zh-cn_image_0000002589244325.png?HW-CC-KV=V1&HW-CC-Date=20260429T052818Z&HW-CC-Expire=86400&HW-CC-Sign=43DFF0AA9990FC64B49CD10554E304246F28CADBAF8680DBEDE1E4E0CD7A3580)
