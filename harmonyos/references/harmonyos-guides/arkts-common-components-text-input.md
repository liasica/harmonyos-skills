---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input
title: 文本输入 (TextInput/TextArea/Search)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 文本输入 (TextInput/TextArea/Search)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:46+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a0a21021192989b655607bd4a1667ab7d5133afbd79c97b8d233240d7ecc88ed
---

TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](../harmonyos-references/ts-basic-components-textinput.md)和[TextArea](../harmonyos-references/ts-basic-components-textarea.md)组件的API文档。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](../harmonyos-references/ts-basic-components-search.md)组件的API文档。

说明

仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件。

## 创建输入框

TextInput是单行输入框，TextArea是多行输入框，Search是搜索框。通过以下接口创建这些组件。

```
1. TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

```
1. TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```
1. Search(options?:{placeholder?: ResourceStr, value?: ResourceStr, controller?: SearchController, icon?: string})
```

* 单行输入框。

  ```
  1. TextInput()
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L26-L28)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ZsuCJfMkRR6SkVTOI1F9fg/zh-cn_image_0000002558604642.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=56F26E57DC314E23E5FDD97CF7A7933259AAA8CCB8AF42784DBE664215B32C33)
* 多行输入框。

  ```
  1. TextArea()
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L38-L40)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/4C80bGYqR0iWG5Xrdrf9Fg/zh-cn_image_0000002589324167.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=C4B2DD3C82D3C944DE0FCE41724C6336F6FE69C8DBCE41EE06B6797F937C1DC2)
* 多行输入框文字超出一行时会自动折行。

  ```
  1. /* 请将$r('app.string.CreatTextInput_textContent')替换为实际资源文件，在本示例中该资源文件的value值为
  2. * "我是TextArea我是TextArea我是TextArea我是TextArea"
  3. */
  4. TextArea({ text: $r('app.string.CreatTextInput_textContent') })
  5. .width(300)
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L41-L46)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Pe5VB5M7R7CJlwXh2mzGZQ/zh-cn_image_0000002589244107.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=D8FEF8D0BEABFD28D8679929A16684EFAF2EA4D38C1D6785D771FF073B07AC92)
* 搜索框。

  ```
  1. Search()
  2. // 请将$r('app.string.Creat_TextInput_Content')替换为实际资源文件，在本示例中该资源文件的value值为"搜索"
  3. .searchButton($r('app.string.Creat_TextInput_Content'))
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L52-L56)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/7nn3E205Td-x2VrTIWTqKA/zh-cn_image_0000002558764300.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=BB0306950E3B6937E71B854170B8994DEB836533AC16D14B1C51B8DD46F25932)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER\_NAME用户名输入模式、NEW\_PASSWORD新密码输入模式、NUMBER\_PASSWORD纯数字密码输入模式、NUMBER\_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](../harmonyos-references/ts-basic-components-textinput.md#type)属性进行设置：

### 基本输入模式（默认类型）

```
1. TextInput()
2. .type(InputType.Normal)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L27-L30)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/_e8qywflS92FUIAdNbzs4g/zh-cn_image_0000002558604644.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=7A7E1983CB418FC34B3B8107402D19F62A464E8DFD13FA453AA5BA254770F287)

### 密码模式

包括Password密码输入模式、NUMBER\_PASSWORD纯数字密码模式、NEW\_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```
1. TextInput()
2. .type(InputType.Password)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L36-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/9t9PzjKqS1SzK7JkzoEj6w/zh-cn_image_0000002589324169.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=8F15B0796BAA0FA66B28FD90325FA42CC3257B75757EB63CCB1E5220DA597FBF)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```
1. TextInput()
2. .type(InputType.Email)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L45-L48)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/OzQPtHZdSliROEyV76m8mA/zh-cn_image_0000002589244109.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=C8A1F61514D48C2123140360D4AE3B130F1553A932D5DD190A1082914BEE8053)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```
1. TextInput()
2. .type(InputType.Number)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L54-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Jurv_lu1Qs-TTn6zHrj9SA/zh-cn_image_0000002558764302.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=C13235B21F8C56A20F5E9339F27CA54FC6DF5D1A8C395EB07B977FDD74EA5588)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。

```
1. TextInput()
2. .type(InputType.PhoneNumber)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L63-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/HP2CHJkvRB257RpENX_Gcw/zh-cn_image_0000002558604646.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=EAD4C7D0188B538ADA9FFC056274EF414B0A2BD708D7D1B6896E54DCDCA9FFA3)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```
1. TextInput()
2. .type(InputType.NUMBER_DECIMAL)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L72-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/aC6xpEIeTPKy7lTmo4n8eA/zh-cn_image_0000002589324171.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=0D98A5AA65FA6CB40B22AFD70FD33DE554B9FD23C9B45D71C9D8784992FB9BAB)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```
1. TextInput()
2. .type(InputType.URL)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L81-L84)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/W8bNxye9TDyyXzj688VzMA/zh-cn_image_0000002589244111.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=8B5D4FF7DEEEC23FC64AAAD290B520BAF970F6303DB357ACA3669479704AB00E)

## 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](../harmonyos-references/ts-basic-components-textarea.md#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

### 默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

```
1. TextArea()
2. .style(TextContentStyle.DEFAULT)
```

[SetInputMultiTypeStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetInputMultiTypeStyle.ets#L25-L28)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/XMKYou3VQEia8tRulnv8Ew/zh-cn_image_0000002558764304.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=E820DF58155741B726A291FC717CD93BD1154564707CDF42C5061FB193ACF697)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```
1. TextArea()
2. .style(TextContentStyle.INLINE)
```

[SetInputMultiTypeStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetInputMultiTypeStyle.ets#L32-L35)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/V0lzbirFTPWNtYn_NT9Cbg/zh-cn_image_0000002558604648.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=E2009E478B05BE882CD38BB2B15AF832206649FB4FD501EC521445F7B05E952E)

## 自定义样式

* 设置无输入时的提示文本。

  ```
  1. // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  2. TextInput({ placeholder: $r('app.string.i_am_placeholder') })
  ```

  [CustomTextInputStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CustomTextInputStyle.ets#L26-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/CYNJpCecRBm4zD1h70lJ0Q/zh-cn_image_0000002589324173.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=2F810FB0F475BD920E52FADF64AF889C4C2517A303D6FAC43ED954835212D16A)
* 设置输入框当前的文本内容。

  ```
  1. TextInput({
  2. // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  3. placeholder: $r('app.string.i_am_placeholder'),
  4. // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
  5. text: $r('app.string.i_am_current_text_content')
  6. })
  ```

  [CustomTextInputStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CustomTextInputStyle.ets#L35-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/QJjWmrwIRcylOi-iiwvrIg/zh-cn_image_0000002589244113.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=C09462B030AFEFAAEE36E96C2730B912E0AB592972A9836322E014EA5C2B3193)
* 添加backgroundColor改变输入框的背景颜色。

  ```
  1. TextInput({
  2. // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  3. placeholder: $r('app.string.i_am_placeholder'),
  4. // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
  5. text: $r('app.string.i_am_current_text_content')
  6. })
  7. .backgroundColor(Color.Pink)
  ```

  [CustomTextInputStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CustomTextInputStyle.ets#L47-L55)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/nxu614IyQR-AfA2hjQvIdQ/zh-cn_image_0000002558764306.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=A63ED0AC0704F8D39E6ECD4C76C66D2A72B5B80953146C0693E239D6EE4CD8EB)

  更丰富的样式可以结合[通用属性](../harmonyos-references/ts-component-general-attributes.md)实现。

## 添加事件

文本框主要用于获取用户输入的信息，并将信息处理成数据进行上传，绑定[onChange](../harmonyos-references/ts-basic-components-textinput.md#onchange)事件可以获取输入框内改变的文本内容，绑定[onSubmit](../harmonyos-references/ts-basic-components-textinput.md#onsubmit)事件可以获取回车提交的文本信息，绑定[onTextSelectionChange](../harmonyos-references/ts-basic-components-textinput.md#ontextselectionchange10)事件可以获取文本选中时手柄的位置信息或者编辑时光标的位置信息等等。用户也可以使用通用事件进行相应的交互操作。

说明

在密码模式下，设置[showPassword](../harmonyos-references/ts-basic-components-textinput.md#showpassword12)属性时，在[onSecurityStateChange](../harmonyos-references/ts-basic-components-textinput.md#onsecuritystatechange12)回调中，建议增加状态同步，具体详见如下示例。

[onWillInsert](../harmonyos-references/ts-basic-components-textinput.md#onwillinsert12)、[onDidInsert](../harmonyos-references/ts-basic-components-textinput.md#ondidinsert12)、[onWillDelete](../harmonyos-references/ts-basic-components-textinput.md#onwilldelete12)、[onDidDelete](../harmonyos-references/ts-basic-components-textinput.md#ondiddelete12)回调仅支持系统输入法的场景。

[onWillChange](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)的回调时序晚于[onWillInsert](../harmonyos-references/ts-basic-components-textinput.md#onwillinsert12)、[onWillDelete](../harmonyos-references/ts-basic-components-textinput.md#onwilldelete12)，早于[onDidInsert](../harmonyos-references/ts-basic-components-textinput.md#ondidinsert12)、[onDidDelete](../harmonyos-references/ts-basic-components-textinput.md#ondiddelete12)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_Textcomponent]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'Textcomponent_';

7. @Entry
8. @Component
9. struct TextInputEventAdd {
10. @State text: string = '';
11. @State textStr1: string = '';
12. @State textStr2: string = '';
13. @State textStr3: string = '';
14. @State textStr4: string = '';
15. @State textStr5: string = '';
16. @State textStr6: string = '';
17. @State textStr7: string = '';
18. @State textStr8: string = '';
19. @State textStr9: string = '';
20. @State passwordState: boolean = false;
21. controller: TextInputController = new TextInputController();

23. build() {
24. Row() {
25. Column() {
26. Text(`${this.textStr1}\n${this.textStr2}\n${this.textStr3}
27. \n${this.textStr4}\n${this.textStr5}\n${this.textStr6}
28. \n${this.textStr7}\n${this.textStr8}\n${this.textStr9}`)
29. .fontSize(20)
30. .width('70%')
31. TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
32. .type(InputType.Password)
33. .showPassword(this.passwordState)
34. .onChange((value: string) => {
35. // 文本内容发生变化时触发该回调
36. hilog.info(DOMAIN, TAG, BUNDLE + 'onChange is triggering: ' + value);
37. this.textStr1 = `onChange is triggering: ${value}`;
38. })
39. .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
40. // 按下输入法回车键时触发该回调
41. hilog.info(DOMAIN, TAG, BUNDLE + 'onSubmit is triggering: ' + enterKey + event.text);
42. this.textStr2 = `onSubmit is triggering: ${enterKey} ${event.text}`;
43. })
44. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
45. // 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调
46. hilog.info(DOMAIN, TAG, BUNDLE + 'onTextSelectionChange is triggering: ' + selectionStart + selectionEnd);
47. this.textStr3 = `onTextSelectionChange is triggering: ${selectionStart} ${selectionEnd}`;
48. })
49. .onSecurityStateChange((isShowPassword: boolean) => {
50. // 密码显隐状态切换时，触发该回调
51. hilog.info(DOMAIN, TAG, BUNDLE + 'onSecurityStateChange is triggering: ' + isShowPassword);
52. this.passwordState = isShowPassword;
53. this.textStr4 = `onSecurityStateChange is triggering: ${isShowPassword}`;
54. })
55. .onWillInsert((info: InsertValue) => {
56. // 在将要输入时，触发该回调
57. hilog.info(DOMAIN, TAG, BUNDLE + 'onWillInsert is triggering: ' + info.insertValue + info.insertOffset);
58. this.textStr5 = `onWillInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
59. return true;
60. })
61. .onDidInsert((info: InsertValue) => {
62. // 在输入完成时，触发该回调
63. hilog.info(DOMAIN, TAG, BUNDLE + 'onDidInsert is triggering: ' + info.insertValue + info.insertOffset);
64. this.textStr6 = `onDidInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
65. })
66. .onWillDelete((info: DeleteValue) => {
67. // 在将要删除时，触发该回调
68. hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDelete is triggering: ' + info.deleteValue + info.deleteOffset);
69. this.textStr7 = `onWillDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
70. return true;
71. })
72. .onDidDelete((info: DeleteValue) => {
73. // 在删除完成时，触发该回调
74. hilog.info(DOMAIN, TAG, BUNDLE + 'onDidDelete is triggering: ' + info.deleteValue + info.deleteOffset);
75. this.textStr8 = `onDidDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
76. })
77. .onFocus(() => {
78. // 绑定通用事件，输入框获焦时触发该回调
79. hilog.info(DOMAIN, TAG, BUNDLE + 'onFocus is triggering');
80. this.textStr9 = `onFocus is triggering`;
81. })
82. }.width('100%')
83. }
84. .height('100%')
85. }
86. }
```

[TextInputAddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/TextInputAddEvent.ets#L15-L101)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/o4DURoaQSl-oHTpvwAEzLA/zh-cn_image_0000002558604650.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=66B5F0A77223909E4DE48E2965EF0ED654158A800FF0A0AC484A0F2CF5BEE200)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、分享的菜单。

TextInput:

```
1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
2. TextInput({ text: $r('app.string.show_selected_menu') })
```

[SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SelectMenu.ets#L26-L29)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/LZ-_uj6LQKq1-2A-0t5pJw/zh-cn_image_0000002589324175.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=95B5FED6A91EB02366579C63DB8EDE4253312C4AD7FD8CE717538AE405ACC44F)

TextArea:

```
1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
2. TextArea({ text: $r('app.string.show_selected_menu') })
```

[SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SelectMenu.ets#L30-L33)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/8KMR4mKiTNKlzihxsprZgg/zh-cn_image_0000002589244115.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=4C9C298FE7F1ACD1909F7AE060FC93ACCB0CFF4C385E434568C6AF7A1A7D0C17)

## 禁用系统服务类菜单

从API version 20开始，支持使用[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)方法屏蔽文本选择菜单中的所有系统服务菜单项。更多详见[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。

```
1. import { TextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct DisableSystemServiceMenuItem {
6. aboutToAppear(): void {
7. // 禁用所有系统服务菜单项
8. TextMenuController.disableSystemServiceMenuItems(true)
9. }

11. aboutToDisappear(): void {
12. // 页面消失时恢复系统服务菜单项
13. TextMenuController.disableSystemServiceMenuItems(false)
14. }

16. build() {
17. Row() {
18. Column() {
19. // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
20. TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
21. .height(60)
22. .fontStyle(FontStyle.Italic)
23. .fontWeight(FontWeight.Bold)
24. .textAlign(TextAlign.Center)
25. .caretStyle({ width: '4vp' })
26. .editMenuOptions({
27. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
28. // menuItems不包含被屏蔽的系统菜单项
29. return menuItems
30. },
31. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
32. return false
33. }
34. })
35. }.width('100%')
36. }
37. .height('100%')
38. }
39. }
```

[DisableSystemServiceMenuItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/disablemenu/DisableSystemServiceMenuItems.ets#L16-L56)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/q7QfOsJdRd-3xyOd_5GMgg/zh-cn_image_0000002558764308.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=912AE6892EE76EAFB266000691A6D2E557C30EAADAEAB891C74335EE4D198457)

从API version 20开始，支持使用[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)方法屏蔽文本选择菜单中指定的系统服务菜单项。更多详见[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。

```
1. import { TextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct DisableMenuItem {
6. aboutToAppear(): void {
7. // 禁用搜索，翻译和AI帮写
8. TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE, TextMenuItemId.AI_WRITER])
9. }

11. aboutToDisappear(): void {
12. // 页面消失时恢复系统服务菜单项
13. TextMenuController.disableMenuItems([])
14. }

16. build() {
17. Row() {
18. Column() {
19. // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
20. TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
21. .height(60)
22. .fontStyle(FontStyle.Italic)
23. .fontWeight(FontWeight.Bold)
24. .textAlign(TextAlign.Center)
25. .caretStyle({ width: '4vp' })
26. .editMenuOptions({
27. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
28. // menuItems不包含搜索和翻译
29. return menuItems;
30. },
31. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
32. return false
33. }
34. })
35. }.width('100%')
36. }
37. .height('100%')
38. }
39. }
```

[DisableMenuItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/disablemenu/DisableMenuItems.ets#L16-L56)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/3Cj3gpxtQqiWOF4JDMOP0Q/zh-cn_image_0000002558604652.png?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=1367A35A8B66F32678A8A37DBE8674E7FF71F5ECE704C5C166A42BEF959AFB6B)

## 自动填充

输入框可以通过[contentType](../harmonyos-references/ts-basic-components-textinput.md#contenttype12)属性设置自动填充类型。

支持的类型请参考[ContentType](../harmonyos-references/ts-basic-components-textinput.md#contenttype12枚举说明)。

```
1. // 请将$r('app.string.Auto_Fill_PlaceHolder')替换为实际资源文件，在本示例中该资源文件的value值为"输入你的邮箱..."
2. TextInput({ placeholder: $r('app.string.Auto_Fill_PlaceHolder') })
3. .width('95%')
4. .height(40)
5. .margin(20)
6. .contentType(ContentType.EMAIL_ADDRESS)
```

[AutoFill.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/AutoFill.ets#L25-L32)

## 设置属性

* 设置省略属性。

  输入框可以通过[ellipsisMode](../harmonyos-references/ts-basic-components-textinput.md#ellipsismode18)属性设置省略位置。

  ellipsisMode属性需要配合[textOverflow](../harmonyos-references/ts-basic-components-textinput.md#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。

  ```
  1. // 请将$r('app.string.Set_Omission_Property_textContent')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示省略模式"
  2. TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })
  3. .textOverflow(TextOverflow.Ellipsis)
  4. .ellipsisMode(EllipsisMode.END)
  5. .style(TextInputStyle.Inline)
  6. .fontSize(30)
  7. .margin(30)
  ```

  [SetProperty.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetProperty.ets#L26-L34)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/RApnwkHMS-K8plpbIRaaaA/zh-cn_image_0000002589324177.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=1111CE8F18B2875CC3F9D4DDDFBBA6503DBBCEDB4628F70538D4201D13F512C7)
* 设置文本描边属性。

  从API version 20开始，输入框可以通过[strokeWidth](../harmonyos-references/ts-basic-components-textinput.md#strokewidth20)和[strokeColor](../harmonyos-references/ts-basic-components-textinput.md#strokecolor20)属性设置文本的描边宽度及颜色。

  ```
  1. TextInput({ text: 'Text with stroke' })
  2. .width('100%')
  3. .height(60)
  4. .borderWidth(1)
  5. .fontSize(40)
  6. .strokeWidth(LengthMetrics.px(3.0))
  7. .strokeColor(Color.Red)
  ```

  [SetProperty.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetProperty.ets#L39-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/-X27viNmSfCFBfu4YaN3oQ/zh-cn_image_0000002589244117.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=2268EE92F5176BA5C016C09FDBDCE3B5C16B43D7BF1C779AD1DFE0DB8E05D2FE)

## 设置文本行间距

从API version 20开始，支持通过[lineSpacing](../harmonyos-references/ts-basic-components-text.md#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](../harmonyos-references/ts-text-common.md#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

```
1. TextArea({
2. text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
3. })
4. .fontSize(22)
5. .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
```

[SetTextMargin.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextMargin.ets#L26-L32)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/PDw5FkYXRh6CqsKjEY8GSw/zh-cn_image_0000002558764310.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=3B96F96FEC29B1637B715451909DFDD23A923E47E962A85042619AE744760937)

## 键盘避让

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](../harmonyos-references/ts-container-scroll.md)、[List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)。

```
1. @Entry
2. @Component
3. struct KeyboardAvoid {
4. placeHolderArr: string[] = ['1', '2', '3', '4', '5', '6', '7'];

6. build() {
7. Scroll() {
8. Column() {
9. ForEach(this.placeHolderArr, (placeholder: string) => {
10. TextInput({ placeholder: 'TextInput ' + placeholder })
11. .margin(30)
12. // ···
13. })
14. }
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }
```

[KeyboardAvoidance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/KeyboardAvoidance.ets#L18-L40)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/gcTqAoKRQ1SHKFrK_x6tYw/zh-cn_image_0000002558604654.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=5F3A2847C1A7A584B29461EC7A6EA0033F86DC15D0B810AC0A6A9F842AF179A6)

## 光标避让

[keyBoardAvoidMode](../harmonyos-references/arkts-apis-uicontext-e.md#keyboardavoidmode11)枚举中的OFFSET和RESIZE在键盘抬起后，不支持二次避让。如果想要支持光标位置在点击或者通过接口设置变化后发生二次避让，可以考虑使用OFFSET\_WITH\_CARET和RESIZE\_CARET替换原有的OFFSET和RESIZE模式。

对于滚动容器更推荐使用RESIZE\_WITH\_CARET，非滚动容器应该使用OFFSET\_WITH\_CARET。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { window } from '@kit.ArkUI';
3. import { KeyboardAvoidMode } from '@kit.ArkUI';
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/entryability/EntryAbility.ets#L18-L22)

```
1. // Used in UIAbility
2. onWindowStageCreate(windowStage: window.WindowStage): void {
3. // Main window is created, set main page for this ability
4. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

6. windowStage.loadContent('pages/Index', (err, data) => {
7. let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
8. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET_WITH_CARET);
9. if (err.code) {
10. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
11. return;
12. }
13. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
14. });
15. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/entryability/EntryAbility.ets#L34-L50)

```
1. @Entry
2. @Component
3. struct CursorAvoid {
4. @State caretPosition: number = 600;
5. areaController: TextAreaController = new TextAreaController();
6. text = 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot,' +
7. ' or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
8. 'anything that makes ourselves unhappy,' +
9. ' totally forgetting that there is something happy in our own life.\
10. So the best way to destroy happiness is to look at something and focus on even the smallest flaw. ' +
11. 'It is the smallest flaw that would make us complain. And it is the complaint that leads to us becoming unhappy.\
12. If one chooses to be happy, he will be blessed; if he chooses to be unhappy, he will be cursed. ' +
13. 'Happiness is just what you think will make you happy.' +
14. 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, ' +
15. 'or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
16. 'anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life.\
17. ';

19. build() {
20. Scroll() {
21. Column() {
22. Row() {
23. Button('CaretPosition++: ' + this.caretPosition).onClick(() => {
24. this.caretPosition += 1;
25. }).fontSize(10)
26. Button('CaretPosition--: ' + this.caretPosition).onClick(() => {
27. this.caretPosition -= 1;
28. }).fontSize(10)
29. Button('SetCaretPosition: ').onClick(() => {
30. this.areaController.caretPosition(this.caretPosition);
31. }).fontSize(10)
32. }

34. TextArea({ text: this.text, controller: this.areaController })
35. .width('100%')
36. .fontSize('20fp')
37. }
38. }.width('100%').height('100%')
39. }
40. }
```

[CursorAvoidance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CursorAvoidance.ets#L18-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/3iWp-REDTvKZt1gLIn6Sdg/zh-cn_image_0000002589324179.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=960173E69B5C0486EE6612A56A429EFC7AD5F2DCA783FD4B179E5916AE7E9F5F)

## 常见问题

### 如何设置TextArea的文本最少展示行数并自适应高度

**问题现象**

设置TextArea的初始高度来控制最少文本展示行数，当输入文本超过初始高度时，TextArea的高度自适应。

**解决措施**

设置[minLines](../harmonyos-references/ts-basic-components-textarea.md#minlines20)（从API version 20开始），或者设置height为"auto"，并使用[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)自行计算高度。

```
1. import { MeasureUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TextExample {
6. private textAreaPadding = 12;
7. private setMaxLines = 3;
8. private resourceManager = this.getUIContext().getHostContext()?.resourceManager;
9. // 请在resources\base\element\string.json文件中配置name为'NormalQuestion_change'，value为非空字符串的资源
10. private changeText = this.resourceManager?.getStringByNameSync('NormalQuestion_change') as string;
11. @State fullText: string = this.changeText;
12. @State originText: string = this.changeText;
13. @State uiContext: UIContext = this.getUIContext();
14. @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
15. textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
16. textContent: this.originText,
17. fontSize: 18
18. });

20. build() {
21. Column() {
22. TextArea({ text: 'minLines: ' + this.fullText })
23. .fontSize(18)
24. .width(300)
25. .minLines(3)

27. Blank(50)

29. TextArea({ text: 'constraintSize: ' + this.fullText })
30. .fontSize(18)
31. .padding({ top: this.textAreaPadding, bottom: this.textAreaPadding })
32. .width(300)
33. .height('auto')
34. .constraintSize({
35. // 结合padding计算，设置至少显示this.setMaxLines行文本
36. // 若涉及适老化字号缩放，需要监听并调整高度
37. minHeight: this.textAreaPadding * 2 +
38. this.setMaxLines * this.getUIContext().px2vp(Number(this.textSize.height))
39. })

41. Blank(50)
42. // 请将$r('app.string.NormalQuestion_AddInput')替换为实际资源文件，在本示例中该资源文件的value值为"增加输入"
43. Button($r('app.string.NormalQuestion_AddInput'))
44. .onClick(() => {
45. this.fullText += this.changeText;
46. })
47. }
48. .justifyContent(FlexAlign.Center)
49. .width('100%')
50. .padding({ top: 30 })
51. }
52. }
```

[NormalQuestion.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/NormalQuestion.ets#L15-L68)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/aTEByXpUSEiPxMMH9Boevg/zh-cn_image_0000002589244119.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052743Z&HW-CC-Expire=86400&HW-CC-Sign=F46EBA165B40C321FD1032914030D05B5C746B250B99C8FE71A6BE55CBFA516B)
