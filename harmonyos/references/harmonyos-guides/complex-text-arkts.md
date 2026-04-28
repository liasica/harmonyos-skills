---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-arkts
title: 复杂文本绘制与显示（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 复杂文本绘制与显示（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d3a4e8e8bf0339e881018eb04018c15f1fdc7a2367e3c1d2fca1928dfb2bd9b5
---

在进行文本绘制时，可以通过选择合适的字体、大小和颜色完成简单文本的绘制与显示；此外，还支持通过设置其他丰富的样式、语言、段落等进行复杂文本的绘制。

复杂文本绘制主要包含以下几个场景：

* 多语言文本绘制与显示
* 多行文本绘制与显示
* 多样式文本绘制与显示

## 多语言文本绘制与显示

多语言支持是全球化应用的基础。多语言文本绘制需要支持不同语言的字符集及其独特的显示需求，例如右到左语言（如阿拉伯语）或竖排文本（如中文）。开发者需要理解不同语言的渲染特性，确保文本的正确显示。

在多语言文本使用的场景下，主要通过指定[TextStyle](../harmonyos-references/js-apis-graphics-text.md#textstyle)文本样式中的**locale**字段来实现，可直接通过locale字段的值优先匹配对应字体，跳过遍历列表匹配字体的过程，从而降低匹配时间和内存使用。

### 开发步骤

1. 通过context获取到Canvas画布对象。

   ```
   1. // 绘制代码逻辑写在这里
   2. let canvas = context.canvas;
   ```

   [MultilanguageText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multilanguage/MultilanguageText.ets#L23-L26)
2. 初始化文本样式。

   ```
   1. let myTextStyle: text.TextStyle = {
   2. color: {
   3. alpha: 255,
   4. red: 255,
   5. green: 0,
   6. blue: 0
   7. },
   8. fontSize: 50,
   9. // 设置语言偏好为简体中文
   10. locale: 'zh-Hans'
   11. };
   ```

   [MultilanguageText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multilanguage/MultilanguageText.ets#L28-L40)
3. 初始化段落样式。

   ```
   1. let myParagraphStyle: text.ParagraphStyle = {
   2. textStyle: myTextStyle,
   3. };
   ```

   [MultilanguageText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multilanguage/MultilanguageText.ets#L42-L46)
4. 初始化段落对象，并添加文本。

   ```
   1. let fontCollection = text.FontCollection.getGlobalInstance();
   2. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   3. // 更新文本样式
   4. paragraphBuilder.pushStyle(myTextStyle);
   5. // 添加文本
   6. paragraphBuilder.addText('你好，世界');
   ```

   [MultilanguageText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multilanguage/MultilanguageText.ets#L47-L54)
5. 排版段落并进行文本绘制。

   ```
   1. // 生成段落
   2. let paragraph = paragraphBuilder.build();
   3. // 布局
   4. paragraph.layoutSync(1250);
   5. // 绘制文本
   6. paragraph.paint(canvas, 10, 0);
   ```

   [MultilanguageText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multilanguage/MultilanguageText.ets#L55-L62)

### 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/VabGSeXCT2OPpDMbGIaOeA/zh-cn_image_0000002583438721.png?HW-CC-KV=V1&HW-CC-Date=20260427T234715Z&HW-CC-Expire=86400&HW-CC-Sign=9F424324D66088935643BCA9CC10127E2316BF1C2A399329EC7067189E07EDA5)

## 多行文本绘制与显示

多行文本相对于单行文本比较复杂，一般针对多行文本，需要进行文本排版、断词策略设置、文本对齐方式、最大行数限制等，主要通过设置段落样式实现。

### 实现说明

**段落样式**（[ParagraphStyle](../harmonyos-references/js-apis-graphics-text.md#paragraphstyle)）是对多行文本中每段内容的样式设置，包括断词策略、文本对齐方式、最大行数限制等。开发者可以通过对不同段落进行样式化，以提高文本的可读性和美观性。

### 开发步骤

1. 通过context获取到Canvas画布对象。

   ```
   1. // 绘制代码逻辑写在这里
   2. let canvas = context.canvas;
   ```

   [MultilineText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multiline/MultilineText.ets#L23-L26)
2. 初始化文本样式。

   ```
   1. let myTextStyle: text.TextStyle = {
   2. color: {
   3. alpha: 255,
   4. red: 255,
   5. green: 0,
   6. blue: 0
   7. },
   8. fontSize: 50,
   9. // 当wordBreak为text.WordBreak.BREAK_HYPHEN时，需要为段落设置语言偏好，段落会在不同语言偏好下呈现不同的文本断词效果
   10. locale: 'en-gb'
   11. };
   ```

   [MultilineText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multiline/MultilineText.ets#L28-L40)
3. 初始化段落样式。

   ```
   1. let myParagraphStyle: text.ParagraphStyle = {
   2. textStyle: myTextStyle,
   3. // 文本对齐方式
   4. align: text.TextAlign.LEFT,
   5. // 最大行数
   6. maxLines: 3,
   7. // 断词策略
   8. wordBreak: text.WordBreak.BREAK_WORD
   9. };
   ```

   [MultilineText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multiline/MultilineText.ets#L42-L52)
4. 初始化段落对象，并添加占位符和文本。

   ```
   1. let fontCollection = text.FontCollection.getGlobalInstance();
   2. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   3. // 更新文本样式
   4. paragraphBuilder.pushStyle(myTextStyle);
   5. // 添加文本
   6. paragraphBuilder.addText('Hello World Hello World Hello World Hello World Hello World Hello World ' +
   7. 'Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World ' +
   8. 'Hello World Hello World Hello World Hello World Hello World ');
   ```

   [MultilineText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multiline/MultilineText.ets#L53-L62)
5. 排版段落并进行文本绘制。

   ```
   1. // 生成段落
   2. let paragraph = paragraphBuilder.build();
   3. // 布局
   4. paragraph.layoutSync(1250);
   5. // 绘制文本
   6. paragraph.paint(canvas, 10, 0);
   ```

   [MultilineText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/multiline/MultilineText.ets#L70-L77)

### 效果展示

| 段落样式设置（断词策略、文本对齐方式、最大行数限制） | 效果示意 |
| --- | --- |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为3，断词策略为text.WordBreak.BREAK\_WORD。 |  |
| 文本对齐方式为text.TextAlign.RIGHT，最大行数为3，断词策略为text.WordBreak.BREAK\_WORD。 |  |
| 文本对齐方式为text.TextAlign.JUSTIFY，最大行数为10，断词策略为text.WordBreak.BREAK\_WORD。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为3，断词策略为text.WordBreak.BREAK\_ALL。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_ALL。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_HYPHEN，  不设置语言偏好。段落无连字符“-”断词效果。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_HYPHEN，  语言偏好为en-gb（英式英语）。段落产生连字符“-”断词效果，并根据语言偏好呈现英式语言环境断词效果。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_HYPHEN，  语言偏好为en-us（美式英语）。段落产生连字符“-”断词效果，并根据语言偏好呈现美式语言环境断词效果。 |  |

## 多样式文本绘制与显示

除基本文字、排版属性之外，针对应用中不同文本的设计，开发者可能需要设置使用不同的绘制样式或能力，以凸显对应文本的独特表现或风格，此时可以结合使用多种绘制样式进行文本的渲染。

当前支持的多样式绘制及各绘制样式侧重效果如下：

* **装饰线样式绘制：** 主要通过不同的线条样式对文本进行装饰，可以使文本更加突出，富有表现力。
* **字体特性绘制：** 主要通过字体的变化，包括粗细、斜体等特性来改变文本的外观，增强文本的可读性和美观性。
* **可变字体绘制：** 对应提供文本在不同的显示环境和设备上灵活调整的能力，可满足更为精细的视觉效果。
* **文本阴影绘制：** 主要通过在文本周围添加阴影效果，以提升文本的层次感和立体感，从而使文本更具吸引力。
* **占位符绘制：** 可以在不确定文本内容时保持文本布局的稳定性，使得文本显示更为流畅和自然。
* **自动间距绘制：** 可以在一些字符混排切换的地方自动添加额外间距，提升阅读体验。
* **垂直对齐：** 调整文本在垂直方向排版位置，提升排版质量。
* **上下标：** 可以将任意字符处理成上标或下标，更精准表达文本含义。
* **高对比度文字绘制：** 主要通过将深色文字变黑、浅色文字变白，增强文本的对比效果。
* **行高调整：** 调整行高可改变文本行的垂直间距，使行间距更松散或更紧凑，显著改善文本垂直截断问题，提高可读性。
* **行间距调整：** 通过调整行间距的方式可以实现行高调整一样的效果，优化阅读体验。

### 装饰线

装饰线（[Decoration](../harmonyos-references/js-apis-graphics-text.md#decoration)）是指在文本上方、下方或中间添加的装饰性线条，当前支持上划线、下划线、删除线。

可以通过添加文本装饰线，提升文本的视觉效果和可读性。

使用装饰线需要初始化装饰线样式对象，并添加到文本样式中，从而在文本绘制时生效。

具体使用效果可参见下文[示例一](complex-text-arkts.md#示例一装饰线字体特征)。

### 字体特征

**字体特征**（[FontFeature](../harmonyos-references/js-apis-graphics-text.md#fontfeature)）绘制专注于在文本渲染过程中对字体特性（如粗体、斜体、字体变种等）的处理，允许字体在不同的排版场景下表现出不同的效果，可用于增强文本的表现力，使其更符合设计和阅读需求。

常见的**FontFeature**包含有liga、frac、case等，需要对应的ttf文件支持才能正常使能。

具体使用效果可参见下文[示例一](complex-text-arkts.md#示例一装饰线字体特征)。

### 可变字体

**可变字体**（[FontVariation](../harmonyos-references/js-apis-graphics-text.md#fontvariation)）是一种在一个字体文件中包含多个字形变体的字体格式，允许在一个字体文件内灵活地调整字体的各种属性（如字重、字宽、斜体等）。

与传统字体文件（每种变体需要一个独立的文件）不同，可变字体在一个字体文件中包含多个变体轴，可通过使用可变字体实现文本渲染绘制时的平滑过渡。

具体使用效果可参见下文[示例二](complex-text-arkts.md#示例二可变字体文本阴影占位符)。

### 文本阴影

**文本阴影**（[TextShadow](../harmonyos-references/js-apis-graphics-text.md#textshadow)）为文本提供了深度感，使得文本在背景上更具立体感。通常用于提升文本的视觉吸引力或增强可读性，尤其是在色彩对比度较低的场景下。

其中，TextShadow有三个属性，分别为阴影颜色color、阴影基于当前文本的偏移位置point、阴影半径blurRadius。

使用阴影效果需要在文本样式中设置对应的阴影效果数组，从而在文本绘制时生效。

具体使用效果可参见下文[示例二](complex-text-arkts.md#示例二可变字体文本阴影占位符)。

### 占位符

占位符绘制用于处理文本中占位符符号的渲染。

占位符也是用来实现图文混排的关键，是指在实际图像或内容注册之前，用来预先提供或替代某个位置的视觉元素。

具体使用效果可参见下文[示例二](complex-text-arkts.md#示例二可变字体文本阴影占位符)。

### 自动间距

使能自动间距，则会在文本排版时自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。例如，在中英文混排场景中，使能自动间距即可在中英文切换的地方自动添加额外间距，提升阅读体验。

关键示例如下：

```
1. let myParagraphStyle: text.ParagraphStyle = {
2. autoSpace: true
3. };
```

### 垂直对齐

垂直对齐用于调整文本在一行中垂直方向的排版位置。开启行高缩放或行内存在不同字号文本混排时使能垂直对齐，可以让文本实现顶部对齐、居中对齐、底部对齐或基线对齐（默认）。关键代码如下：

```
1. let myParagraphStyle: text.ParagraphStyle = {
2. verticalAlign: text.TextVerticalAlign.CENTER
3. };
```

具体使用效果可参见下文[示例三](complex-text-arkts.md#示例三垂直对齐)。

### 上下标

使能上下标，能将文本作为上标或下标参与排版。一般用于数学公式、化学式等场景。关键代码如下：

```
1. let superScriptStyle: text.TextStyle = {
2. badgeType: text.TextBadgeType.TEXT_SUPERSCRIPT
3. };
```

具体使用效果可参见下文[示例四](complex-text-arkts.md#示例四上下标文本)。

### 高对比度

高对比度可将深色文字变黑、浅色文字变白。开发者可选择开启或关闭应用的高对比度文字渲染，或遵循系统设置中的高对比度文字配置。

高对比度模式有3种，具体参考[TextHighContrast](../harmonyos-references/js-apis-graphics-text.md#texthighcontrast20)。

具体使用效果可参见下文[示例五](complex-text-arkts.md#示例五高对比度)。

### 行高调整

当前行高调整方式包括两种：设置行高上限/下限和使用行高缩放系数。

**行高调整（方式一）**

从API version 21开始，支持通过设置行高上限和下限调整行高，关键代码如下：

```
1. let myTextStyle: text.TextStyle = {
2. // 设置行高上限
3. lineHeightMaximum: 65,
4. // 设置行高下限
5. lineHeightMinimum: 65
6. };
```

使用效果参考下文[示例六](complex-text-arkts.md#示例六行高调整方式一)。

**行高调整（方式二）**

通过设置行高缩放系数调整行高，关键代码如下：

```
1. let myTextStyle: text.TextStyle = {
2. // 开启行高缩放开关
3. heightOnly: true,
4. // 设置行高缩放系数
5. heightScale: 1.5,
6. // 设置行高缩放风格
7. lineHeightStyle: text.LineHeightStyle.FONT_HEIGHT
8. };
```

使用效果参考下文[示例七](complex-text-arkts.md#示例七行高调整方式二)。

### 行间距调整

从API version 21开始，支持设置行间距改善文本行之间的距离，提高阅读体验，关键代码如下：

```
1. let myParagraphStyle: text.ParagraphStyle = {
2. // 设置行间距
3. lineSpacing: 100,
4. // 关闭段落上升部和下降部
5. textHeightBehavior: text.TextHeightBehavior.DISABLE_ALL,
6. };
```

具体使用效果可参见下文[示例八](complex-text-arkts.md#示例八行间距调整)。

### 示例一（装饰线、字体特征）

这里以文本样式中的装饰线和字体特征为例，呈现多样式文本的绘制与显示。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext } from '@kit.ArkUI'
2. import { UIContext } from '@kit.ArkUI'
3. import { text } from '@kit.ArkGraphics2D'

5. // 创建一个MyRenderNode类，并绘制文本。
6. class MyRenderNode extends RenderNode {
7. async draw(context: DrawContext) {
8. let canvas = context.canvas;

10. // 初始化装饰线对象
11. let decorations: text.Decoration =
12. {
13. // 装饰线类型，支持上划线、下划线、删除线
14. textDecoration: text.TextDecorationType.UNDERLINE,
15. // 装饰线颜色
16. color: {
17. alpha: 255,
18. red: 255,
19. green: 0,
20. blue: 0
21. },
22. // 装饰线样式，支持波浪，虚线，直线等
23. decorationStyle:text.TextDecorationStyle.SOLID,
24. // 装饰线的高度
25. decorationThicknessScale: 1
26. };

28. let myTextStyle: text.TextStyle = {
29. color: {
30. alpha: 255,
31. red: 255,
32. green: 0,
33. blue: 0
34. },
35. fontSize: 200,
36. // 设置装饰线
37. decoration: decorations,
38. // 开启字体特征
39. fontFeatures: [{name: 'frac', value: 1}]
40. };

42. let myParagraphStyle: text.ParagraphStyle = {
43. textStyle: myTextStyle,
44. };

46. let fontCollection = text.FontCollection.getGlobalInstance();
47. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

49. // 更新文本样式
50. paragraphBuilder.pushStyle(myTextStyle);
51. // 添加文本
52. paragraphBuilder.addText('1/2 1/3 1/4 ');

54. // 生成段落
55. let paragraph = paragraphBuilder.build();
56. // 布局
57. paragraph.layoutSync(1250);
58. // 绘制文本
59. paragraph.paint(canvas, 0, 0);
60. }
61. }

63. // 创建一个MyRenderNode对象
64. const textNode = new MyRenderNode();
65. // 定义newNode的像素格式
66. textNode.frame = {
67. x: 0,
68. y: 0,
69. width: 400,
70. height: 600
71. };
72. textNode.pivot = { x: 0.2, y: 0.8 };
73. textNode.scale = { x: 1, y: 1 };

75. class MyNodeController extends NodeController {
76. private rootNode: FrameNode | null = null;

78. makeNode(uiContext: UIContext): FrameNode {
79. this.rootNode = new FrameNode(uiContext);
80. if (this.rootNode == null) {
81. return this.rootNode;
82. }
83. const renderNode = this.rootNode.getRenderNode();
84. if (renderNode != null) {
85. renderNode.frame = {
86. x: 0,
87. y: 0,
88. width: 10,
89. height: 500
90. }
91. }
92. return this.rootNode;
93. }

95. addNode(node: RenderNode): void {
96. if (this.rootNode == null) {
97. return;
98. }
99. const renderNode = this.rootNode.getRenderNode();
100. if (renderNode != null) {
101. renderNode.appendChild(node);
102. }
103. }

105. clearNodes(): void {
106. if (this.rootNode == null) {
107. return;
108. }
109. const renderNode = this.rootNode.getRenderNode();
110. if (renderNode != null) {
111. renderNode.clearChildren();
112. }
113. }
114. }

116. let myNodeController: MyNodeController = new MyNodeController();

118. async function performTask() {
119. myNodeController.clearNodes();
120. myNodeController.addNode(textNode);
121. }

123. @Entry
124. @Component
125. struct Font08 {
126. @State src: Resource = $r('app.media.startIcon');
127. build() {
128. Column() {
129. Row() {
130. NodeContainer(myNodeController)
131. .height('100%')
132. .width('100%')
133. Image(this.src)
134. .width('0%').height('0%')
135. .onComplete(
136. () => {
137. performTask();
138. })
139. }
140. .width('100%')
141. }
142. }
143. }
```

[ComplexStyleExample1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample1.ets#L16-L160)

具体示意效果如下所示：

| 样式设置（装饰线样式、字体特征） | 示意效果 |
| --- | --- |
| 不开启装饰线和字体特征 |  |
| 开启装饰线和字体特征 |  |

### 示例二（可变字体、文本阴影、占位符）

这里以可变字体、文本阴影、占位符三个特性为例，呈现多样式文本的绘制与显示。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext } from '@kit.ArkUI'
2. import { UIContext } from '@kit.ArkUI'
3. import { drawing } from '@kit.ArkGraphics2D'
4. import { text } from '@kit.ArkGraphics2D'
5. import { common2D } from '@kit.ArkGraphics2D'

7. // 创建一个MyRenderNode类，并绘制文本。
8. class MyRenderNode extends RenderNode {
9. async draw(context: DrawContext) {
10. let canvas = context.canvas;

12. let myTextStyle: text.TextStyle = {
13. color: {
14. alpha: 255,
15. red: 255,
16. green: 0,
17. blue: 0
18. },
19. fontSize: 120,
20. // 可变字体
21. fontVariations: [{axis: 'wght', value: 555}],
22. // 文本阴影
23. textShadows: [{color: { alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00 }, point: {x:10,y:10}, blurRadius: 10}],
24. };

26. let myParagraphStyle: text.ParagraphStyle = {
27. textStyle: myTextStyle,
28. };

30. let fontCollection = text.FontCollection.getGlobalInstance();
31. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

33. // 初始化占位符对象
34. let myPlaceholderSpan: text.PlaceholderSpan = {
35. // 宽度
36. width: 300,
37. // 高度
38. height: 300,
39. // 基线对齐策略
40. align: text.PlaceholderAlignment.BOTTOM_OF_ROW_BOX,
41. // 使用的文本基线类型
42. baseline: text.TextBaseline.ALPHABETIC,
43. // 相比基线的偏移量。只有对齐策略是OFFSET_AT_BASELINE时生效
44. baselineOffset: 100
45. };
46. // 添加占位符
47. paragraphBuilder.addPlaceholder(myPlaceholderSpan);

49. // 更新文本样式
50. paragraphBuilder.pushStyle(myTextStyle);
51. // 添加文本
52. paragraphBuilder.addText('Hello Test');

54. // 生成段落
55. let paragraph = paragraphBuilder.build();
56. // 布局
57. paragraph.layoutSync(1250);
58. // 绘制文本
59. paragraph.paint(canvas, 0, 0);

61. //获取全部占位符的数组
62. let placeholderRects = paragraph.getRectsForPlaceholders();
63. // 获取第一个占位符的左边界
64. let left = placeholderRects[0].rect.left;
65. // 获取第一个占位符的上边界
66. let top = placeholderRects[0].rect.top;
67. // 获取第一个占位符的右边界
68. let right = placeholderRects[0].rect.right;
69. // 获取第一个占位符的下边界
70. let bottom = placeholderRects[0].rect.bottom;
71. let pen: drawing.Pen =  new drawing.Pen();
72. let penColor : common2D.Color = { alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00 };
73. pen.setColor(penColor);
74. canvas.attachPen(pen);
75. // 使用draw方法绘制占位符矩形框
76. canvas.drawRect(left,top,right,bottom);
77. }
78. }

80. // 创建一个MyRenderNode对象
81. const textNode = new MyRenderNode();
82. // 定义newNode的像素格式
83. textNode.frame = {
84. x: 0,
85. y: 0,
86. width: 400,
87. height: 600,
88. };
89. textNode.pivot = { x: 0.2, y: 0.8 };
90. textNode.scale = { x: 1, y: 1 };

92. class MyNodeController extends NodeController {
93. private rootNode: FrameNode | null = null;

95. makeNode(uiContext: UIContext): FrameNode {
96. this.rootNode = new FrameNode(uiContext);
97. if (this.rootNode == null) {
98. return this.rootNode;
99. }
100. const renderNode = this.rootNode.getRenderNode();
101. if (renderNode != null) {
102. renderNode.frame = {
103. x: 0,
104. y: 0,
105. width: 10,
106. height: 500
107. };
108. }
109. return this.rootNode;
110. }

112. addNode(node: RenderNode): void {
113. if (this.rootNode == null) {
114. return;
115. }
116. const renderNode = this.rootNode.getRenderNode();
117. if (renderNode != null) {
118. renderNode.appendChild(node);
119. }
120. }

122. clearNodes(): void {
123. if (this.rootNode == null) {
124. return;
125. }
126. const renderNode = this.rootNode.getRenderNode();
127. if (renderNode != null) {
128. renderNode.clearChildren();
129. }
130. }
131. }

133. let myNodeController: MyNodeController = new MyNodeController();

135. async function performTask() {
136. myNodeController.clearNodes();
137. myNodeController.addNode(textNode);
138. }

140. @Entry
141. @Component
142. struct Font08 {
143. @State src: Resource = $r('app.media.startIcon');
144. build() {
145. Column() {
146. Row() {
147. NodeContainer(myNodeController)
148. .height('100%')
149. .width('100%')
150. Image(this.src)
151. .width('0%').height('0%')
152. .onComplete(
153. () => {
154. performTask();
155. })
156. }
157. .width('100%')
158. }
159. }
160. }
```

[ComplexStyleExample2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample2.ets#L16-L177)

具体示意效果如下所示：

| 样式设置（可变字体、文本阴影、占位符） | 示意效果 |
| --- | --- |
| 不开启可变字体和文本阴影，不使用占位符 |  |
| 开启可变字体和文本阴影，使用占位符 |  |

### 示例三（垂直对齐）

这里以垂直对齐-居中对齐特性为例，呈现文本垂直方向排版的特性。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
2. import { text } from '@kit.ArkGraphics2D'

4. // 创建一个MyRenderNode类，并绘制文本。
5. class MyRenderNode extends RenderNode {
6. async draw(context: DrawContext) {
7. let canvas = context.canvas;

9. let myTextStyle: text.TextStyle = {
10. color: {
11. alpha: 255,
12. red: 255,
13. green: 0,
14. blue: 0
15. },
16. fontSize: 30,
17. // 开启行高缩放
18. heightOnly: true,
19. // 行高缩放系数为字号的2倍
20. heightScale: 2
21. };

23. let myParagraphStyle: text.ParagraphStyle = {
24. textStyle: myTextStyle,
25. // 设置垂直对齐-居中对齐模式
26. verticalAlign: text.TextVerticalAlign.CENTER,
27. };

29. let fontCollection = text.FontCollection.getGlobalInstance();
30. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

32. // 设置待排版文本要应用的样式
33. paragraphBuilder.pushStyle(myTextStyle);
34. // 添加文本
35. paragraphBuilder.addText('VerticalAlignment-center');

37. // 生成段落
38. let paragraph = paragraphBuilder.build();
39. // 布局
40. paragraph.layoutSync(1000);
41. // 绘制文本
42. paragraph.paint(canvas, 0, 0);
43. }
44. }

46. // 创建一个MyRenderNode对象
47. const textNode = new MyRenderNode();
48. // 定义newNode的像素格式
49. textNode.frame = {
50. x: 0,
51. y: 0,
52. width: 400,
53. height: 600
54. };
55. textNode.pivot = { x: 0.2, y: 0.8 };
56. textNode.scale = { x: 1, y: 1 };

58. class MyNodeController extends NodeController {
59. private rootNode: FrameNode | null = null;

61. makeNode(uiContext: UIContext): FrameNode {
62. this.rootNode = new FrameNode(uiContext);
63. if (this.rootNode == null) {
64. return this.rootNode;
65. }
66. const renderNode = this.rootNode.getRenderNode();
67. if (renderNode != null) {
68. renderNode.frame = {
69. x: 0,
70. y: 0,
71. width: 10,
72. height: 500
73. }
74. renderNode.pivot = { x: 50, y: 50 };
75. }
76. return this.rootNode;
77. }

79. addNode(node: RenderNode): void {
80. if (this.rootNode == null) {
81. return;
82. }
83. const renderNode = this.rootNode.getRenderNode();
84. if (renderNode != null) {
85. renderNode.appendChild(node);
86. }
87. }

89. clearNodes(): void {
90. if (this.rootNode == null) {
91. return;
92. }
93. const renderNode = this.rootNode.getRenderNode();
94. if (renderNode != null) {
95. renderNode.clearChildren();
96. }
97. }
98. }

100. let myNodeController: MyNodeController = new MyNodeController();

102. async function performTask() {
103. myNodeController.clearNodes();
104. myNodeController.addNode(textNode);
105. }

107. @Entry
108. @Component
109. struct Font08 {
110. @State src: Resource = $r('app.media.startIcon');
111. build() {
112. Column() {
113. Row() {
114. NodeContainer(myNodeController)
115. .height('100%')
116. .width('100%')
117. Text('Test for vertical alignment')
118. .onAppear(() => {
119. performTask();
120. })
121. }
122. .width('100%')
123. }
124. }
125. }
```

[ComplexStyleExample3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample3.ets#L16-L142)

具体示意效果如下所示：

| 样式设置（垂直对齐） | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| 基线对齐（默认） |  |
| 顶部对齐 |  |
| 居中对齐 |  |
| 底部对齐 |  |

### 示例四（上下标文本）

这里以下标样式为例，呈现上下标文本排版特性。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
2. import { text } from '@kit.ArkGraphics2D'

4. // 创建一个MyRenderNode类，并绘制文本。
5. class MyRenderNode extends RenderNode {
6. async draw(context: DrawContext) {
7. let canvas = context.canvas;

9. let myTextStyle: text.TextStyle = {
10. color: {
11. alpha: 255,
12. red: 255,
13. green: 0,
14. blue: 0
15. },
16. fontSize: 30,
17. };

19. let subScriptStyle: text.TextStyle = {
20. color: {
21. alpha: 255,
22. red: 255,
23. green: 0,
24. blue: 0
25. },
26. fontSize: 30,
27. // 设置下标样式
28. badgeType: text.TextBadgeType.TEXT_SUBSCRIPT
29. };

31. let myParagraphStyle: text.ParagraphStyle = {
32. textStyle: myTextStyle,
33. };

35. let fontCollection = text.FontCollection.getGlobalInstance();
36. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

38. // 设置待排版文本要应用的样式
39. paragraphBuilder.pushStyle(myTextStyle);
40. // 添加文本
41. paragraphBuilder.addText('The chemical formula for water: H');
42. paragraphBuilder.pushStyle(subScriptStyle);
43. paragraphBuilder.addText('2');
44. paragraphBuilder.pushStyle(myTextStyle);
45. paragraphBuilder.addText('o');

47. // 生成段落
48. let paragraph = paragraphBuilder.build();
49. // 布局
50. paragraph.layoutSync(1000);
51. // 绘制文本
52. paragraph.paint(canvas, 0, 0);
53. }
54. }

56. // 创建一个MyRenderNode对象
57. const textNode = new MyRenderNode();
58. // 定义newNode的像素格式
59. textNode.frame = {
60. x: 0,
61. y: 0,
62. width: 400,
63. height: 600
64. };
65. textNode.pivot = { x: 0.2, y: 0.8 };
66. textNode.scale = { x: 1, y: 1 };

68. class MyNodeController extends NodeController {
69. private rootNode: FrameNode | null = null;

71. makeNode(uiContext: UIContext): FrameNode {
72. this.rootNode = new FrameNode(uiContext);
73. if (this.rootNode == null) {
74. return this.rootNode;
75. }
76. const renderNode = this.rootNode.getRenderNode();
77. if (renderNode != null) {
78. renderNode.frame = {
79. x: 0,
80. y: 0,
81. width: 10,
82. height: 500
83. }
84. renderNode.pivot = { x: 50, y: 50 };
85. }
86. return this.rootNode;
87. }

89. addNode(node: RenderNode): void {
90. if (this.rootNode == null) {
91. return;
92. }
93. const renderNode = this.rootNode.getRenderNode();
94. if (renderNode != null) {
95. renderNode.appendChild(node);
96. }
97. }

99. clearNodes(): void {
100. if (this.rootNode == null) {
101. return;
102. }
103. const renderNode = this.rootNode.getRenderNode();
104. if (renderNode != null) {
105. renderNode.clearChildren();
106. }
107. }
108. }

110. let myNodeController: MyNodeController = new MyNodeController();

112. async function performTask() {
113. myNodeController.clearNodes();
114. myNodeController.addNode(textNode);
115. }

117. @Entry
118. @Component
119. struct Font08 {
120. @State src: Resource = $r('app.media.startIcon');
121. build() {
122. Column() {
123. Row() {
124. NodeContainer(myNodeController)
125. .height('100%')
126. .width('100%')
127. Text('Test for superscript and subscript')
128. .onAppear(() => {
129. performTask();
130. })
131. }
132. }
133. .width('100%')
134. }
135. }
```

[ComplexStyleExample4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample4.ets#L16-L152)

具体示意效果如下所示：

| 样式设置（上下标） | 示意效果 |
| --- | --- |
| 上标文本 |  |
| 下标文本 |  |

### 示例五（高对比度）

这里以高对比度为例，呈现高对比度文字的绘制与显示。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext, UIContext} from '@kit.ArkUI'
2. import { text } from '@kit.ArkGraphics2D'

4. // 创建一个MyRenderNode类，并绘制文本。
5. class MyRenderNode extends RenderNode {
6. async draw(context: DrawContext) {
7. let canvas = context.canvas;

9. // 开启APP的文字渲染高对比度配置
10. text.setTextHighContrast(text.TextHighContrast.TEXT_APP_ENABLE_HIGH_CONTRAST);

12. let myTextStyle: text.TextStyle = {
13. color: {
14. alpha: 255,
15. red: 111,
16. green: 255,
17. blue: 255
18. },
19. fontSize: 100,
20. };

22. let myParagraphStyle: text.ParagraphStyle = {
23. textStyle: myTextStyle,
24. };

26. let fontCollection = text.FontCollection.getGlobalInstance();
27. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

29. // 更新文本样式
30. paragraphBuilder.pushStyle(myTextStyle);
31. // 添加文本
32. paragraphBuilder.addText('Hello World');

34. // 生成段落
35. let paragraph = paragraphBuilder.build();
36. // 布局
37. paragraph.layoutSync(1250);
38. // 绘制文本
39. paragraph.paint(canvas, 10, 800);
40. }
41. }

43. // 创建一个MyRenderNode对象
44. const textNode = new MyRenderNode();
45. // 定义newNode的像素格式
46. textNode.frame = {
47. x: 0,
48. y: 0,
49. width: 400,
50. height: 600
51. };
52. textNode.pivot = { x: 0.2, y: 0.8 };
53. textNode.scale = { x: 1, y: 1 };

55. class MyNodeController extends NodeController {
56. private rootNode: FrameNode | null = null;

58. makeNode(uiContext: UIContext): FrameNode {
59. this.rootNode = new FrameNode(uiContext);
60. if (this.rootNode == null) {
61. return this.rootNode;
62. }
63. const renderNode = this.rootNode.getRenderNode();
64. if (renderNode != null) {
65. renderNode.frame = {
66. x: 0,
67. y: 0,
68. width: 10,
69. height: 500
70. };
71. renderNode.pivot = { x: 0.2, y: 0.8 };
72. }
73. return this.rootNode;
74. }

76. addNode(node: RenderNode): void {
77. if (this.rootNode == null) {
78. return;
79. }
80. const renderNode = this.rootNode.getRenderNode();
81. if (renderNode != null) {
82. renderNode.appendChild(node);
83. }
84. }

86. clearNodes(): void {
87. if (this.rootNode == null) {
88. return;
89. }
90. const renderNode = this.rootNode.getRenderNode();
91. if (renderNode != null) {
92. renderNode.clearChildren();
93. }
94. }
95. }

97. let myNodeController: MyNodeController = new MyNodeController();

99. async function performTask() {
100. myNodeController.clearNodes();
101. myNodeController.addNode(textNode);
102. }

104. @Entry
105. @Component
106. struct Font08 {
107. build() {
108. Column() {
109. Row() {
110. NodeContainer(myNodeController)
111. .height('100%')
112. .width('100%')
113. Text('Test high contrast')
114. .onAppear(() => {
115. performTask();
116. })
117. }
118. .width('100%')
119. }
120. }
121. }
```

[ComplexStyleExample5.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample5.ets#L16-L138)

具体示意效果如下所示：

| 高对比度设置 | 示意效果 |
| --- | --- |
| 不开启高对比度 |  |
| 开启高对比度 |  |

### 示例六（行高调整方式一）

这里以行高上限与行高下限设置相同值为例，呈现固定行高时的绘制表现。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
2. import { text } from '@kit.ArkGraphics2D'

4. // 创建一个MyRenderNode类，并绘制文本。
5. class MyRenderNode extends RenderNode {
6. async draw(context: DrawContext) {
7. let canvas = context.canvas;

9. let myTextStyle: text.TextStyle = {
10. color: {
11. alpha: 255,
12. red: 255,
13. green: 0,
14. blue: 0
15. },
16. fontSize: 50,
17. // 设置行高上限
18. lineHeightMaximum: 65,
19. // 设置行高下限
20. lineHeightMinimum: 65,
21. };

23. let myParagraphStyle: text.ParagraphStyle = {
24. textStyle: myTextStyle,
25. };

27. let fontCollection = text.FontCollection.getGlobalInstance();
28. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

30. // 设置待排版文本要应用的样式
31. paragraphBuilder.pushStyle(myTextStyle);
32. // 添加文本
33. paragraphBuilder.addText('Hello World!');

35. // 生成段落
36. let paragraph = paragraphBuilder.build();
37. // 布局
38. paragraph.layoutSync(1000);
39. // 绘制文本
40. paragraph.paint(canvas, 0, 0);
41. }
42. }

44. // 创建一个MyRenderNode对象
45. const textNode = new MyRenderNode()
46. // 定义newNode的像素格式
47. textNode.frame = {
48. x: 0,
49. y: 0,
50. width: 400,
51. height: 600
52. }
53. textNode.pivot = { x: 0.2, y: 0.8 };
54. textNode.scale = { x: 1, y: 1 };

56. class MyNodeController extends NodeController {
57. private rootNode: FrameNode | null = null;

59. makeNode(uiContext: UIContext): FrameNode {
60. this.rootNode = new FrameNode(uiContext)
61. if (this.rootNode == null) {
62. return this.rootNode;
63. }
64. const renderNode = this.rootNode.getRenderNode();
65. if (renderNode != null) {
66. renderNode.frame = {
67. x: 0,
68. y: 0,
69. width: 10,
70. height: 500
71. }
72. renderNode.pivot = { x: 50, y: 50 };
73. }
74. return this.rootNode;
75. }

77. addNode(node: RenderNode): void {
78. if (this.rootNode == null) {
79. return;
80. }
81. const renderNode = this.rootNode.getRenderNode();
82. if (renderNode != null) {
83. renderNode.appendChild(node);
84. }
85. }

87. clearNodes(): void {
88. if (this.rootNode == null) {
89. return;
90. }
91. const renderNode = this.rootNode.getRenderNode()
92. if (renderNode != null) {
93. renderNode.clearChildren();
94. }
95. }
96. }

98. let myNodeController: MyNodeController = new MyNodeController();

100. async function performTask() {
101. myNodeController.clearNodes();
102. myNodeController.addNode(textNode);
103. }

105. @Entry
106. @Component
107. struct Font08 {
108. @State src: Resource = $r('app.media.startIcon')
109. build() {
110. Column() {
111. Row() {
112. NodeContainer(myNodeController)
113. .height('100%')
114. .width('100%')
115. Text('Test for line height limit')
116. .onAppear(() => {
117. performTask();
118. })
119. }
120. }
121. .width('100%')
122. }
123. }
```

[ComplexStyleExample6.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample6.ets#L16-L140)

具体效果如下所示：

| 行高上限值 | 行高下限值 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- | --- |
| 65 | 65 |  |
| 200 | 200 |  |

### 示例七（行高调整方式二）

这里以行高缩放且行高缩放样式FontHeight为例，呈现行高调整后文字的绘制与显示。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
2. import { text } from '@kit.ArkGraphics2D'

4. // 创建一个MyRenderNode类，并绘制文本。
5. class MyRenderNode extends RenderNode {
6. async draw(context: DrawContext) {
7. let canvas = context.canvas;

9. let myTextStyle: text.TextStyle = {
10. color: {
11. alpha: 255,
12. red: 255,
13. green: 0,
14. blue: 0
15. },
16. fontSize: 50,
17. // 开启行高缩放开关
18. heightOnly: true,
19. // 设置行高缩放系数
20. heightScale: 1.5,
21. // 设置行高缩放风格
22. lineHeightStyle: text.LineHeightStyle.FONT_HEIGHT,
23. };

25. let myParagraphStyle: text.ParagraphStyle = {
26. textStyle: myTextStyle,
27. };

29. let fontCollection = text.FontCollection.getGlobalInstance();
30. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

32. // 设置待排版文本要应用的样式
33. paragraphBuilder.pushStyle(myTextStyle);
34. // 添加文本
35. paragraphBuilder.addText('Hello World!');

37. // 生成段落
38. let paragraph = paragraphBuilder.build();
39. // 布局
40. paragraph.layoutSync(1000);
41. // 绘制文本
42. paragraph.paint(canvas, 0, 0);
43. }
44. }

46. // 创建一个MyRenderNode对象
47. const textNode = new MyRenderNode();
48. // 定义newNode的像素格式
49. textNode.frame = {
50. x: 0,
51. y: 0,
52. width: 400,
53. height: 600
54. }
55. textNode.pivot = { x: 0.2, y: 0.8 };
56. textNode.scale = { x: 1, y: 1 };

58. class MyNodeController extends NodeController {
59. private rootNode: FrameNode | null = null;

61. makeNode(uiContext: UIContext): FrameNode {
62. this.rootNode = new FrameNode(uiContext)
63. if (this.rootNode == null) {
64. return this.rootNode;
65. }
66. const renderNode = this.rootNode.getRenderNode();
67. if (renderNode != null) {
68. renderNode.frame = {
69. x: 0,
70. y: 0,
71. width: 10,
72. height: 500
73. };
74. renderNode.pivot = { x: 50, y: 50 };
75. }
76. return this.rootNode;
77. }

79. addNode(node: RenderNode): void {
80. if (this.rootNode == null) {
81. return
82. }
83. const renderNode = this.rootNode.getRenderNode();
84. if (renderNode != null) {
85. renderNode.appendChild(node);
86. }
87. }

89. clearNodes(): void {
90. if (this.rootNode == null) {
91. return;
92. }
93. const renderNode = this.rootNode.getRenderNode()
94. if (renderNode != null) {
95. renderNode.clearChildren();
96. }
97. }
98. }

100. let myNodeController: MyNodeController = new MyNodeController();

102. async function performTask() {
103. myNodeController.clearNodes();
104. myNodeController.addNode(textNode);
105. }

107. @Entry
108. @Component
109. struct Font08 {
110. @State src: Resource = $r('app.media.startIcon')
111. build() {
112. Column() {
113. Row() {
114. NodeContainer(myNodeController)
115. .height('100%')
116. .width('100%')
117. Text('Test for line height limit')
118. .onAppear(() => {
119. performTask();
120. })
121. }
122. }
123. .width('100%')
124. }
125. }
```

[ComplexStyleExample7.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample7.ets#L16-L142)

具体效果如下所示：

| 行高缩放样式 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| FontSize |  |
| FontHeight |  |

### 示例八（行间距调整）

这里以关闭段落上升部下降部并设置行间距为例，呈现行间距增加后的文本绘制与显示。

```
1. import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
2. import { text } from '@kit.ArkGraphics2D'

4. // 创建一个MyRenderNode类，并绘制文本。
5. class MyRenderNode extends RenderNode {
6. async draw(context: DrawContext) {
7. let canvas = context.canvas;

9. let myTextStyle: text.TextStyle = {
10. color: {
11. alpha: 255,
12. red: 255,
13. green: 0,
14. blue: 0
15. },
16. fontSize: 50,
17. };

19. let myParagraphStyle: text.ParagraphStyle = {
20. textStyle: myTextStyle,
21. // 设置行间距
22. lineSpacing: 100,
23. // 关闭段落上升部和下降部
24. textHeightBehavior: text.TextHeightBehavior.DISABLE_ALL,
25. };

27. let fontCollection = text.FontCollection.getGlobalInstance();
28. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

30. // 设置待排版文本要应用的样式
31. paragraphBuilder.pushStyle(myTextStyle);
32. // 添加文本
33. paragraphBuilder.addText('Hello World!');

35. // 生成段落
36. let paragraph = paragraphBuilder.build();
37. // 布局
38. paragraph.layoutSync(200);
39. // 绘制文本
40. paragraph.paint(canvas, 0, 0);
41. }
42. }

44. // 创建一个MyRenderNode对象
45. const textNode = new MyRenderNode();
46. // 定义newNode的像素格式
47. textNode.frame = {
48. x: 0,
49. y: 0,
50. width: 400,
51. height: 600
52. }
53. textNode.pivot = { x: 0.2, y: 0.8 };
54. textNode.scale = { x: 1, y: 1 };

56. class MyNodeController extends NodeController {
57. private rootNode: FrameNode | null = null;

59. makeNode(uiContext: UIContext): FrameNode {
60. this.rootNode = new FrameNode(uiContext);
61. if (this.rootNode == null) {
62. return this.rootNode
63. }
64. const renderNode = this.rootNode.getRenderNode();
65. if (renderNode != null) {
66. renderNode.frame = {
67. x: 0,
68. y: 0,
69. width: 10,
70. height: 500
71. }
72. renderNode.pivot = { x: 50, y: 50 };
73. }
74. return this.rootNode;
75. }

77. addNode(node: RenderNode): void {
78. if (this.rootNode == null) {
79. return;
80. }
81. const renderNode = this.rootNode.getRenderNode();
82. if (renderNode != null) {
83. renderNode.appendChild(node);
84. }
85. }

87. clearNodes(): void {
88. if (this.rootNode == null) {
89. return;
90. }
91. const renderNode = this.rootNode.getRenderNode();
92. if (renderNode != null) {
93. renderNode.clearChildren();
94. }
95. }
96. }

98. let myNodeController: MyNodeController = new MyNodeController();

100. async function performTask() {
101. myNodeController.clearNodes();
102. myNodeController.addNode(textNode);
103. }

105. @Entry
106. @Component
107. struct Font08 {
108. @State src: Resource = $r('app.media.startIcon')
109. build() {
110. Column() {
111. Row() {
112. NodeContainer(myNodeController)
113. .height('100%')
114. .width('100%')
115. Text('Test for lineSpacing and height behavior')
116. .onAppear(() => {
117. performTask();
118. })
119. }
120. }
121. .width('100%')
122. }
123. }
```

[ComplexStyleExample8.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/complexStyle/ComplexStyleExample8.ets#L16-L140)

具体效果如下所示：

| 上升部下降部开关 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| DISABLE\_ALL |  |
| ALL |  |
