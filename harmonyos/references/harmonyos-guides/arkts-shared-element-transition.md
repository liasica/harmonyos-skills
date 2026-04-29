---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shared-element-transition
title: 共享元素转场 (一镜到底)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 转场动画 > 共享元素转场 (一镜到底)
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62cd02ec4d7e3bd477be5533cac4cefb96738e3a89a27e22f7eb35dee4dc0eab
---

共享元素转场是一种界面切换时对相同或者相似的两个元素做的一种位置和大小匹配的过渡动画效果，也称一镜到底动效。

如下例所示，在点击图片后，该图片消失，同时在另一个位置出现新的图片，二者之间内容相同，可以对它们添加一镜到底动效。左图为不添加一镜到底动效的效果，右图为添加一镜到底动效的效果，一镜到底的效果能够让二者的出现消失产生联动，使得内容切换过程显得灵动自然而不生硬。

| 一帧切换效果 | 一镜到底效果 |
| --- | --- |
|  |  |

一镜到底的动效有多种实现方式，在实际开发过程中，应根据具体场景选择合适的方法进行实现。

以下是不同实现方式的对比：

| 一镜到底实现方式 | 特点 | 适用场景 |
| --- | --- | --- |
| 不新建容器直接变化原容器 | 不发生路由跳转，需要在一个组件中实现展开及关闭两种状态的布局，展开后组件层级不变。 | 适用于转场开销小的简单场景，如点开页面无需加载大量数据及组件。 |
| 新建容器并跨容器迁移组件 | 通过使用NodeController，将组件从一个容器迁移到另一个容器，在开始迁移时，需要根据前后两个布局的位置大小等信息对组件添加位移及缩放，确保迁移开始时组件能够对齐初始布局，避免出现视觉上的跳变现象。之后再添加动画将位移及缩放等属性复位，实现组件从初始布局到目标布局的一镜到底过渡效果。 | 适用于新建对象开销大的场景，如视频直播组件点击转为全屏等。 |
| 使用geometryTransition共享元素转场 | 利用系统能力，转场前后两个组件调用geometryTransition接口绑定同一id，同时将转场逻辑置于animateTo动画闭包内，这样系统侧会自动为二者添加一镜到底的过渡效果。 | 系统将调整绑定的两个组件的宽高及位置至相同值，并切换二者的透明度，以实现一镜到底过渡效果。因此，为了实现流畅的动画效果，需要确保对绑定geometryTransition的节点添加宽高动画不会有跳变。此方式适用于创建新节点开销小的场景。 |

## 不新建容器并直接变化原容器

该方法不新建容器，通过在已有容器上增删组件触发[transition](../harmonyos-references/ts-transition-animation-component.md)，搭配组件[属性动画](arkts-attribute-animation-apis.md)实现一镜到底效果。

对于同一个容器展开，容器内兄弟组件消失或者出现的场景，可通过对同一个容器展开前后进行宽高位置变化并配置属性动画，对兄弟组件配置出现消失转场动画实现一镜到底效果。基本步骤为：

1. 构建需要展开的页面，并通过状态变量构建好普通状态和展开状态的界面。
2. 将需要展开的页面展开，通过状态变量控制兄弟组件消失或出现，并通过绑定出现消失转场实现兄弟组件转场效果。

以点击卡片后显示卡片内容详情场景为例：

```
1. import { common } from '@kit.AbilityKit';

3. class PostData {
4. // 请将$r('app.media.flower')替换为实际资源文件
5. avatar: Resource = $r('app.media.flower');
6. name: string = '';
7. message: ResourceStr = '';
8. images: Resource[] = [];
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State isExpand: boolean = false;
15. @State @Watch('onItemClicked') selectedIndex: number = -1;
16. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. // 数组中图片均使用Resource资源，需用户自定义
18. private allPostData: PostData[] = [
19. {
20. // 请将$r('app.media.flower')替换为实际资源文件
21. avatar: $r('app.media.flower'),
22. name: 'Alice',
23. // 请将$r('app.string.shareTransition_text1')替换为实际资源文件，在本示例中该资源文件的value值为"天气晴朗"
24. message: $r('app.string.shareTransition_text1'),
25. // 请将$r('app.media.spring')替换为实际资源文件
26. // 请将$r('app.media.tall_tree')替换为实际资源文件
27. images: [$r('app.media.spring'), $r('app.media.tall_tree')]
28. },
29. {
30. // 请将$r('app.media.sunset_sky')替换为实际资源文件
31. avatar: $r('app.media.sunset_sky'),
32. name: 'Bob',
33. // 请将$r('app.string.shareTransition_text2')替换为实际资源文件，在本示例中该资源文件的value值为"你好世界"
34. message: $r('app.string.shareTransition_text2'),
35. // 请将$r('app.media.island')替换为实际资源文件
36. images: [$r('app.media.island')]
37. },
38. {
39. // 请将$r('app.media.tall_tree')替换为实际资源文件
40. avatar: $r('app.media.tall_tree'),
41. name: 'Carl',
42. // 请将$r('app.string.shareTransition_text3')替换为实际资源文件，在本示例中该资源文件的value值为"万物生长"
43. message: $r('app.string.shareTransition_text3'),
44. // 请将$r('app.media.flower')替换为实际资源文件
45. // 请将$r('app.media.sunset_sky')替换为实际资源文件
46. // 请将$r('app.media.spring')替换为实际资源文件
47. images: [$r('app.media.flower'), $r('app.media.sunset_sky'), $r('app.media.spring')]
48. }];

50. private onItemClicked(): void {
51. if (this.selectedIndex < 0) {
52. return;
53. }
54. this.getUIContext()?.animateTo({
55. duration: 350,
56. curve: Curve.Friction
57. }, () => {
58. this.isExpand = !this.isExpand;
59. });
60. }

62. build() {
63. Column({ space: 20 }) {
64. ForEach(this.allPostData, (postData: PostData, index: number) => {
65. // 当点击了某个post后，会使其余的post消失下树
66. if (!this.isExpand || this.selectedIndex === index) {
67. Column() {
68. Post({ data: postData, selectedIndex: this.selectedIndex, index: index })
69. }
70. .width('100%')
71. // 对出现消失的post添加透明度转场和位移转场效果
72. .transition(TransitionEffect.OPACITY
73. .combine(TransitionEffect.translate({ y: index < this.selectedIndex ? -250 : 250 }))
74. .animation({ duration: 350, curve: Curve.Friction }))
75. }
76. }, (postData: PostData, index: number) => index.toString())
77. }
78. .size({ width: '100%', height: '100%' })
79. .backgroundColor('#40808080')
80. }
81. }

83. @Component
84. export default struct Post {
85. @Link selectedIndex: number;
86. @Prop data: PostData;
87. @Prop index: number;
88. @State itemHeight: number = 250;
89. @State isExpand: boolean = false;
90. @State expandImageSize: number = 100;
91. @State avatarSize: number = 50;

93. build() {
94. Column({ space: 20 }) {
95. Row({ space: 10 }) {
96. Image(this.data.avatar)
97. .size({ width: this.avatarSize, height: this.avatarSize })
98. .borderRadius(this.avatarSize / 2)
99. .clip(true)

101. Text(this.data.name)
102. }
103. .justifyContent(FlexAlign.Start)

105. Text(this.data.message)

107. Row({ space: 15 }) {
108. ForEach(this.data.images, (imageResource: Resource, index: number) => {
109. Image(imageResource)
110. .size({ width: this.expandImageSize, height: this.expandImageSize })
111. }, (imageResource: Resource, index: number) => index.toString())
112. }

114. // 展开态下组件增加的内容
115. if (this.isExpand) {
116. Column() {
117. // 请将$r('app.string.shareTransition_text4')替换为实际资源文件，在本示例中该资源文件的value值为"评论区"
118. Text($r('app.string.shareTransition_text4'))
119. // 对评论区文本添加出现消失转场效果
120. .transition(TransitionEffect.OPACITY
121. .animation({ duration: 350, curve: Curve.Friction }))
122. .padding({ top: 10 })
123. }
124. .transition(TransitionEffect.asymmetric(
125. TransitionEffect.opacity(0.99)
126. .animation({ duration: 350, curve: Curve.Friction }),
127. TransitionEffect.OPACITY.animation({ duration: 0 })
128. ))
129. .size({ width: '100%' })
130. }
131. }
132. .backgroundColor(Color.White)
133. .size({ width: '100%', height: this.itemHeight })
134. .alignItems(HorizontalAlign.Start)
135. .padding({ left: 10, top: 10 })
136. .onClick(() => {
137. this.selectedIndex = -1;
138. this.selectedIndex = this.index;
139. this.getUIContext()?.animateTo({
140. duration: 350,
141. curve: Curve.Friction
142. }, () => {
143. // 对展开的post做宽高动画，并对头像尺寸和图片尺寸加动画
144. this.isExpand = !this.isExpand;
145. this.itemHeight = this.isExpand ? 780 : 250;
146. this.avatarSize = this.isExpand ? 75 : 50;
147. this.expandImageSize = (this.isExpand && this.data.images.length > 0)
148. ? (360 - (this.data.images.length + 1) * 15) / this.data.images.length : 100;
149. })
150. })
151. }
152. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template2/Index.ets#L16-L170)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/KSXF96bWR9K7gkIQrIm6iA/zh-cn_image_0000002558604822.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=E0FFB9480395C8A50CE2037455DF604E2D9EA40A415CE36BA447425A9A6E022A)

## 新建容器并跨容器迁移组件

通过[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)[自定义占位节点](arkts-user-defined-place-holder.md)，利用[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)实现组件的跨节点迁移，配合属性动画给组件的迁移过程赋予一镜到底效果。这种一镜到底的实现方式可以结合多种转场方式使用，如导航转场（[Navigation](../harmonyos-references/ts-basic-components-navigation.md)）、半模态转场（[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)）等。

### 结合Stack使用

可以利用Stack内后定义组件位于最上方的特性，控制组件在跨节点迁移后的顺序位置最高。以展开收起卡片的场景为例，实现步骤为：

* 展开卡片时，获取被点击卡片A的位置信息，将被点击卡片A迁移到与卡片A位置一致的展开页B处，展开页B的层级高于被点击卡片A的层级。
* 对展开页B添加属性动画，使之展开并运动到展开后的位置，完成一镜到底的动画效果。
* 收起卡片时，对展开页B添加属性动画，使之收起并运动到收起时的位置，即被点击卡片A的位置，实现一镜到底的动画效果。
* 在动画结束回调函数中将展开页B中的组件迁移回被点击卡片A处。

```
1. // Index.ets
2. import { createPostNode, getPostNode, PostNode } from './PostNode';
3. import { componentUtils, curves, UIContext } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. // 新建一镜到底动画类
9. private uiContext: UIContext = this.getUIContext();
10. @State animationProperties: AnimationProperties = new AnimationProperties(this.uiContext);
11. private listArray: Array<number> = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

13. build() {
14. // 卡片折叠态，展开态的共同父组件
15. Stack() {
16. List({ space: 20 }) {
17. ForEach(this.listArray, (item: number) => {
18. ListItem() {
19. // 卡片折叠态
20. PostItem({ index: item, animationProperties: this.animationProperties })
21. }
22. })
23. }
24. .clip(false)
25. .alignListItem(ListItemAlign.Center)

27. if (this.animationProperties.isExpandPageShow) {
28. // 卡片展开态
29. ExpandPage({ animationProperties: this.animationProperties })
30. }
31. }
32. .key('rootStack')
33. .enabled(this.animationProperties.isEnabled)
34. }
35. }

37. @Component
38. struct PostItem {
39. @Prop index: number
40. @Link animationProperties: AnimationProperties;
41. @State nodeController: PostNode | undefined = undefined;
42. // 折叠时详细内容隐藏
43. private showDetailContent: boolean = false;

45. aboutToAppear(): void {
46. this.nodeController = createPostNode(this.getUIContext(), this.index.toString(), this.showDetailContent);
47. if (this.nodeController != undefined) {
48. // 设置回调，当卡片从展开态回到折叠态时触发
49. this.nodeController.setCallback(this.resetNode.bind(this));
50. }
51. }

53. resetNode() {
54. this.nodeController = getPostNode(this.index.toString());
55. }

57. build() {
58. Stack() {
59. NodeContainer(this.nodeController)
60. }
61. .width('100%')
62. .height(100)
63. .key(this.index.toString())
64. .onClick(() => {
65. if (this.nodeController != undefined) {
66. // 卡片从折叠态节点下树
67. this.nodeController.onRemove();
68. }
69. // 触发卡片从折叠到展开态的动画
70. this.animationProperties.expandAnimation(this.index);
71. })
72. }
73. }

75. @Component
76. struct ExpandPage {
77. @Link animationProperties: AnimationProperties;
78. @State nodeController: PostNode | undefined = undefined;
79. // 展开时详细内容出现
80. private showDetailContent: boolean = true;

82. aboutToAppear(): void {
83. // 获取对应序号的卡片组件
84. this.nodeController = getPostNode(this.animationProperties.curIndex.toString());
85. // 更新为详细内容出现
86. this.nodeController?.update(this.animationProperties.curIndex.toString(), this.showDetailContent);
87. }

89. build() {
90. Stack() {
91. NodeContainer(this.nodeController)
92. }
93. .width('100%')
94. .height(this.animationProperties.changedHeight ? '100%' : 100)
95. .translate({ x: this.animationProperties.translateX, y: this.animationProperties.translateY })
96. .position({ x: this.animationProperties.positionX, y: this.animationProperties.positionY })
97. .onClick(() => {
98. this.getUIContext()?.animateTo({
99. curve: curves.springMotion(0.6, 0.9),
100. onFinish: () => {
101. if (this.nodeController != undefined) {
102. // 执行回调，折叠态节点获取卡片组件
103. this.nodeController.callCallback();
104. // 当前展开态节点的卡片组件下树
105. this.nodeController.onRemove();
106. }
107. // 卡片展开态节点下树
108. this.animationProperties.isExpandPageShow = false;
109. this.animationProperties.isEnabled = true;
110. }
111. }, () => {
112. // 卡片从展开态回到折叠态
113. this.animationProperties.isEnabled = false;
114. this.animationProperties.translateX = 0;
115. this.animationProperties.translateY = 0;
116. this.animationProperties.changedHeight = false;
117. // 更新为详细内容消失
118. this.nodeController?.update(this.animationProperties.curIndex.toString(), false);
119. })
120. })
121. }
122. }

124. class RectInfo {
125. left: number = 0;
126. top: number = 0;
127. right: number = 0;
128. bottom: number = 0;
129. width: number = 0;
130. height: number = 0;
131. }

133. // 封装的一镜到底动画类
134. @Observed
135. class AnimationProperties {
136. public isExpandPageShow: boolean = false;
137. // 控制组件是否响应点击事件
138. public isEnabled: boolean = true;
139. // 展开卡片的序号
140. public curIndex: number = -1;
141. public translateX: number = 0;
142. public translateY: number = 0;
143. public positionX: number = 0;
144. public positionY: number = 0;
145. public changedHeight: boolean = false;
146. private calculatedTranslateX: number = 0;
147. private calculatedTranslateY: number = 0;
148. // 设置卡片展开后相对父组件的位置
149. private expandTranslateX: number = 0;
150. private expandTranslateY: number = 0;
151. private uiContext: UIContext;

153. constructor(uiContext: UIContext) {
154. this.uiContext = uiContext
155. }

157. public expandAnimation(index: number): void {
158. // 记录展开态卡片的序号
159. if (index != undefined) {
160. this.curIndex = index;
161. }
162. // 计算折叠态卡片相对父组件的位置
163. this.calculateData(index.toString());
164. // 展开态卡片上树
165. this.isExpandPageShow = true;
166. // 卡片展开的属性动画
167. this.uiContext?.animateTo({
168. curve: curves.springMotion(0.6, 0.9)
169. }, () => {
170. this.translateX = this.calculatedTranslateX;
171. this.translateY = this.calculatedTranslateY;
172. this.changedHeight = true;
173. })
174. }

176. // 获取需要跨节点迁移的组件的位置，及迁移前后节点的公共父节点的位置，用以计算做动画组件的动画参数
177. public calculateData(key: string): void {
178. let clickedImageInfo = this.getRectInfoById(this.uiContext, key);
179. let rootStackInfo = this.getRectInfoById(this.uiContext, 'rootStack');
180. this.positionX = this.uiContext.px2vp(clickedImageInfo.left - rootStackInfo.left);
181. this.positionY = this.uiContext.px2vp(clickedImageInfo.top - rootStackInfo.top);
182. this.calculatedTranslateX = this.uiContext.px2vp(rootStackInfo.left - clickedImageInfo.left) +
183. this.expandTranslateX;
184. this.calculatedTranslateY = this.uiContext.px2vp(rootStackInfo.top - clickedImageInfo.top) + this.expandTranslateY;
185. }

187. // 根据组件的id获取组件的位置信息
188. private getRectInfoById(context: UIContext, id: string): RectInfo {
189. let componentInfo: componentUtils.ComponentInfo = context.getComponentUtils().getRectangleById(id);

191. if (!componentInfo) {
192. throw Error('object is empty');
193. }

195. let rstRect: RectInfo = new RectInfo();
196. const widthScaleGap = componentInfo.size.width * (1 - componentInfo.scale.x) / 2;
197. const heightScaleGap = componentInfo.size.height * (1 - componentInfo.scale.y) / 2;
198. rstRect.left = componentInfo.translate.x + componentInfo.windowOffset.x + widthScaleGap;
199. rstRect.top = componentInfo.translate.y + componentInfo.windowOffset.y + heightScaleGap;
200. rstRect.right =
201. componentInfo.translate.x + componentInfo.windowOffset.x + componentInfo.size.width - widthScaleGap;
202. rstRect.bottom =
203. componentInfo.translate.y + componentInfo.windowOffset.y + componentInfo.size.height - heightScaleGap;
204. rstRect.width = rstRect.right - rstRect.left;
205. rstRect.height = rstRect.bottom - rstRect.top;

207. return {
208. left: rstRect.left,
209. right: rstRect.right,
210. top: rstRect.top,
211. bottom: rstRect.bottom,
212. width: rstRect.width,
213. height: rstRect.height
214. }
215. }
216. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template3/Index.ets#L15-L233)

```
1. // PostNode.ets
2. // 跨容器迁移能力
3. import { UIContext, curves, NodeController, BuilderNode, FrameNode } from '@kit.ArkUI';
4. import { common } from '@kit.AbilityKit';

6. class Data {
7. public item: string | null = null;
8. public isExpand: boolean = false;
9. }
10. let context: undefined | common.UIAbilityContext = undefined;
11. @Builder
12. function postBuilder(data: Data) {
13. // 跨容器迁移组件置于@Builder内
14. Column() {
15. Row() {
16. Row()
17. .backgroundColor(Color.Pink)
18. .borderRadius(20)
19. .width(80)
20. .height(80)
21. Column() {
22. // 请在resources\base\element\string.json文件中配置name为'shareTransition_text5'，value为非空字符串的资源
23. Text((context as common.UIAbilityContext)?.resourceManager.getStringByNameSync('shareTransition_text5') + data.item)
24. .fontSize(20)
25. // 请将$r('app.string.shareTransition_text6')替换为实际资源文件，在本示例中该资源文件的value值为"共享元素转场"
26. Text($r('app.string.shareTransition_text6'))
27. .fontSize(12)
28. .fontColor(0x909399)
29. }
30. .alignItems(HorizontalAlign.Start)
31. .justifyContent(FlexAlign.SpaceAround)
32. .margin({ left: 10 })
33. .height(80)
34. }
35. .width('90%')
36. .height(100)

38. // 展开后显示细节内容
39. if (data.isExpand) {
40. Row() {
41. // 请将$r('app.string.shareTransition_text7')替换为实际资源文件，在本示例中该资源文件的value值为"展开态"
42. Text($r('app.string.shareTransition_text7'))
43. .fontSize(28)
44. .fontColor(0x909399)
45. .textAlign(TextAlign.Center)
46. .transition(TransitionEffect.OPACITY.animation({ curve: curves.springMotion(0.6, 0.9) }))
47. }
48. .width('90%')
49. .justifyContent(FlexAlign.Center)
50. }
51. }
52. .width('90%')
53. .height('100%')
54. .alignItems(HorizontalAlign.Center)
55. .borderRadius(10)
56. .margin({ top: 15 })
57. .backgroundColor(Color.White)
58. .shadow({
59. radius: 20,
60. color: 0x909399,
61. offsetX: 20,
62. offsetY: 10
63. })
64. }

66. class InternalValue {
67. public flag: boolean = false;
68. };

70. export class PostNode extends NodeController {
71. private node: BuilderNode<Data[]> | null = null;
72. private isRemove: InternalValue = new InternalValue();
73. private callback: Function | undefined = undefined;
74. private data: Data | null = null;

76. makeNode(uiContext: UIContext): FrameNode | null {
77. if (this.isRemove.flag === true) {
78. return null;
79. }
80. if (this.node != null) {
81. return this.node.getFrameNode();
82. }

84. return null;
85. }

87. init(uiContext: UIContext, id: string, isExpand: boolean) {
88. if (this.node != null) {
89. return;
90. }
91. // 创建节点，需要uiContext
92. this.node = new BuilderNode(uiContext);
93. context = uiContext.getHostContext() as common.UIAbilityContext;
94. // 创建离线组件
95. this.data = { item: id, isExpand: isExpand };
96. this.node.build(wrapBuilder<Data[]>(postBuilder), this.data);
97. }

99. update(id: string, isExpand: boolean) {
100. if (this.node !== null) {
101. // 调用update进行更新。
102. this.data = { item: id, isExpand: isExpand };
103. this.node.update(this.data);
104. }
105. }

107. setCallback(callback: Function | undefined) {
108. this.callback = callback;
109. }

111. callCallback() {
112. if (this.callback != undefined) {
113. this.callback();
114. }
115. }

117. onRemove() {
118. this.isRemove.flag = true;
119. // 组件迁移出节点时触发重建
120. this.rebuild();
121. this.isRemove.flag = false;
122. }
123. }

125. let gNodeMap: Map<string, PostNode | undefined> = new Map();

127. export const createPostNode =
128. (uiContext: UIContext, id: string, isExpand: boolean): PostNode | undefined => {
129. let node = new PostNode();
130. node.init(uiContext, id, isExpand);
131. gNodeMap.set(id, node);
132. return node;
133. }

135. export const getPostNode = (id: string): PostNode | undefined => {
136. if (!gNodeMap.has(id)) {
137. return undefined;
138. }
139. return gNodeMap.get(id);
140. }

142. export const deleteNode = (id: string) => {
143. gNodeMap.delete(id);
144. }
```

[PostNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template3/PostNode.ets#L16-L162)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/pu4Qek_oT_i_7WXj7Hnkqg/zh-cn_image_0000002589324347.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=41CCFF3171C0D6FFAF18982594AD9449F8D4780A349F6B8E1CCB8568CC33E775)

### 结合Navigation使用

可以利用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)的自定义导航转场动画能力（[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)，可参考Navigation[示例3](../harmonyos-references/ts-basic-components-navigation.md#示例3设置可交互转场动画)）实现一镜到底动效。共享元素转场期间，组件由消失页面迁移至出现页面。

以展开收起缩略图的场景为例，实现步骤为：

* 通过customNavContentTransition配置PageOne与PageTwo的自定义导航转场动画。
* 自定义的共享元素转场效果由属性动画实现，具体实现方式为抓取页面内组件相对窗口的位置信息从而正确匹配组件在PageOne与PageTwo的位置、缩放等，即动画开始和结束的属性信息。
* 点击缩略图后共享元素组件从PageOne被迁移至PageTwo，随后触发由PageOne至PageTwo的自定义转场动画，即PageTwo的共享元素组件从原来的缩略图状态做动画到全屏状态。
* 由全屏状态返回到缩略图时，触发由PageTwo至PageOne的自定义转场动画，即PageTwo的共享元素组件从全屏状态做动画到原PageOne的缩略图状态，转场结束后共享元素组件从PageTwo被迁移回PageOne。

```
1. ├──entry/src/main/ets                 // 代码区
2. │  ├──CustomTransition
3. │  │  ├──AnimationProperties.ets      // 一镜到底转场动画封装
4. │  │  └──CustomNavigationUtils.ets    // Navigation自定义转场动画配置
5. │  ├──entryability
6. │  │  └──EntryAbility.ets             // 程序入口类
7. │  ├──NodeContainer
8. │  │  └──CustomComponent.ets          // 自定义占位节点
9. │  ├──pages
10. │  │  ├──Index.ets                    // 导航页面
11. │  │  ├──PageOne.ets                  // 缩略图页面
12. │  │  └──PageTwo.ets                  // 全屏展开页面
13. │  └──utils
14. │     ├──ComponentAttrUtils.ets       // 组件位置获取
15. │     └──WindowUtils.ets              // 窗口信息
16. └──entry/src/main/resources           // 资源文件
```

```
1. // Index.ets
2. import { AnimateCallback, CustomTransition } from '../../../CustomTransition/CustomNavigationUtils';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = 'Index';
6. const DOMAIN = 0xF811;

8. @Entry
9. @Component
10. struct Index {
11. private pageInfos: NavPathStack = new NavPathStack();
12. // 允许进行自定义转场的页面名称
13. private allowedCustomTransitionFromPageName: string[] = ['PageOne'];
14. private allowedCustomTransitionToPageName: string[] = ['PageTwo'];

16. aboutToAppear(): void {
17. this.pageInfos.pushPath({ name: 'PageOne' });
18. }

20. private isCustomTransitionEnabled(fromName: string, toName: string): boolean {
21. // 点击和返回均需要进行自定义转场，因此需要分别判断
22. if ((this.allowedCustomTransitionFromPageName.includes(fromName) &&
23. this.allowedCustomTransitionToPageName.includes(toName)) ||
24. (this.allowedCustomTransitionFromPageName.includes(toName) &&
25. this.allowedCustomTransitionToPageName.includes(fromName))) {
26. return true;
27. }
28. return false;
29. }

31. build() {
32. Navigation(this.pageInfos)
33. .hideNavBar(true)
34. .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
35. if ((!from || !to) || (!from.name || !to.name)) {
36. return undefined;
37. }

39. // 通过from和to的name对自定义转场路由进行管控
40. if (!this.isCustomTransitionEnabled(from.name, to.name)) {
41. return undefined;
42. }

44. // 需要对转场页面是否注册了animation进行判断，来决定是否进行自定义转场
45. let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.index);
46. let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.index);
47. if (!fromParam.animation || !toParam.animation) {
48. return undefined;
49. }

51. // 一切判断完成后，构造customAnimation给系统侧调用，执行自定义转场动画
52. let customAnimation: NavigationAnimatedTransition = {
53. onTransitionEnd: (isSuccess: boolean) => {
54. hilog.info(DOMAIN, 'current transition result is', 'isSuccess: %s', isSuccess.toString());
55. },
56. timeout: 2000,
57. transition: (transitionProxy: NavigationTransitionProxy) => {
58. hilog.info(DOMAIN, TAG, 'trigger transition callback');
59. if (fromParam.animation) {
60. fromParam.animation(operation === NavigationOperation.PUSH, true, transitionProxy);
61. }
62. if (toParam.animation) {
63. toParam.animation(operation === NavigationOperation.PUSH, false, transitionProxy);
64. }
65. }
66. };
67. return customAnimation;
68. })
69. }
70. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template4/Index.ets#L15-L87)

```
1. // PageOne.ets
2. import { CustomTransition } from '../../../CustomTransition/CustomNavigationUtils';
3. import { MyNodeController, createMyNode, getMyNode } from '../../../NodeContainer/CustomComponent';
4. import { ComponentAttrUtils, RectInfoInPx } from '../../../utils/ComponentAttrUtils';
5. import { WindowUtils } from '../../../utils/WindowUtils';

7. @Builder
8. export function PageOneBuilder() {
9. PageOne();
10. }

12. @Component
13. export struct PageOne {
14. private pageInfos: NavPathStack = new NavPathStack();
15. private pageId: number = -1;
16. @State myNodeController: MyNodeController | undefined = new MyNodeController(false);

18. aboutToAppear(): void {
19. let node = getMyNode();
20. if (node === undefined) {
21. // 新建自定义节点
22. createMyNode(this.getUIContext());
23. }
24. this.myNodeController = getMyNode();
25. }

27. private doFinishTransition(): void {
28. // PageTwo结束转场时将节点从PageTwo迁移回PageOne
29. this.myNodeController = getMyNode();
30. }

32. private registerCustomTransition(): void {
33. // 注册自定义动画协议
34. CustomTransition.getInstance().registerNavParam(this.pageId,
35. (isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => {
36. }, 500);
37. }

39. private onCardClicked(): void {
40. let cardItemInfo: RectInfoInPx =
41. ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), 'card');
42. let param: Record<string, Object> = {};
43. param['cardItemInfo'] = cardItemInfo;
44. param['doDefaultTransition'] = (myController: MyNodeController) => {
45. this.doFinishTransition();
46. };
47. this.pageInfos.pushPath({ name: 'PageTwo', param: param });
48. // 自定义节点从PageOne下树
49. if (this.myNodeController != undefined) {
50. (this.myNodeController as MyNodeController).onRemove();
51. }
52. }

54. build() {
55. NavDestination() {
56. Stack() {
57. Column({ space: 20 }) {
58. Row({ space: 10 }) {
59. // 请将$r('app.media.avatar')替换为实际资源文件
60. Image($r('app.media.avatar'))
61. .size({ width: 50, height: 50 })
62. .borderRadius(25)
63. .clip(true)

65. Text('Alice')
66. }
67. .justifyContent(FlexAlign.Start)

69. // 请将$r('app.string.shareTransition_text2')替换为实际资源文件，在本示例中该资源文件的value值为"你好世界"
70. Text($r('app.string.shareTransition_text2'))

72. NodeContainer(this.myNodeController)
73. .size({ width: 320, height: 250 })
74. .onClick(() => {
75. this.onCardClicked();
76. })
77. }
78. .alignItems(HorizontalAlign.Start)
79. .margin(30)
80. }
81. }
82. .onReady((context: NavDestinationContext) => {
83. this.pageInfos = context.pathStack;
84. this.pageId = this.pageInfos.getAllPathName().length - 1;
85. this.registerCustomTransition();
86. })
87. .onDisAppear(() => {
88. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
89. // 自定义节点从PageOne下树
90. if (this.myNodeController != undefined) {
91. (this.myNodeController as MyNodeController).onRemove();
92. }
93. })
94. }
95. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template4/PageOne.ets#L16-L113)

```
1. // PageTwo.ets
2. import { CustomTransition } from '../../../CustomTransition/CustomNavigationUtils';
3. import { AnimationProperties } from '../../../CustomTransition/AnimationProperties';
4. import { RectInfoInPx } from '../../../utils/ComponentAttrUtils';
5. import { getMyNode, MyNodeController } from '../../../NodeContainer/CustomComponent';

7. @Builder
8. export function PageTwoBuilder() {
9. PageTwo();
10. }

12. @Component
13. export struct PageTwo {
14. @State pageInfos: NavPathStack = new NavPathStack();
15. @State animationProperties: AnimationProperties = new AnimationProperties(this.getUIContext());
16. @State myNodeController: MyNodeController | undefined = new MyNodeController(false);
17. private pageId: number = -1;
18. private shouldDoDefaultTransition: boolean = false;
19. private prePageDoFinishTransition: () => void = () => {};
20. private cardItemInfo: RectInfoInPx = new RectInfoInPx();
21. @StorageProp('windowSizeChanged') @Watch('unRegisterNavParam') windowSizeChangedTime: number = 0;
22. @StorageProp('onConfigurationUpdate') @Watch('unRegisterNavParam') onConfigurationUpdateTime: number = 0;

24. aboutToAppear(): void {
25. // 迁移自定义节点至当前页面
26. this.myNodeController = getMyNode();
27. }

29. private unRegisterNavParam(): void {
30. this.shouldDoDefaultTransition = true;
31. }

33. private onBackPressed(): boolean {
34. if (this.shouldDoDefaultTransition) {
35. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
36. this.pageInfos.pop();
37. this.prePageDoFinishTransition();
38. this.shouldDoDefaultTransition = false;
39. return true;
40. }
41. this.pageInfos.pop();
42. return true;
43. }

45. build() {
46. NavDestination() {
47. // Stack需要设置alignContent为TopStart，否则在高度变化过程中，截图和内容都会随高度重新布局位置
48. Stack({ alignContent: Alignment.TopStart }) {
49. Stack({ alignContent: Alignment.TopStart }) {
50. Column({ space: 20 }) {
51. NodeContainer(this.myNodeController);
52. if (this.animationProperties.showDetailContent) {
53. // 请将$r('app.string.shareTransition_text8')替换为实际资源文件，在本示例中该资源文件的value值为"展开态内容"
54. Text($r('app.string.shareTransition_text8'))
55. .fontSize(20)
56. .transition(TransitionEffect.OPACITY)
57. .margin(30)
58. }
59. }
60. .alignItems(HorizontalAlign.Start)
61. }
62. .position({ y: this.animationProperties.positionValue });
63. }
64. .scale({ x: this.animationProperties.scaleValue, y: this.animationProperties.scaleValue })
65. .translate({ x: this.animationProperties.translateX, y: this.animationProperties.translateY })
66. .width(this.animationProperties.clipWidth)
67. .height(this.animationProperties.clipHeight)
68. .borderRadius(this.animationProperties.radius)
69. // expandSafeArea使得Stack做沉浸式效果，向上扩到状态栏，向下扩到导航条
70. .expandSafeArea([SafeAreaType.SYSTEM])
71. // 对高度进行裁切
72. .clip(true)
73. }
74. .backgroundColor(this.animationProperties.navDestinationBgColor)
75. .hideTitleBar(true)
76. .onReady((context: NavDestinationContext) => {
77. this.pageInfos = context.pathStack;
78. this.pageId = this.pageInfos.getAllPathName().length - 1;
79. let param = context.pathInfo?.param as Record<string, Object>;
80. this.prePageDoFinishTransition = param['doDefaultTransition'] as () => void;
81. this.cardItemInfo = param['cardItemInfo'] as RectInfoInPx;
82. CustomTransition.getInstance().registerNavParam(this.pageId,
83. (isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => {
84. this.animationProperties.doAnimation(
85. this.cardItemInfo, isPush, isExit, transitionProxy, 0,
86. this.prePageDoFinishTransition, this.myNodeController);
87. }, 500);
88. })
89. .onBackPressed(() => {
90. return this.onBackPressed();
91. })
92. .onDisAppear(() => {
93. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
94. })
95. }
96. }
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template4/PageTwo.ets#L16-L114)

```
1. // CustomNavigationUtils.ets
2. // 配置Navigation自定义转场动画
3. export interface AnimateCallback {
4. animation: ((isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => void | undefined)
5. | undefined;
6. timeout: (number | undefined) | undefined;
7. }

9. const customTransitionMap: Map<number, AnimateCallback> = new Map();

11. export class CustomTransition {
12. private constructor() {
13. };

15. static delegate = new CustomTransition();

17. static getInstance() {
18. return CustomTransition.delegate;
19. }

21. // 注册页面的动画回调，name是注册页面的动画的回调
22. // animationCallback是需要执行的动画内容，timeout是转场结束的超时时间
23. registerNavParam(
24. name: number,
25. animationCallback: (operation: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => void,
26. timeout: number): void {
27. if (customTransitionMap.has(name)) {
28. let param = customTransitionMap.get(name);
29. if (param != undefined) {
30. param.animation = animationCallback;
31. param.timeout = timeout;
32. return;
33. }
34. }
35. let params: AnimateCallback = { timeout: timeout, animation: animationCallback };
36. customTransitionMap.set(name, params);
37. }

39. unRegisterNavParam(name: number): void {
40. customTransitionMap.delete(name);
41. }

43. getAnimateParam(name: number): AnimateCallback {
44. let result: AnimateCallback = {
45. animation: customTransitionMap.get(name)?.animation,
46. timeout: customTransitionMap.get(name)?.timeout,
47. };
48. return result;
49. }
50. }
```

[CustomNavigationUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/CustomTransition/CustomNavigationUtils.ets#L15-L67)

```
1. // 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}
2. // route_map.json
3. {
4. "routerMap": [
5. {
6. "name": "PageOne",
7. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
8. "buildFunction": "PageOneBuilder"
9. },
10. {
11. "name": "PageTwo",
12. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
13. "buildFunction": "PageTwoBuilder"
14. }
15. ]
16. }
```

```
1. // AnimationProperties.ets
2. // 一镜到底转场动画封装
3. import { curves, UIContext } from '@kit.ArkUI';
4. import { RectInfoInPx } from '../utils/ComponentAttrUtils';
5. import { WindowUtils } from '../utils/WindowUtils';
6. import { MyNodeController } from '../NodeContainer/CustomComponent';
7. import { hilog } from '@kit.PerformanceAnalysisKit';

9. const TAG: string = 'AnimationProperties';
10. const DOMAIN = 0xF811;
11. const DEVICE_BORDER_RADIUS: number = 34;

13. // 将自定义一镜到底转场动画进行封装，其他界面也需要做自定义一镜到底转场的话，可以直接复用，减少工作量
14. @Observed
15. export class AnimationProperties {
16. public navDestinationBgColor: ResourceColor = Color.Transparent;
17. public translateX: number = 0;
18. public translateY: number = 0;
19. public scaleValue: number = 1;
20. public clipWidth: Dimension = 0;
21. public clipHeight: Dimension = 0;
22. public radius: number = 0;
23. public positionValue: number = 0;
24. public showDetailContent: boolean = false;
25. private uiContext: UIContext;

27. constructor(uiContext: UIContext) {
28. this.uiContext = uiContext;
29. }

31. public doAnimation(cardItemInfoPx: RectInfoInPx, isPush: boolean, isExit: boolean,
32. transitionProxy: NavigationTransitionProxy, extraTranslateValue: number,
33. prePageOnFinish: (index: MyNodeController) => void, myNodeController: MyNodeController | undefined): void {
34. // 首先计算卡片的宽高与窗口宽高的比例
35. let widthScaleRatio = cardItemInfoPx.width / WindowUtils.windowWidthPx;
36. let heightScaleRatio = cardItemInfoPx.height / WindowUtils.windowHeightPx;
37. let isUseWidthScale = widthScaleRatio > heightScaleRatio;
38. let initScale: number = isUseWidthScale ? widthScaleRatio : heightScaleRatio;

40. let initTranslateX: number = 0;
41. let initTranslateY: number = 0;
42. let initClipWidth: Dimension = 0;
43. let initClipHeight: Dimension = 0;
44. // 使得PageTwo卡片向上扩到状态栏
45. let initPositionValue: number = -this.uiContext.px2vp(WindowUtils.topAvoidAreaHeightPx + extraTranslateValue);

47. if (isUseWidthScale) {
48. initTranslateX = this.uiContext.px2vp(cardItemInfoPx.left -
49. (WindowUtils.windowWidthPx - cardItemInfoPx.width) / 2);
50. initClipWidth = '100%';
51. initClipHeight = this.uiContext.px2vp((cardItemInfoPx.height) / initScale);
52. initTranslateY = this.uiContext.px2vp(cardItemInfoPx.top - ((this.uiContext.vp2px(initClipHeight) -
53. this.uiContext.vp2px(initClipHeight) * initScale) / 2));
54. } else {
55. initTranslateY = this.uiContext.px2vp(cardItemInfoPx.top -
56. (WindowUtils.windowHeightPx - cardItemInfoPx.height) / 2);
57. initClipHeight = '100%';
58. initClipWidth = this.uiContext.px2vp((cardItemInfoPx.width) / initScale);
59. initTranslateX = this.uiContext.px2vp(cardItemInfoPx.left -
60. (WindowUtils.windowWidthPx / 2 - cardItemInfoPx.width / 2));
61. }

63. // 转场动画开始前通过计算scale、translate、position和clip height & width，确定节点迁移前后位置一致
64. hilog.info(DOMAIN, TAG, 'initScale: ' + initScale + ' initTranslateX ' + initTranslateX +
65. ' initTranslateY ' + initTranslateY + ' initClipWidth ' + initClipWidth +
66. ' initClipHeight ' + initClipHeight + ' initPositionValue ' + initPositionValue);

68. // 转场至新页面
69. if (isPush && !isExit) {
70. this.scaleValue = initScale;
71. this.translateX = initTranslateX;
72. this.clipWidth = initClipWidth;
73. this.clipHeight = initClipHeight;
74. this.translateY = initTranslateY;
75. this.positionValue = initPositionValue;

77. this.uiContext?.animateTo({
78. curve: curves.interpolatingSpring(0, 1, 328, 36),
79. onFinish: () => {
80. if (transitionProxy) {
81. transitionProxy.finishTransition();
82. }
83. }
84. }, () => {
85. this.scaleValue = 1.0;
86. this.translateX = 0;
87. this.translateY = 0;
88. this.clipWidth = '100%';
89. this.clipHeight = '100%';
90. // 页面圆角与系统圆角一致
91. this.radius = DEVICE_BORDER_RADIUS;
92. this.showDetailContent = true;
93. })

95. this.uiContext?.animateTo({
96. duration: 100,
97. curve: Curve.Sharp,
98. }, () => {
99. // 页面由透明逐渐变为设置背景色
100. this.navDestinationBgColor = '#00ffffff';
101. })

103. // 返回旧页面
104. } else if (!isPush && isExit) {

106. this.uiContext?.animateTo({
107. duration: 350,
108. curve: Curve.EaseInOut,
109. onFinish: () => {
110. if (transitionProxy) {
111. transitionProxy.finishTransition();
112. }
113. prePageOnFinish(myNodeController);
114. // 自定义节点从PageTwo下树
115. if (myNodeController != undefined) {
116. (myNodeController as MyNodeController).onRemove();
117. }
118. }
119. }, () => {
120. this.scaleValue = initScale;
121. this.translateX = initTranslateX;
122. this.translateY = initTranslateY;
123. this.radius = 0;
124. this.clipWidth = initClipWidth;
125. this.clipHeight = initClipHeight;
126. this.showDetailContent = false;
127. })

129. this.uiContext?.animateTo({
130. duration: 200,
131. delay: 150,
132. curve: Curve.Friction,
133. }, () => {
134. this.navDestinationBgColor = Color.Transparent;
135. })
136. }
137. }
138. }
```

[AnimationProperties.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/CustomTransition/AnimationProperties.ets#L15-L155)

```
1. // ComponentAttrUtils.ets
2. // 获取组件相对窗口的位置
3. import { componentUtils, UIContext } from '@kit.ArkUI';
4. import { JSON } from '@kit.ArkTS';

6. export class ComponentAttrUtils {
7. // 根据组件的id获取组件的位置信息
8. public static getRectInfoById(context: UIContext, id: string): RectInfoInPx {
9. if (!context || !id) {
10. throw Error('object is empty');
11. }
12. let componentInfo: componentUtils.ComponentInfo = context.getComponentUtils().getRectangleById(id);

14. if (!componentInfo) {
15. throw Error('object is empty');
16. }

18. let rstRect: RectInfoInPx = new RectInfoInPx();
19. const widthScaleGap = componentInfo.size.width * (1 - componentInfo.scale.x) / 2;
20. const heightScaleGap = componentInfo.size.height * (1 - componentInfo.scale.y) / 2;
21. rstRect.left = componentInfo.translate.x + componentInfo.windowOffset.x + widthScaleGap;
22. rstRect.top = componentInfo.translate.y + componentInfo.windowOffset.y + heightScaleGap;
23. rstRect.right =
24. componentInfo.translate.x + componentInfo.windowOffset.x + componentInfo.size.width - widthScaleGap;
25. rstRect.bottom =
26. componentInfo.translate.y + componentInfo.windowOffset.y + componentInfo.size.height - heightScaleGap;
27. rstRect.width = rstRect.right - rstRect.left;
28. rstRect.height = rstRect.bottom - rstRect.top;
29. return {
30. left: rstRect.left,
31. right: rstRect.right,
32. top: rstRect.top,
33. bottom: rstRect.bottom,
34. width: rstRect.width,
35. height: rstRect.height
36. }
37. }
38. }

40. export class RectInfoInPx {
41. public left: number = 0;
42. public top: number = 0;
43. public right: number = 0;
44. public bottom: number = 0;
45. public width: number = 0;
46. public height: number = 0;
47. }

49. export class RectJson {
50. public $rect: Array<number> = [];
51. }
```

[ComponentAttrUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/utils/ComponentAttrUtils.ets#L16-L69)

```
1. // WindowUtils.ets
2. // 窗口信息
3. import { window } from '@kit.ArkUI';

5. export class WindowUtils {
6. public static window: window.Window;
7. public static windowWidthPx: number;
8. public static windowHeightPx: number;
9. public static topAvoidAreaHeightPx: number;
10. public static navigationIndicatorHeightPx: number;
11. }
```

[WindowUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/utils/WindowUtils.ets#L16-L29)

```
1. // EntryAbility.ets
2. // 程序入口处的onWindowStageCreate增加对窗口宽高等的抓取

4. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
5. import { WindowUtils } from '../utils/WindowUtils';
6. import { display, window } from '@kit.ArkUI';
7. import { hilog } from '@kit.PerformanceAnalysisKit';

9. const DOMAIN = 0x0000;
10. const TAG: string = 'EntryAbility';

12. export default class EntryAbility extends UIAbility {
13. private currentBreakPoint: string = '';

15. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
16. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onCreate');
17. }

19. onDestroy(): void {
20. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onDestroy');
21. }

23. onWindowStageCreate(windowStage: window.WindowStage): void {
24. // Main window is created, set main page for this ability
25. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageCreate');
26. // ...
27. // 获取窗口宽高
28. WindowUtils.window = windowStage.getMainWindowSync();
29. WindowUtils.windowWidthPx = WindowUtils.window.getWindowProperties().windowRect.width;
30. WindowUtils.windowHeightPx = WindowUtils.window.getWindowProperties().windowRect.height;

32. this.updateBreakpoint(WindowUtils.windowWidthPx);

34. // 获取上方避让区(状态栏等)高度
35. let avoidArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
36. WindowUtils.topAvoidAreaHeightPx = avoidArea.topRect.height;

38. // 获取导航条高度
39. let navigationArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
40. WindowUtils.navigationIndicatorHeightPx = navigationArea.bottomRect.height;

42. hilog.info(DOMAIN, TAG, 'the width is ' + WindowUtils.windowWidthPx + '  ' + WindowUtils.windowHeightPx + '  ' +
43. WindowUtils.topAvoidAreaHeightPx + '  ' + WindowUtils.navigationIndicatorHeightPx);

45. // 监听窗口尺寸、状态栏高度及导航条高度的变化并更新
46. try {
47. WindowUtils.window.on('windowSizeChange', (data) => {
48. hilog.info(DOMAIN, TAG, 'on windowSizeChange, the width is ' + data.width + ', the height is ' + data.height);
49. WindowUtils.windowWidthPx = data.width;
50. WindowUtils.windowHeightPx = data.height;
51. this.updateBreakpoint(data.width);
52. AppStorage.setOrCreate('windowSizeChanged', Date.now());
53. })

55. WindowUtils.window.on('avoidAreaChange', (data) => {
56. if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
57. let topRectHeight = data.area.topRect.height;
58. hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the top avoid area height is ' + topRectHeight);
59. WindowUtils.topAvoidAreaHeightPx = topRectHeight;
60. } else if (data.type === window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
61. let bottomRectHeight = data.area.bottomRect.height;
62. hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the navigation indicator height is ' + bottomRectHeight);
63. WindowUtils.navigationIndicatorHeightPx = bottomRectHeight;
64. }
65. })
66. } catch (exception) {
67. hilog.error(DOMAIN, TAG, `register failed. code: ${exception.code}, message: ${exception.message}`);
68. }

70. windowStage.loadContent('pages/Index', (err) => {
71. if (err.code) {
72. hilog.error(DOMAIN, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
73. return;
74. }
75. hilog.info(DOMAIN, TAG, 'Succeeded in loading the content.');
76. });
77. }

79. updateBreakpoint(width: number) {
80. let windowWidthVp = width / (display.getDefaultDisplaySync().densityDPI / 160);
81. let newBreakPoint: string = '';
82. if (windowWidthVp < 400) {
83. newBreakPoint = 'xs';
84. } else if (windowWidthVp < 600) {
85. newBreakPoint = 'sm';
86. } else if (windowWidthVp < 800) {
87. newBreakPoint = 'md';
88. } else {
89. newBreakPoint = 'lg';
90. }
91. if (this.currentBreakPoint !== newBreakPoint) {
92. this.currentBreakPoint = newBreakPoint;
93. // 使用状态变量记录当前断点值
94. AppStorage.setOrCreate('currentBreakpoint', this.currentBreakPoint);
95. }
96. }
97. onWindowStageDestroy(): void {
98. // Main window is destroyed, release UI related resources
99. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageDestroy');
100. }

102. onForeground(): void {
103. // Ability has brought to foreground
104. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onForeground');
105. }

107. onBackground(): void {
108. // Ability has back to background
109. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onBackground');
110. }
111. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/entryability/EntryAbility.ets#L15-L161)

```
1. // CustomComponent.ets
2. // 自定义占位节点，跨容器迁移能力
3. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

5. @Builder
6. function cardBuilder() {
7. // 请将$r('app.media.card')替换为实际资源文件
8. Image($r('app.media.card'))
9. .width('100%')
10. .id('card')
11. }

13. export class MyNodeController extends NodeController {
14. private cardNode: BuilderNode<[]> | null = null;
15. private wrapBuilder: WrappedBuilder<[]> = wrapBuilder(cardBuilder);
16. private needCreate: boolean = false;
17. private isRemove: boolean = false;

19. constructor(create: boolean) {
20. super();
21. this.needCreate = create;
22. }

24. makeNode(uiContext: UIContext): FrameNode | null {
25. if (this.isRemove === true) {
26. return null;
27. }
28. if (this.needCreate && this.cardNode === null) {
29. this.cardNode = new BuilderNode(uiContext);
30. this.cardNode.build(this.wrapBuilder);
31. }
32. if (this.cardNode === null) {
33. return null;
34. }
35. return this.cardNode!.getFrameNode()!;
36. }

38. getNode(): BuilderNode<[]> | null {
39. return this.cardNode;
40. }

42. setNode(node: BuilderNode<[]> | null) {
43. this.cardNode = node;
44. this.rebuild();
45. }

47. onRemove() {
48. this.isRemove = true;
49. this.rebuild();
50. this.isRemove = false;
51. }

53. init(uiContext: UIContext) {
54. this.cardNode = new BuilderNode(uiContext);
55. this.cardNode.build(this.wrapBuilder);
56. }
57. }

59. let myNode: MyNodeController | undefined;

61. export const createMyNode =
62. (uiContext: UIContext) => {
63. myNode = new MyNodeController(false);
64. myNode.init(uiContext);
65. }

67. export const getMyNode = (): MyNodeController | undefined => {
68. return myNode;
69. }
```

[CustomComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/NodeContainer/CustomComponent.ets#L15-L86)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/-D3ZbfgJRvyOswJf9-4WhQ/zh-cn_image_0000002589244287.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=306F43CC8ED8A02C7527FC9EEA1991A8056185B9A157105812C0A13C9C4FBDF9)

### 结合BindSheet使用

想实现半模态转场（[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)）的同时，组件从初始界面做一镜到底动画到半模态页面的效果，可以使用这样的设计思路。将[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)中的mode设置为SheetMode.EMBEDDED，该模式下新起的页面可以覆盖在半模态弹窗上，页面返回后该半模态依旧存在，半模态面板内容不丢失。在半模态转场的同时设置一全模态转场（[bindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)）页面无转场出现，该页面仅有需要做共享元素转场的组件，通过属性动画，展示组件从初始界面至半模态页面的一镜到底动效，并在动画结束时关闭页面，并将该组件迁移至半模态页面。

以点击图片展开半模态页的场景为例，实现步骤为：

* 在初始界面挂载半模态转场和全模态转场两个页面，半模态页按需布局，全模态页面仅放置一镜到底动效需要的组件，抓取布局信息，使其初始位置为初始界面图片的位置。点击初始界面图片时，同时触发半模态和全模态页面出现，因设置为SheetMode.EMBEDDED模式，此时全模态页面层级最高。
* 设置不可见的占位图片置于半模态页上，作为一镜到底动效结束时图片的终止位置。利用[布局回调](../harmonyos-references/js-apis-arkui-inspector.md)监听该占位图片布局完成的时候，此时执行回调抓取占位图片的位置信息，随后全模态页面上的图片利用属性动画开始进行共享元素转场。
* 全模态页面的动画结束时触发结束回调，关闭全模态页面，将共享元素图片的节点迁移至半模态页面，替换占位图片。
* 需注意，半模态页面的弹起高度不同，其页面起始位置也有所不同，而全模态则是全屏显示，两者存在一高度差，做一镜到底动画时，需要计算差值并进行修正，具体可见demo。
* 还可以配合一镜到底动画，给初始界面图片也增加一个从透明到出现的动画，使得动效更为流畅。

```
1. ├──entry/src/main/ets                 // 代码区
2. │  ├──entryability
3. │  │  └──EntryAbility.ets             // 程序入口类
4. │  ├──NodeContainer
5. │  │  └──CustomComponent.ets          // 自定义占位节点
6. │  ├──pages
7. │  │  └──Index.ets                    // 进行共享元素转场的主页面
8. │  └──utils
9. │     ├──ComponentAttrUtils.ets       // 组件位置获取
10. │     └──WindowUtils.ets              // 窗口信息
11. └──entry/src/main/resources           // 资源文件
```

```
1. // index.ets
2. import { MyNodeController, createMyNode, getMyNode } from '../NodeContainer/CustomComponent';
3. import { ComponentAttrUtils, RectInfoInPx } from '../utils/ComponentAttrUtils';
4. import { WindowUtils } from '../utils/WindowUtils';
5. import { inspector } from '@kit.ArkUI'

7. class AnimationInfo {
8. scale: number = 0;
9. translateX: number = 0;
10. translateY: number = 0;
11. clipWidth: Dimension = 0;
12. clipHeight: Dimension = 0;
13. }

15. @Entry
16. @Component
17. struct Index {
18. @State isShowSheet: boolean = false;
19. @State isShowImage: boolean = false;
20. @State isShowOverlay: boolean = false;
21. @State isAnimating: boolean = false;
22. @State isEnabled: boolean = true;

24. @State scaleValue: number = 0;
25. @State translateX: number = 0;
26. @State translateY: number = 0;
27. @State clipWidth: Dimension = 0;
28. @State clipHeight: Dimension = 0;
29. @State radius: number = 0;
30. // 原图的透明度
31. @State opacityDegree: number = 1;

33. // 抓取照片原位置信息
34. private originInfo: AnimationInfo = new AnimationInfo;
35. // 抓取照片在半模态页上位置信息
36. private targetInfo: AnimationInfo = new AnimationInfo;
37. // 半模态高度
38. private bindSheetHeight: number = 450;
39. // 半模态上图片圆角
40. private sheetRadius: number = 20;

42. // 设置半模态上图片的布局监听
43. listener:inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('target');
44. aboutToAppear(): void {
45. // 设置半模态上图片的布局完成回调
46. let onLayoutComplete:()=>void=():void=>{
47. // 目标图片布局完成时抓取布局信息
48. this.targetInfo = this.calculateData('target');
49. // 仅半模态正确布局且此时无动画时触发一镜到底动画
50. if (this.targetInfo.scale != 0 && this.targetInfo.clipWidth != 0 && this.targetInfo.clipHeight != 0 && !this.isAnimating) {
51. this.isAnimating = true;
52. // 用于一镜到底的模态页的属性动画
53. this.getUIContext()?.animateTo({
54. duration: 1000,
55. curve: Curve.Friction,
56. onFinish: () => {
57. // 模态转场页（overlay）上的自定义节点下树
58. this.isShowOverlay = false;
59. // 半模态上的自定义节点上树，由此完成节点迁移
60. this.isShowImage = true;
61. }
62. }, () => {
63. this.scaleValue = this.targetInfo.scale;
64. this.translateX = this.targetInfo.translateX;
65. this.clipWidth = this.targetInfo.clipWidth;
66. this.clipHeight = this.targetInfo.clipHeight;
67. // 修正因半模态高度和缩放导致的高度差
68. this.translateY = this.targetInfo.translateY +
69. (this.getUIContext().px2vp(WindowUtils.windowHeight_px) - this.bindSheetHeight
70. - this.getUIContext().px2vp(WindowUtils.navigationIndicatorHeight_px) - this.getUIContext().px2vp(WindowUtils.topAvoidAreaHeight_px));
71. // 修正因缩放导致的圆角差异
72. this.radius = this.sheetRadius / this.scaleValue
73. })
74. // 原图从透明到出现的动画
75. this.getUIContext()?.animateTo({
76. duration: 2000,
77. curve: Curve.Friction,
78. }, () => {
79. this.opacityDegree = 1;
80. })
81. }
82. }
83. // 打开布局监听
84. this.listener.on('layout', onLayoutComplete)
85. }

87. // 获取对应id的组件相对窗口左上角的属性
88. calculateData(id: string): AnimationInfo {
89. let itemInfo: RectInfoInPx =
90. ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), id);
91. // 首先计算图片的宽高与窗口宽高的比例
92. let widthScaleRatio = itemInfo.width / WindowUtils.windowWidth_px;
93. let heightScaleRatio = itemInfo.height / WindowUtils.windowHeight_px;
94. let isUseWidthScale = widthScaleRatio > heightScaleRatio;
95. let itemScale: number = isUseWidthScale ? widthScaleRatio : heightScaleRatio;
96. let itemTranslateX: number = 0;
97. let itemClipWidth: Dimension = 0;
98. let itemClipHeight: Dimension = 0;
99. let itemTranslateY: number = 0;

101. if (isUseWidthScale) {
102. itemTranslateX = this.getUIContext().px2vp(itemInfo.left - (WindowUtils.windowWidth_px - itemInfo.width) / 2);
103. itemClipWidth = '100%';
104. itemClipHeight = this.getUIContext().px2vp((itemInfo.height) / itemScale);
105. itemTranslateY = this.getUIContext().px2vp(itemInfo.top - ((this.getUIContext().vp2px(itemClipHeight) - this.getUIContext().vp2px(itemClipHeight) * itemScale) / 2));
106. } else {
107. itemTranslateY = this.getUIContext().px2vp(itemInfo.top - (WindowUtils.windowHeight_px - itemInfo.height) / 2);
108. itemClipHeight = '100%';
109. itemClipWidth = this.getUIContext().px2vp((itemInfo.width) / itemScale);
110. itemTranslateX = this.getUIContext().px2vp(itemInfo.left - (WindowUtils.windowWidth_px / 2 - itemInfo.width / 2));
111. }

113. return {
114. scale: itemScale,
115. translateX: itemTranslateX ,
116. translateY: itemTranslateY,
117. clipWidth: itemClipWidth,
118. clipHeight: itemClipHeight,
119. }
120. }

122. // 照片页
123. build() {
124. Column() {
125. Text('照片')
126. .textAlign(TextAlign.Start)
127. .width('100%')
128. .fontSize(30)
129. .padding(20)
130. // 图片使用Resource资源，需用户自定义
131. Image($r("app.media.flower"))
132. .opacity(this.opacityDegree)
133. .width('90%')
134. .id('origin')// 挂载半模态页
135. .enabled(this.isEnabled)
136. .onClick(() => {
137. // 获取原始图像的位置信息，将模态页上图片移动缩放至该位置
138. this.originInfo = this.calculateData('origin');
139. this.scaleValue = this.originInfo.scale;
140. this.translateX = this.originInfo.translateX;
141. this.translateY = this.originInfo.translateY;
142. this.clipWidth = this.originInfo.clipWidth;
143. this.clipHeight = this.originInfo.clipHeight;
144. this.radius = 0;
145. this.opacityDegree = 0;
146. // 启动半模态页和模态页
147. this.isShowSheet = true;
148. this.isShowOverlay = true;
149. // 设置原图为不可交互抗打断
150. this.isEnabled = false;
151. })
152. }
153. .width('100%')
154. .height('100%')
155. .padding({ top: 20 })
156. .alignItems(HorizontalAlign.Center)
157. .bindSheet(this.isShowSheet, this.mySheet(), {
158. // Embedded模式使得其他页面可以高于半模态页
159. mode: SheetMode.EMBEDDED,
160. height: this.bindSheetHeight,
161. onDisappear: () => {
162. // 保证半模态消失时状态正确
163. this.isShowImage = false;
164. this.isShowSheet = false;
165. // 设置一镜到底动画又进入可触发状态
166. this.isAnimating = false;
167. // 原图重新变为可交互状态
168. this.isEnabled = true;
169. }
170. }) // 挂载模态页作为一镜到底动画的实现页
171. .bindContentCover(this.isShowOverlay, this.overlayNode(), {
172. // 模态页面设置为无转场
173. transition: TransitionEffect.IDENTITY,
174. })
175. }

177. // 半模态页面
178. @Builder
179. mySheet() {
180. Column({space: 20}) {
181. Text('半模态页面')
182. .fontSize(30)
183. Row({space: 40}) {
184. Column({space: 20}) {
185. ForEach([1, 2, 3, 4], () => {
186. Stack()
187. .backgroundColor(Color.Pink)
188. .borderRadius(20)
189. .width(60)
190. .height(60)
191. })
192. }
193. Column() {
194. if (this.isShowImage) {
195. // 半模态页面的自定义图片节点
196. ImageNode()
197. }
198. else {
199. // 抓取布局和占位用，实际不显示
200. // 图片使用Resource资源，需用户自定义
201. Image($r("app.media.flower"))
202. .visibility(Visibility.Hidden)
203. }
204. }
205. .height(300)
206. .width(200)
207. .borderRadius(20)
208. .clip(true)
209. .id('target')
210. }
211. .alignItems(VerticalAlign.Top)
212. }
213. .alignItems(HorizontalAlign.Start)
214. .height('100%')
215. .width('100%')
216. .margin(40)
217. }

219. @Builder
220. overlayNode() {
221. // Stack需要设置alignContent为TopStart，否则在高度变化过程中，截图和内容都会随高度重新布局位置
222. Stack({ alignContent: Alignment.TopStart }) {
223. ImageNode()
224. }
225. .scale({ x: this.scaleValue, y: this.scaleValue, centerX: undefined, centerY: undefined})
226. .translate({ x: this.translateX, y: this.translateY })
227. .width(this.clipWidth)
228. .height(this.clipHeight)
229. .borderRadius(this.radius)
230. .clip(true)
231. }
232. }

234. @Component
235. struct ImageNode {
236. @State myNodeController: MyNodeController | undefined = new MyNodeController(false);

238. aboutToAppear(): void {
239. // 获取自定义节点
240. let node = getMyNode();
241. if (node == undefined) {
242. // 新建自定义节点
243. createMyNode(this.getUIContext());
244. }
245. this.myNodeController = getMyNode();
246. }

248. aboutToDisappear(): void {
249. if (this.myNodeController != undefined) {
250. // 节点下树
251. this.myNodeController.onRemove();
252. }
253. }
254. build() {
255. NodeContainer(this.myNodeController)
256. }
257. }
```

```
1. // CustomComponent.ets
2. // 自定义占位节点，跨容器迁移能力
3. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

5. @Builder
6. function flowerBuilder() {
7. // 请将$r('app.media.longevity_flower')替换为实际资源文件
8. Image($r('app.media.longevity_flower'))
9. // 避免第一次加载图片时图片闪烁
10. .syncLoad(true);
11. }

13. export class MyNodeController extends NodeController {
14. private flowerNode: BuilderNode<[]> | null = null;
15. private wrapBuilder: WrappedBuilder<[]> = wrapBuilder(flowerBuilder);
16. private needCreate: boolean = false;
17. private isRemove: boolean = false;

19. constructor(create: boolean) {
20. super();
21. this.needCreate = create;
22. }

24. makeNode(uiContext: UIContext): FrameNode | null {
25. if (this.isRemove === true) {
26. return null;
27. }
28. if (this.needCreate && this.flowerNode === null) {
29. this.flowerNode = new BuilderNode(uiContext);
30. this.flowerNode.build(this.wrapBuilder);
31. }
32. if (this.flowerNode === null) {
33. return null;
34. }
35. return this.flowerNode!.getFrameNode()!;
36. }

38. getNode(): BuilderNode<[]> | null {
39. return this.flowerNode;
40. }

42. setNode(node: BuilderNode<[]> | null) {
43. this.flowerNode = node;
44. this.rebuild();
45. }

47. onRemove() {
48. this.isRemove = true;
49. this.rebuild();
50. this.isRemove = false;
51. }

53. init(uiContext: UIContext) {
54. this.flowerNode = new BuilderNode(uiContext);
55. this.flowerNode.build(this.wrapBuilder);
56. }
57. }

59. let myNode: MyNodeController | undefined;

61. export const createMyNode =
62. (uiContext: UIContext) => {
63. myNode = new MyNodeController(false);
64. myNode.init(uiContext);
65. }

67. export const getMyNode = (): MyNodeController | undefined => {
68. return myNode;
69. }
```

[CustomComponentBindSheet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/NodeContainer/CustomComponentBindSheet.ets#L15-L86)

```
1. // ComponentAttrUtils.ets
2. // 获取组件相对窗口的位置
3. import { componentUtils, UIContext } from '@kit.ArkUI';
4. import { JSON } from '@kit.ArkTS';

6. export class ComponentAttrUtils {
7. // 根据组件的id获取组件的位置信息
8. public static getRectInfoById(context: UIContext, id: string): RectInfoInPx {
9. if (!context || !id) {
10. throw Error('object is empty');
11. }
12. let componentInfo: componentUtils.ComponentInfo = context.getComponentUtils().getRectangleById(id);

14. if (!componentInfo) {
15. throw Error('object is empty');
16. }

18. let rstRect: RectInfoInPx = new RectInfoInPx();
19. const widthScaleGap = componentInfo.size.width * (1 - componentInfo.scale.x) / 2;
20. const heightScaleGap = componentInfo.size.height * (1 - componentInfo.scale.y) / 2;
21. rstRect.left = componentInfo.translate.x + componentInfo.windowOffset.x + widthScaleGap;
22. rstRect.top = componentInfo.translate.y + componentInfo.windowOffset.y + heightScaleGap;
23. rstRect.right =
24. componentInfo.translate.x + componentInfo.windowOffset.x + componentInfo.size.width - widthScaleGap;
25. rstRect.bottom =
26. componentInfo.translate.y + componentInfo.windowOffset.y + componentInfo.size.height - heightScaleGap;
27. rstRect.width = rstRect.right - rstRect.left;
28. rstRect.height = rstRect.bottom - rstRect.top;
29. return {
30. left: rstRect.left,
31. right: rstRect.right,
32. top: rstRect.top,
33. bottom: rstRect.bottom,
34. width: rstRect.width,
35. height: rstRect.height
36. }
37. }
38. }

40. export class RectInfoInPx {
41. public left: number = 0;
42. public top: number = 0;
43. public right: number = 0;
44. public bottom: number = 0;
45. public width: number = 0;
46. public height: number = 0;
47. }

49. export class RectJson {
50. public $rect: Array<number> = [];
51. }
```

[ComponentAttrUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/utils/ComponentAttrUtils.ets#L16-L69)

```
1. // WindowUtils.ets
2. // 窗口信息
3. import { window } from '@kit.ArkUI';

5. export class WindowUtils {
6. public static window: window.Window;
7. public static windowWidthPx: number;
8. public static windowHeightPx: number;
9. public static topAvoidAreaHeightPx: number;
10. public static navigationIndicatorHeightPx: number;
11. }
```

[WindowUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/utils/WindowUtils.ets#L16-L29)

```
1. // EntryAbility.ets
2. // 程序入口处的onWindowStageCreate增加对窗口宽高等的抓取

4. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
5. import { WindowUtils } from '../utils/WindowUtils';
6. import { display, window } from '@kit.ArkUI';
7. import { hilog } from '@kit.PerformanceAnalysisKit';

9. const DOMAIN = 0x0000;
10. const TAG: string = 'EntryAbility';

12. export default class EntryAbility extends UIAbility {
13. private currentBreakPoint: string = '';

15. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
16. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onCreate');
17. }

19. onDestroy(): void {
20. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onDestroy');
21. }

23. onWindowStageCreate(windowStage: window.WindowStage): void {
24. // Main window is created, set main page for this ability
25. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageCreate');
26. // ...
27. // 获取窗口宽高
28. WindowUtils.window = windowStage.getMainWindowSync();
29. WindowUtils.windowWidthPx = WindowUtils.window.getWindowProperties().windowRect.width;
30. WindowUtils.windowHeightPx = WindowUtils.window.getWindowProperties().windowRect.height;

32. this.updateBreakpoint(WindowUtils.windowWidthPx);

34. // 获取上方避让区(状态栏等)高度
35. let avoidArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
36. WindowUtils.topAvoidAreaHeightPx = avoidArea.topRect.height;

38. // 获取导航条高度
39. let navigationArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
40. WindowUtils.navigationIndicatorHeightPx = navigationArea.bottomRect.height;

42. hilog.info(DOMAIN, TAG, 'the width is ' + WindowUtils.windowWidthPx + '  ' + WindowUtils.windowHeightPx + '  ' +
43. WindowUtils.topAvoidAreaHeightPx + '  ' + WindowUtils.navigationIndicatorHeightPx);

45. // 监听窗口尺寸、状态栏高度及导航条高度的变化并更新
46. try {
47. WindowUtils.window.on('windowSizeChange', (data) => {
48. hilog.info(DOMAIN, TAG, 'on windowSizeChange, the width is ' + data.width + ', the height is ' + data.height);
49. WindowUtils.windowWidthPx = data.width;
50. WindowUtils.windowHeightPx = data.height;
51. this.updateBreakpoint(data.width);
52. AppStorage.setOrCreate('windowSizeChanged', Date.now());
53. })

55. WindowUtils.window.on('avoidAreaChange', (data) => {
56. if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
57. let topRectHeight = data.area.topRect.height;
58. hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the top avoid area height is ' + topRectHeight);
59. WindowUtils.topAvoidAreaHeightPx = topRectHeight;
60. } else if (data.type === window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
61. let bottomRectHeight = data.area.bottomRect.height;
62. hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the navigation indicator height is ' + bottomRectHeight);
63. WindowUtils.navigationIndicatorHeightPx = bottomRectHeight;
64. }
65. })
66. } catch (exception) {
67. hilog.error(DOMAIN, TAG, `register failed. code: ${exception.code}, message: ${exception.message}`);
68. }

70. windowStage.loadContent('pages/Index', (err) => {
71. if (err.code) {
72. hilog.error(DOMAIN, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
73. return;
74. }
75. hilog.info(DOMAIN, TAG, 'Succeeded in loading the content.');
76. });
77. }

79. updateBreakpoint(width: number) {
80. let windowWidthVp = width / (display.getDefaultDisplaySync().densityDPI / 160);
81. let newBreakPoint: string = '';
82. if (windowWidthVp < 400) {
83. newBreakPoint = 'xs';
84. } else if (windowWidthVp < 600) {
85. newBreakPoint = 'sm';
86. } else if (windowWidthVp < 800) {
87. newBreakPoint = 'md';
88. } else {
89. newBreakPoint = 'lg';
90. }
91. if (this.currentBreakPoint !== newBreakPoint) {
92. this.currentBreakPoint = newBreakPoint;
93. // 使用状态变量记录当前断点值
94. AppStorage.setOrCreate('currentBreakpoint', this.currentBreakPoint);
95. }
96. }
97. onWindowStageDestroy(): void {
98. // Main window is destroyed, release UI related resources
99. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageDestroy');
100. }

102. onForeground(): void {
103. // Ability has brought to foreground
104. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onForeground');
105. }

107. onBackground(): void {
108. // Ability has back to background
109. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onBackground');
110. }
111. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/entryability/EntryAbility.ets#L15-L161)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/AsR98LiaTuCtESpqqKznLQ/zh-cn_image_0000002558764480.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=4D4B11B09806833E1AF26465F04AC15CC90CEE71B45E7824515CA7618996A601)

## 使用geometryTransition共享元素转场

[geometryTransition](../harmonyos-references/ts-transition-animation-geometrytransition.md)用于组件内隐式共享元素转场，在视图状态切换过程中提供丝滑的上下文继承过渡体验。

geometryTransition的使用方式为对需要添加一镜到底动效的两个组件使用geometryTransition接口绑定同一id，这样在其中一个组件消失同时另一个组件创建出现的时候，系统会对二者添加一镜到底动效。

geometryTransition绑定两个对象的实现方式使得geometryTransition区别于其他方法，最适合用于两个不同对象之间完成一镜到底。

### geometryTransition的简单使用

对于同一个页面中的两个元素的一镜到底效果，geometryTransition接口的简单使用示例如下：

```
1. import { curves } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct IfElseGeometryTransition {
6. @State isShow: boolean = false;

8. build() {
9. Stack({ alignContent: Alignment.Center }) {
10. if (this.isShow) {
11. // 请将$r('app.media.spring')替换为实际资源文件
12. Image($r('app.media.spring'))
13. .autoResize(false)
14. .clip(true)
15. .width(200)
16. .height(200)
17. .borderRadius(100)
18. .geometryTransition('picture')
19. .transition(TransitionEffect.OPACITY)
20. // 在打断场景下，即动画过程中点击页面触发下一次转场，如果不加id，则会出现重影
21. // 加了id之后，新建的spring图片会复用之前的spring图片节点，不会重新创建节点，也就不会有重影问题
22. // 加id的规则为加在if和else下的第一个节点上，有多个并列节点则也需要进行添加
23. .id('item1')
24. } else {
25. // geometryTransition此处绑定的是容器，那么容器内的子组件需设为相对布局跟随父容器变化，
26. // 套多层容器为了说明相对布局约束传递
27. Column() {
28. Column() {
29. // 请将$r('app.media.sunset_sky')替换为实际资源文件
30. Image($r('app.media.sunset_sky'))
31. .size({ width: '100%', height: '100%' })
32. }
33. .size({ width: '100%', height: '100%' })
34. }
35. .width(100)
36. .height(100)
37. // geometryTransition会同步圆角，但仅限于geometryTransition绑定处，此处绑定的是容器
38. // 则对容器本身有圆角同步而不会操作容器内部子组件的borderRadius
39. .borderRadius(50)
40. .clip(true)
41. .geometryTransition('picture')
42. // transition保证节点离场不被立即析构，设置通用转场效果
43. .transition(TransitionEffect.OPACITY)
44. .position({ x: 40, y: 40 })
45. .id('item2')
46. }
47. }
48. .onClick(() => {
49. this.getUIContext()?.animateTo({
50. curve: curves.springMotion()
51. }, () => {
52. this.isShow = !this.isShow;
53. })
54. })
55. .size({ width: '100%', height: '100%' })
56. }
57. }
```

[IfElseGeometryTransition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template6/IfElseGeometryTransition.ets#L15-L74)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/bj2zO0bAT5GwHnl97Zb-7w/zh-cn_image_0000002558604824.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=59167B6855910939CC9B52BBFFF020CC9940215F5A250BBEE15D0223EF81AA91)

### geometryTransition结合模态转场使用

更多的场景中，需要对一个页面的元素与另一个页面的元素添加一镜到底动效。可以通过geometryTransition搭配模态转场接口实现。以点击头像弹出个人信息页的demo为例：

```
1. import { common } from '@kit.AbilityKit';

3. class PostData {
4. // 请将$r('app.media.flower')替换为实际资源文件
5. avatar: Resource = $r('app.media.flower');
6. name: string = '';
7. message: ResourceStr = '';
8. images: Resource[] = [];
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State isPersonalPageShow: boolean = false;
15. @State selectedIndex: number = 0;
16. @State alphaValue: number = 1;
17. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

19. // 数组中图片均使用Resource资源，需用户自定义
20. private allPostData: PostData[] = [
21. {
22. // 请将$r('app.media.flower')替换为实际资源文件
23. avatar: $r('app.media.flower'),
24. name: 'Alice',
25. // 请将$r('app.string.shareTransition_text1')替换为实际资源文件，在本示例中该资源文件的value值为"天气晴朗"
26. message: $r('app.string.shareTransition_text1'),
27. // 请将$r('app.media.spring')替换为实际资源文件
28. // 请将$r('app.media.tall_tree')替换为实际资源文件
29. images: [$r('app.media.spring'), $r('app.media.tall_tree')]
30. },
31. {
32. // 请将$r('app.media.sunset_sky')替换为实际资源文件
33. avatar: $r('app.media.sunset_sky'),
34. name: 'Bob',
35. // 请将$r('app.string.shareTransition_text2')替换为实际资源文件，在本示例中该资源文件的value值为"你好世界"
36. message: $r('app.string.shareTransition_text2'),
37. // 请将$r('app.media.island')替换为实际资源文件
38. images: [$r('app.media.island')]
39. },
40. {
41. // 请将$r('app.media.tall_tree')替换为实际资源文件
42. avatar: $r('app.media.tall_tree'),
43. name: 'Carl',
44. // 请将$r('app.string.shareTransition_text3')替换为实际资源文件，在本示例中该资源文件的value值为"万物生长"
45. message: $r('app.string.shareTransition_text3'),
46. // 请将$r('app.media.flower')替换为实际资源文件
47. // 请将$r('app.media.sunset_sky')替换为实际资源文件
48. // 请将$r('app.media.spring')替换为实际资源文件
49. images: [$r('app.media.flower'), $r('app.media.sunset_sky'), $r('app.media.spring')]
50. }];

52. private onAvatarClicked(index: number): void {
53. this.selectedIndex = index;
54. this.getUIContext()?.animateTo({
55. duration: 350,
56. curve: Curve.Friction
57. }, () => {
58. this.isPersonalPageShow = !this.isPersonalPageShow;
59. this.alphaValue = 0;
60. });
61. }

63. private onPersonalPageBack(index: number): void {
64. this.getUIContext()?.animateTo({
65. duration: 350,
66. curve: Curve.Friction
67. }, () => {
68. this.isPersonalPageShow = !this.isPersonalPageShow;
69. this.alphaValue = 1;
70. });
71. }

73. @Builder
74. PersonalPageBuilder(index: number) {
75. Column({ space: 20 }) {
76. Image(this.allPostData[index].avatar)
77. .size({ width: 200, height: 200 })
78. .borderRadius(100)
79. // 头像配置共享元素效果，与点击的头像的id匹配
80. .geometryTransition(index.toString())
81. .clip(true)
82. .transition(TransitionEffect.opacity(0.99))

84. Text(this.allPostData[index].name)
85. .font({ size: 30, weight: 600 })
86. // 对文本添加出现转场效果
87. .transition(TransitionEffect.asymmetric(
88. TransitionEffect.OPACITY
89. .combine(TransitionEffect.translate({ y: 100 })),
90. TransitionEffect.OPACITY.animation({ duration: 0 })
91. ))

93. // 请在resources\base\element\string.json文件中配置name为'shareTransition_text11'，value为非空字符串的资源
94. Text(this.context.resourceManager.getStringByNameSync('shareTransition_text11') + this.allPostData[index].name)
95. // 对文本添加出现转场效果
96. .transition(TransitionEffect.asymmetric(
97. TransitionEffect.OPACITY
98. .combine(TransitionEffect.translate({ y: 100 })),
99. TransitionEffect.OPACITY.animation({ duration: 0 })
100. ))
101. }
102. .padding({ top: 20 })
103. .size({ width: 360, height: 780 })
104. .backgroundColor(Color.White)
105. .onClick(() => {
106. this.onPersonalPageBack(index);
107. })
108. .transition(TransitionEffect.asymmetric(
109. TransitionEffect.opacity(0.99),
110. TransitionEffect.OPACITY
111. ))
112. }

114. build() {
115. Column({ space: 20 }) {
116. ForEach(this.allPostData, (postData: PostData, index: number) => {
117. Column() {
118. Post({
119. data: postData, index: index, onAvatarClicked: (index: number) => {
120. this.onAvatarClicked(index);
121. }
122. })
123. }
124. .width('100%')
125. }, (postData: PostData, index: number) => index.toString())
126. }
127. .size({ width: '100%', height: '100%' })
128. .backgroundColor('#40808080')
129. .bindContentCover(this.isPersonalPageShow,
130. this.PersonalPageBuilder(this.selectedIndex), { modalTransition: ModalTransition.NONE })
131. .opacity(this.alphaValue)
132. }
133. }

135. @Component
136. export default struct Post {
137. @Prop data: PostData;
138. @Prop index: number;
139. @State expandImageSize: number = 100;
140. @State avatarSize: number = 50;
141. private onAvatarClicked: (index: number) => void = (index: number) => { };

143. build() {
144. Column({ space: 20 }) {
145. Row({ space: 10 }) {
146. Image(this.data.avatar)
147. .size({ width: this.avatarSize, height: this.avatarSize })
148. .borderRadius(this.avatarSize / 2)
149. .clip(true)
150. .onClick(() => {
151. this.onAvatarClicked(this.index);
152. })
153. // 对头像绑定共享元素转场的id
154. .geometryTransition(this.index.toString(), { follow: true })
155. .transition(TransitionEffect.OPACITY.animation({ duration: 350, curve: Curve.Friction }))

157. Text(this.data.name)
158. }
159. .justifyContent(FlexAlign.Start)

161. Text(this.data.message)

163. Row({ space: 15 }) {
164. ForEach(this.data.images, (imageResource: Resource, index: number) => {
165. Image(imageResource)
166. .size({ width: 100, height: 100 })
167. }, (imageResource: Resource, index: number) => index.toString())
168. }
169. }
170. .backgroundColor(Color.White)
171. .size({ width: '100%', height: 250 })
172. .alignItems(HorizontalAlign.Start)
173. .padding({ left: 10, top: 10 })
174. }
175. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/shareTransition/template7/Index.ets#L16-L193)

效果为点击主页的头像后，弹出模态页面显示个人信息，并且两个页面之间的头像做一镜到底动效：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Dp2dGyGcQrKfvuUhEUhhuw/zh-cn_image_0000002589324349.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=5BB3CA0DBFDC551C5341366916485F64544E0133C27994A92BDF59099BD2510D)

## 示例代码

* [转场动效合集](https://gitcode.com/harmonyos_samples/transitions-collection)
