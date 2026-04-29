---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-styled-string
title: 属性字符串（StyledString/MutableStyledString）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 属性字符串（StyledString/MutableStyledString）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1478a9f52d666806e4b3e43d1b501e397af329c83bf2f93e62f8edbcebef88d6
---

属性字符串StyledString/MutableStyledString（其中MutableStyledString继承自StyledString，下文统称为StyledString），可用于在字符或段落级别上设置文本样式。将StyledString应用到文本组件上，可以采用多种方式修改文本，包括调整字号、添加字体颜色、使文本具备可点击性，以及通过自定义方式绘制文本等。具体使用方法请参考[属性字符串](../harmonyos-references/ts-universal-styled-string.md)的API文档。

属性字符串提供多种类型样式对象，涵盖各种常见的文本样式格式，例如文本装饰线样式、文本行高样式、文本阴影样式等。也可以自行创建[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)，以应用自定义样式。

## 创建并应用StyledString和MutableStyledString

可以通过[TextController](../harmonyos-references/ts-basic-components-text.md#textcontroller11)提供的[setStyledString](../harmonyos-references/ts-basic-components-text.md#setstyledstring12)方法，将属性字符串附加到文本组件，并推荐在[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)或者文本组件的[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)回调中触发绑定。

说明

在[aboutToAppear](../harmonyos-references/ts-custom-component-new-lifecycle.md#abouttoappear)中调用setStyledString方法时，由于该方法运行阶段组件尚未完成创建并成功挂载节点树，因此无法在页面初始化时显示属性字符串。

从API version 15开始，在aboutToAppear中调用setStyledString方法，页面初始化时可以显示属性字符串。

```
1. @Entry
2. @Component
3. struct styled_string_demo1 {
4. // 请将$r('app.string.CreateApply_Text_Forty_Five')替换为实际资源文件，在本示例中该资源文件的value值为"运动45分钟"
5. styledString1: StyledString = new StyledString( this.getUIContext()
6. .getHostContext()!.resourceManager.getStringSync($r('app.string.CreateApply_Text_Forty_Five').id));
7. // 请将$r('app.string.CreateApply_Text_Third_Five')替换为实际资源文件，在本示例中该资源文件的value值为"运动35分钟"
8. mutableStyledString1: MutableStyledString = new MutableStyledString( this.getUIContext()
9. .getHostContext()!.resourceManager.getStringSync($r('app.string.CreateApply_Text_Third_Five').id));
10. controller1: TextController = new TextController();
11. controller2: TextController = new TextController();

13. async onPageShow() {
14. // 在生命周期onPageShow回调中绑定属性字符串
15. this.controller1.setStyledString(this.styledString1);
16. }

18. build() {
19. Column() {
20. // 显示属性字符串
21. Text(undefined, { controller: this.controller1 })
22. Text(undefined, { controller: this.controller2 })
23. .onAppear(() => {
24. // 在组件onAppear回调中绑定属性字符串
25. this.controller2.setStyledString(this.mutableStyledString1);
26. })
27. }
28. .width('100%')
29. }
30. }
```

[CreateApply.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/CreateApply.ets#L17-L46)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/LKKkwUykTwaUBrBvmx0S4Q/zh-cn_image_0000002558604676.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=C9F4CE500311419407CC5B726247BBFAD8ACBF1493FDB3F238A59F2786E9BFC9)

## 设置文本样式

属性字符串目前提供了多种Style对象，包括[TextStyle](../harmonyos-references/ts-universal-styled-string.md#textstyle)、[TextShadowStyle](../harmonyos-references/ts-universal-styled-string.md#textshadowstyle)、[DecorationStyle](../harmonyos-references/ts-universal-styled-string.md#decorationstyle)、[BaselineOffsetStyle](../harmonyos-references/ts-universal-styled-string.md#baselineoffsetstyle)、[LineHeightStyle](../harmonyos-references/ts-universal-styled-string.md#lineheightstyle)、[LetterSpacingStyle](../harmonyos-references/ts-universal-styled-string.md#letterspacingstyle)，用于设置文本的各类样式。

* 创建及应用文本字体样式对象（TextStyle）

  ```
  1. import { LengthMetrics } from '@kit.ArkUI';

  3. @Entry
  4. @Component
  5. struct styled_string_demo2 {
  6. @State str: string =
  7. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply_Text_3') as string;
  8. textStyleAttrs: TextStyle =
  9. new TextStyle({
  10. fontWeight: FontWeight.Bolder,
  11. fontSize: LengthMetrics.vp(24),
  12. fontStyle: FontStyle.Italic,
  13. strokeWidth: LengthMetrics.px(5),
  14. strokeColor: Color.Green
  15. });
  16. mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [
  17. {
  18. start: 2,
  19. length: 2,
  20. styledKey: StyledStringKey.FONT,
  21. styledValue: this.textStyleAttrs
  22. },
  23. {
  24. start: 7,
  25. length: 4,
  26. styledKey: StyledStringKey.FONT,
  27. styledValue: new TextStyle({
  28. fontColor: Color.Orange, fontSize: LengthMetrics.vp(12),
  29. superscript: SuperscriptStyle.SUPERSCRIPT
  30. })
  31. }
  32. ]);
  33. controller: TextController = new TextController();

  35. async onPageShow() {
  36. this.controller.setStyledString(this.mutableStyledString);
  37. }

  39. build() {
  40. Column() {
  41. // 显示属性字符串
  42. Text(undefined, { controller: this.controller })
  43. .margin({ top: 10 })
  44. }
  45. .width('100%')
  46. }
  47. }
  ```

  [StyledStringTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringTextStyle.ets#L15-L63)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/Sl2kSkDpS9aDi0Te2kQxyQ/zh-cn_image_0000002589324201.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=151A297D34CF8AE520D5DFFE4109A25D83C84EBC53DA8CE4E123A13AA190301C)
* 创建及应用文本阴影对象（TextShadowStyle）

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct styled_string_demo3 {
  5. @State str: string =
  6. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply_Text_Third_Five') as string;
  7. mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [
  8. {
  9. start: 0,
  10. length: 3,
  11. styledKey: StyledStringKey.TEXT_SHADOW,
  12. styledValue: new TextShadowStyle({
  13. radius: 5,
  14. type: ShadowType.COLOR,
  15. color: Color.Red,
  16. offsetX: 10,
  17. offsetY: 10
  18. })
  19. }
  20. ]);
  21. controller: TextController = new TextController();

  23. async onPageShow() {
  24. this.controller.setStyledString(this.mutableStyledString);
  25. }

  27. build() {
  28. Column() {
  29. // 显示属性字符串
  30. Text(undefined, { controller: this.controller })
  31. }
  32. .width('100%')
  33. }
  34. }
  ```

  [StyledStringTextShadowStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringTextShadowStyle.ets#L15-L50)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/wYG9od4rT0yFqpXN8fN42w/zh-cn_image_0000002589244141.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=21CC418CD4BBA045F62245A63233BDC9033BF74DD25A4C3F752DECAFD0A9532A)
* 创建及应用文本装饰线对象（DecorationStyle）

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct styled_string_demo4 {
  5. @State str: string =
  6. this.getUIContext()
  7. .getHostContext()?.resourceManager.getStringByNameSync('CreateApply_Text_Third_Five') as string;
  8. mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [
  9. {
  10. start: 0,
  11. length: 4,
  12. styledKey: StyledStringKey.DECORATION,
  13. styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough, color: Color.Red, thicknessScale: 3 })
  14. },
  15. {
  16. start: 4,
  17. length: 2,
  18. styledKey: StyledStringKey.DECORATION,
  19. styledValue: new DecorationStyle(
  20. {
  21. type: TextDecorationType.Underline,
  22. },
  23. {
  24. // 开启多装饰线
  25. enableMultiType: true
  26. }
  27. )
  28. },
  29. {
  30. start: 4,
  31. length: 2,
  32. styledKey: StyledStringKey.DECORATION,
  33. styledValue: new DecorationStyle(
  34. {
  35. type: TextDecorationType.LineThrough,
  36. },
  37. {
  38. // 开启多装饰线
  39. enableMultiType: true
  40. }
  41. )
  42. },
  43. ]);
  44. controller: TextController = new TextController();

  46. async onPageShow() {
  47. this.controller.setStyledString(this.mutableStyledString);
  48. }

  50. build() {
  51. Column() {
  52. // 显示属性字符串
  53. Text(undefined, { controller: this.controller })
  54. }
  55. .width('100%')
  56. }
  57. }
  ```

  [StyledStringDecorationStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringDecorationStyle.ets#L15-L73)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/9EYOAxDbRmuPskwFWFYsfg/zh-cn_image_0000002558764334.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=44CD1D57927B2E2D584D8031FDE909D5323A6DD0A1FF34939DFB78E20F1EFE7F)
* 创建及应用文本基线偏移量对象（BaselineOffsetStyle）

  ```
  1. import { LengthMetrics } from '@kit.ArkUI';

  3. // xxx.ets
  4. @Entry
  5. @Component
  6. struct styled_string_demo5 {
  7. @State str: string =
  8. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply_Text_Third_Five') as string;

  10. mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [
  11. {
  12. start: 0,
  13. length: 3,
  14. styledKey: StyledStringKey.BASELINE_OFFSET,
  15. styledValue: new BaselineOffsetStyle(LengthMetrics.px(20))
  16. }
  17. ]);
  18. controller: TextController = new TextController();

  20. async onPageShow() {
  21. this.controller.setStyledString(this.mutableStyledString);
  22. }

  24. build() {
  25. Column() {
  26. // 显示属性字符串
  27. Text(undefined, { controller: this.controller })
  28. }
  29. .width('100%')
  30. }
  31. }
  ```

  [StyledStringBaselineOffsetStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringBaselineOffsetStyle.ets#L15-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/G1buKLViRiaOSrI9ffKXsw/zh-cn_image_0000002558604678.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=6E30A356243C807CC41A1C433A0EA5219AD3EE0B494FC2CA64AAF057255166CA)
* 创建及应用文本行高对象（LineHeightStyle）

  ```
  1. import { LengthMetrics } from '@kit.ArkUI';

  3. // xxx.ets
  4. @Entry
  5. @Component
  6. struct styled_string_demo6 {
  7. @State str: string =
  8. this.getUIContext()
  9. .getHostContext()?.resourceManager.getStringByNameSync('StyledStringStyle_Text_5') as string;
  10. mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [
  11. {
  12. start: 8,
  13. length: 3,
  14. styledKey: StyledStringKey.LINE_HEIGHT,
  15. styledValue: new LineHeightStyle(LengthMetrics.vp(50))
  16. }
  17. ]);
  18. controller: TextController = new TextController();

  20. async onPageShow() {
  21. this.controller.setStyledString(this.mutableStyledString);
  22. }

  24. build() {
  25. Column() {
  26. // 显示属性字符串
  27. Text(undefined, { controller: this.controller })
  28. }
  29. .width('100%')
  30. .margin({ top: 10 })
  31. }
  32. }
  ```

  [StyledStringLineHeightStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringLineHeightStyle.ets#L15-L48)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/zIOsLfiLTNqq6iqHbVSqDQ/zh-cn_image_0000002589324203.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=4E1A0F04D696FFDA8720191B53C1D38F1C573569273C0A6B6B987E43DFE5C85F)
* 创建及应用文本字符间距对象（LetterSpacingStyle）

  ```
  1. import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

  3. // xxx.ets
  4. @Entry
  5. @Component
  6. struct styled_string_demo7 {
  7. @State str: string =
  8. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('CreateApply_Text_Third_Five') as string;
  9. mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [
  10. {
  11. start: 0,
  12. length: 2,
  13. styledKey: StyledStringKey.LETTER_SPACING,
  14. styledValue: new LetterSpacingStyle(new LengthMetrics(20, LengthUnit.VP))
  15. }
  16. ]);
  17. controller: TextController = new TextController();

  19. async onPageShow() {
  20. this.controller.setStyledString(this.mutableStyledString);
  21. }

  23. build() {
  24. Column() {
  25. // 显示属性字符串
  26. Text(undefined, { controller: this.controller })
  27. }
  28. .width('100%')
  29. }
  30. }
  ```

  [StyledStringLetterSpacingStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringLetterSpacingStyle.ets#L15-L46)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/7iRor2QbTkOphaogSYzj9g/zh-cn_image_0000002589244143.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=D3BC694DF195F1AFBD646CACB89C033F5B8BBC1C642E0622E2D13570CF0FD091)

## 设置段落样式

可通过[ParagraphStyle](../harmonyos-references/ts-universal-styled-string.md#paragraphstyle)设置段落样式布局。下图显示了如何分割文本中的段落，段落以换行符 \n 结尾。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/gZaongqYRCOWFN1qirZ9cg/zh-cn_image_0000002558764336.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=25D32B03C09F3E8B02640744B34E7B44ACCAE73F15082D6800189299F1B954CF)

以下代码示例展示了如何创建ParagraphStyle并应用。如果将ParagraphStyle附加到段落开头、末尾或之间的任何位置，均会应用样式，非段落区间内则不会应用样式。

```
1. import { LengthMetrics} from '@kit.ArkUI';

3. // xxx.ets
4. @Entry
5. @Component
6. struct Index {
7. @State str: string =
8. this.getUIContext()
9. .getHostContext()?.resourceManager.getStringByNameSync('StyledStringParagraphStyle_Text_1') as string;
10. titleParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });
11. // 段落首行缩进15vp
12. paragraphStyleAttr1: ParagraphStyle = new ParagraphStyle({ textIndent: LengthMetrics.vp(15) });
13. // 行高样式对象
14. lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));
15. // 创建含段落样式的对象paragraphStyledString1
16. paragraphStyledString1: MutableStyledString =
17. new MutableStyledString(this.str, [
18. {
19. start: 0,
20. length: 4,
21. styledKey: StyledStringKey.PARAGRAPH_STYLE,
22. styledValue: this.titleParagraphStyleAttr
23. },
24. {
25. start: 0,
26. length: 4,
27. styledKey: StyledStringKey.LINE_HEIGHT,
28. styledValue: new LineHeightStyle(new LengthMetrics(50))
29. }, {
30. start: 0,
31. length: 4,
32. styledKey: StyledStringKey.FONT,
33. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
34. },
35. {
36. start: 5,
37. length: 3,
38. styledKey: StyledStringKey.PARAGRAPH_STYLE,
39. styledValue: this.paragraphStyleAttr1
40. },
41. {
42. start: 5,
43. length: 20,
44. styledKey: StyledStringKey.LINE_HEIGHT,
45. styledValue: this.lineHeightStyle1
46. }
47. ]);
48. controller: TextController = new TextController();

50. async onPageShow() {
51. this.controller.setStyledString(this.paragraphStyledString1);
52. }

54. build() {
55. Column() {
56. // 显示属性字符串
57. Text(undefined, { controller: this.controller })
58. }
59. .width('100%')
60. }
61. }
```

[StyledStringParagraphStyleOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringParagraphStyleOne.ets#L15-L77)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/6DvLra4cS7OkXF37XPlucA/zh-cn_image_0000002558604680.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=FC32A9A96522F379EBD399AEACD5867B73329F0B358301A3345121C95342850D)

除了可以在创建属性字符串时就预设样式，也可以后续通过[replaceStyle](../harmonyos-references/ts-universal-styled-string.md#replacestyle)清空原样式替换新样式，同时需要在附加的文本组件controller上主动触发更新绑定的属性字符串。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. // xxx.ets
4. @Entry
5. @Component
6. struct Index {
7. context = this.getUIContext().getHostContext();
8. /* 请将$r('app.string.StyledStringParagraphStyle_Text_2')替换为实际资源文件，在本示例中该资源文件的value值为
9. "段落标题\n正文第一段落开始0123456789正文第一段落结束，通过replaceStyle清空原样式替换新样式。"*/
10. @State message1: string =
11. this.context!.resourceManager.getStringSync($r('app.string.StyledStringParagraphStyle_Text_2').id);
12. titleParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });
13. // 段落首行缩进15vp
14. paragraphStyleAttr1: ParagraphStyle = new ParagraphStyle({ textIndent: LengthMetrics.vp(15) });
15. // 行高样式对象
16. lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));
17. // 创建含段落样式的对象paragraphStyledString1
18. paragraphStyledString1: MutableStyledString =
19. new MutableStyledString(this.message1, [
20. {
21. start: 0,
22. length: 4,
23. styledKey: StyledStringKey.PARAGRAPH_STYLE,
24. styledValue: this.titleParagraphStyleAttr
25. },
26. {
27. start: 0,
28. length: 4,
29. styledKey: StyledStringKey.LINE_HEIGHT,
30. styledValue: new LineHeightStyle(new LengthMetrics(50))
31. }, {
32. start: 0,
33. length: 4,
34. styledKey: StyledStringKey.FONT,
35. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
36. },
37. {
38. start: 5,
39. length: 3,
40. styledKey: StyledStringKey.PARAGRAPH_STYLE,
41. styledValue: this.paragraphStyleAttr1
42. },
43. {
44. start: 5,
45. length: 20,
46. styledKey: StyledStringKey.LINE_HEIGHT,
47. styledValue: this.lineHeightStyle1
48. }
49. ]);
50. paragraphStyleAttr3: ParagraphStyle = new ParagraphStyle({
51. textAlign: TextAlign.End,
52. maxLines: 1,
53. wordBreak: WordBreak.BREAK_ALL,
54. overflow: TextOverflow.Ellipsis
55. });
56. controller: TextController = new TextController();

58. async onPageShow() {
59. this.controller.setStyledString(this.paragraphStyledString1);
60. }

62. build() {
63. Column() {
64. // 显示属性字符串
65. Text(undefined, { controller: this.controller }).width(300)
66. // 请将$r('app.string.Replace_paragraph_style')替换为实际资源文件，在本示例中该资源文件的value值为"替换段落样式"
67. Button($r('app.string.Replace_paragraph_style'))
68. .onClick(() => {
69. this.paragraphStyledString1.replaceStyle({
70. start: 5,
71. length: 3,
72. styledKey: StyledStringKey.PARAGRAPH_STYLE,
73. styledValue: this.paragraphStyleAttr3
74. });
75. this.controller.setStyledString(this.paragraphStyledString1);
76. })
77. }
78. .width('100%')
79. }
80. }
```

[StyledStringReplaceParagraphStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringReplaceParagraphStyle.ets#L15-L96)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/8SQVYO4MQ1iqA-0myhYSNg/zh-cn_image_0000002589324205.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=B562D3F86B7D3C49054C9975D7241B2590E4438F6CC46C63E5FD26FC621CA54E)

## 支持将属性字符串转换成Paragraph

可通过[getParagraphs](../harmonyos-references/arkts-apis-uicontext-measureutils.md#getparagraphs20)将属性字符串根据文本布局选项转换成对应的[Paragraph](../harmonyos-references/js-apis-graphics-text.md#paragraph)数组。

* 以下示例展示了通过[MeasureUtils](../harmonyos-references/arkts-apis-uicontext-measureutils.md)的getParagraphs方法测算文本，当内容超出最大显示行数的时候，截断文本显示并展示“...全文”的效果。

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

  51. public width: number = 160;
  52. public word: string = 'drawing';
  53. public height: number = 10;
  54. public context: UIContext;
  55. }

  57. @Entry
  58. @Component
  59. struct Index {
  60. // 请在resources\base\element\string.json文件中配置name为'Full_text'，value为非空字符串的资源
  61. @State fullText: string =
  62. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Full_text') as string;
  63. // 请将$r('app.string.Original_text')替换为实际资源文件，在本示例中该资源文件的value值为"原文"
  64. @State originalText: ResourceStr = $r('app.string.Original_text');
  65. // 请将$r('app.string.After_typesetting')替换为实际资源文件，在本示例中该资源文件的value值为"排版后"
  66. @State afterTypesetting: ResourceStr = $r('app.string.After_typesetting');
  67. str: string =
  68. 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.';
  69. mutableStr2 = new MutableStyledString(this.str, [
  70. {
  71. start: 0,
  72. length: 3,
  73. styledKey: StyledStringKey.FONT,
  74. styledValue: new TextStyle({ fontSize: LengthMetrics.px(20) })
  75. },
  76. {
  77. start: 3,
  78. length: 3,
  79. styledKey: StyledStringKey.FONT,
  80. styledValue: new TextStyle({ fontColor: Color.Brown })
  81. }
  82. ]);

  84. // 测算属性字符串在指定宽度下能显示的行数
  85. getLineNum(styledString: StyledString, width: LengthMetrics) {
  86. let paragraphArr = this.getUIContext().getMeasureUtils().getParagraphs(styledString, { constraintWidth: width });
  87. let res = 0;
  88. for (let i = 0; i < paragraphArr.length; ++i) {
  89. res += paragraphArr[i].getLineCount();
  90. }
  91. return res;
  92. }

  94. // 测算属性字符串显示maxLines行时最多可以显示的字数
  95. getCorrectIndex(styledString: MutableStyledString, maxLines: number, width: LengthMetrics) {
  96. let low = 0;
  97. let high = styledString.length - 1;
  98. // 使用二分查找
  99. while (low <= high) {
  100. let mid = (low + high) >> 1;
  101. console.info('demo: get ' + low + ' ' + high + ' ' + mid);
  102. let moreStyledString = new MutableStyledString(this.fullText, [{
  103. start: 4,
  104. length: 2,
  105. styledKey: StyledStringKey.FONT,
  106. styledValue: new TextStyle({ fontColor: Color.Blue })
  107. }]);
  108. moreStyledString.insertStyledString(0, styledString.subStyledString(0, mid));
  109. let lineNum = this.getLineNum(moreStyledString, LengthMetrics.px(500));
  110. if (lineNum <= maxLines) {
  111. low = mid + 1;
  112. } else {
  113. high = mid - 1;
  114. }
  115. }
  116. return high;
  117. }

  119. mutableStrAllContent = new MutableStyledString(this.str, [
  120. {
  121. start: 0,
  122. length: 3,
  123. styledKey: StyledStringKey.FONT,
  124. styledValue: new TextStyle({ fontSize: LengthMetrics.px(40) })
  125. },
  126. {
  127. start: 3,
  128. length: 3,
  129. styledKey: StyledStringKey.FONT,
  130. styledValue: new TextStyle({ fontColor: Color.Brown })
  131. }
  132. ]);
  133. customSpan1: MyCustomSpan = new MyCustomSpan('Hello', 120, 10, this.getUIContext());
  134. mutableStrAllContent2 = new MutableStyledString(this.str, [
  135. {
  136. start: 0,
  137. length: 3,
  138. styledKey: StyledStringKey.FONT,
  139. styledValue: new TextStyle({ fontSize: LengthMetrics.px(100) })
  140. },
  141. {
  142. start: 3,
  143. length: 3,
  144. styledKey: StyledStringKey.FONT,
  145. styledValue: new TextStyle({ fontColor: Color.Brown })
  146. }
  147. ]);
  148. controller: TextController = new TextController();
  149. controller2: TextController = new TextController();
  150. textController: TextController = new TextController();
  151. textController2: TextController = new TextController();

  153. aboutToAppear() {
  154. this.mutableStrAllContent2.insertStyledString(0, new StyledString(this.customSpan1));
  155. this.mutableStr2.insertStyledString(0, new StyledString(this.customSpan1));
  156. }

  158. build() {
  159. Scroll() {
  160. Column() {
  161. Text(this.originalText)
  162. Text(undefined, { controller: this.controller }).width('500px').onAppear(() => {
  163. this.controller.setStyledString(this.mutableStrAllContent);
  164. })
  165. Divider().strokeWidth(8).color('#F1F3F5')
  166. Text(this.afterTypesetting)
  167. Text(undefined, { controller: this.textController }).onAppear(() => {
  168. let now = this.getCorrectIndex(this.mutableStrAllContent, 3, LengthMetrics.px(500));
  169. if (now != this.mutableStrAllContent.length - 1) {
  170. let moreStyledString = new MutableStyledString(this.fullText, [{
  171. start: 4,
  172. length: 2,
  173. styledKey: StyledStringKey.FONT,
  174. styledValue: new TextStyle({ fontColor: Color.Blue })
  175. }]);
  176. moreStyledString.insertStyledString(0, this.mutableStrAllContent.subStyledString(0, now));
  177. this.textController.setStyledString(moreStyledString);
  178. } else {
  179. this.textController.setStyledString(this.mutableStrAllContent);
  180. }
  181. })
  182. .width('500px')
  183. Divider().strokeWidth(8).color('#F1F3F5')
  184. Text(this.originalText)
  185. Text(undefined, { controller: this.controller2 }).width('500px').onAppear(() => {
  186. this.controller2.setStyledString(this.mutableStrAllContent2);
  187. })
  188. Divider().strokeWidth(8).color('#F1F3F5')
  189. Text(this.afterTypesetting)
  190. Text(undefined, { controller: this.textController2 }).onAppear(() => {
  191. let now = this.getCorrectIndex(this.mutableStrAllContent2, 3, LengthMetrics.px(500));
  192. let moreStyledString = new MutableStyledString(this.fullText, [{
  193. start: 4,
  194. length: 2,
  195. styledKey: StyledStringKey.FONT,
  196. styledValue: new TextStyle({ fontColor: Color.Blue })
  197. }]);
  198. moreStyledString.insertStyledString(0, this.mutableStrAllContent2.subStyledString(0, now));
  199. this.textController2.setStyledString(moreStyledString);
  200. })
  201. .width('500px')
  202. }.width('100%')
  203. }
  204. }
  205. }
  ```

  [StyledStringConvertedToParagraph.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringConvertedToParagraph.ets#L15-L221)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/XAaal4GCQ2i5rXXSfYdLnw/zh-cn_image_0000002589244145.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=DEC14D739B08EF38D598D5AEE5A19E53F176EE10875E9AF9AC4966C00723ADDE)

## 使用图片

可通过[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)来添加图片。

以下示例展示了如何将图片和文本附加到同一个MutableStyledString对象上，并实现图文混排。

说明

属性字符串的构造函数[constructor](../harmonyos-references/ts-universal-styled-string.md#constructor)中，当入参value的类型为ImageAttachment或CustomSpan时，styles参数不生效。需要设置styles时，通过[setStyle](../harmonyos-references/ts-universal-styled-string.md#setstyle)、[insertStyledString](../harmonyos-references/ts-universal-styled-string.md#insertstyledstring)等方法实现。

```
1. // xxx.ets
2. import { image } from '@kit.ImageKit';
3. import { LengthMetrics } from '@kit.ArkUI';

5. @Entry
6. @Component
7. export struct StyledStringImageAttachment {
8. @State abled: boolean = true;
9. @State message: string = 'Hello World';
10. imagePixelMap: image.PixelMap | undefined = undefined;
11. @State imagePixelMap3: image.PixelMap | undefined = undefined;
12. mutableStr: MutableStyledString = new MutableStyledString('123');
13. controller: TextController = new TextController();
14. mutableStr2: MutableStyledString = new MutableStyledString('This is set decoration line style to the mutableStr2', [{
15. start: 0,
16. length: 15,
17. styledKey: StyledStringKey.DECORATION,
18. styledValue: new DecorationStyle({
19. type: TextDecorationType.Overline,
20. color: Color.Orange,
21. style: TextDecorationStyle.DOUBLE
22. })
23. }]);

25. async aboutToAppear() {
26. console.info('aboutToAppear initial imagePixelMap');
27. // $r('app.media.sea')需要替换为开发者所需的图像资源文件。
28. this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.sea'));
29. }

31. private async getPixmapFromMedia(resource: Resource) {
32. let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
33. let imageSource = image.createImageSource(unit8Array?.buffer?.slice(0, unit8Array?.buffer?.byteLength));
34. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
35. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
36. });
37. await imageSource.release();
38. return createPixelMap;
39. }

41. leadingMarginValue: ParagraphStyle = new ParagraphStyle({ leadingMargin: LengthMetrics.vp(5)});
42. //行高样式对象
43. lineHeightStyle1: LineHeightStyle= new LineHeightStyle(new LengthMetrics(24));
44. //Bold样式
45. boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });
46. //创建含段落样式的对象paragraphStyledString1
47. // 请将$r('app.string.StyledStringImageAttachment_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"\n品牌相纸 高清冲印30张\n限时直降5.15元 限量赠送"
48. paragraphStyledString1: MutableStyledString =
49. new MutableStyledString(this.getUIContext()
50. .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringImageAttachment_Text_1').id), [
51. {
52. start: 0,
53. length: 28,
54. styledKey: StyledStringKey.PARAGRAPH_STYLE,
55. styledValue: this.leadingMarginValue
56. },
57. {
58. start: 14,
59. length: 9,
60. styledKey: StyledStringKey.FONT,
61. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontColor: '#B22222' })
62. },
63. {
64. start: 24,
65. length: 4,
66. styledKey: StyledStringKey.FONT,
67. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontWeight: FontWeight.Lighter })
68. },
69. {
70. start: 11,
71. length: 4,
72. styledKey: StyledStringKey.LINE_HEIGHT,
73. styledValue: this.lineHeightStyle1
74. }
75. ]);
76. // 请将$r('app.string.StyledStringImageAttachment_Text_2')替换为实际资源文件，在本示例中该资源文件的value值为"\n￥16.21 3000+人好评"
77. paragraphStyledString2: MutableStyledString =
78. new MutableStyledString(this.getUIContext()
79. .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringImageAttachment_Text_2').id), [
80. {
81. start: 0,
82. length: 5,
83. styledKey: StyledStringKey.PARAGRAPH_STYLE,
84. styledValue: this.leadingMarginValue
85. },
86. {
87. start: 0,
88. length: 4,
89. styledKey: StyledStringKey.LINE_HEIGHT,
90. styledValue: new LineHeightStyle(new LengthMetrics(60))
91. },
92. {
93. start: 0,
94. length: 7,
95. styledKey: StyledStringKey.FONT,
96. styledValue: this.boldTextStyle
97. },
98. {
99. start: 1,
100. length: 1,
101. styledKey: StyledStringKey.FONT,
102. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18) })
103. },
104. {
105. start: 2,
106. length: 2,
107. styledKey: StyledStringKey.FONT,
108. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(36) })
109. },
110. {
111. start: 4,
112. length: 3,
113. styledKey: StyledStringKey.FONT,
114. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(20) })
115. },
116. {
117. start: 7,
118. length: 9,
119. styledKey: StyledStringKey.FONT,
120. styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14)})
121. }
122. ]);

124. build() {
125. NavDestination() {
126. Column({ space: 12 }) {
127. // ...
128. Row() {
129. Column({ space: 10 }) {
130. Text(undefined, { controller: this.controller })
131. .id('text1')
132. .copyOption(CopyOptions.InApp)
133. .draggable(true)
134. .backgroundColor('#FFFFFF')
135. .borderRadius(5)
136. // 请将$r('app.string.StyledStringImageAttachment_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击查看商品卡片"
137. Button($r('app.string.StyledStringImageAttachment_Button_1'))
138. .enabled(this.abled)
139. .onClick(() => {
140. if (this.imagePixelMap !== undefined) {
141. this.mutableStr = new MutableStyledString(new ImageAttachment({
142. value: this.imagePixelMap,
143. size: { width: 180, height: 160 },
144. verticalAlign: ImageSpanAlignment.BASELINE,
145. objectFit: ImageFit.Fill
146. }));
147. this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
148. this.mutableStr.appendStyledString(this.paragraphStyledString1);
149. this.controller.setStyledString(this.mutableStr);
150. }
151. this.abled = false;
152. })
153. }
154. .width('100%')
155. }
156. .height('100%')
157. .backgroundColor('#F8F8FF')
158. }
159. // ...
160. }
161. .backgroundColor('#f1f2f3')
162. // 请将$r('app.string.StyledStringImageAttachment_title')替换为实际资源文件，在本示例中该资源文件的value值为"通过ImageAttachment来添加图片"
163. .title($r('app.string.StyledStringImageAttachment_title'))
164. }
165. }
```

[StyledStringImageAttachment.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringImageAttachment.ets#L18-L186)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/TDqSo6VpQ5CepX0E8LJpbQ/zh-cn_image_0000002558764338.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=89F696FBB631EA9C9226DE9596720023ED3B60FA35E1E4FD7BE3F7678F1B42BC)

## 设置事件

可通过[GestureStyle](../harmonyos-references/ts-universal-styled-string.md#gesturestyle)设置onClick、onLongPress事件来使文本响应点击长按事件。

除了初始化属性字符串对象即初始样式对象，亦可通过[setStyle](../harmonyos-references/ts-universal-styled-string.md#setstyle)接口再叠加新样式或更新已有样式，同时需要在附加的文本组件controller上主动触发更新绑定的属性字符串。

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let gUIContext: UIContext;

5. class MyCustomSpan extends CustomSpan {
6. constructor(word: string, width: number, height: number, fontSize: number) {
7. super();
8. this.word = word;
9. this.width = width;
10. this.height = height;
11. this.fontSize = fontSize;
12. }

14. onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics {
15. return { width: this.width, height: this.height };
16. }

18. onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
19. let canvas = context.canvas;

21. const brush = new drawing.Brush();
22. brush.setColor({
23. alpha: 255,
24. red: 0,
25. green: 0,
26. blue: 0
27. });
28. const font = new drawing.Font();
29. font.setSize(gUIContext.vp2px(this.fontSize));
30. const textBlob =
31. drawing.TextBlob.makeFromString(this.word.substring(0, 5), font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
32. canvas.attachBrush(brush);

34. this.onDrawRectByRadius(context, options.x, options.x + gUIContext.vp2px(this.width), options.lineTop,
35. options.lineBottom, 20);
36. brush.setColor({
37. alpha: 255,
38. red: 255,
39. green: 255,
40. blue: 255
41. });
42. canvas.attachBrush(brush);
43. canvas.drawTextBlob(textBlob, options.x, options.lineBottom - 30);
44. brush.setColor({
45. alpha: 255,
46. red: 255,
47. green: 228,
48. blue: 196
49. });
50. canvas.attachBrush(brush);
51. const textBlob1 =
52. drawing.TextBlob.makeFromString(this.word.substring(5), font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
53. canvas.drawTextBlob(textBlob1, options.x + gUIContext.vp2px(100), options.lineBottom - 30);

55. canvas.detachBrush();
56. }

58. onDrawRectByRadius(context: DrawContext, left: number, right: number, top: number, bottom: number, radius: number) {
59. let canvas = context.canvas;
60. let path = new drawing.Path();

62. // 画带radius的rect
63. path.moveTo(left + radius, top);
64. path.lineTo(right - radius, top);
65. path.arcTo(right - 2 * radius, top, right, top + 2 * radius, 270, 90);
66. path.lineTo(right, bottom - radius);
67. path.arcTo(right - 2 * radius, bottom - 2 * radius, right, bottom, 0, 90);

69. path.lineTo(left + 2 * radius, bottom);
70. path.arcTo(left, bottom - 2 * radius, left + 2 * radius, bottom, 90, 90);
71. path.lineTo(left, top + 2 * radius);
72. path.arcTo(left, top, left + 2 * radius, top + 2 * radius, 180, 90);

74. canvas.drawPath(path);
75. }

77. setWord(word: string) {
78. this.word = word;
79. }

81. public width: number = 160;
82. public word: string = 'drawing';
83. public height: number = 10;
84. public fontSize: number = 16;
85. }

87. @Entry
88. @Component
89. export struct StyledStringGestureStyle {
90. customSpan3: MyCustomSpan = new MyCustomSpan('99VIP88%off', 200, 40, 30);
91. customSpanStyledString: MutableStyledString = new MutableStyledString(this.customSpan3);
92. textController: TextController = new TextController();
93. isPageShow: boolean = true;
94. @State backgroundColor1: ResourceColor | undefined = undefined;
95. gestureStyleAttr: GestureStyle = new GestureStyle({
96. onClick: () => {
97. this.backgroundColor1 = Color.Green;
98. },
99. onLongPress: () => {
100. this.backgroundColor1 = Color.Grey;
101. }
102. });

104. aboutToAppear() {
105. gUIContext = this.getUIContext();
106. }

108. async onPageShow() {
109. if (!this.isPageShow) {
110. return;
111. }
112. this.isPageShow = false;
113. this.customSpanStyledString.setStyle({
114. start: 0,
115. length: 1,
116. styledKey: StyledStringKey.GESTURE,
117. styledValue: this.gestureStyleAttr
118. })
119. this.textController.setStyledString(this.customSpanStyledString);
120. }

122. build() {
123. NavDestination() {
124. Column({ space: 12 }) {
125. // ...
126. Row() {
127. Column() {
128. // 请将$r('app.string.StyledStringGestureStyle_button_content')替换为实际资源文件，在本示例中该资源文件的value值为"响应属性字符串事件改变背景色"
129. Button($r('app.string.StyledStringGestureStyle_button_content'))
130. .backgroundColor(this.backgroundColor1)
131. .width('80%')
132. .margin(10)
133. Text(undefined, { controller: this.textController })
134. .id('text1')
135. .copyOption(CopyOptions.InApp)
136. .fontSize(30)
137. }
138. .width('100%')
139. }
140. .height('100%')
141. }
142. // ...
143. }
144. .backgroundColor('#f1f2f3')
145. // 请将$r('app.string.TStyledStringGestureStyle_title')替换为实际资源文件，在本示例中该资源文件的value值为"设置事件"
146. .title($r('app.string.TStyledStringGestureStyle_title'))
147. }
148. }
```

[StyledStringGestureStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringGestureStyle.ets#L17-L170)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/_GPF8szoRpKpuCq8eYwjGw/zh-cn_image_0000002558604682.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=80CA11352E2455962919B8F4D863D41F88F51E07B90EEE96F8057B80D71A3217)

## 格式转换

可以通过[toHtml](../harmonyos-references/ts-universal-styled-string.md#tohtml14)、[fromHtml](../harmonyos-references/ts-universal-styled-string.md#fromhtml)接口实现属性字符串与HTML格式字符串的相关转换，当前支持转换的HTML标签范围：<p>、<span>、<img>、<br>、<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>。

* 以下示例展示了如何将属性字符串转换成HTML格式，并展示了如何从HTML格式转换回属性字符串。

```
1. // xxx.ets
2. import { image } from '@kit.ImageKit';
3. import { LengthMetrics } from '@kit.ArkUI';

5. @Entry
6. @Component
7. export struct StyledStringHtml {
8. imagePixelMap: image.PixelMap | undefined = undefined;
9. @State html: string | undefined = undefined;
10. @State styledString: StyledString | undefined = undefined;
11. controller1: TextController = new TextController;
12. controller2: TextController = new TextController;
13. private uiContext: UIContext = this.getUIContext();

15. async aboutToAppear() {
16. console.info('aboutToAppear initial imagePixelMap');
17. this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.startIcon'));
18. }

20. private async getPixmapFromMedia(resource: Resource) {
21. let unit8Array = await this.uiContext.getHostContext()?.resourceManager?.getMediaContent(resource.id);
22. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
23. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
24. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
25. });
26. await imageSource.release();
27. return createPixelMap;
28. }

30. build() {
31. NavDestination() {
32. Column({ space: 12 }) {
33. // ...
34. Column() {
35. Text(undefined, { controller: this.controller1 }).height(100)
36. Row() {
37. // 请将$r('app.string.StyledStringHtml_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"添加属性字符串"
38. Button($r('app.string.StyledStringHtml_Button_1')).onClick(() => {
39. // 请将$r('app.string.StyledStringHtml_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"属性字符串"
40. let mutableStyledString1: MutableStyledString =
41. new MutableStyledString(this.getUIContext()
42. .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringHtml_Text_1').id), [{
43. start: 0,
44. length: 6,
45. styledKey: StyledStringKey.FONT,
46. styledValue: new TextStyle({ fontColor: Color.Green, fontSize: LengthMetrics.px(50) })
47. }]);
48. if (this.imagePixelMap !== undefined) {
49. let mutableStyledString2 = new MutableStyledString(new ImageAttachment({
50. value: this.imagePixelMap,
51. size: { width: 50, height: 50 },
52. }));
53. mutableStyledString1.appendStyledString(mutableStyledString2);
54. }
55. this.styledString = mutableStyledString1;
56. this.controller1.setStyledString(mutableStyledString1);
57. }).margin(5)
58. // 请将$r('app.string.StyledStringHtml_Button_2')替换为实际资源文件，在本示例中该资源文件的value值为"toHtml"
59. Button($r('app.string.StyledStringHtml_Button_2')).onClick(() => {
60. this.html = StyledString.toHtml(this.styledString);
61. }).margin(5)
62. // 请将$r('app.string.StyledStringHtml_Button_3')替换为实际资源文件，在本示例中该资源文件的value值为"fromHtml"
63. Button($r('app.string.StyledStringHtml_Button_3')).onClick(async () => {
64. let styledString = await StyledString.fromHtml(this.html);
65. this.controller2.setStyledString(styledString);
66. }).margin(5)
67. }

69. Text(undefined, { controller: this.controller2 }).height(100)
70. Text(this.html)
71. }.width('100%')
72. }
73. // ...
74. }
75. .backgroundColor('#f1f2f3')
76. // 请将$r('app.string.StyledStringHtml_title')替换为实际资源文件，在本示例中该资源文件的value值为"格式转换"
77. .title($r('app.string.StyledStringHtml_title'))
78. }
79. }
```

[StyledStringHtml.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringHtml.ets#L18-L101)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/7UIPZoY6TxGXjk3K4ideEA/zh-cn_image_0000002589324207.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=A607F26A79129DCE94045CFEBD633766C0A8077FCD5DC493B7541049B51A933B)

* 将HTML中<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>标签及其style属性中的background-color转换为属性字符串并转回HTML。

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct HtmlSpanStringDemo {
  5. @State html: string =
  6. "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span style =   \"foreground-color:blue\"> <a href='https://www.example.com'>www.example</a> </span> <span   style=\"background-color: red;\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>";
  7. @State spanString: StyledString | undefined = undefined;
  8. @State resultText: string = ''; // 保存结果文本的状态
  9. controller: TextController = new TextController;

  11. build() {
  12. Column() {
  13. // 显示转换后的spanString
  14. Text(undefined, { controller: this.controller }).height(100).id('text1')

  16. // TextArea显示每个步骤的结果
  17. TextArea({ text: this.html })
  18. .width('100%')
  19. .height(100)
  20. .margin(5)

  22. // 按钮1:将HTML转换为SpanString
  23. // 请将$r('app.string.Converted_HTML_to_SpanString')替换为实际资源文件，在本示例中该资源文件的value值为"Converted HTML to SpanString"
  24. Button($r('app.string.Converted_HTML_to_SpanString')).onClick(async () => {
  25. this.spanString = await StyledString.fromHtml(this.html);
  26. this.controller.setStyledString(this.spanString);
  27. this.resultText = 'Converted HTML to SpanString successfully.';
  28. }).margin(5)

  30. // 按钮2:将SpanString转换为HTML
  31. // 请将$r('app.string.Converted_SpanString_to_HTML')替换为实际资源文件，在本示例中该资源文件的value值为"Converted SpanString to HTML"
  32. Button($r('app.string.Converted_SpanString_to_HTML')).onClick(() => {
  33. if (this.spanString) {
  34. // 将spanString转换为HTML并替换当前的HTML状态
  35. const newHtml = StyledString.toHtml(this.spanString);
  36. if (newHtml !== this.html) { // 通过检查内容是否已经相同来防止重复
  37. this.html = newHtml;
  38. }
  39. this.resultText = 'Converted SpanString to HTML successfully.';
  40. } else {
  41. this.resultText = 'SpanString is undefined.';
  42. }
  43. }).margin(5)

  45. // 按钮3:将HTML转换回SpanString
  46. /* 请将$r('app.string.Converted_HTML_back_to_SpanString')替换为实际资源文件，在本示例中该资源文件的
  47. value值为"Converted HTML back to SpanString" */
  48. Button($r('app.string.Converted_HTML_back_to_SpanString')).onClick(async () => {
  49. this.spanString = await StyledString.fromHtml(this.html);
  50. this.controller.setStyledString(this.spanString);
  51. this.resultText = 'Converted HTML back to SpanString successfully.';
  52. }).margin(5)

  54. // 重置：重置HTML和SpanString
  55. // 请将$r('app.string.Reset')替换为实际资源文件，在本示例中该资源文件的value值为"Reset"
  56. Button($r('app.string.Reset')).onClick(() => {
  57. this.html =
  58. "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span   style = \"foreground-color:blue\"> <a href='https://www.example.com'>www.example</a> </span> <span   style=\"background-color: red;\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>";
  59. this.spanString = undefined;
  60. this.controller.setStyledString(new StyledString('')); // 使用空的StyledString实例
  61. this.resultText = 'Reset HTML and SpanString successfully.';
  62. }).margin(5)
  63. }.width('100%').padding(20)
  64. }
  65. }
  ```

  [StyledStringHtmlOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringHtmlOne.ets#L15-L81)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/sC3KYdDNTWqaApEwV7A3Hw/zh-cn_image_0000002589244147.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=786AD41B3BE51441586079B13FAD014BC11E5F3397F5146A63995EE39BECDB24)

## 场景示例

该示例通过ParagraphStyle、LineHeightStyle、TextStyle对象展示了会员过期提示的效果。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. export struct StyledStringSceneExample {
6. alignCenterParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });
7. //行高样式对象
8. lineHeightStyle1: LineHeightStyle = new LineHeightStyle(LengthMetrics.vp(24));
9. //Bold样式
10. boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });
11. //创建含段落样式的对象paragraphStyledString1
12. // 请将$r('app.string.StyledStringSceneExample_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"您的豪华钻石已过期1天\n续费可继续享受会员专属权益"
13. paragraphStyledString1: MutableStyledString =
14. new MutableStyledString(this.getUIContext()
15. .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample_Text_1').id), [
16. {
17. start: 0,
18. length: 4,
19. styledKey: StyledStringKey.PARAGRAPH_STYLE,
20. styledValue: this.alignCenterParagraphStyleAttr
21. },
22. {
23. start: 0,
24. length: 4,
25. styledKey: StyledStringKey.LINE_HEIGHT,
26. styledValue: new LineHeightStyle(LengthMetrics.vp(40))
27. },
28. {
29. start: 11,
30. length: 14,
31. styledKey: StyledStringKey.FONT,
32. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontColor: Color.Grey })
33. },
34. {
35. start: 11,
36. length: 4,
37. styledKey: StyledStringKey.PARAGRAPH_STYLE,
38. styledValue: this.alignCenterParagraphStyleAttr
39. },
40. {
41. start: 11,
42. length: 4,
43. styledKey: StyledStringKey.LINE_HEIGHT,
44. styledValue: this.lineHeightStyle1
45. }
46. ]);
47. // 请将$r('app.string.StyledStringSceneExample_Text_2')替换为实际资源文件，在本示例中该资源文件的value值为"\n￥4.88￥15"
48. paragraphStyledString2: MutableStyledString =
49. new MutableStyledString(this.getUIContext()
50. .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample_Text_2').id), [
51. {
52. start: 0,
53. length: 4,
54. styledKey: StyledStringKey.PARAGRAPH_STYLE,
55. styledValue: this.alignCenterParagraphStyleAttr
56. },
57. {
58. start: 0,
59. length: 4,
60. styledKey: StyledStringKey.LINE_HEIGHT,
61. styledValue: new LineHeightStyle(LengthMetrics.vp(60))
62. },
63. {
64. start: 0,
65. length: 6,
66. styledKey: StyledStringKey.FONT,
67. styledValue: this.boldTextStyle
68. },
69. {
70. start: 1,
71. length: 1,
72. styledKey: StyledStringKey.FONT,
73. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18) })
74. },
75. {
76. start: 2,
77. length: 4,
78. styledKey: StyledStringKey.FONT,
79. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(40) })
80. },
81. {
82. start: 6,
83. length: 3,
84. styledKey: StyledStringKey.FONT,
85. styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14) })
86. },
87. {
88. start: 6,
89. length: 3,
90. styledKey: StyledStringKey.DECORATION,
91. styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough, color: Color.Grey })
92. }
93. ]);
94. // 请将$r('app.string.StyledStringSceneExample_Text_3')替换为实际资源文件，在本示例中该资源文件的value值为"\n02时06分后将失去该优惠"
95. paragraphStyledString3: MutableStyledString =
96. new MutableStyledString(this.getUIContext()
97. .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample_Text_3').id), [
98. {
99. start: 0,
100. length: 4,
101. styledKey: StyledStringKey.PARAGRAPH_STYLE,
102. styledValue: this.alignCenterParagraphStyleAttr
103. },
104. {
105. start: 0,
106. length: 4,
107. styledKey: StyledStringKey.LINE_HEIGHT,
108. styledValue: new LineHeightStyle(LengthMetrics.vp(30))
109. },
110. {
111. start: 1,
112. length: 2,
113. styledKey: StyledStringKey.FONT,
114. styledValue: new TextStyle({ fontColor: '#FFD700', fontWeight: FontWeight.Bold })
115. },
116. {
117. start: 4,
118. length: 2,
119. styledKey: StyledStringKey.FONT,
120. styledValue: new TextStyle({ fontColor: '#FFD700', fontWeight: FontWeight.Bold })
121. }
122. ]);
123. controller: TextController = new TextController();

125. build() {
126. NavDestination() {
127. Column({ space: 12 }) {
128. // ...
129. Row() {
130. Column({ space: 5 }) {
131. Text(undefined, { controller: this.controller })
132. .id('text1')
133. .width(240)
134. .copyOption(CopyOptions.InApp)
135. .draggable(true)
136. .onAppear(() => {
137. this.paragraphStyledString2.appendStyledString(this.paragraphStyledString3);
138. this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
139. this.controller.setStyledString(this.paragraphStyledString1);
140. })
141. // 请将$r('app.string.StyledStringSceneExample_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"限时4.88元 立即续费"
142. Button($r('app.string.StyledStringSceneExample_Button_1'))
143. .width(200)
144. .fontColor(Color.White)
145. .fontSize(18)
146. .backgroundColor('#3CB371')
147. .margin({ bottom: 10 })
148. }
149. .borderWidth(1).borderColor('#FFDEAD')
150. .margin({ left: 10 })
151. }
152. .height('60%')
153. }
154. // ...
155. }
156. .backgroundColor('#f1f2f3')
157. // 请将$r('app.string.StyledStringSceneExample_title')替换为实际资源文件，在本示例中该资源文件的value值为"场景示例"
158. .title($r('app.string.StyledStringSceneExample_title'))
159. }
160. }
```

[StyledStringSceneExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/propertyString/StyledStringSceneExample.ets#L18-L180)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/LEhyzmCST7CqPj1Mz632jA/zh-cn_image_0000002558764340.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=1B88D1CA5D055403AFB33F03DBAEF39149BA2D4BE52327D252C935486D23EDE8)
