---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq
title: 使用文本常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 使用文本常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:207119cd24d7e1e042ebb7c8b79d75563532d982f0275a11bf24acca76d9451b
---

本文档介绍使用文本的常见问题并提供参考。

## 文本显示（Text/Span）常见问题

以下内容介绍了使用[Text](../harmonyos-references/ts-basic-components-text.md)和[Span](../harmonyos-references/ts-basic-components-span.md)组件进行文本显示时可能遇到的常见问题，包括文本截断、添加标签、显示表情等场景的处理方法。

### Text组件尾部省略号后为什么还有一段空白，没有占满组件宽度

**问题现象**

在Text组件上未设置宽度，当内容过长时，省略号与组件边缘之间会留有较大空白，且内容更新时省略号的位置会发生变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/iDg-DMmuTcS54NB9Zjs4GQ/zh-cn_image_0000002583478167.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=3700C1024DB7CEB2DEFE8B42FE99C4DABE34551CAE039FA98EFB48812C81FA59)

**原因分析**

当Text组件未设置宽度且内容超长时，组件宽度将采用父组件传递的布局约束的最大宽度。不同内容、不同的断词模式导致排版塑型结果不同，因此省略开始位置也会不同。

**解决措施**

设置[wordBreak](../harmonyos-references/ts-basic-components-text.md#wordbreak11)属性为WordBreak.BREAK\_ALL，任意2个字符间断行使文本内容尽量占满组件区域。

示例代码如下：

```
1. import { common } from '@kit.AbilityKit';
2. @Entry
3. @Component
4. export struct WordBreakd {
5. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. private manager = this.context.resourceManager;

8. // 'Text_WordBreak'资源文件中的value值为'混合Hello World! honorificabilitudinitatibus'
9. @State message: string = this.manager.getStringByNameSync('Text_WordBreak');
10. build() {
11. NavDestination() {
12. Column() {
13. Text(this.message)
14. .id('HelloWorld')
15. .fontSize('25fp')
16. .maxLines(1)
17. .textOverflow({ overflow: TextOverflow.Ellipsis})
18. .onClick(() => {
19. this.message = 'Welcome try try try 1235628327434348';
20. })
21. .border({ width: 1})
22. .wordBreak(WordBreak.BREAK_ALL) // 修改断词模式
23. }
24. .width(300)
25. .border({ width: 1, color: Color.Blue})
26. .margin({left: 30, top: 50})
27. }
28. // ...
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/RntXpPe9T8eKU5ax6BdMog/zh-cn_image_0000002552798518.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=D84CF891C67CB08E22E9729A55B46E9D1E66252242812C35F710BBE9A8996CC1)

### Text组件如何实现行末展开样式

**解决措施**

自行测算截断字符，并在行末添加...展开或者...图标作为组件内容。实现方式请参考[属性字符串转Paragraph数组](../harmonyos-references/arkts-apis-uicontext-measureutils.md#getparagraphs20)、[文本展开折叠](../best-practices/bpta-text-expand-collapse.md)。

### Text组件如何实现内容超长时自动显示省略样式吗？

**问题现象**

在固定尺寸的组件区域内，不同字号的内容显示的最大行数会有所不同。期望实现内容超长时自动显示省略样式，则无需设置固定的maxLines值。

**解决措施**

设置[heightAdaptivePolicy](../harmonyos-references/ts-basic-components-text.md#heightadaptivepolicy10)为TextHeightAdaptivePolicy.LAYOUT\_CONSTRAINT\_FIRST，该模式会删除超过布局约束的行，从而实现类似设置maxLines的效果。

示例代码如下：

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. export struct HeightAdaptivePolicy {
6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. private manager = this.context.resourceManager;

9. // 'Text_Adaptive_Layout'资源文件中的value值为'混合Hello World! 多行文本 中英文数字混合 1282378283 ~'
10. @State message: string = this.manager.getStringByNameSync('Text_Adaptive_Layout');
11. @State fontSize: number = 25;
12. build() {
13. NavDestination() {
14. Column({ space: 10 }) {
15. Text(this.message)
16. .id('HelloWorld')
17. .fontSize(this.fontSize)
18. .textOverflow({ overflow: TextOverflow.Ellipsis })
19. .border({ width: 1 })
20. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST) // 调整自适应布局策略
21. .width(300)
22. .height(200)
23. Row() {
24. Button('fontSize+5')
25. .onClick(() => {
26. this.fontSize += 5;
27. })
28. Button('fontSize-5')
29. .onClick(() => {
30. this.fontSize -= 5;
31. })
32. }
33. }
34. .margin({ left: 30, top: 50 })
35. }
36. // ...
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/enpNIV3VRQmvDfN1JzeZ2Q/zh-cn_image_0000002583438213.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=887001D3B4127FE304C4E3946622C3A539273CCA59F11AF1DC44F39ECFB4C469)

### 在文本前后添加自定义标签

**问题现象**

如何在文本的前后各添加一个标签，例如“专题”或“Top1”，且这些标签的[背景设置](../harmonyos-references/ts-universal-attributes-background.md)、[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)需要能够自定义。

**解决措施一**

如果标签和中间的长文本需在同一行显示，开发者可能会考虑使用[Span](../harmonyos-references/ts-basic-components-span.md)实现，但是Span不支持设置尺寸。此时，可以在[弹性布局 (Flex)](arkts-layout-development-flex-layout.md)或者[Row](../harmonyos-references/ts-container-row.md)中放置标签和长文本，并为长文本设置[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)属性，以确保文本超长时能够自适应截断，显示在一行之内。

实现步骤：

1.将标签和长文本放在同一个沿水平方向布局的容器Row中。

2.中间长文本设置textOverflow属性为TextOverflow.Ellipsis，空间不足时截断文本，显示省略号。

实现案例请参考[实现热搜榜](arkts-common-components-text-display.md#实现热搜榜)，该示例中，文字“1”、“爆”就是“我是热搜词条”的两个标签。这种实现方式写法简便，适合单行文本添加标签的场景。

**解决措施二**

如果需在多行文本前后添加标签并且不截断文本，上述方案会导致三个Text中的文本不能对齐，因为多行文本会在Row的宽度内折行。此时，可以在[层叠布局 (Stack)](arkts-layout-development-stack-layout.md)中放置标签和长文本，给中间多行文本设置首行文本缩进距离[textIndent](../harmonyos-references/ts-basic-components-text.md#textindent10)。多行文本后面的标签则需要通过[offset](../harmonyos-references/ts-universal-attributes-location.md#offset)属性调整位置。这种实现方式，可以让三个Text组件中的文字水平对齐。实现步骤如下：

实现步骤：

1.将标签和长文本放在Stack中。

2.在组件显示之前的回调[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)中，使用[measureTextSize](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)计算前标签的宽度，作为中间多行文本的首行缩进距离。

3.在组件显示之前的回调aboutToAppear中，通过[getParagraphs](../harmonyos-references/arkts-apis-uicontext-measureutils.md#getparagraphs20)计算中间多行文本最后一行的宽度、除最后一行文本之外的高度，作为后标签的偏移量offset。

4.设置后标签相对于Stack左上角的偏移量。

示例：

```
1. import { LengthMetrics } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. export struct LengthMetric {
7. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. private manager = this.context.resourceManager;

10. // 'Text_Add_Tags_Front_and_Post'资源文件中的value值为'这是一段长文本，超长部分折行，前后添加标签'
11. @State message: string = this.manager.getStringByNameSync('Text_Add_Tags_Front_and_Post');
12. // 'Text_Add_Tags_Front'前标签'
13. @State frontTag: string = this.manager.getStringByNameSync('Text_Add_Tags_Front');
14. // 'Text_Add_Tags_Post'资源文件中的value值为'后标签'
15. @State backTag: string = this.manager.getStringByNameSync('Text_Add_Tags_Post');
16. @State frontPaddingVp: number = 20;
17. @State backPaddingVp: number = 10;
18. @State fontTagWidthVp: Length = 0;
19. @State backTagWidthVp: Length = 0;
20. @State backOffsetVpX: Length = 0;
21. @State backOffsetVpY: Length = 0;
22. @State messageLines: number = 0;
23. @State stackWidthVp: number = 300;

25. // 显示之前，测算前后标签的位置，中间文本的缩进距离
26. aboutToAppear(): void {
27. // 计算前标签的宽度fontTagWidthVp，作为message的首行缩进距离
28. let frontTagSize: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
29. textContent: this.frontTag,
30. });
31. this.fontTagWidthVp = this.getUIContext().px2vp(Number(frontTagSize.width)) + this.frontPaddingVp * 2

33. // 计算frontTag+message占据的行数
34. let linesFrontTagPlusMessage = 0;
35. let mutableStr = new MutableStyledString(this.message,
36. [{
37. start: 0,
38. length: 1,
39. styledKey: StyledStringKey.PARAGRAPH_STYLE,
40. styledValue: new ParagraphStyle({ textIndent: LengthMetrics.vp(this.fontTagWidthVp) })
41. }]
42. )
43. let paragraphArr = this.getUIContext()
44. .getMeasureUtils()
45. .getParagraphs(mutableStr, { constraintWidth: LengthMetrics.vp(this.stackWidthVp) });
46. for (let i = 0; i < paragraphArr.length; ++i) {
47. linesFrontTagPlusMessage += paragraphArr[i].getLineCount();
48. }

50. // 后标签offsetX的偏移量backOffsetVpX=frontTag+message最后一行的宽度
51. this.backOffsetVpX =
52. this.getUIContext().px2vp((paragraphArr[paragraphArr.length-1].getLineWidth(linesFrontTagPlusMessage - 1)))
53. // 后标签offsetY的偏移量backOffsetVpY=frontTag+message总高度-最后一行的高度
54. let heightFrontTagPlusMessageVp = 0;
55. for (let i = 0; i < paragraphArr.length; ++i) {
56. heightFrontTagPlusMessageVp += this.getUIContext().px2vp(paragraphArr[i].getHeight());
57. }
58. let lastLineHeight =
59. this.getUIContext().px2vp(paragraphArr[paragraphArr.length-1].getLineHeight(linesFrontTagPlusMessage - 1))
60. this.backOffsetVpY = heightFrontTagPlusMessageVp - lastLineHeight
61. }

63. build() {
64. NavDestination() {
65. Column({ space: 20 }) {
66. Blank()
67. .height(200)
68. Stack() {
69. Text(this.frontTag)
70. .padding({ left: this.frontPaddingVp, right: this.frontPaddingVp })
71. .backgroundColor('rgb(39, 135, 217)')
72. Text(this.message)
73. .textIndent(this.fontTagWidthVp)
74. .padding(0)
75. Text(this.backTag)
76. .padding({ left: this.backPaddingVp, right: this.backPaddingVp })
77. .backgroundColor('rgb(0, 74, 175)')
78. .offset({
79. x: this.backOffsetVpX,
80. y: this.backOffsetVpY
81. })
82. }
83. .alignContent(Alignment.TopStart) // 顶部起始端对齐
84. .width(this.stackWidthVp)
85. }
86. .height('100%')
87. .width('90%')
88. .padding('5%')
89. }
90. // ...
91. }
92. }
```

[LengthMetric.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/LengthMetric.ets#L15-L112)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/sLxlHqKGTq6JlyyUqhvS9g/zh-cn_image_0000002552958168.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=B56CF07166E5C3F0100050E667AE1ED8AED84AB520870E9268636C06161E25F2)

### Text组件如何实现表情与文字一起显示

**问题现象**

emoji表情有时以表情符号的形式表示，如何将表情符号转换为emoji表情，并在Text组件中与文字一同显示？

**解决措施**

使用正则表达式解析表情符号，再将表情符号与图片资源建立映射，通过[Span](../harmonyos-references/ts-basic-components-span.md)和[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)同时展示表情和文字。

```
1. // 请将$r('app.media.xxx')替换为实际资源文件
2. import { common } from '@kit.AbilityKit';
3. @Entry
4. @Component
5. export struct DisplayedTogether {
6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. private manager = this.context.resourceManager;

9. // 'Text_Full_Text'资源文件中的value值为
10. // '你好我是Text[grin]，你好我[rolling_on_the_floor_laughing]是Text，[slightly_smiling_face]你好我是Text[grin]'
11. @State fulltext: string = this.manager.getStringByNameSync('Text_Full_Text');

13. static classifyTextAndEmojis(input: string): Map<string, string[]> {
14. const emojiRegex = /\[([a-zA-Z_]+)\]/g; // 根据实际情况编写正则表达式
15. const resultMap = new Map<string, string[]>(); // 用map记录普通文本和表情
16. resultMap.set('text', []);
17. resultMap.set('emojis', []);

19. let lastIndex = 0;
20. let match: RegExpExecArray | null = null;

22. while ((match = emojiRegex.exec(input)) !== null) {
23. // 添加普通文本
24. if (match.index >= lastIndex) {
25. resultMap.get('text')?.push(input.substring(lastIndex, match.index));
26. }
27. // 添加匹配到的表情
28. resultMap.get('emojis')?.push(match[1]);
29. lastIndex = match.index + match[0].length;
30. }
31. // 添加最后一段文本
32. if (lastIndex < input.length) {
33. resultMap.get('text')?.push(input.substring(lastIndex));
34. }
35. return resultMap;
36. }

38. static getEmojiImg(emojis: string[]): Resource[] { // 根据正则匹配结果返回自定义表情资源
39. let emojisImg: Resource[] = []
40. for (let i = 0; i < emojis.length; i++) {
41. switch (emojis[i]) {
42. case 'rolling_on_the_floor_laughing':
43. emojisImg.push($r('app.media.rolling_on_the_floor_laughing'))
44. break;
45. case 'slightly_smiling_face':
46. emojisImg.push($r('app.media.slightly_smiling_face'))
47. break;
48. case 'grin':
49. emojisImg.push($r('app.media.grin'))
50. break;
51. default:
52. break;
53. }
54. }
55. return emojisImg
56. }

58. build() {
59. NavDestination() {
60. Column() {
61. TextInput({
62. // 请将$r('app.string.Text_emoji')替换为实际资源文件，在本示例中该资源文件的value值为"用户输入带表情的文本，例如：你好[grin]"
63. placeholder: $r('app.string.Text_emoji')
64. })
65. .width('80%')
66. .padding(10)
67. .border({ width: 1, color: '#EEEEEE' })
68. .onChange((value: string) => {
69. // 输入变化时，更新 fulltext
70. this.fulltext = value;
71. });

73. Text() {
74. ForEach(DisplayedTogether.classifyTextAndEmojis(this.fulltext).get('text'),
75. (item: string, index: number) => { // 展示文本和自定义表情资源
76. Span(item)
77. .fontSize(18)
78. .fontColor('#666666')
79. .fontWeight(FontWeight.Regular)

81. ImageSpan(DisplayedTogether.getEmojiImg(
82. DisplayedTogether.classifyTextAndEmojis(this.fulltext).get('emojis'))[index])
83. .verticalAlign(ImageSpanAlignment.BOTTOM)
84. .height(24)
85. })
86. }
87. .width('80%')
88. .padding(15)
89. }
90. .width('100%')
91. .height('100%')
92. .justifyContent(FlexAlign.Center)
93. .alignItems(HorizontalAlign.Center)
94. .padding(20)
95. }
96. // ...
97. }
98. }
```

[DisplayedTogether.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/DisplayedTogether.ets#L15-L120)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/qTHJnVDnQGqPuhi0oesP1A/zh-cn_image_0000002583478169.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=449B5C122EC5C1F6B1E476D17DEEABB4B5FAE889581915C50F2858DEBEC2DE9C)

### 文本超长时如何展示

**问题现象**

Text组件中内容过多，超出父组件容器[Column](../harmonyos-references/ts-container-column.md)的高度，会导致文本溢出容器边界，如何让文本显示在父组件容器的区域内？

**解决措施一**

Text文本是自动折行的，当没有限制Text高度[height](../harmonyos-references/ts-universal-attributes-size.md#height)时，Text高度在文本的行数增加时自动调整。可以通过设置[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)属性限制文本的最大行数，如果有多余的文本默认会被截断。也可以通过[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)属性来指定截断方式。

以下示例展示了限制Text组件不超过三行的场景。

```
1. @Entry
2. @Component
3. export struct TextLong {
4. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. private manager = this.context.resourceManager;

7. // 'Text_Long_String'资源文件中的value值为'这是一段超长文本'
8. @State message: string = this.manager.getStringByNameSync('Text_Long_String').repeat(50);

10. build() {
11. NavDestination() {
12. Column() {
13. Text(this.message)
14. .height('auto')
15. .maxLines(3)
16. }
17. .height(200)
18. .width('80%')
19. .margin('10%')
20. .borderWidth(1)
21. .justifyContent(FlexAlign.Center)
22. }
23. // ...
24. }
25. }
```

[TextLong.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextLong.ets#L17-L46)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/lVz_oUvZRX2IuxdcosMleA/zh-cn_image_0000002552798520.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=C3DB8D9E60C9B3AD65A09786C480818D134FDC4C5BAD09AE7F1D1B9CF69C29ED)

**解决措施二**

上述方法会导致部分文本被裁剪掉，如果需要保留全部文本，可以把Text组件放在滚动容器[Scroll](../harmonyos-references/ts-container-scroll.md)内，再通过手势滑动来浏览全部文本，具体示例如下：

```
1. @Entry
2. @Component
3. export struct TextLongTow {
4. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. private manager = this.context.resourceManager;

7. // 'Text_Long_String'资源文件中的value值为'这是一段超长文本'
8. @State message: string = this.manager.getStringByNameSync('Text_Long_String').repeat(50);

10. build() {
11. NavDestination() {
12. Column() {
13. Scroll() {
14. Text(this.message)
15. }
16. .scrollBar(BarState.Off)
17. }
18. .height(200)
19. .width('80%')
20. .margin('10%')
21. .borderWidth(1)
22. .justifyContent(FlexAlign.Center)
23. }
24. // ...
25. }
26. }
```

[TextLongTow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextLongTow.ets#L17-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/fPHvixPkRVeeE6P1rO1Lmw/zh-cn_image_0000002583438215.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=DCE4EEEBA419177F53E400DC5F7CE279D6C59AB443CE5101AE3C3B592AD33A87)

### selection如何触发弹出自定义菜单并设置菜单字体大小

**问题现象**

在[bindSelectionMenu](../harmonyos-references/ts-basic-components-text.md#bindselectionmenu11)自定义选择菜单中，可通过TextResponseType设置文本选择菜单的响应类型。通过[selection](../harmonyos-references/ts-basic-components-text.md#selection11)如何触发弹出自定义菜单并设置菜单字体大小。

**解决措施**

若希望由selection触发自定义菜单，可将TextResponseType设置为DEFAULT。同时，在[Menu](../harmonyos-references/ts-basic-components-menu.md)组件上通过配置font属性，即可自定义菜单的字体大小，灵活适配界面设计需求。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextExample8 {
5. controller: TextController = new TextController();
6. options: TextOptions = { controller: this.controller };
7. @State selectStart: number = 0;
8. @State selectEnd: number = 0;

10. build() {
11. Column() {
12. Column() {
13. Text("TextTextTextText")
14. .fontSize(14)
15. .selection(this.selectStart, this.selectEnd)
16. .copyOption(CopyOptions.InApp)
17. .bindSelectionMenu(TextSpanType.TEXT, this.CustomMenu, TextResponseType.DEFAULT, {
18. onDisappear: () => {
19. this.selectStart = -1;
20. this.selectEnd = -1;
21. },
22. })
23. .textAlign(TextAlign.Center)
24. .borderWidth(1)
25. .borderColor(Color.Red)
26. Button("Set selection")
27. .onClick(() => {
28. this.selectStart = 0;
29. this.selectEnd = 10;
30. })
31. .fontSize(14)
32. .margin({ top: 20 })
33. }
34. .width('100%')
35. .padding({ top: 300 })
36. }
37. .height('100%')
38. }

40. @Builder
41. CustomMenu() {
42. Column() {
43. Menu() {
44. MenuItem({ content: "Item Content" })
45. MenuItem({ content: "Item Content" })
46. MenuItem({ content: "Item Content" })
47. }
48. .font({ size: 14 })
49. .radius($r('sys.float.ohos_id_corner_radius_card'))
50. .clip(true)
51. .backgroundColor('#F0F0F0')
52. }
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/reVh9Uc-S-WuNFRXYxBWfQ/zh-cn_image_0000002552958170.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=17F3ED2D6542672B1E4A48641AD8C9350A4BB82BF7BAE3282B380D629AAC9E88)

### 如何屏蔽文本的长按手势

**问题现象**

配置[CopyOptions](../harmonyos-references/ts-appendix-enums.md#copyoptions9)将文本设置为可选择，此时长按文本会选择文字内容并弹出系统菜单，如何使长按手势不生效。

**解决措施**

想要使长按手势对文本不生效，可以设置触发时间小于系统菜单触发时间（500ms）的自定义长按手势。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextExample8 {
5. build() {
6. Column() {
7. Text("TextTextTextText")
8. .copyOption(CopyOptions.InApp)
9. .gesture(LongPressGesture({ repeat: false, duration: 400 })
10. .onAction(() => {
11. }))
12. .margin({
13. top: 100,
14. bottom: 100,
15. left: 100,
16. right: 100
17. })
18. }
19. .height('100%')
20. }
21. }
```

### 设置enableVariableFontWeight为true后字重不能跟随设置调节

**问题现象**

Text组件调用[fontWeight](../harmonyos-references/ts-basic-components-text.md#fontweight12)接口，[FontSettingOptions](../harmonyos-references/ts-text-common.md#fontsettingoptions12对象说明)类型的入参options设置enableVariableFontWeight值为true之后，在系统设置的“字体大小和界面缩放”页面中调节字体粗细，Text组件的字重不跟随变化。

**解决措施**

1. 如果需要Text组件字重跟随系统设置变化，需要在[configuration标签](app-configuration-file.md#configuration标签)设置followSystem。
2. 字体配置项options控制是否启用可变字重调节。

* 当options的参数enableVariableFontWeight取值true时，启用可变字重调节。weight取值为[100, 900]范围内任意整数时，字重取值为weight。此时如果在设置中调节字体粗细，字重始终是开发者设置的数值weight，字体粗细不会变化。
* 当options的参数enableVariableFontWeight取值false时，禁用可变字重调节。weight取值为[100, 900]范围内的整百数值时，字重取值为weight。weight是非整百数值时，字重取默认值400。此时更改设置中的字体粗细，字重会随设置变化。此时如果在设置中调节字体粗细，字重会随设置变化。

## 文本输入（TextInput/TextArea/Search）常见问题

以下内容介绍了使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)和[Search](../harmonyos-references/ts-basic-components-search.md)组件输入文本时可能遇到的问题。

### TextInput被遮挡时光标仍然不消失

**问题现象**

在Stack中堆叠了多个组件，包含一个输入框（TextInput），当TextInput组件被遮挡时，偶尔会出现带有小圆圈的手柄，显示在其他组件上。

**解决措施**

当TextInput组件处于选中状态并显示操作手柄时，选中区域和操作手柄可能不在同一图层渲染。其中，选中区域与输入框在同一图层，而操作手柄则在更高的图层上。因此，当输入框被其他元素遮挡时，选中区域也会被遮挡，但操作手柄仍然可见。

TextInput被遮挡时，如果通过[TextInputController](../harmonyos-references/ts-basic-components-textinput.md#textinputcontroller8)设置焦点和选中区域会出现上述现象。涉及的选中区域设置接口包括[selectAll](../harmonyos-references/ts-basic-components-textinput.md#selectall11)和[setTextSelection](../harmonyos-references/ts-basic-components-textinput.md#settextselection10)。建议检查应用代码中以下接口的调用时机，在输入框被遮挡后避免设置选中区域。

| 组件 | 接口 |
| --- | --- |
| Search | [setTextSelection](../harmonyos-references/ts-basic-components-search.md#settextselection12) |
| TextArea | [setTextSelection](../harmonyos-references/ts-basic-components-textarea.md#settextselection10) |
| TextInput | [selectAll](../harmonyos-references/ts-basic-components-textinput.md#selectall11) |
| TextInput | [setTextSelection](../harmonyos-references/ts-basic-components-textinput.md#settextselection10) |

以下示例展示了一个典型的问题场景，存在一个内容为“TextInput被遮挡不显示”的TextInput组件被隐藏，但点击按钮后，图片上会出现TextInput操作手柄。此时，开发者需要检查应用代码，确保在输入框被遮挡时没有设置选中区域。移除设置输入框选中区域的代码逻辑，即可解决操作手柄出现的问题。

```
1. @Entry
2. @Component
3. export struct CursorPersistsWhenTextInputIsCoveredExample {
4. controller: TextInputController = new TextInputController();
5. @State message1: string = 'TextInput被遮挡不显示';

7. build() {
8. NavDestination() {
9. Column({ space: 50 }) {
10. Stack() {
11. TextInput({ text: this.message1, controller: this.controller })
12. .copyOption(CopyOptions.LocalDevice)
13. .backgroundColor(Color.Green)
14. .width(200)
15. .id('textInput_1')

17. // $r('app.media.foreground')需要替换为开发者所需的图像资源文件。
18. Image($r('app.media.foreground'))
19. .width(200)
20. .height(200)
21. .backgroundColor('rgb(213,213,213)')
22. }

24. Button('点击出现手柄')
25. .onClick(() => {
26. this.getUIContext().getFocusController().requestFocus('textInput_1')
27. this.controller.setTextSelection(0, 5, { menuPolicy: MenuPolicy.HIDE })
28. })
29. }
30. .padding('10%')
31. .alignItems(HorizontalAlign.Center)
32. .height('100%')
33. .width('90%')
34. }
35. .backgroundColor('#f1f2f3')
36. .title($r('app.string.Cursor_Persists_When_TextInput_Is_Covered'))
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/IMl5cfgCRAyn6FU007xVEg/zh-cn_image_0000002583478171.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=A2B8684A3CA1928E992E4FD3414F2F2C3D68C99138E4A4757EB94926C258CA89)
