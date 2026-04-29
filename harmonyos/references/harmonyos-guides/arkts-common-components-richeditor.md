---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor
title: 富文本编辑（RichEditor）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 富文本编辑（RichEditor）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:89401a1e402db64d4051a1abfcb54e97649cda864648c468d341982725c6cf4d
---

RichEditor是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。具体用法参考[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件的API文档。

对于仅需图文展示而不需要编辑的场景，建议使用[Text](../harmonyos-references/ts-basic-components-text.md)组件。

对于需要大量展示Html格式内容的场景，建议使用[RichText](../harmonyos-references/ts-basic-components-richtext.md)组件。

## 组件构成

下图展示了组件元素的构成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/bo-oEjmbQHWU5hnK9cn1YQ/zh-cn_image_0000002558764312.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=81DE195C54A8C37A132FABDDE9701F5B7E3FBEA34AADE41AB16B4CD4A054E5EE)

组件的元素构成包括：

| 元素 | 说明 |
| --- | --- |
| 内容区 | 内容可显示的区域。 |
| 光标 | 用于指明当前输入位置。 |
| 手柄 | 分为左手柄和右手柄，可分别进行拖动，用于调整文本选择区域范围。 |
| 菜单 | 选中内容后弹出，其中包含复制、粘贴等内容操作按钮。 |

## 创建RichEditor组件

开发者可以[创建基于属性字符串进行内容管理的RichEditor组件](arkts-common-components-richeditor.md#创建基于属性字符串进行内容管理的richeditor组件)或[创建基于Span进行内容管理的RichEditor组件](arkts-common-components-richeditor.md#创建基于span进行内容管理的richeditor组件)。

### 创建基于属性字符串进行内容管理的RichEditor组件

使用RichEditor(options: [RichEditorStyledStringOptions](../harmonyos-references/ts-basic-components-richeditor.md#richeditorstyledstringoptions12))接口可以创建基于属性字符串（[StyledString/MutableStyledString](arkts-styled-string.md)）进行内容管理的RichEditor组件。这种构建方式开发者可以通过在应用侧持有属性字符串对象来管理数据，通过修改属性字符串对象的内容、样式，再传递给组件，即可实现对富文本组件内容的更新。

相比于使用controller提供的接口进行内容样式更新，使用起来更加灵活便捷。同时属性字符串对象可以设置到各类支持属性字符串的文本组件中，可以快速实现内容的迁移。

```
1. @Entry
2. @Component
3. export struct CreateRichEditor {
4. // ...
5. fontStyle: TextStyle = new TextStyle({
6. fontColor: Color.Pink
7. })
8. // 定义字体样式对象
9. mutableStyledString: MutableStyledString =
10. // 请将$r('app.string.CreateRichEditor_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"创建使用属性字符串构建的RichEditor组件。"
11. new MutableStyledString(this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.CreateRichEditor_Text_1').id),
12. [{
13. start: 0,
14. length: 5,
15. styledKey: StyledStringKey.FONT,
16. styledValue: this.fontStyle
17. }])
18. // 创建属性字符串

20. controller: RichEditorStyledStringController = new RichEditorStyledStringController();
21. options: RichEditorStyledStringOptions = { controller: this.controller };
22. build() {
23. NavDestination() {
24. Column({ space: 12 }) {
25. Column({ space: 3 }) {
26. // ...
27. RichEditor(this.options)
28. .onReady(() => {
29. this.controller.setStyledString(this.mutableStyledString);
30. })
31. }
32. // ...
33. }
34. .width('100%')
35. .height('100%')
36. .padding({ left: 12, right: 12 })
37. }
38. .backgroundColor('#f1f2f3')
39. // 请将$r('app.string.Create_RichEditor_Component_title')替换为实际资源文件，在本示例中该资源文件的value值为"创建RichEditor组件"
40. .title($r('app.string.Create_RichEditor_Component_title'))
41. }
42. }
```

[CreateRichEditor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/CreateRichEditor.ets#L17-L111)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Sy0acW7MR5e69o7l7AMOXA/zh-cn_image_0000002558604656.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=3BCD30CBFF3540708646A73512C81A1CBC12A3EBE42E5A9FC5BBCAD8791EED29)

### 创建基于Span进行内容管理的RichEditor组件

使用RichEditor(value: [RichEditorOptions](../harmonyos-references/ts-basic-components-richeditor.md#richeditoroptions))接口可以创建基于Span进行内容管理的RichEditor组件，通常用于复杂内容场景，开发者通过RichEditorController提供的接口实现内容、样式的管理。

```
1. @Entry
2. @Component
3. export struct CreateRichEditor {
4. controllerNoStyledString: RichEditorController = new RichEditorController();
5. optionsNoStyledString: RichEditorOptions = { controller: this.controllerNoStyledString };
6. // ...
7. build() {
8. NavDestination() {
9. Column({ space: 12 }) {
10. // ...
11. Column({ space: 3 }) {
12. // ...
13. RichEditor(this.optionsNoStyledString)
14. .onReady(() => {
15. this.controllerNoStyledString.addTextSpan(
16. /**
17. * 请将$r('app.string.CreateRichEditor_Text_2')替换为实际资源文件，
18. * 在本示例中该资源文件的value值为"创建不使用属性字符串构建的RichEditor组件。"
19. */
20. $r('app.string.CreateRichEditor_Text_2'), {
21. style: {
22. fontColor: Color.Black,
23. fontSize: 15
24. }
25. })
26. })
27. }
28. // ...
29. }
30. .width('100%')
31. .height('100%')
32. .padding({ left: 12, right: 12 })
33. }
34. .backgroundColor('#f1f2f3')
35. // 请将$r('app.string.Create_RichEditor_Component_title')替换为实际资源文件，在本示例中该资源文件的value值为"创建RichEditor组件"
36. .title($r('app.string.Create_RichEditor_Component_title'))
37. }
38. }
```

[CreateRichEditor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/CreateRichEditor.ets#L16-L112)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ew-Dt18gQ9GPSBXojKcv-w/zh-cn_image_0000002589324181.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=FEC9DB6278306F87F1FACB07CF528033E04F592D7AE533FBB2C1555079C38E51)

## 添加内容

富文本组件可以通过不同的接口添加多种形式的内容。

### 添加文本内容

除了直接在组件内输入内容，也可以通过[addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)添加文本内容。

此接口可以实现文本样式多样化，例如创建混合样式文本。

如果组件是获焦状态并且光标在闪烁，那么通过addTextSpan添加文本内容后，光标位置会更新，在新添加文本内容的右侧闪烁。

```
1. @Entry
2. @Component
3. export struct AddTextContent {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };

7. build() {
8. // ...
9. RichEditor(this.options)
10. .onReady(() => {
11. // 请将$r('app.string.AddTextContent_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击按钮在此处添加text。"
12. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddTextContent_Text_1')), {
13. style: {
14. fontColor: Color.Black,
15. fontSize: 15
16. }
17. })
18. })
19. .border({ width: 1, color: Color.Gray })
20. .constraintSize({
21. maxHeight: 100
22. })
23. .width(300)
24. .margin(10)
25. // 请将$r('app.string.AddTextContent_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"addTextSpan"
26. Button($r('app.string.AddTextContent_Button_1'), {
27. buttonStyle: ButtonStyleMode.NORMAL
28. })
29. .height(30)
30. .fontSize(13)
31. .onClick(() => {
32. // 请将$r('app.string.AddTextContent_Text_2')替换为实际资源文件，在本示例中该资源文件的value值为"新添加一段文字。"
33. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddTextContent_Text_2')))
34. })
35. // ...
36. }
37. }
```

[AddTextContent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddTextContent.ets#L19-L70)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/sNDTgngeQ5ah4S2etLAgvg/zh-cn_image_0000002589244121.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=8FC14E45A65FCEC38B7AF7069C9879971A5E8EAA5196700DB72EBBED101A9DD4)

### 添加图片内容

通过[addImageSpan](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)添加图片内容。

此接口可用于内容丰富与可视化展示，例如在新闻中加入图片，在文档中加入数据可视化图形等。

如果组件是获焦状态并且光标在闪烁，那么通过addImageSpan添加图片内容后，光标位置会更新，在新添加图片内容的右侧闪烁。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.string.AddImageContent_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击按钮在此处添加image。"
7. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddImageContent_Text_1')), {
8. style: {
9. fontColor: Color.Black,
10. fontSize: 15
11. }
12. })
13. })
14. .width(300)
15. .height(100)
16. // 请将$r('app.string.AddImageContent_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"addImageSpan"
17. Button($r('app.string.AddImageContent_Button_1'), {
18. buttonStyle: ButtonStyleMode.NORMAL
19. })
20. .height(30)
21. .fontSize(13)
22. .onClick(() => {
23. // 请将$r('app.media.xxx')替换为实际资源文件
24. this.controller.addImageSpan($r('app.media.startIcon'), {
25. imageStyle: {
26. size: ['57px', '57px']
27. }
28. })
29. })
```

[AddImageContent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddImageContent.ets#L19-L70)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Yyi8f4TXR6-Jo831IxzlAQ/zh-cn_image_0000002558764314.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=C13F3FCE4F6807349D998B849624356C0439D493FA8B492C5218A1593BDA52BE)

### 添加@Builder装饰器修饰的内容

通过[addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)添加@Builder装饰器修饰的内容。

此接口可用于自定义复杂组件的嵌入，例如在组件内加入自定义图表。

该接口内可通过[RichEditorBuilderSpanOptions](../harmonyos-references/ts-basic-components-richeditor.md#richeditorbuilderspanoptions11)设置在组件中添加builder的位置，省略或者为异常值时，则添加builder到所有内容的最后位置。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. private myBuilder: CustomBuilder = undefined;

5. @Builder
6. TextBuilder() {
7. Row() {
8. Image($r('app.media.startIcon')).width(50).height(50).margin(16)
9. Column() {
10. // 请将$r('app.string.AddBuilderDecoratorContent_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"文本文档.txt"
11. Text($r('app.string.AddBuilderDecoratorContent_Text_1')).fontWeight(FontWeight.Bold).fontSize(16)
12. // 请将$r('app.string.AddBuilderDecoratorContent_Text_2')替换为实际资源文件，在本示例中该资源文件的value值为"123.45KB"
13. Text($r('app.string.AddBuilderDecoratorContent_Text_2')).fontColor('#8a8a8a').fontSize(12)
14. }.alignItems(HorizontalAlign.Start)
15. }.backgroundColor('#f4f4f4')
16. .borderRadius('20')
17. .width(220)
18. }
19. build() {
20. // ...
21. Column({ space: 12 }) {
22. RichEditor(this.options)
23. .onReady(() => {
24. this.controller.addTextSpan(
25. /*
26. * 请将$r('app.string.AddBuilderDecoratorContent_Text_3')替换为实际资源文件，
27. * 在本示例中该资源文件的value值为"点击按钮在此处添加builderspan。"
28. */
29. $r('app.string.AddBuilderDecoratorContent_Text_3'), {
30. style: {
31. fontColor: Color.Black,
32. fontSize: 15
33. }
34. })
35. })
36. Row() {
37. /*
38. * 请将$r('app.string.AddBuilderDecoratorContent_Button_1')替换为实际资源文件，
39. * 在本示例中该资源文件的value值为"addBuilderSpan"
40. */
41. Button($r('app.string.AddBuilderDecoratorContent_Button_1'), {
42. buttonStyle: ButtonStyleMode.NORMAL
43. })
44. .height(30)
45. .fontSize(13)
46. .onClick(() => {
47. this.myBuilder = () => {
48. this.TextBuilder()
49. }
50. this.controller.addBuilderSpan(this.myBuilder)
51. })
52. }.justifyContent(FlexAlign.Center).width('100%')
53. }
54. // ...
55. }
```

[AddBuilderDecoratorContent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddBuilderDecoratorContent.ets#L19-L83)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/4ichfG_XSjK5uc_d76IsDQ/zh-cn_image_0000002558604658.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=CBCFD1B642D8C83C7E8E80444B11858373032F06C0C856A7564C77C65CF0BF5D)

### 添加SymbolSpan内容

可通过[addSymbolSpan](../harmonyos-references/ts-basic-components-richeditor.md#addsymbolspan11)添加Symbol内容。此接口可用于特殊符号的添加，例如在编辑学术论文时，此接口可用于添加各种数学符号。

添加Symbol内容时，如果组件是获焦状态并且光标在闪烁，那么添加Symbol后，光标将移动到新插入Symbol的右侧。

Symbol内容暂不支持手势、复制、拖拽处理。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.string.AddSymbolSpanContent_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击按钮在此处添加symbol。"
7. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddSymbolSpanContent_Text_1')), {
8. style: {
9. fontColor: Color.Black,
10. fontSize: 15
11. }
12. })
13. })
14. .width(300)
15. .height(100)
16. // 请将$r('app.string.AddSymbolSpanContent_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"addSymbolSpan"
17. Button($r('app.string.AddSymbolSpanContent_Button_1'), {
18. buttonStyle: ButtonStyleMode.NORMAL
19. })
20. .height(30)
21. .fontSize(13)
22. .onClick(() => {
23. // 请将$r('sys.symbol.basketball_fill')替换为开发者所需的资源文件
24. this.controller.addSymbolSpan($r('sys.symbol.basketball_fill'), {
25. style: {
26. fontSize: 30
27. }
28. })
29. })
```

[AddSymbolSpanContent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddSymbolSpanContent.ets#L20-L71)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/uhLZpOI6RLSw4-c5wcIarQ/zh-cn_image_0000002589324183.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=00CD567EFB9DB5F3C380499ED7ACCC548280DB78BD62F70F213433EB34051385)

## 管理内容

富文本组件可以通过接口对内容进行管理，例如[获取组件内的图文信息](arkts-common-components-richeditor.md#获取组件内图文信息)、[设置无输入时的提示文本](arkts-common-components-richeditor.md#设置无输入时的提示文本)或[设置组件内容的最大字符数](arkts-common-components-richeditor.md#设置最大长度)。

### 获取组件内图文信息

可通过[getSpans](../harmonyos-references/ts-basic-components-richeditor.md#getspans)获取组件内所有图文内容的信息，包括图文的内容、id、样式、位置等信息。获取内容位置信息后，可对指定范围内容进行样式的更新。

此接口适用于已有的内容样式获取与检查，例如在模板应用场景下，可利用此接口获取文本样式。此外，它还适用于内容解析与处理，例如在文本分析应用中，此接口能够获取特定范围内的文本信息。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. infoShowController: RichEditorController = new RichEditorController();
4. infoShowOptions: RichEditorOptions = { controller: this.infoShowController };
5. // 创建两个富文本组件
6. // ...
7. RichEditor(this.options)
8. .onReady(() => {
9. this.controller.addTextSpan(
10. // 请将$r('app.string.GetGraphicInfoInComponent_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击按钮获取此处span信息。"
11. resource.resourceToString($r('app.string.GetGraphicInfoInComponent_Text_1')), {
12. style: {
13. fontColor: Color.Black,
14. fontSize: 15
15. }
16. })
17. })
18. .width(300)
19. .height(50)
20. // 请将$r('app.string.GetGraphicInfoInComponent_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击按钮获取此处span信息。"
21. Text($r('app.string.GetGraphicInfoInComponent_Text_1')).fontSize(10).fontColor(Color.Gray).width(300);
22. RichEditor(this.infoShowOptions)
23. .width(300)
24. .height(50)
25. // 请将$r('app.string.GetGraphicInfoInComponent_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"getSpans"
26. Button($r('app.string.GetGraphicInfoInComponent_Button_1'), {
27. buttonStyle: ButtonStyleMode.NORMAL
28. })
29. .height(30)
30. .fontSize(13)
31. .onClick(() => {
32. this.infoShowController.addTextSpan(JSON.stringify(this.controller.getSpans()), {
33. style: {
34. fontColor: Color.Gray,
35. fontSize: 10
36. }
37. })
38. })
```

[GetGraphicInfoInComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/GetGraphicInfoInComponent.ets#L15-L78)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/cNw9uNjwT-eKQnEPIXzrdg/zh-cn_image_0000002589244123.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=A5E2781CDBDE6641917495BDFA07EC032AE18F1C09585C10F38F7A75B67432CB)

### 设置无输入时的提示文本

通过[placeholder](../harmonyos-references/ts-basic-components-richeditor.md#placeholder12)设置无输入时的提示文本。

例如，在用户登录界面采用提示文本，有助于用户区分用户名与密码的输入框。又如，在文本编辑框中，使用提示文本明确输入要求，如“限输入100字以内”，以此指导用户正确操作。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. // 请将$r('app.string.SetAttributes_Text_6')替换为实际资源文件，在本示例中该资源文件的value值为"此处为提示文本..."
6. .placeholder(resource.resourceToString($r('app.string.SetAttributes_Text_6')), {
7. fontColor: Color.Gray,
8. font: {
9. size: 15,
10. weight: FontWeight.Normal,
11. family: 'HarmonyOS Sans',
12. style: FontStyle.Normal
13. }
14. })
15. .width(300)
16. .height(50)
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L204-L243)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/b_Ag3GW_RZqJQaIoucpJhQ/zh-cn_image_0000002558764316.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=774357C827A8007F25726A9C0BC13C804CB98967C14F0B64BF28C1352C866871)

### 设置最大长度

通过[maxLength](../harmonyos-references/ts-basic-components-richeditor.md#maxlength18)可以设置富文本的最大可输入字符数。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. // 请将$r('app.string.SetAttributes_Text_8')替换为实际资源文件，在本示例中该资源文件的value值为"组件设置了最大字符数：7"
6. .placeholder(resource.resourceToString($r('app.string.SetAttributes_Text_8')))
7. .maxLength(7)
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L294-L326)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/VAFVRof6SMGQi-ZYvLMD1g/zh-cn_image_0000002558604660.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=6C1D49BC860D2BA1B91818D4C65332E777020C52632F99AAB19A3C84BACFB84C)

## 事件回调

开发者可以通过注册事件回调，感知组件事件的触发。

### 添加图文变化前和图文变化后可触发的回调

通过[onWillChange](../harmonyos-references/ts-basic-components-richeditor.md#onwillchange12)添加图文变化前可触发的回调。此回调适用于用户实时数据校验与提醒，例如在用户输入文本时，可在回调内实现对输入内容的检测，若检测到敏感词汇，应立即弹出提示框。此外，它还适用于实时字数统计与限制，对于有字数限制的输入场景，可在回调中实时统计用户输入的字数，并在接近字数上限时提供相应的提示。

通过[onDidChange](../harmonyos-references/ts-basic-components-richeditor.md#ondidchange12)添加图文变化后可触发的回调。此回调适用于内容保存与同步，例如在用户完成内容编辑后，可使用该回调自动将最新内容保存至本地或同步至服务器。此外，它还适用于内容状态更新与渲染，例如在待办事项列表应用中，用户编辑富文本格式的待办事项描述后，可使用该回调更新待办事项在列表中的显示样式。

使用[RichEditorStyledStringOptions](../harmonyos-references/ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持上述两种回调。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };

4. infoShowController: RichEditorController = new RichEditorController();
5. infoShowOptions: RichEditorOptions = { controller: this.infoShowController };
6. // ...
7. RichEditor(this.options)
8. .onReady(() => {
9. // 请将$r('app.string.AddEvent_Text_5')替换为实际资源文件，在本示例中该资源文件的value值为"组件内图文变化前，触发回调。\n图文变化后，触发回调。"
10. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_5')), {
11. style: {
12. fontColor: Color.Black,
13. fontSize: 15
14. }
15. })
16. })
17. .onWillChange((value: RichEditorChangeValue) => {
18. // 请将$r('app.string.AddEvent_Text_6')替换为实际资源文件，在本示例中该资源文件的value值为"组件内图文变化前，触发回调：\"
19. this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_6')) +
20. JSON.stringify(value), {
21. style: {
22. fontColor: Color.Gray,
23. fontSize: 10
24. }
25. })
26. return true;
27. })
28. .onDidChange((rangeBefore: TextRange, rangeAfter: TextRange) => {
29. // 请将$r('app.string.AddEvent_Text_7')替换为实际资源文件，在本示例中该资源文件的value值为"\n图文变化后，触发回调：\n rangeBefore"
30. this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_7')) +
31. JSON.stringify(rangeBefore) + '\nrangeAfter: ' + JSON.stringify(rangeBefore), {
32. style: {
33. fontColor: Color.Gray,
34. fontSize: 10
35. }
36. })
37. })
38. .width(300)
39. .height(50);
40. // 请将$r('app.string.AddEvent_Text_4')替换为实际资源文件，在本示例中该资源文件的value值为"查看回调内容："
41. Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300);
42. RichEditor(this.infoShowOptions)
43. .width(300)
44. .height(70);
```

[AddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddEvent.ets#L109-L179)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/er9pqp_gRZ6C5ZIwaSQwKg/zh-cn_image_0000002589324185.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=AF0845255C433B5858D1E9B3ECDD0063AEA4F73E68BE64F5F1D7C02CE7948B05)

### 添加输入法输入内容前和完成输入后可触发的回调

添加输入法输入内容前和完成输入后可触发的回调。

在添加输入法输入内容前，可以通过[aboutToIMEInput](../harmonyos-references/ts-basic-components-richeditor.md#abouttoimeinput)触发回调。在输入法完成输入后，可以通过[onDidIMEInput](../harmonyos-references/ts-basic-components-richeditor.md#ondidimeinput12)触发回调。

这两种回调机制适用于文本上屏过程的业务逻辑处理。例如：在用户输入的文本上屏前，利用回调提供联想词汇，在用户完成输入后，执行自动化纠错或格式转换。两种回调的时序依次为：aboutToIMEInput、onDidIMEInput。

使用[RichEditorStyledStringOptions](../harmonyos-references/ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的组件不支持上述两种回调功能。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };

4. infoShowController: RichEditorController = new RichEditorController();
5. infoShowOptions: RichEditorOptions = { controller: this.infoShowController };
6. // ...
7. // 请将$r('app.string.xxx')替换为开发者所需的资源文件
8. RichEditor(this.options)
9. .onReady(() => {
10. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_8')), {
11. style: {
12. fontColor: Color.Black,
13. fontSize: 15
14. }
15. })
16. })
17. .aboutToIMEInput((value: RichEditorInsertValue) => {
18. this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_9')) +
19. JSON.stringify(value), {
20. style: {
21. fontColor: Color.Gray,
22. fontSize: 10
23. }
24. })
25. return true;
26. })
27. .onDidIMEInput((value: TextRange) => {
28. this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_10')) +
29. JSON.stringify(value), {
30. style: {
31. fontColor: Color.Gray,
32. fontSize: 10
33. }
34. })
35. })
36. .width(300)
37. .height(50)
38. Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300)
39. RichEditor(this.infoShowOptions)
40. .width(300)
41. .height(70)
```

[AddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddEvent.ets#L184-L252)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/6r6tl87-QoirNe2zVYcU7A/zh-cn_image_0000002589244125.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=CE3A88FF0AA719698CF2FC106FBA64DDB59805A5106F5AA23995385AA310CD24)

### 添加完成粘贴前可触发的回调

通过[onPaste](../harmonyos-references/ts-basic-components-richeditor.md#onpaste11)回调，来添加粘贴前要处理的流程。

此回调适用于内容格式的处理。例如，当用户复制包含HTML标签的文本时，可在回调中编写代码，将其转换为富文本组件所支持的格式，同时剔除不必要的标签或仅保留纯文本内容。

由于组件默认的粘贴行为仅限于纯文本，无法处理图片粘贴，开发者可利用此方法实现图文并茂的粘贴功能，从而替代组件原有的粘贴行为。

```
1. import { pasteboard } from '@kit.BasicServicesKit';
2. // ...
3. @Component
4. struct on_cut_copy_paste {
5. controller: RichEditorController = new RichEditorController();
6. options: RichEditorOptions = { controller: this.controller };
7. infoShowController: RichEditorController = new RichEditorController();
8. infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

10. PopDataFromPasteboard() {
11. let selection = this.controller.getSelection();
12. let start = selection.selection[0];
13. let end = selection.selection[1];
14. if (start == end) {
15. start = this.controller.getCaretOffset();
16. end = this.controller.getCaretOffset();
17. }
18. let moveOffset = 0;
19. let sysBoard = pasteboard.getSystemPasteboard();
20. sysBoard.getData((err, data) => {
21. if (err) {
22. return;
23. }
24. if (start != end) {
25. this.controller.deleteSpans({ start: start, end: end });
26. }
27. let count = data.getRecordCount();
28. for (let i = 0; i < count; i++) {
29. const element = data.getRecord(i);
30. if (element && element.plainText && element.mimeType === pasteboard.MIMETYPE_TEXT_PLAIN) {
31. this.controller.addTextSpan(element.plainText,
32. {
33. style: { fontSize: 26, fontColor: Color.Red },
34. offset: start + moveOffset
35. }
36. )
37. moveOffset += element.plainText.length;
38. }
39. }
40. this.controller.setCaretOffset(start + moveOffset);
41. });
42. }

44. build() {
45. Column() {
46. ComponentCard({
47. // 请将$r('app.string.Add_Event_title_5')替换为实际资源文件，在本示例中该资源文件的value值为"添加完成粘贴前可触发的回调"
48. title: $r('app.string.Add_Event_title_5'),
49. // 请将$r('app.string.Add_Event_title_5_desc')替换为实际资源文件，在本示例中该资源文件的value值为"通过onPaste回调，来添加粘贴前要处理的流程"
50. description: $r('app.string.Add_Event_title_5_desc')
51. }) {
52. Column({ space: 3 }) {
53. RichEditor(this.options)
54. .onReady(() => {
55. // 请将$r('app.string.AddEvent_Text_11')替换为实际资源文件，在本示例中该资源文件的value值为"对此处文本进行复制粘贴操作可触发对应回调。"
56. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_11')),
57. { style: { fontColor: Color.Black, fontSize: 15 } })
58. })
59. .onPaste((event) => {
60. // 请将$r('app.string.AddEvent_Text_12')替换为实际资源文件，在本示例中该资源文件的value值为"触发onPaste回调\n"
61. this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_12')),
62. { style: { fontColor: Color.Gray, fontSize: 10 } })
63. if (event != undefined && event.preventDefault) {
64. event.preventDefault();
65. }
66. this.PopDataFromPasteboard()
67. })
68. .width(300)
69. .height(50);
70. // 请将$r('app.string.AddEvent_Text_4')替换为实际资源文件，在本示例中该资源文件的value值为"查看回调内容："
71. Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300);
72. RichEditor(this.infoShowOptions)
73. .width(300)
74. .height(70);
75. }.width('100%').alignItems(HorizontalAlign.Start);
76. }
77. }
78. }
79. }
```

[AddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddEvent.ets#L17-L346)

### 添加完成剪切前可触发的回调

通过[onCut](../harmonyos-references/ts-basic-components-richeditor.md#oncut12)回调，来添加剪切前要处理的流程。

此回调功能适用于数据处理与存储。例如，当用户从富文本组件中剪切内容时，可在回调中临时存储被剪切的内容，确保后续的粘贴操作能够准确无误地还原内容。

由于组件默认的剪切行为仅限于纯文本，无法处理图片剪切，开发者可利用此方法实现图文并茂的剪切功能，从而替代组件原有的剪切行为。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };

4. infoShowController: RichEditorController = new RichEditorController();
5. infoShowOptions: RichEditorOptions = { controller: this.infoShowController };
6. // ...
7. RichEditor(this.options)
8. .onReady(() => {
9. // 请将$r('app.string.AddEvent_Text_13')替换为实际资源文件，在本示例中该资源文件的value值为"对此处文本进行复制粘贴操作可触发对应回调。"
10. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_13')), {
11. style: {
12. fontColor: Color.Black,
13. fontSize: 15
14. }
15. })
16. })
17. .onCut(() => {
18. // 请将$r('app.string.AddEvent_Text_14')替换为实际资源文件，在本示例中该资源文件的value值为"触发onCut回调\n"
19. this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_14')), {
20. style: {
21. fontColor: Color.Gray,
22. fontSize: 10
23. }
24. })
25. })
26. .width(300)
27. .height(70)
28. RichEditor(this.infoShowOptions)
29. .width(300)
30. .height(70)
```

[AddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddEvent.ets#L350-L405)

### 添加完成复制前可触发的回调

通过[onCopy](../harmonyos-references/ts-basic-components-richeditor.md#oncopy12)回调，来添加复制前要处理的流程。

此回调适用于内容的备份与共享，例如在用户复制内容时，可在回调中执行以下操作：将复制的内容及其格式信息保存至本地备份文件夹，或自动生成一段包含复制内容及产品购买链接的分享文案，以方便用户进行粘贴和分享。

组件默认的复制行为仅限于纯文本，无法处理图片。开发者可利用此方法实现图文并茂的复制功能，替代组件的默认行为。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };

4. infoShowController: RichEditorController = new RichEditorController();
5. infoShowOptions: RichEditorOptions = { controller: this.infoShowController };
6. // ...
7. RichEditor(this.options)
8. .onReady(() => {
9. // 请将$r('app.string.AddEvent_Text_15')替换为实际资源文件，在本示例中该资源文件的value值为"对此处文本进行复制粘贴操作可触发对应回调。"
10. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_15')), {
11. style: {
12. fontColor: Color.Black,
13. fontSize: 15
14. }
15. })
16. })
17. .onCopy(() => {
18. // 请将$r('app.string.AddEvent_Text_16')替换为实际资源文件，在本示例中该资源文件的value值为"触发onCopy回调\n"
19. this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_16')), {
20. style: {
21. fontColor: Color.Gray,
22. fontSize: 10
23. }
24. })
25. })
26. .width(300)
27. .height(50)
28. RichEditor(this.infoShowOptions)
29. .width(300)
30. .height(70)
```

[AddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddEvent.ets#L410-L466)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/MpvVNBCOReCI6Et_5SH_1g/zh-cn_image_0000002558764318.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=E399B36788FBCC3DC7382FA5ED5E9E424DDAFB87E0FA946FDDD0B6E96E321EE9)

更多事件使用请参考[RichEditor事件](../harmonyos-references/ts-basic-components-richeditor.md#事件)。

## 组件交互

可以通过接口配置交互元素属性，感知交互元素变化。

### 设置输入框光标和手柄的颜色

通过[caretColor](../harmonyos-references/ts-basic-components-richeditor.md#caretcolor12)设置输入框光标和手柄的颜色。

设置不同颜色的光标和手柄可以提高视觉辨识度，特别是在包含多个输入区域的复杂界面中，独特的光标颜色能帮助快速定位当前操作的输入区域。这一特性也可以提升用户体验，使光标颜色与应用页面整体的风格相协调。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.string.SetAttributes_Text_5')替换为实际资源文件，在本示例中该资源文件的value值为"组件设置了光标手柄颜色。"
7. this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes_Text_5')), {
8. style: {
9. fontColor: Color.Black,
10. fontSize: 15
11. }
12. })
13. })
14. .caretColor(Color.Orange)
15. .width(300)
16. .height(300)
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L158-L199)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/O6nuu-P1TzOzOwQiPb4tmQ/zh-cn_image_0000002558604662.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=D8A40104B5340BC6D3F4CDAF538759EE7987DD76893F3697C5DB397FCC2753DC)

### 添加组件内容选择区域或编辑状态下光标位置改变时可触发的回调

通过[onSelectionChange](../harmonyos-references/ts-basic-components-richeditor.md#onselectionchange12)来添加组件内容选择区域或编辑状态下光标位置改变时可触发的回调。

该回调可用于实时监听组件内容选中区域变化，例如实现实时更新工具栏状态（显示字体、段落格式等）、统计选中内容长度或生成选中内容摘要。实时响应选中状态，动态联动交互元素，提升富文本编辑的操作反馈体验和功能的灵活性。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };

4. infoShowController: RichEditorController = new RichEditorController();
5. infoShowOptions: RichEditorOptions = { controller: this.infoShowController };
6. // ...
7. // 请将$r('app.string.xxx')替换为实际资源文件
8. RichEditor(this.options)
9. .onReady(() => {
10. this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_2')), {
11. style: {
12. fontColor: Color.Black,
13. fontSize: 15
14. }
15. })
16. })
17. .onSelectionChange((value: RichEditorRange) => {
18. this.infoShowController.addTextSpan('\n' + resource.resourceToString($r('app.string.AddEvent_Text_3')) +
19. value.start + ',' + value.end + ')', {
20. style: {
21. fontColor: Color.Gray,
22. fontSize: 10
23. }
24. })
25. })
26. .width(300)
27. .height(50)
28. Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300)
29. RichEditor(this.infoShowOptions)
30. .width(300)
31. .height(70)
```

[AddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/AddEvent.ets#L51-L104)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/5BYoD_VGQq60gX8MT8cK1g/zh-cn_image_0000002589324187.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=4DC7054DFB283065C31E4B10F4014BE2CEABD50BBADD92F05ACBB35C46244F21)

### 设置内容选中区范围

通过[setSelection](../harmonyos-references/ts-basic-components-richeditor.md#setselection11)设置组件内的内容选中时部分背板高亮。

此接口可用于实现文本聚焦效果，例如当用户点击某个文本段落的标题或摘要时，可通过该接口自动选中并高亮出对应正文内容。

当组件内未获焦出现光标时，调用该接口不产生选中效果。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.string.BackplaneHighlighting_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击按钮在此处选中0-2位置的文本。"
7. this.controller.addTextSpan(resource.resourceToString($r('app.string.BackplaneHighlighting_Text_1')), {
8. style: {
9. fontColor: Color.Black,
10. fontSize: 15
11. }
12. })
13. })
14. .width(300)
15. .height(60)
16. // 请将$r('app.string.BackplaneHighlighting_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"setSelection(0,2)"
17. Button($r('app.string.BackplaneHighlighting_Button_1'), {
18. buttonStyle: ButtonStyleMode.NORMAL
19. })
20. .height(30)
21. .fontSize(13)
22. .onClick(() => {
23. this.controller.setSelection(0, 2)
24. })
```

[BackplaneHighlighting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/BackplaneHighlighting.ets#L20-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/DsUavnPgQli6S0PrKZsQ0A/zh-cn_image_0000002589244127.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=0473BACCCCB967A6D687E335829373D6CD41A3C2B4311DA745B46F8542E3051F)

## 菜单配置

通过接口可以对文本选择菜单进行配置。

### 管理选中菜单项

当富文本选择区域变化后显示菜单之前触发[onPrepareMenu](../harmonyos-references/ts-text-common.md#属性-1)回调，可在该回调中进行菜单数据设置。

```
1. @Component
2. struct PrepareMenu {
3. controller: RichEditorController = new RichEditorController();
4. options: RichEditorOptions = { controller: this.controller };
5. @State endIndex: number | undefined = 0;
6. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
7. const idsToFilter = [
8. TextMenuItemId.TRANSLATE,
9. TextMenuItemId.SHARE,
10. TextMenuItemId.SEARCH,
11. TextMenuItemId.AI_WRITER
12. ]
13. const items = menuItems.filter(item => !idsToFilter.some(id => id.equals(item.id)));
14. // 请将$r('app.media.xxx')替换为实际资源文件
15. let item1: TextMenuItem = {
16. content: 'create1',
17. icon: $r('app.media.startIcon'),
18. id: TextMenuItemId.of('create1'),
19. }
20. let item2: TextMenuItem = {
21. content: 'create2',
22. id: TextMenuItemId.of('create2'),
23. icon: $r('app.media.startIcon'),
24. }
25. items.push(item1);
26. items.unshift(item2);
27. return items;
28. }

30. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
31. if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
32. return true;
33. }
34. if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
35. return true;
36. }
37. if (menuItem.id.equals(TextMenuItemId.COPY)) {
38. return true;
39. }
40. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
41. return false;
42. }
43. return false;
44. }

46. onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
47. // 请将$r('app.media.xxx')替换为实际资源文件
48. let item1: TextMenuItem = {
49. content: 'prepare1_' + this.endIndex,
50. icon: $r('app.media.startIcon'),
51. id: TextMenuItemId.of('prepare1'),
52. };
53. menuItems.unshift(item1);
54. return menuItems;
55. }

57. @State editMenuOptions: EditMenuOptions = {
58. onCreateMenu: this.onCreateMenu,
59. onMenuItemClick: this.onMenuItemClick,
60. onPrepareMenu: this.onPrepareMenu
61. };

63. build() {
64. Column() {
65. // ...
66. RichEditor(this.options)
67. .onReady(() => {
68. this.controller.addTextSpan('RichEditor editMenuOptions');
69. })
70. .editMenuOptions(this.editMenuOptions)
71. .onSelectionChange((range: RichEditorRange) => {
72. this.endIndex = range.end;
73. })
74. .height(50)
75. .margin({ top: 100 })
76. .borderWidth(1)
77. .borderColor(Color.Red)
78. // ...
79. }.alignItems(HorizontalAlign.Start)
80. .backgroundColor('#fff')
81. .borderRadius(12)
82. .padding(12)
83. .width('100%')
84. }
85. }
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L582-L683)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/pxqxzUocRIqNFDM33hJg2w/zh-cn_image_0000002558764320.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=0A4031CE68354E44075E86FD5300FCCA216F6E6F4B157D0C3AD8EB5207B0646C)

### 屏蔽系统服务类菜单项

通过[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)屏蔽富文本选择菜单内所有系统服务菜单项。

此接口保护内容安全，适用于限制文本操作的场景，例如展示保密内容或禁止复制的版权文本。屏蔽系统服务菜单项，防止用户通过系统服务菜单复制、分享文本，降低内容泄露风险。

```
1. import { TextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. export struct DisableSystemServiceMenu {
6. controller: RichEditorController = new RichEditorController();
7. options: RichEditorOptions = { controller: this.controller };

9. aboutToAppear(): void {
10. // 禁用所有系统服务菜单
11. TextMenuController.disableSystemServiceMenuItems(true);
12. }

14. aboutToDisappear(): void {
15. // 页面消失恢复系统服务菜单
16. TextMenuController.disableSystemServiceMenuItems(false);
17. }

19. build() {
20. // ...
21. RichEditor(this.options).onReady(() => {
22. // 请将$r('app.string.Demo_richEditor')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个RichEditor"
23. this.controller.addTextSpan($r('app.string.Demo_richEditor'),
24. {
25. style:
26. {
27. fontSize: 30
28. }
29. })
30. })
31. .height(60)
32. .editMenuOptions({
33. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
34. // menuItems不包含被屏蔽的系统菜单项
35. return menuItems;
36. },
37. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
38. return false;
39. }
40. })
41. // ...
42. }
43. }
```

[DisableSystemServiceMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/DisableSystemServiceMenu.ets#L16-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/BUy-5heMRCquV10kSvp3UA/zh-cn_image_0000002558604664.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=4C43DB66C7F4035D4DC58FC675A17093820FF5A0EF640CC0EE550482CB55B0A9)

通过[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)可以屏蔽富文本选择菜单内指定的系统服务菜单项。

此接口可精确屏蔽指定的系统服务菜单项，保留应用所需的系统菜单功能，使菜单更贴合实际交互设计。

```
1. import { TextMenuController } from '@kit.ArkUI';

4. @Entry
5. @Component
6. export struct DisableMenuItem {
7. controller: RichEditorController = new RichEditorController();
8. options: RichEditorOptions = { controller: this.controller };

10. aboutToAppear(): void {
11. // 禁用搜索和翻译菜单
12. TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE]);
13. }

15. aboutToDisappear(): void {
16. // 恢复系统服务菜单
17. TextMenuController.disableMenuItems([]);
18. }

20. build() {
21. // ...
22. RichEditor(this.options)
23. .onReady(() => {
24. // 请将$r('app.string.Demo_richEditor')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个RichEditor"
25. this.controller.addTextSpan($r('app.string.Demo_richEditor'), {
26. style: {
27. fontSize: 30
28. }
29. })
30. })
31. .height(60)
32. .editMenuOptions({
33. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
34. // menuItems不包含搜索和翻译
35. return menuItems;
36. },
37. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
38. return false;
39. }
40. })
41. // ...
42. }
43. }
```

[DisableMenuItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/DisableMenuItem.ets#L16-L74)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/EBXmEP8FQ2CySCzDzt6vCQ/zh-cn_image_0000002589324189.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=DD75C2E16DF994CDA234B5534D40FEA41F1E3189E0F2D56042DE48D7DD60EB80)

### 设置自定义选择菜单

通过[bindSelectionMenu](../harmonyos-references/ts-basic-components-richeditor.md#bindselectionmenu)设置自定义选择菜单。

组件原本具有默认的文本选择菜单，包含复制、剪切和全选的功能。用户可使用该属性设定自定义菜单，例如翻译英文、加粗字体等丰富的菜单功能。

当自定义菜单超长时，建议内部嵌套Scroll组件使用，避免键盘被遮挡。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. sliderShow: boolean = false;
4. private theme: SelectionMenuTheme = defaultTheme;

6. build() {
7. Column() {
8. ComponentCard({
9. // 请将$r('app.string.Set_Attributes_title_1')替换为实际资源文件，在本示例中该资源文件的value值为"设置自定义选择菜单"
10. title: $r('app.string.Set_Attributes_title_1'),
11. // 请将$r('app.string.Set_Attributes_title_1_desc')替换为实际资源文件，在本示例中该资源文件的value值为"通过bindSelectionMenu设置自定义选择菜单"
12. description: $r('app.string.Set_Attributes_title_1_desc'),
13. }) {
14. RichEditor(this.options)
15. .onReady(() => {
16. // 请将$r('app.string.SetAttributes_Text_4')替换为实际资源文件，在本示例中该资源文件的value值为"组件设置了自定义菜单，长按可触发。"
17. this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes_Text_4')), {
18. style: {
19. fontColor: Color.Black,
20. fontSize: 18
21. }
22. })
23. })
24. .bindSelectionMenu(RichEditorSpanType.TEXT, this.SystemMenu, ResponseType.LongPress, {
25. onDisappear: () => {
26. this.sliderShow = false
27. }
28. })
29. // 绑定自定义菜单
30. .width(300)
31. .height(300)
32. }
33. }
34. }

36. @Builder
37. SystemMenu() {
38. Column() {
39. Menu() {
40. if (this.controller) {
41. MenuItemGroup() {
42. MenuItem({
43. startIcon: this.theme.cutIcon,
44. // 请将$r('app.string.SetAttributes_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"剪切"
45. content: resource.resourceToString($r('app.string.SetAttributes_Text_1')),
46. labelInfo: 'Ctrl+X'
47. })
48. MenuItem({
49. startIcon: this.theme.copyIcon,
50. // 请将$r('app.string.SetAttributes_Text_2')替换为实际资源文件，在本示例中该资源文件的value值为"复制"
51. content: resource.resourceToString($r('app.string.SetAttributes_Text_2')),
52. labelInfo: 'Ctrl+C'
53. })
54. MenuItem({
55. startIcon: this.theme.pasteIcon,
56. // 请将$r('app.string.SetAttributes_Text_3')替换为实际资源文件，在本示例中该资源文件的value值为"粘贴"
57. content: resource.resourceToString($r('app.string.SetAttributes_Text_3')),
58. labelInfo: 'Ctrl+V'
59. })
60. }
61. }
62. }
63. .radius(this.theme.containerBorderRadius)
64. .clip(true)
65. .backgroundColor(Color.White)
66. .width(this.theme.defaultMenuWidth)
67. }
68. .width(this.theme.defaultMenuWidth)
69. }
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L70-L153)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/kFVZCWosSg-qVoReZ4j4gA/zh-cn_image_0000002589244129.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=54C1AA5A0D6E78002E9354143603B06E050755BC88A19D451C20F112081A6D10)

## 布局配置

组件支持通过接口配置布局规则，开发者可以根据业务场景定制合适的布局规则。

### 设置最大行数

通过[maxLines](../harmonyos-references/ts-basic-components-richeditor.md#maxlines18)可以设置富文本组件内可显示文本的最大行数。

此接口控制组件内文本的显示范围，防止文本过长影响页面布局，确保不同设备和场景下的文本显示效果一致，提升界面兼容性和美观度。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };

4. build() {
5. Column() {
6. // ...
7. /*
8. * 请将$r('app.string.SetAttributes_Text_7')替换为实际资源文件，在本示例中该资源文件的
9. * value值为"组件设置了最大行数\n超出内容将会以滚动显示\n超出1行\n超出2行\n超出3行\n超出4行"
10. */
11. RichEditor(this.options)
12. .onReady(() => {
13. this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes_Text_7')),
14. {
15. style: {
16. fontColor: Color.Black,
17. fontSize: 15
18. }
19. })
20. })
21. .maxLines(2)
22. // ...
23. }.alignItems(HorizontalAlign.Start)
24. .backgroundColor('#fff')
25. .borderRadius(12)
26. .padding(12)
27. .width('100%')
28. }
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L248-L289)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/jvPoJjGxQe6qtkBaXFXA9g/zh-cn_image_0000002558764322.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=AE887578DC45A8673CA3DA929290715AE11F9BEB379488E32B119A91D77F8D97)

## 样式设置

组件支持对内容设置复杂的样式。

### 设置用户预设的文本样式

通过[setTypingStyle](../harmonyos-references/ts-basic-components-richeditor.md#settypingstyle11)可以设置用户预设的文本样式。

此接口可用于个性化的写作体验，例如可以使用此接口让输入的不同层级标题自动应用相应格式（如一级、二级标题）。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.string.SetUserPresetTextStyles_Text_1')替换为实际资源文件，在本示例中该资源文件的value值为"点击按钮，改变预设文本样式。"
7. this.controller.addTextSpan(resource.resourceToString($r('app.string.SetUserPresetTextStyles_Text_1')),
8. {
9. style: {
10. fontColor: Color.Black,
11. fontSize: 15
12. }
13. })
14. })
15. .width(300)
16. .height(60)
17. // 请将$r('app.string.SetUserPresetTextStyles_Button_1')替换为实际资源文件，在本示例中该资源文件的value值为"setTypingStyle"
18. Button($r('app.string.SetUserPresetTextStyles_Button_1'), {
19. buttonStyle: ButtonStyleMode.NORMAL
20. })
21. .height(30)
22. .fontSize(13)
23. .onClick(() => {
24. this.controller.setTypingStyle({
25. fontWeight: 'medium',
26. fontColor: Color.Pink,
27. fontSize: 15,
28. fontStyle: FontStyle.Italic,
29. decoration: {
30. type: TextDecorationType.Underline,
31. color: Color.Gray
32. }
33. })
34. })
```

[SetUserPresetTextStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetUserPresetTextStyles.ets#L16-L77)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/C7QJmdKJR2SG8PpE5XtxWw/zh-cn_image_0000002558604666.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=904DBC181329453B14F916AF008F91C020769FC6A922DC662D4029AD155EA43F)

### 设置装饰线

通过[decoration](../harmonyos-references/ts-basic-components-span.md#decoration)设置富文本组件中文本装饰线的样式、颜色和粗细。

设置文本装饰线可突出关键信息、区分文本状态、增强视觉层次。例如，为重要标题或关键词添加装饰线，帮助用户快速获取信息。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.string.Demo_oneText')替换为实际资源文件，在本示例中该资源文件的value值为"一段预置的文本"
7. this.controller.addTextSpan($r('app.string.Demo_oneText'), {
8. style: {
9. fontSize: 25,
10. decoration: {
11. type: TextDecorationType.LineThrough,
12. color: Color.Blue,
13. // 设置装饰线粗细比例为6
14. thicknessScale: 6
15. }
16. }
17. })
18. })
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L360-L403)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/_gRYSeqMTlq9LEjfFL4SaQ/zh-cn_image_0000002589324191.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=E4A08299D3FB87A36534F65540AF918E51A39C16B164184BFE09656A8871AF72)

通过[DecorationOptions](../harmonyos-references/ts-universal-styled-string.md#decorationoptions20)中的enableMultiType设置多装饰线，比如同时设置下划线和中划线。

此接口适用于复杂业务场景，满足文本装饰的多样化需求。在文档协作过程中，多人编辑时，可以通过使用不同的装饰线组合来区分文本状态，从而提高协作效率。

```
1. RichEditor({ controller: this.styledStringController });
2. // 请将$r('app.string.Demo_SetStyledStringButton')替换为实际资源文件，在本示例中该资源文件的value值为"多装饰线文本"
3. Button($r('app.string.Demo_SetStyledStringButton'))
4. .fontSize(20)
5. .onClick(() => {
6. let mutString: MutableStyledString = new MutableStyledString(
7. // 请将$r('app.string.Demo_styledString')替换为实际资源文件，在本示例中该资源文件的value值为"需设置富文本多装饰线"
8. resource.resourceToString($r('app.string.Demo_styledString')), [
9. {
10. start: 0,
11. length: 9,
12. styledKey: StyledStringKey.FONT,
13. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(25) })
14. },
15. {
16. start: 0,
17. length: 5,
18. styledKey: StyledStringKey.DECORATION,
19. styledValue: new DecorationStyle(
20. {
21. type: TextDecorationType.Underline,
22. },
23. {
24. // 开启多装饰线
25. enableMultiType: true
26. })
27. },
28. {
29. start: 2,
30. length: 4,
31. styledKey: StyledStringKey.DECORATION,
32. styledValue: new DecorationStyle(
33. {
34. type: TextDecorationType.LineThrough,
35. },
36. {
37. // 开启多装饰线
38. enableMultiType: true
39. })
40. }
41. ])
42. this.styledStringController.setStyledString(mutString);
43. })
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L419-L463)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ES5d-nWCTxuEYWKiUoJMSg/zh-cn_image_0000002589244131.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=610559A94771E2A0B7BF70656F44E500C70D34DC48D88B98BADF5E3A53F4B9B8)

### 设置垂直居中

通过[textVerticalAlign](../harmonyos-references/ts-basic-components-text.md#textverticalalign20)设置文本段落在垂直方向的对齐方式。

此接口优化多元素排版，使组件内容与图片、图标等在垂直方向对齐时，整体布局更协调。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.media.startIcon')替换为实际资源文件
7. this.controller.addImageSpan($r('app.media.startIcon'), {
8. imageStyle: {
9. size: [100, 100]
10. }
11. })
12. // 请将$r('app.string.Demo_verticalAlignString')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段富文本，展示了文本垂直居中的效果。"
13. this.controller.addTextSpan($r('app.string.Demo_verticalAlignString'), {
14. style: {
15. fontColor: Color.Pink,
16. fontSize: '32'
17. },
18. paragraphStyle: {
19. textAlign: TextAlign.Start,
20. textVerticalAlign: TextVerticalAlign.CENTER,
21. leadingMargin: 16
22. }
23. })
24. })
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L472-L522)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/2XNEju5GS-mKLn_S3WsvyQ/zh-cn_image_0000002558764324.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=2384B0D2047340F75517787C539654E26DFA51FB66F4D351BB83C00CBD65DA66)

### 设置中西文自动间距

通过[enableAutoSpacing](../harmonyos-references/ts-basic-components-richeditor.md#enableautospacing20)设置是否开启中文与西文的自动间距。

此接口优化文本排版，提升组件内文本的可读性。设置自动间距后，中文与西文间产生适当空隙，便于区分不同语种，减少视觉干扰。

```
1. controller: RichEditorController = new RichEditorController();
2. options: RichEditorOptions = { controller: this.controller };
3. // ...
4. RichEditor(this.options)
5. .onReady(() => {
6. // 请将$r('app.string.Demo_autoSpacingString')替换为实际资源文件，在本示例中该资源文件的value值为"中西文Auto Spacing自动间距"
7. this.controller.addTextSpan($r('app.string.Demo_autoSpacingString'),
8. {
9. style:
10. {
11. fontColor: Color.Orange,
12. fontSize: 20
13. }
14. })
15. })
16. .enableAutoSpacing(this.enableAutoSpace)
```

[SetAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/richEditor/SetAttributes.ets#L525-L580)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/IYhlllz8ReKqgkU7xI26wQ/zh-cn_image_0000002558604668.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=4B10BA6E2EABDCAF9372C49C6F34C0ADBC6928C232F9938091C1AC80300D58E8)

## 示例代码

* [内容发布器](https://gitcode.com/HarmonyOS_Samples/content-publisher)
