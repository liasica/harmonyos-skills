---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display
title: 文本显示 (Text/Span)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 文本显示 (Text/Span)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9d6de8c407795e964c26024a077615b7532d73a32cdd907d8543603bfe45cd34
---

Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于展示行内文本。

具体用法请参考[Text](../harmonyos-references/ts-basic-components-text.md)和[Span](../harmonyos-references/ts-basic-components-span.md)组件的API文档。

常见问题请参考[文本显示（Text/Span）常见问题](arkts-text-faq.md#文本显示textspan常见问题)。

## 创建文本

Text可通过以下两种方式来创建：

* string字符串。

  ```
  1. Text('我是一段文本')
  ```

  [CreateText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CreateText.ets#L25-L28)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/32CG9ZPMRCKWMJLc9F1Gow/zh-cn_image_0000002583477791.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=32A768D1800E3F0F3969A4915C158B9DDBCFA1F1913D6C11E6DB623D4D067866)

* 引用Resource资源。

  资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json，具体内容如下：

  ```
  1. {
  2. "string": [
  3. {
  4. "name": "module_desc",
  5. "value": "模块描述"
  6. }
  7. ]
  8. }
  ```

  ```
  1. // 请将$r('app.string.module_desc')替换为实际资源文件，在本示例中该资源文件的value值为"模块描述"
  2. Text($r('app.string.module_desc'))
  3. .baselineOffset(0)
  4. .fontSize(30)
  5. .border({ width: 1 })
  6. .padding(10)
  7. .width(300)
  ```

  [CreateText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CreateText.ets#L35-L43)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Br6ijKAsR2iHMFzHtxWQvg/zh-cn_image_0000002552798142.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=5966D5565C16CC83BA66DFEECD6DCE86CB1E691F84D33930F72FC23B0A2719C2)

## 添加子组件

[Span](../harmonyos-references/ts-basic-components-span.md)只能作为[Text](../harmonyos-references/ts-basic-components-text.md)和[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

* 创建Span。

  Span组件需嵌入在Text组件中才能显示，单独使用时不会显示任何内容。Text与Span同时配置文本内容时，Span内容将覆盖Text内容。

  ```
  1. // 请将$r('app.string.TextSpan_textContent_text')替换为实际资源文件，在本示例中该资源文件的value值为"我是Text"
  2. Text($r('app.string.TextSpan_textContent_text')) {
  3. // 请将$r('app.string.TextSpan_textContent_span')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span"
  4. Span($r('app.string.TextSpan_textContent_span'))
  5. }
  6. .padding(10)
  7. .borderWidth(1)
  ```

  [TextSpan.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextSpan.ets#L28-L36)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/h1FMdyhgTj6EbLJ73ik0iQ/zh-cn_image_0000002583437837.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=10C64152F32CA82FA886BB6B7E642D93032593F2EF597D2C66CDB6FE03C1C1AC)
* 设置文本装饰线及颜色。

  通过[decoration](../harmonyos-references/ts-basic-components-span.md#decoration)设置文本装饰线及颜色。

  ```
  1. Text() {
  2. // 请将$r('app.string.TextSpan_textContent_span_one')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span1，"
  3. Span($r('app.string.TextSpan_textContent_span_one'))
  4. .fontSize(16)
  5. .fontColor(Color.Grey)
  6. .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
  7. // 请将$r('app.string.TextSpan_textContent_span_two')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span2"
  8. Span($r('app.string.TextSpan_textContent_span_two'))
  9. .fontColor(Color.Blue)
  10. .fontSize(16)
  11. .fontStyle(FontStyle.Italic)
  12. .decoration({ type: TextDecorationType.Underline, color: Color.Black })
  13. // 请将$r('app.string.TextSpan_textContent_span_three')替换为实际资源文件，在本示例中该资源文件的value值为"，我是Span3"
  14. Span($r('app.string.TextSpan_textContent_span_three'))
  15. .fontSize(16)
  16. .fontColor(Color.Grey)
  17. .decoration({ type: TextDecorationType.Overline, color: Color.Green })
  18. }
  19. .borderWidth(1)
  20. .padding(10)
  ```

  [TextSpan.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextSpan.ets#L41-L62)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/bxmUBhkbS3OesOtntsWIMA/zh-cn_image_0000002552957792.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=DBDC4F51946621432C0294C45FFF57AC0A3A6CBB9524E979F536D2F283D172B9)
* 通过[textCase](../harmonyos-references/ts-basic-components-span.md#textcase)设置文字一直保持大写或者小写状态。

  ```
  1. Text() {
  2. Span('I am Upper-span').fontSize(12)
  3. .textCase(TextCase.UpperCase)
  4. }
  5. .borderWidth(1)
  6. .padding(10)
  ```

  [TextSpan.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextSpan.ets#L67-L74)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/lt_rAauHTYam7ImpSlD57w/zh-cn_image_0000002583477793.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=75CF1CCCD29C44F92BA6B5F20CDE24264BCC87CCAA1C18C4963F9F206C754F13)
* 添加事件。

  由于Span组件无尺寸信息，仅支持添加点击事件[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)、悬浮事件[onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)。

  ```
  1. // xxx.ets
  2. import { hilog } from '@kit.PerformanceAnalysisKit';

  4. @Entry
  5. @Component
  6. export struct TextSpanOnHover {
  7. @State textStr1: string = '';
  8. @State textStr2: string = '';

  10. build() {
  11. NavDestination() {
  12. Row() {
  13. Column() {
  14. Text() {
  15. Span('I am Upper-span')
  16. .textCase(TextCase.UpperCase)
  17. .fontSize(30)
  18. .onClick(() => {
  19. hilog.info(0x0000, 'Sample_TextComponent', 'Span onClick is triggering');
  20. this.textStr1 = 'Span onClick is triggering';
  21. })
  22. .onHover(() => {
  23. hilog.info(0x0000, 'Sample_TextComponent', 'Span onHover is triggering');
  24. this.textStr2 = 'Span onHover is triggering';
  25. })
  26. }

  28. Text('onClick：' + this.textStr1)
  29. .fontSize(20)
  30. Text('onHover：' + this.textStr2)
  31. .fontSize(20)
  32. }.width('100%')
  33. }
  34. .height('100%')
  35. }
  36. // ···
  37. }
  38. }
  ```

  [TextSpanOnHover.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextSpanOnHover.ets#L15-L58)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/L6IqNXqsSS6pYudlOpu4hw/zh-cn_image_0000002552798144.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=24C73C526FB0CFA3BA6B2A09E69B4F84EA2554A1C1EDB08508996DCAFBDB4382)

## 创建自定义文本样式

Text组件支持创建自定义文本样式，以下为修改文本样式的主要属性。

| 属性名称 | 功能描述 |
| --- | --- |
| baselineOffset | 设置文本基线的偏移量。 |
| contentTransition | 设置数字翻牌效果。 |
| copyOption | 设置文本是否可复制粘贴。 |
| decoration | 设置文本装饰线样式，如类型、颜色及其粗细。 |
| enableAutoSpacing | 设置是否开启中文与西文的自动间距。 |
| enableDataDetector | 设置是否进行文本特殊实体识别。 |
| font | 设置文本字体相关属性。 |
| fontColor | 设置文本字体颜色。 |
| fontFamily | 设置文本字体族。 |
| fontFeature | 设置文字特性效果，比如数字等宽的特性。 |
| fontSize | 设置文本字体大小。 |
| fontStyle | 设置文本字体风格。 |
| fontWeight | 设置文本字体粗细。 |
| halfLeading | 设置文本是否将行间距平分至行的顶部与底部。 |
| heightAdaptivePolicy | 设置文本自适应布局调整字号的方式。 |
| letterSpacing | 设置文本字符间距。 |
| lineHeight | 设置文本行高。 |
| lineSpacing | 设置文本的行间距。 |
| marqueeOptions | 设置跑马灯配置项，如开关、步长、循环次数、方向等。 |
| maxFontSize | 设置自适应字体最大尺寸。 |
| maxLines | 设置文本最大显示行数。 |
| minFontSize | 设置自适应字体最小尺寸。 |
| optimizeTrailingSpace | 控制每行末尾空格的优化。 |
| privacySensitive | 设置是否支持卡片敏感隐私信息。 |
| shaderStyle | 设置文本渐变色样式。 |
| textCase | 设置文本大小写转换。 |
| textAlign | 设置文本段落在水平方向的对齐方式。 |
| textIndent | 设置首行文本缩进。 |
| textOverflow | 控制文本超长处理方式。 |
| textSelectable | 设置文本是否可选择。 |
| textVerticalAlign | 设置文本段落在垂直方向的对齐方式。 |
| wordBreak | 设置断行规则。 |

下面对常用的接口进行举例说明。

* 通过[textAlign](../harmonyos-references/ts-basic-components-text.md#textalign)属性设置文本对齐样式。

  ```
  1. // 请将$r('app.string.TextAlign_Start')替换为实际资源文件，在本示例中该资源文件的value值为"左对齐"
  2. Text($r('app.string.TextAlign_Start'))
  3. .width(300)
  4. .textAlign(TextAlign.Start)
  5. .border({ width: 1 })
  6. .padding(10)
  7. // 请将$r('app.string.TextAlign_Center')替换为实际资源文件，在本示例中该资源文件的value值为"中间对齐"
  8. Text($r('app.string.TextAlign_Center'))
  9. .width(300)
  10. .textAlign(TextAlign.Center)
  11. .border({ width: 1 })
  12. .padding(10)
  13. // 请将$r('app.string.TextAlign_End')替换为实际资源文件，在本示例中该资源文件的value值为"右对齐"
  14. Text($r('app.string.TextAlign_End'))
  15. .width(300)
  16. .textAlign(TextAlign.End)
  17. .border({ width: 1 })
  18. .padding(10)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L30-L49)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/eTUzFI_xTRmEHXmoVIg7rg/zh-cn_image_0000002583437839.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=062DA603EF6979ADD398F57B40DC47BF7CC525C55DC057EDFBFE3AEB48FFEAB2)
* 通过[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)属性控制文本超长处理，textOverflow需配合[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)一起使用（默认情况下文本自动折行）。从API version 18开始，文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。

  ```
  1. Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +
  2. 'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +
  3. 'of textOverflow to None text content.')
  4. .width(250)
  5. .textOverflow({ overflow: TextOverflow.None })
  6. .maxLines(1)
  7. .fontSize(12)
  8. .border({ width: 1 })
  9. .padding(10)
  10. // 'app.string.CustomTextStyle_textContent_epsis'资源文件中的value值为
  11. // '我是超长文本，超出的部分显示省略号 I am an extra long text, with ellipses displayed for any excess。'
  12. Text($r('app.string.CustomTextStyle_textContent_epsis'))
  13. .width(250)
  14. .textOverflow({ overflow: TextOverflow.Ellipsis })
  15. .maxLines(1)
  16. .fontSize(12)
  17. .border({ width: 1 })
  18. .padding(10)
  19. // 'app.string.CustomTextStyle_textContent_marq'资源文件中的value值为
  20. // '当文本溢出其尺寸时，文本将滚动显示
  21. // When the text overflows its dimensions,the text will scroll for displaying.'
  22. Text($r('app.string.CustomTextStyle_textContent_marq'))
  23. .width(250)
  24. .textOverflow({ overflow: TextOverflow.MARQUEE })
  25. .maxLines(1)
  26. .fontSize(12)
  27. .border({ width: 1 })
  28. .padding(10)
  29. // 'app.string.CustomTextStyle_textContent_marq_def'资源文件中的value值为
  30. // '当文本溢出其尺寸时，文本将滚动显示，支持设置跑马灯配置项
  31. // When the text overflows its dimensions, the text will scroll for displaying.'
  32. Text($r('app.string.CustomTextStyle_textContent_marq_def'))
  33. .width(250)
  34. .textOverflow({ overflow: TextOverflow.MARQUEE })
  35. .maxLines(1)
  36. .fontSize(12)
  37. .border({ width: 1 })
  38. .padding(10)
  39. .marqueeOptions({
  40. start: true,
  41. fromStart: true,
  42. step: 6,
  43. loop: -1,
  44. delay: 0,
  45. fadeout: false,
  46. marqueeStartPolicy: MarqueeStartPolicy.DEFAULT
  47. })
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L62-L110)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/V-eFrC2LTuC2MRs1D_Z-qA/zh-cn_image_0000002552957794.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=DE963C0C262AF732D92DCBD3F891417DAEDA9D5F5A75D7D278285C4F2F4350FA)
* 通过[lineHeight](../harmonyos-references/ts-basic-components-text.md#lineheight)属性设置文本行高。

  ```
  1. Text('This is the text with the line height set. This is the text with the line height set.')
  2. .width(300).fontSize(12).border({ width: 1 }).padding(10)
  3. Text('This is the text with the line height set. This is the text with the line height set.')
  4. .width(300)
  5. .fontSize(12)
  6. .border({ width: 1 })
  7. .padding(10)
  8. .lineHeight(20)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L117-L126)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/NgZeInL-S-iqOa3ZKE0xTg/zh-cn_image_0000002583477795.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=B7FDC7780A752866F5AEF7EC44565D300F393C004E3DE10B40176FC7C04260C6)
* 通过[decoration](../harmonyos-references/ts-basic-components-text.md#decoration)属性设置文本装饰线样式、颜色及其粗细。

  ```
  1. Text('This is the text')
  2. .decoration({
  3. type: TextDecorationType.LineThrough,
  4. color: Color.Red
  5. })
  6. .borderWidth(1).padding(15).margin(5)
  7. Text('This is the text')
  8. .decoration({
  9. type: TextDecorationType.Overline,
  10. color: Color.Red
  11. })
  12. .borderWidth(1).padding(15).margin(5)
  13. Text('This is the text')
  14. .decoration({
  15. type: TextDecorationType.Underline,
  16. color: Color.Red
  17. })
  18. .borderWidth(1).padding(15).margin(5)
  19. Text('This is the text')
  20. .decoration({
  21. type: TextDecorationType.Underline,
  22. color: Color.Blue,
  23. style: TextDecorationStyle.DASHED
  24. })
  25. .borderWidth(1).padding(15).margin(5)
  26. Text('This is the text')
  27. .decoration({
  28. type: TextDecorationType.Underline,
  29. color: Color.Blue,
  30. style: TextDecorationStyle.DOTTED
  31. })
  32. .borderWidth(1).padding(15).margin(5)
  33. Text('This is the text')
  34. .decoration({
  35. type: TextDecorationType.Underline,
  36. color: Color.Blue,
  37. style: TextDecorationStyle.DOUBLE
  38. })
  39. .borderWidth(1).padding(15).margin(5)
  40. Text('This is the text')
  41. .decoration({
  42. type: TextDecorationType.Underline,
  43. color: Color.Blue,
  44. style: TextDecorationStyle.WAVY,
  45. thicknessScale: 4
  46. })
  47. .borderWidth(1).padding(15).margin(5)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L134-L182)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/-jgWOS5iRQmY9NizyoFxQQ/zh-cn_image_0000002552798146.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=254070A68ABA5E87B760FA3E90940449776B30D13331C890CB7B1637E420869C)
* 通过[baselineOffset](../harmonyos-references/ts-basic-components-text.md#baselineoffset)属性设置文本基线的偏移量。

  ```
  1. Text('This is the text content with baselineOffset 0.')
  2. .baselineOffset(0)
  3. .fontSize(12)
  4. .border({ width: 1 })
  5. .padding(10)
  6. .width('100%')
  7. .margin(5)
  8. Text('This is the text content with baselineOffset 30.')
  9. .baselineOffset(30)
  10. .fontSize(12)
  11. .border({ width: 1 })
  12. .padding(10)
  13. .width('100%')
  14. .margin(5)
  15. Text('This is the text content with baselineOffset -20.')
  16. .baselineOffset(-20)
  17. .fontSize(12)
  18. .border({ width: 1 })
  19. .padding(10)
  20. .width('100%')
  21. .margin(5)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L190-L212)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/J93K16ZHQ569mJqoNnjsjw/zh-cn_image_0000002583437841.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=EF7F139ADF63069A81343CD83BB818ED628D0A73B9DBD1097F2B780CCBA5FF75)
* 通过[letterSpacing](../harmonyos-references/ts-basic-components-text.md#letterspacing)属性设置文本字符间距。

  ```
  1. Text('This is the text content with letterSpacing 0.')
  2. .letterSpacing(0)
  3. .fontSize(12)
  4. .border({ width: 1 })
  5. .padding(10)
  6. .width('100%')
  7. .margin(5)
  8. Text('This is the text content with letterSpacing 3.')
  9. .letterSpacing(3)
  10. .fontSize(12)
  11. .border({ width: 1 })
  12. .padding(10)
  13. .width('100%')
  14. .margin(5)
  15. Text('This is the text content with letterSpacing -1.')
  16. .letterSpacing(-1)
  17. .fontSize(12)
  18. .border({ width: 1 })
  19. .padding(10)
  20. .width('100%')
  21. .margin(5)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L219-L241)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/jjs4tpIvR3qMeDphRhe3gQ/zh-cn_image_0000002552957796.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=0C94F2AC0A93FFC65C417D1C16CEA6515A3DC87C4F44162F96D23C4BEADE9BAC)
* 通过[minFontSize](../harmonyos-references/ts-basic-components-text.md#minfontsize)与[maxFontSize](../harmonyos-references/ts-basic-components-text.md#maxfontsize)自适应字体大小。

  minFontSize用于设置文本的最小显示字号，maxFontSize用于设置文本的最大显示字号。这两个属性必须同时设置才能生效，并且需要与[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)属性或布局大小限制配合使用，单独设置任一属性将不会产生效果。

  ```
  1. /* 请将$r('app.string.CustomTextStyle_textContent_one_style')替换为实际资源文件，
  2. * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为5，宽度为250，maxLines为1"
  3. */
  4. Text($r('app.string.CustomTextStyle_textContent_one_style'))
  5. .width(250)
  6. .maxLines(1)
  7. .maxFontSize(30)
  8. .minFontSize(5)
  9. .border({ width: 1 })
  10. .padding(10)
  11. .margin(5)
  12. /* 请将$r('app.string.CustomTextStyle_textContent_two_style')替换为实际资源文件，
  13. * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为5，宽度为250，maxLines为2"
  14. */
  15. Text($r('app.string.CustomTextStyle_textContent_two_style'))
  16. .width(250)
  17. .maxLines(2)
  18. .maxFontSize(30)
  19. .minFontSize(5)
  20. .border({ width: 1 })
  21. .padding(10)
  22. .margin(5)
  23. /* 请将$r('app.string.CustomTextStyle_textContent_no_max')替换为实际资源文件，
  24. * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为15，宽度为250,高度为50"
  25. */
  26. Text($r('app.string.CustomTextStyle_textContent_no_max'))
  27. .width(250)
  28. .height(50)
  29. .maxFontSize(30)
  30. .minFontSize(15)
  31. .border({ width: 1 })
  32. .padding(10)
  33. .margin(5)
  34. /* 请将$r('app.string.CustomTextStyle_textContent_high')替换为实际资源文件，
  35. * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为15，宽度为250,高度为100"
  36. */
  37. Text($r('app.string.CustomTextStyle_textContent_high'))
  38. .width(250)
  39. .height(100)
  40. .maxFontSize(30)
  41. .minFontSize(15)
  42. .border({ width: 1 })
  43. .padding(10)
  44. .margin(5)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L249-L290)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/j739LVrIRMetCIkY15zdWg/zh-cn_image_0000002583477797.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=3DD8C231CD7B43345790F922DA122E2151C74C6E2F499B3C284C52F9C70ED155)
* 通过[textCase](../harmonyos-references/ts-basic-components-text.md#textcase)属性设置文本大小写。

  ```
  1. Text('This is the text content with textCase set to Normal.')
  2. .textCase(TextCase.Normal)
  3. .padding(10)
  4. .border({ width: 1 })
  5. .padding(10)
  6. .margin(5)

  8. // 文本全小写展示
  9. Text('This is the text content with textCase set to LowerCase.')
  10. .textCase(TextCase.LowerCase)
  11. .border({ width: 1 })
  12. .padding(10)
  13. .margin(5)

  15. // 文本全大写展示
  16. Text('This is the text content with textCase set to UpperCase.')
  17. .textCase(TextCase.UpperCase)
  18. .border({ width: 1 })
  19. .padding(10)
  20. .margin(5)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L297-L318)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/MFhbZ3PRQB-eZW52_a0XUA/zh-cn_image_0000002552798148.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=31EE9787F360C2520566EE2A4C05E2C933E321A7924672C4B65AD9EF6A41D5B7)
* 通过[copyOption](../harmonyos-references/ts-basic-components-text.md#copyoption9)属性设置文本是否可复制粘贴。

  ```
  1. // 请将$r('app.string.CustomTextStyle_textContent_incopy')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段可复制文本。"
  2. Text($r('app.string.CustomTextStyle_textContent_incopy'))
  3. .fontSize(30)
  4. .copyOption(CopyOptions.InApp)
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L329-L334)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/T6UAWpD2QFyyGnRBmbolcw/zh-cn_image_0000002583437843.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=553FC395428E1D97116B6CA19685CFA2DF8057AE1A5B38BAE7A131E76DE032D1)
* 通过[fontFamily](../harmonyos-references/ts-basic-components-text.md#fontfamily)属性设置字体列表。应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](../harmonyos-references/js-apis-font.md)。

  ```
  1. Text('This is the text content with fontFamily')
  2. .fontSize(30)
  3. .fontFamily('HarmonyOS Sans')
  ```

  [CustomTextStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/CustomTextStyle.ets#L319-L323)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/DTTNlh9eQ5uwjIBPuTUmvw/zh-cn_image_0000002552957798.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=46C83B7CDA1624B6AE5F10ABAEB9073BA740D7B6D0389FD70DCCFB745016F7FC)
* 从API version 20开始，支持通过[contentTransition](../harmonyos-references/ts-basic-components-text.md#contenttransition20)属性设置数字翻牌效果。

  ```
  1. @Entry
  2. @Component
  3. export struct ContentTransition {
  4. private static readonly INITIAL_SCORE: number = 98;
  5. @State number: number = ContentTransition.INITIAL_SCORE;
  6. @State numberTransition: NumericTextTransition =
  7. new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });
  8. build() {
  9. NavDestination() {
  10. Column() {
  11. Text(this.number + '')
  12. .borderWidth(1)
  13. .fontSize(40)
  14. .contentTransition(this.numberTransition)
  15. Button('chang number')
  16. .onClick(() => {
  17. this.number++
  18. })
  19. .margin(10)
  20. }
  21. .width('100%')
  22. .height('100%')
  23. }
  24. // ···
  25. }
  26. }
  ```

  [ContentTransition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/ContentTransition.ets#L15-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/T_w3N4GoQUCdhyJF5KRFpw/zh-cn_image_0000002583477799.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=968B024FC968036E57D3A6C8E3923DE130D6B11C0D1EEFC8915839E784A9EC01)
* 从API version 20开始，支持通过[optimizeTrailingSpace](../harmonyos-references/ts-basic-components-text.md#optimizetrailingspace20)设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。

  ```
  1. Column() {
  2. // 启用优化行尾空格功能
  3. Text('Trimmed space enabled     ')
  4. .fontSize(30)
  5. .fontWeight(FontWeight.Bold)
  6. .margin({ top: 20 })
  7. .optimizeTrailingSpace(true)
  8. .textAlign(TextAlign.Center)
  9. // 不启用优化行尾空格功能
  10. Text('Trimmed space disabled     ')
  11. .fontSize(30)
  12. .fontWeight(FontWeight.Bold)
  13. .margin({ top: 20 })
  14. .optimizeTrailingSpace(false)
  15. .textAlign(TextAlign.Center)
  16. }
  ```

  [TextLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextLayout.ets#L65-L83)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/0TjMp4Q5Qla45vz8-dJ3dw/zh-cn_image_0000002552798150.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=1F32FE1648CAB936FEF582E327F66F7DBEF32C1741F2F2F3FF0C351D78B9575F)
* 从API version 20开始，支持通过[lineSpacing](../harmonyos-references/ts-basic-components-text.md#linespacing20)设置文本的行间距。当不配置[LineSpacingOptions](../harmonyos-references/ts-text-common.md#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距，当onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外的行间距。

  ```
  1. import { LengthMetrics } from '@kit.ArkUI';

  3. @Extend(Text)
  4. function style() {
  5. .width(250)
  6. .height(100)
  7. .maxFontSize(30)
  8. .minFontSize(15)
  9. .border({ width: 1 })
  10. }

  12. @Entry
  13. @Component
  14. export struct LineSpacing {
  15. build() {
  16. NavDestination() {
  17. Column() {
  18. Text('The line spacing of this context is set to 20_px, and the spacing is effective only between the lines.')
  19. .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
  20. .style()
  21. }
  22. }
  23. // ···
  24. }
  25. }
  ```

  [LineSpacing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/LineSpacing.ets#L16-L46)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/T7FKbXpjSau9Le8zAPsfqg/zh-cn_image_0000002583437845.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=C130CD98B5DF5A8CF0C5C9D972D47B24AA3E23ECACC40D97B5CE2A01A30A1A36)
* 从API version 20开始，支持通过[enableAutoSpacing](../harmonyos-references/ts-basic-components-text.md#enableautospacing20)设置是否开启中文与西文的自动间距。

  ```
  1. @Entry
  2. @Component
  3. export struct EnableAutoSpacing {
  4. @State enableSpacing: boolean = false;

  6. build() {
  7. NavDestination() {
  8. Column() {
  9. Row({ space: 20 }) {
  10. // 请将$r('app.string.Enable_automatic_spacing')替换为实际资源文件，在本示例中该资源文件的value值为"开启自动间距"
  11. Button($r('app.string.Enable_automatic_spacing'))
  12. .onClick(() => this.enableSpacing = true)
  13. .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')
  14. .fontColor(this.enableSpacing ? Color.White : Color.Black)
  15. // 请将$r('app.string.off_automatic_spacing')替换为实际资源文件，在本示例中该资源文件的value值为"关闭自动间距"
  16. Button($r('app.string.off_automatic_spacing'))
  17. .onClick(() => this.enableSpacing = false)
  18. .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')
  19. .fontColor(!this.enableSpacing ? Color.White : Color.Black)
  20. }
  21. .width('100%')
  22. .justifyContent(FlexAlign.Center)
  23. .margin({ top: 30, bottom: 20 })
  24. // 请将$r('app.string.Automatic_spacing_has_been_enabled')替换为实际资源文件，在本示例中该资源文件的value值为"当前状态:已开启自动间距"
  25. // 请将$r('app.string.Automatic_spacing_has_been_turned_off')替换为实际资源文件，在本示例中该资源文件的value值为"当前状态:已关闭自动间距"
  26. Text(this.enableSpacing ? $r('app.string.Automatic_spacing_has_been_enabled') : $r('app.string.Automatic_spacing_has_been_turned_off'))
  27. .fontSize(16)
  28. .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')
  29. .margin({ bottom: 20 })

  31. // 设置是否应用中西文自动间距
  32. /* 请将$r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing')替换为实际资源文件，
  33. * 在本示例中该资源文件的value值为"中西文Auto Spacing自动间距"
  34. */
  35. Text($r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing'))
  36. .fontSize(24)
  37. .padding(15)
  38. .backgroundColor('#F5F5F5')
  39. .width('90%')
  40. .enableAutoSpacing(this.enableSpacing)
  41. }
  42. .width('100%')
  43. .height('100%')
  44. .padding(20)
  45. }
  46. // ...
  47. }
  48. }
  ```

  [EnableAutoSpacing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/EnableAutoSpacing.ets#L16-L68)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/rjyecvPSQCGlD-5rKvXcpg/zh-cn_image_0000002552957800.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=45DDBE4171150D79D6718B885210248044036835CB9C14A9A0BC164FD4FEA784)
* 从API version 20开始，支持通过[shaderStyle](../harmonyos-references/ts-basic-components-text.md#shaderstyle20)设置渐变色。

  ```
  1. @Entry
  2. @Component
  3. export struct ShaderStyle {
  4. @State message: string = 'Hello World';
  5. @State linearGradientOptions: LinearGradientOptions =
  6. {
  7. direction: GradientDirection.LeftTop,
  8. colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
  9. repeating: true,
  10. };

  12. build() {
  13. NavDestination() {
  14. Column({ space: 5 }) {
  15. // 请将$r('app.string.direction_LeftTop')替换为实际资源文件，在本示例中该资源文件的value值为"direction为LeftTop的线性渐变"
  16. Text($r('app.string.direction_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)
  17. .margin({ top: 40, left: 40 })
  18. Text(this.message)
  19. .fontSize(50)
  20. .width('80%')
  21. .height(50)
  22. .shaderStyle(this.linearGradientOptions)
  23. }
  24. .height('100%')
  25. .width('100%')
  26. }
  27. // ...
  28. }
  29. }
  ```

  [ShaderStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/ShaderStyle.ets#L16-L51)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/qMhTMj7MRSOst11uztKqKw/zh-cn_image_0000002583477801.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=F35E4F95BB49FD95172FE3857AF6062A68C5B82CEEF15D7C9A80C8A198EA371D)

## 添加事件

Text组件可以添加通用事件，可以绑定[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)、[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)等事件来响应操作。

```
1. // xxx.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. @Entry
4. @Component
5. export struct GeneralEvents {
6. @State textStr1: string = '';
7. @State textStr2: string = '';

9. build() {
10. NavDestination() {
11. Row() {
12. Column() {
13. Text('This is a text component.')
14. .fontSize(30)
15. .onClick(() => {
16. hilog.info(0x0000, 'Sample_TextComponent', 'Text onClick is triggering');
17. this.textStr1 = 'Text onClick is triggering';
18. })
19. .onTouch(() => {
20. hilog.info(0x0000, 'Sample_TextComponent', 'Text onTouch is triggering');
21. this.textStr2 = 'Text onTouch is triggering';
22. })
23. Text('onClick：' + this.textStr1)
24. .fontSize(20)
25. Text('onTouch：' + this.textStr2)
26. .fontSize(20)
27. }.width('100%')
28. }
29. .height('100%')
30. }
31. // ···
32. }
33. }
```

[GeneralEvents.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/GeneralEvents.ets#L16-L54)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Uq37VIvDSC-6lpIbXEUBbA/zh-cn_image_0000002552798152.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=FF4147CFDFB4CDC01103973F01155D71F2D1C34E273B3155704949CF0EA01779)

## 设置垂直居中

从API version 20开始，Text组件支持通过[textVerticalAlign](../harmonyos-references/ts-basic-components-text.md#textverticalalign20)属性实现文本段落在垂直方向的对齐。

* 以下示例展示了如何通过textVerticalAlign属性设置文本垂直居中对齐效果。

  ```
  1. // 请将$r('app.media.startIcon')替换为实际资源文件
  2. Text() {
  3. Span('Hello')
  4. .fontSize(50)
  5. ImageSpan($r('app.media.startIcon'))
  6. .width(30).height(30)
  7. .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)
  8. Span('World')
  9. }
  10. .textVerticalAlign(TextVerticalAlign.CENTER)
  ```

  [TextLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextLayout.ets#L85-L97)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/WbFW4fZXTPK-UOXuJYxf1w/zh-cn_image_0000002583437847.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=70ACFECCBEE5626A04E033DD8AC16718097EAAC951AB0B77DBB34EA7D62C61CA)

## 设置选中菜单

### 弹出选中菜单

* 设置Text被选中时，会弹出包含复制、翻译、搜索的菜单。

  Text组件需要设置[copyOption](../harmonyos-references/ts-basic-components-text.md#copyoption9)属性才可以被选中。

  ```
  1. // 请将$r('app.string.selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
  2. Text($r('app.string.selected_menu'))
  3. .fontSize(30)
  4. .copyOption(CopyOptions.InApp)
  ```

  [TextLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextLayout.ets#L101-L106)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/In8xW-OpTgSmZZpbG8OujQ/zh-cn_image_0000002552957802.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=74F275E3775C33A6434245F2F522073209633A5D78D9B691CA39EC096DED7A6A)
* Text组件通过设置[bindSelectionMenu](../harmonyos-references/ts-basic-components-text.md#bindselectionmenu11)属性绑定自定义选择菜单。

  ```
  1. controller: TextController = new TextController();
  2. options: TextOptions = { controller: this.controller };
  ```

  [SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/SelectMenu.ets#L23-L26)

  ```
  1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
  2. Text($r('app.string.show_selected_menu'), this.options)
  3. .fontSize(30)
  4. .copyOption(CopyOptions.InApp)
  5. .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT_CLICK, {
  6. onAppear: () => {
  7. // 请将$r('app.string.SelectMenu_Text_Ejected')替换为实际资源文件，在本示例中该资源文件的value值为"自定义选择菜单弹出时触发该回调"
  8. hilog.info(0x0000, 'Sample_TextComponent',
  9. this.getUIContext()
  10. .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Ejected').id));
  11. },
  12. onDisappear: () => {
  13. // 'SelectMenu_Text_Close'资源文件中的value值为'自定义选择菜单关闭时触发该回调'
  14. hilog.info(0x0000, 'Sample_TextComponent',
  15. this.getUIContext()
  16. .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Close').id));
  17. }
  18. })
  ```

  [SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/SelectMenu.ets#L102-L119)

  ```
  1. // 定义菜单项
  2. @Builder
  3. RightClickTextCustomMenu() {
  4. Column() {
  5. Menu() {
  6. MenuItemGroup() {
  7. // 请将$r('app.media.app_icon')替换为实际资源文件
  8. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu One', labelInfo: '' })
  9. .onClick(() => {
  10. // 使用closeSelectionMenu接口关闭菜单
  11. this.controller.closeSelectionMenu();
  12. })
  13. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Two', labelInfo: '' })
  14. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Three', labelInfo: '' })
  15. }
  16. }.backgroundColor('#F0F0F0')
  17. }
  18. }
  ```

  [SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/SelectMenu.ets#L27-L46)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/XdbfxwNXQM688zI5grIyFg/zh-cn_image_0000002583477803.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=E1B5759CEF358C844473B2F4C36CC4E62CC2DCE2B7DB361D79D485548A9070D6)
* Text组件通过设置[editMenuOptions](../harmonyos-references/ts-basic-components-text.md#editmenuoptions12)属性扩展自定义选择菜单，可以设置扩展项的文本内容、图标以及回调方法。

  ```
  1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
  2. Text($r('app.string.show_selected_menu'))
  3. .fontSize(20)
  4. .copyOption(CopyOptions.LocalDevice)
  5. .editMenuOptions({
  6. onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick
  7. })
  ```

  [SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/SelectMenu.ets#L123-L131)

  ```
  1. // 定义onCreateMenu，onMenuItemClick
  2. // 请将$r('app.media.app_icon')替换为实际资源文件
  3. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
  4. let item1: TextMenuItem = {
  5. content: 'customMenu1',
  6. icon: $r('app.media.app_icon'),
  7. id: TextMenuItemId.of('customMenu1'),
  8. };
  9. let item2: TextMenuItem = {
  10. content: 'customMenu2',
  11. id: TextMenuItemId.of('customMenu2'),
  12. icon: $r('app.media.app_icon'),
  13. };
  14. menuItems.push(item1);
  15. menuItems.unshift(item2);
  16. return menuItems;
  17. }
  18. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
  19. if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {
  20. // 请将$r('app.string.SelectMenu_Text_customMenu')替换为实际资源文件，在本示例中该资源文件的value值为"拦截 id: customMenu2 start:"
  21. hilog.info(0x0000, 'Sample_TextComponent',
  22. this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_customMenu')
  23. .id) + textRange.start + '; end:' +
  24. textRange.end);
  25. return true;
  26. }
  27. if (menuItem.id.equals(TextMenuItemId.COPY)) {
  28. // 请将$r('app.string.SelectMenu_Text_copy')替换为实际资源文件，在本示例中该资源文件的value值为"拦截 COPY start:"
  29. hilog.info(0x0000, 'Sample_TextComponent',
  30. this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_copy').id) +
  31. textRange.start + '; end:' + textRange.end);
  32. return true;
  33. }
  34. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
  35. // 请将$r('app.string.SelectMenu_Text_SelectionAll')替换为实际资源文件，在本示例中该资源文件的value值为"不拦截 SELECT_ALL start:"
  36. hilog.info(0x0000, 'Sample_TextComponent',
  37. this.getUIContext()
  38. .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_SelectionAll').id) +
  39. textRange.start + '; end:' +
  40. textRange.end);
  41. return false;
  42. }
  43. return false;
  44. };
  ```

  [SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/SelectMenu.ets#L47-L88)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/f_Qh0SyBSZSGfOtblNUyhg/zh-cn_image_0000002552798154.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=99FD556457311D77F924147DBA755893B0487014CB9C590DA4B1401ECC51C304)

### 关闭选中菜单

使用Text组件时，若需要实现点击空白处关闭选中的场景，分为以下两种情况：

* 在Text组件区域内点击空白处，会正常关闭选中态和菜单；
* 在Text组件区域外点击空白处，前提是Text组件设置[selection](../harmonyos-references/ts-basic-components-text.md#selection11)属性，具体示例如下：

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. export struct SelectionChange {
  5. @State text: string =
  6. 'This is set selection to Selection text content This is set selection to Selection text content.';
  7. @State start: number = 0;
  8. @State end: number = 20;

  10. build() {
  11. NavDestination() {
  12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
  13. Text(this.text)
  14. .fontSize(12)
  15. .border({ width: 1 })
  16. .lineHeight(20)
  17. .margin(30)
  18. .copyOption(CopyOptions.InApp)
  19. .selection(this.start, this.end)
  20. .onTextSelectionChange((selectionStart, selectionEnd) => {
  21. // 更新选中态位置
  22. this.start = selectionStart;
  23. this.end = selectionEnd;
  24. })
  25. }
  26. .height(600)
  27. .width(335)
  28. .borderWidth(1)
  29. .onClick(() => {
  30. // 监听父组件的点击事件，将选中首尾位置均设置为-1，即可清除选中
  31. this.start = -1;
  32. this.end = -1;
  33. })
  34. }
  35. // ···
  36. }
  37. }
  ```

  [SelectionChange.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/SelectionChange.ets#L15-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/LyyxTHF0R-a6GNW_fHN1fA/zh-cn_image_0000002583437849.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=4A95BA4794264195CAED81F83FFA016C1CD4BC5FAE16D76991500A7D3167713F)

### 屏蔽系统菜单回调和自定义扩展菜单

从API version 12开始，支持通过[editMenuOptions](../harmonyos-references/ts-basic-components-text.md#editmenuoptions12)屏蔽系统菜单回调和自定义扩展菜单项。

```
1. // xxx.ets
2. @Entry
3. @Component
4. export struct CustomAndBlockMenus {
5. private static readonly CREATE_MENU_ITEM_ID_1: string = 'create1';
6. private static readonly CREATE_MENU_ITEM_ID_2: string = 'create2';
7. private static readonly PREPARE_MENU_ITEM_ID: string = 'prepare1';
8. private controller: TextController = new TextController();
9. @State private text: string = 'Text editMenuOptions';
10. @State private endIndex: number = 0;
11. @State blockCallbackText: string = '';

13. // 创建菜单项辅助方法
14. private createMenuItem(id: string, content: string): TextMenuItem {
15. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
16. return {
17. content: content,
18. icon: $r('app.media.startIcon'),
19. id: TextMenuItemId.of(id)
20. };
21. }

23. // 查找菜单项索引
24. private findMenuItemIndex(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): number {
25. return menuItems.findIndex((item: TextMenuItem) => item.id.equals(menuItemId));
26. }

28. // 创建菜单回调
29. private onCreateMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
30. const createItem1: TextMenuItem = this.createMenuItem(
31. CustomAndBlockMenus.CREATE_MENU_ITEM_ID_1,
32. 'create1'
33. );

35. const createItem2: TextMenuItem = this.createMenuItem(
36. CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2,
37. 'create2'
38. );

40. // 添加自定义菜单项
41. menuItems.push(createItem1);
42. menuItems.unshift(createItem2);

44. // 移除不需要的系统菜单项
45. this.removeMenuItemById(menuItems, TextMenuItemId.AI_WRITER);
46. this.removeMenuItemById(menuItems, TextMenuItemId.TRANSLATE);

48. return menuItems;
49. }

51. // 移除指定菜单项
52. private removeMenuItemById(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): void {
53. const targetIndex: number = this.findMenuItemIndex(menuItems, menuItemId);
54. if (targetIndex !== -1) {
55. menuItems.splice(targetIndex, 1);
56. }
57. }

59. // 菜单项点击回调
60. private onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange): boolean => {
61. const menuItemId: TextMenuItemId = menuItem.id;

63. // 处理自定义菜单项，return false，点击自定义菜单项后菜单会关闭
64. if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2))) {
65. let msg = '拦截 id: create2 start:' + textRange.start + '; end:' + textRange.end;
66. this.blockCallbackText = msg;
67. return false;
68. }
69. // 处理自定义菜单项，return true，点击自定义菜单项后菜单不会关闭
70. if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.PREPARE_MENU_ITEM_ID))) {
71. let msg = '拦截 id: prepare1 start:' + textRange.start + '; end:+' + textRange.end;
72. this.blockCallbackText = msg;
73. return true;
74. }

76. // 处理系统菜单项，return true，拦截系统默认逻辑，此时点击复制菜单不会关闭
77. if (menuItemId.equals(TextMenuItemId.COPY)) {
78. let msg = '拦截 COPY start:' + textRange.start + '; end:' + textRange.end;
79. this.blockCallbackText = msg;
80. // 可以通过文本控制器关闭菜单，手柄也会消失，仅保持选中区域，点击可消失
81. this.controller.closeSelectionMenu();
82. return true;
83. }
84. // 处理系统菜单项，return false，不拦截系统默认逻辑，自定义逻辑亦会被执行
85. if (menuItemId.equals(TextMenuItemId.SELECT_ALL)) {
86. let msg = '不拦截 SELECT_ALL start:' + textRange.start + '; end:' + textRange.end;
87. this.blockCallbackText = msg;
88. return false;
89. }

91. return false;
92. }
93. // 准备菜单回调
94. private onPrepareMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
95. const prepareItem: TextMenuItem = this.createMenuItem(
96. CustomAndBlockMenus.PREPARE_MENU_ITEM_ID,
97. `prepare1_${this.endIndex}`
98. );

100. menuItems.unshift(prepareItem);
101. return menuItems;
102. }
103. // 编辑菜单选项
104. @State private editMenuOptions: EditMenuOptions = {
105. onCreateMenu: this.onCreateMenu,
106. onMenuItemClick: this.onMenuItemClick,
107. onPrepareMenu: this.onPrepareMenu
108. };
109. // 文本选择变化回调
110. private onTextSelectionChange = (selectionStart: number, selectionEnd: number): void => {
111. this.endIndex = selectionEnd;
112. }

114. build() {
115. NavDestination() {
116. Column() {
117. Text(this.text, { controller: this.controller })
118. .fontSize(20)
119. .copyOption(CopyOptions.LocalDevice)
120. .editMenuOptions(this.editMenuOptions)
121. .margin({ top: 100 })
122. .onTextSelectionChange(this.onTextSelectionChange)
123. Text(this.blockCallbackText).borderWidth(1)
124. }
125. .width('90%')
126. .margin('5%')
127. }
128. }
129. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/0og_4XH2Tni_zCzCmCvFSQ/zh-cn_image_0000002552957804.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=20E1C726992EEA219C2EA4F334D0B58F205D1095F0FA27EB1F1C88182E190576)

### 屏蔽系统服务类菜单

* 从API version 20开始，支持通过[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)屏蔽文本选择菜单内所有系统服务菜单项。

  ```
  1. import { TextMenuController } from '@kit.ArkUI';
  2. // xxx.ets
  3. @Entry
  4. @Component
  5. export struct ServiceMenuItems {
  6. aboutToAppear(): void {
  7. // 禁用所有系统服务菜单
  8. TextMenuController.disableSystemServiceMenuItems(true);
  9. }

  11. aboutToDisappear(): void {
  12. // 页面消失恢复系统服务菜单
  13. TextMenuController.disableSystemServiceMenuItems(false);
  14. }
  15. build() {
  16. NavDestination() {
  17. Row() {
  18. Column() {
  19. // 请将$r('app.string.Service_MenuItems_Text')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，长按弹出文本选择菜单。"
  20. Text($r('app.string.Service_MenuItems_Text'))
  21. .height(60)
  22. .fontStyle(FontStyle.Italic)
  23. .fontWeight(FontWeight.Bold)
  24. .textAlign(TextAlign.Center)
  25. .copyOption(CopyOptions.InApp)
  26. .editMenuOptions({
  27. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
  28. // menuItems不包含被屏蔽的系统菜单项
  29. return menuItems;
  30. },
  31. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
  32. return false;
  33. }
  34. })
  35. }.width('100%')
  36. }
  37. .height('100%')
  38. }
  39. // ...
  40. }
  41. }
  ```

  [ServiceMenuItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/ServiceMenuItems.ets#L15-L62)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ltsGohv3QOaUetwkslL4Cw/zh-cn_image_0000002583477805.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=44413D09A5790B60DC6681B3F6602943C2E32236B6E4C891075C8F7A005D67D8)
* 从API version 20开始，支持通过[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)屏蔽文本选择菜单内指定的系统服务菜单项。

  ```
  1. import { TextMenuController } from '@kit.ArkUI';

  3. // xxx.ets
  4. @Entry
  5. @Component
  6. export struct DisableMenuItems {
  7. aboutToAppear(): void {
  8. // 禁用搜索菜单
  9. TextMenuController.disableMenuItems([TextMenuItemId.SEARCH])
  10. }

  12. aboutToDisappear(): void {
  13. // 恢复系统服务菜单
  14. TextMenuController.disableMenuItems([])
  15. }

  17. build() {
  18. NavDestination() {
  19. Row() {
  20. Column() {
  21. // 请将$r('app.string.Service_MenuItems_Text')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，长按弹出文本选择菜单。"
  22. Text($r('app.string.Service_MenuItems_Text'))
  23. .height(60)
  24. .fontStyle(FontStyle.Italic)
  25. .fontWeight(FontWeight.Bold)
  26. .textAlign(TextAlign.Center)
  27. .copyOption(CopyOptions.InApp)
  28. .editMenuOptions({
  29. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
  30. // menuItems不包含搜索
  31. return menuItems;
  32. },
  33. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
  34. return false
  35. }
  36. })
  37. }.width('100%')
  38. }
  39. .height('100%')
  40. }
  41. // ...
  42. }
  43. }
  ```

  [DisableMenuItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/DisableMenuItems.ets#L15-L64)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/o80gVJicTL61kUknHTcLlw/zh-cn_image_0000002552798156.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=1D288C49D92056CC0AF4643E81B73A5F233B52879BF0B791B8A411305B5FB714)

### 默认菜单支持自定义刷新能力

从API version 20开始，当文本选择区域变化后显示菜单之前触发[onPrepareMenu](../harmonyos-references/ts-text-common.md#属性-1)回调，可在该回调中进行菜单数据设置。

```
1. // 请将$r('app.media.xxx')替换为实际资源文件
2. // xxx.ets
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. const DOMAIN = 0x0000;
5. @Entry
6. @Component

8. export struct PrepareMenu {
9. @State text: string = 'Text editMenuOptions';
10. @State endIndex: number = 0;
11. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
12. let item1: TextMenuItem = {
13. content: 'create1',
14. icon: $r('app.media.startIcon'),
15. id: TextMenuItemId.of('create1'),
16. };
17. let item2: TextMenuItem = {
18. content: 'create2',
19. id: TextMenuItemId.of('create2'),
20. icon: $r('app.media.startIcon'),
21. };
22. menuItems.push(item1);
23. menuItems.unshift(item2);
24. return menuItems;
25. }
26. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
27. if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
28. hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: create2 start:' + textRange.start + '; end:' + textRange.end);
29. return true;
30. }
31. if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
32. hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: prepare1 start:' + textRange.start + '; end:' + textRange.end);
33. return true;
34. }
35. if (menuItem.id.equals(TextMenuItemId.COPY)) {
36. hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept COPY start:' + textRange.start + '; end:' + textRange.end);
37. return true;
38. }
39. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
40. hilog.info(DOMAIN, 'testTag', '%{public}s', 'No interception SELECT_ALL start:' + textRange.start + '; end:' + textRange.end);
41. return false;
42. }
43. return false;
44. }
45. onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
46. let item1: TextMenuItem = {
47. content: 'prepare1_' + this.endIndex,
48. icon: $r('app.media.startIcon'),
49. id: TextMenuItemId.of('prepare1'),
50. };
51. menuItems.unshift(item1);
52. return menuItems;
53. }
54. @State editMenuOptions: EditMenuOptions = {
55. onCreateMenu: this.onCreateMenu,
56. onMenuItemClick: this.onMenuItemClick,
57. onPrepareMenu: this.onPrepareMenu
58. };

60. build() {
61. NavDestination() {
62. Column() {
63. Text(this.text)
64. .fontSize(20)
65. .copyOption(CopyOptions.LocalDevice)
66. .editMenuOptions(this.editMenuOptions)
67. .margin({ top: 100 })
68. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
69. this.endIndex = selectionEnd;
70. })
71. }
72. .width('90%')
73. .margin('5%')
74. }
75. // ...
76. }
77. }
```

[PrepareMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/PrepareMenu.ets#L15-L96)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/dUEkmTZdTxCHVWbARZDRKA/zh-cn_image_0000002583437851.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=E3DA0891D201C560593F34A90EE08124603DC7A091D57600027237730EC9AB3B)

## 设置AI菜单

Text组件通过[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)和[dataDetectorConfig](../harmonyos-references/ts-basic-components-text.md#datadetectorconfig11)属性实现AI菜单的显示。AI菜单的表现形式包括：单击AI实体（指可被识别的内容，包括地址、邮箱等）弹出菜单的实体识别选项，选中文本后，文本选择菜单与鼠标右键菜单中显示的实体识别选项。

说明

从API version 20开始，支持在文本选择菜单与鼠标右键菜单中显示实体识别选项。当[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)设置为true，且[copyOption](../harmonyos-references/ts-basic-components-text.md#copyoption9)设置为CopyOptions.LocalDevice时，该功能生效。菜单选项包括[TextMenuItemId](../harmonyos-references/ts-text-common.md#textmenuitemid12)中的url(打开链接)、email(新建邮件)、phoneNumber(呼叫)、address(导航至该位置)、dateTime(新建日程提醒)。

该功能生效时，需选中范围内，包括一个完整的AI实体，才能展示对应的选项。

* 如果需要单击AI实体弹出菜单的实体识别选项，可以配置[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)为true。
* 如果在单击的交互方式之外，还需要文本选择菜单与鼠标右键菜单中显示的实体识别选项，可以配置[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)为true，且[copyOption](../harmonyos-references/ts-basic-components-text.md#copyoption9)设置为CopyOptions.LocalDevice，具体示例如下所示：

  ```
  1. // 'app.string.AIMenu_Text_One'资源文件中的value值为'电话号码：(86) (755) ********  \n \n 链接：www.********.com
  2. // \n \n 邮箱：***@example.com\n \n 地址：XX省XX市XX区XXXX \n \n 时间：XX年XX月XX日XXXX'
  3. Text($r('app.string.AIMenu_Text_One'))
  4. .fontSize(16)
  5. .copyOption(CopyOptions.LocalDevice)
  6. .enableDataDetector(true)// 使能实体识别
  7. .dataDetectorConfig({
  8. // 配置识别样式
  9. // types可支持PHONE_NUMBER电话号码、URL链接、EMAIL邮箱、ADDRESS地址、DATE_TIME时间
  10. // types设置为null或者[]时，识别所有类型的实体
  11. types: [], onDetectResultUpdate: (result: string) => {
  12. }
  13. })
  ```

  [AIMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/AIMenu.ets#L25-L39)
* 如果需要调整识别出的样式，可以通过[dataDetectorConfig](../harmonyos-references/ts-basic-components-text.md#datadetectorconfig11)实现，具体可以参考[TextDataDetectorConfig](../harmonyos-references/ts-text-common.md#textdatadetectorconfig11对象说明)配置项。
* 如果需要调整菜单的位置，可以通过[editMenuOptions](../harmonyos-references/ts-basic-components-text.md#editmenuoptions12)实现，具体可以参考示例[文本扩展自定义菜单](../harmonyos-references/ts-basic-components-text.md#示例12文本扩展自定义菜单)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/5YUX6Di6SYSUslx1bq8KIA/zh-cn_image_0000002552957806.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=F940D64272BE979C814BA8B5D4CDAB555E6656D1693C6C0C2F838A3864BC62F4)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/KErfgerNSfahb-9N2sONMA/zh-cn_image_0000002583477807.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=0C81406D4AB59A73A6A7880C3CA5D854DAE97CFE2D4B588EAE2BCFA8A60E5FE3)

## 实现热搜榜

该示例通过[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)、[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)、[textAlign](../harmonyos-references/ts-basic-components-text.md#textalign)、[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)属性展示了热搜榜的效果。

```
1. import { ComponentCard } from '../../common/Card';

3. @Entry
4. @Component
5. export struct TextHotSearch {
6. build() {
7. NavDestination() {
8. Column({ space: 12 }) {
9. // ...
10. Column() {
11. Row() {
12. Text('1').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
13. // 请将$r('app.string.TextHotSearch_textContent_one')替换为实际资源文件，在本示例中该资源文件的value值为"我是热搜词条1"
14. Text($r('app.string.TextHotSearch_textContent_one'))
15. .fontSize(12)
16. .fontColor(Color.Blue)
17. .maxLines(1)
18. .textOverflow({ overflow: TextOverflow.Ellipsis })
19. .fontWeight(300)
20. // 请将$r('app.string.TextHotSearch_textContent_two')替换为实际资源文件，在本示例中该资源文件的value值为"爆"
21. Text($r('app.string.TextHotSearch_textContent_two'))
22. .margin({ left: 6 })
23. .textAlign(TextAlign.Center)
24. .fontSize(10)
25. .fontColor(Color.White)
26. .fontWeight(600)
27. .backgroundColor(0x770100)
28. .borderRadius(5)
29. .width(15)
30. .height(14)
31. }.width('100%').margin(5)

33. Row() {
34. Text('2').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
35. /* 请将$r('app.string.TextHotSearch_textContent_three')替换为实际资源文件，
36. * 在本示例中该资源文件的value值为"我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2"
37. */
38. Text($r('app.string.TextHotSearch_textContent_three'))
39. .fontSize(12)
40. .fontColor(Color.Blue)
41. .fontWeight(300)
42. .constraintSize({ maxWidth: 200 })
43. .maxLines(1)
44. .textOverflow({ overflow: TextOverflow.Ellipsis })
45. // 请将$r('app.string.TextHotSearch_textContent_four')替换为实际资源文件，在本示例中该资源文件的value值为"热"
46. Text($r('app.string.TextHotSearch_textContent_four'))
47. .margin({ left: 6 })
48. .textAlign(TextAlign.Center)
49. .fontSize(10)
50. .fontColor(Color.White)
51. .fontWeight(600)
52. .backgroundColor(0xCC5500)
53. .borderRadius(5)
54. .width(15)
55. .height(14)
56. }.width('100%').margin(5)

58. Row() {
59. Text('3').fontSize(14).fontColor(Color.Orange).margin({ left: 10, right: 10 })
60. // 请将$r('app.string.TextHotSearch_textContent_five')替换为实际资源文件，在本示例中该资源文件的value值为"我是热搜词条3"
61. Text($r('app.string.TextHotSearch_textContent_five'))
62. .fontSize(12)
63. .fontColor(Color.Blue)
64. .fontWeight(300)
65. .maxLines(1)
66. .constraintSize({ maxWidth: 200 })
67. .textOverflow({ overflow: TextOverflow.Ellipsis })
68. // 请将$r('app.string.TextHotSearch_textContent_four')替换为实际资源文件，在本示例中该资源文件的value值为"热"
69. Text($r('app.string.TextHotSearch_textContent_four'))
70. .margin({ left: 6 })
71. .textAlign(TextAlign.Center)
72. .fontSize(10)
73. .fontColor(Color.White)
74. .fontWeight(600)
75. .backgroundColor(0xCC5500)
76. .borderRadius(5)
77. .width(15)
78. .height(14)
79. }.width('100%').margin(5)

81. Row() {
82. Text('4').fontSize(14).fontColor(Color.Grey).margin({ left: 10, right: 10 })
83. /* 请将$r('app.string.TextHotSearch_textContent_six')替换为实际资源文件，
84. * 在本示例中该资源文件的value值为"我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4"
85. */
86. Text($r('app.string.TextHotSearch_textContent_six'))
87. .fontSize(12)
88. .fontColor(Color.Blue)
89. .fontWeight(300)
90. .constraintSize({ maxWidth: 200 })
91. .maxLines(1)
92. .textOverflow({ overflow: TextOverflow.Ellipsis })
93. }.width('100%').margin(5)
94. }.width('100%')
95. // ...
96. }
97. .width('100%')
98. .height('100%')
99. .padding({ left: 12, right: 12 })
100. }
101. // ...
102. }
103. }
```

[TextHotSearch.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/text/TextHotSearch.ets#L16-L127)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/S8U5-3yATYqY7pnUlSjLTQ/zh-cn_image_0000002552798158.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=ADCB084FC9A8E65498694456203FF808D8EB09F4B25D73F17209949C045C3EA8)

## 示例代码

* [文字特效合集](https://gitcode.com/HarmonyOS_Samples/text-effects)
