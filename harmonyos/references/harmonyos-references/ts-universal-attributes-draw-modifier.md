---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-draw-modifier
title: 自定义绘制设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 自定义绘制设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4751ffc49e642a12918dfc4864a13480ad22296aaf912b9359a83af0fdd668c9
---

当某些组件本身的绘制内容不满足需求时，可使用自定义组件绘制功能，在原有组件基础上部分绘制，或者全部自行绘制，以达到预期效果。例如：独特的按钮形状、文字和图像混合的图标等。自定义组件绘制提供了自定义绘制修改器，来实现更自由地组件绘制。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## drawModifier

PhonePC/2in1TabletTVWearable

drawModifier(modifier: DrawModifier | undefined): T

设置组件的自定义绘制修改器。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**组件支持范围:**

[AlphabetIndexer](ts-container-alphabet-indexer.md)、[Badge](ts-container-badge.md)、[Blank](ts-basic-components-blank.md)、[Button](ts-basic-components-button.md)、[CalendarPicker](ts-basic-components-calendarpicker.md)、[Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Circle](ts-drawing-components-circle.md)、[Column](ts-container-column.md)、[ColumnSplit](ts-container-columnsplit.md)、[Counter](ts-container-counter.md)、[DataPanel](ts-basic-components-datapanel.md)、[DatePicker](ts-basic-components-datepicker.md)、[Ellipse](ts-drawing-components-ellipse.md)、[Flex](ts-container-flex.md)、[FlowItem](ts-container-flowitem.md)、[FolderStack](ts-container-folderstack.md)、[FormLink](ts-container-formlink.md)、[Gauge](ts-basic-components-gauge.md)、[Grid](ts-container-grid.md)、[GridCol](ts-container-gridcol.md)、[GridItem](ts-container-griditem.md)、[GridRow](ts-container-gridrow.md)、[Hyperlink](ts-container-hyperlink.md)、[Image](ts-basic-components-image.md)、[ImageAnimator](ts-basic-components-imageanimator.md)、[ImageSpan](ts-basic-components-imagespan.md)、[Line](ts-drawing-components-line.md)、[List](ts-container-list.md)、[ListItem](ts-container-listitem.md)、[ListItemGroup](ts-container-listitemgroup.md)、[LoadingProgress](ts-basic-components-loadingprogress.md)、[Marquee](ts-basic-components-marquee.md)、[Menu](ts-basic-components-menu.md)、[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)、[NavDestination](ts-basic-components-navdestination.md)、[Navigation](ts-basic-components-navigation.md)、[Navigator](ts-container-navigator.md)、[NavRouter](ts-basic-components-navrouter.md)、[NodeContainer](ts-basic-components-nodecontainer.md)、[Path](ts-drawing-components-path.md)、[PatternLock](ts-basic-components-patternlock.md)、[Polygon](ts-drawing-components-polygon.md)、[Polyline](ts-drawing-components-polyline.md)、[Progress](ts-basic-components-progress.md)、[QRCode](ts-basic-components-qrcode.md)、[Radio](ts-basic-components-radio.md)、[Rating](ts-basic-components-rating.md)、[Rect](ts-drawing-components-rect.md)、[Refresh](ts-container-refresh.md)、[RelativeContainer](ts-container-relativecontainer.md)、[RichEditor](ts-basic-components-richeditor.md)、[Row](ts-container-row.md)、[RowSplit](ts-container-rowsplit.md)、[Scroll](ts-container-scroll.md)、[ScrollBar](ts-basic-components-scrollbar.md)、[Search](ts-basic-components-search.md)、[Select](ts-basic-components-select.md)、[Shape](ts-drawing-components-shape.md)、[SideBarContainer](ts-container-sidebarcontainer.md)、[Slider](ts-basic-components-slider.md)、[Stack](ts-container-stack.md)、[Stepper](ts-basic-components-stepper.md)、[StepperItem](ts-basic-components-stepperitem.md)、[Swiper](ts-container-swiper.md)、[SymbolGlyph](ts-basic-components-symbolglyph.md)、[TabContent](ts-container-tabcontent.md)、[Tabs](ts-container-tabs.md)、[Text](ts-basic-components-text.md)、[TextArea](ts-basic-components-textarea.md)、[TextClock](ts-basic-components-textclock.md)、[TextInput](ts-basic-components-textinput.md)、[TextPicker](ts-basic-components-textpicker.md)、[TextTimer](ts-basic-components-texttimer.md)、[TimePicker](ts-basic-components-timepicker.md)、[Toggle](ts-basic-components-toggle.md)、[WaterFlow](ts-container-waterflow.md)、[XComponent](ts-basic-components-xcomponent.md)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [DrawModifier](ts-universal-attributes-draw-modifier.md#drawmodifier-1) | undefined | 是 | 自定义绘制修改器，其中定义了自定义绘制的逻辑。  默认值：undefined  **说明：**  每个自定义修改器只对当前绑定组件的[FrameNode](js-apis-arkui-framenode.md)生效，对其子节点不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## DrawModifier

PhonePC/2in1TabletTVWearable

DrawModifier可设置遮罩层前景（drawOverlay）、前景（drawForeground）、内容前景（drawFront）、内容（drawContent）和内容背景（drawBehind）的绘制方法，还提供主动触发重绘的方法[invalidate](ts-universal-attributes-draw-modifier.md#invalidate)。每个DrawModifier实例只能设置到一个组件上，禁止进行重复设置。

自定义层级示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/rwCxU_LuT9CBy0WQjb4Plg/zh-cn_image_0000002558606440.png?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=8CFED5E651B23B70711BA3CB0FA665FB191ED42359CBABE4753FFAAC18AE4065)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### drawFront

PhonePC/2in1TabletTVWearable

drawFront?(drawContext: DrawContext): void

自定义绘制内容前景的接口，若重载该方法则可进行内容前景的自定义绘制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drawContext | [DrawContext](ts-universal-attributes-draw-modifier.md#drawcontext) | 是 | 图形绘制上下文。 |

**示例：**

请参考[示例1（通过DrawModifier进行自定义绘制）](ts-universal-attributes-draw-modifier.md#示例1通过drawmodifier进行自定义绘制)。

### drawContent

PhonePC/2in1TabletTVWearable

drawContent?(drawContext: DrawContext): void

自定义绘制内容的接口，若重载该方法则可进行内容的自定义绘制，会替换组件原本的内容绘制函数。

该接口的[DrawContext](js-apis-arkui-graphics.md#drawcontext)中的Canvas是用于记录指令的临时Canvas，并非节点的真实Canvas。使用请参见[调整自定义绘制Canvas的变换矩阵](../harmonyos-guides/arkts-user-defined-extension-drawmodifier.md#调整自定义绘制canvas的变换矩阵)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drawContext | [DrawContext](ts-universal-attributes-draw-modifier.md#drawcontext) | 是 | 图形绘制上下文。 |

**示例：**

请参考[示例1（通过DrawModifier进行自定义绘制）](ts-universal-attributes-draw-modifier.md#示例1通过drawmodifier进行自定义绘制)。

### drawBehind

PhonePC/2in1TabletTVWearable

drawBehind?(drawContext: DrawContext): void

自定义绘制背景的接口，若重载该方法则可进行背景的自定义绘制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drawContext | [DrawContext](ts-universal-attributes-draw-modifier.md#drawcontext) | 是 | 图形绘制上下文。 |

**示例：**

请参考[示例1（通过DrawModifier进行自定义绘制）](ts-universal-attributes-draw-modifier.md#示例1通过drawmodifier进行自定义绘制)。

### drawForeground20+

PhonePC/2in1TabletTVWearable

drawForeground(drawContext: DrawContext): void

自定义绘制前景的接口，若重载该方法则可进行前景的自定义绘制。需要对其组件的前景层进行绘制时重载该方法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drawContext | [DrawContext](ts-universal-attributes-draw-modifier.md#drawcontext) | 是 | 图形绘制上下文。 |

**示例：**

请参考[示例2（通过DrawModifier对容器的前景进行自定义绘制）](ts-universal-attributes-draw-modifier.md#示例2通过drawmodifier对容器的前景进行自定义绘制)。

### drawOverlay23+

PhonePC/2in1TabletTVWearable

drawOverlay(drawContext: DrawContext): void

自定义绘制遮罩层的接口，若重载该方法则可进行遮罩层的自定义绘制。需要对其组件的遮罩层进行绘制时重载该方法。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drawContext | [DrawContext](ts-universal-attributes-draw-modifier.md#drawcontext) | 是 | 图形绘制上下文。 |

**示例：**

```
1. // test.ets
2. import { drawing } from '@kit.ArkGraphics2D';

4. class MyForegroundDrawModifier extends DrawModifier {
5. public scaleX: number = 3;
6. public scaleY: number = 3;
7. uiContext: UIContext;

9. constructor(uiContext: UIContext) {
10. super();
11. this.uiContext = uiContext;
12. }

14. // 重载drawOverlay方法，实现自定义绘制遮罩层前景
15. drawOverlay(context: DrawContext): void {
16. const brush = new drawing.Brush();
17. brush.setColor({
18. alpha: 255,
19. red: 0,
20. green: 50,
21. blue: 100
22. });
23. context.canvas.attachBrush(brush);
24. const halfWidth = context.size.width / 2;
25. const halfHeight = context.size.height / 2;
26. context.canvas.drawRect({
27. left: this.uiContext.vp2px(halfWidth - 30 * this.scaleX),
28. top: this.uiContext.vp2px(halfHeight - 30 * this.scaleY),
29. right: this.uiContext.vp2px(halfWidth + 30 * this.scaleX),
30. bottom: this.uiContext.vp2px(halfHeight + 60 * this.scaleY)
31. });
32. }
33. }

35. @Entry
36. @Component
37. struct DrawModifierExample {
38. // 将自定义绘制遮罩层前景的类实例化，传入UIContext实例
39. private overlayModifier: MyForegroundDrawModifier = new MyForegroundDrawModifier(this.getUIContext());

41. build() {
42. Column() {
43. Text('此文本是子节点')
44. .fontSize(36)
45. .width('100%')
46. .height('100%')
47. .textAlign(TextAlign.Center)
48. }
49. .margin(50)
50. .width(280)
51. .height(300)
52. .backgroundColor(0x87CEEB)
53. // 调用此接口并传入自定义绘制前景的类实例，即可实现自定义绘制前景
54. .drawModifier(this.overlayModifier)
55. }
56. }
```

### invalidate

PhonePC/2in1TabletTVWearable

invalidate(): void

主动触发重绘的接口，开发者无需也无法重载，调用会触发所绑定组件的重绘。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[示例1（通过DrawModifier进行自定义绘制）](ts-universal-attributes-draw-modifier.md#示例1通过drawmodifier进行自定义绘制)。

### DrawContext

PhonePC/2in1TabletTVWearable

type DrawContext = DrawContext

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [DrawContext](js-apis-arkui-graphics.md#drawcontext) | 图形绘制上下文。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（通过DrawModifier进行自定义绘制）

通过DrawModifier对[Text](ts-basic-components-text.md)组件进行自定义绘制。

```
1. // xxx.ets
2. import { drawing } from '@kit.ArkGraphics2D';
3. import { AnimatorResult } from '@kit.ArkUI';

5. // 继承DrawModifier实现自定义绘制控制器
6. class MyFullDrawModifier extends DrawModifier {
7. public scaleX: number = 1;
8. public scaleY: number = 1;
9. uiContext: UIContext;

11. constructor(uiContext: UIContext) {
12. super();
13. this.uiContext = uiContext;
14. }

16. // 重载drawBehind方法，自定义绘制背景
17. drawBehind(context: DrawContext): void {
18. const brush = new drawing.Brush();
19. brush.setColor({
20. alpha: 255,
21. red: 255,
22. green: 0,
23. blue: 0
24. });
25. context.canvas.attachBrush(brush);
26. const halfWidth = context.size.width / 2;
27. const halfHeight = context.size.height / 2;
28. context.canvas.drawRect({
29. left: this.uiContext.vp2px(halfWidth - 50 * this.scaleX),
30. top: this.uiContext.vp2px(halfHeight - 50 * this.scaleY),
31. right: this.uiContext.vp2px(halfWidth + 50 * this.scaleX),
32. bottom: this.uiContext.vp2px(halfHeight + 50 * this.scaleY)
33. });
34. }

36. // 重载drawContent方法，自定义绘制内容
37. drawContent(context: DrawContext): void {
38. const brush = new drawing.Brush();
39. brush.setColor({
40. alpha: 255,
41. red: 0,
42. green: 255,
43. blue: 0
44. });
45. context.canvas.attachBrush(brush);
46. const halfWidth = context.size.width / 2;
47. const halfHeight = context.size.height / 2;
48. context.canvas.drawRect({
49. left: this.uiContext.vp2px(halfWidth - 30 * this.scaleX),
50. top: this.uiContext.vp2px(halfHeight - 30 * this.scaleY),
51. right: this.uiContext.vp2px(halfWidth + 30 * this.scaleX),
52. bottom: this.uiContext.vp2px(halfHeight + 30 * this.scaleY)
53. });
54. }

56. // 重载drawFront方法，自定义绘制内容前景
57. drawFront(context: DrawContext): void {
58. const brush = new drawing.Brush();
59. brush.setColor({
60. alpha: 255,
61. red: 0,
62. green: 0,
63. blue: 255
64. });
65. context.canvas.attachBrush(brush);
66. const halfWidth = context.size.width / 2;
67. const halfHeight = context.size.height / 2;
68. const radiusScale = (this.scaleX + this.scaleY) / 2;
69. context.canvas.drawCircle(this.uiContext.vp2px(halfWidth), this.uiContext.vp2px(halfHeight),
70. this.uiContext.vp2px(20 * radiusScale));
71. }
72. }

74. // 继承DrawModifier实现自定义绘制控制器，仅支持自定义绘制内容前景
75. class MyFrontDrawModifier extends DrawModifier {
76. public scaleX: number = 1;
77. public scaleY: number = 1;
78. uiContext: UIContext;

80. constructor(uiContext: UIContext) {
81. super();
82. this.uiContext = uiContext;
83. }

85. drawFront(context: DrawContext): void {
86. const brush = new drawing.Brush();
87. brush.setColor({
88. alpha: 255,
89. red: 0,
90. green: 0,
91. blue: 255
92. });
93. context.canvas.attachBrush(brush);
94. const halfWidth = context.size.width / 2;
95. const halfHeight = context.size.height / 2;
96. const radiusScale = (this.scaleX + this.scaleY) / 2;
97. context.canvas.drawCircle(this.uiContext.vp2px(halfWidth), this.uiContext.vp2px(halfHeight),
98. this.uiContext.vp2px(20 * radiusScale));
99. }
100. }

102. @Entry
103. @Component
104. struct DrawModifierExample {
105. private fullModifier: MyFullDrawModifier = new MyFullDrawModifier(this.getUIContext());
106. private frontModifier: MyFrontDrawModifier = new MyFrontDrawModifier(this.getUIContext());
107. private drawAnimator: AnimatorResult | undefined = undefined;
108. @State modifier: DrawModifier = new MyFrontDrawModifier(this.getUIContext());
109. private count = 0;

111. // 创建Animator对象并设置动画
112. create() {
113. let self = this;
114. this.drawAnimator = this.getUIContext().createAnimator({
115. duration: 1000,
116. easing: 'ease',
117. delay: 0,
118. fill: 'forwards',
119. direction: 'normal',
120. iterations: 1,
121. begin: 0,
122. end: 2
123. });
124. this.drawAnimator.onFrame = (value: number) => {
125. console.info('frame value =', value);
126. const tempModifier = self.modifier as MyFullDrawModifier | MyFrontDrawModifier;
127. tempModifier.scaleX = Math.abs(value - 1);
128. tempModifier.scaleY = Math.abs(value - 1);
129. // 主动触发重绘
130. self.modifier.invalidate();
131. };
132. }

134. build() {
135. Column() {
136. Row() {
137. Text('test text')
138. .width(100)
139. .height(100)
140. .margin(10)
141. .backgroundColor(Color.Gray)
142. .onClick(() => {
143. const tempModifier = this.modifier as MyFullDrawModifier | MyFrontDrawModifier;
144. tempModifier.scaleX -= 0.1;
145. tempModifier.scaleY -= 0.1;
146. })
147. .drawModifier(this.modifier)
148. }

150. Row() {
151. Button('create')
152. .width(100)
153. .height(100)
154. .borderRadius(50)
155. .margin(10)
156. .onClick(() => {
157. this.create();
158. })
159. Button('play')
160. .width(100)
161. .height(100)
162. .borderRadius(50)
163. .margin(10)
164. .onClick(() => {
165. if (this.drawAnimator) {
166. this.drawAnimator.play();
167. }
168. })
169. Button('changeModifier')
170. .width(100)
171. .height(100)
172. .borderRadius(50)
173. .margin(10)
174. .onClick(() => {
175. this.count += 1;
176. if (this.count % 2 === 1) {
177. console.info('change to full modifier');
178. this.modifier = this.fullModifier;
179. } else {
180. console.info('change to front modifier');
181. this.modifier = this.frontModifier;
182. }
183. })
184. }
185. }
186. .width('100%')
187. .height('100%')
188. }
189. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/9ylHAaoHRYqBCOqeHjYSEA/zh-cn_image_0000002589325967.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=20B68C4DAFEAEB9FFFE13CB4F04DC5AB2642D4A1BBD576B5FB102EA41851B08C)

### 示例2（通过DrawModifier对容器的前景进行自定义绘制）

通过DrawModifier对[Column](ts-container-column.md)容器的前景进行自定义绘制。

```
1. // xxx.ets
2. import { drawing } from '@kit.ArkGraphics2D';

4. class MyForegroundDrawModifier extends DrawModifier {
5. public scaleX: number = 3;
6. public scaleY: number = 3;
7. uiContext: UIContext;

9. constructor(uiContext: UIContext) {
10. super();
11. this.uiContext = uiContext;
12. }

14. // 重载drawForeground方法，实现自定义绘制前景
15. drawForeground(context: DrawContext): void {
16. const brush = new drawing.Brush();
17. brush.setColor({
18. alpha: 255,
19. red: 0,
20. green: 50,
21. blue: 100
22. });
23. context.canvas.attachBrush(brush);
24. const halfWidth = context.size.width / 2;
25. const halfHeight = context.size.height / 2;
26. context.canvas.drawRect({
27. left: this.uiContext.vp2px(halfWidth - 30 * this.scaleX),
28. top: this.uiContext.vp2px(halfHeight - 30 * this.scaleY),
29. right: this.uiContext.vp2px(halfWidth + 30 * this.scaleX),
30. bottom: this.uiContext.vp2px(halfHeight + 30 * this.scaleY)
31. });
32. }
33. }

35. @Entry
36. @Component
37. struct DrawModifierExample {
38. // 将自定义绘制前景的类实例化，传入UIContext实例
39. private foregroundModifier: MyForegroundDrawModifier = new MyForegroundDrawModifier(this.getUIContext());

41. build() {
42. Column() {
43. Text('此文本是子节点')
44. .fontSize(36)
45. .width('100%')
46. .height('100%')
47. .textAlign(TextAlign.Center)
48. }
49. .margin(50)
50. .width(280)
51. .height(300)
52. .backgroundColor(0x87CEEB)
53. // 调用此接口并传入自定义绘制前景的类实例，即可实现自定义绘制前景
54. .drawModifier(this.foregroundModifier)
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/AMG3dnA3T56iTlgjg_Ri9Q/zh-cn_image_0000002589245909.png?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=CC100DD2F21992831A21280D894662F00C7816497923B771CC557F645BD0EB05)
