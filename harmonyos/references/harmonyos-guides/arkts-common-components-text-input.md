---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input
title: 文本输入 (TextInput/TextArea/Search)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 文本输入 (TextInput/TextArea/Search)
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3cfb64e262f81a45c0c6f4f3944a5ad965601d33c9d11e2e473f34854b239329
---

TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](../harmonyos-references/ts-basic-components-textinput.md)和[TextArea](../harmonyos-references/ts-basic-components-textarea.md)组件的API文档。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](../harmonyos-references/ts-basic-components-search.md)组件的API文档。

**说明** 

仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件。

## 创建输入框

TextInput是单行输入框，TextArea是多行输入框，Search是搜索框。通过以下接口创建这些组件。

```ts
TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

```ts
TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```ts
Search(options?:{placeholder?: ResourceStr, value?: ResourceStr, controller?: SearchController, icon?: string})
```

* 单行输入框。

  ```typescript
  TextInput()
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/GpGaWUKTQ8uAuSH7wgwOMA/zh-cn_image_0000002791564992.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A4586EDFC9E5489AC3358E4DC2E52758C0E19568783F47DEFFD01F1D01AE42D)
* 多行输入框。

  ```typescript
  TextArea()
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/patIBn7ZRSOdVqnhxJoIgg/zh-cn_image_0000002820524945.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=221A7D77DB1A7CDF7208CC25B2D882000D985EABE2D0862C771CF6757B758746)
* 多行输入框文字超出一行时会自动折行。

  ```typescript
  /* 请将$r('app.string.CreatTextInput_textContent')替换为实际资源文件，在本示例中该资源文件的value值为
   * "我是TextArea我是TextArea我是TextArea我是TextArea"
   */
  TextArea({ text: $r('app.string.CreatTextInput_textContent') })
    .width(300)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/c9fDROtLTmW9SWvAct933Q/zh-cn_image_0000002820404943.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C4ED765B865465B65B1BFD171B6601CF14EDC985E1B30B8765FDE68E248C64C)
* 搜索框。

  ```typescript
  Search()
    // 请将$r('app.string.Creat_TextInput_Content')替换为实际资源文件，在本示例中该资源文件的value值为"搜索"
    .searchButton($r('app.string.Creat_TextInput_Content'))
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Esu36jFpStmhFkF-MzWoeg/zh-cn_image_0000002791724966.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=E08443E354966A69C0136CB4011AD671245555896B458F4BE2196D1342C4FE43)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER\_NAME用户名输入模式、NEW\_PASSWORD新密码输入模式、NUMBER\_PASSWORD纯数字密码输入模式、NUMBER\_DECIMAL带小数点的数字输入模式、URL带链接的输入模式。通过[type](../harmonyos-references/ts-basic-components-textinput.md#type)属性进行设置：

### 基本输入模式（默认类型）

```typescript
TextInput()
  .type(InputType.Normal)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/IHp2xV06S4iqUYuoomkiOw/zh-cn_image_0000002791564994.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED19C609B3711CB1947587018941F6D595F0C39E093573B1D24020E62AC457D8)

### 密码模式

包括Password密码输入模式、NUMBER\_PASSWORD纯数字密码模式、NEW\_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```typescript
TextInput()
  .type(InputType.Password)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/pEPy4L2wR6KvLLHDwuHfPw/zh-cn_image_0000002820524947.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F8376A71EC6C31FA0CC7102F74375A665DA4582C86B54A4241652C3A237DAE1)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```typescript
TextInput()
  .type(InputType.Email)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/T-7o0TYySnC5mKl6RF70vQ/zh-cn_image_0000002820404945.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C3B3154BC64D8367D1051D79E0187E2286D8F6DF25EDEFFE3E33BCBC11A75E3)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```typescript
TextInput()
  .type(InputType.Number)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/GGucn_qnRe21vNk8sZsQGA/zh-cn_image_0000002791724968.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=4887872F7686FEC1A90BEE1E9C27060FD466D3DF6D7A282FE55EA4D3C75C83BB)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。

```typescript
TextInput()
  .type(InputType.PhoneNumber)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/CEFycdcxQ9qdG_0UrqO3eQ/zh-cn_image_0000002791564996.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=734B8FCF3A3307190821536D31951B026E26F59D828DFC00CBF35CACCC46CF6A)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```typescript
TextInput()
  .type(InputType.NUMBER_DECIMAL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/v5FFdz-hTbmN-9m8sJSo5w/zh-cn_image_0000002820524949.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FE3732DBEBAD20ABF71281C0775E06A209B895C27AECF81701BBE87591059AD)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```typescript
TextInput()
  .type(InputType.URL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/YrhaqTu5TNmwYvsNW0JmYQ/zh-cn_image_0000002820404947.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=08AE9DC78C2832F720EBFD1D7CB638EC8777894D31ECF42F899157111A373E18)

## 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](../harmonyos-references/ts-basic-components-textarea.md#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

### 默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

```typescript
TextArea()
  .style(TextContentStyle.DEFAULT)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/K_qtHts2TyCIUXfcIhIE0A/zh-cn_image_0000002791724970.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF5B7888ABA713B89A0CBE2C13DEAB989224A5AAA80F5F424EAC09DE0BF3C44E)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```typescript
TextArea()
  .style(TextContentStyle.INLINE)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/W_Jdg1baTka1rylF-DWGuQ/zh-cn_image_0000002791564998.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=6ACBEA285D7E1ED685F4A5E3BAE938C7D3B0FC5A772E2C78AA77EDB13439B010)

## 自定义样式

* 设置无输入时的提示文本。

  ```typescript
  // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  TextInput({ placeholder: $r('app.string.i_am_placeholder') })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/uPuH-1rlS7Kc-AJnsey9eg/zh-cn_image_0000002820524951.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AC4D36134FAEF848C9B3024F8325819160FCE344037ED4C0126EE92C9D9F658)
* 设置输入框当前的文本内容。

  ```typescript
  TextInput({
    // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
    placeholder: $r('app.string.i_am_placeholder'),
    // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
    text: $r('app.string.i_am_current_text_content')
  })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/DfjC173SRl2jXs0HZHKepA/zh-cn_image_0000002820404949.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=759238010FB4681FC1455A48CFB96C16345C7AF37C0A2E5FD0FA2CF004232CC0)
* 添加backgroundColor改变输入框的背景颜色。

  ```typescript
  TextInput({
    // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
    placeholder: $r('app.string.i_am_placeholder'),
    // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
    text: $r('app.string.i_am_current_text_content')
  })
    .backgroundColor(Color.Pink)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/caVuDYRpTraLXSlUaVo_Wg/zh-cn_image_0000002791724972.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8552508FB35D1E42694CCAF2C8C7739A4F91B2907118D9DC00240852D9DAB2D)

  更丰富的样式可以结合[通用属性](../harmonyos-references/ts-component-general-attributes.md)实现。

## 添加事件

文本框主要用于获取用户输入的信息，并将信息处理成数据进行上传，绑定[onChange](../harmonyos-references/ts-basic-components-textinput.md#onchange)事件可以获取输入框内改变的文本内容，绑定[onSubmit](../harmonyos-references/ts-basic-components-textinput.md#onsubmit)事件可以获取回车提交的文本信息，绑定[onTextSelectionChange](../harmonyos-references/ts-basic-components-textinput.md#ontextselectionchange10)事件可以获取文本选中时手柄的位置信息或者编辑时光标的位置信息等等。用户也可以使用通用事件进行相应的交互操作。

**说明** 

在密码模式下，设置[showPassword](../harmonyos-references/ts-basic-components-textinput.md#showpassword12)属性时，在[onSecurityStateChange](../harmonyos-references/ts-basic-components-textinput.md#onsecuritystatechange12)回调中，建议增加状态同步，具体详见如下示例。

[onWillInsert](../harmonyos-references/ts-basic-components-textinput.md#onwillinsert12)、[onDidInsert](../harmonyos-references/ts-basic-components-textinput.md#ondidinsert12)、[onWillDelete](../harmonyos-references/ts-basic-components-textinput.md#onwilldelete12)、[onDidDelete](../harmonyos-references/ts-basic-components-textinput.md#ondiddelete12)回调仅支持系统输入法的场景。

[onWillChange](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)的回调时序晚于[onWillInsert](../harmonyos-references/ts-basic-components-textinput.md#onwillinsert12)、[onWillDelete](../harmonyos-references/ts-basic-components-textinput.md#onwilldelete12)，早于[onDidInsert](../harmonyos-references/ts-basic-components-textinput.md#ondidinsert12)、[onDidDelete](../harmonyos-references/ts-basic-components-textinput.md#ondiddelete12)。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = '[Sample_Textcomponent]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent_';

@Entry
@Component
struct TextInputEventAdd {
  @State text: string = '';
  @State textStr1: string = '';
  @State textStr2: string = '';
  @State textStr3: string = '';
  @State textStr4: string = '';
  @State textStr5: string = '';
  @State textStr6: string = '';
  @State textStr7: string = '';
  @State textStr8: string = '';
  @State textStr9: string = '';
  @State passwordState: boolean = false;
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      Column() {
        Text(`${this.textStr1}\n${this.textStr2}\n${this.textStr3}
          \n${this.textStr4}\n${this.textStr5}\n${this.textStr6}
          \n${this.textStr7}\n${this.textStr8}\n${this.textStr9}`)
          .fontSize(20)
        TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
          .type(InputType.Password)
          .showPassword(this.passwordState)
          .onChange((value: string) => {
            // 文本内容发生变化时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onChange is triggering: ' + value);
            this.textStr1 = `onChange is triggering: ${value}`;
          })
          .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
            // 按下输入法回车键时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onSubmit is triggering: ' + enterKey + event.text);
            this.textStr2 = `onSubmit is triggering: ${enterKey} ${event.text}`;
          })
          .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
            // 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onTextSelectionChange is triggering: ' + selectionStart + selectionEnd);
            this.textStr3 = `onTextSelectionChange is triggering: ${selectionStart} ${selectionEnd}`;
          })
          .onSecurityStateChange((isShowPassword: boolean) => {
            // 密码显隐状态切换时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onSecurityStateChange is triggering: ' + isShowPassword);
            this.passwordState = isShowPassword;
            this.textStr4 = `onSecurityStateChange is triggering: ${isShowPassword}`;
          })
          .onWillInsert((info: InsertValue) => {
            // 在将要输入时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr5 = `onWillInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
            return true;
          })
          .onDidInsert((info: InsertValue) => {
            // 在输入完成时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr6 = `onDidInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
          })
          .onWillDelete((info: DeleteValue) => {
            // 在将要删除时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr7 = `onWillDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
            return true;
          })
          .onDidDelete((info: DeleteValue) => {
            // 在删除完成时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr8 = `onDidDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
          })
          .onFocus(() => {
            // 绑定通用事件，输入框获焦时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onFocus is triggering');
            this.textStr9 = `onFocus is triggering`;
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/0o1TJkdFRryL8CwM-icTHA/zh-cn_image_0000002791565000.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B56685743CECC157DD8A5E156568D684F20663C2978A57053767821B0528B8F)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、分享的菜单。

TextInput:

```typescript
// 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
TextInput({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/6OegO-VxQ0KER7zFstkxtw/zh-cn_image_0000002820524953.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=1800E02A44824BB758B50FC88D36D1CAE87B02D67F77C4436871092AE8762132)

TextArea:

```typescript
// 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
TextArea({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/XI5BXuUyT-CeD20Vitzlsg/zh-cn_image_0000002820404951.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D688FF16D6A551652FFB5B6C8E5CF1F45EC22309E82DF5F91229C771663AD2E)

## 禁用系统服务类菜单

从API version 20开始，支持使用[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)方法屏蔽文本选择菜单中的所有系统服务菜单项。更多详见[disableSystemServiceMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableSystemServiceMenuItem {
  aboutToAppear(): void {
    // 禁用所有系统服务菜单项
    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {
    // 页面消失时恢复系统服务菜单项
    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {
        // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems不包含被屏蔽的系统菜单项
              return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/-f_u3q_dREiSM37C5IytUw/zh-cn_image_0000002791724974.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDAFE362C5637AC7AED9D37C9E8C3AC59176CFB780DA42AC39E58B935EF0682D)

从API version 20开始，支持使用[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)方法屏蔽文本选择菜单中指定的系统服务菜单项。更多详见[disableMenuItems](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)的API文档接口说明。以下示例只是完整示例工程中的一个示例，为了不影响工程其他页面示例效果，仅在页面的出现和消失生命周期中进行系统服务菜单的禁用和恢复，实际场景可自行选择其他时机，比如[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableMenuItem {
  aboutToAppear(): void {
    // 禁用搜索，翻译和AI帮写
    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE, TextMenuItemId.AI_WRITER])
  }

  aboutToDisappear(): void {
    // 页面消失时恢复系统服务菜单项
    TextMenuController.disableMenuItems([])
  }

  build() {
    Row() {
      Column() {
        // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems不包含搜索、翻译和AI帮写
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
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/f_MTBO19TIKC22T91we0zA/zh-cn_image_0000002791565002.png?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=0628D0A92F14316686D221ADC5000313CA8C5B5356249EE88EC5EDFCB7E17DBC)

## 自动填充

输入框可以通过[contentType](../harmonyos-references/ts-basic-components-textinput.md#contenttype12)属性设置自动填充类型。

支持的类型请参考[ContentType](../harmonyos-references/ts-basic-components-textinput.md#contenttype12枚举说明)。

```typescript
// 请将$r('app.string.Auto_Fill_PlaceHolder')替换为实际资源文件，在本示例中该资源文件的value值为"输入你的邮箱..."
TextInput({ placeholder: $r('app.string.Auto_Fill_PlaceHolder') })
  .width('95%')
  .height(40)
  .margin(20)
  .contentType(ContentType.EMAIL_ADDRESS)
```

## 设置属性

* 设置省略属性。

  输入框可以通过[ellipsisMode](../harmonyos-references/ts-basic-components-textinput.md#ellipsismode18)属性设置省略位置。

  ellipsisMode属性需要配合[textOverflow](../harmonyos-references/ts-basic-components-textinput.md#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。

  ```typescript
  // 请将$r('app.string.Set_Omission_Property_textContent')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示省略模式"
  TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })
    .textOverflow(TextOverflow.Ellipsis)
    .ellipsisMode(EllipsisMode.END)
    .style(TextInputStyle.Inline)
    .fontSize(30)
    .margin(30)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/aaZPzkTLSaOR0B2cdo7F0A/zh-cn_image_0000002820524955.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=D689698DB20FCFA552F171E2539AAAE957B7A7E1C395DA21A914086BA44888C4)
* 设置文本描边属性。

  从API version 20开始，输入框可以通过[strokeWidth](../harmonyos-references/ts-basic-components-textinput.md#strokewidth20)和[strokeColor](../harmonyos-references/ts-basic-components-textinput.md#strokecolor20)属性设置文本的描边宽度及颜色。

  ```typescript
  TextInput({ text: 'Text with stroke' })
    .width('100%')
    .height(60)
    .borderWidth(1)
    .fontSize(40)
    .strokeWidth(LengthMetrics.px(3.0))
    .strokeColor(Color.Red)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/k93ih5yZTSmSbTsR7Zn51w/zh-cn_image_0000002820404953.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE1CAB2A6E54D6B2100056420B2CD641100AA564EFE6F46E042B7F5090B99113)

## 设置文本行间距

从API version 20开始，支持通过[lineSpacing](../harmonyos-references/ts-basic-components-text.md#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](../harmonyos-references/ts-text-common.md#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

```typescript
TextArea({
  text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
})
  .fontSize(22)
  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/PtHXB2E_QIKAF4p2Q6YXMA/zh-cn_image_0000002791724976.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE5B495C8ED4B9B926D5BFFBEBAF046921331FB6C0F26F8E55F861869F37DDAA)

## 键盘避让

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](../harmonyos-references/ts-container-scroll.md)、[List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)。

```typescript
@Entry
@Component
struct KeyboardAvoid {
  placeHolderArr: string[] = ['1', '2', '3', '4', '5', '6', '7'];

  build() {
    Scroll() {
      Column() {
        ForEach(this.placeHolderArr, (placeholder: string) => {
          TextInput({ placeholder: 'TextInput ' + placeholder })
            .margin(30)
            // ···
        })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/S0aHr6AXQhmyPF0GwmD3Bw/zh-cn_image_0000002791565004.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DE74289A9AAC3AEB67D784937DE0ED915883D4D9C9C9784A1C92241C5C7D956)

## 光标避让

[keyBoardAvoidMode](../harmonyos-references/arkts-apis-uicontext-e.md#keyboardavoidmode11)枚举中的OFFSET和RESIZE在键盘抬起后，不支持二次避让。如果想要支持光标位置在点击或者通过接口设置变化后发生二次避让，可以考虑使用OFFSET\_WITH\_CARET和RESIZE\_CARET替换原有的OFFSET和RESIZE模式。

对于滚动容器更推荐使用RESIZE\_WITH\_CARET，非滚动容器应该使用OFFSET\_WITH\_CARET。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { KeyboardAvoidMode } from '@kit.ArkUI';
```

```typescript
// Used in UIAbility
onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err, data) => {
    windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
    windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET_WITH_CARET);
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  });
}
```

```typescript
@Entry
@Component
struct CursorAvoid {
  @State caretPosition: number = 600;
  areaController: TextAreaController = new TextAreaController();
  text = 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot,' +
    ' or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy,' +
    ' totally forgetting that there is something happy in our own life.\
    So the best way to destroy happiness is to look at something and focus on even the smallest flaw. ' +
    'It is the smallest flaw that would make us complain. And it is the complaint that leads to us becoming unhappy.\
    If one chooses to be happy, he will be blessed; if he chooses to be unhappy, he will be cursed. ' +
    'Happiness is just what you think will make you happy.' +
    'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, ' +
    'or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life.\
  ';

  build() {
    Scroll() {
      Column() {
        Row() {
          Button('CaretPosition++: ' + this.caretPosition).onClick(() => {
            this.caretPosition += 1;
          }).fontSize(10)
          Button('CaretPosition--: ' + this.caretPosition).onClick(() => {
            this.caretPosition -= 1;
          }).fontSize(10)
          Button('SetCaretPosition: ').onClick(() => {
            this.areaController.caretPosition(this.caretPosition);
          }).fontSize(10)
        }

        TextArea({ text: this.text, controller: this.areaController })
          .width('100%')
          .fontSize('20fp')
      }
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/qnWjdyEVT3iK6jYerrJKNw/zh-cn_image_0000002820524957.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=693785E973A1D14F05E00C67DE295421494C83BEFCA79DE03C8F235166F572F8)

## 常见问题

### 如何设置TextArea的文本最少展示行数并自适应高度

**问题现象**

设置TextArea的初始高度来控制最少文本展示行数，当输入文本超过初始高度时，TextArea的高度自适应。

**解决措施**

设置[minLines](../harmonyos-references/ts-basic-components-textarea.md#minlines20)（从API version 20开始），或者设置height为"auto"，并使用[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)自行计算高度。

```typescript
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct TextExample {
  private textAreaPadding = 12;
  private setMaxLines = 3;
  private resourceManager = this.getUIContext().getHostContext()?.resourceManager;
  // 请在resources\base\element\string.json文件中配置name为'NormalQuestion_change'，value为非空字符串的资源
  private changeText = this.resourceManager?.getStringByNameSync('NormalQuestion_change') as string;
  @State fullText: string = this.changeText;
  @State originText: string = this.changeText;
  @State uiContext: UIContext = this.getUIContext();
  @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.originText,
    fontSize: 18
  });

  build() {
    Column() {
      TextArea({ text: 'minLines: ' + this.fullText })
        .fontSize(18)
        .width(300)
        .minLines(3)

      Blank(50)

      TextArea({ text: 'constraintSize: ' + this.fullText })
        .fontSize(18)
        .padding({ top: this.textAreaPadding, bottom: this.textAreaPadding })
        .width(300)
        .height('auto')
        .constraintSize({
          // 结合padding计算，设置至少显示this.setMaxLines行文本
          // 若涉及适老化字号缩放，需要监听并调整高度
          minHeight: this.textAreaPadding * 2 +
            this.setMaxLines * this.getUIContext().px2vp(Number(this.textSize.height))
        })

      Blank(50)
      // 请将$r('app.string.NormalQuestion_AddInput')替换为实际资源文件，在本示例中该资源文件的value值为"增加输入"
      Button($r('app.string.NormalQuestion_AddInput'))
        .onClick(() => {
          this.fullText += this.changeText;
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .padding({ top: 30 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/R1fFyB2fQxag8SyiYhGP6g/zh-cn_image_0000002820404955.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014740Z&HW-CC-Expire=31536000000&HW-CC-Sign=632D95CB736151D8B3C250845ED0857D021243F5593E90B710B27F8365073DA1)
