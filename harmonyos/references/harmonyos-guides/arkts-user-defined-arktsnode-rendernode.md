---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-rendernode
title: 自定义渲染节点 (RenderNode)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 自定义渲染节点 (RenderNode)
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:104903202411a4d8f2898f51aa9871ab1c9443d3cac3b2d055e00a001efe2885
---

## 概述

对于不具备自己的渲染环境的三方框架，尽管已实现前端解析、布局及事件处理等功能，但仍需依赖系统的基础渲染和动画能力。[FrameNode](arkts-user-defined-arktsnode-framenode.md)上的通用属性与通用事件对这类框架而言是冗余的，会导致多次不必要的操作，涵盖布局、事件处理等逻辑。

自定义渲染节点 ([RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md))是更加轻量的渲染节点，仅具备与渲染相关的功能。它提供了设置基础渲染属性的能力，以及节点的动态添加、删除和自定义绘制的能力。RenderNode能够为第三方框架提供基础的渲染和动画支持。

## 创建和删除节点

RenderNode提供了节点创建和删除的能力。可以通过RenderNode的构造函数创建自定义的RenderNode节点。通过构造函数创建的节点对应一个实体的节点。同时，可以通过RenderNode中的[dispose](../harmonyos-references/js-apis-arkui-rendernode.md#dispose12)接口来实现与实体节点的绑定关系的解除。

## 操作节点树

RenderNode提供了节点的增、删、查、改的能力，能够修改节点的子树结构；可以对所有RenderNode的节点的父子节点做出查询操作，并返回查询结果。

说明

* RenderNode中获取的子树结构由开发通过RenderNode的[appendChild](../harmonyos-references/js-apis-arkui-rendernode.md#appendchild)接口传入的参数构建。
* RenderNode如果要与系统直接结合显示，需通过FrameNode中获取的RenderNode进行挂载上树。

```
1. import { FrameNode, NodeController, RenderNode } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. const TEST_TAG: string = 'RenderNode';
7. const renderNode = new RenderNode();
8. renderNode.frame = {
9. x: 0,
10. y: 0,
11. width: 200,
12. height: 350
13. };
14. renderNode.backgroundColor = 0xffff0000;
15. for (let i = 0; i < 5; i++) {
16. const node = new RenderNode();
17. // 设置node节点的Frame大小
18. node.frame = {
19. x: 10,
20. y: 10 + 60 * i,
21. width: 50,
22. height: 50
23. };
24. // 设置node节点的背景颜色
25. node.backgroundColor = 0xff00ff00;
26. // 将新增节点挂载在renderNode上
27. renderNode.appendChild(node);
28. }

30. class MyNodeController extends NodeController {
31. private rootNode: FrameNode | null = null;

33. makeNode(uiContext: UIContext): FrameNode | null {
34. this.rootNode = new FrameNode(uiContext);

36. const rootRenderNode = this.rootNode?.getRenderNode();
37. if (rootRenderNode) {
38. rootRenderNode.appendChild(renderNode);
39. }
40. return this.rootNode;
41. }
42. }

44. @Entry
45. @Component
46. export struct OperationNodeTree {
47. private myNodeController: MyNodeController = new MyNodeController();
48. @State myLog: string = '';

50. build() {
51. // ...
52. Column() {
53. NodeContainer(this.myNodeController)
54. .width(200)
55. .height(350);
56. Text(this.myLog).width(300).height(40).margin({ top: 20, left: 20, bottom: 20 });
57. Button('getNextSibling')
58. .onClick(() => {
59. const child = renderNode.getChild(1);
60. const nextSibling = child!.getNextSibling()
61. if (child === null || nextSibling === null) {
62. hilog.info(DOMAIN, TEST_TAG, ' the child or nextChild is null');
63. this.myLog = 'the child or nextChild is null';
64. } else {
65. // 获取子节点的位置信息
66. hilog.info(DOMAIN, TEST_TAG, `the position of child is x: ${child.position.x}, y: ${child.position.y}, ` +
67. `the position of nextSibling is x: ${nextSibling.position.x}, y: ${nextSibling.position.y}`);
68. this.myLog = `the position of child is x: ${child.position.x}, y: ${child.position.y}, ` +
69. `the position of nextSibling is x: ${nextSibling.position.x}, y: ${nextSibling.position.y}`;
70. }
71. });
72. }.width(300).margin({ left: 20 });

74. // ...
75. }
76. }
```

[OperationNodeTree.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/ets/pages/OperationNodeTree.ets#L16-L97)

## 设置和获取渲染相关属性

RenderNode中可以设置渲染相关的属性，包括：[backgroundColor](../harmonyos-references/js-apis-arkui-rendernode.md#backgroundcolor)，[clipToFrame](../harmonyos-references/js-apis-arkui-rendernode.md#cliptoframe)，[opacity](../harmonyos-references/js-apis-arkui-rendernode.md#opacity)，[size](../harmonyos-references/js-apis-arkui-rendernode.md#size)，[position](../harmonyos-references/js-apis-arkui-rendernode.md#position)，[frame](../harmonyos-references/js-apis-arkui-rendernode.md#frame)，[pivot](../harmonyos-references/js-apis-arkui-rendernode.md#pivot)，[scale](../harmonyos-references/js-apis-arkui-rendernode.md#scale)，[translation](../harmonyos-references/js-apis-arkui-rendernode.md#translation)，[rotation](../harmonyos-references/js-apis-arkui-rendernode.md#rotation)，[transform](../harmonyos-references/js-apis-arkui-rendernode.md#transform)，[shadowColor](../harmonyos-references/js-apis-arkui-rendernode.md#shadowcolor)，[shadowOffset](../harmonyos-references/js-apis-arkui-rendernode.md#shadowoffset)，[shadowAlpha](../harmonyos-references/js-apis-arkui-rendernode.md#shadowalpha)，[shadowElevation](../harmonyos-references/js-apis-arkui-rendernode.md#shadowelevation)，[shadowRadius](../harmonyos-references/js-apis-arkui-rendernode.md#shadowradius)，[borderStyle](../harmonyos-references/js-apis-arkui-rendernode.md#borderstyle12)，[borderWidth](../harmonyos-references/js-apis-arkui-rendernode.md#borderwidth12)，[borderColor](../harmonyos-references/js-apis-arkui-rendernode.md#bordercolor12)，[borderRadius](../harmonyos-references/js-apis-arkui-rendernode.md#borderradius12)，[shapeMask](../harmonyos-references/js-apis-arkui-rendernode.md#shapemask12)，[shapeClip](../harmonyos-references/js-apis-arkui-rendernode.md#shapeclip12)，[markNodeGroup](../harmonyos-references/js-apis-arkui-rendernode.md#marknodegroup12)等。具体属性支持范围参考[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)接口说明。

说明

* RenderNode中获取的属性为设置的属性值。
* 若未传入参数或者传入参数为非法值则查询获得的为默认值。
* 不建议对BuilderNode中的RenderNode进行修改操作。BuilderNode中具体属性设置是由状态管理实现的，属性更新的时序开发者不可控，BuilderNode和FrameNode中同时设置RenderNode属性可能会导致RenderNode属性设置与预期不相符。

```
1. import { RenderNode, FrameNode, NodeController, ShapeMask, ShapeClip } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. const TEST_TAG: string = 'RenderNode';
7. const mask = new ShapeMask();
8. mask.setRectShape({
9. left: 0,
10. right: 150,
11. top: 0,
12. bottom: 150
13. });
14. mask.fillColor = 0X55FF0000;
15. mask.strokeColor = 0XFFFF0000;
16. mask.strokeWidth = 24;

18. const clip = new ShapeClip();
19. clip.setCommandPath({ commands: 'M100 0 L0 100 L50 200 L150 200 L200 100 Z' });

21. const renderNode = new RenderNode();
22. renderNode.backgroundColor = 0xff519db4;
23. renderNode.size = { width: 100, height: 100 };

25. class MyNodeController extends NodeController {
26. private rootNode: FrameNode | null = null;

28. makeNode(uiContext: UIContext): FrameNode | null {
29. this.rootNode = new FrameNode(uiContext);

31. const rootRenderNode = this.rootNode.getRenderNode();
32. if (rootRenderNode !== null) {
33. rootRenderNode.appendChild(renderNode);
34. }

36. return this.rootNode;
37. }
38. }

40. @Entry
41. @Component
42. export struct RenderingProperties {
43. private myNodeController: MyNodeController = new MyNodeController();

45. build() {
46. // ...
47. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
48. Column() {
49. NodeContainer(this.myNodeController).height(260);
50. };

52. Flex() {
53. // 设置RenderNode的位置
54. Button('position')
55. .width(300)
56. .onClick(() => {
57. renderNode.position = { x: 10, y: 10 };
58. hilog.info(DOMAIN, TEST_TAG, ' position:' + JSON.stringify(renderNode.position));
59. });
60. Column().width(20);
61. // 设置RenderNode的轴心
62. Button('pivot')
63. .width(300)
64. .onClick(() => {
65. renderNode.pivot = { x: 0.5, y: 0.6 };
66. hilog.info(DOMAIN, TEST_TAG, ' pivot:' + JSON.stringify(renderNode.pivot));
67. });
68. }

70. Flex() {
71. // 修改RenderNode的缩放比例
72. Button('scale')
73. .width(300)
74. .onClick(() => {
75. renderNode.scale = { x: 0.5, y: 1 };
76. hilog.info(DOMAIN, TEST_TAG, ' scale:' + JSON.stringify(renderNode.scale));
77. });
78. Column().width(20);
79. // 设置RenderNode的平移量
80. Button('translation')
81. .width(300)
82. .onClick(() => {
83. renderNode.translation = { x: 100, y: 0 };
84. hilog.info(DOMAIN, TEST_TAG, ' translation:' + JSON.stringify(renderNode.translation));
85. });
86. }

88. Flex() {
89. // 设置RenderNode的旋转角度
90. Button('rotation')
91. .width(300)
92. .onClick(() => {
93. renderNode.rotation = { x: 45, y: 0, z: 0 };
94. hilog.info(DOMAIN, TEST_TAG, ' rotation:' + JSON.stringify(renderNode.rotation));
95. });
96. Column().width(20);
97. // 设置RenderNode的变换矩阵
98. Button('transform')
99. .width(300)
100. .onClick(() => {
101. renderNode.transform = [
102. 1, 0, 0, 0,
103. 0, 2, 0, 0,
104. 0, 0, 1, 0,
105. 0, 0, 0, 1
106. ];
107. hilog.info(DOMAIN, TEST_TAG, ' transform:' + JSON.stringify(renderNode.transform));
108. });
109. }

111. Flex() {
112. // 设置RenderNode的阴影属性
113. Button('shadow')
114. .width(300)
115. .onClick(() => {
116. renderNode.shadowElevation = 10; // 设置阴影的光照高度
117. renderNode.shadowColor = 0xff2787d9;
118. renderNode.shadowOffset = { x: 10, y: 10 };
119. renderNode.shadowAlpha = 0.1;
120. hilog.info(DOMAIN, TEST_TAG, ' shadowElevation:' + JSON.stringify(renderNode.shadowElevation));
121. hilog.info(DOMAIN, TEST_TAG, ' shadowColor:' + JSON.stringify(renderNode.shadowColor));
122. hilog.info(DOMAIN, TEST_TAG, ' shadowOffset:' + JSON.stringify(renderNode.shadowOffset));
123. hilog.info(DOMAIN, TEST_TAG, ' shadowAlpha:' + JSON.stringify(renderNode.shadowAlpha));
124. });
125. Column().width(20);
126. // 设置RenderNode的阴影模糊半径
127. Button('shadowRadius')
128. .width(300)
129. .onClick(() => {
130. renderNode.shadowOffset = { x: 10, y: 10 };
131. renderNode.shadowAlpha = 0.7;
132. renderNode.shadowRadius = 30;
133. hilog.info(DOMAIN, TEST_TAG, ' shadowOffset:' + JSON.stringify(renderNode.shadowOffset));
134. hilog.info(DOMAIN, TEST_TAG, ' shadowAlpha:' + JSON.stringify(renderNode.shadowAlpha));
135. hilog.info(DOMAIN, TEST_TAG, ' shadowRadius:' + JSON.stringify(renderNode.shadowRadius));
136. });
137. }

139. Flex() {
140. // 设置RenderNode的边框样式
141. Button('border')
142. .width(300)
143. .onClick(() => {
144. renderNode.borderWidth = {
145. left: 8,
146. top: 8,
147. right: 8,
148. bottom: 8
149. };
150. renderNode.borderStyle = {
151. left: BorderStyle.Solid,
152. top: BorderStyle.Dotted,
153. right: BorderStyle.Dashed,
154. bottom: BorderStyle.Solid
155. }
156. renderNode.borderColor = {
157. left: 0xffd5d5d5,
158. top: 0xffd5d5d5,
159. right: 0xffd5d5d5,
160. bottom: 0xffd5d5d5
161. };
162. renderNode.borderRadius = {
163. topLeft: 32,
164. topRight: 32,
165. bottomLeft: 32,
166. bottomRight: 32
167. };
168. hilog.info(DOMAIN, TEST_TAG, ' borderWidth:' + JSON.stringify(renderNode.borderWidth));
169. hilog.info(DOMAIN, TEST_TAG, ' borderStyle:' + JSON.stringify(renderNode.borderStyle));
170. hilog.info(DOMAIN, TEST_TAG, ' borderColor:' + JSON.stringify(renderNode.borderColor));
171. hilog.info(DOMAIN, TEST_TAG, ' borderRadius:' + JSON.stringify(renderNode.borderRadius));
172. })
173. Column().width(20);
174. // 设置RenderNode的遮罩
175. Button('shapeMask')
176. .width(300)
177. .onClick(() => {
178. renderNode.shapeMask = mask;
179. hilog.info(DOMAIN, TEST_TAG, ' shapeMask:' + JSON.stringify(renderNode.shapeMask));
180. });
181. }

183. // 设置RenderNode的剪裁形状
184. Button('shapeClip')
185. .width(300)
186. .onClick(() => {
187. renderNode.shapeClip = clip;
188. hilog.info(DOMAIN, TEST_TAG, ' shapeClip:' + JSON.stringify(renderNode.shapeClip));
189. });
190. }
191. .padding({
192. left: 35,
193. right: 35,
194. top: 35,
195. bottom: 35
196. })
197. .width('100%')
198. .height('100%');

200. // ...
201. }
202. }
```

[RenderingProperties.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/ets/pages/RenderingProperties.ets#L16-L218)

## 自定义绘制

通过重写RenderNode中的[draw](../harmonyos-references/js-apis-arkui-rendernode.md#draw)方法，可以自定义RenderNode的绘制内容，通过[invalidate](../harmonyos-references/js-apis-arkui-rendernode.md#invalidate)接口可以主动触发节点的重新绘制。

说明

* 同时同步触发多个invalidate仅会触发一次重新绘制。
* 自定义绘制有两种绘制方式：通过ArkTS接口进行调用和通过Node-API进行调用。

**ArkTS接口调用示例：**

```
1. import { FrameNode, NodeController, RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. class MyRenderNode extends RenderNode {
8. public width: number = 200;

10. draw(context: DrawContext) {
11. // 获取canvas对象
12. const canvas = context.canvas;
13. // 创建笔刷
14. const brush = new drawing.Brush();
15. // 设置笔刷颜色
16. brush.setColor({
17. alpha: 255,
18. red: 81,
19. green: 157,
20. blue: 180
21. });
22. canvas.attachBrush(brush);
23. // 绘制矩阵
24. canvas.drawRect({
25. left: 0,
26. right: this.width,
27. top: 0,
28. bottom: 200
29. });
30. canvas.detachBrush();
31. hilog.info(DOMAIN, 'testTag', `RenderNode draw width = ${this.width}`);
32. }
33. }

35. const renderNode = new MyRenderNode();
36. renderNode.frame = {
37. x: 0,
38. y: 0,
39. width: 300,
40. height: 300
41. };
42. renderNode.backgroundColor = 0xffd5d5d5;
43. renderNode.opacity = 0.5;

45. class MyNodeController extends NodeController {
46. private rootNode: FrameNode | null = null;

48. makeNode(uiContext: UIContext): FrameNode | null {
49. this.rootNode = new FrameNode(uiContext);

51. const rootRenderNode = this.rootNode?.getRenderNode();
52. if (rootRenderNode !== null) {
53. rootRenderNode.frame = {
54. x: 0,
55. y: 0,
56. width: 500,
57. height: 500
58. };
59. rootRenderNode.appendChild(renderNode);
60. }

62. return this.rootNode;
63. }
64. }

66. @Entry
67. @Component
68. export struct CustomDraw {
69. private myNodeController: MyNodeController = new MyNodeController();

71. build() {
72. // ...
73. Column() {
74. NodeContainer(this.myNodeController)
75. .width('100%').height(320);
76. Button('Invalidate')
77. .onClick(() => {
78. // 同步调用多次，仅触发一次重绘，draw回调中的日志仅打印一次
79. renderNode.width += 10;
80. renderNode.invalidate();
81. renderNode.invalidate();
82. }).margin({left: -80});
83. };

85. // ...
86. }
87. }
```

[CustomDraw.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/ets/pages/CustomDraw.ets#L16-L113)

## 调整自定义绘制Canvas的变换矩阵

从API version 12开始，通过重写RenderNode中的[draw](../harmonyos-references/js-apis-arkui-rendernode.md#draw)方法，可以自定义RenderNode的绘制内容。

通过[concatMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#concatmatrix12)可以调整自定义绘制Canvas的变换矩阵。

说明

* [getTotalMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#gettotalmatrix12)获取的是用来记录绘制指令的临时canvas的变换矩阵。
* 如果开发者希望对画布进行预期的变换，应使用[concatMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#concatmatrix12)而不是[setMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#setmatrix12)，因为setMatrix会覆盖原本真实canvas上存在的变换矩阵。

**ArkTS接口调用示例：**

```
1. import { NodeController, UIContext, RenderNode, DrawContext, FrameNode } from '@kit.ArkUI';
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
13. green: 74,
14. blue: 175
15. });
16. canvas.attachPen(pen);
17. const brush = new drawing.Brush();
18. brush.setColor({
19. alpha: 255,
20. red: 0,
21. green: 74,
22. blue: 175
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
37. // 1. getTotalMatrix获取的是用来记录绘制指令的临时canvas的变换矩阵
38. // 2. 如果开发者希望这个画布进行一个预期的变换，应该使用concatMatrix而不是setMatrix，因为setMatrix会覆盖原本真实canvas上存在的变换矩阵
39. canvas.getTotalMatrix();
40. canvas.setMatrix(matrix);
41. const pen = new drawing.Pen();
42. pen.setStrokeWidth(5);
43. pen.setColor({
44. alpha: 255,
45. red: 0,
46. green: 74,
47. blue: 175
48. });
49. canvas.attachPen(pen);
50. const brush = new drawing.Brush();
51. brush.setColor({
52. alpha: 255,
53. red: 0,
54. green: 74,
55. blue: 175
56. });
57. canvas.attachBrush(brush);
58. canvas.drawRect({
59. left: 10,
60. top: 10,
61. right: 110,
62. bottom: 60
63. });
64. canvas.detachPen();
65. }

67. class MyRenderNode extends RenderNode {
68. draw(context: DrawContext): void {
69. drawImage(context.canvas);
70. }
71. }

73. class MyRenderNode1 extends RenderNode {
74. draw(context: DrawContext): void {
75. drawImage1(context.canvas);
76. }
77. }

79. class MyNodeController extends NodeController {
80. makeNode(uiContext: UIContext): FrameNode | null {
81. const rootNode: FrameNode = new FrameNode(uiContext);
82. rootNode.commonAttribute.width(300).height(300);
83. const theRenderNode: MyRenderNode = new MyRenderNode();
84. theRenderNode.frame = {
85. x: 10,
86. y: 100,
87. width: 100,
88. height: 50
89. };
90. theRenderNode.backgroundColor = 0xFF2787D9;
91. rootNode.getRenderNode()?.appendChild(theRenderNode);
92. return rootNode;
93. }
94. }

96. class MyNodeController1 extends NodeController {
97. makeNode(uiContext: UIContext): FrameNode | null {
98. const rootNode: FrameNode = new FrameNode(uiContext);
99. rootNode.commonAttribute.width(300).height(300);
100. const theRenderNode: MyRenderNode1 = new MyRenderNode1();
101. theRenderNode.frame = {
102. x: 10,
103. y: 100,
104. width: 100,
105. height: 50
106. };
107. theRenderNode.backgroundColor = 0xFF2787D9;
108. rootNode.getRenderNode()?.appendChild(theRenderNode);
109. return rootNode;
110. }
111. }

113. @Entry
114. @Component
115. export struct CustomDrawCanvas {
116. myNodeController: MyNodeController = new MyNodeController();
117. myNodeController1: MyNodeController1 = new MyNodeController1();

119. build() {
120. // ...
121. Row() {
122. Column() {
123. NodeContainer(this.myNodeController)
124. }
125. .height('100%')
126. .width('45%');

128. Column() {
129. NodeContainer(this.myNodeController1)
130. }
131. .height('100%')
132. .width('45%');
133. };

135. // ...
136. }
137. }
```

[CustomDrawCanvas.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/ets/pages/CustomDrawCanvas.ets#L16-L163)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/zzFlXtRQSQSQD6yEG6vXWw/zh-cn_image_0000002558764500.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=86C0C42217C71CC3B11D21B5C53DD348CC430AF0234F936E7F9A3A42B8AF3AA7)

**Node-API调用示例：**

C++侧可通过Node-API来获取Canvas，并进行后续的自定义绘制操作。

```
1. // native_bridge.cpp
2. #include "napi/native_api.h"
3. #include <native_drawing/drawing_canvas.h>
4. #include <native_drawing/drawing_color.h>
5. #include <native_drawing/drawing_path.h>
6. #include <native_drawing/drawing_pen.h>

8. namespace {
9. const int32_t ARG_NUM0 = 0;
10. const int32_t ARG_NUM1 = 1;
11. const int32_t ARG_NUM2 = 2;
12. const int32_t ARG_NUM3 = 3;
13. const int32_t ARG_NUM4 = 4;
14. }

16. static napi_value OnDraw(napi_env env, napi_callback_info info)
17. {
18. size_t argc = ARG_NUM4;
19. napi_value args[ARG_NUM4] = {nullptr};
20. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

22. int32_t id;
23. napi_get_value_int32(env, args[ARG_NUM0], &id);

25. // 获取 Canvas 指针
26. void *temp = nullptr;
27. napi_unwrap(env, args[ARG_NUM1], &temp);
28. OH_Drawing_Canvas *canvas = reinterpret_cast<OH_Drawing_Canvas *>(temp);

30. // 获取 Canvas 宽度
31. int32_t width;
32. napi_get_value_int32(env, args[ARG_NUM2], &width);

34. // 获取 Canvas 高度
35. int32_t height;
36. napi_get_value_int32(env, args[ARG_NUM3], &height);

38. const float kQuarter = 0.25f;
39. const float kThreeQuarters  = 0.75f;
40. // 传入canvas、height、width等信息至绘制函数中进行自定义绘制
41. auto path = OH_Drawing_PathCreate();
42. OH_Drawing_PathMoveTo(path, width * kQuarter, height * kQuarter);
43. OH_Drawing_PathLineTo(path, width * kThreeQuarters, height * kQuarter);
44. OH_Drawing_PathLineTo(path, width * kThreeQuarters, height * kThreeQuarters);
45. OH_Drawing_PathLineTo(path, width * kQuarter, height * kThreeQuarters);
46. OH_Drawing_PathLineTo(path, width * kQuarter, height * kQuarter);
47. OH_Drawing_PathClose(path);

49. auto pen = OH_Drawing_PenCreate();
50. const int lineWidth = 10;
51. OH_Drawing_PenSetWidth(pen, lineWidth);
52. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0x00, 0x00));
53. OH_Drawing_CanvasAttachPen(canvas, pen);

55. OH_Drawing_CanvasDrawPath(canvas, path);

57. return nullptr;
58. }

60. EXTERN_C_START
61. static napi_value Init(napi_env env, napi_value exports)
62. {
63. napi_property_descriptor desc[] = {
64. {"nativeOnDraw", nullptr, OnDraw, nullptr, nullptr, nullptr, napi_default, nullptr}};
65. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
66. return exports;
67. }
68. EXTERN_C_END

70. static napi_module demoModule = {
71. .nm_version = 1,
72. .nm_flags = 0,
73. .nm_filename = nullptr,
74. .nm_register_func = Init,
75. .nm_modname = "entry",
76. .nm_priv = ((void *)0),
77. .reserved = {0},
78. };

80. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
81. {
82. napi_module_register(&demoModule);
83. }
```

[NativeBridge.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/cpp/NativeBridge.cpp#L16-L100)

修改工程中的src/main/cpp/CMakeLists.txt文件，添加如下内容：

```
1. # the minimum version of CMake.
2. cmake_minimum_required(VERSION 3.4.1)
3. project(NapiTest)

5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

7. include_directories(${NATIVERENDER_ROOT_PATH}
8. ${NATIVERENDER_ROOT_PATH}/include)

10. add_library(entry SHARED NativeBridge.cpp)
11. target_link_libraries(entry PUBLIC libace_napi.z.so)
12. target_link_libraries(entry PUBLIC libace_ndk.z.so)
13. target_link_libraries(entry PUBLIC libnative_drawing.so)
```

同时在工程中的src/main/cpp/types/libentry/index.d.ts文件中，添加自定义绘制函数在ArkTS侧的定义，如：

```
1. import { DrawContext } from '@kit.ArkUI'

3. export const nativeOnDraw: (id: number, context: DrawContext, width: number, height: number) => number;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L20)

ArkTS侧代码：

```
1. import bridge from 'libentry.so'; // 该 so 由 Node-API 编写并生成
2. import { DrawContext, FrameNode, NodeController, RenderNode } from '@kit.ArkUI';

4. class MyRenderNode extends RenderNode {
5. private uiContext: UIContext;

7. constructor(uiContext: UIContext) {
8. super();
9. this.uiContext = uiContext;
10. }

12. draw(context: DrawContext) {
13. // 需要将 context 中的宽度和高度从vp转换为px
14. bridge.nativeOnDraw(0, context, this.uiContext.vp2px(context.size.height),
15. this.uiContext.vp2px(context.size.width));
16. }
17. }

19. class MyNodeController extends NodeController {
20. private rootNode: FrameNode | null = null;

22. makeNode(uiContext: UIContext): FrameNode | null {
23. this.rootNode = new FrameNode(uiContext);

25. const rootRenderNode = this.rootNode.getRenderNode();
26. if (rootRenderNode !== null) {
27. const renderNode = new MyRenderNode(uiContext);
28. renderNode.size = { width: 100, height: 100 };
29. rootRenderNode.appendChild(renderNode);
30. }
31. return this.rootNode;
32. }
33. }

35. @Entry
36. @Component
37. export struct CustomDrawCanvasNative {
38. private myNodeController: MyNodeController = new MyNodeController();

40. build() {
41. // ...
42. Row() {
43. NodeContainer(this.myNodeController);
44. };

46. // ...
47. }
48. }
```

[CustomDrawCanvasNative.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/ets/pages/CustomDrawCanvasNative.ets#L16-L74)

## 设置标签

开发者可利用[label](../harmonyos-references/js-apis-arkui-rendernode.md#label12)接口向RenderNode设置标签信息，这有助于在节点Inspector中更清晰地区分各节点。

```
1. import { RenderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. class MyNodeController extends NodeController {
7. private rootNode: FrameNode | null = null;

9. makeNode(uiContext: UIContext): FrameNode | null {
10. this.rootNode = new FrameNode(uiContext);
11. const renderNode: RenderNode | null = this.rootNode.getRenderNode();
12. if (renderNode !== null) {
13. const renderChildNode: RenderNode = new RenderNode();
14. renderChildNode.frame = {
15. x: 0,
16. y: 0,
17. width: 100,
18. height: 100
19. };
20. renderChildNode.backgroundColor = 0xff519db4;
21. renderChildNode.label = 'customRenderChildNode';
22. hilog.info(DOMAIN, 'label:', renderChildNode.label);
23. renderNode.appendChild(renderChildNode);
24. }

26. return this.rootNode;
27. }
28. }

30. @Entry
31. @Component
32. export struct SetLabel {
33. private myNodeController: MyNodeController = new MyNodeController();

35. build() {
36. // ...
37. Column() {
38. NodeContainer(this.myNodeController)
39. .width(300)
40. .height(700)
41. .backgroundColor(0xffd5d5d5);
42. };

44. // ...
45. }
46. }
```

[SetLabel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/ets/pages/SetLabel.ets#L16-L72)

## 查询当前RenderNode是否解除引用

前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。在ArkUI框架中，前端节点是在ArkTS代码层面创建的节点，负责与开发者交互；后端节点是在ArkUI框架底层维护的实体节点，负责具体逻辑的处理。

从API version 20开始，使用[isDisposed](../harmonyos-references/js-apis-arkui-rendernode.md#isdisposed20)接口查询当前RenderNode对象是否已解除与后端实体节点的引用关系，从而可以在操作节点前检查其有效性，避免潜在风险。

```
1. import { NodeController, FrameNode, RenderNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. private rootNode: FrameNode | null = null;
5. private renderNode: RenderNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. this.rootNode = new FrameNode(uiContext);
9. this.renderNode = new RenderNode();
10. this.renderNode.size = { width: 300, height: 300 };
11. this.renderNode.backgroundColor = 0xffd5d5d5;

13. // 挂载RenderNode
14. this.rootNode.getRenderNode()?.appendChild(this.renderNode);
15. return this.rootNode;
16. }

18. disposeRenderNode() {
19. // 解除RenderNode与后端实体节点的引用关系
20. this.renderNode?.dispose();
21. }

23. isDisposed(): string {
24. if (this.renderNode !== null) {
25. // 查询RenderNode是否解除引用
26. if (this.renderNode.isDisposed()) {
27. return 'renderNode isDisposed is true';
28. } else {
29. return 'renderNode isDisposed is false';
30. }
31. }
32. return 'renderNode is null';
33. }
34. }

36. @Entry
37. @Component
38. export struct CheckRanderNodeDisposed {
39. @State text: string = '';
40. private myNodeController: MyNodeController = new MyNodeController();

42. build() {
43. // ...
44. Column({ space: 4 }) {
45. NodeContainer(this.myNodeController);
46. Button('RenderNode dispose')
47. .onClick(() => {
48. this.myNodeController.disposeRenderNode();
49. this.text = '';
50. })
51. .width(200)
52. .height(50);
53. Button('RenderNode isDisposed')
54. .onClick(() => {
55. this.text = this.myNodeController.isDisposed();
56. })
57. .width(200)
58. .height(50);
59. Text(this.text)
60. .fontSize(25);
61. }
62. .width('100%')
63. .height('100%');

65. // ...
66. }
67. }
```

[CheckRanderNodeDisposed.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomRenderNode/entry/src/main/ets/pages/CheckRanderNodeDisposed.ets#L16-L93)
