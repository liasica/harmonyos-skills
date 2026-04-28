---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-docking-softkeyboard
title: Web组件对接软键盘
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > Web组件对接软键盘
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f6482413a7e4e96ab6190f410cee4b86e49a3b198896c7cd7f24708ff3bc8307
---

开发者能够通过Web组件对接软键盘，来处理系统软键盘的显示与交互问题，同时实现软键盘的自定义功能。主要有以下场景：

* 拉起系统软键盘输入文字：点击网页输入框时，屏幕下方将弹出系统默认的软键盘。开发者可以通过软键盘输入文字，输入的内容会显示在输入框中。
* 自定义系统软键盘的回车键类型：设置不同的回车键类型，例如：确认、下一个和提交。
* 软键盘避让：在移动设备上，由于输入法通常显示在屏幕下方区域，应用可设置不同的Web页面软键盘避让模式，来避让软键盘。例如：平移、调整大小和不避让。
* 自定义软键盘输入：在移动设备上，可以使用自绘制输入法在Web页面输入，以此替代系统软键盘。

## Web页面输入框输入与软键盘交互的W3C标准支持

为支持Web页面与系统软键盘、自定义软键盘等的良好交互，ArkWeb遵循并实现了W3C规范中的以下输入控制属性：

* type属性

  type属性定义了input元素的类型，影响输入的验证、显示方式和键盘类型。常见的type值包括：

  | type值 | 描述 |
  | --- | --- |
  | text | 默认值。普通文本输入 |
  | number | 数字输入 |
  | email | 电子邮件地址输入 |
  | password | 密码输入 |
  | tel | 电话号码输入 |
  | url | URL输入 |
  | date | 日期选择器 |
  | time | 时间选择器 |
  | checkbox | 复选框 |
  | radio | 单选按钮 |
  | file | 文件上传 |
  | submit | 提交按钮 |
  | reset | 重置按钮 |
  | button | 普通按钮 |
* inputmode属性

  inputmode属性用于配置输入法类型，默认值：text。

  | inputmode | 描述 |
  | --- | --- |
  | decimal | 只显示数字键盘，通常还有一个逗号键。 |
  | email | 文本键盘，键通常用于电子邮件地址，如[@]。 |
  | none | 不应出现键盘。 |
  | numeric | 只显示数字键盘。 |
  | search | 文本键盘，[enter]键通常显示为[go]。 |
  | tel | 只显示数字键盘，通常还有[+]、[\*]和[#]键。 |
  | text | 默认文本键盘。 |
  | url | 文本键盘，键通常用于网址，如[.]和[/]，以及特殊的[.com]键，或者其他通常用于本地设置的域名结束符。 |
* enterkeyhint属性

  enterkeyhint属性用于指定移动设备虚拟键盘上回车键的显示方式。

  | enterkeyhint值 | 描述 |
  | --- | --- |
  | enter | 显示默认的回车键 |
  | done | 表示输入完成 |
  | go | 表示跳转或执行 |
  | next | 进入下一个输入字段 |
  | previous | 返回上一个输入字段 |
  | search | 执行搜索 |
  | send | 发送信息 |

说明

点击网页输入框时，屏幕下方将弹出系统默认的软键盘，用户可以进行文字输入。

type属性影响键盘显示、输入验证和元素外观。

inputmode优化移动设备键盘输入体验，不影响基本行为或验证。

## 软键盘自动弹出

为提升用户体验，可以在页面完成加载后，输入框自动获焦并弹出软键盘。通过调用[showTextInput()](../harmonyos-references/js-apis-inputmethod.md#showtextinput10)设置软键盘自动弹出功能。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>DEMO</h1>
9. <input type="text" id="input_a">
10. </body>
11. </html>
```

```
1. // Index.ets
2. import { webview } from '@kit.ArkWeb';
3. import { inputMethod } from '@kit.IMEKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller})
12. .onPageEnd(() => {
13. this.controller.runJavaScript(`document.getElementById('input_a').focus()`).then(() => {
14. setTimeout(() => {
15. inputMethod.getController().showTextInput();
16. }, 10);
17. });
18. });
19. }
20. }
21. }
```

## 设置软键盘避让模式

在移动设备上，支持设置Web页面的软键盘避让模式。

1. 在应用代码中设置[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)的软键盘避让模式[setKeyboardAvoidMode()](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)。ArkWeb组件支持Resize和Offset两种模式。

* Resize模式下，应用窗口高度可缩小避开软键盘，ArkWeb组件跟随ArkUI重新布局。
* Offset模式下（以及默认模式），应用窗口高度不变，ArkWeb组件根据自身的避让模式进行避让。

（1）设置UIContext的软键盘避让模式。

```
1. import { KeyboardAvoidMode } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // ···
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

8. windowStage.loadContent('pages/Index', (err, data) => {
9. let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
10. // 设置虚拟键盘抬起时压缩页面大小为减去键盘的高度
11. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
12. if (err.code) {
13. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
14. return;
15. }
16. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
17. });
18. }
```

[Entry2Ability.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageInteracts/entry2/src/main/ets/entry2ability/Entry2Ability.ets#L18-L48)

（2）在Web组件中调起软键盘。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>DEMO</h1>
9. <input type="text" id="input_a">
10. </body>
11. </html>
```

```
1. // Index.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct KeyboardAvoidExample {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Row().height("50%").width("100%").backgroundColor(Color.Gray)
11. Web({ src: $rawfile("index.html"),controller: this.controller})
12. Text("I can see the bottom of the page").width("100%").textAlign(TextAlign.Center).backgroundColor(Color.Pink).layoutWeight(1)
13. }.width('100%').height("100%")
14. }
15. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageInteracts/entry2/src/main/ets/pages/Index.ets#L16-L32)

ArkWeb组件将跟随ArkUI重新布局，效果如图1和图2所示。

**图1** Web组件网页默认软键盘避让模式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/kvaRzTPdSwaOMR1Vw2iXMw/zh-cn_image_0000002552958216.png?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=651DC4AA41FA8986DFF2F4D9B8B15B5EA6CE72D84D5663B1ACD43F45D14A35D1)

**图2** Web组件网页跟随ArkUI软键盘避让模式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/gc3rf-4MS1eDr2zNM2Yt_Q/zh-cn_image_0000002583478217.png?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=20CEB98499CBE1918AA9170B4F263D03A00EE30ED38F4778CFE2B8E6C876CD52)

2.在UIContext的键盘避让模式为Offset模式时，应用可通过[WebKeyboardAvoidMode()](../harmonyos-references/arkts-basic-components-web-e.md#webkeyboardavoidmode12)设置ArkWeb组件的键盘避让模式。Web组件的[WebKeyboardAvoidMode()](../harmonyos-references/arkts-basic-components-web-e.md#webkeyboardavoidmode12)接口优先级高于W3C侧virtualKeyboard.overlayContent。

* RESIZE\_VISUAL：仅调整可视视口的大小，而不调整布局视口的大小。
* RESIZE\_CONTENT：调整可视视口和布局视口的大小。
* OVERLAYS\_CONTENT：不调整任何视口的大小，获焦input元素没有滚动到可视区域的行为。

说明

可视视口指用户正在看到的网站的区域，该区域的宽度等于移动设备的浏览器窗口的宽度。

布局视口指网页本身的宽度。

在应用代码中设置ArkWeb的软键盘避让模式。

```
1. // Index.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct KeyboardAvoidExample {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Row().height('50%').width('100%').backgroundColor(Color.Gray)
11. Web({ src: $rawfile('index.html'),controller: this.controller})
12. .keyboardAvoidMode(WebKeyboardAvoidMode.OVERLAYS_CONTENT) // 此时ArkWeb组件不会调整任何视口的大小。
13. Text('I can see the bottom of the page')
14. .width('100%')
15. .textAlign(TextAlign.Center)
16. .backgroundColor(Color.Pink)
17. .layoutWeight(1)
18. }.width('100%').height('100%')
19. }
20. }
```

[SetSKBMode\_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageInteracts/entry/src/main/ets/pages/SetSKBMode_one.ets#L16-L37)

ArkWeb组件根据避让模式进行避让，效果见图3。

**图3** Web组件网页自身软键盘避让模式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/OqbK5mRbTMyCJc_G3QycGw/zh-cn_image_0000002552798568.png?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=E9D9646D2B5725586720EF3D43CF969E28140ACD1F03311CEC1F3B2003E8CB70)

3.在软键盘弹出时，为使Web组件不发生避让行为，可通过调用[expandSafeArea()](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)设置Web组件扩展安全区域。更多详细示例可参考[网页中安全区域计算和避让适配](web-safe-area-insets.md)。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .width('100%').height('100%')
13. .expandSafeArea([SafeAreaType.KEYBOARD, SafeAreaType.SYSTEM])
14. }
15. }
16. }
```

与其他Web组件行为的交互场景：

| 交叉场景 | 规格 |
| --- | --- |
| 同层渲染 | 同层Web：软键盘避让方式与普通场景相同。  同层系统组件：由ArkUI负责软键盘避让模式。 |
| 离屏创建组件 | 默认使用与非离屏创建一致的软键盘避让模式，在添加至组件树前设置其他避让模式即可生效。 |
| customDialog | customDialog自身避让。 |
| 折叠屏 | 软键盘避让行为与普通场景行为一致。屏幕软键盘将根据屏幕开合状态进行调整。 |
| 软键盘托管 | 软键盘避让行为与普通场景行为一致。 |
| Web嵌套滚动 | 在嵌套滚动场景下，建议不要使用Web软键盘避让，包括RESIZE\_VISUAL和RESIZE\_CONTENT。 |

## 拦截系统软键盘与自定义软键盘输入

应用可以通过监听[onInterceptKeyboardAttach](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptkeyboardattach12)回调，在软键盘拉起前，控制软键盘的显示，包括系统默认软键盘、带有特定Enter键的软键盘，或完全自定义软键盘。借助这一功能，开发者能够实现对软键盘的灵活管理。

* 使用系统默认软键盘
* 使用带有定制Enter键的系统软键盘
* 使用完全由应用程序自定义的软键盘

```
1. // Index.ets
2. import { webview } from '@kit.ArkWeb';
3. import { inputMethodEngine } from '@kit.IMEKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. webKeyboardController: WebKeyboardController = new WebKeyboardController();
10. inputAttributeMap: Map<string, number> = new Map([
11. ['UNSPECIFIED', inputMethodEngine.ENTER_KEY_TYPE_UNSPECIFIED],
12. ['GO', inputMethodEngine.ENTER_KEY_TYPE_GO],
13. ['SEARCH', inputMethodEngine.ENTER_KEY_TYPE_SEARCH],
14. ['SEND', inputMethodEngine.ENTER_KEY_TYPE_SEND],
15. ['NEXT', inputMethodEngine.ENTER_KEY_TYPE_NEXT],
16. ['DONE', inputMethodEngine.ENTER_KEY_TYPE_DONE],
17. ['PREVIOUS', inputMethodEngine.ENTER_KEY_TYPE_PREVIOUS]
18. ])

20. /**
21. * 自定义键盘组件Builder
22. */
23. @Builder
24. customKeyboardBuilder() {
25. // 这里实现自定义键盘组件，对接WebKeyboardController实现输入、删除、关闭等操作。
26. Row() {
27. Text("完成")
28. .fontSize(20)
29. .fontColor(Color.Blue)
30. .onClick(() => {
31. this.webKeyboardController.close();
32. })
33. // 插入字符。
34. Button("insertText").onClick(() => {
35. this.webKeyboardController.insertText('insert ');
36. }).margin({
37. bottom: 200,
38. })
39. // 从后往前删除length参数指定长度的字符。
40. Button("deleteForward").onClick(() => {
41. this.webKeyboardController.deleteForward(1);
42. }).margin({
43. bottom: 200,
44. })
45. // 从前往后删除length参数指定长度的字符。
46. Button("deleteBackward").onClick(() => {
47. this.webKeyboardController.deleteBackward(1);
48. }).margin({
49. left: -220,
50. })
51. // 插入功能按键。
52. Button("sendFunctionKey").onClick(() => {
53. this.webKeyboardController.sendFunctionKey(6);
54. })
55. }
56. }

58. build() {
59. Column() {
60. Web({ src: $rawfile('index.html'), controller: this.controller })
61. .onInterceptKeyboardAttach((KeyboardCallbackInfo) => {
62. // option初始化，默认使用系统默认键盘
63. let option: WebKeyboardOptions = {
64. useSystemKeyboard: true,
65. };
66. if (!KeyboardCallbackInfo) {
67. return option;
68. }

70. // 保存WebKeyboardController，使用自定义键盘时候，需要使用该handler控制输入、删除、软键盘关闭等行为
71. this.webKeyboardController = KeyboardCallbackInfo.controller;
72. let attributes: Record<string, string> = KeyboardCallbackInfo.attributes;
73. // 遍历attributes
74. let attributeKeys = Object.keys(attributes);
75. for (let i = 0; i < attributeKeys.length; i++) {
76. console.info('WebCustomKeyboard key = ' + attributeKeys[i] + ', value = ' + attributes[attributeKeys[i]]);
77. }

79. if (attributes) {
80. if (attributes['data-keyboard'] == 'customKeyboard') {
81. // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有data-keyboard，且值为customKeyboard，则使用自定义键盘
82. console.info('WebCustomKeyboard use custom keyboard');
83. option.useSystemKeyboard = false;
84. // 设置自定义键盘builder
85. option.customKeyboard = () => {
86. this.customKeyboardBuilder()
87. }
88. return option;
89. }

91. if (attributes['keyboard-return'] != undefined) {
92. // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有keyboard-return，使用系统键盘，并且指定系统软键盘enterKey类型
93. option.useSystemKeyboard = true;
94. let enterKeyType: number | undefined = this.inputAttributeMap.get(attributes['keyboard-return']);
95. if (enterKeyType != undefined) {
96. option.enterKeyType = enterKeyType;
97. }
98. return option;
99. }
100. }

102. return option;
103. })
104. }
105. }
106. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>

5. <head>
6. <meta charset="utf-8">
7. <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0">
8. </head>

10. <body>

12. <p style="font-size:12px">input标签，原有默认行为：</p>
13. <input type="text" style="width: 300px; height: 20px"><br>
14. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

16. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key UNSPECIFIED：</p>
17. <input type="text" keyboard-return="UNSPECIFIED" style="width: 300px; height: 20px"><br>
18. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

20. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key GO：</p>
21. <input type="text" keyboard-return="GO" style="width: 300px; height: 20px"><br>
22. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

24. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key SEARCH：</p>
25. <input type="text" keyboard-return="SEARCH" style="width: 300px; height: 20px"><br>
26. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

28. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key SEND：</p>
29. <input type="text" keyboard-return="SEND" style="width: 300px; height: 20px"><br>
30. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

32. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key NEXT：</p>
33. <input type="text" keyboard-return="NEXT" style="width: 300px; height: 20px"><br>
34. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

36. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key DONE：</p>
37. <input type="text" keyboard-return="DONE" style="width: 300px; height: 20px"><br>
38. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

40. <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key PREVIOUS：</p>
41. <input type="text" keyboard-return="PREVIOUS" style="width: 300px; height: 20px"><br>
42. <hr style="height:2px;border-width:0;color:gray;background-color:gray">

44. <p style="font-size:12px">input标签，应用自定义键盘：</p>
45. <input type="text" data-keyboard="customKeyboard" style="width: 300px; height: 20px"><br>

47. </body>

49. </html>
```

ArkWeb自定义键盘的示例效果如图4、图5和图6所示。

**图4** ArkWeb自定义键盘数字键盘

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/-kAEBtGGSXK6-t-1FMVrPA/zh-cn_image_0000002583438263.png?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=A8FCC443E487342E3A6512B850702D13E91F9E61250F9AFD6DC531D770141CFE)

**图5** ArkWeb自定义键盘字母键盘

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/MrOyvFm5QFirn3EdnEWvaw/zh-cn_image_0000002552958218.png?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=E09B65A477917F3E23150CFA3483E26CD76C66DD63A7265D8CFE8CB1E679FD46)

**图6** ArkWeb自定义键盘符号键盘

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/H9ErCANBT8W8icsLxbF0NA/zh-cn_image_0000002583478219.png?HW-CC-KV=V1&HW-CC-Date=20260427T234054Z&HW-CC-Expire=86400&HW-CC-Sign=1B66B4ADA861DFEF63EFE47BE023F78501BA850B6337EA91E7BCB127913A05EA)
