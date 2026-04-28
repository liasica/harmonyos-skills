---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-debug
title: UI显示异常调试
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI显示异常调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c458b55cc2eb5d6ea914e241aaa6367f782f7eeb52c900388c7e3fbc832646f1
---

本章节主要介绍UI显示异常问题的调试方法，并结合案例讲解具体的解决步骤。

## 定位UI显示异常问题

UI显示异常问题主要是通过分析UI布局信息来定位。当前分析UI布局主要通过getInspectorTree接口获取组件树信息，或者通过getRectangleById接口获取单个节点的信息。

**组件树**

从API version 9开始，可以使用[getInspectorTree](../harmonyos-references/ts-universal-attributes-component-id.md#getinspectortree9)接口获取组件树及其属性。

**单个节点**

从API version 10开始，可以使用[getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)接口获取组件的大小、位置、平移、缩放、旋转及仿射矩阵等属性信息。

## 解决UI显示异常问题

下面通过具体案例，介绍如何解决UI显示异常问题。

### 通过ComponentUtils.getRectangleById获取的tabBar组件坐标尺寸异常

**问题现象**

在动态控制tabBar显示或隐藏的场景下，通过ComponentUtils.getRectangleById获取的tabBar组件坐标或尺寸可能与预期不符。例如，当tabBar隐藏时（宽度设为0），获取的坐标位于屏幕中央，恢复显示后，该错误坐标仍被沿用。

**可能原因**

* 使用同步接口查询布局信息时，目标节点的宽度临时设置为0，节点布局默认居中显示，导致获取的坐标位于屏幕中央。
* 调用接口时，如果当前布局尚未完成渲染（例如，组件刚被隐藏或显示，布局计算未结束），查询到的将是未更新的旧布局信息。

**解决措施**

* 选择合适的调用时机：在组件完成布局渲染后调用接口。例如，tabBar恢复显示后，使用延迟函数等待布局更新完成，再获取坐标。
* 监听布局变化事件：利用组件的onAreaChange回调，在布局变化并稳定后，触发坐标获取逻辑。
* 增加有效性校验：获取坐标后，校验组件尺寸，过滤无效数据。宽度或高度为0的组件被视为无效。

**代码示例**

```
1. import { ComponentUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Page {
6. @State currentIndex: number = 0;
7. @State msg: string = 'info';
8. @State pivotX: number = 0;
9. @State pivotY: number = 0;
10. @State pivotShow: boolean = false;
11. @State tabBarShow: boolean = true;

13. private controller : TabsController = new TabsController();
14. private uiContext : UIContext | undefined = undefined;
15. private componentUtils : ComponentUtils | undefined = undefined;
16. private componentId : string = 'tab-pink';
17. private flag : boolean = false;
18. private baseX : number = 0;
19. private baseY : number = 0;

21. @Builder
22. tabBuilder(index: number, name: string) {
23. Column() {
24. Text(name)
25. .fontSize(16)
26. .fontWeight(this.currentIndex === index ? 500 : 400)
27. .fontColor(this.currentIndex === index ? '#007DFF': '#182431')
28. .lineHeight(22)
29. }
30. .id(`tab-${name}`)
31. .width('100%')
32. .height('100%')
33. .borderStyle(BorderStyle.Solid)
34. .borderWidth(1)
35. }

37. aboutToAppear(): void {
38. this.uiContext = this.getUIContext();
39. this.componentUtils = this.getUIContext().getComponentUtils();
40. }

42. getRectInfo(id?: string) : string {
43. let componentId : string = id??this.componentId;
44. let info = this.componentUtils?.getRectangleById(componentId);
45. let infoStr : string = '';
46. if (info) {
47. infoStr = 'Size: ' + JSON.stringify(info.size) + ', WindowOffset: ' + JSON.stringify(info.windowOffset);
48. }
49. return infoStr;
50. }

52. getBasePosition() : void {
53. if (this.flag) {
54. return;
55. }
56. let info = this.componentUtils?.getRectangleById('root-stack');
57. if (info) {
58. this.baseX = info.windowOffset.x;
59. this.baseY = info.windowOffset.y;
60. this.msg = `${this.componentId}: ` + this.getRectInfo(this.componentId) + `, pivot: {x: ${this.pivotX}, y: ${this.pivotY}}`;
61. this.flag = true;
62. }
63. }

65. onDidBuild(): void {
66. }

68. build() {
69. Stack() {
70. Column() {
71. Text(this.msg)
72. .fontSize(20)
73. .border({ width: 5, color: Color.Brown })
74. .width('100%')
75. .height('30%')
76. .margin({ top: 50 })
77. Row() {
78. Button('Rect')
79. .onClick(() => {
80. this.msg = JSON.stringify(this.componentUtils?.getRectangleById('tab-pink'))
81. })
82. .width('33%')
83. Button('replay')
84. .onClick(() => {
85. this.pivotShow = false;
86. this.tabBarShow = false;
87. this.pivotShow = true;
88. setTimeout(() => {
89. this.tabBarShow = true
90. }, 100)
91. })
92. .width('33%')
93. Button('pivot')
94. .onClick(() => {
95. this.pivotShow = !this.pivotShow;
96. })
97. .width('33%')
98. }
99. .width('100%')
100. .height('10%')
101. .justifyContent(FlexAlign.SpaceEvenly)
102. Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
103. TabContent() {
104. Column()
105. .width('100%')
106. .height('100%')
107. .backgroundColor('#00CB87')
108. }
109. .tabBar(this.tabBuilder(0, 'green'))
110. TabContent() {
111. Column()
112. .width('100%')
113. .height('100%')
114. .backgroundColor('#007DFF')
115. }
116. .tabBar(this.tabBuilder(1, 'blue'))
117. TabContent() {
118. Column()
119. .width('100%')
120. .height('100%')
121. .backgroundColor('#FFBF00')
122. }
123. .tabBar(this.tabBuilder(2, 'yellow'))
124. .width('25%')
125. TabContent() {
126. Column()
127. .width('100%')
128. .height('100%')
129. .backgroundColor('#E67C92')
130. }
131. .tabBar(this.tabBuilder(3, 'pink'))
132. }
133. .expandSafeArea([SafeAreaType.CUTOUT, SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD],
134. [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
135. .barWidth(this.tabBarShow ? '100%' : 0)
136. .width('100%')
137. .height('40%')
138. .barHeight(44)
139. .vertical(false)
140. .barMode(BarMode.Fixed)
141. .backgroundColor('#F1F2F3')
142. .onChange((index: number) => {
143. this.currentIndex = index;
144. if (index == 3) {
145. this.pivotShow = false;
146. }
147. })
148. .animation({ duration: 100, curve: Curve.Linear })
149. }
150. .id('col')
151. .width('100%')
152. .height('100%')
153. .justifyContent(FlexAlign.SpaceBetween)
154. if (this.pivotShow) {
155. Text('X')
156. .width(18)
157. .height(18)
158. .textAlign(TextAlign.Center)
159. .borderRadius(9)
160. .fontColor(Color.White)
161. .backgroundColor(Color.Red)
162. .position({ x: this.uiContext?.px2vp(this.pivotX), y: this.uiContext?.px2vp(this.pivotY) })
163. .onAreaChange(() => {
164. let info = this.componentUtils?.getRectangleById(this.componentId);
165. if (info) {
166. this.getBasePosition();
167. this.pivotX = info.windowOffset.x - this.baseX;
168. this.pivotY = info.windowOffset.y - this.baseY;
169. this.msg = `${this.componentId}: ` + this.getRectInfo(this.componentId) + `, pivot: {x: ${this.pivotX}, y: ${this.pivotY}}`;
170. }
171. })
172. }
173. }
174. .id('root-stack')
175. }
176. }
```
