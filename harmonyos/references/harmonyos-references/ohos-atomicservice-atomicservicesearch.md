---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicesearch
title: AtomicServiceSearch
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > AtomicServiceSearch
category: harmonyos-references
scraped_at: 2026-04-28T08:02:27+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:cbfe77fe7e81a483c8ba39abadabe096a367a3767a5ea5e9fb6a3b5243d20562
---

AtomicServiceSearch为开发者提供满足定制化需求的功能，内容包括默认显示的搜索区、可自定义的选择区和功能区（最多两个）。

说明

该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';
```

## AtomicServiceSearch

PhonePC/2in1TabletTVWearable

```
1. AtomicServiceSearch({
2. value?: ResourceStr,
3. placeholder?: ResourceStr,
4. controller?: SearchController,
5. select?: SelectParams,
6. search?: SearchParams,
7. operation?: OperationParams,
8. })
```

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**装饰器类型：** @Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 设置当前显示的搜索文本内容。默认值为空字符串。 |
| placeholder | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 搜索框内默认显示的提示文本。默认值为Search。 |
| controller | [SearchController](ts-basic-components-search.md#searchcontroller) | 否 | - | Search组件控制器，用于设置输入光标的位置、退出编辑态等操作。默认值为undefined。 |
| select | [SelectParams](ohos-atomicservice-atomicservicesearch.md#selectparams) | 否 | @Prop | select选择区的内容、事件及样式。默认值为undefined。 |
| search | [SearchParams](ohos-atomicservice-atomicservicesearch.md#searchparams) | 否 | @Prop | search搜索区可支持的事件及样式。默认值为undefined。 |
| operation | [OperationParams](ohos-atomicservice-atomicservicesearch.md#operationparams) | 否 | - | 选择区（右侧）的功能设置项。默认值为undefined。 |

## SelectParams

PhonePC/2in1TabletTVWearable

AtomicServiceSearch中“选择区”的可选属性。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | Array<[SelectOption](ts-basic-components-select.md#selectoption对象说明)> | 否 | 是 | 下拉选项内容。默认值为undefined。 |
| selected | number | 否 | 是 | 设置下拉菜单初始选项的索引。第一项的索引为0。当不设置selected属性时，默认选择值为-1，菜单项不选中。 |
| selectValue | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置下拉按钮本身的文本内容。默认值为undefined。 |
| onSelect | [OnSelectCallback](ohos-atomicservice-atomicservicesearch.md#onselectcallback) | 否 | 是 | 下拉菜单选中某一项的回调。默认值为undefined。 |
| menuItemContentModifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)<[MenuItemConfiguration](ts-basic-components-select.md#menuitemconfiguration12对象说明)> | 否 | 是 | 在Select组件上，定制下拉菜单项内容区的方法。在应用了该属性后，下拉菜单的内容将完全由开发者自定义，此时为选择区设置的下拉菜单分割线、背景色及字体样式等属性将不再生效。  modifier: 内容修改器，开发者需要自定义class实现ContentModifier接口。默认值为undefined。 |
| divider | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)> | null | 否 | 是 | 1.设置DividerOptions，则按设置的样式显示分割线。默认值：{strokeWidth: '1px', color: '#33182431'}。  2.设置为null时，不显示分割线。  3.strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。  4.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。 startMargin和endMargin的和超过optionWidth的值时，按照默认样式显示分割线。 |
| font | [Font](ts-types.md#font) | 否 | 是 | 下拉按钮本身的文本样式。默认值：{size: $r('sys.float.ohos\_id\_text\_size\_body1')}。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉菜单选中项的文本颜色。默认值：{fontColor: $r('sys.color.ohos\_id\_color\_text\_primary')}。 |
| selectedOptionBgColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉菜单选中项的背景色。默认值：$r('sys.color.ohos\_id\_color\_component\_activated')混合$r('sys.color.ohos\_id\_alpha\_highlight\_bg')的透明度。 |
| selectedOptionFont | [Font](ts-types.md#font) | 否 | 是 | 下拉菜单选中项的文本样式。默认值：{size:&nbsp;$r('sys.color.ohos\_id\_text\_size\_body1'), weight:&nbsp;FontWeight.Regular}。 |
| selectedOptionFontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉菜单选中项的文本颜色。默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated')。 |
| optionBgColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉菜单项的背景色。默认值：Color.Transparent。 |
| optionFont | [Font](ts-types.md#font) | 否 | 是 | 下拉菜单项的文本样式。默认值：{size:&nbsp;$r('sys.float.ohos\_id\_text\_size\_body1'), weight:&nbsp;FontWeight.Regular}。 |
| optionFontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉菜单项的文本颜色。默认值：$r('sys.color.ohos\_id\_color\_text\_primary')。 |
| optionWidth | [Dimension](ts-types.md#dimension10) | [OptionWidthMode](ts-appendix-enums.md#optionwidthmode11) | 否 | 是 | 设置下拉菜单项的宽度，不支持设置百分比。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。当设置为异常值或小于最小宽度56vp时，属性不生效，菜单项宽度设为默认值，即菜单默认宽度为2栅格。 |
| optionHeight | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置下拉菜单显示的最大高度，不支持设置百分比。下拉菜单的默认最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过默认最大高度。 |
| space | [Length](ts-types.md#length) | 否 | 是 | 下拉菜单项的文本与箭头之间的间距。默认值：8。 |
| arrowPosition | [ArrowPosition](ts-basic-components-select.md#arrowposition10枚举说明) | 否 | 是 | 下拉菜单项的文本与箭头之间的对齐方式。默认值：ArrowPosition.END。 |
| menuAlign | [MenuAlignParams](ohos-atomicservice-atomicservicesearch.md#menualignparams) | 否 | 是 | 设置下拉按钮与下拉菜单间的对齐方式。默认值：{alignType: MenuAlignType.START, offset: {dx: 0, dy: 0}}。 |
| menuBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 下拉菜单的背景色。默认值：Color.Transparent。 |
| menuBackgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 下拉菜单的背景模糊材质。默认值：BlurStyle.COMPONENT\_ULTRA\_THICK。 |

## SearchParams

PhonePC/2in1TabletTVWearable

AtomicServiceSearch中“搜索区”的可选属性。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| searchKey | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 用作找到一个唯一的search组件。默认值：undefined。 |
| componentBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置组件的背景色。默认值：$r('sys.color.ohos\_id\_color\_text\_field\_sub\_bg')。 |
| pressedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置组件按压态的背景色。默认值：$r('sys.color.ohos\_id\_color\_click\_effect')。 |
| searchButton | [SearchButtonParams](ohos-atomicservice-atomicservicesearch.md#searchbuttonparams) | 否 | 是 | 设置搜索框末尾搜索按钮。点击搜索按钮，同时触发onSubmit与onClick回调。  -value：搜索框末尾搜索按钮文本内容。  -option: 配置搜索框文本样式。默认值：{fontSize: '16fp', fontColor: '#ff3f97e9'}。 |
| placeholderColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | placeholder文本颜色。默认值：$r('sys.color.ohos\_id\_color\_text\_secondary')。 |
| placeholderFont | [Font](ts-types.md#font) | 否 | 是 | 设置placeholder文本样式，包括字体大小，字体粗细，字体族，字体风格。默认值：{size: $r('sys\_float.ohos\_id\_text\_size\_body1')}。 |
| textFont | [Font](ts-types.md#font) | 否 | 是 | 设置搜索框内输入文本样式，包括字体大小，字体粗细，字体族，字体风格。目前仅支持默认字体族。默认值：{size: $r('sys\_float.ohos\_id\_text\_size\_body1')}。 |
| textAlign | [TextAlign](ts-appendix-enums.md#textalign) | 否 | 是 | 文本在搜索框中的对齐方式。默认值：TextAlign.Start。 |
| copyOptions | [CopyOptions](ts-appendix-enums.md#copyoptions9) | 否 | 是 | 输入的文本是否可复制。默认值：CopyOptions.LocalDevice，支持设备内复制。 |
| searchIcon | [IconOptions](ts-basic-components-search.md#iconoptions10对象说明) | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 左侧搜索图标样式。  浅色模式默认值：{size: '16vp', color: '#99182431', src: ' '}。  深色模式默认值：{size: '16vp', color: '#99ffffff', src: ' '}。 |
| cancelIcon | [IconOptions](ts-basic-components-search.md#iconoptions10对象说明) | 否 | 是 | 右侧清除按钮样式。默认值：{style: CancelButtonStyle.INPUT, icon: {size: '16vp', color: '#99ffffff', src: ' '}}。  当style为CancelButtonStyle.CONSTANT时，默认显示清除样式。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 输入文本的字体颜色。默认值：$r('sys.color.ohos\_id\_color\_text\_secondary')。 |
| caretStyle | [CaretStyle](ts-text-common.md#caretstyle10) | 否 | 是 | 光标样式。默认值：{width: '1.5vp', color: '#007DFF'}。 |
| enableKeyboardOnFocus | boolean | 否 | 是 | Search获焦时，是否主动拉起软键盘。true表示Search获焦时主动拉起软键盘。默认值：true。 |
| hideSelectionMenu | boolean | 否 | 是 | 是否不弹出系统文本选择菜单。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，不弹出系统文本选择菜单。设置为false时，弹出系统文本选择菜单。默认值：false。 |
| type | [SearchType](ts-basic-components-search.md#searchtype11枚举说明) | 否 | 是 | 输入框类型。默认值：SearchType.Normal。 |
| maxLength | number | 否 | 是 | 设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符。默认值：-1。 |
| enterKeyType | [EnterKeyType](ts-basic-components-textinput.md#enterkeytype枚举说明) | 否 | 是 | 输入法回车键类型。默认值：EnterKeyType.Search。 |
| decoration | [TextDecorationOptions](ts-universal-attributes-text-style.md#textdecorationoptions12对象说明) | 否 | 是 | 文本装饰线对象。默认值：{type: TextDecorationType.None, color: Color.Black, style: TextDecorationStyle.SOLID}。 |
| letterSpacing | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本字符间距。正数拉开字符距离，负数则拉近字符距离。浮点数默认值为0.0，单位为物理像素px。若输入类型非number且无法解析为数字，则使用默认值。 |
| fontFeature | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置文字特性效果，比如数字等宽的特性。  格式为：normal | <feature-tag-value>  <feature-tag-value>的格式为：<string> [ <integer> | on | off ]  <feature-tag-value>的个数可以有多个，中间用','隔开。  例如，使用等宽数字的输入格式为："ss01" on。默认值为undefined。 |
| selectedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本选中底板颜色。默认为20%不透明度。 |
| inputFilter | [InputFilterParams](ohos-atomicservice-atomicservicesearch.md#inputfilterparams) | 否 | 是 | 通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。仅支持单个字符匹配，不支持字符串匹配。默认值为undefined。  -value: 正则表达式。  -error: 正则匹配失败时，返回被过滤的内容。 |
| textIndent | [Dimension](ts-types.md#dimension10) | 否 | 是 | 首行文本缩进。默认值：0。 |
| minFontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本最小显示字号。需要配合maxFontSize以及布局大小限制使用，单独设置不生效。默认值为undefined。 |
| maxFontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本最大显示字号。需要配合minFontSize以及布局大小限制使用，单独设置不生效。默认值为undefined。 |
| editMenuOptions | [EditMenuOptions](ts-text-common.md#editmenuoptions) | 否 | 是 | 设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。默认值为undefined。 |
| enablePreviewText | boolean | 否 | 是 | 是否开启输入预上屏。true表示开启输入预上屏。默认值：true。  需要配合开启输入法的预上屏功能。预上屏内容定义为文字暂存态，目前不支持文字拦截功能，因此该值为true时不触发onWillInsert、onDidInsert回调。 |
| enableHapticFeedback | boolean | 否 | 是 | 是否开启触控反馈。true表示开启。默认值：true。 |
| onSubmit | Callback<string> | [SearchSubmitCallback](ts-basic-components-search.md#searchsubmitcallback14) | 否 | 是 | 点击搜索图标、搜索按钮或者按下软键盘搜索按钮时触发该回调。默认值为undefined。 |
| onChange | [EditableTextOnChangeCallback](ts-text-common.md#editabletextonchangecallback12) | 否 | 是 | 输入内容发生变化时，触发该回调。默认值为undefined。 |
| onCopy | Callback<string> | 否 | 是 | 进行复制操作时，触发该回调。默认值为undefined。 |
| onCut | Callback<string> | 否 | 是 | 进行剪切操作时，触发该回调。默认值为undefined。 |
| onPaste | [OnPasteCallback](ohos-atomicservice-atomicservicesearch.md#onpastecallback) | 否 | 是 | 进行粘贴操作时，触发该回调。默认值为undefined。 |
| onTextSelectionChange | [OnTextSelectionChangeCallback](ohos-atomicservice-atomicservicesearch.md#ontextselectionchangecallback) | 否 | 是 | 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调。默认值为undefined。 |
| onContentScroll | [OnContentScrollCallback](ohos-atomicservice-atomicservicesearch.md#oncontentscrollcallback) | 否 | 是 | 文本内容滚动时，触发该回调。默认值为undefined。 |
| onEditChange | Callback<boolean> | 否 | 是 | 输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。isEditing为true表示正在输入。默认值为undefined。 |
| onWillInsert | Callback<[InsertValue](ts-text-common.md#insertvalue12对象说明), boolean> | 否 | 是 | 在将要输入时，触发该回调。true表示将输入内容正常插入结果字符串，false表示不插入。默认值为undefined。 |
| onDidInsert | Callback<[InsertValue](ts-text-common.md#insertvalue12对象说明)> | 否 | 是 | 在输入完成时，触发该回调。默认值为undefined。 |
| onWillDelete | Callback<[DeleteValue](ts-text-common.md#deletevalue12对象说明), boolean> | 否 | 是 | 在将要删除时，触发该回调。true表示正常删除，false表示不删除。默认值为undefined。 |
| onDidDelete | Callback<[DeleteValue](ts-text-common.md#deletevalue12对象说明)> | 否 | 是 | 在删除完成时，触发该回调。默认值为undefined。 |

## OperationParams

PhonePC/2in1TabletTVWearable

AtomicServiceSearch中“功能区”的初始化参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| auxiliaryItem | [OperationOption](ohos-arkui-advanced-subheader.md#operationoption) | 否 | 是 | 附属于搜索区（右侧）的功能位。默认值为undefined。 |
| independentItem | [OperationOption](ohos-arkui-advanced-subheader.md#operationoption) | 否 | 是 | 独立于搜索区（右侧）的功能位。默认值为undefined。 |

## InputFilterParams

PhonePC/2in1TabletTVWearable

搜索框过滤设置项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputFilterValue | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 正则表达式。 |
| error | Callback<string> | 否 | 是 | 正则匹配失败时，返回被过滤的内容。默认值为undefined。 |

## SearchButtonParams

PhonePC/2in1TabletTVWearable

搜索框末尾搜索按钮设置项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| searchButtonValue | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 搜索框末尾搜索按钮文本内容。 |
| options | [SearchButtonOptions](ts-basic-components-search.md#searchbuttonoptions10对象说明) | 否 | 是 | 配置搜索框文本样式。默认值：{fontSize: '16fp',fontColor: '#ff3f97e9'}。 |

## MenuAlignParams

PhonePC/2in1TabletTVWearable

下拉按钮与下拉菜单间的对齐方式设置项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alignType | [MenuAlignType](ts-basic-components-select.md#menualigntype10枚举说明) | 否 | 否 | 对齐方式类型。默认值：MenuAlignType.START。 |
| offset | [Offset](ts-types.md#offset) | 否 | 是 | 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。默认值：{dx: 0, dy: 0}。 |

## OnSelectCallback

PhonePC/2in1TabletTVWearable

type OnSelectCallback = (index: number, selectValue: string) => void

下拉菜单选中某一项的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项的索引，索引从0开始。 |
| selectValue | string | 是 | 选中项的值。 |

## OnPasteCallback

PhonePC/2in1TabletTVWearable

type OnPasteCallback = (pasteValue: string, event: PasteEvent) => void

进行粘贴操作时，触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pasteValue | string | 是 | 要粘贴的文本内容。 |
| event | [PasteEvent](ts-basic-components-richeditor.md#pasteevent11) | 是 | 用户自定义粘贴事件。 |

## OnTextSelectionChangeCallback

PhonePC/2in1TabletTVWearable

type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void

文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 文本选择区域的起始位置。 |
| selectionEnd | number | 是 | 文本选择区域的结束位置。 |

## OnContentScrollCallback

PhonePC/2in1TabletTVWearable

type OnContentScrollCallback = (totalOffsetX: number, totalOffsetY: number) => void

文本内容滚动时，触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| totalOffsetX | number | 是 | 文本左上角横坐标相较于整个内容输入区左上角横坐标的偏移量。 |
| totalOffsetY | number | 是 | 文本左上角纵坐标相较于整个内容输入区左上角纵坐标的偏移量。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（AtomicServiceSearch添加选择区）

该示例通过select参数为AtomicServiceSearch组件添加左侧选择区。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space: 6 }) {
8. Text('AtomicServiceSearch添加选择区').alignSelf(ItemAlign.Start).decoration({
9. type: TextDecorationType.Underline,
10. color: Color.Black,
11. style: TextDecorationStyle.SOLID
12. }).margin({ top: 20, bottom: 20 })

14. AtomicServiceSearch({
15. select: {
16. options: [
17. { value: 'Select1', icon: $r("app.media.sweep") }, // 自定义资源
18. { value: 'Select2', icon: $r("app.media.sweep") }, // 自定义资源
19. { value: 'Select3', icon: $r("app.media.sweep") }, // 自定义资源
20. { value: 'Select4', icon: $r("app.media.sweep") } // 自定义资源
21. ],
22. selected: -1,
23. selectValue: 'Select1',
24. onSelect: (index: number, selectValue: string) => { // 自定义事件
25. if (index === 0) {
26. this.alert(`index: ${index}, selectValue: ${selectValue}`);
27. } else if (index === 1) {
28. this.alert(`index: ${index}, selectValue: ${selectValue}`);
29. } else if (index === 2) {
30. this.alert(`index: ${index}, selectValue: ${selectValue}`);
31. } else if (index === 3) {
32. this.alert(`index: ${index}, selectValue: ${selectValue}`);
33. }
34. },
35. }
36. })
37. }.padding({ left: 16, right: 16 })
38. }

40. private alert(message: string): void {
41. this.getUIContext().showAlertDialog({ message: message });
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/3mwedwruRgGHkOeDrjixnQ/zh-cn_image_0000002552960080.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=78CD2889F9893845C401151AF4C0ACFD0F3C63AEF1C463CEA002926363CA8355)

### 示例2（AtomicServiceSearch添加功能位）

该示例通过operation参数为AtomicServiceSearch组件添加右侧功能位。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space: 6 }) {
8. Text('AtomicServiceSearch添加功能位').alignSelf(ItemAlign.Start).decoration({
9. type: TextDecorationType.Underline,
10. color: Color.Black,
11. style: TextDecorationStyle.SOLID
12. }).margin({ top: 20, bottom: 20 })

14. AtomicServiceSearch({
15. operation: {
16. // 附属于Search组件的功能位
17. auxiliaryItem: {
18. value: $r("app.media.sweep"), // 自定义资源
19. action: () => {
20. this.alert('扫一扫'); // 自定义事件
21. }
22. },
23. // 独立于Search组件的功能位
24. independentItem: {
25. value: $r("app.media.dingding"), // 自定义资源
26. action: () => {
27. this.alert('通知'); // 自定义事件
28. }
29. }
30. }
31. })
32. }.padding({ left: 16, right: 16 })
33. }

35. private alert(message: string): void {
36. this.getUIContext().showAlertDialog({ message: message });
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/ABvhDjvmTXS7cc9dlmlE4Q/zh-cn_image_0000002583480081.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=1F139D7FB95467E112872BDDE1237423B0C818747E32CBA5A1FB1EFD05FA94E5)

### 示例3（AtomicServiceSearch添加选择区及功能位）

该示例中为AtomicServiceSearch组件同时添加左侧选择区和右侧功能位。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space: 6 }) {
8. Text('AtomicServiceSearch+选择区+功能位').alignSelf(ItemAlign.Start).decoration({
9. type: TextDecorationType.Underline,
10. color: Color.Black,
11. style: TextDecorationStyle.SOLID
12. }).margin({ top: 20, bottom: 20 })

14. AtomicServiceSearch({
15. select: {
16. options: [
17. { value: 'Select1', icon: $r("app.media.sweep") }, // 自定义资源
18. { value: 'Select2', icon: $r("app.media.sweep") }, // 自定义资源
19. { value: 'Select3', icon: $r("app.media.sweep") }, // 自定义资源
20. { value: 'Select4', icon: $r("app.media.sweep") } // 自定义资源
21. ],
22. selected: -1,
23. selectValue: 'Select1',
24. onSelect: (index: number, selectValue:string) => {
25. if (index === 0) {
26. this.alert(`index: ${index}, selectValue: ${selectValue}`);
27. } else if (index === 1) {
28. this.alert(`index: ${index}, selectValue: ${selectValue}`);
29. } else if (index === 2) {
30. this.alert(`index: ${index}, selectValue: ${selectValue}`);
31. } else if (index === 3) {
32. this.alert(`index: ${index}, selectValue: ${selectValue}`);
33. }
34. },
35. },
36. operation: {
37. auxiliaryItem: {
38. value: $r("app.media.sweep"), // 自定义资源
39. action: () => {
40. this.alert('扫一扫'); // 自定义事件
41. }
42. },
43. independentItem: {
44. value: $r("app.media.dingding"), // 自定义资源
45. action: () => {
46. this.alert('通知'); // 自定义事件
47. }
48. }
49. }
50. })
51. }.padding({ left: 16, right: 16 })
52. }

54. private alert(message: string): void {
55. this.getUIContext().showAlertDialog({ message: message });
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/nayhzQj4RMC7Laeczl6HFg/zh-cn_image_0000002552800432.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=DC02EAFD99B75B80FC8C66A3C14E7D86655D96B780369E31091CB3A605B21BD7)

### 示例4（search回调事件）

该示例通过onWillInsert、onDidInsert、onWillDelete、onDidDelete接口实现了插入和删除的功能。

通过onSubmit接口实现了搜索区内容提交的功能。

通过onChange接口实现了监听搜索区内容变化的功能。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State insertValue: string = "";
7. @State deleteValue: string = "";
8. @State insertOffset: number = 0;
9. @State deleteOffset: number = 0;
10. @State deleteDirection: number = 0;
11. @State startIndex: number = 0;
12. @State endIndex: number = 0;
13. @State offsetX: number = 0;
14. @State offsetY: number = 0;
15. @State changeValue: string = '';
16. @State value: string = 'false';
17. @State submitValue: string = '';
18. @State text: string = 'Search editMenuOptions';

20. build() {
21. Column({ space: 6 }) {
22. Text('AtomicServiceSearch绑定事件').alignSelf(ItemAlign.Start).decoration({
23. type: TextDecorationType.Underline,
24. color: Color.Black,
25. style: TextDecorationStyle.SOLID
26. }).margin({ top: 20, bottom: 20 })

28. Column({ space: 6 }) {
29. Text('editing: ' + this.value).width('100%').height(25).borderRadius(15).padding({ left: 15 })
30. .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
31. Text('onSubmit:' + this.submitValue).width('100%').height(25).borderRadius(15).padding({ left: 15 })
32. .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
33. Text('onChange:' + this.changeValue).width('100%').height(25).borderRadius(15).padding({ left: 15 })
34. .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
35. Text('offset x:' + this.offsetX + ' y:' + this.offsetY).width('100%').height(25).borderRadius(15).padding({ left: 15 })
36. .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
37. Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).width('100%').height(25)
38. .borderRadius(15).padding({ left: 15 }).backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1)
39. .textOverflow({ overflow: TextOverflow.MARQUEE });
40. Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).width('100%').height(25)
41. .borderRadius(15).padding({ left: 15 }).backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1)
42. .textOverflow({ overflow: TextOverflow.MARQUEE });
43. Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).width('100%').height(25)
44. .borderRadius(15).padding({ left: 15 }).backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1)
45. .textOverflow({ overflow: TextOverflow.MARQUEE });
46. AtomicServiceSearch({
47. select: {
48. options: [
49. { value: 'Select1', icon: $r("app.media.sweep") },
50. { value: 'Select2', icon: $r("app.media.sweep") },
51. { value: 'Select3', icon: $r("app.media.sweep") },
52. { value: 'Select4', icon: $r("app.media.sweep") }
53. ],
54. selected: -1,
55. selectValue: 'Select1',
56. onSelect: (index: number) => {
57. if (index === 0) {
58. this.alert('Select1');
59. } else if (index === 1) {
60. this.alert('Select2');
61. } else if (index === 2) {
62. this.alert('Select3');
63. } else if (index === 3) {
64. this.alert('Select4');
65. }
66. },
67. },
68. search: {
69. onSubmit: (value: string) => {
70. this.submitValue = value
71. },
72. onChange: (value: string) => {
73. this.changeValue = value
74. },
75. onCopy: () => {
76. this.alert('onCopy');
77. },
78. onCut: () => {
79. this.alert('onCut');
80. },
81. onPaste: () => {
82. this.alert('onPaste');
83. },
84. onTextSelectionChange: (selectionStart: number, selectionEnd: number) => {
85. this.startIndex = selectionStart
86. this.endIndex = selectionEnd
87. },
88. onContentScroll: (totalOffsetX: number, totalOffsetY: number) => {
89. this.offsetX = totalOffsetX
90. this.offsetY = totalOffsetY
91. },
92. onEditChange: (data: boolean) => {
93. this.value = data ? 'true' : 'false'
94. },
95. onWillInsert: (info: InsertValue) => {
96. this.insertValue = info.insertValue
97. return true;
98. },
99. onDidInsert: (info: InsertValue) => {
100. this.insertOffset = info.insertOffset
101. },
102. onWillDelete: (info: DeleteValue) => {
103. this.deleteValue = info.deleteValue
104. info.direction
105. return true;
106. },
107. onDidDelete: (info: DeleteValue) => {
108. this.deleteOffset = info.deleteOffset
109. this.deleteDirection = info.direction
110. }
111. }
112. })
113. }
114. }.padding({ left: 16, right: 16 })
115. }

117. private alert(message: string): void {
118. this.getUIContext().showAlertDialog({ message: message });
119. }
120. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/gg2TNOi8RpWrS2ROMQ61Rw/zh-cn_image_0000002583440127.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=E0612B41D487E92BA6C2A77A8B0A0EB5EB0813EEBF4E871B3D47912F081FBFA8)

### 示例5（AtomicServiceSearch修改样式）

该示例通过search、select、value、placeholder参数实现了AtomicServiceSearch组件样式的自定义。

```
1. import { AtomicServiceSearch, SearchParams, SelectParams } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State private placeholder: string = 'Type to Search...';
7. @State private defaultValue: string = 'default';
8. @State private search?: SearchParams = {};
9. @State private select?: SelectParams = {
10. options: [
11. { value: 'Select1', icon: $r("app.media.sweep") },
12. { value: 'Select2', icon: $r("app.media.sweep") },
13. { value: 'Select3', icon: $r("app.media.sweep") },
14. { value: 'Select4', icon: $r("app.media.sweep") }
15. ],
16. selected: -1,
17. selectValue: 'Select1',
18. onSelect: (index: number) => {
19. if (index === 0) {
20. this.alert('Select1');
21. } else if (index === 1) {
22. this.alert('Select2');
23. } else if (index === 2) {
24. this.alert('Select3');
25. } else if (index === 3) {
26. this.alert('Select4');
27. }
28. }
29. };

31. build() {
32. Column({ space: 8 }) {
33. Text('AtomicServiceSearch修改样式').alignSelf(ItemAlign.Start).decoration({
34. type: TextDecorationType.Underline,
35. color: Color.Black,
36. style: TextDecorationStyle.SOLID
37. }).margin({ top: 20, bottom: 20 })

39. AtomicServiceSearch({
40. value: this.defaultValue,
41. placeholder: this.placeholder,
42. select: this.select,
43. search: this.search,
44. operation: {
45. independentItem: {
46. value: $r(`app.media.dingding`),
47. action: () => {
48. this.alert('通知');
49. }
50. }
51. }
52. })
53. Button("修改placeholder")
54. .width('100%')
55. .type(ButtonType.Normal)
56. .borderRadius(20)
57. .onClick(() => {
58. if (this.placeholder === 'Search...') {
59. this.placeholder = 'Type to Search...';
60. } else {
61. this.placeholder = 'Search...';
62. }
63. });
64. Button("修改defaultValue")
65. .width('100%')
66. .type(ButtonType.Normal)
67. .borderRadius(20)
68. .onClick(() => {
69. if (this.defaultValue === 'value') {
70. this.defaultValue = 'defaultValue';
71. } else {
72. this.defaultValue = 'value';
73. }
74. });
75. Button("修改Select样式")
76. .width('100%')
77. .type(ButtonType.Normal)
78. .borderRadius(20)
79. .onClick(() => {
80. this.select = {
81. options: [
82. { value: '选项1', icon: $r("app.media.dingding") },
83. { value: '选项2', icon: $r("app.media.dingding") },
84. ],
85. selected: -1,
86. selectValue: '选项1',
87. onSelect: (index: number) => {
88. if (index === 0) {
89. this.alert('选项1');
90. } else if (index === 1) {
91. this.alert('选项2');
92. }
93. }
94. };
95. });

97. Button("修改Search样式")
98. .width('100%')
99. .type(ButtonType.Normal)
100. .borderRadius(20)
101. .onClick(() => {
102. this.search = {
103. componentBackgroundColor: '#e0eee8'
104. }
105. });
106. }.padding({ left: 16, right: 16 })
107. }

109. private alert(message: string): void {
110. this.getUIContext().showAlertDialog({ message: message });
111. }
112. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/rhvNF8TOS6yfI7aSb1m7bQ/zh-cn_image_0000002552960082.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=F2F2E40946D37A7E5D86F175C7F64C274CD4BFFA914EC3D92C8399FF8E96D986)

### 示例6（通过controller实现光标位置的设置）

该示例通过controller参数实现了光标位置的设置、选择指定区域中的内容及关闭编辑状态的功能。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. controller: SearchController = new SearchController();

8. build() {
9. Column({ space : 10 }) {
10. Text('通过controller实现光标位置的设置').alignSelf(ItemAlign.Start).decoration({
11. type: TextDecorationType.Underline,
12. color: Color.Black,
13. style: TextDecorationStyle.SOLID
14. }).margin({ top: 20, bottom: 20 })

16. AtomicServiceSearch(
17. {
18. value: 'Default Value',
19. placeholder: 'Type to Search...',
20. controller: this.controller,
21. search: {
22. searchButton: {
23. searchButtonValue: 'SEARCH',
24. options: { fontSize: '12fp', fontColor: '#ff0e1216' }
25. }
26. }
27. },
28. );
29. Button('caretPosition to 1').onClick(() => {
30. this.controller.caretPosition(1);
31. }).width('100%')
32. Button('stopEditing').onClick(() => {
33. this.controller.stopEditing();
34. }).width('100%')
35. Button('Selection [0,3]').onClick(() => {
36. this.controller.setTextSelection(0, 3)
37. }).width('100%')
38. }.padding({ left: 16, right: 16 })
39. }

41. public alert(message: string): void {
42. this.getUIContext().showAlertDialog({ message: message });
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/n3onppKPRfSescr9P3KIlw/zh-cn_image_0000002583480083.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=DCD036E8AC0158A3FA50855BEDC78AE333818913C0E01E5C67C5DE31E3225A23)

### 示例7（设置输入法回车键类型）

该示例通过enterKeyType属性实现了动态切换输入法回车键的效果。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State enterTypes: Array<EnterKeyType> = [EnterKeyType.Go, EnterKeyType.Search, EnterKeyType.Send, EnterKeyType.Done, EnterKeyType.Next, EnterKeyType.PREVIOUS, EnterKeyType.NEW_LINE]
7. @State index: number = 0

9. build() {
10. Column({ space : 10 }) {
11. Text('输入法回车键类型为搜索').alignSelf(ItemAlign.Start).decoration({
12. type: TextDecorationType.Underline,
13. color: Color.Black,
14. style: TextDecorationStyle.SOLID
15. }).margin({ top: 20, bottom: 20 })

17. AtomicServiceSearch({
18. placeholder: '输入法回车键类型为搜索',
19. search: {
20. enterKeyType: this.enterTypes[this.index]
21. }
22. })

24. Button('改变EnterKeyType').onClick(() => {
25. this.index = (this.index + 1) % this.enterTypes.length;
26. }).width('100%')

28. }.padding({ left: 16, right: 16 })
29. }

31. public alert(message: string): void {
32. this.getUIContext().showAlertDialog({ message: message });
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/L_8F4iL8TyGvqpvfNmwESw/zh-cn_image_0000002552800434.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=03D56ECF56D2DE6DDF2E9A4F9B87BFAFE50849413D401B7CC0193F3DE5190D5B)

### 示例8（设置文字特性效果）

该示例通过fontFeature属性实现了文本在不同文字特性下的展示效果。

```
1. ​​​​import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space : 10 }) {
8. Text('设置文字特性效果').alignSelf(ItemAlign.Start).decoration({
9. type: TextDecorationType.Underline,
10. color: Color.Black,
11. style: TextDecorationStyle.SOLID
12. }).margin({ top: 20, bottom: 20 })

14. AtomicServiceSearch({
15. value: 'This is ss01 on : 0123456789',
16. search: {
17. fontFeature: "\"ss01\" on"
18. }
19. });

21. AtomicServiceSearch({
22. value: 'This is ss01 off : 0123456789',
23. search: {
24. fontFeature: "\"ss01\" off"
25. }
26. });

28. AtomicServiceSearch({
29. value: 'fiabc1234567DEFGHIJKLMN',
30. search: {
31. fontFeature: "\"frac\" on"
32. }
33. });

35. AtomicServiceSearch({
36. value: 'fiabc1234567DEFGHIJKLMN',
37. search: {
38. fontFeature: "\"frac\" off"
39. }
40. });
41. }.padding({ left: 16, right: 16 })
42. }

44. public alert(message: string): void {
45. this.getUIContext().showAlertDialog({ message: message });
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/OiWUxwU3QieQdgKAXnUChQ/zh-cn_image_0000002583440129.png?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=C8F82D592AD07CCBB8E2CC23E16D22C935CB686C7D6D6726204F48DE5BFD6300)

### 示例9（设置文本自适应）

该示例通过minFontSize、maxFontSize属性展示了文本自适应字号的效果。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space : 10 }) {
8. Text('设置文本自适应').alignSelf(ItemAlign.Start).decoration({
9. type: TextDecorationType.Underline,
10. color: Color.Black,
11. style: TextDecorationStyle.SOLID
12. }).margin({ top: 20, bottom: 20 })

14. AtomicServiceSearch({
15. value: 'This is the text without the adaptive font',
16. }).width('80%').height(40).borderWidth(1).borderRadius(20)

18. AtomicServiceSearch({
19. value: 'This is the text without the adaptive font',
20. search: {
21. minFontSize: 4,
22. maxFontSize: 40
23. }
24. }).width('80%').height(40).borderWidth(1).borderRadius(20)
25. }.padding({ left: 16, right: 16 })
26. }

28. public alert(message: string): void {
29. this.getUIContext().showAlertDialog({ message: message });
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/vD-h0FK_T2iZ6lTXRXBZ1Q/zh-cn_image_0000002552960084.png?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=F501B319A957BC2066CDC7777D98FF498A0DA99785E217624DEA7BDFB81D0EB3)

### 示例10（文本扩展自定义菜单）

该示例通过editMenuOptions接口实现了文本设置自定义菜单扩展项的文本内容、图标以及回调的功能。

```
1. import { AtomicServiceSearch, TextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. aboutToAppear(): void {
7. TextMenuController.disableMenuItems([TextMenuItemId.AI_WRITER])
8. }

10. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
11. let item1: TextMenuItem = {
12. content: 'custom1',
13. icon: $r('app.media.startIcon'),
14. id: TextMenuItemId.of('custom1'),
15. }
16. let item2: TextMenuItem = {
17. content: 'custom2',
18. id: TextMenuItemId.of('custom2'),
19. icon: $r('app.media.startIcon'),
20. }
21. menuItems.push(item1)
22. menuItems.unshift(item2)
23. return menuItems
24. }
25. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
26. if (menuItem.id.equals(TextMenuItemId.of('custom2'))) {
27. console.info('拦截 id: custom2 start:' + textRange.start + '; end:' + textRange.end)
28. return true
29. }
30. if (menuItem.id.equals(TextMenuItemId.COPY)) {
31. console.info('拦截 COPY start:' + textRange.start + '; end:' + textRange.end)
32. return true
33. }
34. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
35. console.info('不拦截 SELECT_ALL start:' + textRange.start + '; end:' + textRange.end)
36. return false
37. }
38. return false
39. }
40. @State editMenuOptions: EditMenuOptions = {
41. onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick
42. }

44. build() {
45. Column({ space: 10 }) {
46. Text('文本扩展自定义菜单').alignSelf(ItemAlign.Start).decoration({
47. type: TextDecorationType.Underline,
48. color: Color.Black,
49. style: TextDecorationStyle.SOLID
50. }).margin({ top: 20, bottom: 20 })

52. AtomicServiceSearch({
53. value: 'Default input',
54. search: {
55. editMenuOptions: this.editMenuOptions
56. }
57. })
58. }.padding({ left: 16, right: 16 })
59. }

61. public alert(message: string): void {
62. this.getUIContext().showAlertDialog({ message: message });
63. }
64. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/SpRa_fbuQ8uU_Ej9PIbkHg/zh-cn_image_0000002583480085.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=692A39618BE534ED90A26BE491DC8B705F3C033F3A5953DBE279D59DF025E55E)

### 示例11（设置文本水平对齐/光标样式/选中背景色）

该示例通过textAlign、caretStyle、selectedBackgroundColor属性展示如何设置文本的水平对齐、光标样式和选中背景色。

```
1. import { AtomicServiceSearch, TextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. aboutToAppear(): void {
7. TextMenuController.disableMenuItems([TextMenuItemId.AI_WRITER])
8. }

10. build() {
11. Column() {
12. Text('设置文本水平对齐/光标样式/选中背景色').alignSelf(ItemAlign.Start).decoration({
13. type: TextDecorationType.Underline,
14. color: Color.Black,
15. style: TextDecorationStyle.SOLID
16. }).margin({ top: 20, bottom: 20 })

18. AtomicServiceSearch({
19. value: 'Search textAlign sample',
20. search: {
21. textAlign: TextAlign.Center,
22. caretStyle: { width: 3, color: Color.Green },
23. selectedBackgroundColor: Color.Gray
24. }
25. })
26. }.padding({ left: 16, right: 16 })
27. }

29. public alert(message: string): void {
30. this.getUIContext().showAlertDialog({ message: message });
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/tL88Ft7-Sa6HyR6irpxwtg/zh-cn_image_0000002552800436.png?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=4A374DEBC6CAE5442042522587AF82445DC151F7AD3FB4F2733BDB2F25FBA139)

### 示例12（对输入的文本进行过滤）

该示例通过inputFilter属性展示如何对输入的文本进行内容的过滤，以限制输入内容。

```
1. import { AtomicServiceSearch } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State filterValue: string = '';

8. build() {
9. Column() {
10. Column({ space: 10 }) {
11. Text('对输入的文本进行过滤').alignSelf(ItemAlign.Start).decoration({
12. type: TextDecorationType.Underline,
13. color: Color.Black,
14. style: TextDecorationStyle.SOLID
15. }).margin({ top: 20, bottom: 20 })
16. AtomicServiceSearch({
17. placeholder: 'please enter...',
18. search: {
19. inputFilter: {
20. inputFilterValue : '[a-z]',
21. error: (filterValue: string) => {this.filterValue = filterValue}
22. }
23. }
24. })
25. Text('Filter:' + this.filterValue).alignSelf(ItemAlign.Start)

27. }
28. }.padding({ left: 16, right: 16 })
29. }

31. public alert(message: string): void {
32. this.getUIContext().showAlertDialog({ message: message });
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/jQwzm_mJTIKFxf-t4YT22w/zh-cn_image_0000002583440131.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000225Z&HW-CC-Expire=86400&HW-CC-Sign=3B9F3BBD72C8AAC52645BDF36D845876174224158273ABCF76BA940143237AFF)
