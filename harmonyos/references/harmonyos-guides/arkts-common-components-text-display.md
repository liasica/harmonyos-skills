---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display
title: 文本显示 (Text/Span)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 文本显示 (Text/Span)
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:04+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b89379dd1cc5be0c4df188f3903b6668c33c9dda8b38000982a2e62875c3ef11
---

Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于展示行内文本。

具体用法请参考[Text](../harmonyos-references/ts-basic-components-text.md)和[Span](../harmonyos-references/ts-basic-components-span.md)组件的API文档。

常见问题请参考[文本显示（Text/Span）常见问题](arkts-text-faq.md#文本显示textspan常见问题)。

## 创建文本

Text可通过以下两种方式来创建：

* string字符串。

  ```typescript
  Text('我是一段文本')
  ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ivIqDmPFR5uHTfrE-47KHg/zh-cn_image_0000002788306646.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=9832775EC987E4FE7CD180C51A316B5BBECBED329524304E58081EC0E94042D9)

* 引用Resource资源。

  资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json，具体内容如下：

  ```json
  {
    "string": [
      {
        "name": "module_desc",
        "value": "模块描述"
      }
    ]
  }
  ```

  ```typescript
  // 请将$r('app.string.module_desc')替换为实际资源文件，在本示例中该资源文件的value值为"模块描述"
  Text($r('app.string.module_desc'))
    .baselineOffset(0)
    .fontSize(30)
    .border({ width: 1 })
    .padding(10)
    .width(300)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Mi7dtzerSU27uSMRR5LYzA/zh-cn_image_0000002817426009.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8D226D175F15A5563E28FE424891215075597B7FBBB9764F5604726CCCC760C)

## 添加子组件

[Span](../harmonyos-references/ts-basic-components-span.md)只能作为[Text](../harmonyos-references/ts-basic-components-text.md)和[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

* 创建Span。

  Span组件需嵌入在Text组件中才能显示，单独使用时不会显示任何内容。Text与Span同时配置文本内容时，Span内容将覆盖Text内容。

  ```typescript
  // 请将$r('app.string.TextSpan_textContent_text')替换为实际资源文件，在本示例中该资源文件的value值为"我是Text"
  Text($r('app.string.TextSpan_textContent_text')) {
    // 请将$r('app.string.TextSpan_textContent_span')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span"
    Span($r('app.string.TextSpan_textContent_span'))
  }
  .padding(10)
  .borderWidth(1)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/LMDp-cvBSDCh94x-ZxWXww/zh-cn_image_0000002788466590.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CBC065A9A22E3ACD0552291334BF8F2E981B4CB4BD9905D00A4348252B9F61C)
* 设置文本装饰线及颜色。

  通过[decoration](../harmonyos-references/ts-basic-components-span.md#decoration)设置文本装饰线及颜色。

  ```typescript
  Text() {
    // 请将$r('app.string.TextSpan_textContent_span_one')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span1，"
    Span($r('app.string.TextSpan_textContent_span_one'))
      .fontSize(16)
      .fontColor(Color.Grey)
      .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
    // 请将$r('app.string.TextSpan_textContent_span_two')替换为实际资源文件，在本示例中该资源文件的value值为"我是Span2"
    Span($r('app.string.TextSpan_textContent_span_two'))
      .fontColor(Color.Blue)
      .fontSize(16)
      .fontStyle(FontStyle.Italic)
      .decoration({ type: TextDecorationType.Underline, color: Color.Black })
    // 请将$r('app.string.TextSpan_textContent_span_three')替换为实际资源文件，在本示例中该资源文件的value值为"，我是Span3"
    Span($r('app.string.TextSpan_textContent_span_three'))
      .fontSize(16)
      .fontColor(Color.Grey)
      .decoration({ type: TextDecorationType.Overline, color: Color.Green })
  }
  .borderWidth(1)
  .padding(10)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/vAOXtdimTKCmmzfhgfV_ow/zh-cn_image_0000002817506077.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=E533516AFE164B159E425C6E8126B1611D16D78C0B2A4DCE3CA987E03D641213)
* 通过[textCase](../harmonyos-references/ts-basic-components-span.md#textcase)设置文字一直保持大写或者小写状态。

  ```typescript
  Text() {
    Span('I am Upper-span').fontSize(12)
      .textCase(TextCase.UpperCase)
  }
  .borderWidth(1)
  .padding(10)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/-i5C91PCRVqlzWXxq_XEyQ/zh-cn_image_0000002788306648.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=8893AF574640AF4600212D2DC4071BF7A9EB87A440A3EF43B812ABE6E98AB5BA)
* 添加事件。

  由于Span组件无尺寸信息，仅支持添加点击事件[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)、悬浮事件[onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)。

  ```typescript
  // xxx.ets
  import { hilog } from '@kit.PerformanceAnalysisKit';

  @Entry
  @Component
  struct TextSpanOnHover {
    @State textStr1: string = '';
    @State textStr2: string = '';

    build() {
      NavDestination() {
        Row() {
          Column() {
            Text() {
              Span('I am Upper-span')
                .textCase(TextCase.UpperCase)
                .fontSize(30)
                .onClick(() => {
                  hilog.info(0x0000, 'Sample_TextComponent', 'Span onClick is triggering');
                  this.textStr1 = 'Span onClick is triggering';
                })
                .onHover(() => {
                  hilog.info(0x0000, 'Sample_TextComponent', 'Span onHover is triggering');
                  this.textStr2 = 'Span onHover is triggering';
                })
            }

            Text('onClick：' + this.textStr1)
              .fontSize(20)
            Text('onHover：' + this.textStr2)
              .fontSize(20)
          }.width('100%')
        }
        .height('100%')
      }
      // ···
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/oijrayrtQEWEc7oXBZNvWA/zh-cn_image_0000002817426011.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BAAB0AA5CD980CB831621D7FF904103DE435EDB8ABD1A50BE1170A8A735DB83)

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

  ```typescript
  // 请将$r('app.string.TextAlign_Start')替换为实际资源文件，在本示例中该资源文件的value值为"左对齐"
  Text($r('app.string.TextAlign_Start'))
    .width(300)
    .textAlign(TextAlign.Start)
    .border({ width: 1 })
    .padding(10)
  // 请将$r('app.string.TextAlign_Center')替换为实际资源文件，在本示例中该资源文件的value值为"中间对齐"
  Text($r('app.string.TextAlign_Center'))
    .width(300)
    .textAlign(TextAlign.Center)
    .border({ width: 1 })
    .padding(10)
  // 请将$r('app.string.TextAlign_End')替换为实际资源文件，在本示例中该资源文件的value值为"右对齐"
  Text($r('app.string.TextAlign_End'))
    .width(300)
    .textAlign(TextAlign.End)
    .border({ width: 1 })
    .padding(10)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/y7B52sYjRXelPz6azBcoBA/zh-cn_image_0000002788466592.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B48ABCED812AA530FAF7BA5F0E76CA9BB8A6360333696C0A6602E74BABBA125)
* 通过[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)属性控制文本超长处理，textOverflow需配合[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)一起使用（默认情况下文本自动折行）。从API version 18开始，文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。

  ```typescript
  Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +
    'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +
    'of textOverflow to None text content.')
    .width(250)
    .textOverflow({ overflow: TextOverflow.None })
    .maxLines(1)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
  // 'app.string.CustomTextStyle_textContent_epsis'资源文件中的value值为
  // '我是超长文本，超出的部分显示省略号 I am an extra long text, with ellipses displayed for any excess。'
  Text($r('app.string.CustomTextStyle_textContent_epsis'))
    .width(250)
    .textOverflow({ overflow: TextOverflow.Ellipsis })
    .maxLines(1)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
  // 'app.string.CustomTextStyle_textContent_marq'资源文件中的value值为
  // '当文本溢出其尺寸时，文本将滚动显示
  // When the text overflows its dimensions,the text will scroll for displaying.'
  Text($r('app.string.CustomTextStyle_textContent_marq'))
    .width(250)
    .textOverflow({ overflow: TextOverflow.MARQUEE })
    .maxLines(1)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
  // 'app.string.CustomTextStyle_textContent_marq_def'资源文件中的value值为
  // '当文本溢出其尺寸时，文本将滚动显示，支持设置跑马灯配置项
  // When the text overflows its dimensions, the text will scroll for displaying.'
  Text($r('app.string.CustomTextStyle_textContent_marq_def'))
    .width(250)
    .textOverflow({ overflow: TextOverflow.MARQUEE })
    .maxLines(1)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .marqueeOptions({
      start: true,
      fromStart: true,
      step: 6,
      loop: -1,
      delay: 0,
      fadeout: false,
      marqueeStartPolicy: MarqueeStartPolicy.DEFAULT
    })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/KpGwRliUQH-nAKuhb4c2pg/zh-cn_image_0000002817506079.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA4007EBCF6781AC91F9DE4627FAF10F725E9BFB85C998AECF0E948971608662)
* 通过[lineHeight](../harmonyos-references/ts-basic-components-text.md#lineheight)属性设置文本行高。

  ```typescript
  Text('This is the text with the line height set. This is the text with the line height set.')
    .width(300).fontSize(12).border({ width: 1 }).padding(10)
  Text('This is the text with the line height set. This is the text with the line height set.')
    .width(300)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .lineHeight(20)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/Gx2eXmS7T1GNKw1VD8unKw/zh-cn_image_0000002788306650.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=3566D2E3019812F3860C2F42B79AB63B8100036270F2E7D8FB19193FF5AC79C7)
* 通过[decoration](../harmonyos-references/ts-basic-components-text.md#decoration)属性设置文本装饰线样式、颜色及其粗细。

  ```typescript
  Text('This is the text')
    .decoration({
      type: TextDecorationType.LineThrough,
      color: Color.Red
    })
    .borderWidth(1).padding(15).margin(5)
  Text('This is the text')
    .decoration({
      type: TextDecorationType.Overline,
      color: Color.Red
    })
    .borderWidth(1).padding(15).margin(5)
  Text('This is the text')
    .decoration({
      type: TextDecorationType.Underline,
      color: Color.Red
    })
    .borderWidth(1).padding(15).margin(5)
  Text('This is the text')
    .decoration({
      type: TextDecorationType.Underline,
      color: Color.Blue,
      style: TextDecorationStyle.DASHED
    })
    .borderWidth(1).padding(15).margin(5)
  Text('This is the text')
    .decoration({
      type: TextDecorationType.Underline,
      color: Color.Blue,
      style: TextDecorationStyle.DOTTED
    })
    .borderWidth(1).padding(15).margin(5)
  Text('This is the text')
    .decoration({
      type: TextDecorationType.Underline,
      color: Color.Blue,
      style: TextDecorationStyle.DOUBLE
    })
    .borderWidth(1).padding(15).margin(5)
  Text('This is the text')
    .decoration({
      type: TextDecorationType.Underline,
      color: Color.Blue,
      style: TextDecorationStyle.WAVY,
      thicknessScale: 4
    })
    .borderWidth(1).padding(15).margin(5)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/GdR-7OrMR42ZI8MdDmkCzQ/zh-cn_image_0000002817426013.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E56C32E9EA2D4D868CAD8D44CCFA73053DE044ADE8B865C01611F605B4F2925)
* 通过[baselineOffset](../harmonyos-references/ts-basic-components-text.md#baselineoffset)属性设置文本基线的偏移量。

  ```typescript
  Text('This is the text content with baselineOffset 0.')
    .baselineOffset(0)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .width('100%')
    .margin(5)
  Text('This is the text content with baselineOffset 30.')
    .baselineOffset(30)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .width('100%')
    .margin(5)
  Text('This is the text content with baselineOffset -20.')
    .baselineOffset(-20)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .width('100%')
    .margin(5)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/oBHRGGc-TxuuP_HcSQbFUw/zh-cn_image_0000002788466594.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=96345A0A1C93A191D0E132F5A408910DC0022F597A60A61B4E9E455A6CF8F114)
* 通过[letterSpacing](../harmonyos-references/ts-basic-components-text.md#letterspacing)属性设置文本字符间距。

  ```typescript
  Text('This is the text content with letterSpacing 0.')
    .letterSpacing(0)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .width('100%')
    .margin(5)
  Text('This is the text content with letterSpacing 3.')
    .letterSpacing(3)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .width('100%')
    .margin(5)
  Text('This is the text content with letterSpacing -1.')
    .letterSpacing(-1)
    .fontSize(12)
    .border({ width: 1 })
    .padding(10)
    .width('100%')
    .margin(5)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/bO83syjTRj-SUoOuBAW-cg/zh-cn_image_0000002817506081.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=16E87132C924504934FBC2D0EE07959ECF7E9CF854B9C91DCB319BBA11E3232A)
* 通过[minFontSize](../harmonyos-references/ts-basic-components-text.md#minfontsize)与[maxFontSize](../harmonyos-references/ts-basic-components-text.md#maxfontsize)自适应字体大小。

  minFontSize用于设置文本的最小显示字号，maxFontSize用于设置文本的最大显示字号。这两个属性必须同时设置才能生效，并且需要与[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)属性或布局大小限制配合使用，单独设置任一属性将不会产生效果。

  ```typescript
  /* 请将$r('app.string.CustomTextStyle_textContent_one_style')替换为实际资源文件，
   * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为5，宽度为250，maxLines为1"
   */
  Text($r('app.string.CustomTextStyle_textContent_one_style'))
    .width(250)
    .maxLines(1)
    .maxFontSize(30)
    .minFontSize(5)
    .border({ width: 1 })
    .padding(10)
    .margin(5)
  /* 请将$r('app.string.CustomTextStyle_textContent_two_style')替换为实际资源文件，
   * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为5，宽度为250，maxLines为2"
   */
  Text($r('app.string.CustomTextStyle_textContent_two_style'))
    .width(250)
    .maxLines(2)
    .maxFontSize(30)
    .minFontSize(5)
    .border({ width: 1 })
    .padding(10)
    .margin(5)
  /* 请将$r('app.string.CustomTextStyle_textContent_no_max')替换为实际资源文件，
   * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为15，宽度为250,高度为50"
   */
  Text($r('app.string.CustomTextStyle_textContent_no_max'))
    .width(250)
    .height(50)
    .maxFontSize(30)
    .minFontSize(15)
    .border({ width: 1 })
    .padding(10)
    .margin(5)
  /* 请将$r('app.string.CustomTextStyle_textContent_high')替换为实际资源文件，
   * 在本示例中该资源文件的value值为"我的最大字号为30，最小字号为15，宽度为250,高度为100"
   */
  Text($r('app.string.CustomTextStyle_textContent_high'))
    .width(250)
    .height(100)
    .maxFontSize(30)
    .minFontSize(15)
    .border({ width: 1 })
    .padding(10)
    .margin(5)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/bBNUJ6XhS3ehijfncb6Ixw/zh-cn_image_0000002788306652.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=B64236DA0B5E88391FC720CDA67E44D598FB7D1DCD3708C8E3894917B3BF0B59)
* 通过[textCase](../harmonyos-references/ts-basic-components-text.md#textcase)属性设置文本大小写。

  ```typescript
  Text('This is the text content with textCase set to Normal.')
    .textCase(TextCase.Normal)
    .border({ width: 1 })
    .padding(10)
    .margin(5)

  // 文本全小写展示
  Text('This is the text content with textCase set to LowerCase.')
    .textCase(TextCase.LowerCase)
    .border({ width: 1 })
    .padding(10)
    .margin(5)

  // 文本全大写展示
  Text('This is the text content with textCase set to UpperCase.')
    .textCase(TextCase.UpperCase)
    .border({ width: 1 })
    .padding(10)
    .margin(5)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ahLj4k5ySQCMEFTjO2TjAQ/zh-cn_image_0000002817426015.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=F141836A5410680793CED6D40ECFECB08E67B2B4C5F06DC6C89B30FB63A3C9F2)
* 通过[copyOption](../harmonyos-references/ts-basic-components-text.md#copyoption9)属性设置文本是否可复制粘贴。

  ```typescript
  // 请将$r('app.string.CustomTextStyle_textContent_incopy')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段可复制文本。"
  Text($r('app.string.CustomTextStyle_textContent_incopy'))
    .fontSize(30)
    .copyOption(CopyOptions.InApp)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/OXtlRT-gTYi7LJVT_SH1Bg/zh-cn_image_0000002788466596.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DB5CD7368FC03695722C984A5872027FD574F18AF0E31B11D5501BF7BAFAD17)
* 通过[fontFamily](../harmonyos-references/ts-basic-components-text.md#fontfamily)属性设置文本字体族。应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](../harmonyos-references/js-apis-font.md)。

  ```typescript
  Text('This is the text content with fontFamily')
    .fontSize(30)
    .fontFamily('HarmonyOS Sans')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/WdXBAd38SiqaIj9AJHW4EA/zh-cn_image_0000002817506083.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A0698B33FDC8E6BE8C521FC1F0F86F27AD1FFD11B7971398DB3B1F750049453)
* 从API version 20开始，支持通过[contentTransition](../harmonyos-references/ts-basic-components-text.md#contenttransition20)属性设置数字翻牌效果。

  ```typescript
  @Entry
  @Component
  struct ContentTransitionDemo {
    private static readonly INITIAL_SCORE: number = 98;
    @State number: number = ContentTransitionDemo.INITIAL_SCORE;
    @State numberTransition: NumericTextTransition =
      new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });
    build() {
      NavDestination() {
        Column() {
          Text(this.number + '')
            .borderWidth(1)
            .fontSize(40)
            .contentTransition(this.numberTransition)
          Button('change number')
            .onClick(() => {
              this.number++
            })
            .margin(10)
        }
        .width('100%')
        .height('100%')
      }
      // ···
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/oodDqoInTSCdrvS2d_dptg/zh-cn_image_0000002788306654.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C53D9FB140B6F3DE09AAD094F6130DFB528C5D69227ED10EE051997A8D855A7)
* 从API version 20开始，支持通过[optimizeTrailingSpace](../harmonyos-references/ts-basic-components-text.md#optimizetrailingspace20)设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。

  ```typescript
  Column() {
    // 启用优化行尾空格功能
    Text('Trimmed space enabled     ')
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
      .margin({ top: 20 })
      .optimizeTrailingSpace(true)
      .textAlign(TextAlign.Center)
    // 不启用优化行尾空格功能
    Text('Trimmed space disabled     ')
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
      .margin({ top: 20 })
      .optimizeTrailingSpace(false)
      .textAlign(TextAlign.Center)
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/EVtzGzeLQn-itx-20JAg_Q/zh-cn_image_0000002817426017.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F83ACA4179430A3FDB26D76AA06C2C39C87FAAF8C861C0D7AF9294EF323C3CC)
* 从API version 20开始，支持通过[lineSpacing](../harmonyos-references/ts-basic-components-text.md#linespacing20)设置文本的行间距。当不配置[LineSpacingOptions](../harmonyos-references/ts-text-common.md#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距，当onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外的行间距。

  ```typescript
  import { LengthMetrics } from '@kit.ArkUI';

  @Extend(Text)
  function style() {
    .width(250)
    .height(100)
    .maxFontSize(30)
    .minFontSize(15)
    .border({ width: 1 })
  }

  @Entry
  @Component
  struct LineSpacing {
    build() {
      NavDestination() {
        Column() {
          Text('The line spacing of this context is set to 20_px, and the spacing is effective only between the lines.')
            .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
            .style()
        }
      }
      // ···
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/jFdfbPBzSIayd-87DUI-mA/zh-cn_image_0000002788466598.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E4BD9E749412FE45D1DD3241775E1FF08DEA0AE3E2233B4B5074B724A7C8F6E)
* 从API version 20开始，支持通过[enableAutoSpacing](../harmonyos-references/ts-basic-components-text.md#enableautospacing20)设置是否开启中文与西文的自动间距。

  ```typescript
  @Entry
  @Component
  struct EnableAutoSpacing {
    @State enableSpacing: boolean = false;

    build() {
      NavDestination() {
      Column() {
        Row({ space: 20 }) {
          // 请将$r('app.string.Enable_automatic_spacing')替换为实际资源文件，在本示例中该资源文件的value值为"开启自动间距"
          Button($r('app.string.Enable_automatic_spacing'))
            .onClick(() => this.enableSpacing = true)
            .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')
            .fontColor(this.enableSpacing ? Color.White : Color.Black)
          // 请将$r('app.string.off_automatic_spacing')替换为实际资源文件，在本示例中该资源文件的value值为"关闭自动间距"
          Button($r('app.string.off_automatic_spacing'))
            .onClick(() => this.enableSpacing = false)
            .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')
            .fontColor(!this.enableSpacing ? Color.White : Color.Black)
        }
        .width('100%')
        .justifyContent(FlexAlign.Center)
        .margin({ top: 30, bottom: 20 })
        // 请将$r('app.string.Automatic_spacing_has_been_enabled')替换为实际资源文件，在本示例中该资源文件的value值为"当前状态:已开启自动间距"
        // 请将$r('app.string.Automatic_spacing_has_been_turned_off')替换为实际资源文件，在本示例中该资源文件的value值为"当前状态:已关闭自动间距"
        Text(this.enableSpacing ? $r('app.string.Automatic_spacing_has_been_enabled') : $r('app.string.Automatic_spacing_has_been_turned_off'))
          .fontSize(16)
          .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')
          .margin({ bottom: 20 })

        // 设置是否应用中西文自动间距
        /* 请将$r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing')替换为实际资源文件，
         * 在本示例中该资源文件的value值为"中西文Auto Spacing自动间距"
         */
        Text($r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing'))
          .fontSize(24)
          .padding(15)
          .backgroundColor('#F5F5F5')
          .width('90%')
          .enableAutoSpacing(this.enableSpacing)
      }
      .width('100%')
      .height('100%')
      .padding(20)
      }
      // ...
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/oA85qS4JQsWSgWBEi86V2g/zh-cn_image_0000002817506085.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=262067D764B551E23A379DB82D479B6E97326A2A75698DEF0E18F9925438DFE9)
* 从API version 20开始，支持通过[shaderStyle](../harmonyos-references/ts-basic-components-text.md#shaderstyle20)设置渐变色。

  ```typescript
  @Entry
  @Component
  struct ShaderStyleDemo {
    @State message: string = 'Hello World';
    @State linearGradientOptions: LinearGradientOptions =
      {
        direction: GradientDirection.LeftTop,
        colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
        repeating: true,
      };

    build() {
      NavDestination() {
        Column({ space: 5 }) {
          // 请将$r('app.string.direction_LeftTop')替换为实际资源文件，在本示例中该资源文件的value值为"direction为LeftTop的线性渐变"
          Text($r('app.string.direction_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)
            .margin({ top: 40, left: 40 })
          Text(this.message)
            .fontSize(50)
            .width('80%')
            .height(50)
            .shaderStyle(this.linearGradientOptions)
        }
        .height('100%')
        .width('100%')
      }
      // ...
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/8gW7UU1ZQ9uCpPZtAE5IRw/zh-cn_image_0000002788306656.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FE6A38FF2DDE6161B693A206C85004FE0AD13B4E04612315F2858E6FBD667B6)

## 添加事件

Text组件可以添加通用事件，可以绑定[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)、[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)等事件来响应操作。

```typescript
// xxx.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct GeneralEvents {
  @State textStr1: string = '';
  @State textStr2: string = '';

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text('This is a text component.')
            .fontSize(30)
            .onClick(() => {
              hilog.info(0x0000, 'Sample_TextComponent', 'Text onClick is triggering');
              this.textStr1 = 'Text onClick is triggering';
            })
            .onTouch(() => {
              hilog.info(0x0000, 'Sample_TextComponent', 'Text onTouch is triggering');
              this.textStr2 = 'Text onTouch is triggering';
            })
          Text('onClick：' + this.textStr1)
            .fontSize(20)
          Text('onTouch：' + this.textStr2)
            .fontSize(20)
        }.width('100%')
      }
      .height('100%')
    }
    // ···
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/bD55wR0BR9-D8x7CGIsOtA/zh-cn_image_0000002817426019.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D47246ECF6F2F2AB28F0B9ABB8F5194862F41680F88AF921474403FE61CC0D6)

## 设置垂直居中

从API version 20开始，Text组件支持通过[textVerticalAlign](../harmonyos-references/ts-basic-components-text.md#textverticalalign20)属性实现文本段落在垂直方向的对齐。

* 以下示例展示了如何通过textVerticalAlign属性设置文本垂直居中对齐效果。

  ```typescript
  // 请将$r('app.media.startIcon')替换为实际资源文件
  Text() {
    Span('Hello')
      .fontSize(50)
    ImageSpan($r('app.media.startIcon'))
      .width(30).height(30)
      .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)
    Span('World')
  }
  .textVerticalAlign(TextVerticalAlign.CENTER)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/ikj6xriuS0C0YEylyghzxA/zh-cn_image_0000002788466600.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=4DEDE6E89D6A1B74CEA2004730B26A93228AE1153C53CA56EE37C08DC8C2B757)

## 设置选中菜单

### 弹出选中菜单

* 设置Text被选中时，会弹出包含复制、翻译、搜索的菜单。

  Text组件需要设置[copyOption](../harmonyos-references/ts-basic-components-text.md#copyoption9)属性才可以被选中。

  ```typescript
  // 请将$r('app.string.selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
  Text($r('app.string.selected_menu'))
    .fontSize(30)
    .copyOption(CopyOptions.InApp)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Ad-fDUJ6T26iOxyDLLbJBA/zh-cn_image_0000002817506087.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AD18D6CEE9FC47725FD9DB9A475C8E3806BCD218612656A22F4DCAE94961C29)
* Text组件通过设置[bindSelectionMenu](../harmonyos-references/ts-basic-components-text.md#bindselectionmenu11)属性绑定自定义选择菜单。

  ```typescript
  controller: TextController = new TextController();
  options: TextOptions = { controller: this.controller };
  ```

  ```typescript
  // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
  Text($r('app.string.show_selected_menu'), this.options)
    .fontSize(30)
    .copyOption(CopyOptions.InApp)
    .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT_CLICK, {
      onAppear: () => {
        // 请将$r('app.string.SelectMenu_Text_Ejected')替换为实际资源文件，在本示例中该资源文件的value值为"自定义选择菜单弹出时触发该回调"
        hilog.info(0x0000, 'Sample_TextComponent',
          this.getUIContext()
            .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Ejected').id));
      },
      onDisappear: () => {
        // 'SelectMenu_Text_Close'资源文件中的value值为'自定义选择菜单关闭时触发该回调'
        hilog.info(0x0000, 'Sample_TextComponent',
          this.getUIContext()
            .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Close').id));
      }
    })
  ```

  ```typescript
  // 定义菜单项
  @Builder
  RightClickTextCustomMenu() {
    Column() {
      Menu() {
        MenuItemGroup() {
          // 请将$r('app.media.app_icon')替换为实际资源文件
          MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu One', labelInfo: '' })
            .onClick(() => {
              // 使用closeSelectionMenu接口关闭菜单
              this.controller.closeSelectionMenu();
            })
          MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Two', labelInfo: '' })
          MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Three', labelInfo: '' })
        }
      }.backgroundColor('#F0F0F0')
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/tOToWwN5QZ-h51CHgckz7w/zh-cn_image_0000002788306658.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=224E7054EF8E7DC6A524C945F17CF2E4BD40D1FACE0A286C110B7B8E15E14D57)
* Text组件通过设置[editMenuOptions](../harmonyos-references/ts-basic-components-text.md#editmenuoptions12)属性扩展自定义选择菜单，可以设置扩展项的文本内容、图标以及回调方法。

  ```typescript
  // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
  Text($r('app.string.show_selected_menu'))
    .fontSize(20)
    .copyOption(CopyOptions.LocalDevice)
    .editMenuOptions({
      onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick
    })
  ```

  ```typescript
  // 定义onCreateMenu，onMenuItemClick
  // 请将$r('app.media.app_icon')替换为实际资源文件
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'customMenu1',
      icon: $r('app.media.app_icon'),
      id: TextMenuItemId.of('customMenu1'),
    };
    let item2: TextMenuItem = {
      content: 'customMenu2',
      id: TextMenuItemId.of('customMenu2'),
      icon: $r('app.media.app_icon'),
    };
    menuItems.push(item1);
    menuItems.unshift(item2);
    return menuItems;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {
      // 请将$r('app.string.SelectMenu_Text_customMenu')替换为实际资源文件，在本示例中该资源文件的value值为"拦截 id: customMenu2 start:"
      hilog.info(0x0000, 'Sample_TextComponent',
        this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_customMenu')
          .id) + textRange.start + '; end:' +
        textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      // 请将$r('app.string.SelectMenu_Text_copy')替换为实际资源文件，在本示例中该资源文件的value值为"拦截 COPY start:"
      hilog.info(0x0000, 'Sample_TextComponent',
        this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_copy').id) +
        textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
      // 请将$r('app.string.SelectMenu_Text_SelectionAll')替换为实际资源文件，在本示例中该资源文件的value值为"不拦截 SELECT_ALL start:"
      hilog.info(0x0000, 'Sample_TextComponent',
        this.getUIContext()
          .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_SelectionAll').id) +
        textRange.start + '; end:' +
        textRange.end);
      return false;
    }
    return false;
  };
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/QEiEyKQoRUKjiHUgF_zBLA/zh-cn_image_0000002817426021.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=941B7EBE32439253BBD8863ADF2763A93C3CD830D48E0B55B39667BCE1F5EFEE)

### 关闭选中菜单

使用Text组件时，若需要实现点击空白处关闭选中的场景，分为以下两种情况：

* 在Text组件区域内点击空白处，会正常关闭选中态和菜单；
* 在Text组件区域外点击空白处，前提是Text组件设置[selection](../harmonyos-references/ts-basic-components-text.md#selection11)属性，具体示例如下：

  ```typescript
  // xxx.ets
  @Entry
  @Component
  struct SelectionChange {
    @State text: string =
      'This is set selection to Selection text content This is set selection to Selection text content.';
    @State start: number = 0;
    @State end: number = 20;

    build() {
      NavDestination() {
        Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
          Text(this.text)
            .fontSize(12)
            .border({ width: 1 })
            .lineHeight(20)
            .margin(30)
            .copyOption(CopyOptions.InApp)
            .selection(this.start, this.end)
            .onTextSelectionChange((selectionStart, selectionEnd) => {
              // 更新选中态位置
              this.start = selectionStart;
              this.end = selectionEnd;
            })
        }
        .height(600)
        .width(335)
        .borderWidth(1)
        .onClick(() => {
          // 监听父组件的点击事件，将选中首尾位置均设置为-1，即可清除选中
          this.start = -1;
          this.end = -1;
        })
      }
      // ···
    }
  }
  ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/dtjNHVgTTaa7cPjEEPvqWA/zh-cn_image_0000002788466602.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=55F0CBCEE91AE61D785EF565B905067A5116FC6AEC9F45A3D84368B47EB7A3C7)

### 屏蔽系统菜单回调和自定义扩展菜单

从API version 12开始，支持通过[editMenuOptions](../harmonyos-references/ts-basic-components-text.md#editmenuoptions12)屏蔽系统菜单回调和自定义扩展菜单项。

```typescript
// xxx.ets
@Entry
@Component
struct CustomAndBlockMenus {
  private static readonly CREATE_MENU_ITEM_ID_1: string = 'create1';
  private static readonly CREATE_MENU_ITEM_ID_2: string = 'create2';
  private static readonly PREPARE_MENU_ITEM_ID: string = 'prepare1';
  private controller: TextController = new TextController();
  @State private text: string = 'Text editMenuOptions';
  @State private endIndex: number = 0;
  @State blockCallbackText: string = '';

  // 创建菜单项辅助方法
  private createMenuItem(id: string, content: string): TextMenuItem {
    // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
    return {
      content: content,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of(id)
    };
  }

  // 查找菜单项索引
  private findMenuItemIndex(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): number {
    return menuItems.findIndex((item: TextMenuItem) => item.id.equals(menuItemId));
  }

  // 创建菜单回调
  private onCreateMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const createItem1: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE_MENU_ITEM_ID_1,
      'create1'
    );

    const createItem2: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2,
      'create2'
    );

    // 添加自定义菜单项
    menuItems.push(createItem1);
    menuItems.unshift(createItem2);

    // 移除不需要的系统菜单项
    this.removeMenuItemById(menuItems, TextMenuItemId.AI_WRITER);
    this.removeMenuItemById(menuItems, TextMenuItemId.TRANSLATE);

    return menuItems;
  }

  // 移除指定菜单项
  private removeMenuItemById(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): void {
    const targetIndex: number = this.findMenuItemIndex(menuItems, menuItemId);
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
  }

  // 菜单项点击回调
  private onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange): boolean => {
    const menuItemId: TextMenuItemId = menuItem.id;

    // 处理自定义菜单项，return false，点击自定义菜单项后菜单会关闭
    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2))) {
      let msg = '拦截 id: create2 start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg;
      return false;
    }
    // 处理自定义菜单项，return true，点击自定义菜单项后菜单不会关闭
    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.PREPARE_MENU_ITEM_ID))) {
      let msg = '拦截 id: prepare1 start:' + textRange.start + '; end:+' + textRange.end;
      this.blockCallbackText = msg;
      return true;
    }

    // 处理系统菜单项，return true，拦截系统默认逻辑，此时点击复制菜单不会关闭
    if (menuItemId.equals(TextMenuItemId.COPY)) {
      let msg = '拦截 COPY start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg;
      // 可以通过文本控制器关闭菜单，手柄也会消失，仅保持选中区域，点击可消失
      this.controller.closeSelectionMenu();
      return true;
    }
    // 处理系统菜单项，return false，不拦截系统默认逻辑，自定义逻辑亦会被执行
    if (menuItemId.equals(TextMenuItemId.SELECT_ALL)) {
      let msg = '不拦截 SELECT_ALL start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg;
      return false;
    }

    return false;
  }
  // 准备菜单回调
  private onPrepareMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const prepareItem: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.PREPARE_MENU_ITEM_ID,
      `prepare1_${this.endIndex}`
    );

    menuItems.unshift(prepareItem);
    return menuItems;
  }
  // 编辑菜单选项
  @State private editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };
  // 文本选择变化回调
  private onTextSelectionChange = (selectionStart: number, selectionEnd: number): void => {
    this.endIndex = selectionEnd;
  }

  build() {
    NavDestination() {
      Column() {
        Text(this.text, { controller: this.controller })
          .fontSize(20)
          .copyOption(CopyOptions.LocalDevice)
          .editMenuOptions(this.editMenuOptions)
          .margin({ top: 100 })
          .onTextSelectionChange(this.onTextSelectionChange)
        Text(this.blockCallbackText).borderWidth(1)
      }
      .width('90%')
      .margin('5%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/g8rAsu8ZSNenFoHlplGfiQ/zh-cn_image_0000002817506089.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=FACCD2E1BD9199101D6C124AA8744029DE5ABB0DEB6E7EAF5FF97FDB283C6A54)

### 屏蔽系统服务类菜单

* 从API version 20开始，支持通过[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)屏蔽文本选择菜单内所有系统服务菜单项。更多详见[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。

  ```typescript
  import { TextMenuController } from '@kit.ArkUI';
  // xxx.ets
  @Entry
  @Component
  struct ServiceMenuItems {
    aboutToAppear(): void {
      // 禁用所有系统服务菜单
      TextMenuController.disableSystemServiceMenuItems(true);
    }

    aboutToDisappear(): void {
      // 页面消失恢复系统服务菜单
      TextMenuController.disableSystemServiceMenuItems(false);
    }
    build() {
      NavDestination() {
        Row() {
          Column() {
            // 请将$r('app.string.Service_MenuItems_Text')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，长按弹出文本选择菜单。"
            Text($r('app.string.Service_MenuItems_Text'))
              .height(60)
              .fontStyle(FontStyle.Italic)
              .fontWeight(FontWeight.Bold)
              .textAlign(TextAlign.Center)
              .copyOption(CopyOptions.InApp)
              .editMenuOptions({
                onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                  // menuItems不包含被屏蔽的系统菜单项
                  return menuItems;
                },
                onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                  return false;
                }
              })
          }.width('100%')
        }
        .height('100%')
      }
      // ...
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/lGX4fz4eT9y4ss_IqqpO2w/zh-cn_image_0000002788306660.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7CB92DA4A370BFA5BA47E864A2FB1EE4BCDE6C4571E20B53C3EA00B989315B7)
* 从API version 20开始，支持通过[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)屏蔽文本选择菜单内指定的系统服务菜单项。更多详见[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。

  ```typescript
  import { TextMenuController } from '@kit.ArkUI';

  // xxx.ets
  @Entry
  @Component
  struct DisableMenuItems {
    aboutToAppear(): void {
      // 禁用搜索菜单
      TextMenuController.disableMenuItems([TextMenuItemId.SEARCH])
    }

    aboutToDisappear(): void {
      // 恢复系统服务菜单
      TextMenuController.disableMenuItems([])
    }

    build() {
      NavDestination() {
        Row() {
          Column() {
            // 请将$r('app.string.Service_MenuItems_Text')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，长按弹出文本选择菜单。"
            Text($r('app.string.Service_MenuItems_Text'))
              .height(60)
              .fontStyle(FontStyle.Italic)
              .fontWeight(FontWeight.Bold)
              .textAlign(TextAlign.Center)
              .copyOption(CopyOptions.InApp)
              .editMenuOptions({
                onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                  // menuItems不包含搜索
                  return menuItems;
                },
                onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                  return false
                }
              })
          }.width('100%')
        }
        .height('100%')
      }
      // ...
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Zk8KiUn-RFOo1odrLt-ZQw/zh-cn_image_0000002817426023.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=A29108BFCAAF0268FA35A6D5772B400EA706838CAC418B15B47603D8B6CB56D3)

### 默认菜单支持自定义刷新能力

从API version 20开始，当文本选择区域变化后显示菜单之前触发[onPrepareMenu](../harmonyos-references/ts-text-common.md#属性-1)回调，可在该回调中进行菜单数据设置。

```typescript
// 请将$r('app.media.xxx')替换为实际资源文件
// xxx.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0000;
@Entry
@Component
struct PrepareMenu {
  @State text: string = 'Text editMenuOptions';
  @State endIndex: number = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    };
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    };
    menuItems.push(item1);
    menuItems.unshift(item2);
    return menuItems;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: create2 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: prepare1 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept COPY start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'No interception SELECT_ALL start:' + textRange.start + '; end:' + textRange.end);
      return false;
    }
    return false;
  }
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'prepare1_' + this.endIndex,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('prepare1'),
    };
    menuItems.unshift(item1);
    return menuItems;
  }
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  build() {
    NavDestination() {
    Column() {
      Text(this.text)
        .fontSize(20)
        .copyOption(CopyOptions.LocalDevice)
        .editMenuOptions(this.editMenuOptions)
        .margin({ top: 100 })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.endIndex = selectionEnd;
        })
    }
    .width('90%')
    .margin('5%')
    }
    // ...
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/icI-a42NSXiED1RdWFFUOQ/zh-cn_image_0000002788466604.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=75199D2A9C0B36D5C1AEAB05691CB5A8B22C515D191BC0D26A7D80B1220C7812)

## 设置AI菜单

Text组件通过[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)和[dataDetectorConfig](../harmonyos-references/ts-basic-components-text.md#datadetectorconfig11)属性实现AI菜单的显示。AI菜单的表现形式包括：单击AI实体（指可被识别的内容，包括地址、邮箱等）弹出菜单的实体识别选项，选中文本后，文本选择菜单与鼠标右键菜单中显示的实体识别选项。

**说明** 

从API version 20开始，支持在文本选择菜单与鼠标右键菜单中显示实体识别选项。当[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)设置为true，且[copyOption](../harmonyos-references/ts-basic-components-text.md#copyoption9)设置为CopyOptions.LocalDevice时，该功能生效。菜单选项包括[TextMenuItemId](../harmonyos-references/ts-text-common.md#textmenuitemid12)中的url(打开链接)、email(新建邮件)、phoneNumber(呼叫)、address(导航至该位置)、dateTime(新建日程提醒)。

该功能生效时，需选中范围内，包括一个完整的AI实体，才能展示对应的选项。

* 如果需要单击AI实体弹出菜单的实体识别选项，可以配置[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)为true。具体示例如下所示：

  ```typescript
  // 'app.string.AIMenu_Text_One'资源文件中的value值为'电话号码：(86) (755) ********  \n \n 链接：www.********.com
  // \n \n 邮箱：***@example.com\n \n 地址：XX省XX市XX区XXXX \n \n 时间：XX年XX月XX日XXXX'
  Text($r('app.string.AIMenu_Text_One'))
    .fontSize(16)
    .copyOption(CopyOptions.LocalDevice)
    .enableDataDetector(true)// 使能实体识别
    .dataDetectorConfig({
      // 配置识别样式
      // types可支持PHONE_NUMBER电话号码、URL链接、EMAIL邮箱、ADDRESS地址、DATE_TIME时间
      // types设置为null或者[]时，识别所有类型的实体
      types: [], onDetectResultUpdate: (result: string) => {
      }
    })
  ```
* 如果需要调整识别出的样式，可以通过[dataDetectorConfig](../harmonyos-references/ts-basic-components-text.md#datadetectorconfig11)实现，具体可以参考[TextDataDetectorConfig](../harmonyos-references/ts-text-common.md#textdatadetectorconfig11对象说明)配置项。
* 如果需要调整菜单的位置，可以通过[editMenuOptions](../harmonyos-references/ts-basic-components-text.md#editmenuoptions12)实现，具体可以参考示例[文本扩展自定义菜单](../harmonyos-references/ts-basic-components-text.md#示例12文本扩展自定义菜单)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/0AWbUdQ5R12ssFx6BAhTIA/zh-cn_image_0000002817506091.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3875EB49BC02CB8822ED527A4F29FBBC9D30D40C9591FD4F9DE741E1117C85C)

## 跨节点选中

在文章阅读、商品详情、协议条款等场景中，正文内容通常由标题、副标题、多个段落等独立Text组件分别承载。若无法跨越多个文本组件边界连续选择，多Text组件场景下选择体验存在割裂。

从API版本26.0.0开始，可通过[SelectionContainer](../harmonyos-references/ts-basic-components-selectioncontainer.md)组件为多个Text子组件提供统一的跨节点文本选中、复制及菜单扩展能力。用户长按后可在不同Text节点之间拖拽连续选中文本，选中文本按Text组件视觉顺序拼接后统一复制，同时支持统一配置选中手柄颜色、高亮颜色、文本拼接策略及自定义菜单。SelectionContainer默认采用[Stack](../harmonyos-references/ts-container-stack.md)布局，如需线性布局请在SelectionContainer内放置Column或Row等容器组件。

### 实现跨节点文本选中与复制

将多个Text组件置于SelectionContainer内，通过[copyOption](../harmonyos-references/ts-basic-components-selectioncontainer.md#copyoption)设置可复制范围，即可实现跨Text组件的连续选中和复制。通过[caretColor](../harmonyos-references/ts-basic-components-selectioncontainer.md#caretcolor)和[selectedBackgroundColor](../harmonyos-references/ts-basic-components-selectioncontainer.md#selectedbackgroundcolor)可统一设置选中手柄和高亮颜色，通过[onTextSelectionChange](../harmonyos-references/ts-basic-components-selectioncontainer.md#ontextselectionchange)、[onWillCopy](../harmonyos-references/ts-basic-components-selectioncontainer.md#onwillcopy)、[onCopy](../harmonyos-references/ts-basic-components-selectioncontainer.md#oncopy)可监听选中变化和复制流程。

```typescript
// xxx.ets
import {
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerTextJoinStyle
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerDemo {
  @State selectedParts: string = '';
  @State copiedText: string = '';

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text('请在下方区域跨节点选中文本')
          .fontSize(16)
          .fontColor('#999999')

        SelectionContainer() {
          Column({ space: 12 }) {
            Text('跨节点选中示例文章')
              .fontSize(24)
              .fontWeight(FontWeight.Bold)
            Text('在文章阅读场景中，标题与正文通常由多个Text组件分别承载。用户期望能够跨段落连续选中文本。')
              .fontSize(16)
            Text('SelectionContainer组件为多个文本节点提供跨节点选中、复制及菜单扩展能力，提升复杂文本布局中的交互体验。')
              .fontSize(16)
          }
        }
        .copyOption(CopyOptions.InApp)
        .textJoinStyle(SelectionContainerTextJoinStyle.NEWLINE)
        .caretColor(Color.Red)
        .selectedBackgroundColor('#33007DFF')
        .onTextSelectionChange((value: Array<string>) => {
          this.selectedParts = value.join(' | ');
        })
        .onWillCopy((value: string) => {
          this.copiedText = `准备复制：${value}`;
          return true;
        })
        .onCopy((value: string) => {
          this.copiedText = `复制成功：${value}`;
        })
        .border({ width: 1, color: '#DCDCDC' })
        .padding(12)
        .width('100%')

        Text(`选中内容：${this.selectedParts}`)
          .fontSize(14)
          .fontColor('#666666')
        Text(this.copiedText)
          .fontSize(14)
          .fontColor('#666666')
      }
      .width('100%')
      .padding(16)
    }
    // ...
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/hkMkkfPmRP26066yqkF_Jw/zh-cn_image_0000002788306662.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE21093A49EE6B138B6622C955523B13304DEC1FB691ADC8B5925C9C6CF575CD)

### 配置跨节点文本拼接方式

跨节点选中涉及多个Text组件时，复制到剪贴板的文本需按视觉顺序拼接。通过[textJoinStyle](../harmonyos-references/ts-basic-components-selectioncontainer.md#textjoinstyle)可设置拼接方式：[SelectionContainerTextJoinStyle](../harmonyos-references/ts-basic-components-selectioncontainer.md#selectioncontainertextjoinstyle).NEWLINE在不同文本节点间插入换行符，.DIRECT直接拼接不添加分隔符。

```typescript
// xxx.ets
import {
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerTextJoinStyle
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerJoinStyle {
  @State joinStyle: SelectionContainerTextJoinStyle = SelectionContainerTextJoinStyle.NEWLINE;
  @State selectedText: string = '';
  @State copiedText: string = '';

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Row({ space: 12 }) {
          Button('换行拼接')
            .type(ButtonType.Capsule)
            .backgroundColor(this.joinStyle === SelectionContainerTextJoinStyle.NEWLINE ? '#007DFF' : '#E0E0E0')
            .fontColor(this.joinStyle === SelectionContainerTextJoinStyle.NEWLINE ? Color.White : Color.Black)
            .onClick(() => {
              this.joinStyle = SelectionContainerTextJoinStyle.NEWLINE;
            })
          Button('直接拼接')
            .type(ButtonType.Capsule)
            .backgroundColor(this.joinStyle === SelectionContainerTextJoinStyle.DIRECT ? '#007DFF' : '#E0E0E0')
            .fontColor(this.joinStyle === SelectionContainerTextJoinStyle.DIRECT ? Color.White : Color.Black)
            .onClick(() => {
              this.joinStyle = SelectionContainerTextJoinStyle.DIRECT;
            })
        }

        SelectionContainer() {
          Column({ space: 12 }) {
            Text('第一段文本：选中后复制的拼接方式由textJoinStyle决定。')
              .fontSize(18)
            Text('第二段文本：换行拼接时两段文本间会插入换行符，直接拼接时不插入任何分隔符。')
              .fontSize(18)
          }
        }
        .copyOption(CopyOptions.InApp)
        .textJoinStyle(this.joinStyle)
        .onTextSelectionChange((value: Array<string>) => {
          this.selectedText = value.join(' | ');
        })
        .onWillCopy((value: string) => {
          this.copiedText = value;
          return true;
        })
        .onCopy((value: string) => {
          this.copiedText = value;
        })
        .border({ width: 1, color: '#DCDCDC' })
        .padding(12)
        .width('100%')

        Text(`选中内容：${this.selectedText}`)
          .fontSize(14)
          .fontColor('#666666')
        Text('复制内容（体现拼接方式差异）：')
          .fontSize(14)
          .fontColor('#666666')
        Text(this.copiedText)
          .fontSize(14)
          .fontColor('#333333')
          .backgroundColor('#F5F5F5')
          .padding(8)
          .borderRadius(4)
          .width('100%')
      }
      .width('100%')
      .padding(16)
    }
    // ...
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/yDPCamtBQzCCNw_181xplw/zh-cn_image_0000002817426025.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=177C023EA9D7BD722E53B5A8E3CE6AACFEC70AB7EA02D879208303E58A37C06A)

### 绑定自定义选择菜单

当系统默认菜单无法满足业务需求时，可通过[bindSelectionMenu](../harmonyos-references/ts-basic-components-selectioncontainer.md#bindselectionmenu)绑定完全自定义的选择菜单。与系统菜单不同，自定义菜单的内容、样式和触发条件均由开发者定义。

```typescript
// xxx.ets
import {
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerMenuOptions,
  SelectionContainerTextJoinStyle
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerCustomMenu {
  @State selectedText: string = '';
  @State menuLog: string = '';

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text('请在下方区域选中文本，体验自定义菜单')
          .fontSize(16)
          .fontColor('#999999')

        SelectionContainer() {
          Column({ space: 12 }) {
            Text('第一段文本：跨节点选中后长按可弹出完全自定义的选择菜单。')
              .fontSize(18)
            Text('第二段文本：通过bindSelectionMenu绑定自定义菜单，可替代系统默认菜单。')
              .fontSize(18)
          }
        }
        .copyOption(CopyOptions.InApp)
        .textJoinStyle(SelectionContainerTextJoinStyle.DIRECT)
        .bindSelectionMenu(
          TextSpanType.TEXT,
          this.menuBuilder,
          TextResponseType.DEFAULT,
          {
            onAppear: (text: string) => {
              this.menuLog = `菜单出现，选中文本：${text}`;
            },
            onDisappear: () => {
              this.menuLog = '菜单消失';
            }
          } as SelectionContainerMenuOptions
        )
        .onTextSelectionChange((value: Array<string>) => {
          this.selectedText = value.join(' | ');
        })
        .border({ width: 1, color: '#DCDCDC' })
        .padding(12)
        .width('100%')

        Text(`选中内容：${this.selectedText}`)
          .fontSize(14)
          .fontColor('#666666')
        Text(this.menuLog)
          .fontSize(14)
          .fontColor('#999999')
      }
      .width('100%')
      .padding(16)
    }
    // ...
  }

  @Builder
  menuBuilder() {
    Column() {
      Menu() {
        MenuItemGroup() {
          MenuItem({ content: '自定义复制', labelInfo: '' })
            .onClick(() => {
              this.menuLog = '点击了自定义复制';
            })
          MenuItem({ content: '自定义分享', labelInfo: '' })
            .onClick(() => {
              this.menuLog = '点击了自定义分享';
            })
          MenuItem({ content: '自定义翻译', labelInfo: '' })
            .onClick(() => {
              this.menuLog = '点击了自定义翻译';
            })
        }
      }
      .radius($r('sys.float.ohos_id_corner_radius_card'))
      .clip(true)
      .backgroundColor('#F0F0F0')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/LgtlW7WUSOuz4osGAqSw3A/zh-cn_image_0000002788466606.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=D17FD6A96E394C452A2E1807B4205309EA70674B2901EF80794E7176A8447214)

### 扩展系统菜单选项

若需在保留系统菜单项的基础上增加自定义选项，可通过[editMenuOptions](../harmonyos-references/ts-basic-components-selectioncontainer.md#editmenuoptions)实现。该方式支持添加自定义菜单项、移除指定系统菜单项，并在[onMenuItemClick](../harmonyos-references/ts-basic-components-selectioncontainer.md#onmenuitemclickwithtextcallback)回调中通过返回值拦截或放行系统默认行为。

```typescript
// xxx.ets
import {
  OnMenuItemClickWithTextCallback,
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerEditMenuOptions,
  SelectionContainerTextJoinStyle
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerExtendMenu {
  @State selectedText: string = '';
  @State menuClickLog: string = '';

  onCreateMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    let targetIndex: number = menuItems.findIndex((item: TextMenuItem) => item.id.equals(TextMenuItemId.TRANSLATE));
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
    targetIndex = menuItems.findIndex((item: TextMenuItem) => item.id.equals(TextMenuItemId.SEARCH));
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
    let highlightItem: TextMenuItem = {
      content: '标注',
      id: TextMenuItemId.of('highlight')
    };
    let bookmarkItem: TextMenuItem = {
      content: '收藏',
      id: TextMenuItemId.of('bookmark')
    };
    let commentItem: TextMenuItem = {
      content: '批注',
      id: TextMenuItemId.of('comment')
    };
    menuItems.push(highlightItem);
    menuItems.push(bookmarkItem);
    menuItems.push(commentItem);
    return menuItems;
  }

  onMenuItemClick: OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, text: string): boolean => {
    this.menuClickLog = `点击菜单项：${menuItem.content}，选中文本：${text}`;
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      this.selectedText = `已复制：${text}`;
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
      this.selectedText = `全选操作：${text}`;
      return false;
    }
    if (menuItem.id.equals(TextMenuItemId.of('highlight'))) {
      this.selectedText = `已标注：${text}`;
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('bookmark'))) {
      this.selectedText = `已收藏：${text}`;
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('comment'))) {
      this.selectedText = `已批注：${text}`;
      return true;
    }
    return false;
  }

  @State editMenuOptions: SelectionContainerEditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick
  };

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text('请在下方区域选中文本，体验扩展菜单')
          .fontSize(16)
          .fontColor('#999999')

        SelectionContainer() {
          Column({ space: 12 }) {
            Text('第一段文本：通过editMenuOptions可以在系统菜单基础上扩展自定义项。')
              .fontSize(18)
            Text('第二段文本：可以移除不需要的系统菜单项，并添加标注、收藏、批注等自定义项。')
              .fontSize(18)
          }
        }
        .copyOption(CopyOptions.InApp)
        .textJoinStyle(SelectionContainerTextJoinStyle.DIRECT)
        .editMenuOptions(this.editMenuOptions)
        .onTextSelectionChange((value: Array<string>) => {
          this.selectedText = value.join(' | ');
        })
        .border({ width: 1, color: '#DCDCDC' })
        .padding(12)
        .width('100%')

        Text(this.selectedText)
          .fontSize(14)
          .fontColor('#666666')
        Text(this.menuClickLog)
          .fontSize(14)
          .fontColor('#999999')
      }
      .width('100%')
      .padding(16)
    }
    // ...
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/K-CyQkifRYqy6VeOCMXNZw/zh-cn_image_0000002817506093.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=083945B2643E59D1E841AFEBFEE14665A519407B9707EB0E659679F1F089B950)

### 通过控制器关闭菜单与清除选中

在页面跳转、弹窗遮盖等场景下，需主动关闭选择菜单或清除选中状态。可通过[SelectionContainerController](../harmonyos-references/ts-basic-components-selectioncontainer.md#selectioncontainercontroller)的[closeSelectionMenu](../harmonyos-references/ts-basic-components-selectioncontainer.md#closeselectionmenu)关闭菜单，通过[clearTextSelection](../harmonyos-references/ts-basic-components-selectioncontainer.md#cleartextselection)清除选中态。

```typescript
// xxx.ets
import {
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerController
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerControllerDemo {
  private controller: SelectionContainerController = new SelectionContainerController();
  @State selectedText: string = '';

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text('请在下方区域跨节点选中文本，再点击按钮操作')
          .fontSize(16)
          .fontColor('#999999')

        SelectionContainer({ controller: this.controller }) {
          Column({ space: 12 }) {
            Text('第一段文本：选中后可通过控制器关闭选择菜单或清除选中文本。')
              .fontSize(18)
            Text('第二段文本：closeSelectionMenu仅关闭菜单，clearTextSelection会同时清除选中态。')
              .fontSize(18)
          }
        }
        .copyOption(CopyOptions.InApp)
        .onTextSelectionChange((value: Array<string>) => {
          this.selectedText = value.join(' | ');
        })
        .border({ width: 1, color: '#DCDCDC' })
        .padding(12)
        .width('100%')

        Row({ space: 12 }) {
          Button('关闭选择菜单')
            .type(ButtonType.Capsule)
            .onClick(() => {
              this.controller.closeSelectionMenu();
            })
          Button('清除文本选中')
            .type(ButtonType.Capsule)
            .onClick(() => {
              this.controller.clearTextSelection();
              this.selectedText = '';
            })
        }

        Text(`选中内容：${this.selectedText}`)
          .fontSize(14)
          .fontColor('#666666')
      }
      .width('100%')
      .padding(16)
    }
    // ...
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/baRxmWLaSNqLEr3Xzi58wg/zh-cn_image_0000002788306664.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=A95623EB9688F7419EDF078FCF539461DFCF644C186FA3BB98CAF80937F133A3)

## 实现热搜榜

该示例通过[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)、[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)、[textAlign](../harmonyos-references/ts-basic-components-text.md#textalign)、[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)属性展示了热搜榜的效果。

```typescript
@Entry
@Component
struct TextHotSearch {
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Column() {
            Row() {
              Text('1').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
              // 请将$r('app.string.TextHotSearch_textContent_one')替换为实际资源文件，在本示例中该资源文件的value值为"我是热搜词条1"
              Text($r('app.string.TextHotSearch_textContent_one'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .fontWeight(300)
              // 请将$r('app.string.TextHotSearch_textContent_two')替换为实际资源文件，在本示例中该资源文件的value值为"爆"
              Text($r('app.string.TextHotSearch_textContent_two'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0x770100)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('2').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
              /* 请将$r('app.string.TextHotSearch_textContent_three')替换为实际资源文件，
               * 在本示例中该资源文件的value值为"我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2"
               */
              Text($r('app.string.TextHotSearch_textContent_three'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
              // 请将$r('app.string.TextHotSearch_textContent_four')替换为实际资源文件，在本示例中该资源文件的value值为"热"
              Text($r('app.string.TextHotSearch_textContent_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('3').fontSize(14).fontColor(Color.Orange).margin({ left: 10, right: 10 })
              // 请将$r('app.string.TextHotSearch_textContent_five')替换为实际资源文件，在本示例中该资源文件的value值为"我是热搜词条3"
              Text($r('app.string.TextHotSearch_textContent_five'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .maxLines(1)
                .constraintSize({ maxWidth: 200 })
                .textOverflow({ overflow: TextOverflow.Ellipsis })
              // 请将$r('app.string.TextHotSearch_textContent_four')替换为实际资源文件，在本示例中该资源文件的value值为"热"
              Text($r('app.string.TextHotSearch_textContent_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('4').fontSize(14).fontColor(Color.Grey).margin({ left: 10, right: 10 })
              /* 请将$r('app.string.TextHotSearch_textContent_six')替换为实际资源文件，
               * 在本示例中该资源文件的value值为"我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4"
               */
              Text($r('app.string.TextHotSearch_textContent_six'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
            }.width('100%').margin(5)
          }.width('100%')
        // ...
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    // ...
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/jmvj3PE9Swa3UkJq3QST3A/zh-cn_image_0000002817426027.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=99D2AEA3823E98DCFED2BC645981F424A3D70C08FA14DA38F124321D3553D2A9)

## 示例代码

* [文字特效合集](https://gitcode.com/HarmonyOS_Samples/text-effects)
