---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-rich-text-display
title: 富文本显示的选型与开发
breadcrumb: 最佳实践 > 布局与弹窗 > 富文本显示的选型与开发
category: best-practices
scraped_at: 2026-04-28T08:19:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f409ea48d719f940cb797b274c49be936f66de87745be298db571aa008a7def0
---

## 概述

富文本格式是一种便于在不同设备和系统间查看的文本与图形文档格式。本文将重点介绍显示富文本数据所需的相关组件的特性，并探讨如下几种常见场景及其实现方法：

* [实现高亮显示的超链接文本](bpta-rich-text-display.md#section16779144302217)
* [实现文本中的图片表情](bpta-rich-text-display.md#section175121131193714)
* [实现自定义的图文元素](bpta-rich-text-display.md#section48901816104715)
* [实现图标与文本的组合元素](bpta-rich-text-display.md#section20943112412539)

### 能力介绍

**特点**

应用中的富文本可能具有以下特点：

* 文本样式：包括字体前景色、背景色、字体类型、字号、粗体、下划线、删除线等装饰线、基线偏移、字符间距、行高和段落样式等。
* 定制效果：如边框、阴影、渐变和背景图片等。
* 图文混排：支持emoji表情、图标和网络图片等。
* 高亮超链接：包括@提醒、#标签、电话、Email和Https链接等。
* 手势交互：支持单击和长按等操作。
* 应用范围：富文本可能在文本显示的任何区域使用，如详情页内容、列表信息流、编辑器及弹窗提示框等。

**能力支持**

以下为当前各种组件能力支持情况的汇总表，仅供参考。

| 技术方案 | [Text](../harmonyos-references/ts-basic-components-text.md)/[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)+ [StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring) 属性字符串 | [Text](../harmonyos-references/ts-basic-components-text.md)+[Span](../harmonyos-references/ts-basic-components-span.md)子组件 | [Text](../harmonyos-references/ts-basic-components-text.md)+ [enableDataDetector()](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11) 文本识别 | [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)+ [addTextSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan) | [Web](../harmonyos-references/ts-basic-components-web.md) | [RichText](../harmonyos-references/ts-basic-components-richtext.md)(Deprecated) |
| --- | --- | --- | --- | --- | --- | --- |
| 支持元素种类 | 文本、图片、自定义 | [Span](../harmonyos-references/ts-basic-components-span.md)、[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)、 [SymbolSpan](../harmonyos-references/ts-basic-components-symbolspan.md)、 [ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md) | [TextDataDetectorType](../harmonyos-references/ts-text-common.md#textdatadetectortype11枚举说明) 中的类型，包括电话号码、 链接、邮箱、地址、时间 | 文本、图片、自定义 | 丰富，HTML标签元素 | 支持[标签范围](../harmonyos-references/ts-basic-components-richtext.md#支持标签)内的元素 |
| 扩展元素类型 | 支持 | 不支持 | 不支持 | 支持 | 不支持 | 不支持 |
| 自定义元素样式 | 支持 | [Span](../harmonyos-references/ts-basic-components-span.md)、[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)、 [SymbolSpan](../harmonyos-references/ts-basic-components-symbolspan.md)、[ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md) 组件属性范围内的样式设置 | 支持颜色、装饰线设置 | 支持 | 通过css支持 | 通过css有限支持 |
| 元素事件类型 | 点击、长按 | [Span](../harmonyos-references/ts-basic-components-span.md)、[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)支持点击 | 点击 | 点击、长按 | 点击 | 不支持 |
| 自定义元素事件 | 支持 | 支持 | 不支持 | 支持 | 支持 | 不支持 |
| 自定义扩展信息 | 支持 | 自行维护 | 自行维护 | 自行维护 | 自行维护 | 自行维护 |
| 加载HTML文本 并渲染显示 | 仅支持<p>、<span>、 <img> | 不支持 | 不支持 | 不支持 | 支持 | 有限支持：[标签范围](../harmonyos-references/ts-basic-components-richtext.md#支持标签) |
| 长列表中显示 | 支持 | 支持 | 支持 | 支持 | 不推荐，影响性能 | 不推荐，影响性能 |
| 宽高根据内容自 适应 | 支持 | 支持 | 支持 | 支持 | 不支持 | 不支持 |

**使用建议**

建议开发者全面考虑需求场景的特点及其潜在的扩展需求，然后根据自身能力进行技术选型。

| [Text](../harmonyos-references/ts-basic-components-text.md)/[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)+ [StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring) 属性字符串 | [Text](../harmonyos-references/ts-basic-components-text.md)+[Span](../harmonyos-references/ts-basic-components-span.md) 等Text的子组件 | [Text](../harmonyos-references/ts-basic-components-text.md)+ [enableDataDetector()](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11) 文本识别方法 | [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)+ [addTextSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan) 类似方法 | [Web](../harmonyos-references/ts-basic-components-web.md) | [RichText](../harmonyos-references/ts-basic-components-richtext.md)(Deprecated) |
| --- | --- | --- | --- | --- | --- |
| 可以更新各元素的 样式；  可自定义富文本的 呈现效果；  可扩展元素种类并 自定义其样式；  元素可携带自定义 扩展信息。 | 通过子组件布局 实现，结构较为 清晰；  支持的元素种类 有限 （如文本、 图片、图标 等）。 | 使用相对简单；  仅支持文本内容；  依赖底层的识别能力；  事件和菜单不可自定 义。 | 可以自定义富文本 的呈现效果；  可以扩展元素种类 并自定义样式；  不支持更新自定义 Span的样式；  扩展信息需由开发 者自行维护。 | 支持加载和显示本地网页、在线网页及HTML格式的文本；  不适用于长列表等特定场景。 | 可加载并显示 HTML格式的文本， 适用于元素样式在 其标签范围内的 场景；  较为消耗内存 资源；  不适用于长列 表等场景；  不适用于需要 对HTML字符 串显示效果 进行大量自 定义的应用 场景。 |

**选择路线图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/FEm1WsP1SaCmKAWWff4J8g/zh-cn_image_0000002383675044.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=2932F692DFBD8D0134EB09175927E67E161E25845506E0F219B84C4A856CE6A4 "点击放大")

从上图可以看出，在简单场景中通常使用[Text](../harmonyos-references/ts-basic-components-text.md)+[Span](../harmonyos-references/ts-basic-components-span.md)组件，因为其使用简便且能满足需求，可以优先考虑。相比之下，[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)+[addTextSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)较为复杂，适用于更复杂的场景。而[Text](../harmonyos-references/ts-basic-components-text.md)/[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)+[StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring)属性字符串的使用虽然更为复杂，但其兼容性更高，功能更丰富，可以根据具体场景自定义组件，适用范围更广。以下将详细介绍几种常见属性字符串的应用案例。

## 实现高亮显示的超链接文本

### 场景描述

在社交和聊天等应用平台中，常见的文本元素包括@昵称、#话题和https链接等高亮显示的内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/RK09JFdtRmWi4pbk-rCDJg/zh-cn_image_0000002383515160.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=0CD5272040B7A32E9E518B42B7B8AE3560F40CF86FB6E756C05C2116CE5C21D2)

### 实现原理

只需对文中的@昵称和#话题等文字设置高亮样式，并添加点击跳转事件，点击后跳转至相应的话题详情页面或用户详情页面。选择的方案如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/mY7JfndCRImloGgVLDl8sA/zh-cn_image_0000002417154469.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=98B2F6C9A0CC473644F5C53A0305357A8D7C6688AF651812CCA8E55AC9438275 "点击放大")

可以通过属性字符串[StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring)中的[TextStyle](../harmonyos-references/ts-universal-styled-string.md#textstyle)属性设置样式，并通过[GestureStyle](../harmonyos-references/ts-universal-styled-string.md#gesturestyle)属性实现点击事件。

### 开发步骤

1. 初始化时通过[TextStyle](../harmonyos-references/ts-universal-styled-string.md#textstyle)属性定义文字样式，包括文字颜色、大小等。

   ```
   1. textAttribute: TextStyle = new TextStyle({
   2. fontColor: $r('app.color.styled_text_link_font_color'),
   3. fontSize: LengthMetrics.fp(14)
   4. });
   ```

   [TitleLink.ets](https://gitcode.com/harmonyos_samples/styledtext/blob/master/entry/src/main/ets/pages/TitleLink.ets#L34-L38)
2. 使用[GestureStyle](../harmonyos-references/ts-universal-styled-string.md#gesturestyle)属性定义点击超链接时的跳转事件。

   ```
   1. generateClickStyle(span: MyCustomSpan): GestureStyle {
   2. return new GestureStyle({
   3. onClick: () => {
   4. this.linkClickCallback(span);
   5. }
   6. })
   7. }
   ```

   [TitleLink.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/TitleLink.ets#L68-L75)
3. 循环处理文本数据，并生成属性字符串。

   ```
   1. handleStyledString() {
   2. if (this.systemLanguage === 'zh-Hans') {
   3. this.spans = TitleLinkMock;
   4. } else {
   5. this.spans = TitleLinkMock_EN;
   6. }
   7. this.spans.forEach((span) => {
   8. if (span.url) {
   9. this.handleLink(span);
   10. } else {
   11. this.styledStrings.push(new MutableStyledString(span.content, []));
   12. }
   13. });

   15. this.controller = HandleData.handleStyledString(this.styledStrings);
   16. }
   ```

   [TitleLink.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/TitleLink.ets#L82-L98)
4. 设置文本样式和点击事件。

   ```
   1. handleLink(span: MyCustomSpan) {
   2. this.styledStrings.push(new MutableStyledString(span.content, [{
   3. start: 0,
   4. length: span.content.length,
   5. styledKey: StyledStringKey.GESTURE,
   6. styledValue: this.generateClickStyle(span)
   7. }, {
   8. start: 0,
   9. length: span.content.length,
   10. styledKey: StyledStringKey.FONT,
   11. styledValue: this.textAttribute
   12. }
   13. ]));
   14. }
   ```

   [TitleLink.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/TitleLink.ets#L45-L59)
5. 将生成的属性信息拼接成属性字符串，并绑定到[Text](../harmonyos-references/ts-basic-components-text.md)组件以进行渲染显示。

   ```
   1. static handleStyledString(styledStrings: MutableStyledString[]): TextController {
   2. let controller: TextController = new TextController();
   3. let paragraphStyledString: MutableStyledString = new MutableStyledString('', []);

   5. // Append the attribute string generated for each text fragment to the attribute string paragraphStyledString
   6. styledStrings.forEach((mutableStyledString: MutableStyledString) => {
   7. paragraphStyledString.appendStyledString(mutableStyledString);
   8. })

   10. controller.setStyledString(paragraphStyledString);
   11. return controller;
   12. }
   ```

   [HandleData.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/common/HandleData.ets#L21-L33)

## 实现文本中的图片表情

### 场景描述

文本中的自定义emoji表情通常使用类似[哈哈]这样的字符进行传输，但在显示时会被替换为本地或网络图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/z1l2LU8ORMWTWKr6C1sVEw/zh-cn_image_0000002417234329.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=F4F268F208AEFBF65AAD3FF1771D94108912AC217F866AF11248180F62F8877B)

### 实现原理

文本中显示为表情图片，需要调整其样式设置，而无需编辑文本信息。以下是可选方案：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Cd6pvqOCS72uF1_ciXwZDQ/zh-cn_image_0000002383675048.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=15FAD508152902DD1D6793334C1A20D672F82EEB1FCC0FE2CF4368E542E12545 "点击放大")

可以先获取输入字符对应的图片，然后通过属性字符串[StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring)的[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)属性加载图片，并使用[UserDataSpan](../harmonyos-references/ts-universal-styled-string.md#userdataspan)属性存储自定义扩展信息。

### 开发步骤

1. 初始化声明文字和图片的对应关系。

   ```
   1. export const EMOJI_DATA: Map<string, Resource> = new Map([
   2. ["[哈哈]", $r('app.media.smile')]
   3. ]);
   ```

   [MockData.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/mock/MockData.ets#L22-L25)
2. 循环处理文本数据，并生成属性字符串。

   ```
   1. handleStyledString() {
   2. this.spans = EmojiMock;
   3. this.spans.forEach((span) => {
   4. this.handleEmoji(span);
   5. });

   7. this.controller = HandleData.handleStyledString(this.styledStrings);
   8. }
   ```

   [CustomizeEmoji.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/CustomizeEmoji.ets#L51-L59)
3. 将输入的文本转换为图片，使用[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)，设置图片资源和大小等。

   ```
   1. handleEmoji(span: MyCustomSpan) {
   2. this.styledStrings.push(new MutableStyledString(new ImageAttachment({
   3. resourceValue: EMOJI_DATA.get(span.content),
   4. size: {
   5. width: 16,
   6. height: 16
   7. }
   8. })));
   9. }
   ```

   [CustomizeEmoji.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/CustomizeEmoji.ets#L35-L44)
4. 将生成的属性信息拼接成属性字符串，并绑定到[Text](../harmonyos-references/ts-basic-components-text.md)组件以进行渲染显示。

   ```
   1. static handleStyledString(styledStrings: MutableStyledString[]): TextController {
   2. let controller: TextController = new TextController();
   3. let paragraphStyledString: MutableStyledString = new MutableStyledString('', []);

   5. // Append the attribute string generated for each text fragment to the attribute string paragraphStyledString
   6. styledStrings.forEach((mutableStyledString: MutableStyledString) => {
   7. paragraphStyledString.appendStyledString(mutableStyledString);
   8. })

   10. controller.setStyledString(paragraphStyledString);
   11. return controller;
   12. }
   ```

   [HandleData.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/common/HandleData.ets#L21-L33)

## 实现自定义的图文元素

### 场景描述

文中包含小图标与文本的组合，点击可跳转至详情页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/JQzZ1Q61Tl6TvKuy3BiDPA/zh-cn_image_0000002383515168.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=8EA24AA5D2A90E5547C405C09DC97D8A31095E7610C8AD2A5F69B761E2A77E58)

### 实现原理

文本中包含一个系统小图标和一段高亮显示的文字，点击可跳转至详情页面。选择方案如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/K3fCx2eARNaJlkhQleGQSQ/zh-cn_image_0000002417154473.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=F679F70A06BFB7DDD7B7C8ACCD10B8E72722ECA188D3FB478CB43536D91FEDED "点击放大")

需要自定义一个包含系统图标的超链接文本，可以通过属性字符串[StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring)中的[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)属性来加载系统图片，并通过[TextStyle](../harmonyos-references/ts-universal-styled-string.md#textstyle)属性设置来调整字体样式，点击事件则可以通过[GestureStyle](../harmonyos-references/ts-universal-styled-string.md#gesturestyle)属性来实现。

### 开发步骤

1. 初始化时通过[TextStyle](../harmonyos-references/ts-universal-styled-string.md#textstyle)属性定义文字样式，包括文字颜色、大小等。

   ```
   1. textAttribute: TextStyle = new TextStyle({
   2. fontColor: $r('app.color.styled_text_link_font_color'),
   3. fontSize: LengthMetrics.fp(14)
   4. });
   ```

   [VideoLink.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/VideoLink.ets#L34-L38)
2. 使用[GestureStyle](../harmonyos-references/ts-universal-styled-string.md#gesturestyle)属性定义点击超链接时的跳转事件。

   ```
   1. generateClickStyle(span: MyCustomSpan): GestureStyle {
   2. return new GestureStyle({
   3. onClick: () => {
   4. this.linkClickCallback(span);
   5. }
   6. })
   7. }
   ```

   [VideoLink.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/VideoLink.ets#L77-L84)
3. 实现点击跳转。

   ```
   1. private linkClickCallback: (span: MyCustomSpan) => void =
   2. (span: MyCustomSpan) => {
   3. // Process according to the type of text hyperlink.
   4. if (span) {
   5. let uiContext = this.getUIContext();
   6. let router = uiContext.getRouter();
   7. if (span.url !== null) {
   8. router.pushUrl({ url: span.url });
   9. }
   10. }
   11. };
   ```

   [VideoLink.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/VideoLink.ets#L114-L125)
4. 循环处理文本数据，并生成属性字符串。

   ```
   1. handleStyledString() {
   2. if (this.systemLanguage === 'zh-Hans') {
   3. this.spans = VideoLinkMock;
   4. } else {
   5. this.spans = VideoLinkMock_EN;
   6. }
   7. this.spans.forEach((span) => {
   8. if (span.url) {
   9. this.handleVideoLink(span);
   10. } else {
   11. this.styledStrings.push(new MutableStyledString(span.content, []));
   12. }
   13. });

   15. this.controller = HandleData.handleStyledString(this.styledStrings);
   16. }
   ```

   [VideoLink.ets](https://gitcode.com/harmonyos_samples/styledtext/blob/master/entry/src/main/ets/pages/VideoLink.ets#L91-L107)
5. 设置小图标、文本样式和点击事件。

   ```
   1. handleVideoLink(span: MyCustomSpan) {
   2. // If the pixelMap for the video link icon exists, add an image attachment styled string before the corresponding link
   3. this.styledStrings.push(new MutableStyledString(new ImageAttachment({
   4. resourceValue: $r('app.media.play_round_rectangle'),
   5. size: {
   6. width: $r('app.integer.styled_text_video_link_icon_size'),
   7. height: $r('app.integer.styled_text_video_link_icon_size')
   8. },
   9. verticalAlign: ImageSpanAlignment.CENTER,
   10. objectFit: ImageFit.Contain
   11. })));
   12. this.styledStrings.push(new MutableStyledString(span.content, [{
   13. start: 0,
   14. length: span.content.length,
   15. styledKey: StyledStringKey.GESTURE,
   16. styledValue: this.generateClickStyle(span)
   17. }, {
   18. start: 0,
   19. length: span.content.length,
   20. styledKey: StyledStringKey.FONT,
   21. styledValue: this.textAttribute
   22. }
   23. ]));
   24. }
   ```

   [VideoLink.ets](https://gitcode.com/harmonyos_samples/styledtext/blob/master/entry/src/main/ets/pages/VideoLink.ets#L44-L68)
6. 将生成的属性信息拼接成属性字符串，并绑定到[Text](../harmonyos-references/ts-basic-components-text.md)组件以进行渲染显示。

   ```
   1. static handleStyledString(styledStrings: MutableStyledString[]): TextController {
   2. let controller: TextController = new TextController();
   3. let paragraphStyledString: MutableStyledString = new MutableStyledString('', []);

   5. // Append the attribute string generated for each text fragment to the attribute string paragraphStyledString
   6. styledStrings.forEach((mutableStyledString: MutableStyledString) => {
   7. paragraphStyledString.appendStyledString(mutableStyledString);
   8. })

   10. controller.setStyledString(paragraphStyledString);
   11. return controller;
   12. }
   ```

   [HandleData.ets](https://gitcode.com/harmonyos_samples/styledtext/blob/master/entry/src/main/ets/common/HandleData.ets#L21-L33)

## 实现图标与文本的组合元素

### 场景描述

文中包含自定义的小图标与文本的组合。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/3p8hXU0KRymzl-Koji8MNA/zh-cn_image_0000002417234337.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=AEE0B52087F6B142AE0BE3BF3BEBA6FBD84690A82989C0AA674FC043F7148F7D)

### 实现原理

文本中包含一个小图标、文字和背景颜色的复杂样式。以下是选择方案：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/0XzMTzzsT4uSkoteFADa3g/zh-cn_image_0000002383675052.png?HW-CC-KV=V1&HW-CC-Date=20260428T001948Z&HW-CC-Expire=86400&HW-CC-Sign=F10AE55B281F240C59880A7A775E11D6C72D7DBDE37C196A39099BC52AE91959 "点击放大")

需要通过属性字符串[StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring)属性中的自定义[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)来进行绘制。

### 开发步骤

1. 创建自定义的[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)以绘制自定义样式。

   ```
   1. export class MyDrawCustomSpan extends CustomSpan {
   2. width: number = 0;
   3. word: string = "drawing";
   4. height: number = 10;
   5. systemLanguage: string = 'zh-Hans';
   6. color: string | undefined = undefined;
   7. gUIContext: UIContext | undefined = undefined;

   9. // ...

   11. // Draw
   12. onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
   13. let canvas = context.canvas;

   15. // Set brush
   16. const brush = new drawing.Brush();
   17. // ...

   19. // Calculate offset
   20. let _left = options.x - 50;
   21. if (this.systemLanguage !== 'zh-Hans') {
   22. _left = options.x - 40;
   23. }

   25. // Draw a rounded rectangle
   26. let rect: common2D.Rect = {
   27. left: _left,
   28. top: options.lineTop + 11,
   29. right: options.x + this.width,
   30. bottom: options.lineBottom
   31. };

   33. let roundRect = new drawing.RoundRect(rect, 10, 10);
   34. canvas.drawRoundRect(roundRect);
   35. // ...

   37. const font = new drawing.Font();
   38. font.setSize(40);
   39. const textBlob = drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
   40. canvas.attachBrush(brush);
   41. canvas.drawTextBlob(textBlob, options.x + 5, options.lineBottom - 10);
   42. canvas.detachBrush();
   43. }

   45. setWord(word: string) {
   46. this.word = word;
   47. }
   48. }
   ```

   [MyDrawCustomSpan.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/components/MyDrawCustomSpan.ets#L19-L121)
2. 循环处理文本数据，并生成属性字符串。

   ```
   1. handleStyledString() {
   2. if (this.systemLanguage === 'zh-Hans') {
   3. this.spans = ImageTextMock;
   4. } else {
   5. this.spans = ImageTextMock_EN;
   6. }
   7. this.spans.forEach((span) => {
   8. if (span.url) {
   9. this.handleImageText(span);
   10. } else {
   11. this.styledStrings.push(new MutableStyledString(span.content, []));
   12. }
   13. });

   15. this.controller = HandleData.handleStyledString(this.styledStrings);
   16. }
   ```

   [ImageText.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/ImageText.ets#L74-L90)
3. 设置自定义图文元素。

   ```
   1. handleImageText(span: MyCustomSpan) {
   2. let resourceStr = $r('app.media.doc_plaintext_green');
   3. // ...

   5. this.styledStrings.push(new MutableStyledString(new ImageAttachment({
   6. resourceValue: resourceStr,
   7. size: {
   8. width: 13,
   9. height: 13
   10. },
   11. layoutStyle: {
   12. margin: { top: 4 }
   13. },
   14. verticalAlign: ImageSpanAlignment.CENTER
   15. })));
   16. // Calculate the required width based on language
   17. let width = 15 + 40 * span.content.length;
   18. if (this.systemLanguage !== 'zh-Hans') {
   19. width = 25 + 21 * span.content.length;
   20. }
   21. this.styledStrings.push(new MutableStyledString(new MyDrawCustomSpan(span.content, width, 20,this.systemLanguage,
   22. span.url, gUIContext)));
   23. }
   ```

   [ImageText.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/pages/ImageText.ets#L40-L67)
4. 将生成的属性信息拼接成属性字符串，并绑定到[Text](../harmonyos-references/ts-basic-components-text.md)组件以进行渲染和显示。

   ```
   1. static handleStyledString(styledStrings: MutableStyledString[]): TextController {
   2. let controller: TextController = new TextController();
   3. let paragraphStyledString: MutableStyledString = new MutableStyledString('', []);

   5. // Append the attribute string generated for each text fragment to the attribute string paragraphStyledString
   6. styledStrings.forEach((mutableStyledString: MutableStyledString) => {
   7. paragraphStyledString.appendStyledString(mutableStyledString);
   8. })

   10. controller.setStyledString(paragraphStyledString);
   11. return controller;
   12. }
   ```

   [HandleData.ets](https://gitcode.com/HarmonyOS_Samples/styledtext/blob/master/entry/src/main/ets/common/HandleData.ets#L21-L33)

## 示例代码

* [实现富文本信息的显示](https://gitcode.com/harmonyos_samples/styledtext)
