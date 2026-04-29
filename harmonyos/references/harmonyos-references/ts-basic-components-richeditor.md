---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor
title: RichEditor
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > RichEditor
category: harmonyos-references
scraped_at: 2026-04-29T13:52:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:495158dc3b5ede812ef8af4cb81f80dbe8990907c475866d311709bf8a843e47
---

支持图文混排和文本交互式编辑的组件。

说明

该组件从API version 10开始支持。后续版本新增内容，采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

### RichEditor

PhonePC/2in1TabletTVWearable

RichEditor(value: RichEditorOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorOptions](ts-basic-components-richeditor.md#richeditoroptions) | 是 | 富文本组件初始化选项。 |

### RichEditor12+

PhonePC/2in1TabletTVWearable

RichEditor(options: RichEditorStyledStringOptions)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12) | 是 | 富文本组件初始化选项。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

说明

* align属性只支持上方、中间和下方位置的对齐方式。
* 不支持[borderImage](ts-universal-attributes-border-image.md#borderimage)属性。
* 组件水平方向默认padding为16vp，竖直方向默认padding为8vp。

### customKeyboard

PhonePC/2in1TabletTVWearable

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions | undefined)

设置自定义键盘。

当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。

自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。

自定义键盘无法获取焦点，但是会拦截手势事件。

默认在输入控件失去焦点时，关闭自定义键盘。

自定义键盘支持接续功能，使用[setCustomKeyboardContinueFeature](arkts-apis-uicontext-uicontext.md#setcustomkeyboardcontinuefeature23)接口，可以设置自定义键盘之间切换时是否接续。

说明

从API version 23开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](ts-types.md#custombuilder8) | [ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)23+ | undefined23+ | 是 | 自定义键盘。  传入undefined时默认使用系统键盘。 |
| options12+ | [KeyboardOptions](ts-basic-components-richeditor.md#keyboardoptions12) | undefined23+ | 否 | 设置自定义键盘是否支持避让功能。  传入undefined时默认不支持避让。 |

### bindSelectionMenu

PhonePC/2in1TabletTVWearable

bindSelectionMenu(spanType: RichEditorSpanType, content: CustomBuilder, responseType: ResponseType | RichEditorResponseType, options?: SelectionMenuOptions)

设置自定义选择菜单。自定义菜单超长时，建议内部嵌套[Scroll](ts-container-scroll.md)组件使用，避免键盘被遮挡。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spanType | [RichEditorSpanType](ts-basic-components-richeditor.md#richeditorspantype) | 是 | 菜单的类型。  默认值：  RichEditorSpanType.TEXT |
| content | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 菜单的内容。 |
| responseType | [ResponseType](ts-appendix-enums.md#responsetype8) | [RichEditorResponseType](ts-basic-components-richeditor.md#richeditorresponsetype11) | 是 | 菜单的响应类型。  默认值：  ResponseType.LongPress |
| options | [SelectionMenuOptions](ts-basic-components-richeditor.md#selectionmenuoptions) | 否 | 菜单的选项。 |

### copyOptions

PhonePC/2in1TabletTVWearable

copyOptions(value: CopyOptions)

设置组件是否支持文本内容可复制粘贴。

从API version 20开始，RichEditor组件在执行复制或剪切操作时，会将HTML格式的内容添加到剪贴板中。

* 仅支持TextSpan和ImageSpan向剪贴板中添加HTML内容，其他Span类型（如BuilderSpan、SymbolSpan、CustomSpan）则不能添加。
* 设置RichEditor组件的属性字符串时，请参考属性字符串[toHtml](ts-universal-styled-string.md#tohtml14)接口文档，以了解支持转换为HTML的范围。

copyOptions不为CopyOptions.None时，长按组件内容，会弹出文本选择菜单。如果通过bindSelectionMenu等方式自定义文本选择菜单，则会弹出自定义的菜单。

设置copyOptions为CopyOptions.None时，禁用复制、剪切、翻译、分享、搜索、帮写功能，且不支持拖拽操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](ts-appendix-enums.md#copyoptions9) | 是 | 组件支持文本内容是否可复制粘贴。  默认值：CopyOptions.LocalDevice |

### enableDataDetector11+

PhonePC/2in1TabletTVWearable

enableDataDetector(enable: boolean)

设置是否进行文本特殊实体识别。

该接口依赖设备底层应具有文本识别能力，否则设置不会生效。

当enableDataDetector设置为true且未指定[dataDetectorConfig](ts-basic-components-richeditor.md#datadetectorconfig11)属性时，系统将默认识别所有类型的实体，并将这些实体的color和decoration更改为预设样式：

```
1. color: '#ff007dff'
2. decoration:{
3. type: TextDecorationType.Underline,
4. color: '#ff007dff',
5. style: TextDecorationStyle.SOLID
6. }
```

触摸点击或鼠标右键点击实体时，会根据实体类型弹出对应的实体操作菜单，鼠标左键点击实体会直接响应菜单的第一个选项。

对addBuilderSpan的节点文本，该功能不会生效。

当copyOptions设置为CopyOptions.None时，点击实体弹出的菜单没有选择文本和复制功能。

从API version 20开始，组件文本选择菜单支持显示AI菜单。

当enableDataDetector设置为true，并且[copyOptions](ts-basic-components-richeditor.md#copyoptions)设置为CopyOptions.LocalDevice或CopyOptions.CROSS\_DEVICE，组件在非编辑态选中内容，选中区包含单个AI实体时，根据AI实体的类型，在文本选择菜单中显示AI菜单选项。

AI菜单选项包括[TextMenuItemId](ts-text-common.md#textmenuitemid12)中的url（打开链接）、email（新建邮件）、phoneNumber（呼叫）、address（导航至该位置）、dateTime（新建日程提醒）。

从API version 20开始，组件文本选择菜单支持显示问问小艺。

组件在编辑态下，[copyOptions](ts-basic-components-richeditor.md#copyoptions)设置为CopyOptions.LocalDevice或CopyOptions.CROSS\_DEVICE，组件内选中任意文本内容时，文本选择菜单与鼠标右键菜单中都可以显示问问小艺选项。组件在非编辑态下，enableDataDetector设置为true，并且[copyOptions](ts-basic-components-richeditor.md#copyoptions)设置为CopyOptions.LocalDevice或CopyOptions.CROSS\_DEVICE，组件内选中文本，文本选择菜单与鼠标右键菜单中不显示其他AI菜单时，显示问问小艺选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 使能文本识别。  true表示使能文本特殊实体识别，false表示不使能文本特殊实体识别。  默认值： false |

### dataDetectorConfig11+

PhonePC/2in1TabletTVWearable

dataDetectorConfig(config: TextDataDetectorConfig)

设置文本特殊实体识别配置，可配置识别类型、实体显示样式，并可选择是否开启长按预览功能。

需配合[enableDataDetector](ts-basic-components-richeditor.md#enabledatadetector11)一起使用，设置enableDataDetector为true时，dataDetectorConfig的配置才能生效。

当有两个实体A、B重叠时，按以下规则保留实体：

1. 若A ⊂ B，则保留B，反之则保留A。

2. 当A ⊄ B且B ⊄ A时，若A.start < B.start，则保留A，反之则保留B。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [TextDataDetectorConfig](ts-text-common.md#textdatadetectorconfig11对象说明) | 是 | 文本识别配置。 |

### enableSelectedDataDetector22+

PhonePC/2in1TabletTVWearable

enableSelectedDataDetector(enable: boolean | undefined)

设置是否启用文本选择的AI菜单功能。启用后可识别选区中的邮件、电话、网址、日期、地址等，并在文本选择菜单中展示对应的AI菜单项。默认启用AI菜单功能。

AI菜单功能启用时，在组件中选中文本后，文本选择菜单能够展示对应的AI菜单项，包括[TextMenuItemId](ts-text-common.md#textmenuitemid12)中的url（打开连接）、email（新建邮件）、phoneNumber（呼叫）、address（导航前往）、dateTime（新建日程）。

AI菜单生效时，选中范围内需包括且仅包括一个完整的AI实体，才能展示对应的选项。该菜单项与[TextMenuItemId](ts-text-common.md#textmenuitemid12)中的askAI菜单项不同时出现。

本功能仅在[copyOptions](ts-basic-components-richeditor.md#copyoptions)为CopyOptions.LocalDevice或CopyOptions.CROSS\_DEVICE时生效。

该接口依赖设备底层具有文本识别能力，否则设置不会生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | undefined | 是 | 是否启用选择文本识别，true表示启用，false表示不启用。  传入undefined或null时属性重置为默认值。 |

### enablePreviewText12+

PhonePC/2in1TabletTVWearable

enablePreviewText(enable: boolean)

设置是否开启预上屏功能。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 使能预上屏功能。  true表示开启，false表示不开启。  默认值： true |

该接口在CAPI场景使用时默认关闭。可以在工程的module.json5中配置[metadata](../harmonyos-guides/module-structure.md#metadata对象内部结构)字段控制是否启用预上屏，配置如下：

```
1. "metadata": [
2. {
3. "name": "can_preview_text",
4. "value": "true"
5. }
6. ]
```

### placeholder12+

PhonePC/2in1TabletTVWearable

placeholder(value: ResourceStr, style?: PlaceholderStyle)

设置无输入时的提示文本。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 无输入时的提示文本。 |
| style | [PlaceholderStyle](ts-basic-components-richeditor.md#placeholderstyle12) | 否 | 提示文本的字体样式。  缺省时默认跟随主题。 |

### caretColor12+

PhonePC/2in1TabletTVWearable

caretColor(value: ResourceColor)

设置输入框光标、手柄颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 输入框光标、手柄颜色。  默认值：'#007DFF' |

### selectedBackgroundColor12+

PhonePC/2in1TabletTVWearable

selectedBackgroundColor(value: ResourceColor)

设置文本选中的底板颜色。如果未设置不透明度，默认为20%不透明度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 文本选中的底板颜色。  默认为20%不透明度。 |

### editMenuOptions12+

PhonePC/2in1TabletTVWearable

editMenuOptions(editMenu: EditMenuOptions)

设置系统默认菜单的扩展项，允许配置扩展项的文本内容、图标和回调方法。

调用[disableMenuItems](arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)或[disableSystemServiceMenuItems](arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)接口屏蔽文本选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法[onCreateMenu](ts-text-common.md#oncreatemenu12)的入参列表中不包含被屏蔽的菜单选项。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](ts-text-common.md#editmenuoptions) | 是 | 扩展菜单选项。 |

### enterKeyType12+

PhonePC/2in1TabletTVWearable

enterKeyType(value: EnterKeyType)

设置软键盘输入法回车键类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EnterKeyType](ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 软键盘输入法回车键类型。  默认为EnterKeyType.NEW\_LINE。 |

### enableKeyboardOnFocus12+

PhonePC/2in1TabletTVWearable

enableKeyboardOnFocus(isEnabled: boolean)

设置RichEditor通过点击以外的方式获焦时，是否主动拉起软键盘。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 通过点击以外的方式获焦时，是否主动拉起软键盘。  true表示主动拉起软键盘，false表示不主动拉起软键盘。  默认值： true |

### barState13+

PhonePC/2in1TabletTVWearable

barState(state: BarState)

设置RichEditor滚动条的显示模式。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [BarState](ts-appendix-enums.md#barstate) | 是 | 输入框滚动条的显示模式。  默认值：BarState.Auto |

### maxLength18+

PhonePC/2in1TabletTVWearable

maxLength(maxLength: Optional<number>)

设置组件内容的最大长度。当内容（包含文本、图片、Symbol和Builder）的总长度达到此值时，将无法继续添加内容。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxLength | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 文本的最大输入字符数。  默认值：Infinity，可以无限输入，支持undefined类型。  **说明：**  当不设置该属性或设置异常值时，取默认值，设置小数时，取整数部分。 |

### maxLines18+

PhonePC/2in1TabletTVWearable

maxLines(maxLines: Optional<number>)

设置富文本可显示的最大行数。maxLines为可显示行数，当设置maxLines时，超出内容可滚动显示。同时设置组件高度和最大行数，组件高度优先生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxLines | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 设置富文本可显示的最大行数。maxLines为可显示行数，当设置maxLines时，超出内容可滚动显示。同时设置组件高度和最大行数，组件高度优先生效。  默认值：UINT32\_MAX，可以无限输入，支持undefined类型。  取值范围：(0, UINT32\_MAX] |

### enableHapticFeedback13+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(isEnabled: boolean)

设置RichEditor是否支持触感反馈。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 控制触感反馈的开关。  默认值：true。true表示开启触感反馈，false表示关闭触感反馈。  **说明：**  触感反馈需应用具备ohos.permission.VIBRATE权限，用户已启用触感反馈，且系统硬件支持时才会生效。 |

### keyboardAppearance15+

PhonePC/2in1TabletTVWearable

keyboardAppearance(appearance: Optional<KeyboardAppearance>)

设置键盘外观。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appearance | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[KeyboardAppearance](ts-text-common.md#keyboardappearance15枚举说明)> | 是 | 键盘外观。  默认值：KeyboardAppearance.NONE\_IMMERSIVE |

### stopBackPress18+

PhonePC/2in1TabletTVWearable

stopBackPress(isStopped: Optional<boolean>)

设置是否阻止返回键传递。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isStopped | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否阻止返回键。  true表示阻止，false表示不阻止。  默认值：true。异常值取默认值。 |

### undoStyle20+

PhonePC/2in1TabletTVWearable

undoStyle(style: Optional<UndoStyle>)

设置撤销还原时是否保留原内容的样式。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建RichEditor组件时，撤销还原时默认保留原内容样式，不受该接口设置的属性影响。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[UndoStyle](ts-basic-components-richeditor.md#undostyle20-1)> | 是 | 撤销还原是否保留原样式选项。默认值：UndoStyle.CLEAR\_STYLE |

### enableAutoSpacing20+

PhonePC/2in1TabletTVWearable

enableAutoSpacing(enable: Optional<boolean>)

设置是否开启中文与西文的自动间距。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启中文与西文的自动间距。  true为开启自动间距，false为不开启。  默认值：false |

### scrollBarColor21+

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Optional<ColorMetrics>)

设置组件滚动条颜色。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 设置组件滚动条颜色。  默认值：'#66182431'，显示为灰色。  **说明：** 设置异常值时按默认值处理。 |

### includeFontPadding23+

PhonePC/2in1TabletTVWearable

includeFontPadding(include: Optional<boolean>)

设置是否在首行和尾行增加间距以避免文字截断。不通过该接口设置，默认不增加间距。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| include | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否在首行和尾行增加间距以避免文字截断。  true表示在首行和尾行增加间距；false表示在首行和尾行不增加间距。 |

### fallbackLineSpacing23+

PhonePC/2in1TabletTVWearable

fallbackLineSpacing(enabled: Optional<boolean>)

针对多行文字叠加，支持行高基于文字实际高度自适应。不通过该接口设置，默认行高不基于文字实际高度自适应。

该接口依赖[RichEditorTextStyle](ts-basic-components-richeditor.md#richeditortextstyle)的lineHeight属性。当lineHeight设置值小于当前字号下文本渲染出的实际高度时，fallbackLineSpacing属性将生效。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 行高是否基于文字实际高度自适应。  true表示行高基于文字实际高度自适应；false表示行高不基于文字实际高度自适应。 |

### compressLeadingPunctuation23+

PhonePC/2in1TabletTVWearable

compressLeadingPunctuation(enabled: Optional<boolean>)

设置是否开启行首标点符号压缩。

说明

行首标点符号默认不压缩。

支持压缩的标点符号，请参考[ParagraphStyle](js-apis-graphics-text.md#paragraphstyle)的行首压缩的标点范围。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启行首标点符号压缩。  true表示开启行首标点符号压缩；false表示不开启行首标点符号压缩。 |

### selectedDragPreviewStyle23+

PhonePC/2in1TabletTVWearable

selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)

设置拖动预览样式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SelectedDragPreviewStyle](ts-text-common.md#selecteddragpreviewstyle23对象说明) | undefined | 是 | 拖动预览样式。如果设置为undefined，样式将被重置。 |

### singleLine23+

PhonePC/2in1TabletTVWearable

singleLine(isEnable: boolean | undefined)

设置是否启用单行模式。未通过该接口设置时，默认不启用单行模式。

说明

单行模式不显示滚动条。

单行模式下换行符会显示为空格。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnable | boolean | undefined | 是 | 是否启用单行模式。  true表示启用单行模式；false表示不启用单行模式。  设置为undefined或null时，按照false处理，不启用单行模式。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持[OnDidChangeCallback](ts-text-common.md#ondidchangecallback12)、[StyledStringChangedListener](ts-text-common.md#styledstringchangedlistener12)、[StyledStringChangeValue](ts-text-common.md#styledstringchangevalue12)和以下事件：

### onReady

PhonePC/2in1TabletTVWearable

onReady(callback:Callback<void>)

富文本组件初始化完成后触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 订阅富文本组件初始化完成的回调。 |

### onSelect

PhonePC/2in1TabletTVWearable

onSelect(callback:Callback<[RichEditorSelection](ts-basic-components-richeditor.md#richeditorselection)>)

鼠标左键双击选中内容触发回调；松开鼠标左键再次触发回调。

手指长按选中内容触发回调；松开手指再次触发回调。

通过手指或鼠标连续修改选中区、三击选段场景，不回调onSelect。

需要实时感知选中区变化的场景和使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件，请使用onSelectionChange接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[RichEditorSelection](ts-basic-components-richeditor.md#richeditorselection)> | 是 | [RichEditorSelection](ts-basic-components-richeditor.md#richeditorselection)为选中的所有span信息。  选择时触发的回调。 |

### aboutToIMEInput

PhonePC/2in1TabletTVWearable

aboutToIMEInput(callback:Callback<[RichEditorInsertValue](ts-basic-components-richeditor.md#richeditorinsertvalue), boolean>)

输入法输入内容前触发回调。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[RichEditorInsertValue](ts-basic-components-richeditor.md#richeditorinsertvalue), boolean> | 是 | [RichEditorInsertValue](ts-basic-components-richeditor.md#richeditorinsertvalue)为输入法将要输入内容信息。  true:组件执行添加内容操作。  false:组件不执行添加内容操作。  输入法输入内容前的回调。 |

### onDidIMEInput12+

PhonePC/2in1TabletTVWearable

onDidIMEInput(callback:Callback<TextRange>)

输入法输入完成后，触发回调。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[TextRange](ts-text-common.md#textrange12)> | 是 | TextRange为输入法本次输入内容的范围。  输入法完成输入时的回调。 |

### onIMEInputComplete

PhonePC/2in1TabletTVWearable

onIMEInputComplete(callback:Callback<[RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult)>)

输入法输入完成后，触发回调。

该接口仅支持返回一个文本span的信息，当编辑操作涉及返回多个文本span信息时，建议使用[onDidIMEInput](ts-basic-components-richeditor.md#ondidimeinput12)接口。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult)> | 是 | [RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult)为输入法完成输入后的文本Span信息。  输入法完成输入后的回调。 |

### aboutToDelete

PhonePC/2in1TabletTVWearable

aboutToDelete(callback:Callback<[RichEditorDeleteValue](ts-basic-components-richeditor.md#richeditordeletevalue), boolean>)

输入法删除内容前，触发回调。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[RichEditorDeleteValue](ts-basic-components-richeditor.md#richeditordeletevalue), boolean> | 是 | [RichEditorDeleteValue](ts-basic-components-richeditor.md#richeditordeletevalue)为准备删除的内容所在的文本或者图片Span信息。  true:组件执行删除操作。  false:组件不执行删除操作。  输入法删除内容前的回调，英文预上屏点击候选词时会执行该回调。 |

### onDeleteComplete

PhonePC/2in1TabletTVWearable

onDeleteComplete(callback:Callback<void>)

输入法删除内容后，触发回调。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 订阅输入法完成删除内容的回调。 |

### onPaste11+

PhonePC/2in1TabletTVWearable

onPaste(callback: [PasteEventCallback](ts-basic-components-richeditor.md#pasteeventcallback12) )

粘贴时，触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的粘贴。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PasteEventCallback](ts-basic-components-richeditor.md#pasteeventcallback12) | 是 | 订阅粘贴时的回调。 |

### onSelectionChange12+

PhonePC/2in1TabletTVWearable

onSelectionChange(callback:Callback<[RichEditorRange](ts-basic-components-richeditor.md#richeditorrange)>)

内容选择区域或编辑状态下的光标位置发生变化时，将触发该回调。光标位置变化时，回调中选择区域的起始和终止位置相等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[RichEditorRange](ts-basic-components-richeditor.md#richeditorrange)> | 是 | [RichEditorRange](ts-basic-components-richeditor.md#richeditorrange)为所有内容的选择区域起始和终止位置。  订阅文本选择区域发生变化或编辑状态下光标位置发生变化时触发的回调。 |

### onEditingChange12+

PhonePC/2in1TabletTVWearable

onEditingChange(callback: Callback<boolean>)

组件内容的编辑状态发生变化时触发该回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | true表示编辑态，false表示非编辑态。 |

### onSubmit12+

PhonePC/2in1TabletTVWearable

onSubmit(callback: SubmitCallback)

按下软键盘输入法回车键时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SubmitCallback](ts-basic-components-richeditor.md#submitcallback12) | 是 | 订阅事件的回调。 |

### onWillChange12+

PhonePC/2in1TabletTVWearable

onWillChange(callback: Callback<[RichEditorChangeValue](ts-basic-components-richeditor.md#richeditorchangevalue12) , boolean>)

在组件执行增删操作前，触发回调。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[RichEditorChangeValue](ts-basic-components-richeditor.md#richeditorchangevalue12) , boolean> | 是 | [RichEditorChangeValue](ts-basic-components-richeditor.md#richeditorchangevalue12)为图文变化信息；boolean表示当前图文是否允许被更改，true：允许图文被更改；false：不允许图文被更改。 |

### onDidChange12+

PhonePC/2in1TabletTVWearable

onDidChange(callback: OnDidChangeCallback)

在组件执行增删操作后，触发回调。如果文本实际未发生增删，则不触发该回调。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnDidChangeCallback](ts-text-common.md#ondidchangecallback12) | 是 | 图文变化前后的内容范围。 |

### onCut12+

PhonePC/2in1TabletTVWearable

onCut(callback: Callback<CutEvent>)

剪切时触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的剪切。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件，默认支持图文的剪切。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CutEvent](ts-basic-components-richeditor.md#cutevent12)> | 是 | 定义用户剪切事件。 |

### onCopy12+

PhonePC/2in1TabletTVWearable

onCopy(callback: Callback<CopyEvent>)

复制时触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的复制。

使用[RichEditorStyledStringOptions](ts-basic-components-richeditor.md#richeditorstyledstringoptions12)构建的RichEditor组件，默认支持图文的复制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CopyEvent](ts-basic-components-richeditor.md#copyevent12)> | 是 | 定义用户复制事件。 |

### onWillAttachIME22+

PhonePC/2in1TabletTVWearable

onWillAttachIME(callback: Callback<IMEClient> | undefined)

在组件绑定输入法前，触发回调。

调用[IMEClient](ts-text-common.md#imeclient20对象说明)的[setExtraConfig](ts-text-common.md#setextraconfig22)方法设置输入法扩展信息。在绑定输入法成功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IMEClient](ts-text-common.md#imeclient20对象说明)> | undefined | 是 | 在组件绑定输入法前触发的回调。  值为undefined时清除已绑定的回调事件。 |

## RichEditorInsertValue

PhonePC/2in1TabletTVWearable

插入文本的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| insertOffset | number | 否 | 否 | 插入的文本偏移位置。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| insertValue | string | 否 | 否 | 插入的文本内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| previewText12+ | string | 否 | 是 | 插入的预上屏文本内容。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## RichEditorDeleteValue

PhonePC/2in1TabletTVWearable

删除操作和被删除内容的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 否 | 删除内容的偏移位置。 |
| direction | [RichEditorDeleteDirection](ts-basic-components-richeditor.md#richeditordeletedirection) | 否 | 否 | 删除操作的方向。 |
| length | number | 否 | 否 | 删除内容长度。 |
| richEditorDeleteSpans | Array<[RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult) | [RichEditorImageSpanResult](ts-basic-components-richeditor.md#richeditorimagespanresult)> | 否 | 否 | 删除的文本或图片Span的信息。 |

## RichEditorDeleteDirection

PhonePC/2in1TabletTVWearable

删除方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| BACKWARD | 向后删除。 |
| FORWARD | 向前删除。 |

## RichEditorTextSpanResult

PhonePC/2in1TabletTVWearable

文本Span信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | [RichEditorSpanPosition](ts-basic-components-richeditor.md#richeditorspanposition) | 否 | 否 | Span位置。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| value | string | 否 | 否 | 文本Span内容或Symbol的id。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textStyle | [RichEditorTextStyleResult](ts-basic-components-richeditor.md#richeditortextstyleresult) | 否 | 否 | 文本Span样式信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offsetInSpan | [number, number] | 否 | 否 | 文本Span内容里有效内容的起始和结束位置。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| valueResource11+ | [Resource](ts-types.md#resource) | 否 | 是 | 组件SymbolSpan内容。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| symbolSpanStyle11+ | [RichEditorSymbolSpanStyle](ts-basic-components-richeditor.md#richeditorsymbolspanstyle11) | 否 | 是 | 组件SymbolSpan样式信息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| paragraphStyle12+ | [RichEditorParagraphStyle](ts-basic-components-richeditor.md#richeditorparagraphstyle11) | 否 | 是 | 段落样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| previewText12+ | string | 否 | 是 | 文本Span预上屏内容。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| urlStyle19+ | [RichEditorUrlStyle](ts-basic-components-richeditor.md#richeditorurlstyle19) | 否 | 是 | url信息。  默认值：undefined  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## RichEditorSpanPosition

PhonePC/2in1TabletTVWearable

Span位置信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanIndex | number | 否 | 否 | Span索引值。 |
| spanRange | [number, number] | 否 | 否 | Span内容在RichEditor内的起始和结束位置。 |

## RichEditorSpanType

PhonePC/2in1TabletTVWearable

Span类型信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT | 0 | Span类型为文字。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| IMAGE | 1 | Span类型为图像。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MIXED | 2 | Span类型为图文混合。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BUILDER12+ | 3 | Span类型为BuilderSpan。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DEFAULT15+ | 4 | 注册此类型的菜单，但未注册TEXT、IMAGE、MIXED、BUILDER菜单时，文字类型、图像类型、图文混合类型、BuilderSpan类型都会触发并显示此类型对应的菜单。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## RichEditorResponseType11+

PhonePC/2in1TabletTVWearable

菜单的响应类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RIGHT\_CLICK | 0 | 通过鼠标右键触发菜单弹出。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LONG\_PRESS | 1 | 通过长按触发菜单弹出。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SELECT | 2 | 通过鼠标选中触发菜单弹出。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DEFAULT15+ | 3 | 注册此响应类型的菜单，但未注册RIGHT\_CLICK、LONG\_PRESS、SELECT响应类型的菜单时，通过鼠标右键、长按、鼠标选中都会触发菜单弹出。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## UndoStyle20+

PhonePC/2in1TabletTVWearable

撤销还原是否保留原样式选项。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLEAR\_STYLE | 0 | 撤销还原内容不保留原样式。 |
| KEEP\_STYLE | 1 | 撤销还原内容保留原样式。 |

## RichEditorTextStyleResult

PhonePC/2in1TabletTVWearable

后端返回的文本样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 文本颜色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontSize | number | 否 | 否 | 字体大小，默认单位为fp。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontStyle | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 否 | 字体样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontWeight | number | 否 | 否 | 字体粗细。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontFamily | string | 否 | 否 | 字体列表。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| decoration | [DecorationStyleResult](ts-text-common.md#decorationstyleresult12) | 否 | 否 | 文本装饰线样式信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textShadow12+ | Array<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明)> | 否 | 是 | 文字阴影效果。  **说明：**  仅支持查询阴影模糊半径、颜色和偏移量。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| lineHeight12+ | number | 否 | 是 | 文本行高，默认单位为fp。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| letterSpacing12+ | number | 否 | 是 | 文本字符间距，默认单位为fp。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontFeature12+ | string | 否 | 是 | 文字特性效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| halfLeading18+ | boolean | 否 | 是 | 文本是否将行间距平分至行的顶部与底部。  true表示将行间距平分至行的顶部与底部，false则不平分。  默认值：false。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| textBackgroundStyle18+ | [TextBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11对象说明) | 否 | 是 | 文本背景样式。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| strokeWidth23+ | number | 否 | 是 | 文本描边宽度。  单位为[vp](ts-pixel-units.md)。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| strokeColor23+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本描边颜色。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

在RichEditorTextStyle中，fontWeight是设置字体粗细的输入参数。

而在RichEditorTextStyleResult中，会将之前设置的字体粗细转换为数字后返回。

转换关系如下：

| RichEditorTextStyle中的fontWeight | RichEditorTextStyleResult中的fontWeight |
| --- | --- |
| 100 | 0 |
| 200 | 1 |
| 300 | 2 |
| 400 | 3 |
| 500 | 4 |
| 600 | 5 |
| 700 | 6 |
| 800 | 7 |
| 900 | 8 |
| Lighter | 12 |
| Normal | 10 |
| Regular | 14 |
| Medium | 13 |
| Bold | 9 |
| Bolder | 11 |

RichEditorSymbolSpanStyle和RichEditorSymbolSpanStyleResult中fontWeight的转换关系，与RichEditorTextStyle和RichEditorTextStyleResult中fontWeight的转换关系一致。

## RichEditorSymbolSpanStyleResult11+

PhonePC/2in1TabletTVWearable

后端返回的SymbolSpan样式信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | Array<[ResourceColor](ts-types.md#resourcecolor)> | 否 | 否 | SymbolSpan组件颜色。  默认值：不同渲染策略下默认值不同。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 否 | SymbolSpan组件大小，默认单位为fp。  默认值：跟随主题。 |
| fontWeight | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 否 | SymbolSpan组件粗细。  number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。  string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal。 |
| renderingStrategy | [SymbolRenderingStrategy](ts-basic-components-symbolglyph.md#symbolrenderingstrategy11枚举说明) | 否 | 否 | SymbolSpan组件渲染策略。  默认值：SymbolRenderingStrategy.SINGLE。 |
| effectStrategy | [SymbolEffectStrategy](ts-basic-components-symbolglyph.md#symboleffectstrategy11枚举说明) | 否 | 否 | SymbolSpan组件动效策略。  默认值：SymbolEffectStrategy.NONE。 |

## RichEditorImageSpanResult

PhonePC/2in1TabletTVWearable

后端返回的图片信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | [RichEditorSpanPosition](ts-basic-components-richeditor.md#richeditorspanposition) | 否 | 否 | Span位置。 |
| valuePixelMap | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 图片内容。 |
| valueResourceStr | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图片资源id。 |
| imageStyle | [RichEditorImageSpanStyleResult](ts-basic-components-richeditor.md#richeditorimagespanstyleresult) | 否 | 否 | 图片样式。 |
| offsetInSpan | [number, number] | 否 | 否 | Span里图片的起始和结束位置。 |

## RichEditorImageSpanStyleResult

PhonePC/2in1TabletTVWearable

后端返回的图片样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [number, number] | 否 | 否 | 图片的宽度和高度，单位为px。默认值：size的默认值与objectFit的值有关，不同的objectFit值对应的size默认值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| verticalAlign | [ImageSpanAlignment](ts-appendix-enums.md#imagespanalignment10) | 否 | 否 | 图片垂直对齐方式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| objectFit | [ImageFit](ts-appendix-enums.md#imagefit) | 否 | 否 | 图片缩放类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| layoutStyle12+ | [RichEditorLayoutStyle](ts-basic-components-richeditor.md#richeditorlayoutstyle11) | 否 | 是 | 图片布局风格。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## RichEditorLayoutStyle11+

PhonePC/2in1TabletTVWearable

图片布局信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| margin | [Dimension](ts-types.md#dimension10) | [Margin](ts-types.md#margin) | 否 | 是 | 外边距类型，用于描述组件不同方向的外边距。  参数为Dimension类型时，四个方向外边距同时生效。 |
| borderRadius | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 圆角类型，用于描述组件边框圆角半径。  参数为Dimension类型时，不支持以Percentage形式设置。 |

## RichEditorOptions

PhonePC/2in1TabletTVWearable

RichEditor初始化参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [RichEditorController](ts-basic-components-richeditor.md#richeditorcontroller) | 否 | 否 | 富文本控制器。 |

## RichEditorStyledStringOptions12+

PhonePC/2in1TabletTVWearable

RichEditor初始化参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [RichEditorStyledStringController](ts-basic-components-richeditor.md#richeditorstyledstringcontroller12) | 否 | 否 | 富文本控制器。 |

## RichEditorChangeValue12+

PhonePC/2in1TabletTVWearable

图文变化信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rangeBefore | [TextRange](ts-text-common.md#textrange12) | 否 | 否 | 即将被替换内容的开始和结束索引。 |
| replacedSpans | Array<[RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult)> | 否 | 否 | 替换后文本Span的具体信息。 |
| replacedImageSpans | Array<[RichEditorImageSpanResult](ts-basic-components-richeditor.md#richeditorimagespanresult)> | 否 | 否 | 替换后ImageSpan的具体信息。 |
| replacedSymbolSpans | Array<[RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult)> | 否 | 否 | 替换后SymbolSpan的具体信息。 |

## RichEditorBaseController12+

PhonePC/2in1TabletTVWearable

RichEditor组件控制器基类。

### getCaretOffset10+

PhonePC/2in1TabletTVWearable

getCaretOffset(): number

返回当前光标所在位置。

当无法获取光标位置时（例如controller未与组件绑定时），该接口返回-1。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前光标所在位置。 |

### setCaretOffset10+

PhonePC/2in1TabletTVWearable

setCaretOffset(offset: number): boolean

设置光标位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 光标偏移位置。超出所有内容范围时，设置失败。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 光标是否设置成功。  true表示光标位置设置成功，false表示未成功。 |

### closeSelectionMenu10+

PhonePC/2in1TabletTVWearable

closeSelectionMenu(): void

关闭自定义选择菜单或系统默认选择菜单。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getTypingStyle11+

PhonePC/2in1TabletTVWearable

getTypingStyle(): RichEditorTextStyle

获取用户预设的文本样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RichEditorTextStyle](ts-basic-components-richeditor.md#richeditortextstyle) | 用户预设样式。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### setTypingStyle11+

PhonePC/2in1TabletTVWearable

setTypingStyle(value: RichEditorTextStyle): void

设置用户预设的文本样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorTextStyle](ts-basic-components-richeditor.md#richeditortextstyle) | 是 | 预设样式。 |

### setTypingParagraphStyle20+

PhonePC/2in1TabletTVWearable

setTypingParagraphStyle(style: RichEditorParagraphStyle): void

设置用户预设的段落样式。仅在组件内容为空或组件末尾换行后，输入文本生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [RichEditorParagraphStyle](ts-basic-components-richeditor.md#richeditorparagraphstyle11) | 是 | 预设段落样式。 |

### setSelection11+

PhonePC/2in1TabletTVWearable

setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

支持设置组件内的内容选中，选中部分背板高亮。

selectionStart和selectionEnd均为-1时表示全选，均为0时可以清空选中区。

未获焦时调用该接口不产生选中效果。

从API version 12开始，在2in1设备中，无论options取何值，调用setSelection接口都不会弹出菜单，此外，如果组件中已经存在菜单，调用setSelection接口会关闭菜单。

在非2in1设备中，options取值为MenuPolicy.DEFAULT时，遵循以下规则：

1. 组件内有手柄菜单时，接口调用后不关闭菜单，并且调整菜单位置。
2. 组件内有不带手柄的菜单时，接口调用后不关闭菜单，并且菜单位置不变。
3. 组件内无菜单时，接口调用后也无菜单显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 选中开始位置。 |
| selectionEnd | number | 是 | 选中结束位置。 |
| options12+ | [SelectionOptions](ts-universal-attributes-text-style.md#selectionoptions12对象说明) | 否 | 选择项配置。 |

### isEditing12+

PhonePC/2in1TabletTVWearable

isEditing(): boolean

获取当前富文本的编辑状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true为编辑态，false为非编辑态。 |

### stopEditing12+

PhonePC/2in1TabletTVWearable

stopEditing(): void

退出编辑态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getLayoutManager12+

PhonePC/2in1TabletTVWearable

getLayoutManager(): LayoutManager

获取布局管理器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LayoutManager](ts-text-common.md#layoutmanager12) | 布局管理器对象。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### getPreviewText12+

PhonePC/2in1TabletTVWearable

getPreviewText(): PreviewText

获取预上屏信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PreviewText](ts-text-common.md#previewtext12) | 预上屏信息。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### getCaretRect18+

PhonePC/2in1TabletTVWearable

getCaretRect(): RectResult | undefined

返回当前光标与RichEditor组件的相对位置。如果光标不闪烁，返回undefined。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RectResult](ts-universal-attributes-on-child-touch-test.md#rectresult) | undefined | 当前光标与RichEditor的相对位置。 |

### deleteBackward23+

PhonePC/2in1TabletTVWearable

deleteBackward(): void

提供删除字符能力。没有内容被选中时，删除当前光标位置前的1个字符。有内容被选中时，删除选中内容。

该接口不支持预上屏场景使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RichEditorController

PhonePC/2in1TabletTVWearable

RichEditor组件的控制器，继承自[RichEditorBaseController](ts-basic-components-richeditor.md#richeditorbasecontroller12)。

说明

当内容的长度超过组件显示区域的高度时，调用插入接口（例如[addTextSpan](ts-basic-components-richeditor.md#addtextspan)、[addImageSpan](ts-basic-components-richeditor.md#addimagespan)、[addBuilderSpan](ts-basic-components-richeditor.md#addbuilderspan11)、[addSymbolSpan](ts-basic-components-richeditor.md#addsymbolspan11)），组件会自动滚动内容使得插入内容末尾可见。

### 导入对象

```
1. controller: RichEditorController = new RichEditorController();
```

### addTextSpan

PhonePC/2in1TabletTVWearable

addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number

添加文本内容，如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | 文本内容。  从API version 20开始，支持Resource类型。 |
| options | [RichEditorTextSpanOptions](ts-basic-components-richeditor.md#richeditortextspanoptions) | 否 | 文本选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的TextSpan在所有Span中的索引位置。 |

### addImageSpan

PhonePC/2in1TabletTVWearable

addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number

添加图片内容，如果组件光标闪烁，插入后光标位置更新为新插入图片的后面。

该接口为同步接口，在弱网环境下，直接添加网络图片可能会阻塞UI线程造成冻屏问题。不建议直接添加网络图片。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-apis-image-pixelmap.md) | [ResourceStr](ts-types.md#resourcestr) | 是 | 图片内容。 |
| options | [RichEditorImageSpanOptions](ts-basic-components-richeditor.md#richeditorimagespanoptions) | 否 | 图片选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的ImageSpan在所有Span中的索引位置。 |

### addBuilderSpan11+

PhonePC/2in1TabletTVWearable

addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number

在RichEditor中添加用户自定义布局（BuilderSpan）。

说明

* RichEditor组件添加占位Span，占位Span调用系统的measure方法计算真实的长宽和位置。
* 可通过[RichEditorBuilderSpanOptions](ts-basic-components-richeditor.md#richeditorbuilderspanoptions11)设置此builder在RichEditor中的index（一个文字为一个单位）。
* 此占位Span不可获焦，支持拖拽，支持部分通用属性，占位、删除等能力等同于ImageSpan，长度视为一个文字。
* 支持通过[bindSelectionMenu](ts-basic-components-richeditor.md#bindselectionmenu)设置自定义菜单。
* 不支持通过[getSpans](ts-basic-components-richeditor.md#getspans)，[getSelection](ts-basic-components-richeditor.md#getselection11)，[onSelect](ts-basic-components-richeditor.md#onselect)，[aboutToDelete](ts-basic-components-richeditor.md#abouttodelete)获取builderSpan信息。
* 不支持通过[updateSpanStyle](ts-basic-components-richeditor.md#updatespanstyle)，[updateParagraphStyle](ts-basic-components-richeditor.md#updateparagraphstyle11)等方式更新builder。
* 对此builder节点进行复制或粘贴不生效。
* builder的布局约束由RichEditor传入，如果builder里最外层组件不设置大小，则会用RichEditor的大小作为maxSize。
* builder的手势相关事件机制与通用手势事件相同，如果builder中未设置透传，则仅有builder中的子组件响应。
* 如果组件光标闪烁，插入后光标位置更新为新插入builder的后面。

通用属性仅支持[size](ts-universal-attributes-size.md#size)、[padding](ts-universal-attributes-size.md#padding)、[margin](ts-universal-attributes-size.md#margin)、[aspectRatio](ts-universal-attributes-layout-constraints.md#aspectratio)、[borderStyle](ts-universal-attributes-border.md#borderstyle)、[borderWidth](ts-universal-attributes-border.md#borderwidth)、[borderColor](ts-universal-attributes-border.md#bordercolor)、[borderRadius](ts-universal-attributes-border.md#borderradius)、[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、[backgroundBlurStyle](ts-universal-attributes-background.md#backgroundblurstyle9)、[opacity](ts-universal-attributes-opacity.md)、[blur](ts-universal-attributes-image-effect.md#blur)、[backdropBlur](ts-universal-attributes-background.md#backdropblur)、[shadow](ts-universal-attributes-image-effect.md#shadow)、[grayscale](ts-universal-attributes-image-effect.md#grayscale)、[brightness](ts-universal-attributes-image-effect.md#brightness)、[saturate](ts-universal-attributes-image-effect.md#saturate)、[contrast](ts-universal-attributes-image-effect.md#contrast)、[invert](ts-universal-attributes-image-effect.md#invert)、[sepia](ts-universal-attributes-image-effect.md#sepia)、[hueRotate](ts-universal-attributes-image-effect.md#huerotate)、[colorBlend](ts-universal-attributes-image-effect.md#colorblend)、[linearGradientBlur](ts-universal-attributes-image-effect.md#lineargradientblur12)、[clip](ts-universal-attributes-sharp-clipping.md#clip12)、[mask](ts-universal-attributes-sharp-clipping.md#mask12)、[foregroundBlurStyle](ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle)、[accessibilityGroup](ts-universal-attributes-accessibility.md#accessibilitygroup)、[accessibilityText](ts-universal-attributes-accessibility.md#accessibilitytext)、[accessibilityDescription](ts-universal-attributes-accessibility.md#accessibilitydescription)、[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)、[sphericalEffect](ts-universal-attributes-image-effect.md#sphericaleffect12)、[lightUpEffect](ts-universal-attributes-image-effect.md#lightupeffect12)、[pixelStretchEffect](ts-universal-attributes-image-effect.md#pixelstretcheffect12)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义组件。 |
| options | [RichEditorBuilderSpanOptions](ts-basic-components-richeditor.md#richeditorbuilderspanoptions11) | 否 | builder选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的builderSpan在所有Span中的索引位置。 |

### addSymbolSpan11+

PhonePC/2in1TabletTVWearable

addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number

在RichEditor中添加图标小符号（SymbolSpan），如果组件光标闪烁，插入后光标位置更新为新插入SymbolSpan的后面。

暂不支持手势、复制、拖拽处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Resource](ts-types.md#resource) | 是 | symbol资源信息。 |
| options | [RichEditorSymbolSpanOptions](ts-basic-components-richeditor.md#richeditorsymbolspanoptions11) | 否 | symbol选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的SymbolSpan在所有Span中的索引位置。 |

### updateSpanStyle

PhonePC/2in1TabletTVWearable

updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void

更新文本、图片或SymbolSpan样式。

若只更新了一个Span的部分内容，则会根据更新部分、未更新部分将该Span拆分为多个Span。

使用该接口更新文本、图片或SymbolSpan样式时默认不会关闭自定义文本选择菜单。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorUpdateTextSpanStyleOptions](ts-basic-components-richeditor.md#richeditorupdatetextspanstyleoptions) | [RichEditorUpdateImageSpanStyleOptions](ts-basic-components-richeditor.md#richeditorupdateimagespanstyleoptions) | [RichEditorUpdateSymbolSpanStyleOptions](ts-basic-components-richeditor.md#richeditorupdatesymbolspanstyleoptions11) | 是 | 文本、图片或SymbolSpan的样式选项信息。 |

说明

当start大于end时为异常情况，此时start为0，end为无穷大。

### updateParagraphStyle11+

PhonePC/2in1TabletTVWearable

updateParagraphStyle(value: RichEditorParagraphStyleOptions): void

更新段落的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorParagraphStyleOptions](ts-basic-components-richeditor.md#richeditorparagraphstyleoptions11) | 是 | 段落的样式选项信息。 |

### getSpans

PhonePC/2in1TabletTVWearable

getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>

获取span信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorRange](ts-basic-components-richeditor.md#richeditorrange) | 否 | 需要获取span范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[RichEditorImageSpanResult](ts-basic-components-richeditor.md#richeditorimagespanresult) | [RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult)> | 文本和图片Span信息。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### deleteSpans

PhonePC/2in1TabletTVWearable

deleteSpans(value?: RichEditorRange): void

删除指定范围内的文本和图片。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorRange](ts-basic-components-richeditor.md#richeditorrange) | 否 | 删除范围。省略时，删除所有文本和图片。 |

### getParagraphs11+

PhonePC/2in1TabletTVWearable

getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>

获取指定范围的段落信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorRange](ts-basic-components-richeditor.md#richeditorrange) | 否 | 需要获取段落的范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[RichEditorParagraphResult](ts-basic-components-richeditor.md#richeditorparagraphresult11)> | 选中段落的信息。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### getSelection11+

PhonePC/2in1TabletTVWearable

getSelection(): RichEditorSelection

获取选中内容的范围和span信息。未选中时，返回光标所在span信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RichEditorSelection](ts-basic-components-richeditor.md#richeditorselection) | 选中内容信息。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### fromStyledString12+

PhonePC/2in1TabletTVWearable

fromStyledString(value: StyledString): Array<RichEditorSpan>

将属性字符串转换为span信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | 转换前的属性字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[RichEditorSpan](ts-basic-components-richeditor.md#richeditorspan12)> | 文本和图片Span信息。 |

**错误码：**

以下错误码的详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

### toStyledString12+

PhonePC/2in1TabletTVWearable

toStyledString(value: RichEditorRange): StyledString

将给定范围的组件内容转换成属性字符串，SymbolSpan和BuilderSpan不支持转换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RichEditorRange](ts-basic-components-richeditor.md#richeditorrange) | 是 | 需要获取的范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StyledString](ts-universal-styled-string.md#styledstring) | 转换后的属性字符串 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

## RichEditorStyledStringController12+

PhonePC/2in1TabletTVWearable

使用属性字符串构建的RichEditor组件的控制器，继承自[RichEditorBaseController](ts-basic-components-richeditor.md#richeditorbasecontroller12)。

### 导入对象

```
1. controller: RichEditorStyledStringController = new RichEditorStyledStringController();
```

### getSelection12+

PhonePC/2in1TabletTVWearable

getSelection(): RichEditorRange

获取富文本当前的选中区域范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RichEditorRange](ts-basic-components-richeditor.md#richeditorrange) | 选中区域范围。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### setStyledString12+

PhonePC/2in1TabletTVWearable

setStyledString(styledString: StyledString): void

设置富文本组件显示的属性字符串。

说明

* 调用该接口时，会全量替换富文本组件的StyledString，并重新渲染。
* 当内容超过组件本身区域时，组件会自动向上滚动内容直到末尾处可见。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styledString | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | 属性字符串。  **说明：**  StyledString的子类[MutableStyledString](ts-universal-styled-string.md#mutablestyledstring)也可以作为入参值。 |

### getStyledString12+

PhonePC/2in1TabletTVWearable

getStyledString(): MutableStyledString

获取富文本组件显示的属性字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MutableStyledString](ts-universal-styled-string.md#mutablestyledstring) | 富文本组件显示的属性字符串。  当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

### onContentChanged12+

PhonePC/2in1TabletTVWearable

onContentChanged(listener: StyledStringChangedListener): void

注册文本内容变化回调，该回调仅在后端程序导致文本内容变更时触发，调用[setStyledString](ts-basic-components-richeditor.md#setstyledstring12)时不会触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [StyledStringChangedListener](ts-text-common.md#styledstringchangedlistener12) | 是 | 文本内容变化回调监听器。 |

## RichEditorSelection

PhonePC/2in1TabletTVWearable

选中内容信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selection | [number, number] | 否 | 否 | 选中范围。 |
| spans | Array<[RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult) | [RichEditorImageSpanResult](ts-basic-components-richeditor.md#richeditorimagespanresult)> | 否 | 否 | span信息。 |

## RichEditorRange

PhonePC/2in1TabletTVWearable

定义RichEditor的范围。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 需要更新样式的文本起始位置，省略或者设置负值时表示从0开始。 |
| end | number | 否 | 是 | 需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。 |

## RichEditorSpanStyleOptions

PhonePC/2in1TabletTVWearable

文本样式选项。

继承自[RichEditorRange](ts-basic-components-richeditor.md#richeditorrange)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RichEditorUpdateTextSpanStyleOptions

PhonePC/2in1TabletTVWearable

文本样式选项。

继承自[RichEditorSpanStyleOptions](ts-basic-components-richeditor.md#richeditorspanstyleoptions)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textStyle | [RichEditorTextStyle](ts-basic-components-richeditor.md#richeditortextstyle) | 否 | 否 | 文本样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| urlStyle19+ | [RichEditorUrlStyle](ts-basic-components-richeditor.md#richeditorurlstyle19) | 否 | 是 | url信息。  默认值：undefined  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## RichEditorUpdateImageSpanStyleOptions

PhonePC/2in1TabletTVWearable

图片的样式选项。

继承自[RichEditorSpanStyleOptions](ts-basic-components-richeditor.md#richeditorspanstyleoptions)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageStyle | [RichEditorImageSpanStyle](ts-basic-components-richeditor.md#richeditorimagespanstyle) | 否 | 否 | 图片样式。 |

## RichEditorUpdateSymbolSpanStyleOptions11+

PhonePC/2in1TabletTVWearable

SymbolSpan样式选项。

继承自[RichEditorSpanStyleOptions](ts-basic-components-richeditor.md#richeditorspanstyleoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbolStyle | [RichEditorSymbolSpanStyle](ts-basic-components-richeditor.md#richeditorsymbolspanstyle11) | 否 | 否 | 组件样式。 |

## RichEditorParagraphStyleOptions11+

PhonePC/2in1TabletTVWearable

段落样式选项。

继承自[RichEditorRange](ts-basic-components-richeditor.md#richeditorrange)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [RichEditorParagraphStyle](ts-basic-components-richeditor.md#richeditorparagraphstyle11) | 否 | 否 | 段落样式。 |

说明

接口作用的范围：设定的区间所涉及的段落。

## RichEditorParagraphStyle11+

PhonePC/2in1TabletTVWearable

段落样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textAlign | [TextAlign](ts-appendix-enums.md#textalign) | 否 | 是 | 设置文本段落在水平方向的对齐方式。默认值：TextAlign.START  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| leadingMargin | [Dimension](ts-types.md#dimension10) | [LeadingMarginPlaceholder](ts-basic-components-richeditor.md#leadingmarginplaceholder11) | 否 | 是 | 设置文本段落缩进，当段落仅存在ImageSpan或BuilderSpan时，此属性值不生效。参数为Dimension类型时，不支持以Percentage形式设置。默认值：{"size":["0.00px","0.00px"]}  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| wordBreak12+ | [WordBreak](ts-appendix-enums.md#wordbreak11) | 否 | 是 | 设置断行规则。  默认值：WordBreak.BREAK\_WORD  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| lineBreakStrategy12+ | [LineBreakStrategy](ts-appendix-enums.md#linebreakstrategy12) | 否 | 是 | 设置折行规则。  默认值：LineBreakStrategy.GREEDY  在wordBreak不等于breakAll的时候生效，不支持连字符。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| paragraphSpacing19+ | number | 否 | 是 | 设置段落间距大小。  单位：fp  段落间距默认大小为0。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| textVerticalAlign20+ | [TextVerticalAlign](ts-text-common.md#textverticalalign20) | 否 | 是 | 设置文本段落在垂直方向的对齐方式。  默认值：TextVerticalAlign.BASELINE  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| textDirection23+ | [TextDirection](ts-text-common.md#textdirection22) | 否 | 是 | 设置文本方向。  默认值：TextDirection.DEFAULT  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## LeadingMarginPlaceholder11+

PhonePC/2in1TabletTVWearable

前导边距占位符，用于表示文本段落左侧与组件边缘之间的距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 图片内容。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| size | [[Dimension](ts-types.md#dimension10), [Dimension](ts-types.md#dimension10)] | 否 | 否 | 图片大小，不支持设置百分比。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## RichEditorParagraphResult11+

PhonePC/2in1TabletTVWearable

后端返回的段落信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [RichEditorParagraphStyle](ts-basic-components-richeditor.md#richeditorparagraphstyle11) | 否 | 否 | 段落样式。 |
| range | [number, number] | 否 | 否 | 段落起始和结束位置。 |

## RichEditorTextSpanOptions

PhonePC/2in1TabletTVWearable

添加文本的偏移位置和文本样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加文本的位置。省略时，添加到所有内容的最后。  当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| style | [RichEditorTextStyle](ts-basic-components-richeditor.md#richeditortextstyle) | 否 | 是 | 文本样式信息。省略时，使用系统默认文本信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| paragraphStyle11+ | [RichEditorParagraphStyle](ts-basic-components-richeditor.md#richeditorparagraphstyle11) | 否 | 是 | 段落样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| gesture11+ | [RichEditorGesture](ts-basic-components-richeditor.md#richeditorgesture11) | 否 | 是 | 行为触发回调。省略时，仅使用系统默认行为。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| urlStyle19+ | [RichEditorUrlStyle](ts-basic-components-richeditor.md#richeditorurlstyle19) | 否 | 是 | url信息。  默认值：undefined  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## RichEditorTextStyle

PhonePC/2in1TabletTVWearable

文本样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本颜色。  默认值：$r('sys.color.font\_primary')。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontSize | [Length](ts-types.md#length) | number | 否 | 是 | 设置字体大小，Length为number类型时，使用fp单位。字体默认大小16。不支持设置百分比字符串。字体大小设置为0时，显示默认字体大小。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontStyle | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 是 | 字体样式。  默认值：FontStyle.Normal。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontWeight | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 是 | 字体粗细。  number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。  string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontFamily | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和[注册自定义字体](js-apis-font.md)。  默认字体:'HarmonyOS Sans'。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| decoration | [DecorationStyleInterface](ts-universal-styled-string.md#decorationstyleinterface) | 否 | 是 | 设置文本装饰线的样式、颜色和粗细。  type默认值：TextDecorationType.None  color默认值：跟随字体颜色。  style默认值：TextDecorationStyle.SOLID  thicknessScale默认值：1.0  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textShadow11+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | Array<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明)> | 否 | 是 | 设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。  **说明：**  仅支持设置阴影模糊半径、颜色和偏移量，不支持智能取色。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| lineHeight12+ | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小。number类型时单位为fp，不支持设置百分比字符串。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| letterSpacing12+ | number | string | 否 | 是 | 设置文本字符间距，当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示，number类型时单位为fp，不支持设置百分比字符串。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontFeature12+ | string | 否 | 是 | 设置文字特性效果，比如数字等宽的特性。如果未设置，默认为变宽数字。设置无效字符保持默认。  格式为：normal | <feature-tag-value>  <feature-tag-value>的格式为：<string> [ <integer> | on | off ]  <feature-tag-value>的个数可以有多个，中间用','隔开。  例如，使用等宽时钟数字的输入格式为："ss01" on。  Font Feature当前支持的属性见 [fontFeature属性列表](ts-basic-components-text.md#fontfeature12)。  设置 Font Feature 属性，Font Feature 是 OpenType 字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持。  更多 Font Feature 能力介绍可参考 <https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop> 和 <https://sparanoid.com/lab/opentype-features/>  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| halfLeading18+ | boolean | 否 | 是 | 文本是否将行间距平分至行的顶部与底部。  true表示将行间距平分至行的顶部与底部，false则不平分。  默认值：false。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| textBackgroundStyle18+ | [TextBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11对象说明) | 否 | 是 | 文本背景样式。  默认值：  {  color: Color.Transparent,  radius: 0  }  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| strokeWidth23+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | number | 否 | 是 | 文本描边宽度。如果LengthMetrics的unit值是[PERCENT](js-apis-arkui-graphics.md#lengthunit12)，当前设置不生效，作为0处理。  值小于0时为实体字，大于0时为轮廓字，等于0时无描边效果。  默认值：0vp。  单位：LengthMetrics类型时跟随LengthMetrics，number类型时是vp。  取值范围：(-∞, +∞)  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| strokeColor23+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本描边颜色。  默认值：跟随字体颜色。  设置异常值时跟随字体颜色。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## PlaceholderStyle12+

PhonePC/2in1TabletTVWearable

设置提示文本的字体样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| font | [Font](ts-types.md#font) | 否 | 是 | 设置placeholder文本样式。  默认值遵循主题设置。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置placeholder文本颜色。  默认值遵循主题设置。 |

## RichEditorImageSpanOptions

PhonePC/2in1TabletTVWearable

设置图片的偏移位置和图片样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加图片的位置。省略时，添加到所有内容的末尾。  当值小于0时，设置在所有内容最前面；当值大于所有内容长度时，设置在所有内容最后面。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| imageStyle | [RichEditorImageSpanStyle](ts-basic-components-richeditor.md#richeditorimagespanstyle) | 否 | 是 | 图片样式信息。省略时，使用系统默认图片信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| gesture11+ | [RichEditorGesture](ts-basic-components-richeditor.md#richeditorgesture11) | 否 | 是 | 行为触发回调。省略时，仅使用系统默认行为。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onHover14+ | [OnHoverCallback](ts-basic-components-richeditor.md#onhovercallback14) | 否 | 是 | 鼠标悬停触发回调。省略时，不执行相关行为。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## RichEditorImageSpanStyle

PhonePC/2in1TabletTVWearable

图片样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [[Dimension](ts-types.md#dimension10), [Dimension](ts-types.md#dimension10)] | 否 | 是 | 图片宽度和高度。默认值：与objectFit的值相关，不同的objectFit值有不同的默认尺寸。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，宽度为组件宽度减去组件左右内边距。不支持以Percentage形式设置。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| verticalAlign | [ImageSpanAlignment](ts-appendix-enums.md#imagespanalignment10) | 否 | 是 | 图片垂直对齐方式。  默认值:ImageSpanAlignment.BOTTOM  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| objectFit | [ImageFit](ts-appendix-enums.md#imagefit) | 否 | 是 | 图片缩放类型。  默认值:ImageFit.Cover。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| layoutStyle11+ | [RichEditorLayoutStyle](ts-basic-components-richeditor.md#richeditorlayoutstyle11) | 否 | 是 | 图片布局风格。默认值：{"borderRadius":"","margin":""}    **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## RichEditorSymbolSpanOptions11+

PhonePC/2in1TabletTVWearable

设置SymbolSpan组件的偏移位置和样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加组件的位置。省略时，添加到所有内容的最后。  如果值小于0，添加到所有内容的最前面；如果值大于所有内容的长度，添加到所有内容的最后面。 |
| style | [RichEditorSymbolSpanStyle](ts-basic-components-richeditor.md#richeditorsymbolspanstyle11) | 否 | 是 | 组件样式信息。省略时，使用系统默认样式信息。 |

## RichEditorSymbolSpanStyle11+

PhonePC/2in1TabletTVWearable

组件SymbolSpan样式信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | Array<[ResourceColor](ts-types.md#resourcecolor)> | 否 | 是 | 设置SymbolSpan组件颜色。  默认值：不同渲染策略下默认值不同。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置SymbolSpan组件大小，默认单位为fp。  默认值：跟随主题。 |
| fontWeight | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 是 | 设置SymbolSpan组件粗细。  number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。  string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal。 |
| renderingStrategy | [SymbolRenderingStrategy](ts-basic-components-symbolglyph.md#symbolrenderingstrategy11枚举说明) | 否 | 是 | 设置SymbolSpan组件渲染策略。  默认值：SymbolRenderingStrategy.SINGLE。 |
| effectStrategy | [SymbolEffectStrategy](ts-basic-components-symbolglyph.md#symboleffectstrategy11枚举说明) | 否 | 是 | 设置SymbolSpan组件动效策略。  默认值：SymbolEffectStrategy.NONE。 |

## RichEditorBuilderSpanOptions11+

PhonePC/2in1TabletTVWearable

设置builder的偏移位置和样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加builder的位置。省略或者为异常值时，添加到所有内容的最后。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilitySpanOptions23+ | [AccessibilitySpanOptions](ts-text-common.md#accessibilityspanoptions23对象说明) | 否 | 是 | 无障碍朗读功能属性。缺省时，取[AccessibilitySpanOptions](ts-text-common.md#accessibilityspanoptions23对象说明)的默认值。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## RichEditorSpan12+

PhonePC/2in1TabletTVWearable

type RichEditorSpan = RichEditorImageSpanResult | RichEditorTextSpanResult

RichEditor span信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [RichEditorImageSpanResult](ts-basic-components-richeditor.md#richeditorimagespanresult) | 后端返回的图片信息。 |
| [RichEditorTextSpanResult](ts-basic-components-richeditor.md#richeditortextspanresult) | 后端返回的文本信息。 |

## SelectionMenuOptions

PhonePC/2in1TabletTVWearable

菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onAppear | [MenuOnAppearCallback](ts-basic-components-richeditor.md#menuonappearcallback12) | 否 | 是 | 自定义选择菜单弹出时回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onDisappear | Callback<void> | 否 | 是 | 自定义选择菜单关闭时回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| menuType13+ | [MenuType](ts-text-common.md#menutype13枚举说明) | 否 | 是 | 自定义选择菜单类型。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  默认值：MenuType.SELECTION\_MENU。 |
| onMenuShow15+ | [MenuCallback](ts-basic-components-richeditor.md#menucallback15) | 否 | 是 | 自定义选择菜单显示时回调。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| onMenuHide15+ | [MenuCallback](ts-basic-components-richeditor.md#menucallback15) | 否 | 是 | 自定义选择菜单隐藏时回调。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| previewMenuOptions18+ | [PreviewMenuOptions](ts-basic-components-richeditor.md#previewmenuoptions18) | 否 | 是 | 预览菜单的选项。该参数只在RichEditor中生效。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## PreviewMenuOptions18+

PhonePC/2in1TabletTVWearable

预览菜单的选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hapticFeedbackMode | [HapticFeedbackMode](ts-universal-attributes-menu.md#hapticfeedbackmode18) | 否 | 是 | 菜单弹出时振动效果，当ImageSpan或BuilderSpan绑定预览菜单时生效。  默认值：HapticFeedbackMode.DISABLED，菜单弹出时不振动。  **说明：** 仅当应用具备ohos.permission.VIBRATE权限，且用户启用了触感反馈时才会生效。 |

## PasteEvent11+

PhonePC/2in1TabletTVWearable

定义用户粘贴事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| preventDefault | Callback<void> | 否 | 是 | 阻止系统默认粘贴事件。 |

## CutEvent12+

PhonePC/2in1TabletTVWearable

定义用户剪切事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| preventDefault | Callback<void> | 否 | 是 | 阻止系统默认剪切事件。 |

## CopyEvent12+

PhonePC/2in1TabletTVWearable

定义用户复制事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| preventDefault | Callback<void> | 否 | 是 | 阻止组件的默认复制操作。 |

## RichEditorGesture11+

PhonePC/2in1TabletTVWearable

用户手势事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onClick | Callback<[ClickEvent](ts-universal-events-click.md#clickevent)> | 否 | 是 | [ClickEvent](ts-universal-events-click.md#clickevent)为用户点击事件。  点击完成时回调事件。  双击时，第一次点击触发回调事件。 |
| onLongPress | Callback<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 否 | 是 | [GestureEvent](ts-gesture-common.md#gestureevent对象说明)为用户长按事件。  长按完成时回调事件。 |

## KeyboardOptions12+

PhonePC/2in1TabletTVWearable

设置自定义键盘是否支持避让功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportAvoidance | boolean | 否 | 是 | 设置自定义键盘是否支持避让功能。默认值为 false，表示不支持避让；true 表示支持避让。 |

## SubmitCallback12+

PhonePC/2in1TabletTVWearable

type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void

软键盘按下回车键时的回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterKey | [EnterKeyType](ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 软键盘输入法回车键类型。具体类型见EnterKeyType枚举说明。 |
| event | [SubmitEvent](ts-basic-components-textinput.md#submitevent11) | 是 | 当提交的时候，提供保持组件编辑状态的方法。EnterKeyType指定为NEW\_LINE时，默认保持编辑态。 |

## MenuOnAppearCallback12+

PhonePC/2in1TabletTVWearable

type MenuOnAppearCallback = (start: number, end: number) => void

自定义选择菜单弹出时触发的回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 选中内容的起始位置。 |
| end | number | 是 | 选中内容的终止位置。 |

## MenuCallback15+

PhonePC/2in1TabletTVWearable

type MenuCallback = (start: number, end: number) => void

自定义选择菜单显示或隐藏时触发的回调事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 选中内容的起始位置。 |
| end | number | 是 | 选中内容的终止位置。 |

## PasteEventCallback12+

PhonePC/2in1TabletTVWearable

type PasteEventCallback = (event?: PasteEvent) => void

粘贴完成前，触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PasteEvent](ts-basic-components-richeditor.md#pasteevent11) | 否 | 定义用户粘贴事件。 |

## OnHoverCallback14+

PhonePC/2in1TabletTVWearable

type OnHoverCallback = (status: boolean, event: HoverEvent) => void

鼠标悬浮触发回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | boolean | 是 | 表示鼠标是否悬浮在组件上，鼠标进入组件时为true，离开组件时为false。 |
| event | [HoverEvent](ts-universal-events-hover.md#hoverevent10对象说明) | 是 | 设置悬浮事件。 |

## RichEditorTextSpan

PhonePC/2in1TabletTVWearable

文本Span信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | [RichEditorSpanPosition](ts-basic-components-richeditor.md#richeditorspanposition) | 否 | 否 | Span位置。 |
| value | string | 否 | 否 | 文本Span内容。 |
| textStyle | [RichEditorTextStyle](ts-basic-components-richeditor.md#richeditortextstyle) | 否 | 是 | 文本Span样式信息。 |

## RichEditorImageSpan

PhonePC/2in1TabletTVWearable

图片Span信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | [RichEditorSpanPosition](ts-basic-components-richeditor.md#richeditorspanposition) | 否 | 否 | Span位置。 |
| value | [PixelMap](arkts-apis-image-pixelmap.md) | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图片内容。 |
| imageStyle | [RichEditorImageSpanStyle](ts-basic-components-richeditor.md#richeditorimagespanstyle) | 否 | 是 | 图片样式。 |

## RichEditorUrlStyle19+

PhonePC/2in1TabletTVWearable

Url信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | url地址。  默认值：undefined |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（更新文本样式）

通过[updateSpanStyle](ts-basic-components-richeditor.md#updatespanstyle)接口更新已有文本样式，更改样式后，使用[getSpans](ts-basic-components-richeditor.md#getspans)获取文本新的样式信息。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. controller: RichEditorController = new RichEditorController();
6. options: RichEditorOptions = { controller: this.controller };
7. private start: number = -1;
8. private end: number = -1;
9. @State message: string = "[-1, -1]";
10. @State content: string = "";

12. build() {
13. Column() {
14. Column() {
15. Text("selection range:").width("100%")
16. Text() {
17. Span(this.message)
18. }.width("100%")
19. Text("selection content:").width("100%")
20. Text() {
21. Span(this.content)
22. }.width("100%")
23. }
24. .borderWidth(1)
25. .borderColor(Color.Red)
26. .width("100%")
27. .height("20%")

29. Row() {
30. Button("更新样式:加粗").onClick(() => {
31. this.controller.updateSpanStyle({
32. start: this.start,
33. end: this.end,
34. textStyle:
35. {
36. fontWeight: FontWeight.Bolder
37. }
38. })
39. })
40. Button("获取选择内容").onClick(() => {
41. this.content = "";
42. this.controller.getSpans({
43. start: this.start,
44. end: this.end
45. }).forEach(item => {
46. if(typeof(item as RichEditorImageSpanResult)['imageStyle'] != 'undefined'){
47. this.content += (item as RichEditorImageSpanResult).valueResourceStr;
48. this.content += "\n";
49. } else {
50. if(typeof(item as RichEditorTextSpanResult)['symbolSpanStyle'] != 'undefined') {
51. this.content += (item as RichEditorTextSpanResult).symbolSpanStyle?.fontSize;
52. this.content += "\n";
53. }else {
54. this.content += (item as RichEditorTextSpanResult).value;
55. this.content += "\n";
56. }
57. }
58. })
59. })
60. Button("删除选择内容").onClick(() => {
61. this.controller.deleteSpans({
62. start: this.start,
63. end: this.end
64. })
65. this.start = -1;
66. this.end = -1;
67. this.message = "[" + this.start + ", " + this.end + "]";
68. })
69. }
70. .borderWidth(1)
71. .borderColor(Color.Red)
72. .width("100%")
73. .height("10%")

75. Column() {
76. RichEditor(this.options)
77. .onReady(() => {
78. this.controller.addTextSpan("012345",
79. {
80. style:
81. {
82. fontColor: Color.Orange,
83. fontSize: 30
84. }
85. })
86. this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
87. {
88. style:
89. {
90. fontSize: 30
91. }
92. })
93. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
94. this.controller.addImageSpan($r('app.media.startIcon'),
95. {
96. imageStyle:
97. {
98. size: ["57px", "57px"]
99. }
100. })
101. this.controller.addTextSpan("56789",
102. {
103. style:
104. {
105. fontColor: Color.Black,
106. fontSize: 30
107. }
108. })
109. })
110. .onSelect((value: RichEditorSelection) => {
111. this.start = value.selection[0];
112. this.end = value.selection[1];
113. this.message = "[" + this.start + ", " + this.end + "]";
114. })
115. .aboutToIMEInput((value: RichEditorInsertValue) => {
116. console.info("---------------------- aboutToIMEInput ----------------------");
117. console.info("insertOffset:" + value.insertOffset);
118. console.info("insertValue:" + value.insertValue);
119. return true;
120. })
121. .onIMEInputComplete((value: RichEditorTextSpanResult) => {
122. console.info("---------------------- onIMEInputComplete ---------------------");
123. console.info("spanIndex:" + value.spanPosition.spanIndex);
124. console.info("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]");
125. console.info("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]");
126. console.info("value:" + value.value);
127. })
128. .aboutToDelete((value: RichEditorDeleteValue) => {
129. console.info("---------------------- aboutToDelete --------------------------");
130. console.info("offset:" + value.offset);
131. console.info("direction:" + value.direction);
132. console.info("length:" + value.length);
133. value.richEditorDeleteSpans.forEach(item => {
134. console.info("---------------------- item --------------------------");
135. console.info("spanIndex:" + item.spanPosition.spanIndex);
136. console.info("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]");
137. console.info("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]");
138. if (typeof(item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
139. console.info("image:" + (item as RichEditorImageSpanResult).valueResourceStr);
140. } else {
141. console.info("text:" + (item as RichEditorTextSpanResult).value);
142. }
143. })
144. return true;
145. })
146. .onDeleteComplete(() => {
147. console.info("---------------------- onDeleteComplete ------------------------");
148. })
149. .placeholder("input...", {
150. fontColor: Color.Gray,
151. font: {
152. size: 16,
153. weight: FontWeight.Normal,
154. family: "HarmonyOS Sans",
155. style: FontStyle.Normal
156. }
157. })
158. .borderWidth(1)
159. .borderColor(Color.Green)
160. .width("100%")
161. .height("30%")
162. }
163. .borderWidth(1)
164. .borderColor(Color.Red)
165. .width("100%")
166. .height("70%")
167. }
168. }
169. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/BihLGlT5TwSQdMYWnnc8yQ/zh-cn_image_0000002589326167.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=80633B525BDF507DCA822BBEB9D0CC6CA1DF61E63BF26721CDE117F738F3C30C)

### 示例2（绑定自定义键盘）

通过[customKeyboard](ts-basic-components-richeditor.md#customkeyboard)给组件绑定自定义键盘。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RichEditorExample {
5. controller: RichEditorController = new RichEditorController();

7. // 自定义键盘组件
8. @Builder
9. CustomKeyboardBuilder() {
10. Column() {
11. Grid() {
12. ForEach(['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#'], (item: string) => {
13. GridItem() {
14. Button(item).width(110).onClick(() => {
15. this.controller.addTextSpan(item + '', {
16. offset: this.controller.getCaretOffset(),
17. style:
18. {
19. fontColor: Color.Orange,
20. fontSize: 30
21. }
22. })
23. })
24. }
25. })
26. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
27. }.backgroundColor(Color.Gray)
28. }

30. build() {
31. Column() {
32. RichEditor({ controller: this.controller })// 绑定自定义键盘
33. .customKeyboard(this.CustomKeyboardBuilder())
34. .border({ width: 1 })
35. .borderWidth(1)
36. .borderColor(Color.Red)
37. .margin(10)
38. .height(200)
39. .width("100%")
40. }
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/0ZOFabOdRViXumOANqZ53w/zh-cn_image_0000002589246109.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=F44AF50AFF4615CF2E62F612A17599C8312FECCFE7C23E33C0052DE250533E95)

### 示例3（绑定自定义菜单）

通过[bindSelectionMenu](ts-basic-components-richeditor.md#bindselectionmenu)给组件绑定自定义菜单。

示例中的粘贴菜单项涉及读取剪贴板数据，因此需按规范[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。

```
1. // xxx.ets
2. import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

4. export interface SelectionMenuTheme {
5. imageSize: number;
6. buttonSize: number;
7. menuSpacing: number;
8. editorOptionMargin: number;
9. expandedOptionPadding: number;
10. defaultMenuWidth: number;
11. imageFillColor: Resource;
12. backGroundColor: Resource;
13. iconBorderRadius: Resource;
14. containerBorderRadius: Resource;
15. cutIcon: Resource;
16. copyIcon: Resource;
17. pasteIcon: Resource;
18. selectAllIcon: Resource;
19. shareIcon: Resource;
20. translateIcon: Resource;
21. searchIcon: Resource;
22. arrowDownIcon: Resource;
23. iconPanelShadowStyle: ShadowStyle;
24. iconFocusBorderColor: Resource;
25. }

27. export const defaultTheme: SelectionMenuTheme = {
28. imageSize: 24,
29. buttonSize: 48,
30. menuSpacing: 8,
31. editorOptionMargin: 1,
32. expandedOptionPadding: 3,
33. defaultMenuWidth: 256,
34. imageFillColor: $r('sys.color.ohos_id_color_primary'),
35. backGroundColor: $r('sys.color.ohos_id_color_dialog_bg'),
36. iconBorderRadius: $r('sys.float.ohos_id_corner_radius_default_m'),
37. containerBorderRadius: $r('sys.float.ohos_id_corner_radius_card'),
38. cutIcon: $r("sys.media.ohos_ic_public_cut"),
39. copyIcon: $r("sys.media.ohos_ic_public_copy"),
40. pasteIcon: $r("sys.media.ohos_ic_public_paste"),
41. selectAllIcon: $r("sys.media.ohos_ic_public_select_all"),
42. shareIcon: $r("sys.media.ohos_ic_public_share"),
43. translateIcon: $r("sys.media.ohos_ic_public_translate_c2e"),
44. searchIcon: $r("sys.media.ohos_ic_public_search_filled"),
45. arrowDownIcon: $r("sys.media.ohos_ic_public_arrow_down"),
46. iconPanelShadowStyle: ShadowStyle.OUTER_DEFAULT_MD,
47. iconFocusBorderColor: $r('sys.color.ohos_id_color_focused_outline')
48. }

50. @Entry
51. @Component
52. struct SelectionMenu {
53. @State message: string = 'Hello World';
54. @State textSize: number = 40;
55. @State sliderShow: boolean = false;
56. @State start: number = -1;
57. @State end: number = -1;
58. @State colorTransparent: Color = Color.Transparent;
59. controller: RichEditorController = new RichEditorController();
60. options: RichEditorOptions = { controller: this.controller };
61. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
62. private iconArr: Array<Resource> =
63. [$r('app.media.startIcon'), $r('app.media.startIcon'), $r('app.media.startIcon'),
64. $r('app.media.startIcon'), $r('app.media.startIcon')];
65. @State iconBgColor: ResourceColor[] = new Array(this.iconArr.length).fill(this.colorTransparent);
66. @State pasteEnable: boolean = false;
67. @State visibilityValue: Visibility = Visibility.Visible;
68. @State textStyle: RichEditorTextStyle = {};
69. private fontWeightTable: string[] = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "bold", "normal", "bolder", "lighter", "medium", "regular"];
70. private theme: SelectionMenuTheme = defaultTheme;

72. aboutToAppear() {
73. if (this.controller) {
74. let richEditorSelection = this.controller.getSelection();
75. if (richEditorSelection) {
76. let start = richEditorSelection.selection[0];
77. let end = richEditorSelection.selection[1];
78. if (start === 0 && this.controller.getSpans({ start: end + 1, end: end + 1 }).length === 0) {
79. this.visibilityValue = Visibility.None;
80. } else {
81. this.visibilityValue = Visibility.Visible;
82. }
83. }
84. }
85. let sysBoard = pasteboard.getSystemPasteboard()
86. try {
87. if (sysBoard && sysBoard.hasDataSync()) {
88. this.pasteEnable = true
89. } else {
90. this.pasteEnable = false
91. }
92. } catch (err) {
93. console.error('Failed to check the PasteData. Cause:' + err.message)
94. }
95. }

97. build() {
98. Column() {
99. Column() {
100. RichEditor(this.options)
101. .onReady(() => {
102. this.controller.addTextSpan(this.message, { style: { fontColor: Color.Orange, fontSize: 30 } })
103. })
104. .onSelect((value: RichEditorSelection) => {
105. if (value.selection[0] == -1 && value.selection[1] == -1) {
106. return;
107. }
108. this.start = value.selection[0];
109. this.end = value.selection[1];
110. })
111. .bindSelectionMenu(RichEditorSpanType.TEXT, this.panel, ResponseType.LongPress, { onDisappear: () => {
112. this.sliderShow = false;
113. }})
114. .bindSelectionMenu(RichEditorSpanType.TEXT, this.panel, ResponseType.RightClick, { onDisappear: () => {
115. this.sliderShow = false;
116. }})
117. .bindSelectionMenu(RichEditorSpanType.IMAGE, this.panel, ResponseType.LongPress, {
118. menuType : MenuType.PREVIEW_MENU,
119. previewMenuOptions : {
120. hapticFeedbackMode : HapticFeedbackMode.ENABLED
121. }
122. })
123. .borderWidth(1)
124. .borderColor(Color.Red)
125. .width(200)
126. .height(200)
127. }.width('100%').backgroundColor(Color.White)
128. }.height('100%')
129. }

131. PushDataToPasteboard(richEditorSelection: RichEditorSelection) {
132. let sysBoard = pasteboard.getSystemPasteboard();
133. let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, '');
134. if (richEditorSelection.spans && richEditorSelection.spans.length > 0) {
135. let count = richEditorSelection.spans.length;
136. for (let i = count - 1; i >= 0; i--) {
137. let item = richEditorSelection.spans[i]
138. if ((item as RichEditorTextSpanResult)?.textStyle) {
139. let span = item as RichEditorTextSpanResult;
140. let style = span.textStyle;
141. let data = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_PLAIN, span.value.substring(span.offsetInSpan[0], span.offsetInSpan[1]));
142. let prop = pasteData.getProperty();
143. let temp: Record<string, Object> = {
144. 'color': style.fontColor,
145. 'size': style.fontSize,
146. 'style': style.fontStyle,
147. 'weight': this.fontWeightTable[style.fontWeight],
148. 'fontFamily': style.fontFamily,
149. 'decorationType': style.decoration.type,
150. 'decorationColor': style.decoration.color
151. };
152. prop.additions[i] = temp;
153. pasteData.addRecord(data)
154. pasteData.setProperty(prop)
155. }
156. }
157. }
158. sysBoard.clearData()
159. sysBoard.setData(pasteData).then(() => {
160. console.info('SelectionMenu copy option, Succeeded in setting PasteData.');
161. this.pasteEnable = true;
162. }).catch((err: BusinessError) => {
163. console.error('SelectionMenu copy option, Failed to set PasteData. Cause:' + err.message);
164. })
165. }

167. PopDataFromPasteboard(richEditorSelection: RichEditorSelection) {
168. let start = richEditorSelection.selection[0];
169. let end = richEditorSelection.selection[1];
170. if (start == end && this.controller) {
171. start = this.controller.getCaretOffset();
172. end = this.controller.getCaretOffset();
173. }
174. let moveOffset = 0;
175. let sysBoard = pasteboard.getSystemPasteboard();
176. sysBoard.getData((err, data) => {
177. if (err) {
178. return;
179. }
180. let count = data.getRecordCount();
181. for (let i = 0; i < count; i++) {
182. const element = data.getRecord(i);
183. let tex: RichEditorTextStyle = {
184. fontSize: 16,
185. fontColor: Color.Black,
186. fontWeight: FontWeight.Normal,
187. fontFamily: "HarmonyOS Sans",
188. fontStyle: FontStyle.Normal,
189. decoration: { type: TextDecorationType.None, color: "#FF000000", style: TextDecorationStyle.SOLID }
190. }
191. if (data.getProperty() && data.getProperty().additions[i]) {
192. const tmp = data.getProperty().additions[i] as Record<string, Object | undefined>;
193. if (tmp.color) {
194. tex.fontColor = tmp.color as ResourceColor;
195. }
196. if (tmp.size) {
197. tex.fontSize = tmp.size as Length | number;
198. }
199. if (tmp.style) {
200. tex.fontStyle = tmp.style as FontStyle;
201. }
202. if (tmp.weight) {
203. tex.fontWeight = tmp.weight as number | FontWeight | string;
204. }
205. if (tmp.fontFamily) {
206. tex.fontFamily = tmp.fontFamily as ResourceStr;
207. }
208. if (tmp.decorationType && tex.decoration) {
209. tex.decoration.type = tmp.decorationType as TextDecorationType;
210. }
211. if (tmp.decorationColor && tex.decoration) {
212. tex.decoration.color = tmp.decorationColor as ResourceColor;
213. }
214. if (tex.decoration) {
215. tex.decoration = { type: tex.decoration.type, color: tex.decoration.color };
216. }
217. }
218. if (element && element.plainText && element.mimeType === pasteboard.MIMETYPE_TEXT_PLAIN && this.controller) {
219. this.controller.addTextSpan(element.plainText,
220. {
221. style: tex,
222. offset: start + moveOffset
223. }
224. )
225. moveOffset += element.plainText.length;
226. }
227. }
228. if (this.controller) {
229. this.controller.setCaretOffset(start + moveOffset)
230. this.controller.closeSelectionMenu()
231. }
232. if (start != end && this.controller) {
233. this.controller.deleteSpans({ start: start + moveOffset, end: end + moveOffset })
234. }
235. })
236. }

238. @Builder
239. panel() {
240. Column() {
241. this.iconPanel()
242. if (!this.sliderShow) {
243. this.SystemMenu()
244. } else {
245. this.sliderPanel()
246. }
247. }.width(256)
248. }

250. @Builder iconPanel() {
251. Column() {
252. Row({ space: 2 }) {
253. ForEach(this.iconArr, (item:Resource, index ?: number) => {
254. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
255. Image(item).fillColor(this.theme.imageFillColor).width(24).height(24).focusable(true).draggable(false)
256. }
257. .borderRadius(this.theme.iconBorderRadius)
258. .width(this.theme.buttonSize)
259. .height(this.theme.buttonSize)
260. .onClick(() => {
261. if (index as number == 0) {
262. this.sliderShow = false;
263. if (this.controller) {
264. let selection = this.controller.getSelection();
265. let spans = selection.spans;
266. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
267. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
268. let span = item as RichEditorTextSpanResult;
269. this.textStyle = span.textStyle;
270. let start = span.offsetInSpan[0];
271. let end = span.offsetInSpan[1];
272. let offset = span.spanPosition.spanRange[0];
273. if (this.textStyle.fontWeight != 11) {
274. this.textStyle.fontWeight = FontWeight.Bolder;
275. } else {
276. this.textStyle.fontWeight = FontWeight.Normal;
277. }
278. this.controller.updateSpanStyle({
279. start: offset + start,
280. end: offset + end,
281. textStyle: this.textStyle
282. })
283. }
284. })
285. }
286. } else if (index as number == 1) {
287. this.sliderShow = false;
288. if (this.controller) {
289. let selection = this.controller.getSelection();
290. let spans = selection.spans;
291. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
292. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
293. let span = item as RichEditorTextSpanResult;
294. this.textStyle = span.textStyle;
295. let start = span.offsetInSpan[0];
296. let end = span.offsetInSpan[1];
297. let offset = span.spanPosition.spanRange[0];
298. if (this.textStyle.fontStyle == FontStyle.Italic) {
299. this.textStyle.fontStyle = FontStyle.Normal;
300. } else {
301. this.textStyle.fontStyle = FontStyle.Italic;
302. }
303. this.controller.updateSpanStyle({
304. start: offset + start,
305. end: offset + end,
306. textStyle: this.textStyle
307. })
308. }
309. })
310. }
311. } else if (index as number == 2) {
312. this.sliderShow = false;
313. if (this.controller) {
314. let selection = this.controller.getSelection();
315. let spans = selection.spans;
316. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
317. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
318. let span = item as RichEditorTextSpanResult;
319. this.textStyle = span.textStyle;
320. let start = span.offsetInSpan[0];
321. let end = span.offsetInSpan[1];
322. let offset = span.spanPosition.spanRange[0];
323. if (this.textStyle.decoration) {
324. if (this.textStyle.decoration.type == TextDecorationType.Underline) {
325. this.textStyle.decoration.type = TextDecorationType.None;
326. } else {
327. this.textStyle.decoration.type = TextDecorationType.Underline;
328. }
329. } else {
330. this.textStyle.decoration = { type: TextDecorationType.Underline, color: Color.Black, style: TextDecorationStyle.SOLID };
331. }
332. this.controller.updateSpanStyle({
333. start: offset + start,
334. end: offset + end,
335. textStyle: this.textStyle
336. })
337. }
338. })
339. }
340. } else if (index as number == 3) {
341. this.sliderShow = !this.sliderShow;
342. } else if (index as number == 4) {
343. this.sliderShow = false;
344. if (this.controller) {
345. let selection = this.controller.getSelection();
346. let spans = selection.spans;
347. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
348. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
349. let span = item as RichEditorTextSpanResult;
350. this.textStyle = span.textStyle;
351. let start = span.offsetInSpan[0];
352. let end = span.offsetInSpan[1];
353. let offset = span.spanPosition.spanRange[0];
354. if (this.textStyle.fontColor == Color.Orange || this.textStyle.fontColor == '#FFFFA500') {
355. this.textStyle.fontColor = Color.Black;
356. } else {
357. this.textStyle.fontColor = Color.Orange;
358. }
359. this.controller.updateSpanStyle({
360. start: offset + start,
361. end: offset + end,
362. textStyle: this.textStyle
363. })
364. }
365. })
366. }
367. }
368. })
369. .onTouch((event?: TouchEvent | undefined) => {
370. if(event != undefined){
371. if (event.type === TouchType.Down) {
372. this.iconBgColor[index as number] = $r('sys.color.ohos_id_color_click_effect');
373. }
374. if (event.type === TouchType.Up) {
375. this.iconBgColor[index as number] = this.colorTransparent;
376. }
377. }
378. })
379. .onHover((isHover?: boolean, event?: HoverEvent) => {
380. this.iconBgColor.forEach((icon:ResourceColor, index1) => {
381. this.iconBgColor[index1] = this.colorTransparent;
382. })
383. if(isHover != undefined) {
384. this.iconBgColor[index as number] = $r('sys.color.ohos_id_color_hover');
385. }
386. })
387. .backgroundColor(this.iconBgColor[index as number])
388. })
389. }
390. }
391. .clip(true)
392. .width(this.theme.defaultMenuWidth)
393. .padding(this.theme.expandedOptionPadding)
394. .borderRadius(this.theme.containerBorderRadius)
395. .margin({ bottom: this.theme.menuSpacing })
396. .backgroundColor(this.theme.backGroundColor)
397. .shadow(this.theme.iconPanelShadowStyle)
398. }

400. @Builder
401. SystemMenu() {
402. Column() {
403. Menu() {
404. if (this.controller) {
405. MenuItemGroup() {
406. MenuItem({ startIcon: this.theme.cutIcon, content: "剪切", labelInfo: "Ctrl+X" })
407. .onClick(() => {
408. if (!this.controller) {
409. return
410. }
411. let richEditorSelection = this.controller.getSelection();
412. this.PushDataToPasteboard(richEditorSelection);
413. this.controller.deleteSpans({
414. start: richEditorSelection.selection[0],
415. end: richEditorSelection.selection[1]
416. })
417. })
418. MenuItem({ startIcon: this.theme.copyIcon, content: "复制", labelInfo: "Ctrl+C" })
419. .onClick(() => {
420. if (!this.controller) {
421. return;
422. }
423. let richEditorSelection = this.controller.getSelection();
424. this.PushDataToPasteboard(richEditorSelection)
425. this.controller.closeSelectionMenu()
426. })
427. MenuItem({ startIcon: this.theme.pasteIcon, content: "粘贴", labelInfo: "Ctrl+V" })
428. .enabled(this.pasteEnable)
429. .onClick(() => {
430. if (!this.controller) {
431. return;
432. }
433. let richEditorSelection = this.controller.getSelection();
434. this.PopDataFromPasteboard(richEditorSelection)
435. })
436. MenuItem({ startIcon: this.theme.selectAllIcon, content: "全选", labelInfo: "Ctrl+A" })
437. .visibility(this.visibilityValue)
438. .onClick(() => {
439. if (!this.controller) {
440. return;
441. }
442. this.controller.setSelection(-1, -1)
443. this.visibilityValue = Visibility.None;
444. })
445. MenuItem({ startIcon: this.theme.shareIcon, content: "分享", labelInfo: "" })
446. .enabled(false)
447. MenuItem({ startIcon: this.theme.translateIcon, content: "翻译", labelInfo: "" })
448. .enabled(false)
449. MenuItem({ startIcon: this.theme.searchIcon, content: "搜索", labelInfo: "" })
450. .enabled(false)
451. }
452. }
453. }
454. .onVisibleAreaChange([0.0, 1.0], () => {
455. if (!this.controller) {
456. return;
457. }
458. let richEditorSelection = this.controller.getSelection();
459. let start = richEditorSelection.selection[0];
460. let end = richEditorSelection.selection[1];
461. if (start === 0 && this.controller.getSpans({ start: end + 1, end: end + 1 }).length === 0) {
462. this.visibilityValue = Visibility.None;
463. } else {
464. this.visibilityValue = Visibility.Visible;
465. }
466. })
467. .radius(this.theme.containerBorderRadius)
468. .clip(true)
469. .backgroundColor(Color.White)
470. .width(this.theme.defaultMenuWidth)
471. }
472. .width(this.theme.defaultMenuWidth)
473. }

475. @Builder sliderPanel() {
476. Column() {
477. Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
478. Text('A').fontSize(15)
479. Slider({ value: this.textSize, step: 10, style: SliderStyle.InSet })
480. .width(210)
481. .onChange((value: number, mode: SliderChangeMode) => {
482. if (this.controller) {
483. let selection = this.controller.getSelection();
484. if (mode == SliderChangeMode.End) {
485. if (this.textSize == undefined) {
486. this.textSize = 0;
487. }
488. let spans = selection.spans;
489. spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
490. if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
491. this.textSize = Math.max(this.textSize, (item as RichEditorTextSpanResult).textStyle.fontSize);
492. }
493. })
494. }
495. if (mode == SliderChangeMode.Moving || mode == SliderChangeMode.Click) {
496. this.start = selection.selection[0];
497. this.end = selection.selection[1];
498. this.textSize = value;
499. this.controller.updateSpanStyle({
500. start: this.start,
501. end: this.end,
502. textStyle: { fontSize: this.textSize }
503. })
504. }
505. }
506. })
507. Text('A').fontSize(20).fontWeight(FontWeight.Medium)
508. }.borderRadius(this.theme.containerBorderRadius)
509. }
510. .shadow(ShadowStyle.OUTER_DEFAULT_MD)
511. .backgroundColor(Color.White)
512. .borderRadius(this.theme.containerBorderRadius)
513. .padding(15)
514. .height(48)
515. }
516. }
```

说明

系统暂未预置加粗、斜体等图标，示例代码使用系统默认图标，开发者使用时需自行替换iconArr中的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/lFiQ2LmqSG6AruLny0aI7A/zh-cn_image_0000002558766300.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=D2B5E5568EBBE16C40131397D625A95594FA3F514788D63EFE693052A0EA8151)

### 示例4（更新图片样式）

通过[updateSpanStyle](ts-basic-components-richeditor.md#updatespanstyle)接口更新图片样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. controller: RichEditorController = new RichEditorController();
6. options: RichEditorOptions = { controller: this.controller };
7. private start: number = -1;
8. private end: number = -1;
9. @State message: string = "[-1, -1]";
10. @State content: string = "";
11. @State paddingVal: number = 5;
12. @State borderRad: number = 4;

14. build() {
15. Column() {
16. Column() {
17. Text("selection range:").width("100%")
18. Text() {
19. Span(this.message)
20. }.width("100%")
21. Text("selection content:").width("100%")
22. Text() {
23. Span(this.content)
24. }.width("100%")
25. }
26. .borderWidth(1)
27. .borderColor(Color.Red)
28. .width("100%")
29. .height("20%")

31. Row() {
32. Button("updateSpanStyle1")
33. .fontSize(12)
34. .onClick(() => {
35. this.controller.updateSpanStyle({
36. start: this.start,
37. textStyle:
38. {
39. fontWeight: FontWeight.Bolder,
40. fontSize:15
41. },
42. imageStyle: {
43. size: ["80px", "80px"],
44. layoutStyle: {
45. borderRadius: undefined,
46. margin: undefined
47. }
48. }
49. })
50. })

52. Button("updateSpanStyle2")
53. .fontSize(12)
54. .onClick(() => {
55. this.controller.updateSpanStyle({
56. start: this.start,
57. textStyle:
58. {
59. fontWeight: FontWeight.Bolder,
60. fontSize:15
61. },
62. imageStyle: {
63. size: ["70px", "70px"],
64. layoutStyle: {
65. borderRadius: { topLeft: '100px', topRight: '20px', bottomLeft: '100px', bottomRight: '20px' },
66. margin: { left: '30px', top: '20px', right: '20px', bottom: '20px' }
67. }
68. }
69. })
70. })

72. Button("updateSpanStyle3")
73. .fontSize(12)
74. .onClick(() => {
75. this.controller.updateSpanStyle({
76. start: this.start,
77. textStyle:
78. {
79. fontWeight: FontWeight.Bolder,
80. fontSize:15
81. },
82. imageStyle: {
83. size: ["60px", "60px"],
84. layoutStyle: {
85. borderRadius: '-10px',
86. margin: '-10px'
87. }
88. }
89. })
90. })
91. }
92. .borderWidth(1)
93. .borderColor(Color.Red)
94. .width("100%")
95. .height("10%")

97. Row() {
98. Button('addImageSpan1')
99. .fontSize(12)
100. .onClick(() => {
101. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
102. this.controller.addImageSpan($r('app.media.startIcon'), {
103. imageStyle: {
104. size: ["80px", "80px"],
105. layoutStyle: {
106. borderRadius: '50px',
107. margin: '40px'
108. }
109. }
110. })
111. })

113. Button('addImageSpan2')
114. .fontSize(12)
115. .onClick(() => {
116. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
117. this.controller.addImageSpan($r('app.media.startIcon'), {
118. imageStyle: {
119. size: ["100px", "100px"],
120. verticalAlign: ImageSpanAlignment.BOTTOM,
121. layoutStyle: {
122. borderRadius: undefined,
123. margin: undefined
124. }
125. }
126. })
127. })

129. Button('addImageSpan3')
130. .fontSize(12)
131. .onClick(() => {
132. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
133. this.controller.addImageSpan($r('app.media.startIcon'), {
134. imageStyle: {
135. size: ["60px", "60px"],
136. verticalAlign: ImageSpanAlignment.BOTTOM,
137. layoutStyle: {
138. borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },
139. margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }
140. }
141. }
142. })
143. })
144. }
145. .borderWidth(1)
146. .borderColor(Color.Red)
147. .width("100%")
148. .height("10%")

150. Column() {
151. RichEditor(this.options)
152. .onReady(() => {
153. this.controller.addTextSpan("0123456789",
154. {
155. style:
156. {
157. fontColor: Color.Orange,
158. fontSize: 30
159. }
160. })

162. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
163. this.controller.addImageSpan($r('app.media.startIcon'),
164. {
165. imageStyle:
166. {
167. size: ["60px", "60px"],
168. verticalAlign: ImageSpanAlignment.BOTTOM,
169. layoutStyle: {
170. borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },
171. margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }
172. }
173. }
174. })

176. this.controller.addTextSpan("0123456789",
177. {
178. style:
179. {
180. fontColor: Color.Black,
181. fontSize: 30
182. }
183. })
184. })
185. .onSelect((value: RichEditorSelection) => {
186. this.start = value.selection[0];
187. this.end = value.selection[1];
188. this.message = "[" + this.start + ", " + this.end + "]";
189. })
190. .aboutToIMEInput((value: RichEditorInsertValue) => {
191. console.info("---------------------- aboutToIMEInput ----------------------");
192. console.info("insertOffset:" + value.insertOffset);
193. console.info("insertValue:" + value.insertValue);
194. return true;
195. })
196. .onIMEInputComplete((value: RichEditorTextSpanResult) => {
197. console.info("---------------------- onIMEInputComplete ---------------------");
198. console.info("spanIndex:" + value.spanPosition.spanIndex);
199. console.info("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]");
200. console.info("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]");
201. console.info("value:" + value.value);
202. })
203. .aboutToDelete((value: RichEditorDeleteValue) => {
204. console.info("---------------------- aboutToDelete --------------------------");
205. console.info("offset:" + value.offset);
206. console.info("direction:" + value.direction);
207. console.info("length:" + value.length);
208. value.richEditorDeleteSpans.forEach(item => {
209. console.info("---------------------- item --------------------------");
210. console.info("spanIndex:" + item.spanPosition.spanIndex);
211. console.info("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]");
212. console.info("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]");
213. if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
214. console.info("image:" + (item as RichEditorImageSpanResult).valueResourceStr);
215. } else {
216. console.info("text:" + (item as RichEditorTextSpanResult).value);
217. }
218. })
219. return true;
220. })
221. .onDeleteComplete(() => {
222. console.info("---------------------- onDeleteComplete ------------------------");
223. })
224. .borderWidth(1)
225. .borderColor(Color.Green)
226. .width("100%")
227. .height('80.00%')
228. }
229. .borderWidth(1)
230. .borderColor(Color.Red)
231. .width("100%")
232. .height("70%")
233. }
234. }
235. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/WtqShwTNRamlaz30qnUZ4A/zh-cn_image_0000002558606642.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=FDDC12160784379347949E6091FB6E1E7AEBB3AC099813D67416660028AFE876)

### 示例5（Span绑定手势事件）

为Span绑定[gesture](ts-basic-components-richeditor.md#richeditorgesture11)回调。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. controller: RichEditorController = new RichEditorController();
6. options: RichEditorOptions = { controller: this.controller };
7. @State textFlag: string = "TextFlag";

9. build() {
10. Column() {
11. Column() {
12. Text(this.textFlag)
13. .copyOption(CopyOptions.InApp)
14. .fontSize(50)
15. .height(150)
16. }
17. Divider()
18. Column() {
19. RichEditor(this.options)
20. .onReady(() => {
21. this.controller.addTextSpan('Area1\n', {
22. style:
23. {
24. fontColor: Color.Orange,
25. fontSize: 50,
26. },
27. gesture:
28. {
29. onClick: () => {
30. this.textFlag = "Area1 is onClick.";
31. },
32. onLongPress: () => {
33. this.textFlag = "Area1 is onLongPress.";
34. }
35. }
36. })

38. this.controller.addTextSpan('Area2\n', {
39. style:
40. {
41. fontColor: Color.Blue,
42. fontSize: 50
43. },
44. gesture:
45. {
46. onClick: () => {
47. this.textFlag = "Area2 is onClick.";
48. },
49. onLongPress: () => {
50. this.textFlag = "Area2 is onLongPress.";
51. }
52. }
53. })

55. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
56. this.controller.addImageSpan($r('app.media.startIcon'),
57. {
58. imageStyle:
59. {
60. size: ["100px", "100px"],
61. layoutStyle: {
62. margin: 5,
63. borderRadius: 15
64. }
65. },
66. gesture:
67. {
68. onClick: () => {
69. this.textFlag = "ImageSpan is onClick.";
70. },
71. onLongPress: () => {
72. this.textFlag = "ImageSpan is onLongPress.";
73. }
74. },
75. onHover : (status) => {
76. this.textFlag = "ImageSpan is onHover :" + status;
77. }
78. })
79. })
80. }
81. .borderWidth(1)
82. .borderColor(Color.Red)
83. .width("100%")
84. .height("70%")
85. }
86. }
87. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/LJuQbX3dRKC26bzK2FStTw/zh-cn_image_0000002589326169.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=2D806C7817F4136795C882F12890A3E6FAEA3A8CF00CA6FA526B130A72214680)

### 示例6（更新和获取段落样式）

通过[updateParagraphStyle](ts-basic-components-richeditor.md#updateparagraphstyle11)接口更新段落样式，通过[getParagraphs](ts-basic-components-richeditor.md#getparagraphs11)接口获取指定范围段落的信息。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. controller: RichEditorController = new RichEditorController();
6. private spanParagraphs: RichEditorParagraphResult[] = [];

8. build() {
9. Column() {
10. RichEditor({ controller: this.controller })
11. .onReady(() => {
12. this.controller.addTextSpan("0123456789\n", {
13. style: {
14. fontColor: Color.Pink,
15. fontSize: "32"
16. },
17. paragraphStyle: {
18. textAlign: TextAlign.Start,
19. textVerticalAlign: TextVerticalAlign.BASELINE,
20. leadingMargin: 16
21. }
22. })
23. this.controller.addTextSpan("0123456789")
24. })
25. .width("80%")
26. .height("30%")
27. .border({ width: 1, radius: 5 })
28. .draggable(false)

30. Column({ space: 5 }) {
31. Button("段落左对齐").onClick(() => {
32. this.controller.updateParagraphStyle({ start: -1, end: -1,
33. style: {
34. textAlign: TextAlign.Start
35. }
36. })
37. })

39. Button("段落右对齐").onClick(() => {
40. this.controller.updateParagraphStyle({ start: -1, end: -1,
41. style: {
42. textAlign: TextAlign.End
43. }
44. })
45. })

47. Button("段落居中").onClick(() => {
48. this.controller.updateParagraphStyle({ start: -1, end: -1,
49. style: {
50. textAlign: TextAlign.Center
51. }
52. })
53. })

55. Button("段落间距设置50").onClick(() => {
56. this.controller.updateParagraphStyle({ start: -1, end: -1,
57. style: {
58. paragraphSpacing: 50
59. }
60. })
61. })
62. Divider()
63. Button("getParagraphs").onClick(() => {
64. this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 });
65. console.info("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs));
66. })

68. Button("UpdateSpanStyle1").onClick(() => {
69. this.controller.updateSpanStyle({ start: -1, end: -1,
70. textStyle: {
71. fontColor: Color.Brown,
72. fontSize: 20
73. }
74. })
75. })

77. Button("UpdateSpanStyle2").onClick(() => {
78. this.controller.updateSpanStyle({ start: -1, end: -1,
79. textStyle: {
80. fontColor: Color.Green,
81. fontSize: 30
82. }
83. })
84. })
85. }
86. }
87. }
88. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/z5kplW0GRfiDbdK6YVKEYw/zh-cn_image_0000002589246111.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=9D82E377F013FDB5EA1E4ACE623F3B5D01E421A17243E7263BFC68A81229D4AC)

### 示例7（更新预设样式与缩进）

通过[setTypingStyle](ts-basic-components-richeditor.md#settypingstyle11)接口更新文本预设样式，通过[updateParagraphStyle](ts-basic-components-richeditor.md#updateparagraphstyle11)接口设置段落缩进。

```
1. // xxx.ets

3. const canvasWidth = 1000;
4. const canvasHeight = 100;
5. const Indentation = 40;
6. class LeadingMarginCreator {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private offscreenCanvas: OffscreenCanvas = new OffscreenCanvas(canvasWidth, canvasHeight);
9. private offContext: OffscreenCanvasRenderingContext2D = this.offscreenCanvas.getContext("2d", this.settings);
10. public static instance: LeadingMarginCreator = new LeadingMarginCreator();

12. // 获得字体字号级别，分别是从0到4级
13. public getFontSizeLevel(fontSize: number) {
14. const fontScaled: number = Number(fontSize) / 16;

16. enum FontSizeScaleThreshold {
17. SMALL = 0.9,
18. NORMAL = 1.1,
19. LEVEL_1_LARGE = 1.2,
20. LEVEL_2_LARGE = 1.4,
21. LEVEL_3_LARGE = 1.5
22. }

24. let fontSizeLevel: number = 1;

26. if (fontScaled < FontSizeScaleThreshold.SMALL) {
27. fontSizeLevel = 0;
28. } else if (fontScaled < FontSizeScaleThreshold.NORMAL) {
29. fontSizeLevel = 1;
30. } else if (fontScaled < FontSizeScaleThreshold.LEVEL_1_LARGE) {
31. fontSizeLevel = 2;
32. } else if (fontScaled < FontSizeScaleThreshold.LEVEL_2_LARGE) {
33. fontSizeLevel = 3;
34. } else if (fontScaled < FontSizeScaleThreshold.LEVEL_3_LARGE) {
35. fontSizeLevel = 4;
36. } else {
37. fontSizeLevel = 1;
38. }

40. return fontSizeLevel;
41. }
42. // 获得字体字号级别，分别是从0到4级
43. public getmarginLevel(Width: number) {
44. let marginlevel: number = 1;
45. if (Width == 40) {
46. marginlevel = 2.0;
47. } else if (Width == 80) {
48. marginlevel = 1.0;
49. } else if (Width == 120) {
50. marginlevel = 2/3;
51. } else if (Width == 160) {
52. marginlevel = 0.5;
53. } else if (Width == 200) {
54. marginlevel = 0.4;
55. }
56. return marginlevel;
57. }

59. public genStrMark(fontSize: number, str: string): PixelMap {
60. this.offContext = this.offscreenCanvas.getContext("2d", this.settings);
61. this.clearCanvas()
62. this.offContext.font = fontSize + 'vp sans-serif';
63. this.offContext.fillText(str + '.', 0, fontSize * 0.9)
64. return this.offContext.getPixelMap(0, 0, fontSize * (str.length + 1) / 1.75, fontSize)
65. }

67. public genSquareMark(fontSize: number): PixelMap {
68. this.offContext = this.offscreenCanvas.getContext("2d", this.settings);
69. this.clearCanvas()
70. const coordinate = fontSize * (1 - 1 / 1.5) / 2;
71. const sideLength = fontSize / 1.5;
72. this.offContext.fillRect(coordinate, coordinate, sideLength, sideLength)
73. return this.offContext.getPixelMap(0, 0, fontSize, fontSize)
74. }

76. // 生成圆圈符号
77. public genCircleMark(fontSize: number, width: number, level?: number ): PixelMap {
78. const indentLevel = level ?? 1;
79. const offsetLevel = [22, 28, 32, 34, 38];
80. const fontSizeLevel = this.getFontSizeLevel(fontSize);
81. const marginlevel = this.getmarginLevel(width);
82. const newCanvas = new OffscreenCanvas(canvasWidth, canvasHeight);
83. const newOffContext: OffscreenCanvasRenderingContext2D = newCanvas.getContext("2d", this.settings);
84. const centerCoordinate = 50;
85. const radius = 10;
86. this.clearCanvas()
87. newOffContext.ellipse(100 * (indentLevel + 1) - centerCoordinate * marginlevel, offsetLevel[fontSizeLevel], radius * marginlevel, radius, 0, 0, 2 * Math.PI)
88. newOffContext.fillStyle = '66FF0000';
89. newOffContext.fill()
90. return newOffContext.getPixelMap(0, 0, 100 + 100 * indentLevel, 100)
91. }

93. private clearCanvas() {
94. this.offContext.clearRect(0, 0, canvasWidth, canvasHeight)
95. }
96. }

98. @Entry
99. @Component
100. struct Index {
101. controller: RichEditorController = new RichEditorController();
102. options: RichEditorOptions = { controller: this.controller };
103. private leadingMarkCreatorInstance = LeadingMarginCreator.instance;
104. private fontNameRawFile: string = 'MiSans-Bold';
105. @State fs: number = 30;
106. @State cl: number = Color.Black;
107. private leftMargin: Dimension = 0;
108. private richEditorTextStyle: RichEditorTextStyle = {};

110. aboutToAppear() {
111. this.getUIContext().getFont().registerFont({
112. familyName: 'MiSans-Bold',
113. familySrc: '/font/MiSans-Bold.ttf'
114. })
115. }

117. build() {
118. Scroll() {
119. Column() {
120. RichEditor(this.options)
121. .onReady(() => {
122. this.controller.addTextSpan("0123456789\n",
123. {
124. style:
125. {
126. fontWeight: 'medium',
127. fontFamily: this.fontNameRawFile,
128. fontColor: Color.Red,
129. fontSize: 50,
130. fontStyle: FontStyle.Italic,
131. decoration: { type: TextDecorationType.Underline, color: Color.Green }
132. }
133. })

135. this.controller.addTextSpan("abcdefg",
136. {
137. style:
138. {
139. fontWeight: FontWeight.Lighter,
140. fontFamily: 'HarmonyOS Sans',
141. fontColor: 'rgba(0,128,0,0.5)',
142. fontSize: 30,
143. fontStyle: FontStyle.Normal,
144. decoration: { type: TextDecorationType.Overline, color: 'rgba(169, 26, 246, 0.50)' }
145. }
146. })
147. })
148. .borderWidth(1)
149. .borderColor(Color.Green)
150. .width("100%")
151. .height("50%")

153. Row({ space: 5 }) {
154. Button('setTypingStyle1')
155. .fontSize(10)
156. .onClick(() => {
157. this.controller.setTypingStyle(
158. {
159. fontWeight: 'medium',
160. fontFamily: this.fontNameRawFile,
161. fontColor: Color.Blue,
162. fontSize: 50,
163. fontStyle: FontStyle.Italic,
164. decoration: { type: TextDecorationType.Underline, color: Color.Green }
165. })
166. })

168. Button('setTypingStyle2')
169. .fontSize(10)
170. .onClick(() => {
171. this.controller.setTypingStyle(
172. {
173. fontWeight: FontWeight.Lighter,
174. fontFamily: 'HarmonyOS Sans',
175. fontColor: Color.Green,
176. fontSize: '30',
177. fontStyle: FontStyle.Normal,
178. decoration: { type: TextDecorationType.Overline, color: 'rgba(169, 26, 246, 0.50)' }
179. })
180. })
181. }
182. Divider()
183. Button("getTypingStyle").onClick(() => {
184. this.richEditorTextStyle = this.controller.getTypingStyle();
185. console.info("RichEditor getTypingStyle:" + JSON.stringify(this.richEditorTextStyle));
186. })
187. Divider()
188. Row({ space: 5 }) {
189. Button("向右列表缩进").onClick(() => {
190. let margin = Number(this.leftMargin);
191. if (margin < 200) {
192. margin += Indentation;
193. this.leftMargin = margin;
194. }
195. this.controller.updateParagraphStyle({
196. start: -10,
197. end: -10,
198. style: {
199. leadingMargin : {
200. pixelMap : this.leadingMarkCreatorInstance.genCircleMark(100, margin, 1),
201. size: [margin, 40]
202. }
203. }
204. })
205. })

207. Button("向左列表缩进").onClick(() => {
208. let margin = Number(this.leftMargin);
209. if (margin > 0) {
210. margin -= Indentation;
211. this.leftMargin = margin;
212. }
213. this.controller.updateParagraphStyle({
214. start: -10,
215. end: -10,
216. style: {
217. leadingMargin : {
218. pixelMap : this.leadingMarkCreatorInstance.genCircleMark(100, margin, 1),
219. size: [margin, 40]
220. }
221. }
222. })
223. })
224. }
225. Divider()
226. Row({ space: 5 }) {
227. Button("向右空白缩进").onClick(() => {
228. let margin = Number(this.leftMargin);
229. if (margin < 200) {
230. margin += Indentation;
231. this.leftMargin = margin;
232. }
233. this.controller.updateParagraphStyle({
234. start: -10,
235. end: -10,
236. style: {
237. leadingMargin: margin
238. }
239. })
240. })

242. Button("向左空白缩进").onClick(() => {
243. let margin = Number(this.leftMargin)
244. if (margin > 0) {
245. margin -= Indentation;
246. this.leftMargin = margin;
247. }
248. this.controller.updateParagraphStyle({
249. start: -10,
250. end: -10,
251. style: {
252. leadingMargin: margin
253. }
254. })
255. })
256. }
257. }.borderWidth(1).borderColor(Color.Red)
258. }
259. }
260. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/d74vIcG1T0-YiBIpHpkh_g/zh-cn_image_0000002558766302.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=A76B15EB22A3B0DBE61337197B010D370F02734B8E54E00EAE1C022DEF5D12FE)

### 示例8（设置文本字重与阴影）

通过[updateParagraphStyle](ts-basic-components-richeditor.md#updateparagraphstyle11)接口设置文本字重与阴影。

```
1. @Entry
2. @Component
3. struct Index {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };
6. private start: number = -1;
7. private end: number = -1;
8. @State message: string = "[-1, -1]"
9. @State content: string = ""
10. @State textShadows : Array<ShadowOptions> = [
11. { radius: 10, color: Color.Red, offsetX: 10, offsetY: 0 },
12. { radius: 10, color: Color.Black, offsetX: 20, offsetY: 0 },
13. { radius: 10, color: Color.Brown, offsetX: 30, offsetY: 0 },
14. { radius: 10, color: Color.Green, offsetX: 40, offsetY: 0 },
15. { radius: 10, color: Color.Yellow, offsetX: 100, offsetY: 0 }
16. ];

18. build() {
19. Column() {
20. Column() {
21. Text("selection range:").width("100%")
22. Text() {
23. Span(this.message)
24. }.width("100%")
25. Text("selection content:").width("100%")
26. Text() {
27. Span(this.content)
28. }.width("100%")
29. }
30. .borderWidth(1)
31. .borderColor(Color.Red)
32. .width("100%")
33. .height("20%")
34. Row() {
35. Button("更新样式: 加粗 & 文本阴影").onClick(() => {
36. this.controller.updateSpanStyle({
37. start: this.start,
38. end: this.end,
39. textStyle:
40. {
41. fontWeight: FontWeight.Bolder,
42. textShadow: this.textShadows
43. }
44. })
45. })
46. }
47. .borderWidth(1)
48. .borderColor(Color.Red)
49. .width("100%")
50. .height("10%")
51. Column() {
52. RichEditor(this.options)
53. .onReady(() => {
54. this.controller.addTextSpan("0123456789",
55. {
56. style:
57. {
58. fontColor: Color.Orange,
59. fontSize: 30,
60. textShadow: { radius: 10, color: Color.Blue, offsetX: 10, offsetY: 0 }
61. }
62. })
63. })
64. .borderWidth(1)
65. .borderColor(Color.Green)
66. .width("100%")
67. .height("30%")
68. }
69. .borderWidth(1)
70. .borderColor(Color.Red)
71. .width("100%")
72. .height("70%")
73. }
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/bNuA22THRsC3LkE1hzCQ5Q/zh-cn_image_0000002558606644.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=44F457C4D9D690B2464A581ECFACA669548858931DDBF3614FDE549E27A8671E)

### 示例9（添加用户自定义布局Span）

通过[addBuilderSpan](ts-basic-components-richeditor.md#addbuilderspan11)接口添加用户自定义布局Span。

```
1. @Builder
2. function placeholderBuilder2() {
3. Row({ space: 2 }) {
4. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
5. Image($r('app.media.startIcon')).width(24).height(24).margin({ left: -5 })
6. Text('okokokok').fontSize(10)
7. }.width('20%').height(50).padding(10).backgroundColor(Color.Red)
8. }

10. // xxx.ets
11. @Entry
12. @Component
13. struct Index {
14. controller: RichEditorController = new RichEditorController();
15. option: RichEditorOptions = { controller: this.controller };
16. private start: number = 2;
17. private end: number = 4;
18. @State message: string = "[-1, -1]";
19. @State content: string = "";
20. private my_offset: number | undefined = undefined;
21. private my_builder: CustomBuilder = undefined;
22. @BuilderParam my_builder2:() => void = placeholderBuilder2;

24. @Builder
25. placeholderBuilder() {
26. Row({ space: 2 }) {
27. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
28. Image($r('app.media.startIcon')).width(24).height(24).margin({ left: -5 })
29. Text('Custom Popup').fontSize(10)
30. }.width(100).height(50).padding(5)
31. }

33. @Builder
34. placeholderBuilder3() {
35. Text("hello").padding('20').borderWidth(1).width('100%')
36. }

38. @Builder
39. placeholderBuilder4() {
40. Column() {
41. Column({ space: 5 }) {
42. Text('direction:Row').fontSize(9).fontColor(0xCCCCCC).width('90%')
43. Flex({ direction: FlexDirection.Row }) { // 子组件在容器主抽上行布局
44. Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
45. Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
46. Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
47. Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
48. }
49. .height(70)
50. .width('90%')
51. .padding(10)
52. .backgroundColor(0xAFEEEE)

54. Text('direction:RowReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
55. Flex({ direction: FlexDirection.RowReverse }) { // 子组件在容器主抽上反向行布局
56. Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
57. Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
58. Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
59. Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
60. }
61. .height(70)
62. .width('90%')
63. .padding(10)
64. .backgroundColor(0xAFEEEE)

66. Text('direction:Column').fontSize(9).fontColor(0xCCCCCC).width('90%')
67. Flex({ direction: FlexDirection.Column }) { // 子组件在容器主抽上列布局
68. Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
69. Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
70. Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
71. Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
72. }
73. .height(160)
74. .width('90%')
75. .padding(10)
76. .backgroundColor(0xAFEEEE)

78. Text('direction:ColumnReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
79. Flex({ direction: FlexDirection.ColumnReverse }) { // 子组件在容器主抽上反向列布局
80. Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
81. Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
82. Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
83. Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
84. }
85. .height(160)
86. .width('90%')
87. .padding(10)
88. .backgroundColor(0xAFEEEE)
89. }.width('100%').margin({ top: 5 })
90. }.width('100%')
91. }

93. @Builder
94. MyMenu() {
95. Menu() {
96. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
97. MenuItem({ startIcon: $r('app.media.startIcon'), content: "菜单选项1" })
98. MenuItem({ startIcon: $r('app.media.startIcon'), content: "菜单选项2" })
99. .enabled(false)
100. }
101. }

103. build() {
104. Column() {
105. Column() {
106. Text("selection range:").width("100%")
107. Text() {
108. Span(this.message)
109. }.width("100%")

111. Text("selection content:").width("100%")
112. Text() {
113. Span(this.content)
114. }.width("100%")
115. }
116. .borderWidth(1)
117. .borderColor(Color.Red)
118. .width("100%")
119. .height("20%")

121. Row() {
122. Button("获取选择内容 getSpans").onClick(() => {
123. console.info('getSpans='+JSON.stringify(this.controller.getSpans({ start:1, end:5 })));
124. console.info('getParagraphs='+JSON.stringify(this.controller.getParagraphs({ start:1, end:5 })));
125. this.content = "";
126. this.controller.getSpans({
127. start: this.start,
128. end: this.end
129. }).forEach(item => {
130. if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
131. if ((item as RichEditorImageSpanResult).valueResourceStr == "") {
132. console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +
133. (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])
134. } else {
135. console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +
136. (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +
137. (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])
138. }
139. } else {
140. this.content += (item as RichEditorTextSpanResult).value;
141. this.content += "\n";
142. console.info("text span: " + (item as RichEditorTextSpanResult).value);
143. }
144. })
145. })
146. Button("获取选择内容 getSelection").onClick(() => {
147. this.content = "";
148. let select = this.controller.getSelection();
149. console.info("selection start " + select.selection[0] + " end " + select.selection[1]);
150. select.spans.forEach(item => {
151. if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
152. if ((item as RichEditorImageSpanResult).valueResourceStr == "") {
153. console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +
154. (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])
155. } else {
156. console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +
157. (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +
158. (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])
159. }
160. } else {
161. this.content += (item as RichEditorTextSpanResult).value;
162. this.content += "\n";
163. console.info("text span: " + (item as RichEditorTextSpanResult).value);
164. }
165. })
166. })
167. Button("删除选择内容").onClick(() => {
168. this.controller.deleteSpans({
169. start: this.start,
170. end: this.end
171. })
172. })
173. }
174. .borderWidth(1)
175. .borderColor(Color.Red)
176. .width("100%")
177. .height("10%")

179. Column() {
180. RichEditor(this.option)
181. .onReady(() => {
182. this.controller.addTextSpan("0123456789",
183. {
184. style:
185. {
186. fontColor: Color.Orange,
187. fontSize: 30
188. }
189. })
190. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
191. this.controller.addImageSpan($r('app.media.startIcon'),
192. {
193. imageStyle:
194. {
195. size: ["57px", "57px"]
196. }
197. })
198. })
199. .onSelect((value: RichEditorSelection) => {
200. this.start = value.selection[0];
201. this.end = value.selection[1];
202. this.message = "[" + this.start + ", " + this.end + "]";
203. console.info("onSelect="+JSON.stringify(value));
204. })
205. .aboutToIMEInput((value: RichEditorInsertValue) => {
206. console.info("---------------------- aboutToIMEInput --------------------");
207. console.info("aboutToIMEInput="+JSON.stringify(value));
208. console.info("insertOffset:" + value.insertOffset);
209. console.info("insertValue:" + value.insertValue);
210. return true;
211. })
212. .onIMEInputComplete((value: RichEditorTextSpanResult) => {
213. console.info("---------------------- onIMEInputComplete --------------------");
214. console.info("onIMEInputComplete="+JSON.stringify(value));
215. console.info("spanIndex:" + value.spanPosition.spanIndex);
216. console.info("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]");
217. console.info("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]");
218. console.info("value:" + value.value);
219. })
220. .aboutToDelete((value: RichEditorDeleteValue) => {
221. value.richEditorDeleteSpans.forEach(item => {
222. console.info("---------------------- item --------------------");
223. console.info("spanIndex=" + item.spanPosition.spanIndex);
224. console.info("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]");
225. console.info("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]");
226. if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
227. if ((item as RichEditorImageSpanResult).valueResourceStr == "") {
228. console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +
229. (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])
230. } else {
231. console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +
232. (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +
233. (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])
234. }
235. } else {
236. console.info("delete text: " + (item as RichEditorTextSpanResult).value);
237. }
238. })
239. return true;
240. })
241. .borderWidth(1)
242. .borderColor(Color.Green)
243. .width("100%")
244. .height("30%")

246. Button("add span")
247. .onClick(() => {
248. let num = this.controller.addBuilderSpan(this.my_builder,
249. {
250. offset: this.my_offset,
251. accessibilitySpanOptions: { accessibilityText:"hello", accessibilityDescription:"world", accessibilityLevel:"yes" }
252. });
253. console.info('addBuilderSpan return ' + num);
254. })
255. Button("add image")
256. .onClick(() => {
257. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
258. let num = this.controller.addImageSpan($r('app.media.startIcon'), {
259. imageStyle: {
260. size: ["50px", "50px"],
261. verticalAlign: ImageSpanAlignment.BOTTOM,
262. layoutStyle: {
263. borderRadius: undefined,
264. margin: undefined
265. }
266. }
267. })
268. console.info('addImageSpan return' + num);
269. })
270. Row() {
271. Button('builder1').onClick(() => {
272. this.my_builder = () => {
273. this.placeholderBuilder()
274. };
275. })
276. Button('builder2').onClick(() => {
277. this.my_builder = () => {
278. this.my_builder2()
279. };
280. })
281. Button('builder3').onClick(() => {
282. this.my_builder = () => {
283. this.placeholderBuilder3()
284. };
285. })
286. Button('builder4').onClick(() => {
287. this.my_builder = () => {
288. this.placeholderBuilder4()
289. };
290. })
291. }
292. }
293. .borderWidth(1)
294. .borderColor(Color.Red)
295. .width("100%")
296. .height("70%")
297. }
298. }
299. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gD3JXxnRRsiTzW5kIx-9mg/zh-cn_image_0000002589326171.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=E7497AD01D12CC9611809BAD1E828D7A9962998FAC03B60C0BBD5F22D3B54428)

### 示例10（使用和管理组件内的BuilderSpan）

通过[addBuilderSpan](ts-basic-components-richeditor.md#addbuilderspan11)接口添加的自定义布局Span，[getSpans](ts-basic-components-richeditor.md#getspans)、[onWillChange](ts-basic-components-richeditor.md#onwillchange12)等API不会返回BuilderSpan内部的信息。开发者需要自行维护BuilderSpan的状态，并且在组件内容发生变化时同步更新。

```
1. const TAG = 'BuilderSpanDemo';

3. class BuilderObject {
4. content: string
5. imageUri?: string
6. type: string
7. id?: string

9. constructor(content: string, type: string, imageUri?: string, id?: string) {
10. this.content = content
11. this.imageUri = imageUri
12. this.type = type
13. this.id = id
14. }
15. }

17. @Entry
18. @Component
19. struct Index {
20. controller: RichEditorController = new RichEditorController()
21. option: RichEditorOptions = { controller: this.controller }
22. @State content: string = "";
23. @State start: number = 0;
24. @State end: number = 0;
25. private customBuilder: CustomBuilder = undefined;
26. private builderArray: BuilderObject[] = [];
27. private indicesToRemove: number[] = [];
28. private builderId: number = 0;

30. @Builder
31. imageTextBuilder(builder: BuilderObject) {
32. Row({ space: 2 }) {
33. Image($r(builder.imageUri)).width(24).height(24).margin({ left: -5 })
34. Text(builder.content).fontSize(10)
35. }.width(110).height(50).padding(5)
36. }

38. @Builder
39. chipBuilder(builder: BuilderObject) {
40. Row() {
41. Text(builder.content)
42. .fontSize(14)
43. .fontColor(Color.Black)
44. .fontFamily('HarmonyHeiTi')
45. .margin({ right: 4 })

47. SymbolGlyph($r('sys.symbol.xmark'))
48. .width(16)
49. .height(16)
50. .id(builder.id)
51. .onClick((event: ClickEvent) => {
52. this.deleteChipBuilder(event.target.id)
53. })
54. }
55. .width('auto')
56. .height(28)
57. .backgroundColor(Color.Gray)
58. .borderRadius(10)
59. .padding({
60. top: 4,
61. bottom: 4,
62. left: 12,
63. right: 12
64. })
65. }

67. private deleteChipBuilder(builderId?: string) {
68. if (builderId == null || builderId == "") {
69. console.info(TAG, "delete chipBuilder error");
70. return
71. }
72. let deleteRange: number[] = this.getTargetBuilderSpanRange(builderId)
73. if (deleteRange.length == 0) {
74. console.error(TAG, "getTargetBuilderSpanRange failed" + builderId);
75. return
76. }
77. this.builderArray = this.builderArray.filter(item => item.id !== builderId);
78. this.controller.deleteSpans({ start: deleteRange[0], end: deleteRange[1] });
79. console.info(TAG, `deleteChipBuilder start = ${deleteRange[0]}, end = ${deleteRange[1]}`);
80. console.info(TAG, `deleteChipBuilder builderArray + ${this.builderArray.length}`);
81. }

83. private getTargetBuilderSpanRange(builderId: string): number[] {
84. let allSpans = this.controller.getSpans();
85. let result: number[] = [];
86. let chitBuilderIndex = 0;
87. for (let spanIndex = 0; spanIndex < allSpans.length; spanIndex++) {
88. if (!this.isBuilderSpanResult(allSpans[spanIndex])) {
89. continue;
90. }
91. if (this.builderArray.length <= chitBuilderIndex) {
92. break;
93. }
94. if (this.builderArray[chitBuilderIndex].id === builderId) {
95. result = allSpans[spanIndex].spanPosition.spanRange;
96. break;
97. }
98. chitBuilderIndex++;
99. }
100. return result;
101. }

103. private isTextSpanResult(item: RichEditorImageSpanResult | RichEditorTextSpanResult): boolean {
104. return typeof (item as RichEditorImageSpanResult)['imageStyle'] == 'undefined';
105. }

107. private isBuilderSpanResult(item: RichEditorImageSpanResult | RichEditorTextSpanResult): boolean {
108. return typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined'
109. && ((item as RichEditorImageSpanResult).valueResourceStr == " "
110. || (item as RichEditorImageSpanResult).valueResourceStr == "");
111. }

113. build() {
114. Column() {
115. Scroll() {
116. Column() {
117. Text("Builder Info:").width("100%")
118. Text() {
119. Span(this.content)
120. }.width("100%")
121. }
122. }
123. .borderWidth(1)
124. .borderColor(Color.Red)
125. .width("100%")
126. .height("20%")

128. // 添加Builder时，记录builder的相对顺序，以及builder信息
129. // getSpans接口valueResourceStr == " "或""的Span是builderSpan，并且会按顺序返回builder
130. // 可以根据上面两点，在查询时还原builder信息
131. Button("addImageTextBuilder")
132. .onClick(() => {
133. let insertOffset = this.controller.getCaretOffset();
134. // 'app.media.startIcon'需要替换为开发者所需的图像资源文件。
135. let builder = new BuilderObject('Custom PopUP ' + this.builderId, 'imageTextBuilder', 'app.media.startIcon');
136. this.customBuilder = () => {
137. this.imageTextBuilder(builder);
138. }
139. let addIndex = this.addBuilderByIndex(insertOffset);
140. console.info(TAG, "add imageTextBuilder index = " + addIndex);
141. this.builderArray.splice(addIndex, 0, builder);
142. this.controller.addBuilderSpan(this.customBuilder, { offset: insertOffset });
143. this.builderId++;
144. console.info(TAG, "add imageTextBuilder success");
145. })
146. Button("addChipBuilder")
147. .onClick(() => {
148. let insertOffset = this.controller.getCaretOffset();
149. let builder = new BuilderObject('Hello World ' + this.builderId, 'chipBuilder', '',
150. 'chipBuilder' + this.builderId);
151. this.customBuilder = () => {
152. this.chipBuilder(builder);
153. }
154. let addIndex = this.addBuilderByIndex(insertOffset);
155. console.info(TAG, "add addChipBuilder index = " + addIndex);
156. this.builderArray.splice(addIndex, 0, builder);
157. this.controller.addBuilderSpan(this.customBuilder, { offset: insertOffset });
158. this.builderId++;
159. console.info(TAG, "add chipBuilder success");
160. })

162. Row() {
163. Button("getSpans").onClick(() => {
164. console.info(TAG, "getSpans = " + JSON.stringify(this.controller.getSpans()));
165. this.content = "";
166. let allSpans = this.controller.getSpans();
167. let builderSpanIndex = 0;
168. allSpans.forEach(item => {
169. if (this.isTextSpanResult(item)) {
170. console.info(TAG, "text span value: " + (item as RichEditorTextSpanResult).value);
171. } else if (this.isBuilderSpanResult(item)) {
172. let builderOrder = "This is builderSpan " + builderSpanIndex + ":"
173. console.info(TAG, builderOrder);
174. this.content += builderOrder + "\n";
175. let builderResult = (item as RichEditorImageSpanResult);
176. let builderIndex = "index: " + builderResult.spanPosition.spanIndex
177. + ", range: " + builderResult.spanPosition.spanRange[0] + ", "
178. + builderResult.spanPosition.spanRange[1];
179. console.info(TAG, builderIndex);
180. this.content += builderIndex + "\n";
181. if (builderSpanIndex >= this.builderArray.length) {
182. console.error(TAG, "getSpans error,  builderSpanIndex = " + builderSpanIndex
183. + ", builderArray.length = " + this.builderArray.length);
184. return;
185. }
186. let builderInfo = "content: " + this.builderArray[builderSpanIndex].content
187. + ", image uri: " + this.builderArray[builderSpanIndex].imageUri
188. + ", id: " + this.builderArray[builderSpanIndex].id + "\n\n";
189. console.info(TAG, builderInfo);
190. this.content += builderInfo;
191. builderSpanIndex++;
192. } else {
193. let imageResult = (item as RichEditorImageSpanResult);
194. console.info(TAG, "image span " + imageResult.valueResourceStr + ", index: " +
195. imageResult.spanPosition.spanIndex + ", range: " +
196. imageResult.offsetInSpan[0] + ", " + imageResult.offsetInSpan[1] + ", size: " +
197. imageResult.imageStyle.size[0] + ", " + imageResult.imageStyle.size[1]);
198. }
199. })
200. })
201. Button("deleteSelectedSpans")
202. .onClick(() => {
203. this.start = this.controller.getSelection().selection[0];
204. this.end = this.controller.getSelection().selection[1];
205. if (this.start == this.end) {
206. return;
207. }
208. let allSpans = this.controller.getSpans();
209. let needRemoveIndex = 0;
210. for (let i = 0; i < allSpans.length; i++) {
211. if (!this.isBuilderSpanResult(allSpans[i])) {
212. continue;
213. }
214. let builderIndex = (allSpans[i] as RichEditorImageSpanResult).spanPosition.spanRange[0];
215. if (builderIndex < this.start || builderIndex >= this.end) {
216. needRemoveIndex++;
217. continue;
218. }
219. this.indicesToRemove.push(needRemoveIndex);
220. needRemoveIndex++;
221. }
222. console.info(TAG, "deleteSpans indicesToRemove = " + this.indicesToRemove.toString());
223. this.deleteBuilderByIndices();
224. console.info(TAG, "deleteSpans builderArray = " + this.builderArray.length);
225. this.controller.deleteSpans({ start: this.start, end: this.end });
226. })
227. }
228. .borderWidth(1)
229. .borderColor(Color.Red)
230. .width("100%")
231. .height("5%")

233. Column() {
234. RichEditor(this.option)
235. .onReady(() => {
236. this.controller.addTextSpan("0123456789",
237. {
238. style:
239. {
240. fontColor: Color.Orange,
241. fontSize: 30
242. }
243. })
244. })
245. .aboutToDelete((value: RichEditorDeleteValue) => {
246. console.info(TAG, "aboutToDelete = " + JSON.stringify(value));
247. let isBuilderAboutToDelete = this.isBuilderAboutToDelete(value);
248. console.info(TAG, "aboutToDelete isBuilderAboutToDelete = " + isBuilderAboutToDelete);
249. this.getIndicesToRemove(value, isBuilderAboutToDelete);
250. console.info(TAG, "indicesToRemove = " + this.indicesToRemove.toString());
251. this.deleteBuilderByIndices();
252. console.info(TAG, "builderArray = " + this.builderArray.length);
253. return true;
254. })
255. .borderWidth(1)
256. .borderColor(Color.Green)
257. .width("100%")
258. .height("30%")
259. }
260. .margin({ top: 60 })
261. .borderWidth(1)
262. .borderColor(Color.Red)
263. .width("100%")
264. .height("70%")
265. }
266. }

268. private isBuilderAboutToDelete(value: RichEditorDeleteValue): boolean {
269. let flag = false;
270. for (let i = 0; i < value.richEditorDeleteSpans.length; i++) {
271. if (this.isBuilderSpanResult(value.richEditorDeleteSpans[i])) {
272. flag = true;
273. break;
274. }
275. }
276. return flag;
277. }

279. private getIndicesToRemove(value: RichEditorDeleteValue, isBuilderAboutToDelete: boolean): void {
280. if (!isBuilderAboutToDelete) {
281. return
282. }
283. let allSpans = this.controller.getSpans();
284. for (let i = 0; i < value.richEditorDeleteSpans.length; i++) {
285. let needRemoveIndex = 0;
286. let item = value.richEditorDeleteSpans[i];
287. if (!this.isBuilderSpanResult(item)) {
288. continue;
289. }
290. let aboutToDeleteBuilderIndex = (item as RichEditorImageSpanResult).spanPosition.spanIndex
291. for (let j = 0; j < allSpans.length; j++) {
292. if (!this.isBuilderSpanResult(allSpans[j])) {
293. continue;
294. }
295. let builderIndex = (allSpans[j] as RichEditorImageSpanResult).spanPosition.spanIndex
296. if (builderIndex == aboutToDeleteBuilderIndex) {
297. this.indicesToRemove.push(needRemoveIndex)
298. break;
299. }
300. needRemoveIndex++;
301. }
302. }
303. }

305. private deleteBuilderByIndices(): void {
306. let indicesSet: Set<number> = new Set(this.indicesToRemove);
307. let newLength = 0;
308. for (let i = 0; i < this.builderArray.length; i++) {
309. if (!indicesSet.has(i)) {
310. this.builderArray[newLength] = this.builderArray[i];
311. newLength++;
312. }
313. }
314. this.builderArray.length = newLength;
315. this.indicesToRemove.length = 0;
316. }

318. private addBuilderByIndex(insertOffset: number): number {
319. if (insertOffset == 0 || this.builderArray.length == 0) {
320. return 0;
321. }
322. let allSpans = this.controller.getSpans();
323. let addIndex = 0;
324. for (let i = 0; i < allSpans.length; i++) {
325. if (!this.isBuilderSpanResult(allSpans[i])) {
326. continue;
327. }
328. let builderIndex = (allSpans[i] as RichEditorImageSpanResult).spanPosition.spanRange[0];
329. if (builderIndex < insertOffset) {
330. addIndex++;
331. continue;
332. }
333. break;
334. }
335. return addIndex;
336. }
337. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/7QsI3rlqRD6QDSInRjGlYQ/zh-cn_image_0000002589246113.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=45ED8E397E6F4DADF38608294EC88BF00C03A9CDAE702E57C2F2D3256B6C8FB5)

### 示例11（设置文本识别配置）

设置[enableDataDetector](ts-basic-components-richeditor.md#enabledatadetector11)为true时，通过[dataDetectorConfig](ts-basic-components-richeditor.md#datadetectorconfig11)接口设置文本识别配置。

```
1. @Entry
2. @Component
3. struct TextExample7 {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };
6. @State phoneNumber: string = '(86) (755) ********';
7. @State url: string = 'www.********.com';
8. @State email: string = '***@example.com';
9. @State address: string = 'XX省XX市XX区XXXX';
10. @State enableDataDetector: boolean = true;
11. @State enablePreviewText: boolean = false;
12. @State types: TextDataDetectorType[] = [];

14. build() {
15. Row() {
16. Column() {
17. RichEditor(this.options)
18. .onReady(() => {
19. this.controller.addTextSpan('电话号码：' + this.phoneNumber + '\n',
20. {
21. style:
22. {
23. fontSize: 30
24. }
25. })
26. this.controller.addTextSpan('链接：' + this.url + '\n',
27. {
28. style:
29. {
30. fontSize: 30
31. }
32. })
33. this.controller.addTextSpan('邮箱：' + this.email + '\n',
34. {
35. style:
36. {
37. fontSize: 30
38. }
39. })
40. this.controller.addTextSpan('地址：' + this.address,
41. {
42. style:
43. {
44. fontSize: 30
45. }
46. })
47. })
48. .copyOptions(CopyOptions.InApp)
49. .enableDataDetector(this.enableDataDetector)
50. .dataDetectorConfig({types : this.types, onDetectResultUpdate: (result: string)=>{}})
51. .enablePreviewText(this.enablePreviewText)
52. .borderWidth(1)
53. .padding(10)
54. .width('100%')
55. }
56. .width('100%')
57. }
58. }
59. }
```

### 示例12（设置光标、手柄和底板颜色）

通过[caretColor](ts-basic-components-richeditor.md#caretcolor12)属性设置输入框光标、手柄颜色，通过[selectedBackgroundColor](ts-basic-components-richeditor.md#selectedbackgroundcolor12)属性设置文本选中底板颜色。

```
1. @Entry
2. @Component
3. struct RichEditorDemo {
4. @State color: Color = Color.Black;
5. controller: RichEditorController = new RichEditorController();

7. build() {
8. Column() {
9. Row() {
10. Button("改为红色").onClick(() => {
11. this.color = Color.Red;
12. })
13. }.margin({ top: 50 })

15. RichEditor({ controller: this.controller })
16. .onReady(() => {
17. this.controller.addTextSpan('通过caretColor和selectedBackgroundColor属性设置光标和选中背景色');
18. })
19. .width("100%")
20. .border({ width: 1, radius: 5 })
21. .key('RichEditor')
22. .caretColor(this.color)// 光标颜色
23. .selectedBackgroundColor(this.color)// 选中背景色
24. .margin({ top: 50 })
25. }
26. .width('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/9nD-7-rdT6WSkr0pdzgDtw/zh-cn_image_0000002558766304.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=40C23960023CC6094C04D6BB2875095FBDA08D6E2331EC6729706FC937B3D1D3)

### 示例13（设置行高和字符间距）

通过[updateSpanStyle](ts-basic-components-richeditor.md#updatespanstyle)接口配置文本行高（[lineHeight](ts-basic-components-richeditor.md#richeditortextstyle)）和字符间距（[letterSpacing](ts-basic-components-richeditor.md#richeditortextstyle)）。

```
1. @Entry
2. @Component
3. struct RichEditorDemo03 {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };
6. @State start: number = -1;
7. @State end: number = -1;
8. @State LH:number = 50;
9. @State LS:number = 20;

11. build() {
12. Column() {
13. Scroll(){
14. Column(){
15. Row() {
16. Button("行高++").onClick(()=>{
17. this.LH = this.LH + 5;
18. this.controller.updateSpanStyle({
19. start: this.start,
20. end: this.end,
21. textStyle:
22. {
23. lineHeight: this.LH
24. }
25. })
26. })
27. Button("行高--").onClick(()=>{
28. this.LH = this.LH - 5;
29. this.controller.updateSpanStyle({
30. start: this.start,
31. end: this.end,
32. textStyle:
33. {
34. lineHeight: this.LH
35. }
36. })
37. })
38. Button("字符间距++").onClick(()=>{
39. this.LS = this.LS + 5
40. this.controller.updateSpanStyle({
41. start: this.start,
42. end: this.end,
43. textStyle:
44. {
45. letterSpacing: this.LS
46. }
47. })
48. })
49. Button("字符间距--").onClick(()=>{
50. this.LS = this.LS - 5
51. this.controller.updateSpanStyle({
52. start: this.start,
53. end: this.end,
54. textStyle:
55. {
56. letterSpacing: this.LS
57. }
58. })
59. })
60. }
61. }
62. }.borderWidth(1)
63. .borderColor(Color.Red)
64. .width("100%")
65. .height("20%")
66. .margin({top: 20})

68. Scroll(){
69. Column() {
70. Text("LineHeight:" + this.LH).width("100%")
71. Text("LetterSpacing:" + this.LS).width("100%")
72. }
73. }
74. .borderWidth(1)
75. .borderColor(Color.Red)
76. .width("100%")
77. .height("20%")
78. .margin({bottom: 20})

80. Column() {
81. RichEditor(this.options).clip(true).padding(10)
82. .onReady(() => {
83. this.controller.addTextSpan("012345",
84. {
85. style:
86. {
87. fontColor: Color.Orange,
88. fontSize: 30,
89. lineHeight: this.LH,
90. letterSpacing: this.LS
91. }
92. })
93. this.controller.addTextSpan("6789",
94. {
95. style:
96. {
97. fontColor: Color.Black,
98. fontSize: 30,
99. lineHeight: this.LH,
100. letterSpacing: this.LS
101. }
102. })
103. })
104. .borderWidth(1)
105. .borderColor(Color.Green)
106. .width(400)
107. .height(400)
108. }
109. .borderWidth(1)
110. .borderColor(Color.Red)
111. .width("100%")
112. .height("60%")
113. }
114. }
115. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/G5L5j4K8TFa6H0jccj5Syw/zh-cn_image_0000002558606646.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=77A214BC25DCB811563061A57A74564EB73D2C7679EDE870E73207F0D0811EA3)

### 示例14（自定义粘贴事件）

为组件添加[onPaste](ts-basic-components-richeditor.md#onpaste11)事件，通过[PasteEvent](ts-basic-components-richeditor.md#pasteevent11)自定义用户粘贴事件。

```
1. @Entry
2. @Component
3. struct RichEditorDemo {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };

7. build() {
8. Column({ space: 2 }) {
9. RichEditor(this.options)
10. .onReady(() => {
11. this.controller.addTextSpan('RichEditor preventDefault')
12. })
13. .onPaste((event?: PasteEvent) => {
14. if (event != undefined && event.preventDefault) {
15. event.preventDefault();
16. }
17. })
18. .borderWidth(1)
19. .borderColor(Color.Green)
20. .width('100%')
21. .height('40%')
22. }
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/01mnu-8qTEqWGuHgxQqPzg/zh-cn_image_0000002589326173.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=E8A19F85EA6ED5C01818FD7D430C6328AA55A53DD08D6BB8C344F8AFABC782B6)

### 示例15（配置文字特性效果）

通过[addTextSpan](ts-basic-components-richeditor.md#addtextspan)接口设置文字特性效果（[fontFeature](ts-basic-components-richeditor.md#richeditortextstyle)）。当添加“ss01”特性的FontFeature属性时，数字“0”由原来的椭圆形改变为带有倒圆角形。

```
1. @Entry
2. @Component
3. struct RichEditorExample {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };
6. @State enableDataDetector: boolean = true;
7. @State types: TextDataDetectorType[] = [];
8. build() {
9. Row() {
10. Column() {
11. RichEditor(this.options)
12. .onReady(() => {
13. this.controller.addTextSpan('This is ss01 off :' + '0000' + '\n',
14. {
15. style:
16. {
17. fontSize: 30
18. }
19. })
20. this.controller.addTextSpan('This is ss01 on :' + '0000' + '\n',
21. {
22. style:
23. {
24. fontSize: 30,
25. fontFeature: "\"ss01\" 1"
26. }
27. })
28. })
29. .copyOptions(CopyOptions.InApp)
30. .enableDataDetector(this.enableDataDetector)
31. .dataDetectorConfig({types : this.types, onDetectResultUpdate: (result: string)=>{}})
32. .borderWidth(1)
33. .padding(10)
34. .width('100%')
35. }
36. .width('100%')
37. .margin({top:150})
38. }
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/N_djJPLIT6O5BO4MgVdGxA/zh-cn_image_0000002589246115.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=6F44BA48D1DBCDC37DDDA96917DA573EB3EA3DE1071FA6D27A38EA2B765EFE66)

### 示例16（自定义键盘避让）

通过[customKeyboard](ts-basic-components-richeditor.md#customkeyboard)属性绑定自定义键盘，通过参数[KeyboardOptions](ts-basic-components-richeditor.md#keyboardoptions12)设置自定义键盘是否支持避让功能。

```
1. @Entry
2. @Component
3. struct RichEditorExample {
4. controller: RichEditorController = new RichEditorController();
5. @State height1: string | number = '80%';
6. @State height2: number = 100;
7. @State supportAvoidance: boolean = true;

9. // 自定义键盘组件
10. @Builder
11. CustomKeyboardBuilder() {
12. Column() {
13. Row() {
14. Button('增加特表情包').onClick(() => {
15. this.controller.addTextSpan("\uD83D\uDE0A",
16. {
17. style:
18. {
19. fontColor: Color.Orange
20. }
21. })
22. })
23. }

25. Grid() {
26. ForEach(['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#'], (item: string) => {
27. GridItem() {
28. Button(item).width(110).onClick(() => {
29. this.controller.addTextSpan(item, {
30. offset: this.controller.getCaretOffset(),
31. style:
32. {
33. fontColor: Color.Orange,
34. fontSize: 30
35. }
36. })
37. this.controller.setCaretOffset(this.controller.getCaretOffset() + item.toString().length)
38. })
39. }
40. })
41. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
42. }.backgroundColor(Color.Gray)
43. }

45. build() {
46. Column() {
47. Row() {
48. Button("20%")
49. .fontSize(24)
50. .onClick(() => {
51. this.height1 = "20%";
52. })
53. Button("80%")
54. .fontSize(24)
55. .margin({ left: 20 })
56. .onClick(() => {
57. this.height1 = "80%";
58. })
59. }
60. .justifyContent(FlexAlign.Center)
61. .alignItems(VerticalAlign.Bottom)
62. .height(this.height1)
63. .width("100%")
64. .padding({ bottom: 50 })

66. RichEditor({ controller: this.controller })// 绑定自定义键盘
67. .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
68. .margin(10)
69. .border({ width: 1 })
70. .borderWidth(1)
71. .borderColor(Color.Red)
72. .width("100%")
73. }
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/kDiCYxqZQ4Wxzh2QgavLNg/zh-cn_image_0000002558766306.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=8600C4C2A8843254A279F1C35B613EEA3D1C7A629546325E01F75E04357C2CD2)

### 示例17（查看编辑状态）

通过[isEditing](ts-basic-components-richeditor.md#isediting12)接口获取当前富文本的编辑状态。为组件添加[onEditingChange](ts-basic-components-richeditor.md#oneditingchange12)事件，可通过打印日志，获取当前组件是否在编辑态。

```
1. @Entry
2. @Component
3. struct RichEditor_onEditingChange {
4. controller: RichEditorController = new RichEditorController();
5. @State controllerIsEditing: boolean = false;
6. @Builder

8. build() {
9. Column() {
10. Row() {
11. Button("点击查看编辑状态isEditing()：").onClick(() => {
12. this.controllerIsEditing = this.controller.isEditing();
13. })
14. .padding(5)
15. Text('' + this.controllerIsEditing)
16. .width('100%')
17. .padding(5)
18. .fontColor(Color.Orange)
19. .fontSize(20)
20. }
21. RichEditor({ controller: this.controller })
22. .onEditingChange((isEditing: boolean) => {
23. console.info("Current Editing Status:" + isEditing);
24. })
25. .height(400)
26. .borderWidth(1)
27. .borderColor(Color.Red)
28. .width("100%")
29. }
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/PFdm524CRf-eTdNPwP5S9A/zh-cn_image_0000002558606648.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=4D512AB251D7A769109302AB0EB04A9408C3F8BC061B5C5DAE96D1FE9010469E)

### 示例18（配置文本变化回调）

为组件添加[onWillChange](ts-basic-components-richeditor.md#onwillchange12)事件，能够在组件执行增删操作前，触发回调。

```
1. @Entry
2. @Component
3. struct RichEditorExample {
4. controller: RichEditorController = new RichEditorController();
5. build() {
6. Column() {
7. RichEditor({ controller: this.controller })
8. .height(200)
9. .borderWidth(1)
10. .borderColor(Color.Red)
11. .width("100%")
12. .onReady(() => {
13. this.controller.addTextSpan('测试文字TestWord', { style: { fontColor: Color.Orange, fontSize: 30 } })
14. this.controller.updateSpanStyle({
15. start: -1,
16. end: -1,
17. textStyle:
18. {
19. fontWeight: FontWeight.Bolder
20. }
21. })
22. })
23. .onWillChange((value: RichEditorChangeValue) => {
24. console.info('测试log: onWillChange');
25. console.info('rangeBefore: ' + JSON.stringify(value.rangeBefore));
26. console.info('print replacedSpans');
27. value.replacedSpans.forEach((item: RichEditorTextSpanResult) => {
28. console.info('spanPosition:' + JSON.stringify(item.spanPosition));
29. console.info('value:' + item.value);
30. console.info('textStyle:' + JSON.stringify(item.textStyle));
31. console.info('offsetInSpan:' + item.offsetInSpan);
32. console.info('valueResource:' + item.valueResource);
33. console.info('paragraphStyle:' + JSON.stringify(item.paragraphStyle));
34. })
35. console.info('print replacedImageSpans');
36. value.replacedImageSpans.forEach((item: RichEditorImageSpanResult) => {
37. console.info('spanPosition:' + JSON.stringify(item.spanPosition));
38. console.info('valuePixelMap:' + JSON.stringify(item.valuePixelMap));
39. console.info('valueResourceStr:' + item.valueResourceStr);
40. console.info('imageStyle:' + JSON.stringify(item.imageStyle));
41. console.info('offsetInSpan:' + item.offsetInSpan);
42. })
43. console.info('print replacedSymbolSpans');
44. value.replacedSymbolSpans.forEach((item: RichEditorTextSpanResult) => {
45. console.info('spanPosition:' + JSON.stringify(item.spanPosition));
46. console.info('value:' + item.value);
47. console.info('offsetInSpan:' + item.offsetInSpan);
48. console.info('symbolSpanStyle:' + JSON.stringify(item.symbolSpanStyle));
49. console.info('valueResource:' + item.valueResource);
50. console.info('paragraphStyle:' + JSON.stringify(item.paragraphStyle));
51. })
52. return true;
53. })
54. .onDidChange((rangeBefore: TextRange, rangeAfter: TextRange) => {
55. console.info('测试log: onDidChange');
56. console.info('rangeBefore:' + JSON.stringify(rangeBefore));
57. console.info('rangeAfter:' + JSON.stringify(rangeAfter));
58. })
59. .onCut((event:CutEvent) => {
60. event.preventDefault!()
61. console.info('测试log：onCut');
62. })
63. .onCopy((event:CopyEvent) => {
64. event.preventDefault!()
65. console.info('测试log：onCopy');
66. })
67. .onPaste(()=>{
68. console.info('测试log：onPaste');
69. })
70. Text('测试文字Hello')
71. .lineHeight(50)
72. .fontSize(24)
73. .draggable(true)
74. .onDragStart(()=>{})
75. TextInput({text:'测试文字NiHao'})
76. .draggable(true)
77. .margin(20)
78. }
79. }
80. }
```

### 示例19（配置输入法enter键功能）

通过[enterKeyType](ts-basic-components-richeditor.md#enterkeytype12)属性设置软键盘输入法回车键类型。

```
1. @Entry
2. @Component
3. struct SoftKeyboardEnterTypeExample {
4. controller: RichEditorController = new RichEditorController();

6. build() {
7. Column() {
8. Button("停止编辑").onClick(()=>{
9. this.controller.stopEditing()
10. })
11. RichEditor({ controller: this.controller })
12. .margin(10)
13. .border({ width: 1 })
14. .height(200)
15. .borderWidth(1)
16. .borderColor(Color.Red)
17. .width("100%")
18. .enterKeyType(EnterKeyType.Search)
19. .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
20. console.info("trigger richeditor onsubmit" + enterKey);
21. this.controller.addTextSpan(" type["+ enterKey +"] triggered")
22. event.keepEditableState()
23. })
24. }.height("100%").justifyContent(FlexAlign.Center)
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Co1OYzDcRLGAqCiBMIXjpQ/zh-cn_image_0000002589326175.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=B2D90872724DA6DB6F4593A78ACD5335A08962C7C749A66093F8BE05CC44C285)

### 示例20（设置段落折行规则）

通过[updateParagraphStyle](ts-basic-components-richeditor.md#updateparagraphstyle11)接口设置折行类型（[lineBreakStrategy](ts-basic-components-richeditor.md#richeditorparagraphstyle11)），通过[getParagraphs](ts-basic-components-richeditor.md#getparagraphs11)接口获取当前段落的折行类型。

```
1. @Entry
2. @Component
3. struct LineBreakStrategyExample {
4. controller: RichEditorController = new RichEditorController();
5. private spanParagraphs: RichEditorParagraphResult[] = [];
6. @State lineBreakOptionStr: string[] = ['GREEDY', 'HIGH_QUALITY', 'BALANCED'];
7. @State attributeValue: string = "";
8. @State testStr: string = "0123456789,0123456789,0123456789,0123456789,0123456789.";
9. build() {
10. Column() {
11. RichEditor({ controller: this.controller })
12. .onReady(() => {
13. this.controller.addTextSpan(this.testStr, {
14. style: {
15. fontColor: Color.Black,
16. fontSize: "32"
17. },
18. paragraphStyle: {
19. textAlign: TextAlign.Start,
20. lineBreakStrategy: LineBreakStrategy.GREEDY
21. }
22. })
23. })
24. .width(400)
25. .height(300)
26. .margin({bottom:20})
27. .draggable(false)
28. Column(){
29. Text('linebreak属性值为：' + this.attributeValue).fontSize(20).fontColor(Color.Black)
30. }.margin({bottom: 10})
31. Column({ space: 10 }) {
32. Button("设置折行类型GREEDY").onClick(() => {
33. this.controller.updateParagraphStyle({ start: -1, end: -1,
34. style: {
35. lineBreakStrategy: LineBreakStrategy.GREEDY
36. }
37. })
38. })
39. Button("设置折行类型HIGH_QUALITY").onClick(() => {
40. this.controller.updateParagraphStyle({ start: -1, end: -1,
41. style: {
42. lineBreakStrategy: LineBreakStrategy.HIGH_QUALITY
43. }
44. })
45. })
46. Button("设置折行类型BALANCED").onClick(() => {
47. this.controller.updateParagraphStyle({ start: -1, end: -1,
48. style: {
49. lineBreakStrategy: LineBreakStrategy.BALANCED
50. }
51. })
52. })
53. Divider()
54. Row(){
55. Button("获取linebreak属性值").onClick(() => {
56. this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 });
57. console.info("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs));
58. this.spanParagraphs.forEach(item => {
59. if(typeof(item as RichEditorParagraphResult)['style'] != 'undefined'){
60. this.attributeValue = "";
61. console.info('lineBreakStrategy:'+ JSON.stringify((item as RichEditorParagraphResult)['style']));
62. this.attributeValue += this.lineBreakOptionStr[Number((item as RichEditorParagraphResult)['style'].lineBreakStrategy)];
63. }
64. })
65. })
66. }
67. }
68. }
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/wN9iquxiRZekots4TRROsw/zh-cn_image_0000002589246117.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=DBE5D16E741B8424A2A16AACD61FA1C089CD90EAF17CA6673E77C30D236805D3)

### 示例21（属性字符串基本功能）

从API version 20开始，该示例中[属性字符串](ts-universal-styled-string.md)通过[RichEditorStyledStringController](ts-basic-components-richeditor.md#richeditorstyledstringcontroller12)中的[setStyledString](ts-basic-components-richeditor.md#setstyledstring12)方法与RichEditor组件绑定。通过[getStyledString](ts-basic-components-richeditor.md#getstyledstring12)接口获取富文本组件显示的属性字符串。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI'

4. @Entry
5. @Component
6. struct Index {
7. stringLength: number = 0;
8. @State selection: string = "";
9. @State content: string = "";
10. @State range: string = "";
11. @State replaceString: string = "";
12. @State rangeBefore: string = "";
13. @State rangeAfter: string = "";
14. richEditorStyledString: MutableStyledString = new MutableStyledString("");
15. textStyle: TextStyle = new TextStyle({
16. fontWeight: FontWeight.Lighter,
17. fontFamily: 'HarmonyOS Sans',
18. fontColor: Color.Green,
19. fontSize: LengthMetrics.vp(30),
20. fontStyle: FontStyle.Normal
21. })
22. fontStyle1: TextStyle = new TextStyle({ fontColor: Color.Blue });
23. fontStyle2: TextStyle = new TextStyle({
24. fontWeight: FontWeight.Bolder,
25. fontFamily: 'Arial',
26. fontColor: Color.Orange,
27. fontSize: LengthMetrics.vp(30),
28. fontStyle: FontStyle.Italic
29. })

31. controller1: RichEditorController = new RichEditorController();
32. options1: RichEditorOptions = { controller: this.controller1 };
33. // 创建属性字符串对象
34. mutableStyledString: MutableStyledString = new MutableStyledString("初始属性字符串",
35. [{ start: 0, length: 5, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle1 }]);
36. styledString: StyledString = new StyledString("插入属性字符串",
37. [{ start: 2, length: 4, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle2 }]);
38. controller: RichEditorStyledStringController = new RichEditorStyledStringController();
39. options: RichEditorStyledStringOptions = {controller: this.controller};
40. // 文本内容变化回调
41. contentChangedListener: StyledStringChangedListener = {
42. onWillChange: (value: StyledStringChangeValue) => {
43. this.range = '[ ' + value.range.start + ' , ' + value.range.end + ' ]';
44. this.replaceString = value.replacementString.getString();
45. return true;
46. },
47. onDidChange: (rangeBefore, rangeAfter) => {
48. this.rangeBefore = '[ ' + rangeBefore.start + ' , ' + rangeBefore.end + ' ]';
49. this.rangeAfter = '[ ' + rangeAfter.start + ' , ' + rangeAfter.end + ' ]';
50. }
51. }

53. build() {
54. Column({space:6}) {
55. Column() {
56. Text("选中区信息")
57. .fontSize(20)
58. .width("100%")
59. Text("selection range: " + this.selection).width("100%")
60. Text("selection content: " + this.content).width("100%")
61. }
62. .width("100%")
63. .height("10%")

65. Column() {
66. Text("onWillChange回调信息")
67. .fontSize(20)
68. .width("100%")
69. Text("range: " + this.range).width("100%")
70. Text("replacementString: " + this.replaceString).width("100%")
71. Text("onWillChange回调信息")
72. .fontSize(20)
73. .width("100%")
74. Text("rangeBefore: " + this.rangeBefore).width("100%")
75. Text("rangeAfter: " + this.rangeAfter).width("100%")
76. }
77. .borderWidth(1)
78. .borderColor(Color.Black)
79. .width("100%")
80. .height("20%")

82. RichEditor(this.options)
83. .onReady(() => {
84. // 注册文本变化回调
85. this.controller.onContentChanged(this.contentChangedListener);
86. // 设定组件展示的属性字符串
87. this.controller.setStyledString(this.mutableStyledString);
88. })
89. .height("20%")
90. .width("100%")

92. RichEditor(this.options1)
93. .onReady(() => {
94. this.controller1.addTextSpan("把这些文字转换成属性字符串");
95. })
96. .height("10%")
97. .width("100%")
98. .borderWidth(1)
99. .borderColor(Color.Black)

101. Row({space:2}) {
102. Button("插入图片")
103. .stateEffect(true)
104. .onClick(() => {
105. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
106. let imageStyledString = new MutableStyledString(new ImageAttachment({
107. resourceValue: $r('app.media.startIcon'),
108. size: { width: 50, height: 50 },
109. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
110. verticalAlign: ImageSpanAlignment.BASELINE,
111. objectFit: ImageFit.Contain,
112. syncLoad: true
113. }));
114. // 获取组件展示的属性字符串
115. this.richEditorStyledString = this.controller.getStyledString();
116. this.richEditorStyledString.appendStyledString(imageStyledString)
117. // 使插入图片后的属性字符串展示在组件上
118. this.controller.setStyledString(this.richEditorStyledString)
119. this.controller.setCaretOffset(this.richEditorStyledString.length)
120. })
121. Button("插入文本").onClick(() => {
122. // 获取组件展示的属性字符串
123. this.richEditorStyledString = this.controller.getStyledString();
124. this.richEditorStyledString.appendStyledString(this.styledString)
125. // 使插入文本后的属性字符串展示在组件上
126. this.controller.setStyledString(this.richEditorStyledString)
127. this.controller.setCaretOffset(this.richEditorStyledString.length)
128. })
129. Button("删除选中内容").onClick(() => {
130. // 获取选中范围
131. let richEditorSelection = this.controller.getSelection();
132. let start = richEditorSelection.start ? richEditorSelection.start : 0;
133. let end = richEditorSelection.end ? richEditorSelection.end : 0;
134. if (start < 0 || end <= start) {
135. return;
136. }
137. // 获取组件展示的属性字符串
138. this.richEditorStyledString = this.controller.getStyledString();
139. this.richEditorStyledString.removeString(start, end - start)
140. // 使删除内容后的属性字符串展示在组件上
141. this.controller.setStyledString(this.richEditorStyledString)
142. })
143. }
144. Row({space:2}) {
145. Button("获取选中内容").onClick(() => {
146. // 获取选中范围
147. let richEditorSelection = this.controller.getSelection();
148. let start = richEditorSelection.start ? richEditorSelection.start : 0;
149. let end = richEditorSelection.end ? richEditorSelection.end : 0;
150. // 获取组件展示的属性字符串
151. this.richEditorStyledString = this.controller.getStyledString();
152. this.selection = '[ ' + start + ' , ' + end + ' ]';
153. if (start == end) {
154. this.content = "";
155. } else {
156. this.content = this.richEditorStyledString.subStyledString(start, end - start).getString();
157. }
158. })
159. Button("更新选中样式").onClick(() => {
160. // 获取选中范围
161. let richEditorSelection = this.controller.getSelection();
162. let start = richEditorSelection.start ? richEditorSelection.start : 0;
163. let end = richEditorSelection.end ? richEditorSelection.end : 0;
164. if (start < 0 || end <= start) {
165. return;
166. }
167. // 获取组件展示的属性字符串
168. this.richEditorStyledString = this.controller.getStyledString();
169. this.richEditorStyledString.setStyle({
170. start: start,
171. length: end - start,
172. styledKey: StyledStringKey.FONT,
173. styledValue: this.textStyle
174. })
175. // 使变更样式后的属性字符串展示在组件上
176. this.controller.setStyledString(this.richEditorStyledString)
177. })
178. }
179. Row({space:2}){
180. // 将属性字符串转换成span信息
181. Button("调用fromStyledString").onClick(() => {
182. this.controller1.addTextSpan("调用fromStyledString：" +JSON.stringify(this.controller1.fromStyledString(this.mutableStyledString)))
183. })
184. // 将给定范围的组件内容转换成属性字符串
185. Button("调用toStyledString").onClick(() => {
186. this.controller.setStyledString(this.controller1.toStyledString({start:0,end:13}))
187. })
188. }
189. }
190. }
191. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/HBrzkypbQj689Hlnnq8Ycw/zh-cn_image_0000002558766308.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=D9644806046636A7219E987D7D7D9E01E1CFA85587F9BC0E82143BD07F8C447B)

### 示例22（获取布局信息）

通过[getLayoutManager](ts-basic-components-richeditor.md#getlayoutmanager12)接口获取布局管理器对象，通过[getLineCount](ts-text-common.md#getlinecount12)接口获取组件内容或[placeholder](ts-basic-components-richeditor.md#placeholder12)的总行数，通过[getGlyphPositionAtCoordinate](ts-text-common.md#getglyphpositionatcoordinate12)接口获取较为接近给定坐标的字形的位置信息，通过[getLineMetrics](ts-text-common.md#getlinemetrics12)接口获取指定行的行信息、文本样式信息、以及字体属性信息。

```
1. @Entry
2. @Component
3. export struct Index {
4. @State lineCount: string = ""
5. @State glyphPositionAtCoordinate: string = ""
6. @State lineMetrics: string = ""
7. controller: RichEditorController = new RichEditorController();
8. @State textStr: string =
9. 'Hello World! 你好，世界！'

11. build() {
12. Scroll() {
13. Column() {
14. Text('RichEditor组件getLayoutManager接口获取相对于组件的布局信息')
15. .fontSize(9)
16. .fontColor(0xCCCCCC)
17. .width('90%')
18. .padding(10)
19. RichEditor({ controller: this.controller })
20. .borderColor(Color.Red)
21. .borderWidth(1)
22. .onReady(() => {
23. this.controller.addTextSpan(this.textStr)
24. })
25. .onAreaChange(() => {
26. let layoutManager = this.controller.getLayoutManager();
27. this.lineCount = "LineCount: " + layoutManager.getLineCount();
28. })

30. Text('LineCount').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)
31. Text(this.lineCount)

33. Text('GlyphPositionAtCoordinate').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)
34. Button("相对组件坐标[150,50]字形信息")
35. .onClick(() => {
36. let layoutManager: LayoutManager = this.controller.getLayoutManager();
37. let position = layoutManager.getGlyphPositionAtCoordinate(150, 50);
38. this.glyphPositionAtCoordinate =
39. "相对组件坐标[150,50] glyphPositionAtCoordinate position: " + position.position + " affinity: " +
40. position.affinity;
41. })
42. .margin({ bottom: 20, top: 10 })
43. Text(this.glyphPositionAtCoordinate)

45. Text('LineMetrics').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)
46. Button("首行行信息、文本样式信息、以及字体属性信息")
47. .onClick(() => {
48. let layoutManager: LayoutManager = this.controller.getLayoutManager();
49. let lineMetrics = layoutManager.getLineMetrics(0);
50. this.lineMetrics = "lineMetrics is " + JSON.stringify(lineMetrics) + '\n\n';
51. let runMetrics = lineMetrics.runMetrics;
52. runMetrics.forEach((value, key) => {
53. this.lineMetrics += "runMetrics key is " + key + " " + JSON.stringify(value) + "\n\n";
54. });
55. })
56. .margin({ bottom: 20, top: 10 })
57. Text(this.lineMetrics)
58. }
59. .margin({ top: 100, left: 8, right: 8 })
60. }
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/y3OiRyiZSeGUhzgzI8d94A/zh-cn_image_0000002558606650.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=B3A9816281C921AF0620AFDAE922233819383DA1FDDC9D59CBA2B1FED4076170)

### 示例23（设置系统默认菜单扩展项）

从API version 20开始，该示例通过[editMenuOptions](ts-basic-components-richeditor.md#editmenuoptions12)属性设置系统默认菜单的扩展项，允许配置扩展项的文本内容、图标和回调方法。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RichEditorExample {
5. controller: RichEditorController = new RichEditorController();
6. options: RichEditorOptions = { controller: this.controller };
7. @State endIndex: number | undefined = 0;
8. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
9. const idsToFilter: TextMenuItemId[] = [
10. TextMenuItemId.TRANSLATE,
11. TextMenuItemId.SHARE,
12. TextMenuItemId.SEARCH,
13. TextMenuItemId.AI_WRITER,
14. // 从API version 23开始支持TextMenuItemId.autoFill
15. TextMenuItemId.autoFill
16. ]
17. const items = menuItems.filter(item => !idsToFilter.some(id => id.equals(item.id)))
18. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
19. let item1: TextMenuItem = {
20. content: 'create1',
21. icon: $r('app.media.startIcon'),
22. id: TextMenuItemId.of('create1'),
23. };
24. let item2: TextMenuItem = {
25. content: 'create2',
26. id: TextMenuItemId.of('create2'),
27. icon: $r('app.media.startIcon'),
28. };
29. items.push(item1);
30. items.unshift(item2);
31. return items;
32. }
33. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
34. if (menuItem.id.equals(TextMenuItemId.of("create2"))) {
35. console.info("拦截 id: create2 start:" + textRange.start + "; end:" + textRange.end);
36. return true;
37. }
38. if (menuItem.id.equals(TextMenuItemId.of("prepare1"))) {
39. console.info("拦截 id: prepare1 start:" + textRange.start + "; end:" + textRange.end);
40. return true;
41. }
42. if (menuItem.id.equals(TextMenuItemId.COPY)) {
43. console.info("拦截 COPY start:" + textRange.start + "; end:" + textRange.end);
44. return true;
45. }
46. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
47. console.info("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end);
48. return false;
49. }
50. return false;
51. }
52. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
53. onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
54. let item1: TextMenuItem = {
55. content: 'prepare1_' + this.endIndex,
56. icon: $r('app.media.startIcon'),
57. id: TextMenuItemId.of('prepare1'),
58. };
59. menuItems.unshift(item1);
60. return menuItems;
61. }
62. @State editMenuOptions: EditMenuOptions = {
63. onCreateMenu: this.onCreateMenu,
64. onMenuItemClick: this.onMenuItemClick,
65. onPrepareMenu: this.onPrepareMenu
66. };

68. build() {
69. Column() {
70. RichEditor(this.options)
71. .onReady(() => {
72. this.controller.addTextSpan("RichEditor editMenuOptions")
73. })
74. .editMenuOptions(this.editMenuOptions)
75. .onSelectionChange((range: RichEditorRange) => {
76. console.info("onSelectionChange, (" + range.start + "," + range.end + ")");
77. this.endIndex = range.end
78. })
79. .height(50)
80. .margin({ top: 100 })
81. .borderWidth(1)
82. .borderColor(Color.Red)
83. }
84. .width("90%")
85. .margin("5%")
86. }
87. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/twJi466yRFq-3aVa-7Ct9g/zh-cn_image_0000002589326177.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=179619A0D94EF021BE5E8F2D0BE16A7780BF06B8BC07A5BB04CB593ADAA51545)

### 示例24（组件部分常用属性）

从API version 18开始，该示例通过[barState](ts-basic-components-richeditor.md#barstate13)属性设置组件滚动条的显示模式。通过[enableKeyboardOnFocus](ts-basic-components-richeditor.md#enablekeyboardonfocus12)属性设置组件通过点击以外的方式获焦时，是否主动拉起软键盘。通过[enableHapticFeedback](ts-basic-components-richeditor.md#enablehapticfeedback13)属性设置组件是否支持触感反馈。通过[getPreviewText](ts-basic-components-richeditor.md#getpreviewtext12)接口获取组件预上屏信息。通过[stopBackPress](ts-basic-components-richeditor.md#stopbackpress18)属性设置是否阻止返回键向其它组件或应用侧传递。

从API version 21开始，该示例通过[scrollBarColor](ts-basic-components-richeditor.md#scrollbarcolor21)属性设置RichEditor组件滚动条颜色。

```
1. // xxx.ets
2. import { JSON } from '@kit.ArkTS';
3. import { ColorMetrics } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct RichEditor_example {
8. controller: RichEditorController = new RichEditorController();
9. options: RichEditorOptions = { controller: this.controller };

11. controller1: RichEditorController = new RichEditorController();
12. options1: RichEditorOptions = { controller: this.controller1 };

14. @State e: boolean = true;
15. @State bs_num: number = 0;
16. @State bs: (BarState | undefined)[] = [BarState.Auto, BarState.On, BarState.Off, undefined];
17. @State bs_string: string[] = ["Auto", "On", "Off", "undefined"];

19. build() {
20. Column({space: 3}) {
21. RichEditor(this.options)
22. .onReady(() => {
23. this.controller.addTextSpan('文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本', {
24. style: {
25. fontColor: Color.Black,
26. fontSize: 20
27. }
28. });
29. })
30. .onDidIMEInput((value: TextRange) => {
31. this.controller1.addTextSpan("\n" + "触发了onDidIMEInput回调,输入法本次输入内容范围为：(" + value.start + "," + value.end + ")", {
32. style: {
33. fontColor: Color.Gray,
34. fontSize: 10
35. }
36. });
37. })
38. .onSelectionChange((value: RichEditorRange) => {
39. this.controller1.addTextSpan("\n" + "触发了onSelectionChange回调，起始范围信息为：(" + value.start + "," + value.end + ")", {
40. style: {
41. fontColor: Color.Gray,
42. fontSize: 10
43. }
44. });
45. })
46. .width(300)
47. .height(100)
48. .margin(20)
49. .barState(this.bs[this.bs_num])
50. .enableKeyboardOnFocus(this.e)
51. .enableHapticFeedback(true)
52. .stopBackPress(false)
53. .scrollBarColor(ColorMetrics.resourceColor("#2787D9"));

55. RichEditor(this.options1).width(300)

57. Button('设置barState为：' + this.bs_string[this.bs_num])
58. .height(30)
59. .fontSize(13)
60. .onClick(() => {
61. this.bs_num++;
62. if (this.bs_num > (this.bs.length - 1)) {
63. this.bs_num = 0;
64. }
65. })

67. Button('设置enableKeyboardOnFocus为：' + this.e)
68. .height(30)
69. .fontSize(13)
70. .onClick(() => {
71. this.e = !this.e;
72. })

74. Button('获取预上屏信息')
75. .height(30)
76. .fontSize(13)
77. .onClick(() => {
78. this.controller1.addTextSpan("\n获取预上屏信息:" + JSON.stringify(this.controller.getPreviewText()))
79. })
80. }
81. }
82. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/cnCtfF8DRFGc_m53glYG7g/zh-cn_image_0000002589246119.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=1EC9CE960E42D9BE62B5CCD90E20E7F90ABD175FC8DFC2E16A86FCE86010F1A3)

### 示例25（获取光标相对组件位置的矩形）

从API version 18开始，该示例通过RichEditorBaseController的[getCaretRect](ts-basic-components-richeditor.md#getcaretrect18)方法来获取当前光标相对于组件位置的Rect。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. controller: RichEditorController = new RichEditorController();
6. options: RichEditorOptions = { controller: this.controller };
7. @State caretRect: string = "not found";

9. build() {
10. Column() {
11. Button('get caret rect')
12. .onClick(() => {
13. let rectCaret = this.controller.getCaretRect();
14. if(rectCaret == undefined) {
15. this.caretRect = 'undefined';
16. } else {
17. this.caretRect = 'X: ' + rectCaret.x + '\nY: ' + rectCaret.y
18. + '\nWidth: ' + rectCaret.width + '\nHeight: ' + rectCaret.height;
19. }
20. })
21. .fontSize(24)
22. .width("60%")
23. .height("10%")

25. Text(this.caretRect)
26. .margin(12)
27. .fontSize(24)

29. RichEditor(this.options)
30. .onReady(() => {
31. this.controller.addTextSpan('12345678901234567890', {
32. style:
33. {
34. fontColor: Color.Orange,
35. fontSize: 50
36. }
37. })
38. })
39. .borderWidth(1)
40. .borderColor(Color.Red)
41. .width("100%")
42. .height("60%")
43. }
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Qw-RaO4lSmO1u4Q73ErdOA/zh-cn_image_0000002558766310.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=E1D420FEFCCE00054956363A765A52C2BB7419A9EBB45B22EBF0F49D9830D92E)

### 示例26（设置最大行数和最大字符数）

从API version 18开始，该示例通过[maxLength](ts-basic-components-richeditor.md#maxlength18)设置可输入的最大字符数，通过[maxLines](ts-basic-components-richeditor.md#maxlines18)设置可输入的最大行数。

```
1. @Entry
2. @Component
3. struct RichEditorExample {
4. @State text: string = "As the sun begins to set, casting a warm golden hue across the sky," +
5. "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
6. " pink, and lavender, creating a breathtaking tapestry that stretches as far as the eye can see." +
7. "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil." +
8. "it casts a warm," +
9. "golden hue that spreads like liquid amber across the vast expanse of the sky." +
10. "The once-blue heavens gradually transform, " +
11. "now painted in a breathtaking palette of soft oranges, pinks, " +
12. "and purples, each color blending seamlessly into the next. Wisps of clouds, tinged with fiery edges, " +
13. "float lazily amidst this celestial canvas," +
14. "creating a scene so serene and beautiful that it almost seems to pause time itself." +
15. "As the sun begins to set, casting a warm golden hue across the sky," +
16. "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
17. " pink, and lavender, creating a breathtaking tapestry that stretches as far as the eye can see." +
18. "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil." +
19. "it casts a warm," +
20. "golden hue that spreads like liquid amber across the vast expanse of the sky." +
21. "The once-blue heavens gradually transform, ";
22. @State maxLineList: (number | undefined)[] = [2, 6, undefined];
23. @State maxLineIndex: number = 0;
24. @State maxLineStringList: (string)[] = ["2", "6", "undefined"];
25. richEditorStyledString: MutableStyledString = new MutableStyledString("");
26. controller1: RichEditorController = new RichEditorController();
27. controller2: TextInputController = new TextInputController();
28. controller3: RichEditorController = new RichEditorController();
29. controller4: RichEditorStyledStringController = new RichEditorStyledStringController();
30. controller: RichEditorController = new RichEditorController();
31. option: RichEditorOptions = { controller: this.controller };

33. build() {
34. Column() {
35. Text("当前的maxLength为7 ")
36. .margin(10)
37. .fontSize(25)
38. Row() {
39. Button("插入占1字符数的图片")
40. .onClick(() => {
41. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
42. this.controller1.addImageSpan($r('app.media.startIcon'),
43. {
44. imageStyle:
45. {
46. size: ["57px", "57px"]
47. }
48. })
49. })
50. Button("插入占2字符数图片")
51. .onClick(() => {
52. this.controller1.addSymbolSpan($r("sys.symbol.ohos_trash"),
53. {
54. style:
55. {
56. fontSize: 30
57. }
58. })
59. })
60. .margin({ left: 20 })
61. }

63. RichEditor({ controller: this.controller1 })
64. .width('95%')
65. .margin(10)
66. .height(60)
67. .maxLength(7)
68. .backgroundColor('rgb(240,250,255)')
69. Text("当前的maxLine为 " + this.maxLineStringList[this.maxLineIndex]).margin(10)
70. .fontSize(25)
71. Button("更改maxLines").onClick(() => {
72. this.maxLineIndex++;
73. if (this.maxLineIndex > this.maxLineList.length - 1) {
74. this.maxLineIndex = 0;
75. }
76. })
77. RichEditor({ controller: this.controller3 })
78. .onReady(() => {
79. this.controller3.addTextSpan(this.text,
80. {
81. style:
82. {
83. fontColor: 'rgb(0,74,175)'
84. }
85. })
86. })
87. .margin(10)
88. .width('95%')
89. .maxLines(this.maxLineList[this.maxLineIndex])
90. .backgroundColor('rgb(240,250,255)')
91. }
92. }
93. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/97kE3ZzBQbePFei-moX-xg/zh-cn_image_0000002558606652.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=FB1234806BF9CA254E2BBBD737EE11F38F1EFC46E83794E5CD4BD4A559427CDD)

### 示例27（文本设置Url样式）

从API version 19开始，该示例通过在addTextSpan和UpdateSpanStyle接口中加入[UrlStyle](ts-basic-components-richeditor.md#richeditorurlstyle19)，来实现文本点击时跳转到指定链接的功能。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct RichEditorExample {
6. controller: RichEditorController = new RichEditorController();
7. options: RichEditorOptions = { controller: this.controller };

9. build() {
10. Column() {
11. Row() {
12. Button("Add Example Url").onClick(() => {
13. this.controller.addTextSpan("示例网址", {
14. urlStyle: { url: "https://www.example.com" }
15. })
16. })
17. Button("Clear Url").onClick(() => {
18. this.controller.updateSpanStyle({
19. start: 0,
20. textStyle: {},
21. urlStyle: { url: "" }
22. })
23. })
24. }

26. Row() {
27. RichEditor(this.options)
28. .height('35%')
29. .border({ width: 1, color: Color.Blue })
30. }
31. }
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/k5MZIx2HRFeHqU_8NSx9AQ/zh-cn_image_0000002589326179.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=77FF47FCF2A8252BFC23EA153341DD2BE4BC73583126C61F6D8C37DA3ACF3975)

### 示例28（开启带样式的撤销还原能力）

从API version 20开始，该示例对于不使用属性字符串的富文本组件，可以通过配置[undoStyle](ts-basic-components-richeditor.md#undostyle20)属性为UndoStyle.KEEP\_STYLE，以支持撤销还原时保留原内容的样式。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct StyledUndo {
6. controller: RichEditorController = new RichEditorController();
7. options: RichEditorOptions = { controller: this.controller };
8. private start: number = 0;
9. private end: number = 0;
10. @State undoStyle: UndoStyle = UndoStyle.KEEP_STYLE;
11. build() {
12. Column() {
13. Column() {
14. Row({space:2}) {
15. Button("插入文本").onClick(() => {
16. this.controller.addTextSpan("插入文本",
17. {
18. style:
19. {
20. fontColor: Color.Orange,
21. fontSize: 32
22. }
23. })
24. })
25. Button("插入图片").onClick(() => {
26. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
27. this.controller.addImageSpan($r('app.media.startIcon'),
28. {
29. imageStyle:
30. {
31. size: ["100px", "100px"]
32. }
33. });
34. })
35. Button("插入Symbol").onClick(() => {
36. this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
37. {
38. style:
39. {
40. fontSize: 32
41. }
42. });
43. })
44. }
45. .borderWidth(1)
46. .borderColor(Color.Red)
47. .justifyContent(FlexAlign.Center)
48. .width("100%")
49. .height("10%")
50. Row({space:2}) {
51. Button("更新选中范围样式").onClick(() => {
52. if (this.start < this.end) {
53. this.controller.updateSpanStyle({
54. start: this.start,
55. end: this.end,
56. textStyle:
57. {
58. fontColor: Color.Red,
59. fontWeight: FontWeight.Bolder
60. }
61. });
62. }
63. })
64. Button("删除选中范围内容").onClick(() => {
65. if (this.start < this.end) {
66. this.controller.deleteSpans({
67. start: this.start,
68. end: this.end
69. })
70. }
71. })
72. }
73. .borderWidth(1)
74. .borderColor(Color.Red)
75. .justifyContent(FlexAlign.Center)
76. .width("100%")
77. .height("10%")
78. Row({space:2}) {
79. Button("撤销时不还原样式").onClick(() => {
80. this.undoStyle = UndoStyle.CLEAR_STYLE;
81. })
82. Button("撤销时还原样式").onClick(() => {
83. this.undoStyle = UndoStyle.KEEP_STYLE;
84. })
85. }
86. .borderWidth(1)
87. .borderColor(Color.Red)
88. .justifyContent(FlexAlign.Center)
89. .width("100%")
90. .height("10%")
91. }
92. Column() {
93. RichEditor(this.options)
94. .onReady(()=>{
95. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
96. this.controller.addImageSpan($r('app.media.startIcon'),
97. {
98. imageStyle:
99. {
100. size: ["100px", "100px"]
101. }
102. });
103. this.controller.addTextSpan("初始化图文混排内容",
104. {
105. style:
106. {
107. fontColor: Color.Orange,
108. fontSize: 32
109. }
110. })
111. this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
112. {
113. style:
114. {
115. fontSize: 32
116. }
117. });
118. })
119. .undoStyle(this.undoStyle)
120. .onSelect((value: RichEditorSelection) => {
121. this.start = value.selection[0];
122. this.end = value.selection[1];
123. })
124. .borderWidth(1)
125. .borderColor(Color.Green)
126. .width("100%")
127. .height("50%")
128. }
129. }
130. }
131. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/5VS-sVHNTp6Qk0FQuKNcpg/zh-cn_image_0000002589246121.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=A673BF1B453D840AC076DCF9431E30D36CF486BA6C6274F983FA9176C1F77E61)

### 示例29（文本设置预设段落样式）

从API version 20开始，该示例通过[setTypingParagraphStyle](ts-basic-components-richeditor.md#settypingparagraphstyle20)接口设置预设段落样式。

```
1. @Entry
2. @Component
3. struct RichEditorExample {
4. controller: RichEditorController = new RichEditorController()
5. options: RichEditorOptions = { controller: this.controller }
6. ssController: RichEditorStyledStringController = new RichEditorStyledStringController()
7. ssOptions: RichEditorStyledStringOptions = { controller: this.ssController }
8. contentChangedListener: StyledStringChangedListener = {
9. onWillChange: (value: StyledStringChangeValue) => {
10. let range = '[ ' + value.range.start + ' , ' + value.range.end + ' ]';
11. let replaceString = value.replacementString.getString();
12. console.info('styledString, onWillChange, range=' + range);
13. console.info('styledString, onWillChange, replaceString=' + replaceString);
14. let styles: Array<SpanStyle> = []
15. if (replaceString.length != 0) {
16. styles = value.replacementString.getStyles(0, replaceString.length, StyledStringKey.PARAGRAPH_STYLE)
17. }
18. styles.forEach((style) => {
19. let value = style.styledValue
20. let paraStyle: ParagraphStyle = value as ParagraphStyle
21. if (paraStyle != undefined) {
22. console.info('styledString, onWillChange, textAlign=' + JSON.stringify(paraStyle.textAlign)
23. + ', textIndent=' + JSON.stringify(paraStyle.textIndent)
24. + ', maxLines=' + JSON.stringify(paraStyle.maxLines)
25. + ', overflow=' + JSON.stringify(paraStyle.overflow)
26. + ', wordBreak=' + JSON.stringify(paraStyle.wordBreak)
27. + ', leadingMargin=' + JSON.stringify(paraStyle.leadingMargin)
28. + ', paragraphSpacing=' + JSON.stringify(paraStyle.paragraphSpacing)
29. );
30. }
31. })
32. return true;
33. }
34. }

36. build() {
37. Column() {
38. Row() {
39. Text('ParaStyle')
40. // 设置预设段落样式为居中对齐
41. Button('setStyle1').onClick(() => {
42. let paragraphStyle: RichEditorParagraphStyle = {
43. textAlign: TextAlign.Center
44. }
45. this.controller.setTypingParagraphStyle(paragraphStyle)
46. this.ssController.setTypingParagraphStyle(paragraphStyle)
47. })
48. // 设置预设段落样式为左对齐、带有缩进
49. Button('setStyle2').onClick(() => {
50. let paragraphStyle: RichEditorParagraphStyle = {
51. textAlign: TextAlign.Start,
52. leadingMargin: 80
53. }
54. this.controller.setTypingParagraphStyle(paragraphStyle)
55. this.ssController.setTypingParagraphStyle(paragraphStyle)
56. })
57. // 清除预设段落样式
58. Button('clearParaStyle').onClick(() => {
59. this.controller.setTypingParagraphStyle(undefined)
60. this.ssController.setTypingParagraphStyle(undefined)
61. })
62. }

64. Row() {
65. Column() {
66. RichEditor(this.options)
67. .height('25%')
68. .width('100%')
69. .border({ width: 1, color: Color.Blue })
70. .onWillChange((value: RichEditorChangeValue) => {
71. console.info('controller, onWillChange, rangeBefore=' + JSON.stringify(value.rangeBefore))
72. value.replacedSpans.forEach((item: RichEditorTextSpanResult) => {
73. console.info('controller, onWillChange, replacedTextSpans=' + JSON.stringify(item))
74. })
75. return true
76. })
77. RichEditor(this.ssOptions)
78. .height('25%')
79. .width('100%')
80. .onReady(() => {
81. this.ssController.onContentChanged(this.contentChangedListener);
82. })
83. }
84. }
85. }
86. }
87. }
```

### 示例30（设置装饰线粗细和多装饰线）

从API version 20开始，该示例通过[thicknessScale](ts-universal-styled-string.md#decorationstyle)设置装饰线粗细，通过[enableMultiType](ts-universal-styled-string.md#decorationoptions20)设置多装饰线。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. private controller: RichEditorController = new RichEditorController();
7. private styledStringController: RichEditorStyledStringController = new RichEditorStyledStringController();

9. build() {
10. Column({ space: 20 }) {
11. RichEditor({ controller: this.controller })
12. .onReady(() => {
13. // 预置一段文本
14. this.controller.addTextSpan('一段预置的文本', {
15. style: {
16. fontSize: 25,
17. decoration: {
18. type: TextDecorationType.LineThrough,
19. // 设置装饰线粗细比例为2
20. thicknessScale: 2
21. }
22. }
23. })
24. })

26. // 设置富文本多装饰线
27. RichEditor({ controller: this.styledStringController })

29. Button('追加粗细比例为8的文本')
30. .fontSize(20)
31. .onClick(() => {
32. this.controller.addTextSpan('追加的文本', {
33. style: {
34. fontSize: 25,
35. decoration: {
36. type: TextDecorationType.LineThrough,
37. // 设置装饰线粗细比例为8
38. thicknessScale: 8
39. }
40. }
41. })
42. })

44. Button('修改全段文本的粗细比例为4')
45. .fontSize(20)
46. .onClick(() => {
47. this.controller.updateSpanStyle({
48. start: 0,
49. end: 1000, // 下标超过文本长度时，会更新整段文本
50. textStyle: {
51. decoration: {
52. type: TextDecorationType.LineThrough,
53. // 设置装饰线粗细比例为4
54. thicknessScale: 4
55. }
56. }
57. })
58. })

60. Button('多装饰线文本')
61. .fontSize(20)
62. .onClick(() => {
63. let mutString: MutableStyledString = new MutableStyledString('设置富文本多装饰线', [
64. {
65. start: 0,
66. length: 9,
67. styledKey: StyledStringKey.FONT,
68. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(25) })
69. },
70. {
71. start: 0,
72. length: 5,
73. styledKey: StyledStringKey.DECORATION,
74. styledValue: new DecorationStyle(
75. {
76. type: TextDecorationType.Underline,
77. },
78. {
79. // 开启多装饰线
80. enableMultiType: true
81. }
82. )
83. },
84. {
85. start: 2,
86. length: 4,
87. styledKey: StyledStringKey.DECORATION,
88. styledValue: new DecorationStyle(
89. {
90. type: TextDecorationType.LineThrough,
91. },
92. {
93. // 开启多装饰线
94. enableMultiType: true
95. }
96. )
97. },
98. {
99. start: 4,
100. length: 5,
101. styledKey: StyledStringKey.DECORATION,
102. styledValue: new DecorationStyle(
103. {
104. type: TextDecorationType.Overline,
105. },
106. {
107. // 开启多装饰线
108. enableMultiType: true
109. }
110. )
111. },
112. ])
113. this.styledStringController.setStyledString(mutString);
114. })
115. }
116. .height('100%')
117. .width('100%')
118. .justifyContent(FlexAlign.Center)
119. .alignItems(HorizontalAlign.Center)
120. }
121. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/LcwNN0KxQlauCzRqMV7H0g/zh-cn_image_0000002558766312.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=984D71EA68DB21FC7821B4341040E6FFAF51A96F14B79F27DBEFE519E9C963CF)

### 示例31（设置开启中西文自动间距）

从API version 20开始，该示例通过[enableAutoSpacing](ts-basic-components-richeditor.md#enableautospacing20)属性设置中西文自动间距。

```
1. @Entry
2. @Component
3. struct AutoSpacing {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };
6. @State enableAutoSpace: boolean = false;

8. build() {
9. Column() {
10. Column() {
11. Row({ space: 2 }) {
12. Button("插入中西文内容").onClick(() => {
13. this.controller.addTextSpan("Add文本Span",
14. {
15. style:
16. {
17. fontColor: Color.Orange,
18. fontSize: 20
19. }
20. })
21. })
22. Button("插入图片").onClick(() => {
23. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
24. this.controller.addImageSpan($r('app.media.startIcon'),
25. {
26. imageStyle:
27. {
28. size: ["100px", "100px"]
29. }
30. });
31. })
32. Button("插入Symbol").onClick(() => {
33. this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
34. {
35. style:
36. {
37. fontSize: 32
38. }
39. });
40. })
41. }
42. .borderWidth(1)
43. .borderColor(Color.Red)
44. .justifyContent(FlexAlign.Center)
45. .width("100%")
46. .height("10%")

48. Row({ space: 2 }) {
49. Button("开启中西文自动间距").onClick(() => {
50. this.enableAutoSpace = true;
51. })
52. Button("关闭中西文自动间距").onClick(() => {
53. this.enableAutoSpace = false;
54. })
55. }
56. .borderWidth(1)
57. .borderColor(Color.Red)
58. .justifyContent(FlexAlign.Center)
59. .width("100%")
60. .height("10%")
61. }

63. Column() {
64. RichEditor(this.options)
65. .onReady(() => {
66. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
67. this.controller.addImageSpan($r('app.media.startIcon'),
68. {
69. imageStyle:
70. {
71. size: ["100px", "100px"]
72. }
73. });
74. this.controller.addTextSpan("中西文Auto Spacing自动间距",
75. {
76. style:
77. {
78. fontColor: Color.Orange,
79. fontSize: 20
80. }
81. })
82. this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
83. {
84. style:
85. {
86. fontSize: 20
87. }
88. });
89. })
90. .enableAutoSpacing(this.enableAutoSpace)
91. .borderWidth(1)
92. .borderColor(Color.Green)
93. .width("100%")
94. .height("50%")
95. }
96. }
97. }
98. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/AGv-nIzsQQuRfzsTCvS5TA/zh-cn_image_0000002558606654.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=24A720471A5530C7B6639C885A55E05468DDD532144D46673A9250096CFB9536)

### 示例32（设置文本选择的AI菜单）

从API version 22开始，该示例通过[enableSelectedDataDetector](ts-basic-components-richeditor.md#enableselecteddatadetector22)，配置文本选择AI菜单功能。

```
1. @Entry
2. @Component
3. struct Demo32 {
4. controller: RichEditorController = new RichEditorController();
5. textSpanOptions: RichEditorTextSpanOptions = { style: { fontSize: 20 } };
6. exampleText: string = '示例网址：www.example.com';

8. build() {
9. Column() {
10. Row() {
11. RichEditor({ controller: this.controller })
12. .onReady(() => {
13. this.controller.addTextSpan(this.exampleText, this.textSpanOptions)
14. })
15. .copyOptions(CopyOptions.LocalDevice)
16. .enableSelectedDataDetector(true)
17. .border({ width: 1, color: Color.Black })
18. .height(300)
19. .margin(10)
20. }
21. }
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/VE3uyejxRniOMsCNVzqxEw/zh-cn_image_0000002589326181.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=8FA1948AE07EF9D2EFEE825227CBE1D2C98555F285056CCF55F06B220286C43B)

### 示例33（设置监听输入法绑定事件）

从API version 22开始，该示例通过[onWillAttachIME](ts-basic-components-richeditor.md#onwillattachime22)事件监听输入法绑定事件。

```
1. @Entry
2. @Component
3. struct SetOnWillAttachIME {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };
6. @State message: string = "RichEditor未绑定输入法"

8. build() {
9. Column() {
10. Text(this.message)
11. .fontSize(24)
12. .width("100%")
13. .textAlign(TextAlign.Center)
14. RichEditor(this.options)
15. .onReady(() => {
16. this.controller.addTextSpan("RichEditor组件",
17. {
18. style:
19. {
20. fontColor: Color.Orange,
21. fontSize: 30
22. }
23. })
24. })
25. .onWillAttachIME((value:IMEClient) => {
26. // 给输入法传递自定义消息
27. const inputConfig: InputMethodExtraConfig = {
28. customSettings: {
29. component: 'RichEditor',
30. id: 8 as number,
31. isEnable: true
32. }
33. };
34. value.setExtraConfig(inputConfig);
35. this.message = "RichEditor已绑定输入法"
36. })
37. .borderWidth(1)
38. .borderColor(Color.Green)
39. .width("100%")
40. .height("20%")
41. }
42. .height("100%")
43. .justifyContent(FlexAlign.Center)
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/H6BXDzQBTsutf0rvbIWSJw/zh-cn_image_0000002589246123.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=1A35DC38A0F853041F61831C9ABDB7B3ED00A2A8A415FD4E4E630FA095A105DF)

### 示例34（删除输入框文本尾部字符）

从API version 23开始，该示例通过[deleteBackward](ts-basic-components-richeditor.md#deletebackward23)事件在编辑态用自定义键盘删除光标前字符。

```
1. @Entry
2. @Component
3. struct RichEditorExample {
4. controller: RichEditorController = new RichEditorController();

6. // 自定义键盘删除键
7. @Builder
8. CustomKeyboardBuilder() {
9. Column() {
10. Button('DELETE')
11. .width(200)
12. .height(60)
13. .backgroundColor(Color.Blue)
14. .fontColor(Color.White)
15. .fontSize(16)
16. .onClick(() => {
17. // 调用deleteBackward接口删除字符
18. this.controller.deleteBackward()
19. })
20. }
21. .padding(10)
22. .backgroundColor(Color.Gray)
23. }

25. build() {
26. Column() {
27. Blank()
28. .height(400)
29. RichEditor({ controller: this.controller })
30. .customKeyboard(this.CustomKeyboardBuilder())
31. .margin(10)
32. .border({ width: 1 })
33. .height(150)
34. .borderWidth(1)
35. .borderColor(Color.Blue)
36. .width("100%")
37. .onReady(() => {
38. // 设置初始文本用于测试
39. this.controller.addTextSpan('点击DELETE键测试删除功能', {
40. style: {
41. fontColor: Color.Black,
42. fontSize: 16
43. }
44. })
45. })
46. }.margin(90)
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/svOxqdpIROGUf5VLPfVm3A/zh-cn_image_0000002558766314.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=BAE9D67F084ACF6F3658B8285BFAD40497FEBCB7512BB0EF913F8B66FF29B509)

### 示例35（优化小语种文字显示）

该示例通过[includeFontPadding](ts-basic-components-richeditor.md#includefontpadding23)属性，在首行文字顶部和尾行文字底部添加文字内边距，同时通过[fallbackLineSpacing](ts-basic-components-richeditor.md#fallbacklinespacing23)属性实现行高自适应，基于文字实际高度动态调整。

从API version 23开始，新增includeFontPadding、fallbackLineSpacing属性。

```
1. @Entry
2. @Component
3. struct RichEditorExample {
4. controller: RichEditorController = new RichEditorController();
5. @State fallbackLineSpacing: boolean = true;
6. @State includeFontPadding: boolean = true;

8. build() {
9. Column() {
10. RichEditor({ controller: this.controller })
11. .onReady(() => {
12. this.controller.addTextSpan('བོད་ཀྱི་སྐད་ཡིག་ནི་བོད་མིའི་རྒྱུན་ལྡན་པའི་སྐད་ཡིག་དང་།\n འཇིག་རྟེན་གྱི་ཆོས་ལུགས་དང་རྒྱུན་ལྡན་པའི་ཆོས་ལུགས་ཀྱི་དོན་ཚན་གྱི་སྐད་ཡིག་རེད།\n',
13. {
14. style: {
15. fontColor: Color.Black,
16. fontSize: "30",
17. lineHeight: 10
18. },
19. paragraphStyle: {
20. textAlign: TextAlign.Start,
21. }
22. })
23. this.controller.addTextSpan('བོད་ཀྱི་སྐད་ཡིག་ནི་བོད་མིའི་རྒྱུན་ལྡན་པའི་སྐད་ཡིག་དང་།\n འཇིག་རྟེན་གྱི་ཆོས་ལུགས་དང་རྒྱུན་ལྡན་པའི་ཆོས་ལུགས་ཀྱི་དོན་ཚན་གྱི་སྐད་ཡིག་རེད།',
24. {
25. style: {
26. fontColor: Color.Black,
27. fontSize: "30",
28. },
29. paragraphStyle: {
30. textAlign: TextAlign.Start,
31. }
32. })
33. })
34. .width("100%")
35. .height("35%")
36. .border({ width: 1, radius: 5 })
37. .draggable(false)
38. .includeFontPadding(this.includeFontPadding)
39. .fallbackLineSpacing(this.fallbackLineSpacing)
40. Row() {
41. Button('开启文字行间自适应')
42. .onClick(() => {
43. this.fallbackLineSpacing = true
44. })
45. .width("45%")
46. .height("10%")
47. .margin({ right: 10 })
48. Button('关闭文字行间自适应')
49. .onClick(() => {
50. this.fallbackLineSpacing = false
51. })
52. .width("45%")
53. .height("10%")
54. .margin({ left: 5 })
55. }
56. .margin({ top: 20 })

58. Row() {
59. Button('开启段落首行尾行边距增高')
60. .onClick(() => {
61. this.includeFontPadding = true
62. })
63. .width("45%")
64. .height("10%")
65. .margin({ right: 10 })
66. Button('关闭段落首行尾行边距增高')
67. .onClick(() => {
68. this.includeFontPadding = false
69. })
70. .width("45%")
71. .height("10%")
72. .margin({ left: 5 })
73. }
74. .margin({ top: 20 })
75. }
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/XK7L4je9SbWJhovZe7BOjw/zh-cn_image_0000002558606656.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=5FF868EC5BA81180D2409405DD07C9F4FC037D559B1B00628B5CE429BA56D9A0)

### 示例36（设置开启行首标点符号压缩）

该示例通过[compressLeadingPunctuation](ts-basic-components-richeditor.md#compressleadingpunctuation23)属性设置行首标点符号压缩。

从API version 23开始，新增compressLeadingPunctuation属性。

```
1. @Entry
2. @Component
3. struct CompressLeadingPunctuationDemo {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };

7. @State compressLeadingPunctuation: boolean = false;
8. @State text: string = '「0123456789\n『0123456789\n（0123456789\n《0123456789\n〈0123456789\n【0123456789\n〖0123456789\n〔0123456789\n［0123456789\n｛0123456789';

10. build() {
11. Column() {
12. RichEditor(this.options)
13. .onReady(() => {
14. this.controller.addTextSpan(this.text)
15. })
16. .compressLeadingPunctuation(this.compressLeadingPunctuation)
17. .borderWidth(1)
18. .borderColor(Color.Green)
19. .align(Alignment.Center)
20. .height("30%")
21. .width("50%")

23. Column() {
24. Button("开启行首标点符号压缩").onClick(() => {
25. this.compressLeadingPunctuation = true
26. }).margin({ top: 10 })
27. Button("关闭行首标点符号压缩").onClick(() => {
28. this.compressLeadingPunctuation = false
29. }).margin({ top: 10 })
30. }
31. }.width("100%").padding(20)
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/LyfoaOZHQvKnjwGm_cuBmg/zh-cn_image_0000002589326183.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=AF4F8D2FE241A540493CF76B90998023DDC4CA2461DF89AD8A820382A9AA4572)

### 示例37（设置拖动预览样式）

该示例通过[selectedDragPreviewStyle](ts-basic-components-richeditor.md#selecteddragpreviewstyle23)接口设置拖动预览样式。

从API version 23开始，新增selectedDragPreviewStyle接口。

```
1. @Entry
2. @Component
3. struct RichEditorDemo {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };

7. build() {
8. Column({ space: 2 }) {
9. RichEditor(this.options)
10. .onReady(() => {
11. this.controller.addTextSpan('RichEditor selectedDragPreviewStyle')
12. })
13. .borderWidth(1)
14. .borderColor(Color.Green)
15. .draggable(true)
16. .selectedDragPreviewStyle({ color: Color.Gray })
17. .width('100%')
18. .height('20%')
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/sK7omFLsRKiDLrotwtmp3A/zh-cn_image_0000002589246125.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=0AE82105AD01CE28404376D94BA4F6EBF2B822D9CC8EE5F90F4C5DDC4F15C16F)

### 示例38（设置单行模式）

该示例通过[singleLine](ts-basic-components-richeditor.md#singleline23)接口设置单行模式。

从API version 23开始，新增singleLine接口。

```
1. @Entry
2. @Component
3. struct SingleLineDemo {
4. controller: RichEditorController = new RichEditorController();
5. textSpanOptions: RichEditorTextSpanOptions = { style: { fontSize: 30 } };
6. exampleText: string = '这是一段示例文本\n这是一段示例文本\n这是一段示例文本';
7. @State enableSingleLine: boolean = false;

9. build() {
10. Column() {
11. Row() {
12. RichEditor({ controller: this.controller })
13. .onReady(() => {
14. this.controller.addTextSpan(this.exampleText, this.textSpanOptions)
15. })
16. .singleLine(this.enableSingleLine)
17. .border({ width: 1, color: Color.Black })
18. .margin(10)
19. }
20. Row() {
21. Button('切换单行模式').onClick((event: ClickEvent) => {
22. this.enableSingleLine = true
23. }).margin(5)
24. Button('切换多行模式').onClick((event: ClickEvent) => {
25. this.enableSingleLine = false
26. }).margin(5)
27. }
28. }
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/j4HxJZBjS22HHhbgm3Lj2g/zh-cn_image_0000002558766316.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=D78941ED21784D1ECB63EB7485F486D4E2CD54E36CE989FC580CA536052542EC)
