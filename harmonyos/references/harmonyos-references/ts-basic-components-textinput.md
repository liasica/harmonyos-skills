---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput
title: TextInput
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > TextInput
category: harmonyos-references
scraped_at: 2026-04-28T08:01:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b1abb92296f4f64fdc2205fca6521349564bb8b63b4fd8974d1ea6d13524e87
---

单行文本输入框组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](ts-basic-components-richeditor.md)组件。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

TextInput(value?: TextInputOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextInputOptions](ts-basic-components-textinput.md#textinputoptions对象说明) | 否 | TextInput组件参数。 |

## TextInputOptions对象说明

PhonePC/2in1TabletTVWearable

TextInput初始化参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| placeholder | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置无输入时的提示文本。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置输入框当前的文本内容。  建议通过onChange事件将状态变量与文本实时绑定，  避免组件刷新时TextInput中的文本内容异常。  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。 |
| controller8+ | [TextInputController](ts-basic-components-textinput.md#textinputcontroller8) | 否 | 是 | 设置TextInput控制器。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)，还支持以下属性：

说明

默认情况下，通用属性[padding](ts-universal-attributes-size.md#padding)的默认值为：

{

top: '8vp',

right: '16vp',

bottom: '8vp',

left: '16vp'

}

输入框开启下划线模式时，通用属性padding的默认值为：

{

top: '12vp',

right: '0vp',

bottom: '12vp',

left: '0vp'

}

当输入框设置padding为0时，可设置[borderRadius](ts-universal-attributes-border.md#borderradius)为0避免光标被截断。当光标在文本框边缘显示异常时，请检查是否是padding、borderRadius属性影响造成。

从API version 10开始，单行输入框可设置.width('auto')使组件宽度自适应文本宽度，自适应时组件宽度受constraintSize属性以及父容器传递的最大最小宽度限制，其余使用方式参考[尺寸设置](ts-universal-attributes-size.md)。

### type

PhonePC/2in1TabletTVWearable

type(value: InputType)

设置输入框类型。

不同的InputType会拉起对应类型的键盘，同时限制输入。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [InputType](ts-basic-components-textinput.md#inputtype枚举说明) | 是 | 输入框类型。  默认值：InputType.Normal |

说明

密码填充服务需要特定的输入框类型。如何使用密码填充服务参考[快速适配](../harmonyos-guides/passwordvault-quick-adaptation.md)。

设置[密码模式](../harmonyos-guides/arkts-common-components-text-input.md#密码模式)时，装饰线[decoration](ts-basic-components-textinput.md#decoration12)、下划线[showUnderline](ts-basic-components-textinput.md#showunderline10)不生效。

### placeholderColor

PhonePC/2in1TabletTVWearable

placeholderColor(value: ResourceColor)

设置placeholder文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | placeholder文本颜色。  默认值：跟随主题。  Wearable设备上默认值为：'#99ffffff' |

### placeholderFont

PhonePC/2in1TabletTVWearable

placeholderFont(value?: Font)

设置placeholder文本样式，包括字体大小、字体粗细、字体族、字体风格。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 否 | placeholder文本样式。  Wearable设备上默认值为：18fp |

说明

可以使用[loadFontSync](js-apis-graphics-text.md#loadfontsync)注册自定义字体。

### enterKeyType

PhonePC/2in1TabletTVWearable

enterKeyType(value: EnterKeyType)

设置输入法回车键类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EnterKeyType](ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 输入法回车键类型。  默认值：EnterKeyType.Done |

### caretColor

PhonePC/2in1TabletTVWearable

caretColor(value: ResourceColor)

设置输入框光标颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 输入框光标颜色。  默认值：'#007DFF' |

说明

从API version 12开始，此接口支持设置文本手柄颜色，光标和文本手柄颜色保持一致。

### maxLength

PhonePC/2in1TabletTVWearable

maxLength(value: number)

设置文本的最大输入字符数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 文本的最大输入字符数。  默认值：Infinity，可以无限输入。  **说明：**  当不设置该属性或设置异常值时，取默认值，设置小数时，取整数部分，设置值超过2^31-1时，可能导致异常行为。 |

### fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

设置字体颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 字体颜色。  Wearable设备上默认值为：'#dbffffff' |

### fontSize

PhonePC/2in1TabletTVWearable

fontSize(value: Length)

设置字体大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp。不支持设置百分比字符串。  Wearable设备上默认值为：18fp |

### fontStyle

PhonePC/2in1TabletTVWearable

fontStyle(value: FontStyle)

设置字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 字体样式。  默认值：FontStyle.Normal |

### fontWeight

PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | ResourceStr)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](ts-appendix-enums.md#fontweight) | [ResourceStr](ts-types.md#resourcestr) | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal  从API version 20开始，支持Resource类型。 |

### fontFamily

PhonePC/2in1TabletTVWearable

fontFamily(value: ResourceStr)

设置字体列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 字体列表。默认字体'HarmonyOS Sans'。  使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。例如：'Arial,HarmonyOS Sans'。  应用当前支持'HarmonyOS Sans'字体和自定义字体。  卡片当前仅支持'HarmonyOS Sans'字体。 |

说明

推荐使用[loadFontSync](js-apis-graphics-text.md#loadfontsync)注册自定义字体。

### inputFilter8+

PhonePC/2in1TabletTVWearable

inputFilter(value: ResourceStr, error?: Callback<string>)

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。

单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

从API version 11开始，设置inputFilter且输入的字符不为空字符，会导致[type](ts-basic-components-textinput.md#type)接口附带的文本过滤效果失效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 正则表达式。 |
| error | Callback<string> | 否 | 正则匹配失败时，返回被过滤的内容。 |

### copyOption9+

PhonePC/2in1TabletTVWearable

copyOption(value: CopyOptions)

设置输入的文本是否可复制。设置CopyOptions.None时，只支持粘贴和全选。

设置CopyOptions.None时，不允许拖拽。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](ts-appendix-enums.md#copyoptions9) | 是 | 输入的文本是否可复制。  默认值：CopyOptions.LocalDevice，支持设备内复制。 |

### showPasswordIcon9+

PhonePC/2in1TabletTVWearable

showPasswordIcon(value: boolean)

设置当密码输入模式时，输入框末尾的图标是否显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 密码输入模式时，输入框末尾的图标是否显示。  true表示显示，false表示不显示。  默认值：TV设备为false，其他设备为true。 |

### style9+

PhonePC/2in1TabletTVWearable

style(value: TextInputStyle | TextContentStyle)

设置输入框为默认风格或内联输入风格，内联输入风格只支持InputType.Normal类型。

输入框类型介绍请参考[type](ts-basic-components-textinput.md#type)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextInputStyle](ts-basic-components-textinput.md#textinputstyle9枚举说明) | [TextContentStyle](ts-appendix-enums.md#textcontentstyle10) | 是 | 输入框为默认风格或内联输入风格。  默认值：TextInputStyle.Default |

### textAlign9+

PhonePC/2in1TabletTVWearable

textAlign(value: TextAlign)

设置文本在输入框中的水平对齐方式。

支持TextAlign.Start、TextAlign.Center和TextAlign.End。TextAlign.JUSTIFY的对齐方式按照TextAlign.Start处理。

可通过[align](ts-universal-attributes-location.md#align)属性控制文本段落在垂直方向上的位置。此组件中不可使用align属性控制文本段落在水平方向上的位置。

* Alignment.TopStart、Alignment.Top、Alignment.TopEnd：内容顶部对齐。
* Alignment.Start、Alignment.Center、Alignment.End：内容垂直居中。
* Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd：内容底部对齐。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextAlign](ts-appendix-enums.md#textalign) | 是 | 文本在输入框中的水平对齐方式。  默认值：TextAlign.Start |

说明

textAlign只能调整文本整体的布局，不影响字符的显示顺序。若需要调整字符的显示顺序，请参考[镜像状态字符对齐](../harmonyos-guides/arkts-internationalization.md#镜像状态字符对齐)。

### textDirection23+

PhonePC/2in1TabletTVWearable

textDirection(direction: TextDirection | undefined)

指定文本排版方向，未通过该接口设置时，默认文本排版方向遵循组件布局方向。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [TextDirection](ts-text-common.md#textdirection22) | undefined | 是 | 文本排版方向。  设置为undefined时，按照TextDirection.DEFAULT处理，表现为文本排版方向遵循组件布局方向。 |

### selectedBackgroundColor10+

PhonePC/2in1TabletTVWearable

selectedBackgroundColor(value: ResourceColor)

设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 文本选中底板颜色。 |

### caretStyle10+

PhonePC/2in1TabletTVWearable

caretStyle(value: CaretStyle)

设置光标风格。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CaretStyle](ts-text-common.md#caretstyle10) | 是 | 光标的风格。 |

说明

当同时设置caretColor属性和caretStyle属性中的color参数时，遵循后设置生效原则。

从API version 12开始，此接口支持设置文本手柄颜色，光标和文本手柄颜色保持一致。

### caretPosition10+

PhonePC/2in1TabletTVWearable

caretPosition(value: number)

设置光标位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 光标的位置。  第一个字符前的位置是0。 |

### showUnit10+

PhonePC/2in1TabletTVWearable

showUnit(value: CustomBuilder)

设置控件作为文本框单位。需搭配[showUnderline](ts-basic-components-textinput.md#showunderline10)使用，当showUnderline为true时生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 文本输入时，文本框的显示单位。 |

### showError10+

PhonePC/2in1TabletTVWearable

showError(value?: ResourceStr | undefined)

设置错误状态下提示的错误文本或者不显示错误状态。

当参数类型为ResourceStr并且输入内容不符合定义规范时，提示错误文本，当提示错误单行文本超长时，末尾以省略号显示。当参数类型为undefined时，不显示错误状态。请参考[示例2](ts-basic-components-textinput.md#示例2设置下划线)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | undefined | 否 | 错误状态下提示的错误文本或者不显示错误状态。  默认不显示错误状态。  Wearable设备上字体大小为：13fp，对齐方式为：居中对齐  **说明：**  从API version 12开始，value支持Resource类型。 |

### showUnderline10+

PhonePC/2in1TabletTVWearable

showUnderline(value: boolean)

设置是否开启下划线。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启下划线。  true表示开启，false表示不开启。  默认值：false  下划线默认颜色为'#33182431'，默认粗细为1px，文本框尺寸48vp，下划线只支持InputType.Normal类型。 |

说明

设置[密码模式](../harmonyos-guides/arkts-common-components-text-input.md#密码模式)时，装饰线[decoration](ts-basic-components-textinput.md#decoration12)、下划线[showUnderline](ts-basic-components-textinput.md#showunderline10)不生效。

### passwordIcon10+

PhonePC/2in1TabletTVWearable

passwordIcon(value: PasswordIcon)

设置当密码输入模式时，输入框末尾的图标。

支持jpg、png、bmp、heic和webp类型的图片格式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PasswordIcon](ts-basic-components-textinput.md#passwordicon10对象说明) | 是 | 密码输入模式时，输入框末尾的图标。  默认为系统提供的密码图标。  该图标的固定尺寸为24vp，Wearable设备上默认值为28vp，若引用的图标过大或过小，均显示为固定尺寸。 |

### enableKeyboardOnFocus10+

PhonePC/2in1TabletTVWearable

enableKeyboardOnFocus(value: boolean)

设置TextInput通过点击以外的方式获焦时，是否主动拉起软键盘。

从API version 10开始，获焦默认绑定输入法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 通过点击以外的方式获焦时，是否主动拉起软键盘。  true表示主动拉起软键盘，false表示不主动拉起。  默认值：TV设备为false，其他设备为true。 |

### selectionMenuHidden10+

PhonePC/2in1TabletTVWearable

selectionMenuHidden(value: boolean)

设置是否隐藏系统文本选择菜单。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏系统文本选择菜单。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。  设置为false时，显示系统文本选择菜单。  默认值：false |

### barState10+

PhonePC/2in1TabletTVWearable

barState(value: BarState)

设置内联输入风格编辑态时滚动条的显示模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarState](ts-appendix-enums.md#barstate) | 是 | 内联输入风格编辑态时滚动条的显示模式。  默认值：BarState.Auto |

### maxLines10+

PhonePC/2in1TabletTVWearable

maxLines(value: number)

设置内联输入风格编辑态时文本可显示的最大行数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内联输入风格编辑态时文本可显示的最大行数。  默认值：3  取值范围：(0, UINT32\_MAX] |

### customKeyboard10+

PhonePC/2in1TabletTVWearable

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)

设置自定义键盘。

当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。

自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。

自定义键盘采用覆盖原始界面的方式呈现，当没有开启避让模式或者输入框不需要避让的场景不会对应用原始界面产生压缩或者上提。

自定义键盘无法获取焦点，但是会拦截手势事件。

默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[TextInputController](ts-basic-components-textinput.md#textinputcontroller8).[stopEditing](ts-basic-components-textinput.md#stopediting10)方法控制键盘关闭。

当设置自定义键盘时，可以通过绑定[onKeyPreIme](ts-universal-events-key.md#onkeypreime12)事件规避物理键盘的输入。

从API version 23开始，自定义键盘可以通过[setCustomKeyboardContinueFeature](arkts-apis-uicontext-uicontext.md#setcustomkeyboardcontinuefeature23)开启接续，在切换至其他自定义键盘时，会直接切换，不会触发键盘关闭和拉起动画。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](ts-types.md#custombuilder8) | [ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)22+ | undefined22+ | 是 | 自定义键盘。设定值为undefined时，关闭自定义键盘。 |
| options12+ | [KeyboardOptions](ts-basic-components-richeditor.md#keyboardoptions12) | 否 | 设置自定义键盘是否支持避让功能。 |

### enableAutoFill11+

PhonePC/2in1TabletTVWearable

enableAutoFill(value: boolean)

设置是否启用自动填充。典型场景参考[密码自动填充服务](../harmonyos-guides/passwordvault.md)、[智能填充服务](../harmonyos-guides/scenario-fusion-intelligent-filling.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否启用自动填充。  true表示启用，false表示不启用。  默认值：true |

### enableSelectedDataDetector22+

PhonePC/2in1TabletTVWearable

enableSelectedDataDetector(enable: boolean | undefined)

设置是否对选中文本进行实体识别。该接口依赖设备底层应具有文本识别能力，否则设置不会生效。

当enableSelectedDataDetector设置为true时，默认识别所有类型的实体。

需要[CopyOptions](ts-appendix-enums.md#copyoptions9)为CopyOptions.LocalDevice或CopyOptions.CROSS\_DEVICE时，本功能生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | undefined | 是 | 开启选中词文本识别。  true：开启识别，false：关闭识别。默认值为：true。 |

### passwordRules11+

PhonePC/2in1TabletTVWearable

passwordRules(value: string)

定义生成密码的规则。在触发自动填充时，所设置的密码规则会透传给密码保险箱，用于新密码的生成。

具体使用指导请参考[为应用添加自动生成高强度密码的建议](../harmonyos-guides/passwordvault-custom-strong-password-rules.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 定义生成密码的规则。 |

### cancelButton11+

PhonePC/2in1TabletTVWearable

cancelButton(options: CancelButtonOptions)

设置右侧清除按钮样式，仅支持图片类型的图标。不支持[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)。示例请参考[示例4（设置右侧清除按钮样式）](ts-basic-components-textinput.md#示例4设置右侧清除按钮样式)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CancelButtonOptions](ts-basic-components-search.md#cancelbuttonoptions12对象说明) | 是 | 右侧清除按钮样式选项。  默认值：  {  style: CancelButtonStyle.INPUT  }  Wearable设备上默认值为：28vp |

### selectAll11+

PhonePC/2in1TabletTVWearable

selectAll(value: boolean)

设置初始状态时，是否全选文本。不支持[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否全选文本。  true表示会全选文本，false表示不会全选文本。  默认值：false |

### showCounter11+

PhonePC/2in1TabletTVWearable

showCounter(value: boolean, options?: InputCounterOptions)

设置当通过InputCounterOptions输入的字符数超过阈值时显示计数器。未调用showCounter接口时，默认不显示计数器。

参数value为true时，才能设置options，文本框开启计数下标功能，需要配合[maxLength](ts-basic-components-textinput.md#maxlength)（设置最大字符限制）一起使用。字符计数器显示的效果是当前输入字符数/最大可输入字符数。

当输入字符数大于最大字符数乘百分比值时，显示字符计数器。如果用户设置计数器时不设置InputCounterOptions，那么当前输入字符数超过最大字符数时，边框和计数器下标将变为红色。用户同时设置参数value为true和[InputCounterOptions](ts-universal-attributes-text-style.md#inputcounteroptions11对象说明)，当thresholdPercentage数值在有效区间内，且输入字符数超过最大字符数时，边框和计数器下标将变为红色，框体抖动。highlightBorder设置为false，则不显示红色边框，计数器默认显示红色，框体抖动。

[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)、[密码模式](../harmonyos-guides/arkts-common-components-text-input.md#密码模式)下字符计数器不显示。

[示例5（设置计数器）](ts-basic-components-textinput.md#示例5设置计数器)展示了设置showCounter的效果。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否显示计数器。  true表示显示计数器，false表示不显示。 |
| options | [InputCounterOptions](ts-universal-attributes-text-style.md#inputcounteroptions11对象说明) | 否 | 计数器的配置项。 |

### contentType12+

PhonePC/2in1TabletTVWearable

contentType(value: ContentType)

设置自动填充类型。典型场景参考[智能填充服务](../harmonyos-guides/scenario-fusion-intelligent-filling.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ContentType](ts-basic-components-textinput.md#contenttype12枚举说明) | 是 | 自动填充类型。 |

### underlineColor12+

PhonePC/2in1TabletTVWearable

underlineColor(value: ResourceColor|UnderlineColor|undefined)

设置下划线颜色。

开启输入框下划线[showUnderline](ts-basic-components-textinput.md#showunderline10)时，支持配置下划线颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [UnderlineColor](ts-basic-components-textinput.md#underlinecolor12对象说明) | undefined | 是 | 设置下划线颜色。  当设置下划线颜色模式时，修改下划线颜色。当只设定非特殊状态下的颜色，可以直接输入ResourceColor。设定值为undefined、null、无效值时，所有下划线恢复为默认值。  默认值：主题配置的下划线颜色。主题配置的默认下划线颜色为'#33182431'。 |

### lineHeight12+

PhonePC/2in1TabletTVWearable

lineHeight(value: number | string | Resource)

设置文本的行高。

设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

说明

* 特殊字符字体高度远超出同行的其他字符高度时，文本框出现截断、遮挡、内容相对位置发生变化等不符合预期的显示异常，需要开发者调整组件高度、行高等属性，修改对应的页面布局。
* 设置[密码模式](../harmonyos-guides/arkts-common-components-text-input.md#密码模式)时，通过该接口设置行高[lineHeight](ts-basic-components-textinput.md#lineheight12)不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 文本的文本行高。 |

### decoration12+

PhonePC/2in1TabletTVWearable

decoration(value: TextDecorationOptions)

设置文本装饰线类型样式及其颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextDecorationOptions](ts-universal-attributes-text-style.md#textdecorationoptions12对象说明) | 是 | 文本装饰线对象。  默认值：{  type: TextDecorationType.None,  color: Color.Black,  style: TextDecorationStyle.SOLID  } |

说明

当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。

当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

设置[密码模式](../harmonyos-guides/arkts-common-components-text-input.md#密码模式)时，装饰线[decoration](ts-basic-components-textinput.md#decoration12)、下划线[showUnderline](ts-basic-components-textinput.md#showunderline10)不生效。

### letterSpacing12+

PhonePC/2in1TabletTVWearable

letterSpacing(value: number | string | Resource)

设置文本字符间距。设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示。

对每个字符生效，包括行尾字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 文本字符间距。  单位：[fp](ts-pixel-units.md) |

### fontFeature12+

PhonePC/2in1TabletTVWearable

fontFeature(value: string)

设置文字特性效果，比如数字等宽的特性。

格式为：normal | <feature-tag-value>

<feature-tag-value>的格式为：<string> [ <integer> | on | off ]

<feature-tag-value>的个数可以有多个，中间用','隔开。

例如，使用等宽数字的输入格式为："ss01" on。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 文字特性效果。 |

Font Feature当前支持的属性见[fontFeature属性列表](ts-basic-components-text.md#fontfeature12)。

设置Font Feature属性，Font Feature是OpenType字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持。

更多Font Feature能力介绍可参考https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop和https://sparanoid.com/lab/opentype-features/。

说明

设置[密码模式](../harmonyos-guides/arkts-common-components-text-input.md#密码模式)时，不支持通过fontFeature设置文本样式。

### wordBreak12+

PhonePC/2in1TabletTVWearable

wordBreak(value: WordBreak)

设置文本断行规则。该属性在组件设置[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)时样式生效，但对placeholder文本无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [WordBreak](ts-appendix-enums.md#wordbreak11) | 是 | 内联输入风格编辑态时断行规则。  默认值：WordBreak.BREAK\_WORD |

说明

组件不支持clip属性设置，设置该属性任意枚举值对组件文本截断无影响。

### textOverflow12+

PhonePC/2in1TabletTVWearable

textOverflow(value: TextOverflow)

设置文本超长时的显示方式。仅在[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)的编辑态、非编辑态下支持。

文本截断是按字进行。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，可将wordBreak属性设置为WordBreak.BREAK\_ALL。

当overflow设置为TextOverflow.None时，效果与TextOverflow.Clip相同。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextOverflow](ts-appendix-enums.md#textoverflow) | 是 | 文本超长时的显示方式。  [内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)非编辑态下默认值：TextOverflow.Ellipsis  内联模式编辑态下默认值：TextOverflow.Clip |

说明

TextInput组件不支持设置TextOverflow.MARQUEE模式，当设置为TextOverflow.MARQUEE模式时，[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)非编辑态下显示为TextOverflow.Ellipsis，内联模式编辑态下以及非内联模式下显示为TextOverflow.Clip。

未设置内联模式时，按照默认风格显示。若此时设置textOverflow，则不生效。

### textIndent12+

PhonePC/2in1TabletTVWearable

textIndent(value: Dimension)

设置首行文本缩进。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 首行文本缩进。  默认值：0 |

### minFontSize12+

PhonePC/2in1TabletTVWearable

minFontSize(value: number | string | Resource)

设置文本最小显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

需配合[maxFontSize](ts-basic-components-textinput.md#maxfontsize12)以及[maxLines](ts-basic-components-textinput.md#maxlines10)(组件设置为内联输入风格且编辑态时使用)或布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

minFontSize小于或等于0时，自适应字号不生效，此时按照[fontSize](ts-basic-components-textinput.md#fontsize)属性的值生效，未设置时按照其默认值生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 文本最小显示字号。  单位：[fp](ts-pixel-units.md) |

### maxFontSize12+

PhonePC/2in1TabletTVWearable

maxFontSize(value: number | string | Resource)

设置文本最大显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

需配合[minFontSize](ts-basic-components-textinput.md#minfontsize12)以及[maxLines](ts-basic-components-textinput.md#maxlines10)(组件设置为内联输入风格且编辑态时使用)或布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

maxFontSize小于等于0或者maxFontSize小于minFontSize时，自适应字号不生效，此时按照[fontSize](ts-basic-components-textinput.md#fontsize)属性的值生效，未设置时按照其默认值生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 文本最大显示字号。  单位：[fp](ts-pixel-units.md) |

### heightAdaptivePolicy12+

PhonePC/2in1TabletTVWearable

heightAdaptivePolicy(value: TextHeightAdaptivePolicy)

组件设置为内联输入风格时，设置文本自适应高度的方式。

当设置为TextHeightAdaptivePolicy.MAX\_LINES\_FIRST时，优先使用[maxLines](ts-basic-components-textinput.md#maxlines10)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束，则尝试在[minFontSize](ts-basic-components-textinput.md#minfontsize12)和[maxFontSize](ts-basic-components-textinput.md#maxfontsize12)的范围内缩小字体以显示更多文本。

当设置为TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST时，优先使用minFontSize属性来调整文本高度。如果使用minFontSize属性可以将文本布局在一行中，则尝试在minFontSize和maxFontSize的范围内增大字体并使用最大限度的字体大小。

当设置为TextHeightAdaptivePolicy.LAYOUT\_CONSTRAINT\_FIRST时，与TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST效果一样。

组件设置为非内联输入风格时，设置文本自适应高度(TextHeightAdaptivePolicy)的三种方式效果一样，即在minFontSize和maxFontSize的范围内缩小字体以显示更多文本。

说明

组件设置为内联输入风格，编辑态与非编辑态存在字体大小不一致情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextHeightAdaptivePolicy](ts-appendix-enums.md#textheightadaptivepolicy10) | 是 | 文本自适应高度的方式。  默认值：TextHeightAdaptivePolicy.MAX\_LINES\_FIRST |

### showPassword12+

PhonePC/2in1TabletTVWearable

showPassword(visible: boolean)

设置密码的显隐状态。

当[输入框的类型](ts-basic-components-textinput.md#inputtype枚举说明)设置为Password、NEW\_PASSWORD和NUMBER\_PASSWORD模式时，密码保护功能才能生效。非密码输入模式则不会触发该功能。

[密码模式](../harmonyos-guides/arkts-common-components-text-input.md#密码模式)时，由于输入框后端的状态和前端应用侧的状态管理变量会不一致，可能导致末尾图标的状态异常。建议在[onSecurityStateChange](ts-basic-components-textinput.md#onsecuritystatechange12)上增加状态同步。参考[示例1（设置与获取光标位置）](ts-basic-components-textinput.md#示例1设置与获取光标位置)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 是否显示密码。  true表示会显示密码，false表示不会显示密码。  默认值：false |

### lineBreakStrategy12+

PhonePC/2in1TabletTVWearable

lineBreakStrategy(strategy: LineBreakStrategy)

设置折行规则。该属性在wordBreak不等于breakAll的时候生效，不支持连词符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [LineBreakStrategy](ts-appendix-enums.md#linebreakstrategy12) | 是 | 文本的折行规则。  默认值：LineBreakStrategy.GREEDY  **说明：**  仅设置[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)时该属性生效。 |

### editMenuOptions12+

PhonePC/2in1TabletTVWearable

editMenuOptions(editMenu: EditMenuOptions)

设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。

调用[disableMenuItems](arkts-apis-uicontext-textmenucontroller.md#disablemenuitems20)或[disableSystemServiceMenuItems](arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems20)接口屏蔽文本选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法[onCreateMenu](ts-text-common.md#oncreatemenu12)的入参列表中不包含被屏蔽的菜单选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](ts-text-common.md#editmenuoptions) | 是 | 扩展菜单选项。 |

### enablePreviewText12+

PhonePC/2in1TabletTVWearable

enablePreviewText(enable: boolean)

设置是否开启输入预上屏。

预上屏内容定义为文字暂存态，目前不支持文字拦截功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否开启输入预上屏。  true表示开启输入预上屏，false表示不开启输入预上屏。  默认值：true |

说明

“预上屏”描述的是一种文字暂存状态。需要在输入法中开启预上屏功能，在输入文本过程中，未确认输入候选词时，文本框中显示标记文本。例如，通过拼音输入中文时，未确定候选词之前，在输入框中显示拼音字母，该状态称为文字预上屏。

### enableHapticFeedback13+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(isEnabled: boolean)

设置是否开启触控反馈。

开启触控反馈时，需要在工程的[module.json5](../harmonyos-guides/module-configuration-file.md)中配置requestPermissions字段以开启振动权限，配置如下：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.VIBRATE",
4. }
5. ]
```

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否开启触控反馈。  true表示开启触控反馈，false表示不开启触控反馈。  默认值：true |

### autoCapitalizationMode20+

PhonePC/2in1TabletTVWearable

autoCapitalizationMode(mode: AutoCapitalizationMode)

设置自动大小写模式的文本模式，只提供接口能力，具体实现以输入法应用为主。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AutoCapitalizationMode](ts-text-common.md#autocapitalizationmode20枚举说明) | 是 | 自动大小写模式，默认状态无效。 |

### keyboardAppearance15+

PhonePC/2in1TabletTVWearable

keyboardAppearance(appearance: Optional<KeyboardAppearance>)

设置输入框拉起的键盘样式，需要输入法适配后生效。具体参考[输入法应用沉浸模式](../harmonyos-guides/inputmethod-immersive-mode-guide.md)。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appearance | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[KeyboardAppearance](ts-text-common.md#keyboardappearance15枚举说明)> | 是 | 键盘样式。  默认值：KeyboardAppearance.NONE\_IMMERSIVE |

### strokeWidth20+

PhonePC/2in1TabletTVWearable

strokeWidth(width: Optional<LengthMetrics>)

设置文本描边的宽度。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 是 | 文本描边的宽度。当LengthMetrics的单位为px时，  若设置值小于0，显示实心字；若大于0，显示空心字。  默认值为0，不做描边处理。 |

### strokeColor20+

PhonePC/2in1TabletTVWearable

strokeColor(color: Optional<ResourceColor>)

设置文本描边的颜色。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 描边颜色。默认值为字体颜色，设置异常值时取默认值。 |

### stopBackPress15+

PhonePC/2in1TabletTVWearable

stopBackPress(isStopped: Optional<boolean>)

设置是否阻止返回键传递。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isStopped | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否阻止返回键。  true表示阻止，false表示不阻止。  默认值：true。异常值取默认值。 |

### halfLeading18+

PhonePC/2in1TabletTVWearable

halfLeading(halfLeading: Optional<boolean>)

设置文本在行内垂直居中，将行间距平分至行的顶部与底部。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| halfLeading | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置文本是否垂直居中。  true表示将行间距平分至行的顶部与底部，false则不平分。  默认值：false |

### minFontScale18+

PhonePC/2in1TabletTVWearable

minFontScale(scale: Optional<number | Resource>)

设置文本最小的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | 文本最小的字体缩放倍数，支持undefined类型。  取值范围：[0, 1]  **说明：**  设置的值小于0时，按值为0处理。设置的值大于1，按值为1处理。异常值默认不生效。  使用前需在工程中配置[configuration.json](../harmonyos-guides/app-configuration-file.md#configuration标签)文件和[app.json5](../harmonyos-guides/app-configuration-file.md)文件，具体详见[示例18设置最小字体范围与最大字体范围](ts-basic-components-textinput.md#示例18设置最小字体范围与最大字体范围)。 |

### maxFontScale18+

PhonePC/2in1TabletTVWearable

maxFontScale(scale: Optional<number | Resource>)

设置文本最大的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | 文本最大的字体缩放倍数，支持undefined类型。  取值范围：[1, +∞)  **说明：**  设置的值小于1时，按值为1处理。异常值默认不生效。  当设置maxFontScale属性后，showError最多放大到2倍。  使用前需在工程中配置[configuration.json](../harmonyos-guides/app-configuration-file.md#configuration标签)文件和[app.json5](../harmonyos-guides/app-configuration-file.md)文件，具体详见[示例18设置最小字体范围与最大字体范围](ts-basic-components-textinput.md#示例18设置最小字体范围与最大字体范围)。 |

### cancelButton18+

PhonePC/2in1TabletTVWearable

cancelButton(symbolOptions: CancelButtonSymbolOptions)

设置右侧清除按钮样式，仅支持symbol图标。不支持[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)。示例请参考[示例15（设置symbol类型清除按钮）](ts-basic-components-textinput.md#示例15设置symbol类型清除按钮)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbolOptions | [CancelButtonSymbolOptions](ts-basic-components-search.md#cancelbuttonsymboloptions12对象说明) | 是 | 右侧清除按钮样式。  默认值：  {  style: CancelButtonStyle.INPUT  } |

### ellipsisMode18+

PhonePC/2in1TabletTVWearable

ellipsisMode(mode: Optional<EllipsisMode>)

设置省略位置。ellipsisMode属性仅在[内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)下生效，需要配合overflow设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。

非编辑态时正常生效，编辑态时EllipsisMode.START和EllipsisMode.CENTER仅在maxLines设置为1时生效，EllipsisMode.END正常生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[EllipsisMode](ts-appendix-enums.md#ellipsismode11)> | 是 | 省略位置。  默认值：EllipsisMode.END |

### enableAutoFillAnimation20+

PhonePC/2in1TabletTVWearable

enableAutoFillAnimation(enabled: Optional<boolean>)

设置是否启用自动填充动效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否启用自动填充动效。  true表示启用，false表示不启用。  默认值：true  **说明：**  启用之后，仅输入模式[InputType](ts-basic-components-textinput.md#inputtype枚举说明)设置为Password、NEW\_PASSWORD或NUMBER\_PASSWORD的输入框在进行自动填充时动效可生效。 |

### enableAutoSpacing20+

PhonePC/2in1TabletTVWearable

enableAutoSpacing(enabled: Optional<boolean>)

设置是否开启中文与西文的自动间距。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启中文与西文的自动间距。  true为开启自动间距，false为不开启。  默认值：false |

### compressLeadingPunctuation23+

PhonePC/2in1TabletTVWearable

compressLeadingPunctuation(enabled: Optional<boolean>)

设置是否开启行首标点符号压缩。

说明

* 行首标点符号默认不压缩。
* 支持压缩的标点符号，请参考[ParagraphStyle](js-apis-graphics-text.md#paragraphstyle)的行首压缩的标点范围。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启行首标点符号压缩。  true表示开启行首标点符号压缩；false表示不开启行首标点符号压缩。 |

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

针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。不通过该接口设置，默认行高不基于文字实际高度自适应。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 行高是否基于文字实际高度自适应。  true表示行高基于文字实际高度自适应；false表示行高不基于文字实际高度自适应。 |

### selectedDragPreviewStyle23+

PhonePC/2in1TabletTVWearable

selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)

设置文本输入框内文本拖拽时的背板样式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SelectedDragPreviewStyle](ts-text-common.md#selecteddragpreviewstyle23对象说明) | undefined | 是 | 文本拖拽时的背板样式。  设置为undefined时：背板颜色跟随主题，浅色模式显示白色，深色模式显示黑色。 |

## InputType枚举说明

PhonePC/2in1TabletTVWearable

单行文本输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Normal | 0 | 基本输入模式，无特殊限制。  内联输入风格只支持InputType.Normal类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Number | 2 | 纯数字输入模式。  不支持负数、小数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PhoneNumber9+ | 3 | 电话号码输入模式。  支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Email | 5 | 邮箱地址输入模式。  支持数字、字母、下划线、小数点、!、#、$、%、&、'、"、\*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Password | 7 | 密码输入模式。  默认输入文字短暂显示后变成圆点。从API version 12开始，PC/2in1设备上输入文字直接显示为圆点。  TV设备上输入框末尾默认不显示小眼睛图标，其他设备输入框末尾默认显示小眼睛图标。  密码输入模式中，[decoration](ts-basic-components-textinput.md#decoration12)、[showUnderline](ts-basic-components-textinput.md#showunderline10)、[lineHeight](ts-basic-components-textinput.md#lineheight12)不生效。  在已启用密码保险箱的情况下，支持用户名、密码的自动保存和自动填充。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NUMBER\_PASSWORD11+ | 8 | 纯数字密码输入模式。  默认输入文字短暂显示后变成圆点。从API version 12开始，PC/2in1设备上输入文字直接显示为圆点。  TV设备上输入框末尾默认不显示小眼睛图标，其他设备输入框末尾默认显示小眼睛图标。  密码输入模式不支持下划线样式。在已启用密码保险箱的情况下，支持用户名、密码的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| USER\_NAME11+ | 10 | 用户名输入模式，无特殊限制。  在已启用密码保险箱的情况下，支持用户名、密码的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NEW\_PASSWORD11+ | 11 | 新密码输入模式，无特殊限制。  默认输入文字短暂显示后变成圆点。从API version 12开始，PC/2in1设备上输入文字直接显示为圆点。  TV设备上输入框末尾默认不显示小眼睛图标，其他设备输入框末尾默认显示小眼睛图标。  在已启用密码保险箱的情况下，支持自动生成新密码。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NUMBER\_DECIMAL11+ | 12 | 带小数点的数字输入模式。  支持数字，小数点（只能存在一个小数点）。不支持负数小数，负数小数的数字输入模式请使用inputFilter实现。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| URL12+ | 13 | 带URL的输入模式，无特殊限制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ONE\_TIME\_CODE20+ | 14 | 验证码输入模式，无特殊限制。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ContentType12+枚举说明

PhonePC/2in1TabletTVWearable

自动填充类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_NAME | 0 | 【用户名】在已启用密码保险箱的情况下，支持用户名的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PASSWORD | 1 | 【密码】在已启用密码保险箱的情况下，支持密码的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NEW\_PASSWORD | 2 | 【新密码】在已启用密码保险箱的情况下，支持自动生成新密码。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FULL\_STREET\_ADDRESS | 3 | 【详细地址】在已启用情景化自动填充的情况下，支持详细地址的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| HOUSE\_NUMBER | 4 | 【门牌号】在已启用情景化自动填充的情况下，支持门牌号的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DISTRICT\_ADDRESS | 5 | 【区/县】在已启用情景化自动填充的情况下，支持区/县的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CITY\_ADDRESS | 6 | 【市】在已启用情景化自动填充的情况下，支持市的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PROVINCE\_ADDRESS | 7 | 【省】在已启用情景化自动填充的情况下，支持省的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COUNTRY\_ADDRESS | 8 | 【国家】在已启用情景化自动填充的情况下，支持国家的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PERSON\_FULL\_NAME | 9 | 【姓名】在已启用情景化自动填充的情况下，支持姓名的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PERSON\_LAST\_NAME | 10 | 【姓氏】在已启用情景化自动填充的情况下，支持姓氏的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PERSON\_FIRST\_NAME | 11 | 【名字】在已启用情景化自动填充的情况下，支持名字的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PHONE\_NUMBER | 12 | 【手机号码】在已启用情景化自动填充的情况下，支持手机号码的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PHONE\_COUNTRY\_CODE | 13 | 【国家代码】在已启用情景化自动填充的情况下，支持国家代码的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FULL\_PHONE\_NUMBER | 14 | 【包含国家代码的手机号码】在已启用情景化自动填充的情况下，支持包含国家代码的手机号码的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| EMAIL\_ADDRESS | 15 | 【邮箱地址】在已启用情景化自动填充的情况下，支持邮箱地址的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BANK\_CARD\_NUMBER | 16 | 【银行卡号】在已启用情景化自动填充的情况下，支持银行卡号的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ID\_CARD\_NUMBER | 17 | 【身份证号】在已启用情景化自动填充的情况下，支持身份证号的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NICKNAME | 23 | 【昵称】在已启用情景化自动填充的情况下，支持昵称的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DETAIL\_INFO\_WITHOUT\_STREET | 24 | 【无街道地址】在已启用情景化自动填充的情况下，支持无街道地址的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FORMAT\_ADDRESS | 25 | 【标准地址】在已启用情景化自动填充的情况下，支持标准地址的自动保存和自动填充。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PASSPORT\_NUMBER18+ | 26 | 【护照号】在已启用情景化自动填充的情况下，支持护照号的自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| VALIDITY18+ | 27 | 【护照有效期】在已启用情景化自动填充的情况下，支持护照有效期的自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| ISSUE\_AT18+ | 28 | 【护照签发地】在已启用情景化自动填充的情况下，支持护照签发地的自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| ORGANIZATION18+ | 29 | 【发票抬头名称】在已启用情景化自动填充的情况下，支持发票抬头名称的自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| TAX\_ID18+ | 30 | 【税号】在已启用情景化自动填充的情况下，支持税号的自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| ADDRESS\_CITY\_AND\_STATE18+ | 31 | 【所在地区】在已启用情景化自动填充的情况下，支持所在地区的自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| FLIGHT\_NUMBER18+ | 32 | 【航班号】暂不支持自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| LICENSE\_NUMBER18+ | 33 | 【驾驶证号】暂不支持自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| LICENSE\_FILE\_NUMBER18+ | 34 | 【驾驶证档案编号】暂不支持自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| LICENSE\_PLATE18+ | 35 | 【车牌号】在已启用情景化自动填充的情况下，支持车牌号的自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| ENGINE\_NUMBER18+ | 36 | 【行驶证发动机号】暂不支持自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| LICENSE\_CHASSIS\_NUMBER18+ | 37 | 【车牌识别号】暂不支持自动保存和自动填充。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## TextInputStyle9+枚举说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| Default | 默认风格，光标宽1.5vp，光标高度与文本选中底板高度和字体大小相关。 |
| Inline | 内联输入风格。文本选中底板高度与输入框高度相同。  内联输入是在有明显的编辑态/非编辑态的区分场景下使用，例如：文件列表视图中的重命名。  不支持showError属性。  [内联模式](../harmonyos-guides/arkts-common-components-text-input.md#内联模式)下，不支持拖入文本。 |

## PasswordIcon10+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onIconSrc | string | [Resource](ts-types.md#resource) | 否 | 是 | 密码输入模式时，能够切换密码可见时显示的图标。  string格式可用于加载网络图片和本地图片。 |
| offIconSrc | string | [Resource](ts-types.md#resource) | 否 | 是 | 密码输入模式时，能够切换密码不可见时显示的图标。  string格式可用于加载网络图片和本地图片。 |

## EnterKeyType枚举说明

PhonePC/2in1TabletTVWearable

输入法回车键类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Go | 2 | 显示为开始样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Search | 3 | 显示为搜索样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Send | 4 | 显示为发送样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Next | 5 | 显示为下一步样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Done | 6 | 显示为完成样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PREVIOUS11+ | 7 | 显示为上一步样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NEW\_LINE11+ | 8 | 显示为换行样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: EditableTextOnChangeCallback)

输入内容发生变化时，触发该回调。

在本回调中，若执行了光标操作，需要开发者在预上屏场景下依据previewText参数调整光标逻辑，以适应预上屏场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [EditableTextOnChangeCallback](ts-text-common.md#editabletextonchangecallback12) | 是 | 当前输入文本内容变化时的回调。 |

### onSubmit

PhonePC/2in1TabletTVWearable

onSubmit(callback: OnSubmitCallback)

按下输入法回车键触发该回调。

非TV设备按下回车键时输入框默认会失焦且收起键盘，可在OnSubmitCallback回调中配置是否收起键盘，参考[示例2（设置下划线）](ts-basic-components-textinput.md#示例2设置下划线)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSubmitCallback](ts-basic-components-textinput.md#onsubmitcallback18) | 是 | 提交回调。 |

### onEditChanged(deprecated)

PhonePC/2in1TabletTVWearable

onEditChanged(callback: (isEditing: boolean) => void)

输入状态变化时，触发该回调。

说明

从API version 7开始支持，从API version 8开始废弃，建议使用[onEditChange](ts-basic-components-textinput.md#oneditchange8)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEditing | boolean | 是 | 当前是否正在输入中。  true表示正在输入；false表示当前没有输入。 |

### onEditChange8+

PhonePC/2in1TabletTVWearable

onEditChange(callback: Callback<boolean>)

输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 输入状态变化回调，返回值为true表示输入框处于编辑态，返回值为false表示输入框处于非编辑态。 |

### onCopy8+

PhonePC/2in1TabletTVWearable

onCopy(callback: Callback<string>)

进行复制操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<string> | 是 | 复制回调，其返回值为复制的文本内容。 |

### onCut8+

PhonePC/2in1TabletTVWearable

onCut(callback: Callback<string>)

进行剪切操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<string> | 是 | 剪切回调，其返回值为剪切的文本内容。 |

### onPaste8+

PhonePC/2in1TabletTVWearable

onPaste(callback: OnPasteCallback)

进行粘贴操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnPasteCallback](ts-basic-components-textinput.md#onpastecallback18) | 是 | 粘贴回调。 |

### onTextSelectionChange10+

PhonePC/2in1TabletTVWearable

onTextSelectionChange(callback: OnTextSelectionChangeCallback)

文本选择的位置或编辑状态下光标位置发生变化时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnTextSelectionChangeCallback](ts-basic-components-textinput.md#ontextselectionchangecallback18) | 是 | 文本选择变化回调或光标位置变化回调。 |

### onContentScroll10+

PhonePC/2in1TabletTVWearable

onContentScroll(callback: OnContentScrollCallback)

文本内容滚动时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnContentScrollCallback](ts-basic-components-textinput.md#oncontentscrollcallback18) | 是 | 文本内容滚动回调。 |

### onSecurityStateChange12+

PhonePC/2in1TabletTVWearable

onSecurityStateChange(callback: Callback<boolean>)

密码显隐状态切换时，触发该回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。  true表示状态切换；false表示状态未切换。 |

### onWillInsert12+

PhonePC/2in1TabletTVWearable

onWillInsert(callback: Callback<InsertValue, boolean>)

在将要输入时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[InsertValue](ts-text-common.md#insertvalue12对象说明), boolean> | 是 | 在将要输入时调用的回调。  在返回true时，表示正常插入，返回false时，表示不插入。  在预上屏和候选词操作时，该回调不触发。  仅支持系统输入法输入的场景。 |

### onDidInsert12+

PhonePC/2in1TabletTVWearable

onDidInsert(callback: Callback<InsertValue>)

在输入完成时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[InsertValue](ts-text-common.md#insertvalue12对象说明)> | 是 | 在输入完成时调用的回调。  仅支持系统输入法输入的场景。 |

### onWillDelete12+

PhonePC/2in1TabletTVWearable

onWillDelete(callback: Callback<DeleteValue, boolean>)

在将要删除时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DeleteValue](ts-text-common.md#deletevalue12对象说明), boolean> | 是 | 在将要删除时调用的回调。  在返回true时，表示正常删除，返回false时，表示不删除。  在预上屏删除操作时，该回调不触发。  仅支持系统输入法输入的场景。 |

### onDidDelete12+

PhonePC/2in1TabletTVWearable

onDidDelete(callback: Callback<DeleteValue>)

在删除完成时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DeleteValue](ts-text-common.md#deletevalue12对象说明)> | 是 | 在删除完成时调用的回调。  仅支持系统输入法输入的场景。 |

说明

点击清除按钮不触发onDidDelete回调。

### onWillChange15+

PhonePC/2in1TabletTVWearable

onWillChange(callback: Callback<EditableTextChangeValue, boolean>)

在文本内容将要发生变化时，触发该回调。

onWillChange的回调时序晚于onWillInsert、onWillDelete，早于onDidInsert、onDidDelete。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[EditableTextChangeValue](ts-text-common.md#editabletextchangevalue15), boolean> | 是 | 在文本内容将要发生变化时的回调。  返回true时，表示正常修改。返回false时，表示拦截此次触发。 |

### onWillAttachIME20+

PhonePC/2in1TabletTVWearable

onWillAttachIME(callback: Callback<IMEClient>)

在输入框将要绑定输入法前触发该回调。

从API version 22开始，调用[IMEClient](ts-text-common.md#imeclient20对象说明)的[setExtraConfig](ts-text-common.md#setextraconfig22)方法可以设置输入法扩展信息。在绑定输入法成功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。

IMEClient仅在onWillAttachIME执行期间有效，不可进行异步调用。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IMEClient](ts-text-common.md#imeclient20对象说明)> | 是 | 在输入框将要绑定输入法前触发该回调。 |

## TextInputController8+

PhonePC/2in1TabletTVWearable

TextInput组件的控制器继承自[TextContentControllerBase](ts-universal-attributes-text-style.md#textcontentcontrollerbase)，涉及的接口有[getTextContentRect](ts-universal-attributes-text-style.md#gettextcontentrect)、[getTextContentLineCount](ts-universal-attributes-text-style.md#gettextcontentlinecount)、[getCaretOffset](ts-universal-attributes-text-style.md#getcaretoffset11)、[addText](ts-universal-attributes-text-style.md#addtext15)、[deleteText](ts-universal-attributes-text-style.md#deletetext15)、[getSelection](ts-universal-attributes-text-style.md#getselection15)、[clearPreviewText](ts-universal-attributes-text-style.md#clearpreviewtext17)、[setStyledPlaceholder](ts-universal-attributes-text-style.md#setstyledplaceholder22)、[deleteBackward](ts-universal-attributes-text-style.md#deletebackward23)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 导入对象

```
1. controller: TextInputController = new TextInputController();
```

### constructor8+

PhonePC/2in1TabletTVWearable

constructor()

TextInputController的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### caretPosition8+

PhonePC/2in1TabletTVWearable

caretPosition(value: number): void

设置输入光标的位置。当取值小于0时，取0，大于文本长度时，显示在文本末尾。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 从字符串开始到光标所在位置的字符长度。 |

### setTextSelection10+

PhonePC/2in1TabletTVWearable

setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

设置文本选择区域并高亮显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 文本选择区域起始位置，文本框中文字的起始位置为0。 |
| selectionEnd | number | 是 | 文本选择区域结束位置。当selectionEnd<0时，按照0处理；当selectionEnd大于文本长度时，按照文本长度处理。 |
| options12+ | [SelectionOptions](ts-universal-attributes-text-style.md#selectionoptions12对象说明) | 否 | 选中文字时的配置。  默认值：MenuPolicy.DEFAULT  从API version 12开始，该接口中的options参数支持在元服务中使用。 |

说明

如果selectionStart或selectionEnd被赋值为undefined时，当作0处理。

如果selectionMenuHidden被赋值为true或设备为2in1时，即使options被赋值为MenuPolicy.SHOW，调用setTextSelection也不弹出菜单。

如果emoji表情被选中区域截断时，表情的起始位置包含在设置的文本选中区域内就会被选中。

### stopEditing10+

PhonePC/2in1TabletTVWearable

stopEditing(): void

退出编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## UnderlineColor12+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| typing | [ResourceColor](ts-types.md#resourcecolor) | undefined | 否 | 是 | 键入时下划线颜色。不填写、undefined、null、无效值时恢复默认。 |
| normal | [ResourceColor](ts-types.md#resourcecolor) | undefined | 否 | 是 | 非特殊状态时下划线颜色。不填写、undefined、null、无效值时恢复默认。 |
| error | [ResourceColor](ts-types.md#resourcecolor) | undefined | 否 | 是 | 错误时下划线颜色。不填写、undefined、null、无效值时恢复默认。此选项会修改showCounter属性中达到最大字符数时的颜色。 |
| disable | [ResourceColor](ts-types.md#resourcecolor) | undefined | 否 | 是 | 禁用时下划线颜色。不填写、undefined、null、无效值时恢复默认。 |

## SubmitEvent11+

PhonePC/2in1TabletTVWearable

定义用户提交事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 输入框文本内容。 |

### keepEditableState11+

PhonePC/2in1TabletTVWearable

keepEditableState(): void

用户自定义输入框编辑状态，调用时保持编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## OnPasteCallback18+

PhonePC/2in1TabletTVWearable

type OnPasteCallback = (content: string, event: PasteEvent) => void

粘贴回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 粘贴的文本内容。 |
| event | [PasteEvent](ts-basic-components-richeditor.md#pasteevent11) | 是 | 用户自定义的粘贴事件。 |

## OnSubmitCallback18+

PhonePC/2in1TabletTVWearable

type OnSubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void

提交回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterKey | [EnterKeyType](ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 输入法回车键类型。 |
| event | [SubmitEvent](ts-basic-components-textinput.md#submitevent11) | 是 | 提交事件。可以控制是否收起键盘。 |

## OnTextSelectionChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void

文本选择变化回调或光标位置变化回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 所选文本的起始位置，文字的起始位置为0。 |
| selectionEnd | number | 是 | 所选文本的结束位置。 |

## OnContentScrollCallback18+

PhonePC/2in1TabletTVWearable

type OnContentScrollCallback = (totalOffsetX: number, totalOffsetY: number) => void

文本内容滚动回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| totalOffsetX | number | 是 | 文本在内容区的横坐标偏移，单位px。 |
| totalOffsetY | number | 是 | 文本在内容区的纵坐标偏移，单位px。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置与获取光标位置）

从API version 8开始，该示例通过[controller](ts-basic-components-textinput.md#textinputcontroller8)实现了光标位置的设置与获取的功能，同时，可以使用!!实现text参数的双向数据绑定（从API version 18开始）。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = '';
6. // index：光标所在位置的索引值
7. // x：光标相对输入框的x坐标位值，单位px
8. // y：光标相对输入框的y坐标位值，单位px
9. @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 };
10. @State passwordState: boolean = false;
11. controller: TextInputController = new TextInputController();

13. build() {
14. Column() {
15. TextInput({ text: this.text!!, placeholder: 'input your word...', controller: this.controller })
16. .placeholderColor(Color.Grey)
17. .placeholderFont({ size: 14, weight: 400 })
18. .caretColor(Color.Blue)
19. .width('95%')
20. .height(40)
21. .margin(20)
22. .fontSize(14)
23. .fontColor(Color.Black)
24. .inputFilter('[a-z]', (e) => {
25. console.info(JSON.stringify(e));
26. })
27. Text(this.text)
28. Button('Set caretPosition 1')
29. .margin(15)
30. .onClick(() => {
31. // 将光标移动至第一个字符后
32. this.controller.caretPosition(1);
33. })
34. Button('Get CaretOffset')
35. .margin(15)
36. .onClick(() => {
37. // 获取光标相对输入框的位置
38. this.positionInfo = this.controller.getCaretOffset();
39. })
40. // 密码输入框
41. TextInput({ placeholder: 'input your password...' })
42. .width('95%')
43. .height(40)
44. .margin(20)
45. .type(InputType.Password)
46. .maxLength(9)
47. .showPasswordIcon(true)
48. .showPassword(this.passwordState)
49. .onSecurityStateChange(((isShowPassword: boolean) => {
50. // 更新密码显示状态
51. console.info('isShowPassword', isShowPassword);
52. this.passwordState = isShowPassword;
53. }))
54. // 邮箱地址自动填充类型
55. TextInput({ placeholder: 'input your email...' })
56. .width('95%')
57. .height(40)
58. .margin(20)
59. .contentType(ContentType.EMAIL_ADDRESS)
60. .maxLength(9)
61. // 内联风格输入框
62. TextInput({ text: 'inline style' })
63. .width('95%')
64. .height(50)
65. .margin(20)
66. .borderRadius(0)
67. .style(TextInputStyle.Inline)
68. }.width('100%')
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/UqxC72iwTqqPW60yYv8l3g/zh-cn_image_0000002583439807.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=3DC730D33F3473BA1ABE99DB87BB856B34A7BFFA9590410E72B3E8C4360F5606)

### 示例2（设置下划线）

从API version 10开始支持，该示例通过[showUnderline](ts-basic-components-textinput.md#showunderline10)、[showError](ts-basic-components-textinput.md#showerror10)、[showUnit](ts-basic-components-textinput.md#showunit10)、[passwordIcon](ts-basic-components-textinput.md#passwordicon10)属性展示了下划线在不同场景的效果，同时，可以通过[underlineColor](ts-basic-components-textinput.md#underlinecolor12)（从API version 12开始）支持配置下划线颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. // $r('app.media.ImageOne')需要替换为开发者所需的图像资源文件。
6. @State passWordSrc1: Resource = $r('app.media.ImageOne');
7. // $r('app.media.ImageTwo')需要替换为开发者所需的图像资源文件。
8. @State passWordSrc2: Resource = $r('app.media.ImageTwo');
9. @State textError: string = '';
10. @State text: string = '';
11. @State nameText: string = 'test';

13. @Builder
14. itemEnd() {
15. Select([{ value: 'KB' },
16. { value: 'MB' },
17. { value: 'GB' },
18. { value: 'TB', }])
19. .height("48vp")
20. .borderRadius(0)
21. .selected(2)
22. .align(Alignment.Center)
23. .value('MB')
24. .font({ size: 20, weight: 500 })
25. .fontColor('#182431')
26. .selectedOptionFont({ size: 20, weight: 400 })
27. .optionFont({ size: 20, weight: 400 })
28. .backgroundColor(Color.Transparent)
29. .responseRegion({
30. height: "40vp",
31. width: "80%",
32. x: '10%',
33. y: '6vp'
34. })
35. .onSelect((index: number) => {
36. console.info('Select:' + index);
37. })
38. }

40. build() {
41. Column({ space: 20 }) {
42. // 自定义密码显示图标
43. TextInput({ placeholder: 'user define password icon' })
44. .type(InputType.Password)
45. .width(350)
46. .height(60)
47. .passwordIcon({ onIconSrc: this.passWordSrc1, offIconSrc: this.passWordSrc2 })
48. // 下划线模式
49. TextInput({ placeholder: 'underline style' })
50. .showUnderline(true)
51. .width(350)
52. .height(60)
53. .showError('Error')
54. .showUnit(this.itemEnd)

56. Text(`用户名：${this.text}`)
57. .width(350)
58. TextInput({ placeholder: '请输入用户名', text: this.text })
59. .showUnderline(true)
60. .width(350)
61. .showError(this.textError)
62. .onChange((value: string) => {
63. this.text = value;
64. })
65. .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
66. // 用户名不正确会清空输入框和用户名并提示错误文本
67. if (this.text == this.nameText) {
68. this.textError = '';
69. } else {
70. this.textError = '用户名输入错误';
71. this.text = '';
72. // 调用keepEditableState方法，输入框保持编辑态
73. event.keepEditableState();
74. }
75. })
76. // 设置下划线颜色
77. TextInput({ placeholder: '提示文本内容' })
78. .width(350)
79. .showUnderline(true)
80. .underlineColor({
81. normal: Color.Orange,
82. typing: Color.Green,
83. error: Color.Red,
84. disable: Color.Gray
85. })
86. TextInput({ placeholder: '提示文本内容' })
87. .width(350)
88. .showUnderline(true)
89. .underlineColor(Color.Gray);

91. }.width('100%').margin({ top: 10 })
92. }
93. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/FhD_iT-2R7-WUVw9ltD98Q/zh-cn_image_0000002552959762.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=5049D013862FF283BCEA04163AAF5A5ADA13B6AD49FB4ACF56684D4B86DD5429)

### 示例3（设置自定义键盘）

该示例通过[customKeyboard](ts-basic-components-textinput.md#customkeyboard10)（从API version 10开始）属性分别将value中的入参类型设置为[CustomBuilder](ts-types.md#custombuilder8)和[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)，实现了自定义键盘的功能。

从API version 22开始[customKeyboard](ts-basic-components-textinput.md#customkeyboard10)属性新增了入参类型[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';
3. class BuilderParams {
4. inputValue: string;
5. controller: TextInputController;

7. constructor(inputValue: string, controller: TextInputController) {
8. this.inputValue = inputValue;
9. this.controller = controller;
10. }
11. }
12. @Builder
13. function CustomKeyboardBuilder(builderParams: BuilderParams) {
14. Column() {
15. Row() {
16. Button('x').onClick(() => {
17. // 关闭自定义键盘
18. builderParams.controller.stopEditing();
19. }).margin(10)
20. }

22. Grid() {
23. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
24. GridItem() {
25. Button(item + "")
26. .width(110).onClick(() => {
27. builderParams.inputValue += item;
28. })
29. }
30. })
31. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
32. }.backgroundColor(Color.Gray)
33. }
34. @Entry
35. @Component
36. struct TextInputExample {
37. controller: TextInputController = new TextInputController();
38. @State inputValue: string = "";
39. @State componentContent ?: ComponentContent<BuilderParams> = undefined;
40. @State builderParam: BuilderParams = new BuilderParams(this.inputValue, this.controller);
41. @State supportAvoidance: boolean = true;

43. aboutToAppear(): void {
44. // 创建ComponentContent
45. this.componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(CustomKeyboardBuilder), this.builderParam);
46. }
47. build(){
48. Column() {
49. Text('Builder').margin(10).border({ width: 1 })
50. TextInput({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
51. .customKeyboard(this.componentContent, { supportAvoidance: this.supportAvoidance })
52. .margin(10).border({ width: 1 }).height('48vp')

54. Text('ComponentContent').margin(10).border({ width: 1 })
55. TextInput({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
56. .customKeyboard(CustomKeyboardBuilder(this.builderParam), { supportAvoidance: this.supportAvoidance })
57. .margin(10).border({ width: 1 }).height('48vp')
58. }
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/m59N5qaCQuurTs-L3z4jjA/zh-cn_image_0000002583479763.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=8D8AB7DB95D65DF08BC151BC06A38480598DA3F59A2C89411D35A36487C7B236)

### 示例4（设置右侧清除按钮样式）

该示例通过[cancelButton](ts-basic-components-textinput.md#cancelbutton11)属性展示了自定义右侧清除按钮样式的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = '';
6. controller: TextInputController = new TextInputController();

8. build() {
9. Column() {
10. TextInput({ placeholder: 'input ...', controller: this.controller })
11. .width(380)
12. .height(60)
13. .cancelButton({
14. style: CancelButtonStyle.CONSTANT,
15. icon: {
16. size: 45,
17. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
18. src: $r('app.media.startIcon'),
19. color: Color.Blue
20. }
21. })
22. .onChange((value: string) => {
23. this.text = value;
24. })
25. }
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/dsSTuOemQ1ac9vJGbswKqA/zh-cn_image_0000002552800114.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=455CBB4AC2487025AAD46F46CB8D612901254575452CC5A3778E41DF5FBC55FF)

### 示例5（设置计数器）

该示例通过[maxLength](ts-basic-components-textinput.md#maxlength)、[showCounter](ts-basic-components-textinput.md#showcounter11)（从API version 11开始）、[showUnderline](ts-basic-components-textinput.md#showunderline10)（从API version 10开始）属性实现了计数器的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = '';
6. controller: TextInputController = new TextInputController();

8. build() {
9. Column() {
10. TextInput({ text: this.text, controller: this.controller })
11. .placeholderFont({ size: 16, weight: 400 })
12. .width(336)
13. .height(56)
14. .maxLength(6)
15. .showUnderline(true)
16. .showCounter(true,
17. { thresholdPercentage: 50, highlightBorder: true })// 计数器显示效果为用户当前输入字符数/最大字符限制数。最大字符限制数通过maxLength()接口设置。
18. // 如果用户当前输入字符数达到最大字符限制乘50%（thresholdPercentage）。字符计数器显示。
19. // 用户设置highlightBorder为false时，配置取消红色边框。不设置此参数时，默认为true。
20. .onChange((value: string) => {
21. this.text = value;
22. })
23. }.width('100%').height('100%').backgroundColor('#F1F3F5')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/gU7ud5eySxGA38AphNt8nw/zh-cn_image_0000002583439809.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=622374F32C5187FA0BEF08817E5C9B2483A277D643F6EE13607BD8D252DE2E15)

### 示例6（电话号码格式化）

该示例通过[onChange](ts-basic-components-textinput.md#onchange)回调实现了电话号码格式化为XXX XXXX XXXX的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State submitValue: string = '';
6. @State text: string = '';
7. public readonly NUM_TEXT_MAXSIZE_LENGTH = 13;
8. @State telNumberNoSpace: string = "";
9. @State nextCaret: number = -1; // 用于记录下次光标设置的位置
10. @State actualCh: number = -1; // 用于记录光标在第i个数字后插入或者第i个数字前删除
11. @State lastCaretPosition: number = 0;
12. @State lastCaretPositionEnd: number = 0;
13. controller: TextInputController = new TextInputController();

15. isEmpty(str?: string): boolean {
16. return str == 'undefined' || !str || !new RegExp("[^\\s]").test(str);
17. }

19. checkNeedNumberSpace(numText: string) {
20. let isSpace: RegExp = new RegExp('[\\+;,#\\*]', 'g');
21. let isRule: RegExp = new RegExp('^\\+.*');

23. if (isSpace.test(numText)) {
24. // 如果电话号码里有特殊字符，就不加空格
25. if (isRule.test(numText)) {
26. return true;
27. } else {
28. return false;
29. }
30. }
31. return true;
32. }

34. removeSpace(str: string): string {
35. if (this.isEmpty(str)) {
36. return '';
37. }
38. return str.replace(new RegExp("[\\s]", "g"), '');
39. }

41. setCaret() {
42. if (this.nextCaret != -1) {
43. console.info("to keep caret position right, change caret to", this.nextCaret);
44. this.controller.caretPosition(this.nextCaret);
45. this.nextCaret = -1;
46. }
47. }

49. calcCaretPosition(nextText: string) {
50. let befNumberNoSpace: string = this.removeSpace(this.text);
51. this.actualCh = 0;
52. if (befNumberNoSpace.length < this.telNumberNoSpace.length) { // 插入场景
53. for (let i = 0; i < this.lastCaretPosition; i++) {
54. if (this.text[i] != ' ') {
55. this.actualCh += 1;
56. }
57. }
58. this.actualCh += this.telNumberNoSpace.length - befNumberNoSpace.length;
59. console.info("actualCh: " + this.actualCh);
60. for (let i = 0; i < nextText.length; i++) {
61. if (nextText[i] != ' ') {
62. this.actualCh -= 1;
63. if (this.actualCh <= 0) {
64. this.nextCaret = i + 1;
65. break;
66. }
67. }
68. }
69. } else if (befNumberNoSpace.length > this.telNumberNoSpace.length) { // 删除场景
70. if (this.lastCaretPosition === this.text.length) {
71. console.info("Caret at last, no need to change");
72. } else if (this.lastCaretPosition === this.lastCaretPositionEnd) {
73. // 按键盘上回退键一个一个删的情况
74. for (let i = this.lastCaretPosition; i < this.text.length; i++) {
75. if (this.text[i] != ' ') {
76. this.actualCh += 1;
77. }
78. }
79. for (let i = nextText.length - 1; i >= 0; i--) {
80. if (nextText[i] != ' ') {
81. this.actualCh -= 1;
82. if (this.actualCh <= 0) {
83. this.nextCaret = i;
84. break;
85. }
86. }
87. }
88. } else {
89. // 剪切/手柄选择 一次删多个字符
90. this.nextCaret = this.lastCaretPosition; // 保持光标位置
91. }
92. }
93. }

95. build() {
96. Column() {
97. Row() {
98. TextInput({ text: `${this.text}`, controller: this.controller }).type(InputType.PhoneNumber).height('48vp')
99. .onChange((value: string) => {
100. this.telNumberNoSpace = this.removeSpace(value);
101. let nextText: string = "";
102. if (this.telNumberNoSpace.length > this.NUM_TEXT_MAXSIZE_LENGTH - 2) {
103. nextText = this.telNumberNoSpace;
104. } else if (this.checkNeedNumberSpace(value)) {
105. if (this.telNumberNoSpace.length <= 3) {
106. nextText = this.telNumberNoSpace;
107. } else {
108. let split1: string = this.telNumberNoSpace.substring(0, 3);
109. let split2: string = this.telNumberNoSpace.substring(3);
110. nextText = split1 + ' ' + split2;
111. if (this.telNumberNoSpace.length > 7) {
112. split2 = this.telNumberNoSpace.substring(3, 7);
113. let split3: string = this.telNumberNoSpace.substring(7);
114. nextText = split1 + ' ' + split2 + ' ' + split3;
115. }
116. }
117. } else {
118. nextText = value;
119. }
120. console.info("onChange Triggered:" + this.text + "|" + nextText + "|" + value);
121. if (this.text === nextText && nextText === value) {
122. // 此时说明数字已经格式化完成了 在这个时候改变光标位置不会被重置掉
123. this.setCaret();
124. } else {
125. this.calcCaretPosition(nextText);
126. }
127. this.text = nextText;
128. })
129. .onTextSelectionChange((selectionStart, selectionEnd) => {
130. // 记录光标位置
131. console.info("selection change: ", selectionStart, selectionEnd);
132. this.lastCaretPosition = selectionStart;
133. this.lastCaretPositionEnd = selectionEnd;
134. })// 从API version 10开始支持
135. }
136. }
137. .width('100%')
138. .height("100%")
139. }
140. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Cw-k3Nb0QyCP2-EtiTAV8Q/zh-cn_image_0000002552959764.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=16DBF89EB92B464905FD301D832F54B17C17E00B09370AFB190378C545068456)

### 示例7（设置文本断行规则）

从API version 12开始，该示例通过[wordBreak](ts-basic-components-textinput.md#wordbreak12)属性实现了TextInput不同断行规则下的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State textStrEn: string =
6. 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.';
7. @State textStrZn: string =
8. '多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。\n高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。';

10. build() {
11. Row() {
12. Column() {
13. Text("TextInput为inline模式，WordBreakType属性为NORMAL的样式：").fontSize(16).fontColor(0xCCCCCC)
14. TextInput({
15. text: this.textStrEn
16. })
17. .margin(10)
18. .fontSize(16)
19. .style(TextInputStyle.Inline)// Inline模式
20. .wordBreak(WordBreak.NORMAL) // 非Inline模式该属性无效

22. Text("TextInput为inline模式，英文文本，WordBreakType属性为BREAK_ALL的样式：").fontSize(16).fontColor(0xCCCCCC)
23. TextInput({
24. text: this.textStrEn
25. })
26. .margin(10)
27. .fontSize(16)
28. .style(TextInputStyle.Inline)
29. .wordBreak(WordBreak.BREAK_ALL)

31. Text("TextInput为inline模式，中文文本，WordBreakType属性为BREAK_ALL的样式：").fontSize(16).fontColor(0xCCCCCC)
32. TextInput({
33. text: this.textStrZn
34. })
35. .margin(10)
36. .fontSize(16)
37. .style(TextInputStyle.Inline)
38. .wordBreak(WordBreak.BREAK_ALL)

40. Text("TextInput为inline模式，WordBreakType属性为BREAK_WORD的样式：").fontSize(16).fontColor(0xCCCCCC)
41. TextInput({
42. text: this.textStrEn
43. })
44. .margin(10)
45. .fontSize(16)
46. .style(TextInputStyle.Inline)
47. .wordBreak(WordBreak.BREAK_WORD)
48. }.width('100%')
49. }.height('100%').margin(10)
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Vz_1gJJnRx-0tmjIB45GEQ/zh-cn_image_0000002583479765.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=2F6F6F1113666F9E696D6496E2487ADC3D3DDE50CEC31D125F70137A0BF5DC15)

### 示例8（设置文本样式）

从API version 12开始，该示例通过[lineHeight](ts-basic-components-textinput.md#lineheight12)、[letterSpacing](ts-basic-components-textinput.md#letterspacing12)、[decoration](ts-basic-components-textinput.md#decoration12)属性展示了不同样式的文本效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. build() {
6. Row() {
7. Column() {
8. Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)
9. TextInput({ text: 'lineHeight unset' })
10. .border({ width: 1 }).padding(10).margin(5)
11. TextInput({ text: 'lineHeight 15' })
12. .border({ width: 1 }).padding(10).margin(5).lineHeight(15)
13. TextInput({ text: 'lineHeight 30' })
14. .border({ width: 1 }).padding(10).margin(5).lineHeight(30)

16. Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)
17. TextInput({ text: 'letterSpacing 0' })
18. .border({ width: 1 }).padding(5).margin(5).letterSpacing(0)
19. TextInput({ text: 'letterSpacing 3' })
20. .border({ width: 1 }).padding(5).margin(5).letterSpacing(3)
21. TextInput({ text: 'letterSpacing -1' })
22. .border({ width: 1 }).padding(5).margin(5).letterSpacing(-1)

24. Text('decoration').fontSize(9).fontColor(0xCCCCCC)
25. TextInput({ text: 'LineThrough, Red' })
26. .border({ width: 1 }).padding(5).margin(5)
27. .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
28. TextInput({ text: 'Overline, Red, DASHED' })
29. .border({ width: 1 }).padding(5).margin(5)
30. .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED })
31. TextInput({ text: 'Underline, Red, WAVY' })
32. .border({ width: 1 }).padding(5).margin(5)
33. .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
34. }.height('90%')
35. }
36. .width('90%')
37. .margin(10)
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/QBTqfChHQBi4DpQUPANagg/zh-cn_image_0000002552800116.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=261BC234DB1042E22178009EE688938B59E44E576443DE5B912240082F37F6E6)

### 示例9（设置文字特性效果）

从API version 12开始，该示例通过[fontFeature](ts-basic-components-textinput.md#fontfeature12)属性实现了文本在不同文字特性下的展示效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text1: string = 'This is ss01 on : 0123456789';
6. @State text2: string = 'This is ss01 off: 0123456789';

8. build() {
9. Column() {
10. TextInput({ text: this.text1 })
11. .fontSize(20)
12. .margin({ top: 200 })
13. .fontFeature("\"ss01\" on")
14. TextInput({ text: this.text2 })
15. .margin({ top: 10 })
16. .fontSize(20)
17. .fontFeature("\"ss01\" off")
18. }
19. .width("90%")
20. .margin("5%")
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/uF1dPFjfS6qBsWgx4APiFA/zh-cn_image_0000002583439811.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=3CC5F45BD863142952F1AC5A3CEA23971E91577177E391632475C368256EF140)

### 示例10（自定义键盘避让）

该示例通过[customKeyboard](ts-basic-components-textinput.md#customkeyboard10)（从API version 10开始）属性配置[KeyboardOptions](ts-basic-components-richeditor.md#keyboardoptions12)（从API version 12开始）接口实现了自定义键盘避让的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. controller: TextInputController = new TextInputController();
6. @State inputValue: string = "";
7. @State height1: string | number = '80%';
8. @State supportAvoidance: boolean = true;

10. // 自定义键盘组件
11. @Builder
12. CustomKeyboardBuilder() {
13. Column() {
14. Row() {
15. Button('x').onClick(() => {
16. // 关闭自定义键盘
17. this.controller.stopEditing();
18. }).margin(10)
19. }

21. Grid() {
22. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
23. GridItem() {
24. Button(item + "")
25. .width(110).onClick(() => {
26. this.inputValue += item;
27. })
28. }
29. })
30. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
31. }.backgroundColor(Color.Gray)
32. }

34. build() {
35. Column() {
36. Row() {
37. Button("20%")
38. .fontSize(24)
39. .onClick(() => {
40. this.height1 = "20%";
41. })
42. Button("80%")
43. .fontSize(24)
44. .margin({ left: 20 })
45. .onClick(() => {
46. this.height1 = "80%";
47. })
48. }
49. .justifyContent(FlexAlign.Center)
50. .alignItems(VerticalAlign.Bottom)
51. .height(this.height1)
52. .width("100%")
53. .padding({ bottom: 50 })

55. TextInput({ controller: this.controller, text: this.inputValue })// 绑定自定义键盘
56. .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
57. .margin(10)
58. .border({ width: 1 })

60. }
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/rkZcdYMgRFihATP0ZZrx9g/zh-cn_image_0000002552959766.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=EFD11EE738D5D0EC120CB359A65B46385C3FD6BE94F8B6ABAB53812F0D17992E)

### 示例11（设置文本自适应）

从API version 12开始，该示例通过[minFontSize](ts-basic-components-textinput.md#minfontsize12)、[maxFontSize](ts-basic-components-textinput.md#maxfontsize12)、[heightAdaptivePolicy](ts-basic-components-textinput.md#heightadaptivepolicy12)属性实现了文本自适应字号的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. build() {
6. Row() {
7. Column() {
8. Text('heightAdaptivePolicy').fontSize(9).fontColor(0xCCCCCC)
9. TextInput({ text: 'This is the text without the height adaptive policy set' })
10. .width('80%').height(50).borderWidth(1).margin(1)
11. TextInput({ text: 'This is the text with the height adaptive policy set' })
12. .width('80%')
13. .height(50)
14. .borderWidth(1)
15. .margin(1)
16. .minFontSize(4)
17. .maxFontSize(40)
18. .maxLines(3)
19. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)
20. TextInput({ text: 'This is the text with the height adaptive policy set' })
21. .width('80%')
22. .height(50)
23. .borderWidth(1)
24. .margin(1)
25. .minFontSize(4)
26. .maxFontSize(40)
27. .maxLines(3)
28. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)
29. TextInput({ text: 'This is the text with the height adaptive policy set' })
30. .width('80%')
31. .height(50)
32. .borderWidth(1)
33. .margin(1)
34. .minFontSize(4)
35. .maxFontSize(40)
36. .maxLines(3)
37. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
38. }.height('90%')
39. }
40. .width('90%')
41. .margin(10)
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/v7gxYZL2RoOwXvgGAA3gTQ/zh-cn_image_0000002583479767.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=D1DE85B9F89949DA71DF805C90EE7EF290CEC2B74BEA4D3F682204F5C3AE7DC5)

### 示例12（设置折行规则）

从API version 12开始，该示例通过[lineBreakStrategy](ts-basic-components-textinput.md#linebreakstrategy12)属性实现了TextInput不同折行规则下的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State message1: string =
6. "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +
7. "The built-in components include buttons radio progress indicators and text You can set the rendering effect of these components in method chaining mode," +
8. "page components are divided into independent UI units to implementindependent creation development and reuse of different units on pages making pages more engineering-oriented.";
9. @State lineBreakStrategyIndex: number = 0;
10. @State lineBreakStrategy: LineBreakStrategy[] =
11. [LineBreakStrategy.GREEDY, LineBreakStrategy.HIGH_QUALITY, LineBreakStrategy.BALANCED];
12. @State lineBreakStrategyStr: string[] = ['GREEDY', 'HIGH_QUALITY', 'BALANCED'];

14. build() {
15. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
16. Text('lineBreakStrategy').fontSize(16).fontColor(Color.Black)
17. TextInput({ text: this.message1 })
18. .fontSize(12)
19. .border({ width: 1 })
20. .padding(10)
21. .width('100%')
22. .maxLines(12)
23. .style(TextInputStyle.Inline)
24. .lineBreakStrategy(this.lineBreakStrategy[this.lineBreakStrategyIndex])
25. Row() {
26. Button('当前lineBreakStrategy模式：' + this.lineBreakStrategyStr[this.lineBreakStrategyIndex]).onClick(() => {
27. this.lineBreakStrategyIndex++;
28. if (this.lineBreakStrategyIndex > (this.lineBreakStrategyStr.length - 1)) {
29. this.lineBreakStrategyIndex = 0;
30. }
31. })
32. }.margin({ top: 20 })
33. }.height(700).width(370).padding({ left: 35, right: 35, top: 35 })
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/kHPZ39CkS5e9bT1zUle97Q/zh-cn_image_0000002552800118.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=A8F7D2EE43494FF9783E4109D27518C7FC35D90E9275AFB3B72A81775AF64E6D)

### 示例13（支持插入和删除回调）

从API version 12开始，该示例通过[onWillInsert](ts-basic-components-textinput.md#onwillinsert12)、[onDidInsert](ts-basic-components-textinput.md#ondidinsert12)、[onWillDelete](ts-basic-components-textinput.md#onwilldelete12)、[onDidDelete](ts-basic-components-textinput.md#ondiddelete12)接口实现了插入和删除的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State insertValue: string = "";
6. @State deleteValue: string = "";
7. @State insertOffset: number = 0;
8. @State deleteOffset: number = 0;
9. @State deleteDirection: number = 0;
10. @State currentValue_1: string = "";
11. @State currentValue_2: string = "";

13. build() {
14. Row() {
15. Column() {
16. TextInput({ text: "TextInput支持插入回调文本" })
17. .height(60)
18. .onWillInsert((info: InsertValue) => {
19. this.insertValue = info.insertValue;
20. return true;
21. })
22. .onDidInsert((info: InsertValue) => {
23. this.insertOffset = info.insertOffset;
24. })
25. .onWillChange((info: EditableTextChangeValue) => {
26. this.currentValue_1 = info.content
27. return true
28. })

30. Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)
31. Text("currentValue_1:" + this.currentValue_1).height(30)

33. TextInput({ text: "TextInput支持删除回调文本b" })
34. .height(60)
35. .onWillDelete((info: DeleteValue) => {
36. this.deleteValue = info.deleteValue;
37. this.deleteDirection = info.direction;
38. return true;
39. })
40. .onDidDelete((info: DeleteValue) => {
41. this.deleteOffset = info.deleteOffset;
42. this.deleteDirection = info.direction;
43. })
44. .onWillChange((info: EditableTextChangeValue) => {
45. this.currentValue_2 = info.content
46. return true
47. })

49. Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(30)
50. Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(30)
51. Text("currentValue_2:" + this.currentValue_2).height(30)

53. }.width('100%')
54. }
55. .height('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/hKYvZ4YPQsyIcrIcyglixA/zh-cn_image_0000002583439813.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=41FF8556FA4BB108D1D8B4C9729D6E40C7633FC1A174CCF1F2961DF60DC8F8DD)

### 示例14（文本扩展自定义菜单）

从API version 12开始，该示例通过[editMenuOptions](ts-basic-components-textinput.md#editmenuoptions12)接口实现了文本设置自定义菜单扩展项的文本内容、图标以及回调的功能，同时，可以在[onPrepareMenu](ts-text-common.md#属性-1)（从API version 20开始）回调中，进行菜单数据的设置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = 'TextInput editMenuOptions';
6. @State endIndex: number = 0;
7. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
8. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
9. // 从API version 23开始支持TextMenuItemId.autoFill
10. const idsToFilter: TextMenuItemId[] = [
11. TextMenuItemId.autoFill
12. ]
13. const items = menuItems.filter(item => !idsToFilter.some(id => id.equals(item.id)))
14. let item1: TextMenuItem = {
15. content: 'create1',
16. icon: $r('app.media.startIcon'),
17. id: TextMenuItemId.of('create1'),
18. };
19. let item2: TextMenuItem = {
20. content: 'create2',
21. id: TextMenuItemId.of('create2'),
22. icon: $r('app.media.startIcon'),
23. };
24. items.push(item1);
25. items.unshift(item2);
26. return items;
27. }
28. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
29. if (menuItem.id.equals(TextMenuItemId.of("create2"))) {
30. console.info("拦截 id: create2 start:" + textRange.start + "; end:" + textRange.end);
31. return true;
32. }
33. if (menuItem.id.equals(TextMenuItemId.of("prepare1"))) {
34. console.info("拦截 id: prepare1 start:" + textRange.start + "; end:" + textRange.end);
35. return true;
36. }
37. if (menuItem.id.equals(TextMenuItemId.COPY)) {
38. console.info("拦截 COPY start:" + textRange.start + "; end:" + textRange.end);
39. return true;
40. }
41. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
42. console.info("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end);
43. return false;
44. }
45. return false;
46. }
47. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
48. onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
49. let item1: TextMenuItem = {
50. content: 'prepare1_' + this.endIndex,
51. icon: $r('app.media.startIcon'),
52. id: TextMenuItemId.of('prepare1'),
53. };
54. menuItems.unshift(item1);
55. return menuItems;
56. }
57. @State editMenuOptions: EditMenuOptions = {
58. onCreateMenu: this.onCreateMenu,
59. onMenuItemClick: this.onMenuItemClick,
60. onPrepareMenu: this.onPrepareMenu
61. };

63. build() {
64. Column() {
65. TextInput({ text: this.text })
66. .width('95%')
67. .height(50)
68. .editMenuOptions(this.editMenuOptions)
69. .margin({ top: 100 })
70. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
71. this.endIndex = selectionEnd;
72. })
73. }
74. .width("90%")
75. .margin("5%")
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/gZFoffCqTUe1xiZ1zP5IUg/zh-cn_image_0000002552959768.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=EDC8E3E007BBA587071B846FD2E2A4006F7D89A4A57E76F39BF0DA078E64BF3F)

### 示例15（设置symbol类型清除按钮）

从API version 18开始，该示例通过[cancelButton](ts-basic-components-textinput.md#cancelbutton18)属性展示了自定义右侧symbol类型清除按钮样式的效果。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';

3. // xxx.ets
4. @Entry
5. @Component
6. struct TextInputExample {
7. @State text: string = '';
8. symbolModifier: SymbolGlyphModifier =
9. new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

11. build() {
12. Column() {
13. TextInput({ text: this.text, placeholder: 'input your word...' })
14. .cancelButton({
15. style: CancelButtonStyle.CONSTANT,
16. icon: this.symbolModifier
17. })
18. }
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/wrebh4o5T8ufP52m3MB4iw/zh-cn_image_0000002583479769.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=1A2EA7ACD2854359174CC8D416702CE584825A8B48C364B23E6372FF4A5B5730)

### 示例16（文本设置省略模式）

该示例通过[textOverflow](ts-basic-components-textinput.md#textoverflow12)（从API version 12开始）、[ellipsisMode](ts-basic-components-textinput.md#ellipsismode18)（从API version 18开始）、[style](ts-basic-components-textinput.md#style9)（从API version 9开始）属性展示了文本超长省略以及调整省略位置的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct EllipsisModeExample {
5. @State text: string = "As the sun begins to set, casting a warm golden hue across the sky," +
6. "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
7. " pink, and lavender, creating a breath taking tapestry that stretches as far as the eye can see." +
8. "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil.";
9. @State ellipsisModeIndex: number = 0;
10. @State ellipsisMode: (EllipsisMode | undefined | null)[] =
11. [EllipsisMode.END, EllipsisMode.START, EllipsisMode.CENTER];
12. @State ellipsisModeStr: string[] = ['END ', 'START', 'CENTER'];
13. @State textOverflowIndex: number = 0;
14. @State textOverflow: TextOverflow[] = [TextOverflow.Ellipsis, TextOverflow.Clip];
15. @State textOverflowStr: string[] = ['Ellipsis', 'Clip'];
16. @State styleInputIndex: number = 0;
17. @State styleInput: TextInputStyle[] = [TextInputStyle.Inline, TextInputStyle.Default];
18. @State styleInputStr: string[] = ['Inline', 'Default'];

20. build() {
21. Row() {
22. Column({ space: 20 }) {
23. TextInput({ text: this.text })
24. .textOverflow(this.textOverflow[this.textOverflowIndex])
25. .ellipsisMode(this.ellipsisMode[this.ellipsisModeIndex])
26. .style(this.styleInput[this.styleInputIndex])
27. .fontSize(30)
28. .margin(30)
29. Button('更改ellipsisMode模式：' + this.ellipsisModeStr[this.ellipsisModeIndex]).onClick(() => {
30. this.ellipsisModeIndex++;
31. if (this.ellipsisModeIndex > (this.ellipsisModeStr.length - 1)) {
32. this.ellipsisModeIndex = 0;
33. }
34. }).fontSize(20)
35. Button('更改textOverflow模式：' + this.textOverflowStr[this.textOverflowIndex]).onClick(() => {
36. this.textOverflowIndex++;
37. if (this.textOverflowIndex > (this.textOverflowStr.length - 1)) {
38. this.textOverflowIndex = 0;
39. }
40. }).fontSize(20)
41. Button('更改Style大小：' + this.styleInputStr[this.styleInputIndex]).onClick(() => {
42. this.styleInputIndex++;
43. if (this.styleInputIndex > (this.styleInputStr.length - 1)) {
44. this.styleInputIndex = 0;
45. }
46. }).fontSize(20)
47. }
48. }
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/nWejPvuPQnuOARV-inD3AQ/zh-cn_image_0000002552800120.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=847A1ADA1F5B8C4051032FDB1AA061B9423D5B6B83656ACCADA26AEB80194077)

### 示例17（输入框支持输入状态变化等回调）

从API version 8开始，该示例通过[onEditChange](ts-basic-components-textinput.md#oneditchange8)、[onCopy](ts-basic-components-textinput.md#oncopy8)、[onCut](ts-basic-components-textinput.md#oncut8)、[onPaste](ts-basic-components-textinput.md#onpaste8)、[onContentScroll](ts-basic-components-textinput.md#oncontentscroll10)（从API version 10开始）接口实现了输入框监测输入状态变化、复制、剪切、粘贴、文本内容滚动回调的效果，同时，可以通过设置[selectAll](ts-basic-components-textinput.md#selectall11)（从API version 11开始）属性，输入框初始状态下是否全选文本。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State editStatus: boolean = false;
6. @State copyValue: string = "";
7. @State cutValue: string = "";
8. @State pasteValue: string = "";
9. @State totalOffsetX: number = 0;
10. @State totalOffsetY: number = 0;

12. build() {
13. Row() {
14. Column() {
15. TextInput({ text: "TextInput支持输入状态变化时回调" })
16. .height(60)
17. .fontStyle(FontStyle.Italic)
18. .fontWeight(FontWeight.Bold)
19. .fontFamily("HarmonyOS Sans")
20. .copyOption(CopyOptions.LocalDevice)
21. .textAlign(TextAlign.Center)
22. .selectedBackgroundColor(Color.Blue)
23. .caretStyle({ width: '4vp' })
24. .caretPosition(10)
25. .selectionMenuHidden(true)
26. .onEditChange((status: boolean) => {
27. this.editStatus = status;
28. })
29. .defaultFocus(true)// 设置TextInput默认获焦
30. .enableKeyboardOnFocus(false)
31. .selectAll(false)

33. Text("editStatus:" + this.editStatus).height(30)

35. TextInput({ text: "TextInput支持复制操作时回调" })
36. .height(60)
37. .fontStyle(FontStyle.Italic)
38. .fontWeight(FontWeight.Bold)
39. .fontFamily("HarmonyOS Sans")
40. .copyOption(CopyOptions.LocalDevice)
41. .textAlign(TextAlign.Center)
42. .selectedBackgroundColor(Color.Blue)
43. .caretStyle({ width: '4vp' })
44. .onCopy((copyValue: string) => {
45. this.copyValue = copyValue;
46. })

48. Text("copyValue:" + this.copyValue).height(30)

50. TextInput({ text: "TextInput支持剪切操作时回调" })
51. .height(60)
52. .fontStyle(FontStyle.Italic)
53. .fontWeight(FontWeight.Bold)
54. .fontFamily("HarmonyOS Sans")
55. .copyOption(CopyOptions.LocalDevice)
56. .textAlign(TextAlign.Center)
57. .selectedBackgroundColor(Color.Blue)
58. .caretStyle({ width: '4vp' })
59. .onCut((cutValue: string) => {
60. this.cutValue = cutValue;
61. })

63. Text("cutValue:" + this.cutValue).height(30)

65. TextInput({ text: "TextInput支持粘贴操作时回调" })
66. .height(60)
67. .fontStyle(FontStyle.Italic)
68. .fontWeight(FontWeight.Bold)
69. .fontFamily("HarmonyOS Sans")
70. .copyOption(CopyOptions.LocalDevice)
71. .textAlign(TextAlign.Center)
72. .selectedBackgroundColor(Color.Blue)
73. .caretStyle({ width: '4vp' })
74. .onPaste((pasteValue: string) => {
75. this.pasteValue = pasteValue;
76. })

78. Text("pasteValue:" + this.pasteValue).height(30)

80. TextInput({ text: "TextInput支持文本内容滚动时回调: 文本内容宽度超出输入框宽度，滚动文本查看偏移量变化" })
81. .height(60)
82. .fontStyle(FontStyle.Italic)
83. .fontWeight(FontWeight.Bold)
84. .fontFamily("HarmonyOS Sans")
85. .copyOption(CopyOptions.LocalDevice)
86. .textAlign(TextAlign.Center)
87. .selectedBackgroundColor(Color.Blue)
88. .caretStyle({ width: '4vp' })
89. .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
90. this.totalOffsetX = totalOffsetX;
91. this.totalOffsetY = totalOffsetY;
92. })

94. Text("totalOffsetX:" + this.totalOffsetX + "  totalOffsetY:" + this.totalOffsetY).height(30)

96. }.width('100%')
97. }
98. .height('100%')
99. }
100. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/hl29WrztSQWw55-mu4AhTA/zh-cn_image_0000002583439815.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=5BD71418BDBDA8F12FB32E5DD150F897F9C38EDAE49C3025BE03E64B71CDBC5E)

### 示例18（设置最小字体范围与最大字体范围）

从API version 18开始，该示例通过[minFontScale](ts-basic-components-textinput.md#minfontscale18)、[maxFontScale](ts-basic-components-textinput.md#maxfontscale18)设置字体显示最小与最大范围。

```
1. // 开启应用缩放跟随系统
2. // AppScope/resources/base，新建文件夹profile。
3. // AppScope/resources/base/profile，新建文件configuration.json。
4. // AppScope/resources/base/profile/configuration.json，增加如下代码。
5. {
6. "configuration": {
7. "fontSizeScale": "followSystem",
8. "fontSizeMaxScale": "3.2"
9. }
10. }
```

```
1. // AppScope/app.json5，修改如下代码。
2. {
3. "app": {
4. "bundleName": "com.example.myapplication",
5. "vendor": "example",
6. "versionCode": 1000000,
7. "versionName": "1.0.0",
8. "icon": "$media:app_icon",
9. "label": "$string:app_name",
10. "configuration": "$profile:configuration"
11. }
12. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State minFontScale: number = 0.85;
6. @State maxFontScale: number = 2;

8. build() {
9. Column() {
10. Column({ space: 30 }) {
11. Text("通过minFontScale、maxFontScale调整文本显示的最大和最小字体缩放倍数。")
12. TextInput({
13. placeholder: 'The text area can hold an unlimited amount of text. input your word...',
14. text: '通过minFontScale、maxFontScale调整文本显示的最大和最小字体缩放倍数。'
15. })
16. .minFontScale(this.minFontScale)// 设置最小字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
17. .maxFontScale(this.maxFontScale) // 设置最大字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
18. }.width('100%')
19. }
20. }
21. }
```

| 系统字体缩放倍数为2倍 | 系统字体缩放倍数为3.2倍 |
| --- | --- |
|  |  |

### 示例19（设置选中指定区域的文本内容）

从API version 10开始，该示例通过[setTextSelection](ts-basic-components-textinput.md#settextselection10)方法展示如何设置选中指定区域的文本内容以及菜单的显隐策略。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct TextInputExample {
6. controller: TextInputController = new TextInputController();
7. @State startIndex: number = 0;
8. @State endIndex: number = 0;

10. build() {
11. Column({ space: 3 }) {
12. Text('Selection start:' + this.startIndex + ' end:' + this.endIndex)
13. TextInput({ text: 'Hello World', controller: this.controller })
14. .width('95%')
15. .height(40)
16. .defaultFocus(true)
17. .enableKeyboardOnFocus(true)
18. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
19. this.startIndex = selectionStart;
20. this.endIndex = selectionEnd;
21. })

23. Button('setTextSelection [0,3], set menuPolicy is MenuPolicy.SHOW')
24. .onClick(() => {
25. this.controller.setTextSelection(0, 3, { menuPolicy: MenuPolicy.SHOW });
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/yAgBUqSjRWSzH7uuZ9BKvA/zh-cn_image_0000002552800122.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=8EEF488117DDC213EDDFE394BC9BFA59D653072AE34B820C013BD152046D6B24)

### 示例20（设置文本描边）

从API version 20开始，该示例通过[strokeWidth](ts-basic-components-textinput.md#strokewidth20)和[strokeColor](ts-basic-components-textinput.md#strokecolor20)属性设置文本的描边宽度及颜色。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TextInputExample {
7. build() {
8. Row() {
9. Column() {
10. Text('stroke feature').fontSize(9).fontColor(0xCCCCCC)

12. TextInput({ text: 'Text without stroke' })
13. .width('100%')
14. .height(60)
15. .borderWidth(1)
16. .fontSize(40)
17. TextInput({ text: 'Text with stroke' })
18. .width('100%')
19. .height(60)
20. .borderWidth(1)
21. .fontSize(40)
22. .strokeWidth(LengthMetrics.px(-3.0))
23. .strokeColor(Color.Red)
24. TextInput({ text: 'Text with stroke' })
25. .width('100%')
26. .height(60)
27. .borderWidth(1)
28. .fontSize(40)
29. .strokeWidth(LengthMetrics.px(3.0))
30. .strokeColor(Color.Red)
31. }.height('90%')
32. }
33. .width('90%')
34. .margin(10)
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/d_JvuLz9Te-6NI7bgFEz4w/zh-cn_image_0000002583439817.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=0CA8B05EA9CDA9D3F1E8D7E616A8D7D4BE190904E9FA80D4EF8B6BA856979B7B)

### 示例21（设置中西文自动间距）

从API version 20开始，该示例通过[enableAutoSpacing](ts-basic-components-textinput.md#enableautospacing20)属性设置中西文自动间距。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. build() {
6. Row() {
7. Column() {
8. Text('开启中西文自动间距').margin(5)
9. TextInput({text: '中西文Auto Spacing自动间距'})
10. .enableAutoSpacing(true)
11. Text('关闭中西文自动间距').margin(5)
12. TextInput({text: '中西文Auto Spacing自动间距'})
13. .enableAutoSpacing(false)
14. }.height('100%')
15. }
16. .width('60%')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/0AsIh7GnRc2Ch8b0ylF2Rg/zh-cn_image_0000002552959772.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=05F56024C9C587D7AC5AE9582D4EC734318C71BC6B2A4D3B3B0CCB48711F8A4C)

### 示例22（设置字符计数颜色以及超出字符颜色）

从API version 22开始，该示例通过[showCounter](ts-basic-components-textinput.md#showcounter11)属性的counterTextColor和counterTextOverflowColor设置字符计数颜色以及超出字符颜色。

```
1. import { ColorMetrics } from '@kit.ArkUI';

3. // xxx.ets
4. @Entry
5. @Component
6. struct TextInputExample {
7. @State text: string = '';
8. controller: TextInputController = new TextInputController();

10. build() {
11. Column() {
12. TextInput({ text: this.text, controller: this.controller })
13. .placeholderFont({ size: 16, weight: 400 })
14. .width(336)
15. .height(56)
16. .maxLength(6)
17. .showCounter(true, {
18. thresholdPercentage: 50,
19. highlightBorder: true,
20. counterTextColor: ColorMetrics.resourceColor(Color.Red),
21. counterTextOverflowColor: ColorMetrics.resourceColor(Color.Orange)
22. })
23. .onChange((value: string) => {
24. this.text = value;
25. })
26. }.width('100%').height('100%').backgroundColor('#F1F3F5')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/21wiLjJ-QfmIOjbz1zpPQA/zh-cn_image_0000002583479773.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=5CD20D61764B9B05D17703A6ECEDF59890953C5E85D353651309977A95F9440E)

### 示例23（设置placeholder富文本样式）

从API version 22开始，该示例通过[setStyledPlaceholder](ts-universal-attributes-text-style.md#setstyledplaceholder22)接口设置placeholder富文本样式。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. @Entry
4. @Component
5. struct TextInputExample  {
6. styledString: MutableStyledString =
7. new MutableStyledString("输入框富文本：文本",
8. [
9. {
10. start: 0,
11. length: 7,
12. styledKey: StyledStringKey.FONT,
13. styledValue: new TextStyle({
14. fontColor: Color.Orange,
15. fontSize: LengthMetrics.fp(24)
16. })
17. },
18. {
19. start: 7,
20. length: 4,
21. styledKey: StyledStringKey.FONT,
22. styledValue: new TextStyle({
23. fontColor: Color.Gray,
24. fontSize: LengthMetrics.fp(20),
25. strokeWidth: LengthMetrics.px(-5),
26. strokeColor: Color.Black,
27. })
28. },
29. {
30. start: 0,
31. length: 1,
32. styledKey: StyledStringKey.PARAGRAPH_STYLE,
33. styledValue: new ParagraphStyle({
34. textVerticalAlign: TextVerticalAlign.CENTER
35. })
36. }
37. ]);
38. controllerInput: TextInputController = new TextInputController();

40. aboutToAppear() {
41. this.controllerInput.setStyledPlaceholder(this.styledString)
42. }

44. build() {
45. Scroll() {
46. Column() {
47. Text("TextInput placeholder富文本")
48. .fontSize(8)
49. TextInput({
50. controller: this.controllerInput
51. })
52. .fontSize(24)
53. .margin(10)
54. }
55. .width('100%')
56. }
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/U-VG14IXQlqgT3_KG9o2hQ/zh-cn_image_0000002552800124.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=8CB948A19C0218700288AF06E48CB680B5352ABD5EC7FB1CF9A7CEEFE3592A2E)

### 示例24（设置输入法扩展信息）

从API version 22开始，该示例通过[IMEClient](ts-text-common.md#imeclient20对象说明)的setExtraConfig设置输入法扩展信息。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. build() {
6. Column() {
7. TextInput({ text: '拉起输入法前执行onWillAttachIME回调' })
8. .onWillAttachIME((client: IMEClient) => {
9. client.setExtraConfig({
10. customSettings: {
11. name: "TextInput", // 自定义属性
12. id: client.nodeId // 自定义属性
13. }
14. })
15. })
16. }.height('100%')
17. }
18. }
```

### 示例25（设置内联输入风格编辑态时滚动条的显示模式）

从API version 10开始，该示例通过[barState](ts-basic-components-textinput.md#barstate10)接口设置内联输入风格编辑态时滚动条的显示或隐藏状态。

```
1. @Entry
2. @Component
3. struct demo {
4. @State message: string = '这里是一段长文本'.repeat(10)

6. build() {
7. Column({ space: 20 }) {
8. TextInput({ text: '内联模式，设置BarState.On，' + this.message })
9. .style(TextInputStyle.Inline)
10. .barState(BarState.On)

12. TextInput({ text: '内联模式，设置BarState.Off，' + this.message })
13. .style(TextInputStyle.Inline)
14. .barState(BarState.Off)
15. }
16. .width('100%')
17. .height('100%')
18. .padding(20)
19. .justifyContent(FlexAlign.Center)
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/a4Vp7JyjScKfVa0qkIt9Jg/zh-cn_image_0000002583439819.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=C22595B0E7516784C50BDCD69648FB178667D0743F3C85BEF91427E62879BE35)

### 示例26（设置行首标点压缩）

该示例通过[compressLeadingPunctuation](ts-basic-components-textinput.md#compressleadingpunctuation23)接口设置行首标点压缩，左侧有间距的标点符号位于行首时，标点会直接压缩间距至左侧边界。

从API version 23开始，支持compressLeadingPunctuation接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column(){
7. TextInput({ text: "\u300C行首标点压缩打开" })
8. .compressLeadingPunctuation(true)
9. .margin(5)
10. .style(TextInputStyle.Inline)
11. .fontSize(30)
12. .width("90%")
13. TextInput({ text: "\u300C行首标点压缩关闭" })
14. .compressLeadingPunctuation(false)
15. .style(TextInputStyle.Inline)
16. .fontSize(30)
17. .width("90%")
18. }
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/2U2fgY-8T5KZRZPOjqklCA/zh-cn_image_0000002552959774.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=523907B317F0562572F74603E141006A66474D8E3FD93D7051BC64BAF122F84D)

### 示例27（设置自适应间距）

该示例通过[includeFontPadding](ts-basic-components-textinput.md#includefontpadding23)接口增加首行尾行间距和[fallbackLineSpacing](ts-basic-components-textinput.md#fallbacklinespacing23)接口设置自适应行间距。

从API version 23开始，新增[includeFontPadding](ts-basic-components-textinput.md#includefontpadding23)和[fallbackLineSpacing](ts-basic-components-textinput.md#fallbacklinespacing23)接口。

```
1. // xxx.ets

3. const UYGHUR_TEXT: string = 'ياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەنياخشىمۇسەن';
4. @Entry
5. @Component
6. struct Index {
7. @State include: boolean | null | undefined = false;
8. @State fallback: boolean | null | undefined = false;
9. @State displayText: string = UYGHUR_TEXT;

11. build() {
12. Column() {
13. TextInput({
14. text: this.displayText,
15. placeholder: '请输入内容...'
16. })
17. .includeFontPadding(this.include)
18. .fallbackLineSpacing(this.fallback)
19. .lineHeight(5)
20. .width('100%')
21. .height(100)
22. .backgroundColor('#eee')
23. .borderWidth(1)
24. .borderColor('#dddddd')

26. Scroll() {
27. Column() {
28. // --- IncludeFontPadding相关按钮 ---
29. Button('设置includePadding: ' + this.include)
30. .onClick(() => {
31. this.include = this.include === false ? true : false;
32. })
33. .margin({ bottom: 10 })

35. // --- FallbackLineSpacing相关按钮 ---
36. Button('设置fallbackLineSpacing: ' + this.fallback)
37. .onClick(() => {
38. this.fallback = this.fallback === false ? true : false;
39. })
40. .margin({ bottom: 10 })

42. }
43. .width('100%')
44. .padding(5)
45. }
46. .height(250)
47. .backgroundColor('transparent')
48. .scrollBarWidth(2)
49. .scrollBarColor('#888')

51. }
52. .width('100%')
53. .height('100%')
54. .padding(20)
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/7tELXRHaSm628OBwU3C1jg/zh-cn_image_0000002583479775.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=ECB141C7738711AF738D26320B207A175898CE2D049B8E3CE7DE9C1D705A59D1)

### 示例28（设置文本拖拽时的背板样式）

该示例通过[selectedDragPreviewStyle](ts-basic-components-textinput.md#selecteddragpreviewstyle23)接口设置文本拖拽时的背板样式。

从API version 23开始，新增selectedDragPreviewStyle接口。

```
1. @Entry
2. @Component
3. struct TextInputTest {
4. build() {
5. Column() {
6. TextInput({ text: 'HelloWorld', placeholder: 'please input words' })
7. .copyOption(CopyOptions.InApp)
8. .width(200)
9. .height(50)
10. .margin(150)
11. .draggable(true)
12. .selectedDragPreviewStyle({color: 'rgba(227, 248, 249, 1)'})
13. }
14. .height('100%')
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/WxEt4YdOREGygb5y3N16lg/zh-cn_image_0000002552800126.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=824B49EBFE81631B7B736A32B3F4B9F550265BA896E9EF97E9E1FF19997EBB53)

### 示例29（删除文本框内的最后一个字符）

该示例通过调用[deleteBackward](ts-universal-attributes-text-style.md#deletebackward23)接口删除文本框内最后一个字符。

从API version 23开始，新增[deleteBackward](ts-universal-attributes-text-style.md#deletebackward23)接口。

```
1. @Entry
2. @Component
3. struct Page {
4. controller: TextInputController = new TextInputController();

6. build() {
7. Column() {
8. TextInput({ text: 'TextInput输入框Deletebackward示例', controller: this.controller })
9. Button('Delete backward')
10. .onClick(() => {
11. this.controller.deleteBackward();
12. })
13. }
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/dWTCS11RQRSLznVrASlgNw/zh-cn_image_0000002583439821.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=B9F9AC793FE11892C7B3D7361ACF9E865F708B04CF8585E1B8D26634E78292B5)

### 示例30（设置文本排版方向）

该示例通过[textDirection](ts-basic-components-textinput.md#textdirection23)接口设置文本排版方向。

从API version 23开始，新增textDirection接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = 'TextInput文本排版方向示例';

7. build() {
8. Column() {
9. Text('TextInput文本排版方向RTL，布局方向default')
10. .fontSize(12).width('90%').margin(5)
11. TextInput({ text: this.text })
12. .width(336)
13. .fontSize(16)
14. .textDirection(TextDirection.RTL)
15. .showCounter(true)
16. .maxLength(50)
17. Text('TextInput文本排版方向RTL，布局方向default，文本水平方向对齐方式LEFT')
18. .fontSize(12).width('90%').margin(5)
19. TextInput({ text: this.text })
20. .width(336)
21. .fontSize(16)
22. .textDirection(TextDirection.RTL)
23. .showCounter(true)
24. .maxLength(50)
25. .textAlign(TextAlign.LEFT)
26. Text('TextInput文本排版方向LTR，布局方向Rtl')
27. .fontSize(12).width('90%').margin(5)
28. TextInput({ text: this.text })
29. .width(336)
30. .fontSize(16)
31. .textDirection(TextDirection.LTR)
32. .direction(Direction.Rtl)
33. .maxLength(50)
34. .showCounter(true)
35. }.width('100%').height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Og3GaXVASbiSYxleNTtd9A/zh-cn_image_0000002552959776.png?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=2A53E9D456F7AF59D8D931F5B3507CB9053DEE290D9AE72CA5B18278EEEBD583)

### 示例31（将指定范围的文字滚动到可视区内）

本示例通过[scrollToVisible](ts-universal-attributes-text-style.md#scrolltovisible23)将可视区外的文本滚动到可视区内。

从API version 23开始，新增scrollToVisible接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = '12345678912345678912346789123456789123456789012121214521';
6. controller: TextInputController = new TextInputController();

8. build() {
9. Column() {
10. TextInput({ text: this.text, controller: this.controller })
11. .width(336)
12. .height(56)
13. Button("滚动文本到可视区").onClick(()=> {
14. this.controller.scrollToVisible({ start: 22, end: 30})
15. })
16. }.width('100%').height('100%').backgroundColor('#F1F3F5')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/uzizvVDFTYSoW64S-yAYMg/zh-cn_image_0000002583479777.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000146Z&HW-CC-Expire=86400&HW-CC-Sign=DA38D4C890E8862EB6BF0C67612481987154E18782D510282CE12E3E076F8EF8)
