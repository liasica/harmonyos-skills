---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils
title: Class (MeasureUtils)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (MeasureUtils)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1dfdc77053783483f3afdb2c03a17a9446b19e631f33730c651f9ac271060723
---

提供文本宽度、高度等相关计算。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需先使用UIContext中的[getMeasureUtils()](arkts-apis-uicontext-uicontext.md#getmeasureutils12)方法获取MeasureUtils实例，再通过此实例调用对应方法。
* 如需更多测算文本参数，建议使用图形对应测算接口[Paragraph](js-apis-graphics-text.md#paragraph)接口。
* 调用文本计算接口时，不推荐同时用[ApplicationContext.setFontSizeScale](js-apis-inner-application-applicationcontext.md#applicationcontextsetfontsizescale13)设置应用字体大小缩放比例。为了确保时序正确性，建议开发者自行监听字体缩放变化，以保证测算结果的准确性。
* 在测算裁剪后的文本时，由于某些Unicode字符（如emoji）的码位长度大于1，直接按字符串长度裁剪会导致不准确的结果。建议基于Unicode码点进行迭代处理，避免错误截断字符，确保测算结果准确，请参考[measureTextSize方法的示例2](arkts-apis-uicontext-measureutils.md#measuretextsize12)。

## measureText12+

PhonePC/2in1TabletTVWearable

measureText(options: MeasureOptions): number

计算指定文本作为单行文本显示时的宽度。如果文本包含多行（由换行符\n分隔），则返回其中最长的行的宽度。

说明

measureText接口的计算结果始终是单行文本的宽度，入参options中配置的布局约束（如constraintWidth、maxLines）对measureText的结果没有影响。如果需要计算布局约束下的宽度，请使用[measureTextSize](arkts-apis-uicontext-measureutils.md#measuretextsize12)方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [MeasureOptions](js-apis-measure.md#measureoptions) | 是 | 被计算文本描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文本宽度。  **说明:**  浮点数会向上取整。  单位：px |

**示例：**

通过MeasureUtils的measureText方法获取"Hello World"文字的宽度。

```
1. import { MeasureUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State uiContext: UIContext = this.getUIContext();
7. @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
8. @State textWidth: number = this.uiContextMeasure.measureText({
9. textContent: "Hello World",
10. fontSize: '50px'
11. });

13. build() {
14. Row() {
15. Column() {
16. Text(`The width of 'Hello World': ${this.textWidth}`)
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

## measureTextSize12+

PhonePC/2in1TabletTVWearable

measureTextSize(options: MeasureOptions): SizeOptions

计算指定文本单行布局下的宽度和高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [MeasureOptions](js-apis-measure.md#measureoptions) | 是 | 被计算文本描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SizeOptions](ts-types.md#sizeoptions) | 返回文本所占布局宽度和高度。  **说明:**  没有传参constraintWidth的情况下，文本宽度返回值浮点数会向上取整。  文本宽度以及高度返回值单位均为px。 |

**示例1：**

通过MeasureUtils的measureTextSize方法获取"Hello World"文字的宽度和高度。

```
1. import { MeasureUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State uiContext: UIContext = this.getUIContext();
7. @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
8. textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
9. textContent: "Hello World",
10. fontSize: '50px'
11. });
12. build() {
13. Row() {
14. Column() {
15. Text(`The width of 'Hello World': ${this.textSize.width}`)
16. Text(`The height of 'Hello World': ${this.textSize.height}`)
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

**示例2：**

通过MeasureUtils的measureTextSize方法和unicode码点计算，手动实现文本截断。与设置[maxLines](ts-basic-components-text.md#maxlines)、[textOverflow](ts-basic-components-text.md#textoverflow)实现同样的效果。

```
1. @Entry
2. @Component
3. struct TextDemo {
4. @State isExpanded: boolean = false;
5. @State displayedText: string = '';
6. @State defaultFontSize: number = 16;
7. @State textWidth: number = 150;
8. @State numLength: number = 0;
9. @State numUnicode: number = 0;
10. private fullText: string =
11. '这是一个超长文本示例，当文本内容超过三行时，超出部分会显示省略号。点击省略号可展开全部内容。此处为测试文本，用于验证多行文本截断效果。';
12. private maxLines: number = 3;

14. aboutToAppear() {
15. const codePoints = this.getCodePoints(this.fullText);
16. this.numLength = this.fullText.length;
17. this.numUnicode = codePoints.length;
18. this.calculateText(this.maxLines, this.fullText);
19. }

21. getCodePoints(text: string): number[] { // 使用codePointAt分割文本
22. const codePoints: number[] = [];
23. let index = 0;
24. while (index < text.length) {
25. const codePoint = text.codePointAt(index);
26. if (codePoint === undefined) {
27. break;
28. }
29. codePoints.push(codePoint);
30. index += codePoint > 0xFFFF ? 2 : 1; // 处理四字节字符
31. }
32. return codePoints;
33. }

35. lastUnicodeLength(str: string) { // 获得字符串最后一个字符的unicode长度
36. if (!str || str.length < 1) {
37. return 0;
38. }
39. if (str.length < 2) {
40. return 1;
41. }
42. let lastCodePoint = str.codePointAt(str.length - 2);
43. if (lastCodePoint == undefined) {
44. return 1;
45. }
46. let lastStr = String.fromCodePoint(lastCodePoint);
47. return lastStr.length;
48. }

50. calculateText(maxLines: number, fullText: string) { // 计算文本是否需要截断
51. const noMaxLinesSize = this.getUIContext().getMeasureUtils().measureTextSize({
52. textContent: fullText,
53. constraintWidth: this.textWidth
54. });
55. const hasMaxLinesSize = this.getUIContext().getMeasureUtils().measureTextSize({
56. textContent: fullText,
57. constraintWidth: this.textWidth,
58. maxLines: this.maxLines
59. });

61. this.displayedText = this.displayedText = this.fullText;
62. if (Number(noMaxLinesSize.height) > Number(hasMaxLinesSize.height)) { // 存在截断
63. while (this.displayedText.length > 0) {
64. this.displayedText =
65. this.displayedText.slice(0,
66. this.displayedText.length - this.lastUnicodeLength(this.displayedText)); // 删掉几个字
67. let textAfterCut = this.displayedText + "…"; // 加上省略号
68. let sizeAfterCut = this.getUIContext().getMeasureUtils().measureTextSize({
69. textContent: textAfterCut,
70. constraintWidth: this.textWidth
71. });
72. if (Number(sizeAfterCut.height) <= Number(hasMaxLinesSize.height)) {
73. break;
74. } else {
75. console.info("displayedText: " + this.displayedText);
76. }
77. }
78. this.displayedText = this.displayedText + "…";
79. }
80. }

82. build() {
83. Column({ space: 10 }) {
84. Text(`用length计算的文本长度 ${this.numLength}`)
85. Text(`用codePointAt计算的文本长度 ${this.numUnicode}`)
86. Text('下面是需要截断的文本')
87. Text(this.fullText)
88. .borderWidth(1)

90. Text('下面是设置了maxLines和texOverflow')
91. Text(this.fullText)
92. .maxLines(this.maxLines)
93. .textOverflow({ overflow: TextOverflow.Ellipsis })
94. .width(this.textWidth)
95. .borderWidth(1)

97. Text('下面是计算后分割的文本')
98. Text(this.displayedText)
99. .width(this.textWidth)
100. .borderWidth(1)
101. }
102. .padding(20)
103. }
104. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/XmDYWVaZTdScIBfwOmKzlA/zh-cn_image_0000002583479411.png?HW-CC-KV=V1&HW-CC-Date=20260428T000023Z&HW-CC-Expire=86400&HW-CC-Sign=B76AAD479820CA71F90ED1E076A2C9D0CBBAC2B47637EDD3E118F9C5FFE2EB78)

## getParagraphs20+

PhonePC/2in1TabletTVWearable

getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>

将属性字符串根据文本布局选项转换成对应的[Paragraph](js-apis-graphics-text.md#paragraph)数组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styledString | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | 待转换的属性字符串。 |
| options | [TextLayoutOptions](ts-text-common.md#textlayoutoptions对象说明20) | 否 | 文本布局选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Paragraph](js-apis-graphics-text.md#paragraph)> | [Paragraph](js-apis-graphics-text.md#paragraph)的数组。 |

**示例：**

通过MeasureUtils的getParagraphs方法测算文本，当内容超出最大显示行数的时候，截断文本显示并展示“...全文”的效果。

```
1. import { LengthMetrics } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class MyCustomSpan extends CustomSpan {
5. constructor(word: string, width: number, height: number, context: UIContext) {
6. super();
7. this.word = word;
8. this.width = width;
9. this.height = height;
10. this.context = context;
11. }

13. onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics {
14. return { width: this.width, height: this.height };
15. }

17. onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
18. let canvas = context.canvas;
19. const brush = new drawing.Brush();
20. brush.setColor({
21. alpha: 255,
22. red: 0,
23. green: 74,
24. blue: 175
25. });
26. const font = new drawing.Font();
27. font.setSize(25);
28. const textBlob = drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
29. canvas.attachBrush(brush);
30. canvas.drawRect({
31. left: options.x + 10,
32. right: options.x + this.context.vp2px(this.width) - 10,
33. top: options.lineTop + 10,
34. bottom: options.lineBottom - 10
35. });
36. brush.setColor({
37. alpha: 255,
38. red: 23,
39. green: 169,
40. blue: 141
41. });
42. canvas.attachBrush(brush);
43. canvas.drawTextBlob(textBlob, options.x + 20, options.lineBottom - 15);
44. canvas.detachBrush();
45. }

47. setWord(word: string) {
48. this.word = word;
49. }

51. width: number = 160;
52. word: string = "drawing";
53. height: number = 10;
54. context: UIContext;
55. }

57. @Entry
58. @Component
59. struct Index {
60. str: string =
61. "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.";
62. mutableStr2 = new MutableStyledString(this.str, [
63. {
64. start: 0,
65. length: 3,
66. styledKey: StyledStringKey.FONT,
67. styledValue: new TextStyle({ fontSize: LengthMetrics.px(20) })
68. },
69. {
70. start: 3,
71. length: 3,
72. styledKey: StyledStringKey.FONT,
73. styledValue: new TextStyle({ fontColor: Color.Brown })
74. }
75. ]);

77. // 测算属性字符串在指定宽度下能显示的行数
78. getLineNum(styledString: StyledString, width: LengthMetrics) {
79. let paragraphArr = this.getUIContext().getMeasureUtils().getParagraphs(styledString, { constraintWidth: width });
80. let res = 0;
81. for (let i = 0; i < paragraphArr.length; ++i) {
82. res += paragraphArr[i].getLineCount();
83. }
84. return res;
85. }

87. // 测算属性字符串显示maxLines行时最多可以显示的字数
88. getCorrectIndex(styledString: MutableStyledString, maxLines: number, width: LengthMetrics) {
89. let low = 0;
90. let high = styledString.length - 1;
91. // 使用二分查找
92. while (low <= high) {
93. let mid = (low + high) >> 1;
94. console.info("demo: get " + low + " " + high + " " + mid);
95. let moreStyledString = new MutableStyledString("... 全文", [{
96. start: 4,
97. length: 2,
98. styledKey: StyledStringKey.FONT,
99. styledValue: new TextStyle({ fontColor: Color.Blue })
100. }]);
101. moreStyledString.insertStyledString(0, styledString.subStyledString(0, mid));
102. let lineNum = this.getLineNum(moreStyledString, LengthMetrics.px(500));
103. if (lineNum <= maxLines) {
104. low = mid + 1;
105. } else {
106. high = mid - 1;
107. }
108. }
109. return high;
110. }

112. mutableStrAllContent = new MutableStyledString(this.str, [
113. {
114. start: 0,
115. length: 3,
116. styledKey: StyledStringKey.FONT,
117. styledValue: new TextStyle({ fontSize: LengthMetrics.px(40) })
118. },
119. {
120. start: 3,
121. length: 3,
122. styledKey: StyledStringKey.FONT,
123. styledValue: new TextStyle({ fontColor: Color.Brown })
124. }
125. ]);
126. customSpan1: MyCustomSpan = new MyCustomSpan("Hello", 120, 10, this.getUIContext());
127. mutableStrAllContent2 = new MutableStyledString(this.str, [
128. {
129. start: 0,
130. length: 3,
131. styledKey: StyledStringKey.FONT,
132. styledValue: new TextStyle({ fontSize: LengthMetrics.px(100) })
133. },
134. {
135. start: 3,
136. length: 3,
137. styledKey: StyledStringKey.FONT,
138. styledValue: new TextStyle({ fontColor: Color.Brown })
139. }
140. ]);
141. controller: TextController = new TextController();
142. controller2: TextController = new TextController();
143. textController: TextController = new TextController();
144. textController2: TextController = new TextController();

146. aboutToAppear() {
147. this.mutableStrAllContent2.insertStyledString(0, new StyledString(this.customSpan1));
148. this.mutableStr2.insertStyledString(0, new StyledString(this.customSpan1));
149. }

151. build() {
152. Scroll() {
153. Column() {
154. Text('原文')
155. Text(undefined, { controller: this.controller }).width('500px').onAppear(() => {
156. this.controller.setStyledString(this.mutableStrAllContent);
157. })
158. Divider().strokeWidth(8).color('#F1F3F5')
159. Text('排版后')
160. Text(undefined, { controller: this.textController }).onAppear(() => {
161. let now = this.getCorrectIndex(this.mutableStrAllContent, 3, LengthMetrics.px(500));
162. if (now != this.mutableStrAllContent.length - 1) {
163. let moreStyledString = new MutableStyledString("... 全文", [{
164. start: 4,
165. length: 2,
166. styledKey: StyledStringKey.FONT,
167. styledValue: new TextStyle({ fontColor: Color.Blue })
168. }]);
169. moreStyledString.insertStyledString(0, this.mutableStrAllContent.subStyledString(0, now));
170. this.textController.setStyledString(moreStyledString);
171. } else {
172. this.textController.setStyledString(this.mutableStrAllContent);
173. }
174. })
175. .width('500px')
176. Divider().strokeWidth(8).color('#F1F3F5')
177. Text('原文')
178. Text(undefined, { controller: this.controller2 }).width('500px').onAppear(() => {
179. this.controller2.setStyledString(this.mutableStrAllContent2);
180. })
181. Divider().strokeWidth(8).color('#F1F3F5')
182. Text('排版后')
183. Text(undefined, { controller: this.textController2 }).onAppear(() => {
184. let now = this.getCorrectIndex(this.mutableStrAllContent2, 3, LengthMetrics.px(500));
185. let moreStyledString = new MutableStyledString("... 全文", [{
186. start: 4,
187. length: 2,
188. styledKey: StyledStringKey.FONT,
189. styledValue: new TextStyle({ fontColor: Color.Blue })
190. }]);
191. moreStyledString.insertStyledString(0, this.mutableStrAllContent2.subStyledString(0, now));
192. this.textController2.setStyledString(moreStyledString);
193. })
194. .width('500px')
195. }.width('100%')
196. }
197. }
198. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/RHWLE2fpT1uuj7SSwc93uQ/zh-cn_image_0000002552799762.png?HW-CC-KV=V1&HW-CC-Date=20260428T000023Z&HW-CC-Expire=86400&HW-CC-Sign=972899F1AC110E6FE21700B303820C86B539F215971D01DD2E40E3ECBA664F98)
