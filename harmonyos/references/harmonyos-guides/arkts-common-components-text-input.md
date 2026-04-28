---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input
title: 文本输入 (TextInput/TextArea/Search)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 文本输入 (TextInput/TextArea/Search)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e2b2eed086b47d2867f367e8b5bc9e50e370c7b2bb712951f4a3b6d957080f34
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/21jEHqVYRXmlpw9mmdYasw/zh-cn_image_0000002583437853.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=A17B38ED20A5AB8990C43C99F16BA50E80AB1C5AF0A89F38B53640B970A2E285)
* 多行输入框。

  ```
  1. TextArea()
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L38-L40)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/_S_Y54ggSsG1EqIpL0GerQ/zh-cn_image_0000002552957808.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=4DFD168D703275C1511E1E0E29E9DE2FF9B0F4291980CBF095B68DCE99BE0C1C)
* 多行输入框文字超出一行时会自动折行。

  ```
  1. /* 请将$r('app.string.CreatTextInput_textContent')替换为实际资源文件，在本示例中该资源文件的value值为
  2. * "我是TextArea我是TextArea我是TextArea我是TextArea"
  3. */
  4. TextArea({ text: $r('app.string.CreatTextInput_textContent') })
  5. .width(300)
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L41-L46)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/6MWgatvRQlq0ltT7D5HIEw/zh-cn_image_0000002583477809.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=B1BA6A9BF3513FADBA6A67FD923FBAF0E19AE4BC738BBD54341FB12B8F559A5B)
* 搜索框。

  ```
  1. Search()
  2. // 请将$r('app.string.Creat_TextInput_Content')替换为实际资源文件，在本示例中该资源文件的value值为"搜索"
  3. .searchButton($r('app.string.Creat_TextInput_Content'))
  ```

  [CreatTextInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CreatTextInput.ets#L52-L56)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/NM_GsJc0QXC74u4JS_HI6Q/zh-cn_image_0000002552798160.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=A412A0271145EBED1E2E63347E0FA9B50EE6FBA9E46FC4DE466D754D12472B8C)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER\_NAME用户名输入模式、NEW\_PASSWORD新密码输入模式、NUMBER\_PASSWORD纯数字密码输入模式、NUMBER\_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](../harmonyos-references/ts-basic-components-textinput.md#type)属性进行设置：

### 基本输入模式（默认类型）

```
1. TextInput()
2. .type(InputType.Normal)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L27-L30)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/TJJSS9hdT06HODwcvAMzVA/zh-cn_image_0000002583437855.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=1ADFEFE300CB972B767A5C8F5F92EC99A38E8B1124404AF84EF849B1216B2CEC)

### 密码模式

包括Password密码输入模式、NUMBER\_PASSWORD纯数字密码模式、NEW\_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```
1. TextInput()
2. .type(InputType.Password)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L36-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/5W_QlUBnRyunx5ecuVYvKQ/zh-cn_image_0000002552957810.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=9C349D27AC56B662138A51F072D27231690B791BB91F6B139F5A3A20FEF7E84E)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```
1. TextInput()
2. .type(InputType.Email)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L45-L48)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/2k31ZHmxS9quvloVbIWrjA/zh-cn_image_0000002583477811.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=5873FEA0864F91FB73B5C4F76A96A0E5A07EB4F8B3A0F01D38D498425DAEAFE8)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```
1. TextInput()
2. .type(InputType.Number)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L54-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/4DtArWmQRZW23UAd566diQ/zh-cn_image_0000002552798162.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=AD1947E2B4FBD23FD5CE22D047018388456EC538733DEFF65402AAB99C6D48DA)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。

```
1. TextInput()
2. .type(InputType.PhoneNumber)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L63-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/k48-ro_CSSqdMn7xAj1b_g/zh-cn_image_0000002583437857.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=2AB4A043CBD93EB3F0F21C68BFBF064BFE86EEF688F653B5DBCBE7D17A3D1A53)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```
1. TextInput()
2. .type(InputType.NUMBER_DECIMAL)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L72-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/V51qeSiFSk-neTXnumC2Og/zh-cn_image_0000002552957812.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=523E57454F7BF148F1601A786D5E4284481C8B9E9C3CBD70AC1CAE825D2E795C)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```
1. TextInput()
2. .type(InputType.URL)
```

[SetTextInputType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetTextInputType.ets#L81-L84)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/oJ2NiRkTRqWuNSMkrnVrLQ/zh-cn_image_0000002583477813.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=781F9E5CA419886691E58C2CA9AF267E20AB7620BC6D9EAB23B21A950AF026FD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/PKSucriqRoiwPHS6rZjLfw/zh-cn_image_0000002552798164.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=B4ACB2BEBEFE5CD614FA5D0C2089A96B144C5FD7524534A604FADA27FFC70ED0)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```
1. TextArea()
2. .style(TextContentStyle.INLINE)
```

[SetInputMultiTypeStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SetInputMultiTypeStyle.ets#L32-L35)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/tb-Idc5YRNi4DDkU5unYBw/zh-cn_image_0000002583437859.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=4653DC3124D0A32C312E950CBDE46A4F1172203383217DAA1221FD1D5831E29A)

## 自定义样式

* 设置无输入时的提示文本。

  ```
  1. // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  2. TextInput({ placeholder: $r('app.string.i_am_placeholder') })
  ```

  [CustomTextInputStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/CustomTextInputStyle.ets#L26-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/e9-O6-h2SeegC9xLezlCQw/zh-cn_image_0000002552957814.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=801CE7D75DD7C544E90F342360F4AD440297E6777E688D6EF8021DD6EBD53AB6)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/_Ces6q0OTXuu_7T1iZqhlA/zh-cn_image_0000002583477815.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=41D23626EB8F2CD8ED343B3FA9F37CD3D387323663818BBF7344AC0C38EE4C76)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Bpp4Q3IAQDaiQSIM7vuG2w/zh-cn_image_0000002552798166.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=8FA8EF95864D179D47133CD03B2EEE647ED2A6BAA1C1B43017AEDAF5EB6737D1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/UOMAf2D0R9qJLq5KCoPnUg/zh-cn_image_0000002583437861.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=CE565C0E3912D02A62B61D18BB9C8993CD17853B6ED78BBAAF0E8A5B9A9E08A0)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、分享的菜单。

TextInput:

```
1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
2. TextInput({ text: $r('app.string.show_selected_menu') })
```

[SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SelectMenu.ets#L26-L29)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/DoQCRPo_SqaZ8-vArIR_6A/zh-cn_image_0000002552957816.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=63B6A1CF43BE43FB77824430B4B58E7710259BB4B6B0408E5551898CED98FA5F)

TextArea:

```
1. // 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
2. TextArea({ text: $r('app.string.show_selected_menu') })
```

[SelectMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textInput/SelectMenu.ets#L30-L33)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/RI4d7OyGSvaRyydKfIGfEw/zh-cn_image_0000002583477817.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=8F35467818FF5F8D729BE5B337927E8D1A2E4D90E3DADA33BD29A42657B4FA71)

## 禁用系统服务类菜单

从API version 20开始，支持使用[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)方法屏蔽文本选择菜单中的所有系统服务菜单项。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/VAkrMtzmRh-XETXr_rTNsg/zh-cn_image_0000002552798168.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=3A6B899D7DD3F69F7E45622926832129E97F316B86D37902A5B273DEFA48594F)

从API version 20开始，支持使用[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)方法屏蔽文本选择菜单中指定的系统服务菜单项。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/PG3uSUVsTb27AnJAyoXEaQ/zh-cn_image_0000002583437863.png?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=2A961A59A6F92894C93238BA527D536BB5E9A3E2D0889460D2A4DC8B4EFF31DD)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/InYfWCMJQ8CcN0JW6ELngg/zh-cn_image_0000002552957818.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=12AE9DA67D6507E17A3291743FF188A9C8710BB9F02C152A551038BB3F895922)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/OrQWJ9VZSTiK9j26XH8hYw/zh-cn_image_0000002583477819.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=127D7A0B53DF65C13B85140F9E60B30CA5B5DBDA53D76F57180C39FECDB4438B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/uqLaScaHQjqxfsvDmNo5CA/zh-cn_image_0000002552798170.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=BB63AB1A29C095A6B90F38924860FF79F51C7A2F6B13BA821BAFD71A17E1BFA8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/IFNeKdygRga4p-DuFgI68Q/zh-cn_image_0000002583437865.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=8666BD72C91DAFBA03F897E9984158D509D16FC9542613929DB1CAD62256889A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/xXviYlwcQjKERTLJZ6e_UA/zh-cn_image_0000002552957820.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=0B26DCF019287FA2058B90E22FAEF99A42F2C055985CCB376C0E5700913A8694)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aDGC0cEgSnKz1aVqC_xlUA/zh-cn_image_0000002583477821.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233933Z&HW-CC-Expire=86400&HW-CC-Sign=995D55EF50887DBF63F50E0D8B2F5C8EAC19576B8B65552476FD4D470861D084)
