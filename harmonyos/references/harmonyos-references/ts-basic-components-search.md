---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search
title: Search
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > Search
category: harmonyos-references
scraped_at: 2026-04-29T13:52:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c33902469ebe2f13fff38ccfce62de76fddca36ed6f1258efc5d7109ec1dc61
---

搜索框组件，适用于浏览器的搜索内容输入框等应用场景。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](ts-basic-components-richeditor.md)组件。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Search(options?: SearchOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SearchOptions](ts-basic-components-search.md#searchoptions18对象说明) | 否 | 搜索框组件初始化选项 |

## SearchOptions18+对象说明

PhonePC/2in1TabletTVWearable

Search初始化参数。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value8+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置当前显示的搜索文本内容。  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  从API version 20开始，支持Resource类型。 |
| placeholder8+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置无输入时的提示文本。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon8+ | string | 否 | 是 | 设置搜索图标路径，默认使用系统搜索图标。  **说明：**  icon的数据源支持[使用相对路径显示图片](ts-basic-components-image.md#示例25使用相对路径显示图片)和网络图片。  - 支持的图片格式包括png、jpg、bmp、svg、gif、pixelmap和heif。  - 支持Base64字符串。格式data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data], 其中[base64 data]为Base64字符串数据。  如果与属性searchIcon同时设置，则searchIcon优先。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| controller8+ | [SearchController](ts-basic-components-search.md#searchcontroller) | 否 | 是 | 设置Search组件控制器。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### searchButton

PhonePC/2in1TabletTVWearable

searchButton(value: ResourceStr, option?: SearchButtonOptions)

设置搜索框末尾搜索按钮。

点击搜索按钮，同时触发onSubmit与onClick回调。

Wearable设备上默认字体大小为18fp。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 搜索框末尾搜索按钮文本内容。  从API version 20开始，支持Resource类型。 |
| option | [SearchButtonOptions](ts-basic-components-search.md#searchbuttonoptions10对象说明) | 否 | 配置搜索框末尾搜索按钮文本样式。  默认值：  {  fontSize: '16fp',  fontColor: '#ff3f97e9'  } |

### placeholderColor

PhonePC/2in1TabletTVWearable

placeholderColor(value: ResourceColor)

设置placeholder文本颜色，Wearable设备上默认值为'#99ffffff'。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | placeholder文本颜色。  默认值：'#99182431'。 |

### placeholderFont

PhonePC/2in1TabletTVWearable

placeholderFont(value?: Font)

设置placeholder文本样式，包括字体大小、字体粗细、字体族、字体风格。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 否 | placeholder文本样式。 |

说明

可以使用[loadFontSync](js-apis-graphics-text.md#loadfontsync)注册自定义字体。

### textFont

PhonePC/2in1TabletTVWearable

textFont(value?: Font)

设置搜索框内输入文本样式，包括字体大小、字体粗细、字体族、字体风格。

Wearable设备上默认字体大小为18fp。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 否 | 搜索框内输入文本样式。 |

### textAlign9+

PhonePC/2in1TabletTVWearable

textAlign(value: TextAlign)

设置文本在搜索框中的对齐方式。目前支持的对齐方式有：TextAlign.Start、TextAlign.Center、TextAlign.End、TextAlign.LEFT、TextAlign.RIGHT。TextAlign.JUSTIFY的对齐方式按照TextAlign.Start处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextAlign](ts-appendix-enums.md#textalign) | 是 | 文本在搜索框中的对齐方式。  默认值：TextAlign.Start |

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

### copyOption9+

PhonePC/2in1TabletTVWearable

copyOption(value: CopyOptions)

设置输入的文本是否可复制。设置CopyOptions.None时，当前Search中的文字无法被复制、剪切、翻译、分享、搜索和帮写，支持粘贴和全选。

设置CopyOptions.None时，不允许拖拽。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](ts-appendix-enums.md#copyoptions9) | 是 | 输入的文本是否可复制。  默认值：CopyOptions.LocalDevice，支持设备内复制。 |

### searchIcon10+

PhonePC/2in1TabletTVWearable

searchIcon(value: IconOptions | SymbolGlyphModifier)

设置左侧搜索图标样式。

Wearable设备上默认图标大小为16vp。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [IconOptions](ts-basic-components-search.md#iconoptions10对象说明) | [SymbolGlyphModifier](ts-universal-attributes-text-style.md#symbolglyphmodifier12) | 是 | 左侧搜索图标样式。  浅色模式默认值：  {  size: '16vp',  color: '#99000000',  src: ' '  }  深色模式默认值：  {  size: '16vp',  color: '#99ffffff',  src: ' '  } |

### cancelButton10+

PhonePC/2in1TabletTVWearable

cancelButton(value: CancelButtonOptions | CancelButtonSymbolOptions)

设置右侧清除按钮样式。示例请参考[示例2（设置搜索和删除图标）](ts-basic-components-search.md#示例2设置搜索和删除图标)和[示例11（设置symbol类型清除按钮）](ts-basic-components-search.md#示例11设置symbol类型清除按钮)。

Wearable设备上默认图标大小为18fp。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CancelButtonOptions](ts-basic-components-search.md#cancelbuttonoptions12对象说明) | [CancelButtonSymbolOptions](ts-basic-components-search.md#cancelbuttonsymboloptions12对象说明) | 是 | 右侧清除按钮样式。  默认值：  {  style: CancelButtonStyle.INPUT,  icon: {  size: '16vp',  color: '#99ffffff',  src: ' '  }  }  当style为CancelButtonStyle.CONSTANT时，默认显示清除样式。 |

### fontColor10+

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

设置输入文本的字体颜色。fontSize、fontStyle、fontWeight和fontFamily在[textFont](ts-basic-components-search.md#textfont)属性中设置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 输入文本的字体颜色。  默认值：'#FF182431'  Wearable设备上默认值为：'#dbffffff' |

### caretStyle10+

PhonePC/2in1TabletTVWearable

caretStyle(value: CaretStyle)

设置光标样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CaretStyle](ts-text-common.md#caretstyle10) | 是 | 光标样式。  默认值：  {  width: '2.0vp',  color: '#007DFF'  } |

说明

从API version 12开始，此接口支持设置文本手柄颜色，光标和文本手柄颜色保持一致。

### enableKeyboardOnFocus10+

PhonePC/2in1TabletTVWearable

enableKeyboardOnFocus(value: boolean)

设置Search通过点击以外的方式获焦时，是否主动拉起软键盘。

从API version 10开始，获焦默认绑定输入法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | Search获焦时，是否主动拉起软键盘。  true表示主动拉起，false表示不主动拉起。  默认值：true |

### selectionMenuHidden10+

PhonePC/2in1TabletTVWearable

selectionMenuHidden(value: boolean)

设置是否不弹出系统文本选择菜单。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否不弹出系统文本选择菜单。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，不弹出系统文本选择菜单。  设置为false时，弹出系统文本选择菜单。  默认值：false |

### customKeyboard10+

PhonePC/2in1TabletTVWearable

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)

设置自定义键盘。

当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。

自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。

自定义键盘采用覆盖原始界面的方式呈现，当没有开启避让模式或者输入框不需要避让的场景不会对应用原始界面产生压缩或者上提。

自定义键盘无法获取焦点，但是会拦截手势事件。

默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[stopEditing](ts-basic-components-search.md#stopediting10)方法控制键盘关闭。

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

### type11+

PhonePC/2in1TabletTVWearable

type(value: SearchType)

设置输入框类型。

不同的SearchType会拉起对应类型的键盘，同时限制输入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SearchType](ts-basic-components-search.md#searchtype11枚举说明) | 是 | 输入框类型。  默认值：SearchType.NORMAL |

### maxLength11+

PhonePC/2in1TabletTVWearable

maxLength(value: number)

设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 文本的最大输入字符数。  当value<0时，按照默认值处理，不设限制。 |

### enterKeyType12+

PhonePC/2in1TabletTVWearable

enterKeyType(value: EnterKeyType)

设置输入法回车键类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EnterKeyType](ts-basic-components-textinput.md#enterkeytype枚举说明) | 是 | 输入法回车键类型。  默认值：EnterKeyType.Search |

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

### lineHeight12+

PhonePC/2in1TabletTVWearable

lineHeight(value: number | string | Resource)

设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 文本的文本行高。 |

说明

特殊字符字体高度远超出同行的其他字符高度时，文本框出现截断、遮挡、内容相对位置发生变化等不符合预期的显示异常，需要开发者调整组件高度、行高等属性，修改对应的页面布局。

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

### selectedBackgroundColor12+

PhonePC/2in1TabletTVWearable

selectedBackgroundColor(value: ResourceColor)

设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 文本选中底板颜色。 |

### inputFilter12+

PhonePC/2in1TabletTVWearable

inputFilter(value: ResourceStr, error?: Callback< string >)

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。

单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

设置inputFilter且输入的字符不为空字符，会导致设置输入框类型(即type接口)附带的文本过滤效果失效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 正则表达式。 |
| error | Callback< string > | 否 | 正则匹配失败时，返回被过滤的内容。 |

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

需配合[maxFontSize](ts-basic-components-search.md#maxfontsize12)以及布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

minFontSize小于或等于0时，自适应字号不生效，此时按照[textFont](ts-basic-components-search.md#textfont)属性里面size的取值生效，未设置时按照其默认值生效。

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

需配合[minFontSize](ts-basic-components-search.md#minfontsize12)以及布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

maxFontSize小于等于0或者maxFontSize小于minFontSize时，自适应字号不生效，此时按照[textFont](ts-basic-components-search.md#textfont)属性里面size的取值生效，未设置时按照其默认值生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 文本最大显示字号。  单位：[fp](ts-pixel-units.md) |

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
| scale | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | 文本最小的字体缩放倍数，支持undefined类型。  取值范围：[0, 1]  **说明：**  设置的值小于0时，按值为0处理。设置的值大于1，按值为1处理。异常值默认不生效。  使用前需在工程中配置[configuration.json](../harmonyos-guides/app-configuration-file.md#configuration标签)文件和[app.json5](../harmonyos-guides/app-configuration-file.md)文件，具体详见[示例19设置最小字体范围与最大字体范围](ts-basic-components-search.md#示例19设置最小字体范围与最大字体范围)。 |

### maxFontScale18+

PhonePC/2in1TabletTVWearable

maxFontScale(scale: Optional<number | Resource>)

设置文本最大的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | 文本最大的字体缩放倍数，支持undefined类型。  取值范围：[1, +∞)  **说明：**  设置的值小于1时，按值为1处理。异常值默认不生效。  设置maxFontScale属性后，search组件内容最多放大到2倍。  使用前需在工程中配置[configuration.json](../harmonyos-guides/app-configuration-file.md#configuration标签)文件和[app.json5](../harmonyos-guides/app-configuration-file.md)文件，具体详见[示例19设置最小字体范围与最大字体范围](ts-basic-components-search.md#示例19设置最小字体范围与最大字体范围)。 |

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

### selectedDragPreviewStyle23+

PhonePC/2in1TabletTVWearable

selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)

设置搜索框内文本拖拽时的背板样式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SelectedDragPreviewStyle](ts-text-common.md#selecteddragpreviewstyle23对象说明) | undefined | 是 | 文本拖拽时的背板样式。  设置为undefined时：背板颜色跟随主题，浅色模式显示白色，深色模式显示黑色。 |

### dividerColor23+

PhonePC/2in1TabletTVWearable

dividerColor(color: Optional<ColorMetrics>)

设置输入框分割线颜色。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 设置分割线颜色。  默认使用系统的主题色：浅色模式下为0x33000000，显示为浅黑色，深色模式下为0x33FFFFFF，显示为浅白色。 |

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

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 行高是否基于文字实际高度自适应。  true表示行高基于文字实际高度自适应；false表示行高不基于文字实际高度自适应。 |

## IconOptions10+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [Length](ts-types.md#length) | 否 | 是 | 图标尺寸，不支持百分比。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 图标颜色。 |
| src | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标/图片源。 |

## SearchButtonOptions10+对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontSize | [Length](ts-types.md#length) | 否 | 是 | 文本按钮字体大小，不支持百分比。**元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本按钮字体颜色。**元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| autoDisable18+ | Boolean | 否 | 是 | Search无文本内容时按钮置灰且不可点击。  默认值：false  true表示开启按钮置灰功能，false表示不开启。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## CancelButtonStyle10+枚举说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| CONSTANT | 清除按钮常显样式。 |
| INVISIBLE | 清除按钮常隐样式。 |
| INPUT | 清除按钮输入样式。 |

## SearchType11+枚举说明

PhonePC/2in1TabletTVWearable

搜索输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 基本输入模式，无特殊限制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NUMBER | 2 | 纯数字输入模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PHONE\_NUMBER | 3 | 电话号码输入模式。  支持输入数字、空格、+ 、-、\*、#、(、)，长度不限。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| EMAIL | 5 | 邮箱地址输入模式。  支持数字，字母，下划线、小数点、!、#、$、%、&、'、\*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NUMBER\_DECIMAL12+ | 12 | 带小数点的数字输入模式。  支持数字，小数点（只能存在一个小数点）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| URL12+ | 13 | 带URL的输入模式，无特殊限制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ONE\_TIME\_CODE20+ | 14 | 验证码输入模式，无特殊限制。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## CancelButtonOptions12+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [CancelButtonStyle](ts-basic-components-search.md#cancelbuttonstyle10枚举说明) | 否 | 是 | 右侧清除按钮显示状态。 |
| icon | [IconOptions](ts-basic-components-search.md#iconoptions10对象说明) | 否 | 是 | 右侧清除按钮图标。 |

## CancelButtonSymbolOptions12+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [CancelButtonStyle](ts-basic-components-search.md#cancelbuttonstyle10枚举说明) | 否 | 是 | 右侧清除按钮显示状态。 |
| icon | [SymbolGlyphModifier](ts-universal-attributes-text-style.md#symbolglyphmodifier12) | 否 | 是 | 右侧清除按钮Symbol图标。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onSubmit

PhonePC/2in1TabletTVWearable

onSubmit(callback: Callback<string>)

点击搜索图标、搜索按钮或者按下软键盘搜索按钮时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<string> | 是 | 搜索提交回调，其返回值为当前搜索框中输入的文本内容。 |

### onSubmit14+

PhonePC/2in1TabletTVWearable

onSubmit(callback: SearchSubmitCallback)

点击搜索图标、搜索按钮或者按下软键盘搜索按钮时触发该回调事件，提交事件时提供保持Search编辑状态的方法。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SearchSubmitCallback](ts-basic-components-search.md#searchsubmitcallback14) | 是 | 点击搜索图标、搜索按钮或者按下软键盘搜索按钮时的回调事件。 |

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

### onCopy

PhonePC/2in1TabletTVWearable

onCopy(callback:Callback<string>)

进行复制操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<string> | 是 | 复制回调，其返回值为复制的文本内容。 |

### onCut

PhonePC/2in1TabletTVWearable

onCut(callback:Callback<string>)

进行剪切操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<string> | 是 | 剪切回调，其返回值为剪切的文本内容。 |

### onPaste

PhonePC/2in1TabletTVWearable

onPaste(callback:OnPasteCallback )

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

### onEditChange12+

PhonePC/2in1TabletTVWearable

onEditChange(callback: Callback< boolean >)

输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback< boolean > | 是 | 编辑状态改变回调，其返回值为true表示正在输入，false表示无焦点，无法输入文字。 |

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

在搜索框将要绑定输入法前触发该回调。

从API version 22开始，调用[IMEClient](ts-text-common.md#imeclient20对象说明)的[setExtraConfig](ts-text-common.md#setextraconfig22)方法可以设置输入法扩展信息。在绑定输入法成功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。

IMEClient仅在onWillAttachIME执行期间有效，不可进行异步调用。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IMEClient](ts-text-common.md#imeclient20对象说明)> | 是 | 在搜索框将要绑定输入法前触发该回调。 |

## SearchController

PhonePC/2in1TabletTVWearable

Search组件的控制器继承自[TextContentControllerBase](ts-universal-attributes-text-style.md#textcontentcontrollerbase)，涉及的接口有[getTextContentRect](ts-universal-attributes-text-style.md#gettextcontentrect)、[getTextContentLineCount](ts-universal-attributes-text-style.md#gettextcontentlinecount)、[getCaretOffset](ts-universal-attributes-text-style.md#getcaretoffset11)、[addText](ts-universal-attributes-text-style.md#addtext15)、[deleteText](ts-universal-attributes-text-style.md#deletetext15)、[getSelection](ts-universal-attributes-text-style.md#getselection15)、[clearPreviewText](ts-universal-attributes-text-style.md#clearpreviewtext17)、[setStyledPlaceholder](ts-universal-attributes-text-style.md#setstyledplaceholder22)、[deleteBackward](ts-universal-attributes-text-style.md#deletebackward23)。

### 导入对象

```
1. controller: SearchController = new SearchController();
```

### constructor

PhonePC/2in1TabletTVWearable

constructor()

SearchController的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### caretPosition

PhonePC/2in1TabletTVWearable

caretPosition(value: number): void

设置输入光标的位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 从字符串开始到光标所在位置的长度。  当value<0时，按照0处理。当value>字符串长度时，按照字符串长度处理。 |

### stopEditing10+

PhonePC/2in1TabletTVWearable

stopEditing(): void

退出编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setTextSelection12+

PhonePC/2in1TabletTVWearable

setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void;

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取并高亮显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 文本选择区域起始位置，文本框中文字的起始位置为0。  当selectionStart小于0时、按照0处理；当selectionStart大于文字最大长度时、按照文字最大长度处理。 |
| selectionEnd | number | 是 | 文本选择区域结束位置。  当selectionEnd小于0时、按照0处理；当selectionEnd大于文字最大长度时、按照文字最大长度处理。 |
| options | [SelectionOptions](ts-universal-attributes-text-style.md#selectionoptions12对象说明) | 否 | 选中文字时的配置。  默认值：MenuPolicy.DEFAULT。 |

说明

如果selectionStart或selectionEnd被赋值为undefined时，当作0处理。

如果selectionMenuHidden被赋值为true或设备为2in1时，即使options被赋值为MenuPolicy.SHOW，调用setTextSelection也不弹出菜单。

如果选中的文本含有emoji表情时，表情的起始位置包含在设置的文本选中区域内就会被选中。

## SearchSubmitCallback14+

PhonePC/2in1TabletTVWearable

type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void

点击搜索图标、搜索按钮或者按下软键盘搜索按钮时的回调事件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchContent | string | 是 | 当前搜索框中输入的文本内容。 |
| event | [SubmitEvent](ts-basic-components-textinput.md#submitevent11) | 否 | 提交事件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置与获取光标位置）

从API version 8开始，该示例通过[controller](ts-basic-components-search.md#searchcontroller)实现了光标位置的设置与获取的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. @State changeValue: string = '';
6. @State submitValue: string = '';
7. @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 };
8. controller: SearchController = new SearchController();

10. build() {
11. Column({space: 10}) {
12. Text('onSubmit:' + this.submitValue).fontSize(18).margin(15)
13. Text('onChange:' + this.changeValue).fontSize(18).margin(15)
14. Search({ value: this.changeValue, placeholder: 'Type to search...', controller: this.controller })
15. .searchButton('SEARCH')
16. .width('95%')
17. .height(40)
18. .backgroundColor('#F5F5F5')
19. .placeholderColor(Color.Grey)
20. .placeholderFont({ size: 14, weight: 400 })
21. .textFont({ size: 14, weight: 400 })
22. .onSubmit((value: string) => {
23. this.submitValue = value;
24. })
25. .onChange((value: string) => {
26. this.changeValue = value;
27. })
28. .margin(20)
29. Button('Set caretPosition 1')
30. .onClick(() => {
31. // 设置光标位置到输入的第一个字符后
32. this.controller.caretPosition(1);
33. })
34. Button('Get CaretOffset')
35. .onClick(() => {
36. this.positionInfo = this.controller.getCaretOffset();
37. })
38. }.width('100%')
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Tz9Yk_q_Q5e1bePFNW9lNQ/zh-cn_image_0000002558606658.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=F414317F338C2F50E6C13F125BFCAAD1A72F040A3C4615AD39F2338EB3EF3D99)

### 示例2（设置搜索和删除图标）

该示例通过[searchButton](ts-basic-components-search.md#searchbutton)（从API version 8开始）、[searchIcon](ts-basic-components-search.md#searchicon10)（从API version 10开始）、[cancelButton](ts-basic-components-search.md#cancelbutton10)（从API version 10开始）属性展示了设置搜索和删除图标的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. @State changeValue: string = '';
6. @State submitValue: string = '';

8. build() {
9. Column() {
10. Text('onSubmit:' + this.submitValue).fontSize(18).margin(15)
11. Search({ value: this.changeValue, placeholder: 'Type to search...' })
12. .searchButton('SEARCH')
13. .searchIcon({
14. src: $r('sys.media.ohos_ic_public_search_filled')
15. })
16. .cancelButton({
17. style: CancelButtonStyle.CONSTANT,
18. icon: {
19. src: $r('sys.media.ohos_ic_public_cancel_filled')
20. }
21. })
22. .width('90%')
23. .height(40)
24. .maxLength(20)
25. .backgroundColor('#F5F5F5')
26. .placeholderColor(Color.Grey)
27. .placeholderFont({ size: 14, weight: 400 })
28. .textFont({ size: 14, weight: 400 })
29. .onSubmit((value: string) => {
30. this.submitValue = value;
31. })
32. .onChange((value: string) => {
33. this.changeValue = value;
34. })
35. .margin(20)
36. }.width('100%')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/GY89cCEPQ36nTL547wi5Aw/zh-cn_image_0000002589326185.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=B1109E8A40A5B78BF4B0FA2E2BD16043D49B6A22BFDFC36B53A697D5C141EA30)

### 示例3（设置自定义键盘）

该示例通过[customKeyboard](ts-basic-components-search.md#customkeyboard10)（从API version 10开始）属性分别将value中的入参类型设置为[CustomBuilder](ts-types.md#custombuilder8)和[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)，实现了自定义键盘的功能。

从API version 22开始[customKeyboard](ts-basic-components-search.md#customkeyboard10)属性新增了入参类型[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';
3. class BuilderParams {
4. inputValue: string;
5. controller: SearchController;

7. constructor(inputValue: string, controller: SearchController) {
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
36. struct SearchExample {
37. controller: SearchController = new SearchController();
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
50. Search({ controller: this.builderParam.controller, value: this.builderParam.inputValue })
51. .customKeyboard(this.componentContent, { supportAvoidance: this.supportAvoidance })
52. .margin(10).border({ width: 1 }).height('48vp')

54. Text('ComponentContent').margin(10).border({ width: 1 })
55. Search({ controller: this.builderParam.controller, value: this.builderParam.inputValue })
56. .customKeyboard(CustomKeyboardBuilder(this.builderParam), { supportAvoidance: this.supportAvoidance })
57. .margin(10).border({ width: 1 }).height('48vp')
58. }
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/MElj6TicQGCL2A03G7kNBg/zh-cn_image_0000002589246127.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=E27CB5EA6F6E2DE09A322282FDCCDB4CE873DE741954A6A9EAA7DFF47D07DFC2)

### 示例4（设置输入法回车键类型）

该示例通过[enterKeyType](ts-basic-components-search.md#enterkeytype12)（从API version 12开始）属性实现了动态切换输入法回车键的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. @State text: string = '';
6. @State enterTypes: Array<EnterKeyType> = [EnterKeyType.Go, EnterKeyType.Search, EnterKeyType.Send, EnterKeyType.Done, EnterKeyType.Next, EnterKeyType.PREVIOUS, EnterKeyType.NEW_LINE];
7. @State index: number = 0;
8. build() {
9. Column({ space: 20 }) {
10. Search({ placeholder: '请输入文本', value: this.text })
11. .width(380)
12. .enterKeyType(this.enterTypes[this.index])
13. .onChange((value: string) => {
14. this.text = value;
15. })
16. .onSubmit((value: string) => {
17. console.info("trigger search onsubmit" + value);
18. })

20. Button('改变EnterKeyType').onClick(() => {
21. this.index = (this.index + 1) % this.enterTypes.length;
22. })
23. }.width('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/4YDrKtoyR5Kbqcl8dC73Tg/zh-cn_image_0000002558766318.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=31C3446E0F43C0ACF49CAD95AB3AB17B9860342A718C63A14E81A4871CB606AC)

### 示例5（设置文本样式）

从API version 12开始，该示例通过[lineHeight](ts-basic-components-search.md#lineheight12)、[letterSpacing](ts-basic-components-search.md#letterspacing12)、[decoration](ts-basic-components-search.md#decoration12)属性展示了不同样式的文本效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. build() {
6. Row() {
7. Column() {
8. Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)
9. Search({value: 'lineHeight unset'})
10. .border({ width: 1 }).padding(10)
11. Search({value: 'lineHeight 15'})
12. .border({ width: 1 }).padding(10).lineHeight(15)
13. Search({value: 'lineHeight 30'})
14. .border({ width: 1 }).padding(10).lineHeight(30)

16. Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)
17. Search({value: 'letterSpacing 0'})
18. .border({ width: 1 }).padding(5).letterSpacing(0)
19. Search({value: 'letterSpacing 3'})
20. .border({ width: 1 }).padding(5).letterSpacing(3)
21. Search({value: 'letterSpacing -1'})
22. .border({ width: 1 }).padding(5).letterSpacing(-1)

24. Text('decoration').fontSize(9).fontColor(0xCCCCCC)
25. Search({value: 'LineThrough, Red'})
26. .border({ width: 1 }).padding(5)
27. .decoration({type: TextDecorationType.LineThrough, color: Color.Red})
28. Search({value: 'Overline, Red, DOTTED'})
29. .border({ width: 1 }).padding(5)
30. .decoration({type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DOTTED})
31. Search({value: 'Underline, Red, WAVY'})
32. .border({ width: 1 }).padding(5)
33. .decoration({type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY})
34. }.height('90%')
35. }
36. .width('90%')
37. .margin(10)
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/N15BWLrxRLmLG92R5duQPQ/zh-cn_image_0000002558606660.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=18712D1D38F694F0381800BA55DDDDD22ED34C7C0519B047D9BCDC5372F9C929)

### 示例6（设置文字特性效果）

该示例通过[fontFeature](ts-basic-components-search.md#fontfeature12)（从API version 12开始）属性实现了文本在不同文字特性下的展示效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. @State text1: string = 'This is ss01 on : 0123456789';
6. @State text2: string = 'This is ss01 off: 0123456789';

8. build() {
9. Column(){
10. Search({value: this.text1})
11. .margin({top:200})
12. .fontFeature("\"ss01\" on")
13. Search({value: this.text2})
14. .margin({top:10})
15. .fontFeature("\"ss01\" off")
16. }
17. .width("90%")
18. .margin("5%")
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/k1LuNq7mTvy0LRiXO1iQjA/zh-cn_image_0000002589326187.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=A632A8FD4495732F2CCEA9C63CFCB2835E133FFBF5DF2EAC29A78899B99B5734)

### 示例7（自定义键盘避让）

该示例通过[customKeyboard](ts-basic-components-search.md#customkeyboard10)（从API version 10开始）属性配置[KeyboardOptions](ts-basic-components-richeditor.md#keyboardoptions12)（从API version 12开始）接口实现了自定义键盘避让的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. controller: SearchController = new SearchController();
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
31. }
32. .backgroundColor(Color.Gray)
33. }

35. build() {
36. Column() {
37. Row() {
38. Button("20%")
39. .fontSize(24)
40. .onClick(() => {
41. this.height1 = "20%";
42. })
43. Button("80%")
44. .fontSize(24)
45. .margin({ left: 20 })
46. .onClick(() => {
47. this.height1 = "80%";
48. })
49. }
50. .justifyContent(FlexAlign.Center)
51. .alignItems(VerticalAlign.Bottom)
52. .height(this.height1)
53. .width("100%")
54. .padding({ bottom: 50 })

56. Search({ controller: this.controller, value: this.inputValue })// 绑定自定义键盘
57. .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
58. .margin(10)
59. .border({ width: 1 })
60. .onChange((value: string) => {
61. this.inputValue = value;
62. })
63. }
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/asK3yLGPQjWYhwOaltl4Rg/zh-cn_image_0000002589246129.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=66103354FEDFCD6EB1A1AB0289BB026DBDE74CD8D7B07110499FF188746632E5)

### 示例8（设置文本自适应）

从API version 12开始，该示例通过[minFontSize](ts-basic-components-search.md#minfontsize12)、[maxFontSize](ts-basic-components-search.md#maxfontsize12)属性展示了文本自适应字号的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. build() {
6. Row() {
7. Column() {
8. Text('adaptive font').fontSize(9).fontColor(0xCCCCCC)

10. Search({value: 'This is the text without the adaptive font'})
11. .width('80%').height(90).borderWidth(1)
12. Search({value: 'This is the text without the adaptive font'})
13. .width('80%').height(90).borderWidth(1)
14. .minFontSize(4)
15. .maxFontSize(40)
16. }.height('90%')
17. }
18. .width('90%')
19. .margin(10)
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/MDd8H7dVRASYsxft0daBwA/zh-cn_image_0000002558766320.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=D485A58D5EED2C3A750208416295F4682132187F9F4E07F11F590AB26BA0DFA0)

### 示例9（支持插入和删除回调）

从API version 12开始，该示例通过[onWillInsert](ts-basic-components-search.md#onwillinsert12)、[onDidInsert](ts-basic-components-search.md#ondidinsert12)、[onWillDelete](ts-basic-components-search.md#onwilldelete12)、[onDidDelete](ts-basic-components-search.md#ondiddelete12)接口实现了插入和删除的效果。从API version 15开始，通过[onWillChange](ts-basic-components-search.md#onwillchange15)接口展示了文本内容将要发生变化时的具体信息。

```
1. // xxx.ets
2. class ChangeState {
3. changeContent: string = "";
4. changePreviewOffset: number | undefined = 0;
5. changePreviewValue: string | undefined = "";
6. changeTextChangeRangeBeforeX: number | undefined = 0;
7. changeTextChangeRangeBeforeY: number | undefined = 0;
8. changeTextChangeRangeAfterX: number | undefined = 0;
9. changeTextChangeRangeAfterY: number | undefined = 0;
10. changeTextChangeOldContent: string | undefined = "";
11. changeTextChangechangePreviewOffset: number | undefined = 0;
12. changeTextChangechangePreviewValue: string | undefined = "";

14. SetInfo(info: EditableTextChangeValue) {
15. this.changeContent = info.content;
16. this.changePreviewOffset = info.previewText?.offset;
17. this.changePreviewValue = info.previewText?.value;
18. this.changeTextChangeRangeBeforeX = info.options?.rangeBefore.start;
19. this.changeTextChangeRangeBeforeY = info.options?.rangeBefore.end;
20. this.changeTextChangeRangeAfterX = info.options?.rangeAfter.start;
21. this.changeTextChangeRangeAfterY = info.options?.rangeAfter.end;
22. this.changeTextChangeOldContent = info.options?.oldContent;
23. this.changeTextChangechangePreviewOffset = info.options?.oldPreviewText.offset;
24. this.changeTextChangechangePreviewValue = info.options?.oldPreviewText.value;
25. }
26. }

28. @Entry
29. @Component
30. struct SearchExample {
31. @State insertValue: string = "";
32. @State deleteValue: string = "";
33. @State insertOffset: number = 0;
34. @State deleteOffset: number = 0;
35. @State deleteDirection: number = 0;
36. @State changeState1: ChangeState = new ChangeState();
37. @State changeState2: ChangeState = new ChangeState();

39. build() {
40. Row() {
41. Column() {
42. Search({ value: "Search支持插入回调文本" })
43. .height(60)
44. .onWillInsert((info: InsertValue) => {
45. this.insertValue = info.insertValue;
46. return true;
47. })
48. .onWillChange((info: EditableTextChangeValue) => {
49. this.changeState1.SetInfo(info);
50. return true;
51. })
52. .onDidInsert((info: InsertValue) => {
53. this.insertOffset = info.insertOffset;
54. })

56. Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(20)

58. Blank(30)

60. Text("context:" + this.changeState1.changeContent).height(20)
61. Text("previewText-offset:" + this.changeState1.changePreviewOffset).height(20)
62. Text("previewText-value:" + this.changeState1.changePreviewValue).height(20)
63. Text("options-rangeBefore-start:" + this.changeState1.changeTextChangeRangeBeforeX).height(20)
64. Text("options-rangeBefore-end:" + this.changeState1.changeTextChangeRangeBeforeY).height(20)
65. Text("options-rangeAfter-start:" + this.changeState1.changeTextChangeRangeAfterX).height(20)
66. Text("options-rangeAfter-end:" + this.changeState1.changeTextChangeRangeAfterY).height(20)
67. Text("options-oldContent:" + this.changeState1.changeTextChangeOldContent).height(20)
68. Text("options-oldPreviewText-offset:" + this.changeState1.changeTextChangechangePreviewOffset).height(20)
69. Text("options-oldPreviewText-value:" + this.changeState1.changeTextChangechangePreviewValue).height(20)

71. Search({ value: "Search支持删除回调文本b" })
72. .height(60)
73. .onWillDelete((info: DeleteValue) => {
74. this.deleteValue = info.deleteValue;
75. this.deleteDirection = info.direction;
76. return true;
77. })
78. .onWillChange((info: EditableTextChangeValue) => {
79. this.changeState2.SetInfo(info);
80. return true;
81. })
82. .onDidDelete((info: DeleteValue) => {
83. this.deleteOffset = info.deleteOffset;
84. this.deleteDirection = info.direction;
85. })

87. Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(20)
88. Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(20)

90. Blank(30)

92. Text("context:" + this.changeState2.changeContent).height(20)
93. Text("previewText-offset:" + this.changeState2.changePreviewOffset).height(20)
94. Text("previewText-value:" + this.changeState2.changePreviewValue).height(20)
95. Text("options-rangeBefore-start:" + this.changeState2.changeTextChangeRangeBeforeX).height(20)
96. Text("options-rangeBefore-end:" + this.changeState2.changeTextChangeRangeBeforeY).height(20)
97. Text("options-rangeAfter-start:" + this.changeState2.changeTextChangeRangeAfterX).height(20)
98. Text("options-rangeAfter-end:" + this.changeState2.changeTextChangeRangeAfterY).height(20)
99. Text("options-oldContent:" + this.changeState2.changeTextChangeOldContent).height(20)
100. Text("options-oldPreviewText-offset:" + this.changeState2.changeTextChangechangePreviewOffset).height(20)
101. Text("options-oldPreviewText-value:" + this.changeState2.changeTextChangechangePreviewValue).height(20)

103. }.width('100%')
104. }
105. .height('100%')
106. }
107. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/4tpgRzLDSmeIsiuqk8dSgw/zh-cn_image_0000002558606662.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=A22994FC233CA66FD9E9158CCB2CC355CD84343D82BA91069DFFB8137F1A5326)

### 示例10（文本扩展自定义菜单）

从API version 12开始，该示例通过[editMenuOptions](ts-basic-components-search.md#editmenuoptions12)接口实现了文本设置自定义菜单扩展项的文本内容、图标以及回调的功能，同时，可以在[onPrepareMenu](ts-text-common.md#属性-1)（从API version 20开始）回调中，进行菜单数据的设置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. @State text: string = 'Search editMenuOptions';
6. @State endIndex: number = 0;
7. onCreateMenu = (menuItems: Array<TextMenuItem>) => {
8. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
9. let item1: TextMenuItem = {
10. content: 'create1',
11. icon: $r('app.media.startIcon'),
12. id: TextMenuItemId.of('create1'),
13. };
14. let item2: TextMenuItem = {
15. content: 'create2',
16. id: TextMenuItemId.of('create2'),
17. icon: $r('app.media.startIcon'),
18. };
19. menuItems.push(item1);
20. menuItems.unshift(item2);
21. let targetIndex = menuItems.findIndex(item => item.id.equals(TextMenuItemId.AI_WRITER));
22. if (targetIndex !== -1) {
23. menuItems.splice(targetIndex, 1); // 从目标索引删除1个元素
24. }
25. // 从API version 23开始支持TextMenuItemId.autoFill
26. targetIndex = menuItems.findIndex(item => item.id.equals(TextMenuItemId.autoFill));
27. if (targetIndex !== -1) {
28. menuItems.splice(targetIndex, 1); // 从目标索引删除1个元素
29. }
30. return menuItems;
31. }
32. onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
33. if (menuItem.id.equals(TextMenuItemId.of("create2"))) {
34. console.info("拦截 id: create2 start:" + textRange.start + "; end:" + textRange.end);
35. return true;
36. }
37. if (menuItem.id.equals(TextMenuItemId.of("prepare1"))) {
38. console.info("拦截 id: prepare1 start:" + textRange.start + "; end:" + textRange.end);
39. return true;
40. }
41. if (menuItem.id.equals(TextMenuItemId.COPY)) {
42. console.info("拦截 COPY start:" + textRange.start + "; end:" + textRange.end);
43. return true;
44. }
45. if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
46. console.info("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end);
47. return false;
48. }
49. return false;
50. }
51. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
52. onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
53. let item1: TextMenuItem = {
54. content: 'prepare1_' + this.endIndex,
55. icon: $r('app.media.startIcon'),
56. id: TextMenuItemId.of('prepare1'),
57. };
58. menuItems.unshift(item1);
59. return menuItems;
60. }
61. @State editMenuOptions: EditMenuOptions = {
62. onCreateMenu: this.onCreateMenu,
63. onMenuItemClick: this.onMenuItemClick,
64. onPrepareMenu: this.onPrepareMenu
65. };

67. build() {
68. Column() {
69. Search({ value: this.text })
70. .width('95%')
71. .editMenuOptions(this.editMenuOptions)
72. .margin({ top: 100 })
73. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
74. this.endIndex = selectionEnd;
75. })
76. }
77. .width("90%")
78. .margin("5%")
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/5pgMTZPxRRmbsiIoht9UGg/zh-cn_image_0000002589326189.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=9A2492EF6BD1AD8D29D8450BDEAEE6F5473D916EB8EEE6F96D5C4C0484322C23)

### 示例11（设置symbol类型清除按钮）

从API version 10开始，该示例通过[searchIcon](ts-basic-components-search.md#searchicon10)、[cancelButton](ts-basic-components-search.md#cancelbutton10)属性展示了自定义右侧symbol类型清除按钮样式的效果。

```
1. // xxx.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SearchExample {
7. controller: SearchController = new SearchController();
8. @State changeValue: string = '';
9. @State submitValue: string = '';

11. build() {
12. Column() {
13. Search({ value: this.changeValue, placeholder: 'Type to search...', controller: this.controller })
14. .searchIcon(new SymbolGlyphModifier($r('sys.symbol.magnifyingglass')).fontColor([Color.Red]))
15. .cancelButton({
16. style: CancelButtonStyle.CONSTANT,
17. icon: new SymbolGlyphModifier($r('sys.symbol.xmark')).fontColor([Color.Green])
18. })
19. .searchButton('SEARCH')
20. .width('95%')
21. .height(40)
22. .backgroundColor('#F5F5F5')
23. .placeholderColor(Color.Grey)
24. .placeholderFont({ size: 14, weight: 400 })
25. .textFont({ size: 14, weight: 400 })
26. .margin(10)
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/WRJr9o8TS6WMZxLAOYjFPw/zh-cn_image_0000002589246131.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=115BC65832C20504C5B49BF73D271E0BC43A1018DC45839B58D5CD328362133C)

### 示例12（设置文本是否可复制）

从API version 9开始，该示例通过[copyOption](ts-basic-components-search.md#copyoption9)属性展示如何设置文本是否可复制。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct SearchExample {
6. controller: SearchController = new SearchController();
7. @State copyValue: string = '';
8. @State cutValue: string = '';

10. build() {
11. Column({ space: 3 }) {
12. Text("copy: " + this.copyValue)
13. Text("cut:" + this.cutValue)
14. Search({ value: 'Search CopyOption:None', controller: this.controller })
15. .width('95%')
16. .height(40)
17. .copyOption(CopyOptions.None)
18. .onCopy((value: string) => {
19. this.copyValue = value;
20. })
21. .onCut((value: string) => {
22. this.cutValue = value;
23. })
24. Search({ value: 'Search CopyOption:InApp', controller: this.controller })
25. .width('95%')
26. .height(40)
27. .copyOption(CopyOptions.InApp)
28. .onCopy((value: string) => {
29. this.copyValue = value;
30. })
31. .onCut((value: string) => {
32. this.cutValue = value;
33. })
34. Search({ value: 'Search CopyOption:LocalDevice', controller: this.controller })
35. .width('95%')
36. .height(40)
37. .copyOption(CopyOptions.LocalDevice)
38. .onCopy((value: string) => {
39. this.copyValue = value;
40. })
41. .onCut((value: string) => {
42. this.cutValue = value;
43. })
44. }
45. .width('100%')
46. .height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/jM896MlkQMa3JmtcMukX0w/zh-cn_image_0000002558766322.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=9B34FC8C4D8FFD36DADF1AEB70059440E61638EE32689CA4405E539175DE0298)

### 示例13（设置文本水平对齐/光标样式/选中背景色）

该示例通过[textAlign](ts-basic-components-search.md#textalign9)（从API version 9开始）、[caretStyle](ts-basic-components-search.md#caretstyle10)（从API version 10开始）、[selectedBackgroundColor](ts-basic-components-search.md#selectedbackgroundcolor12)（从API version 12开始）属性展示如何设置文本的水平对齐、光标样式和选中背景色。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct SearchExample {
6. controller: SearchController = new SearchController();

8. build() {
9. Column({ space: 3 }) {
10. Search({ value: 'Search textAlign sample', controller: this.controller })
11. .width('95%')
12. .height(40)
13. .stopBackPress(true)
14. .textAlign(TextAlign.Center)
15. .caretStyle({ width: 3, color: Color.Green })
16. .selectedBackgroundColor(Color.Gray)
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/2OUrrSPDSIWfcaDjstWnQw/zh-cn_image_0000002558606664.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=8C6292FFBBB69C22F28FCDD2D664EFC7AA4B800BFE43CF2970B60861B13AC83F)

### 示例14（设置默认获焦并拉起软键盘）

该示例通过[defaultFocus](ts-universal-attributes-focus.md#defaultfocus9)（从API version 9开始）、[enableKeyboardOnFocus](ts-basic-components-search.md#enablekeyboardonfocus10)（从API version 10开始）属性展示如何设置默认获焦并拉起软键盘。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct SearchExample {
6. controller: SearchController = new SearchController();
7. @State value: string = 'false';

9. build() {
10. Column({ space: 3 }) {
11. Text('editing: ' + this.value)
12. Search({ placeholder: 'please enter...', controller: this.controller })
13. .width('95%')
14. .height(40)
15. .defaultFocus(true)
16. .enableKeyboardOnFocus(true)
17. .enablePreviewText(true)
18. .enableHapticFeedback(true)
19. .onEditChange((data: boolean) => {
20. this.value = data ? 'true' : 'false';
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/yFNc0SjqRemP1_c-sZYx-Q/zh-cn_image_0000002589326191.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=D35976EB54298AD8B3D2B75F01CBE738DA81A41FDBBBE32D94256550CFE21A1E)

### 示例15（关闭系统文本选择菜单）

该示例通过[selectionMenuHidden](ts-basic-components-search.md#selectionmenuhidden10)（从API version 10开始）属性展示如何关闭系统文本选择菜单。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct SearchExample {
6. controller: SearchController = new SearchController();

8. build() {
9. Column({ space: 3 }) {
10. Search({ value: '123456', controller: this.controller })
11. .width('95%')
12. .height(40)
13. .type(SearchType.NUMBER)
14. .selectionMenuHidden(true)
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/E9WBgPfgQ5G2CmNfpfdSKw/zh-cn_image_0000002589246133.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=E98C25C89CE472789D86B4B6E620700B3A74ED26D5F8E7B35C46D965E35CA370)

### 示例16（对输入的文本进行过滤）

从API version 12开始，该示例通过[inputFilter](ts-basic-components-search.md#inputfilter12)属性展示如何对输入的文本进行内容的过滤，以限制输入内容。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct SearchExample {
6. controller: SearchController = new SearchController();
7. @State filterValue: string = '';

9. build() {
10. Column({ space: 3 }) {
11. Text('Filter:' + this.filterValue)
12. Search({ placeholder: 'please enter...', controller: this.controller })
13. .width('95%')
14. .height(40)
15. .textIndent(5)
16. .halfLeading(true)
17. .inputFilter('[a-z]', (filterValue: string) => {
18. this.filterValue = filterValue;
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/b_zyDp4JS9OjrrV-3q6ZcA/zh-cn_image_0000002558766324.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=B6720E6AAAD10CA10B4116EDB6AFEBE0014D1FCC68CD7229AFECFE3A5513B7DD)

### 示例17（设置选中指定区域的文本内容）

该示例通过[setTextSelection](ts-basic-components-search.md#settextselection12)（从API version 12开始）方法展示如何设置选中指定区域的文本内容以及菜单的显隐策略。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct SearchExample {
6. controller: SearchController = new SearchController();
7. @State startIndex: number = 0;
8. @State endIndex: number = 0;

10. build() {
11. Column({ space: 3 }) {
12. Text('Selection start:' + this.startIndex + ' end:' + this.endIndex)
13. Search({ value: 'Hello World', controller: this.controller })
14. .width('95%')
15. .height(40)
16. .minFontScale(1)
17. .maxFontScale(1.5)
18. .defaultFocus(true)
19. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
20. this.startIndex = selectionStart;
21. this.endIndex = selectionEnd;
22. })

24. Button('Selection [0,3]')
25. .onClick(() => {
26. this.controller.setTextSelection(0, 3, { menuPolicy: MenuPolicy.SHOW });
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Xjy8CwPZRQ-eoVdaJ9kdqg/zh-cn_image_0000002558606666.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=3ABD6EB52024D3B65DFB617A9CB3AE3D2319AE3B1D96B48E5520D64362EDE159)

### 示例18（设置文本滚动事件）

从API version 10开始，该示例通过[onContentScroll](ts-basic-components-search.md#oncontentscroll10)事件展示如何设置文本滚动事件的回调。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct SearchExample {
6. controller: SearchController = new SearchController();
7. @State offsetX: number = 0;
8. @State offsetY: number = 0;

10. build() {
11. Column({ space: 3 }) {
12. Text('offset x:' + this.offsetX + ' y:' + this.offsetY)
13. Search({ value: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', controller: this.controller })
14. .width(200)
15. .height(40)
16. .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
17. this.offsetX = totalOffsetX;
18. this.offsetY = totalOffsetY;
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Tvc1ErObRYWGsEBKvzDdeQ/zh-cn_image_0000002589326193.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=34D41C7F3FCBF64E581B3281C14E61471D91ECDB008C5672BD72941B1A4C9B36)

### 示例19（设置最小字体范围与最大字体范围）

从API version 18开始，该示例通过[minFontScale](ts-basic-components-search.md#minfontscale18)、[maxFontScale](ts-basic-components-search.md#maxfontscale18)设置字体显示最小与最大范围。调整系统字体大小后，文本字体大小不会超过[minFontScale](ts-basic-components-search.md#minfontscale18)、[maxFontScale](ts-basic-components-search.md#maxfontscale18)设置的范围。如下示例展示了Search组件在不同的字体大小限制条件下，调整系统字体后的放大缩小效果。

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
4. struct SearchExample {
5. @State minFontScale: number = 1.0;
6. @State maxFontScale: number = 1.0;
7. @State minFontScale2: number = 0.5;
8. @State maxFontScale2: number = 2.0;

10. build() {
11. Column() {
12. Column() {
13. Text("系统字体变大变小，变大变小aaaaaaaAAAAAA")
14. Blank(30)
15. Text("minFontScale = " + this.minFontScale)
16. Text("maxFontScale = " + this.maxFontScale)
17. Search({
18. placeholder: 'The text area can hold an unlimited amount of text. input your word...',
19. })
20. .minFontScale(this.minFontScale) // 设置最小字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
21. .maxFontScale(this.maxFontScale) // 设置最大字体缩放倍数，参数为undefined则跟随系统默认倍数缩放

23. Blank(30)

25. Text("minFontScale = " + this.minFontScale2)
26. Text("maxFontScale = " + this.maxFontScale2)
27. Search({
28. placeholder: 'The text area can hold an unlimited amount of text. input your word...',
29. })
30. .minFontScale(this.minFontScale2) // 设置最小字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
31. .maxFontScale(this.maxFontScale2) // 设置最大字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
32. }.width('100%')
33. }
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/9i6tlVYCStqIXGuMe0cRrg/zh-cn_image_0000002589246135.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=48001D8B33874C244B077E8AABB9C2F51A52F8AFCB503067E32D6E840FFBB373) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/qjUaGNpRTIev2_mX7TN8Bg/zh-cn_image_0000002558766326.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=FFFB3C8FAB7AF9FF4CE298089BFE14536CDF4307B5DE1BD2B61BAB15C2A279BC)

### 示例20（设置文本描边）

从API version 20开始，该示例通过[strokeWidth](ts-basic-components-search.md#strokewidth20)和[strokeColor](ts-basic-components-search.md#strokecolor20)属性设置文本的描边宽度及颜色。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SearchExample {
7. build() {
8. Row() {
9. Column() {
10. Text('stroke feature').fontSize(9).fontColor(0xCCCCCC)

12. Search({ value: 'Text without stroke' })
13. .width('100%')
14. .height(60)
15. .borderWidth(1)
16. .minFontSize(40)
17. .maxFontSize(40)
18. Search({ value: 'Text with stroke' })
19. .width('100%')
20. .height(60)
21. .borderWidth(1)
22. .minFontSize(40)
23. .maxFontSize(40)
24. .strokeWidth(LengthMetrics.px(-3.0))
25. .strokeColor(Color.Red)
26. Search({ value: 'Text with stroke' })
27. .width('100%')
28. .height(60)
29. .borderWidth(1)
30. .minFontSize(40)
31. .maxFontSize(40)
32. .strokeWidth(LengthMetrics.px(3.0))
33. .strokeColor(Color.Red)
34. }.height('90%')
35. }
36. .width('90%')
37. .margin(10)
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/-FRse0HDQvWtux5oXhulLA/zh-cn_image_0000002558606668.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=3DAB9F6E927A7B4AD241A07C79AE9F44E900CBED2CBC9F2DE71BA390A7C68792)

### 示例21（设置中西文自动间距）

从API version 20开始，该示例通过[enableAutoSpacing](ts-basic-components-search.md#enableautospacing20)属性设置中西文自动间距。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. build() {
6. Row() {
7. Column() {
8. Text('开启中西文自动间距').margin(5)
9. Search({value: '中西文Auto Spacing自动间距'})
10. .enableAutoSpacing(true)
11. Text('关闭中西文自动间距').margin(5)
12. Search({value: '中西文Auto Spacing自动间距'})
13. .enableAutoSpacing(false)
14. }.height('100%')
15. }
16. .width('60%')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/sGcXnh-zTDSrsnGCScjThA/zh-cn_image_0000002589326195.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=B2CADC3675166EA27F3B8DB175E81F17C6C211AA70C606CE5ED65690C5171691)

### 示例22（设置placeholder富文本样式）

从API version 22开始，该示例通过[setStyledPlaceholder](ts-universal-attributes-text-style.md#setstyledplaceholder22)接口设置placeholder富文本样式。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SearchExample {
7. styledString: MutableStyledString =
8. new MutableStyledString("输入框富文本：文本",
9. [
10. {
11. start: 0,
12. length: 7,
13. styledKey: StyledStringKey.FONT,
14. styledValue: new TextStyle({
15. fontColor: Color.Orange,
16. fontSize: LengthMetrics.fp(24)
17. })
18. },
19. {
20. start: 7,
21. length: 4,
22. styledKey: StyledStringKey.FONT,
23. styledValue: new TextStyle({
24. fontColor: Color.Gray,
25. fontSize: LengthMetrics.fp(20),
26. strokeWidth: LengthMetrics.px(-5),
27. strokeColor: Color.Black,
28. })
29. },
30. {
31. start: 0,
32. length: 1,
33. styledKey: StyledStringKey.PARAGRAPH_STYLE,
34. styledValue: new ParagraphStyle({
35. textVerticalAlign: TextVerticalAlign.CENTER
36. })
37. }
38. ]);
39. controller: SearchController = new SearchController();

41. aboutToAppear() {
42. this.controller.setStyledPlaceholder(this.styledString)
43. }

45. build() {
46. Scroll() {
47. Column() {
48. Text("Search placeholder富文本")
49. .fontSize(8)
50. Search({
51. controller: this.controller
52. })
53. .textFont({ size: 24 })
54. .margin(10)
55. }
56. .width('100%')
57. }
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/P1RriphBTVa7nOs5NX0xYQ/zh-cn_image_0000002589246137.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=D3FF497680C48E8AE02702AF3D25A15C128C5B4F163CDD1764EC14B7EE7E6DB1)

### 示例23（设置输入法扩展信息）

从API version 22开始，该示例通过[IMEClient](ts-text-common.md#imeclient20对象说明)的setExtraConfig设置输入法扩展信息。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. build() {
6. Column() {
7. Search({ value: '拉起输入法前执行onWillAttachIME回调' })
8. .onWillAttachIME((client: IMEClient) => {
9. client.setExtraConfig({
10. customSettings: {
11. name: "Search", // 自定义属性
12. id: client.nodeId // 自定义属性
13. }
14. })
15. })
16. }.height('100%')
17. }
18. }
```

### 示例24（设置输入框分割线颜色）

从API version 23开始，该示例通过[dividerColor](ts-basic-components-search.md#dividercolor23)接口设置输入框分割线颜色。

```
1. // xxx.ets
2. import { ColorMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SearchExample {
7. @State colorTypeRGB: ColorMetrics = ColorMetrics.numeric(0x00FF00);
8. @State colorTypeARGB: ColorMetrics = ColorMetrics.numeric(0x3300FF00);
9. @State colorTypeColorWithSpace: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 1.0, 0, 1.0);
10. @State colorTypeRGBA: ColorMetrics = ColorMetrics.rgba(255, 0, 0, 1.0);
11. // 需要替换为开发者所需的资源文件
12. @State colorTypeRes: ColorMetrics = ColorMetrics.resourceColor($r('app.color.color'));
13. @State colorType: ColorMetrics[] =
14. [this.colorTypeRGB, this.colorTypeARGB, this.colorTypeColorWithSpace, this.colorTypeRGBA, this.colorTypeRes];
15. @State colorTypeName: string[] =
16. ["colorTypeRGB", "colorTypeARGB", "colorTypeColorWithSpace", "colorTypeRGBA", "colorTypeRes"];
17. @State count: number = 0;

19. build() {
20. Column() {
21. Blank(30)
22. Search({ value: "Input search text" })
23. .searchButton("SEARCH", { fontSize: '14vp' })
24. .dividerColor(this.colorType[this.count])
25. Button("Change ColorType: " + this.colorTypeName[this.count]).onClick(() => {
26. this.count = (this.count + 1) % (this.colorType.length)
27. })
28. .fontSize('14vp')
29. .width('100%')
30. }
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/KgE86EzpR-SOqKTVFGRvBw/zh-cn_image_0000002558766328.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=523AE5D4490AB656C4ED9A1B15DC82C5ADAACA3FF5A1536364C7506637D87808)

### 示例25（设置行首标点压缩）

该示例通过[compressLeadingPunctuation](ts-basic-components-search.md#compressleadingpunctuation23)接口设置行首标点压缩，左侧有间距的标点符号位于行首时，标点会直接压缩间距至左侧边界。

从API version 23开始，支持compressLeadingPunctuation接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column(){
7. Search({ value: "\u300C行首标点压缩打开" })
8. .compressLeadingPunctuation(true)
9. .margin(5)
10. .textFont({size:30})
11. .width("90%")
12. Search({ value: "\u300C行首标点压缩关闭" })
13. .compressLeadingPunctuation(false)
14. .textFont({size:30})
15. .width("90%")
16. }
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/lHyrLy9dRl2Np_N_RIKi0A/zh-cn_image_0000002558606670.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=507AD501BD2781AFFA850608376B50CDD04FB325378D276CC3559CA99C344F29)

### 示例26（设置自适应间距）

该示例通过[includeFontPadding](ts-basic-components-search.md#includefontpadding23)接口增加首行尾行间距和[fallbackLineSpacing](ts-basic-components-search.md#fallbacklinespacing23)接口设置自适应行间距。

从API version 23开始，新增[includeFontPadding](ts-basic-components-search.md#includefontpadding23)和[fallbackLineSpacing](ts-basic-components-search.md#fallbacklinespacing23)接口。

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
13. Search({
14. value: this.displayText,
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/I3JHTARLRtmTX2HlV33gFw/zh-cn_image_0000002589326197.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=50CA180CB7721953DB25C39CE0EA5660318E57CB90B5B5DEBBC56BA17D722A24)

### 示例27（设置文本拖拽时的背板样式）

该示例通过[selectedDragPreviewStyle](ts-basic-components-search.md#selecteddragpreviewstyle23)接口设置文本拖拽时的背板样式。

从API version 23开始，新增selectedDragPreviewStyle接口。

```
1. @Entry
2. @Component
3. struct SearchTest {
4. build() {
5. Column() {
6. Search({ value: 'HelloWorld', placeholder: 'please input words' })
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/pQl2OK12Q5ew2rOUbrdbTw/zh-cn_image_0000002589246139.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=6D45D55835102EB0AC3BE6A15C5EC436E8D2F19A43131EEB91819B350EBBBF06)

### 示例28（删除文本框内的最后一个字符）

该示例通过调用[deleteBackward](ts-universal-attributes-text-style.md#deletebackward23)接口删除文本框内最后一个字符。

从API version 23开始，新增[deleteBackward](ts-universal-attributes-text-style.md#deletebackward23)接口。

```
1. @Entry
2. @Component
3. struct Page {
4. controller: SearchController = new SearchController();

6. build() {
7. Column() {
8. Search({ placeholder: '搜索框示例', controller: this.controller })
9. Button('Delete backward')
10. .onClick(() => {
11. this.controller.deleteBackward();
12. })
13. }
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/6Ob9AAc-SUGpxFCF24Hj9w/zh-cn_image_0000002558766330.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=1A8A8A358B5BBF3959B9261C4D84B7F6832B4908C06AE6C4C128999B1BC00CDB)

### 示例29（设置文本排版方向）

该示例通过[textDirection](ts-basic-components-search.md#textdirection23)接口设置文本排版方向。

从API version 23开始，新增textDirection接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. @State text: string = 'Search文本排版方向示例';

7. build() {
8. Column({ space: 3 }) {
9. Text('Search文本排版方向RTL，布局方向default')
10. .fontSize(12).width('90%').margin(5)
11. Search({ value: this.text })
12. .width('95%')
13. .height(40)
14. .textDirection(TextDirection.RTL)
15. Text('Search文本排版方向RTL，布局方向default，文本水平方向对齐方式LEFT')
16. .fontSize(12).width('90%').margin(5)
17. Search({ value: this.text })
18. .width('95%')
19. .height(40)
20. .textDirection(TextDirection.RTL)
21. .textAlign(TextAlign.LEFT)
22. Text('Search文本排版方向LTR，布局方向RTL')
23. .fontSize(12).width('90%').margin(5)
24. Search({ value: this.text })
25. .width('95%')
26. .height(40)
27. .textDirection(TextDirection.LTR)
28. .direction(Direction.Rtl)
29. }
30. .width('100%')
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/_INmiHgeRQeuGbJ8jlOhfg/zh-cn_image_0000002558606672.png?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=510D5D3144118065E88E945FD97F4C023DC4CF71E911303A87AB35D0D8F21709)

### 示例30（将指定范围的文字滚动到可视区内）

本示例通过[scrollToVisible](ts-universal-attributes-text-style.md#scrolltovisible23)将可视区外的文本滚动到可视区内。

从API version 23开始，新增scrollToVisible接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SearchExample {
5. @State text: string = '12345678912345678912346789123456789123456789012121214521';
6. controller: SearchController = new SearchController();

8. build() {
9. Column() {
10. Search({ value: this.text, controller: this.controller })
11. .width(336)
12. .height(56)
13. Button("滚动文本到可视区").onClick(()=> {
14. this.controller.scrollToVisible({ start: 22, end: 30})
15. })
16. }.width('100%').height('100%').backgroundColor('#F1F3F5')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/jQGLaKv6SymA0WEEEK1Qmg/zh-cn_image_0000002589326199.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055206Z&HW-CC-Expire=86400&HW-CC-Sign=F1EBD1DB5F1A3A1277ADC6977987AD593F4F323EF1567D5D0EF71970E2497BC9)
