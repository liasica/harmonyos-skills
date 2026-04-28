---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string
title: 属性字符串
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > 属性字符串
category: harmonyos-references
scraped_at: 2026-04-28T08:01:55+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e4354695978299113172d45fdaed0167d2a191548d4a081dd88cdf27e96a50a0
---

方便灵活应用文本样式的对象，可通过[TextController](ts-basic-components-text.md#textcontroller11)中的[setStyledString](ts-basic-components-text.md#setstyledstring12)方法与Text组件绑定，可通过[RichEditorStyledStringController](ts-basic-components-richeditor.md#richeditorstyledstringcontroller12)中的[setStyledString](ts-basic-components-richeditor.md#setstyledstring12)方法与[RichEditor](ts-basic-components-richeditor.md)组件绑定。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

从API version 20开始，支持通过[getParagraphs](arkts-apis-uicontext-measureutils.md#getparagraphs20)获取属性字符串的文本布局信息。

属性字符串目前不支持在worker线程中使用。

属性字符串通过controller绑定时，需要等待布局完成后，绑定生效。当[measure](js-apis-arkui-framenode.md#measure12)和setStyledString同时使用，开发者需要通过[@ohos.arkui.inspector (布局回调)](js-apis-arkui-inspector.md)判断布局完成，再绑定属性字符串。

## 规则说明

PhonePC/2in1TabletTVWearable

* 当组件样式和属性字符串中的样式冲突时，冲突部分以属性字符串设置的样式为准，未冲突部分则生效组件的样式。
* 当属性字符串和[Text](ts-basic-components-text.md)子组件冲突时，属性字符串优先级高，即当Text组件中绑定了属性字符串，忽略Text组件下包含[Span](ts-basic-components-span.md)等子组件的情况。
* 不支持[@State](../harmonyos-guides/arkts-state.md)修饰。
* 建议将StyledString定义为成员变量，从而避免应用退后台后被销毁。
* 不支持在[loadContent()](arkts-apis-window-window.md#loadcontent9)之前创建。

## StyledString

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)

属性字符串的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [ImageAttachment](ts-universal-styled-string.md#imageattachment) | [CustomSpan](ts-universal-styled-string.md#customspan) | 是 | 属性字符串文本内容。  **说明：**  当value的类型为ImageAttachment或CustomSpan时，styles参数不生效。  需要设置styles时，通过[setStyle](ts-universal-styled-string.md#setstyle)等方法实现。 |
| styles | Array<[StyleOptions](ts-universal-styled-string.md#styleoptions对象说明)> | 否 | 属性字符串初始化选项。  **说明：**  start为异常值时，按默认值0处理；  当length为异常值时，length等于属性字符串在start后的实际长度；  当StyledStringKey与StyledStringValue不匹配时，styles不生效。 |

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | 属性字符串字符的长度。  **说明：**  属性字符串中的ImageAttachment和CustomSpan长度都计为1。 |

### getString

PhonePC/2in1TabletTVWearable

getString(): string

获取字符串信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 属性字符串文本内容。  **说明：**  当属性字符串中包含图片或[CustomSpan](ts-universal-styled-string.md#customspan)时，其返回的结果用空格表示。 |

### equals

PhonePC/2in1TabletTVWearable

equals(other: StyledString): boolean

判断两个属性字符串是否相等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | StyledString类型的比较对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 两个属性字符串是否相等。  true表示相等，false表示不相等。  **说明：**  当属性字符串的文本及样式均一致，视为相等。  不比较[GestureStyle](ts-universal-styled-string.md#gesturestyle)，当属性字符串配置了不同事件，文本和其他样式相同时，亦视为相等。  当比较[CustomSpan](ts-universal-styled-string.md#customspan)或[LeadingMarginSpan](ts-universal-styled-string.md#leadingmarginspan22)时，比较的是地址，地址相等，视为相等。 |

### subStyledString

PhonePC/2in1TabletTVWearable

subStyledString(start: number, length?: number): StyledString

获取属性字符串的子属性字符串。不能超出属性字符串的长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 子属性字符串开始位置的下标。 |
| length | number | 否 | 子属性字符串的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StyledString](ts-universal-styled-string.md#styledstring) | 子属性字符串。  **说明：**  当start为合法入参时，length的默认值是被查询属性字符串对象的长度与start的值的差。  当start和length越界或者必填传入undefined时，会抛出异常。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### getStyles

PhonePC/2in1TabletTVWearable

getStyles(start: number, length: number, styledKey?: StyledStringKey): Array<SpanStyle>

获取指定范围属性字符串的样式集合。不能超出属性字符串的长度。

该接口仅返回开发者设置的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 指定范围属性字符串的下标。 |
| length | number | 是 | 指定范围属性字符串的长度。 |
| styledKey | [StyledStringKey](ts-universal-styled-string.md#styledstringkey枚举说明) | 否 | 指定范围属性字符串样式的枚举值。  **说明：**  当不传入该参数时默认获取开发者设置的[StyledStringKey](ts-universal-styled-string.md#styledstringkey枚举说明)所有枚举值样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SpanStyle](ts-universal-styled-string.md#spanstyle对象说明)> | 各样式对象的数组。  **说明：**  当指定范围属性字符串未设置任何样式，则返回空数组。  当start和length越界或者必填传入undefined时，会抛出异常；  当styledKey传入异常值或undefined时，会抛出异常。  当styledKey为CustomSpan时，返回的是创建CustomSpan时传入的样式对象，即修改该样式对象也会影响实际的显示效果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### fromHtml

PhonePC/2in1TabletTVWearable

static fromHtml(html: string): Promise<StyledString>

将HTML格式字符串转换成属性字符串，当前支持转换的HTML标签范围：<p>、<span>、<img>、<br>、<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>。支持将标签中的style属性样式转换成对应的属性字符串样式。

使用方法参考[示例12（fromHtml和toHtml互相转换）](ts-universal-styled-string.md#示例12fromhtml和tohtml互相转换)。

| 标签名称 | 说明 |
| --- | --- |
| <p> | 段落，分隔文本段落 |
| <span> | 行内文本，支持样式设置。API version 17及之前，<span>设置的background-color属性转换不生效。 |
| <img> | 插入图片 |
| <strong> | 加粗文本 |
| <br>20+ | 换行 |
| <b>20+ | 加粗文本 |
| <a>20+ | 超链接 |
| <i>20+ | 斜体文本 |
| <em>20+ | 斜体文本 |
| <s>20+ | 删除线（中划线） |
| <u>20+ | 下划线 |
| <del>20+ | 删除线（中划线） |
| <sup>20+ | 上标文本 |
| <sub>20+ | 下标文本 |

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| html | string | 是 | html格式的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[StyledString](ts-universal-styled-string.md#styledstring)> | 属性字符串。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[属性字符串错误码](errorcode-styled-string.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 170001 | Convert Error. |

### toHtml14+

PhonePC/2in1TabletTVWearable

static toHtml(styledString: StyledString): string

将属性字符串转换成HTML格式字符串。支持转换的属性字符串[StyledStringKey](ts-universal-styled-string.md#styledstringkey枚举说明)包括：StyledStringKey.FONT、StyledStringKey.DECORATION、StyledStringKey.LETTER\_SPACING、StyledStringKey.TEXT\_SHADOW、StyledStringKey.LINE\_HEIGHT、StyledStringKey.IMAGE。

使用方法参考[示例12（fromHtml和toHtml互相转换）](ts-universal-styled-string.md#示例12fromhtml和tohtml互相转换)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styledString | StyledString | 是 | 属性字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | HTML格式字符串。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

## MutableStyledString

PhonePC/2in1TabletTVWearable

继承于[StyledString](ts-universal-styled-string.md#styledstring)类。

说明

当start和length越界或者必填传入undefined时，会抛出异常；

当styledKey和styledValue传入异常值或者两者对应关系不匹配时，会抛出异常。

### replaceString

PhonePC/2in1TabletTVWearable

replaceString(start: number , length: number , other: string): void

替换指定范围的字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 指定范围的下标。 |
| length | number | 是 | 指定范围的长度。 |
| other | string | 是 | 替换的新文本内容。  **说明：**  替换的字符串使用的是start位置字符的样式。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### insertString

PhonePC/2in1TabletTVWearable

insertString(start: number , other: string): void

插入字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 插入位置的下标。 |
| other | string | 是 | 插入的新文本内容。  **说明：**  插入的字符串使用的是start-1位置字符的样式。若start-1位置字符未设置样式，则使用start位置字符样式。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### removeString

PhonePC/2in1TabletTVWearable

removeString(start: number , length: number): void

移除指定范围的字符串。

当属性字符串中包含图片或[CustomSpan](ts-universal-styled-string.md#customspan)时，同样生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 指定范围的下标。 |
| length | number | 是 | 指定范围的长度。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### replaceStyle

PhonePC/2in1TabletTVWearable

replaceStyle(spanStyle: SpanStyle): void

替换指定范围内容为指定类型新样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spanStyle | [SpanStyle](ts-universal-styled-string.md#spanstyle对象说明) | 是 | 样式对象。  **说明：**  默认清空原有样式，替换为新样式。  当SpanStyle的styledKey为IMAGE或CUSTOM\_SPAN时，只有当start的位置当前是image或CustomSpan且长度为1，才会生效，其余情况无效果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### setStyle

PhonePC/2in1TabletTVWearable

setStyle(spanStyle: SpanStyle): void

为指定范围内容设置指定类型新样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spanStyle | [SpanStyle](ts-universal-styled-string.md#spanstyle对象说明) | 是 | 样式对象。  默认不清空原有样式，叠加新样式。如果StyledStringValue类型相同，则新样式将覆盖旧样式。  当SpanStyle的styledKey为IMAGE或CUSTOM\_SPAN时，只有当start的位置当前是image或CustomSpan且长度为1，才会生效，其余情况无效果。 |

说明

样式的最小颗粒度是StyledStringValue，如果设置了多个相同的StyledStringValue，只有最后一次设置会生效。如设置两个属性不同的TextStyle，则只有第二次设置的TextStyle生效。

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

### removeStyle

PhonePC/2in1TabletTVWearable

removeStyle(start: number , length: number , styledKey: StyledStringKey): void

清除指定范围内容的指定类型样式。

被清空样式类型对象属性使用的是对应[Text](ts-basic-components-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

当属性字符串中包含图片时，同样生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 指定范围开始位置的下标。 |
| length | number | 是 | 指定范围的长度。 |
| styledKey | [StyledStringKey](ts-universal-styled-string.md#styledstringkey枚举说明) | 是 | 样式类型枚举值。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### removeStyles

PhonePC/2in1TabletTVWearable

removeStyles(start: number , length: number): void

清除指定范围内容的所有样式。

被清空样式类型对象属性使用的是对应[Text](ts-basic-components-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

当属性字符串中包含图片时，同样生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 指定范围开始位置的下标。 |
| length | number | 是 | 指定范围的长度。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### clearStyles

PhonePC/2in1TabletTVWearable

clearStyles(): void

清除属性字符串对象的所有样式。

被清空样式类型对象属性使用的是对应[Text](ts-basic-components-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### replaceStyledString

PhonePC/2in1TabletTVWearable

replaceStyledString(start: number , length: number , other: StyledString): void

替换指定范围为新的属性字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 指定范围开始位置的下标。 |
| length | number | 是 | 指定范围的长度。 |
| other | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | 新的属性字符串对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### insertStyledString

PhonePC/2in1TabletTVWearable

insertStyledString(start: number , other: StyledString): void

在指定位置插入新的属性字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 开始插入位置的下标。 |
| other | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | 新的属性字符串对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

### appendStyledString

PhonePC/2in1TabletTVWearable

appendStyledString(other: StyledString): void

在末尾位置追加新的属性字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | 新的属性字符串对象。 |

## StyledStringValue

PhonePC/2in1TabletTVWearable

type StyledStringValue = TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle |

TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | UrlStyle | CustomSpan | UserDataSpan | BackgroundColorStyle

样式对象类型，用于设置属性字符串的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [TextStyle](ts-universal-styled-string.md#textstyle) | 文本字体样式。 |
| [DecorationStyle](ts-universal-styled-string.md#decorationstyle) | 文本装饰线样式。 |
| [BaselineOffsetStyle](ts-universal-styled-string.md#baselineoffsetstyle) | 文本基线偏移量样式。 |
| [LetterSpacingStyle](ts-universal-styled-string.md#letterspacingstyle) | 文本字符间距样式。 |
| [LineHeightStyle](ts-universal-styled-string.md#lineheightstyle) | 文本行高样式。 |
| [TextShadowStyle](ts-universal-styled-string.md#textshadowstyle) | 文本阴影样式。 |
| [GestureStyle](ts-universal-styled-string.md#gesturestyle) | 事件手势样式。 |
| [ParagraphStyle](ts-universal-styled-string.md#paragraphstyle) | 文本段落样式。 |
| [ImageAttachment](ts-universal-styled-string.md#imageattachment) | 图片样式。 |
| [CustomSpan](ts-universal-styled-string.md#customspan) | 自定义绘制Span样式。 |
| [UserDataSpan](ts-universal-styled-string.md#userdataspan) | UserDataSpan样式。 |
| [UrlStyle](ts-universal-styled-string.md#urlstyle14) | 超链接样式。 |
| [BackgroundColorStyle](ts-universal-styled-string.md#backgroundcolorstyle14) | 文本背景颜色样式。 |

## StyleOptions对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 设置属性字符串样式的开始位置。  当start的值小于0或超出字符串长度时，按0处理。 |
| length | number | 否 | 是 | 设置属性字符串样式的长度。  当length的值小于0或超出字符串长度与start的差值时，按字符串长度与start的差值处理。 |
| styledKey | [StyledStringKey](ts-universal-styled-string.md#styledstringkey枚举说明) | 否 | 否 | 样式类型的枚举值。 |
| styledValue | [StyledStringValue](ts-universal-styled-string.md#styledstringvalue) | 否 | 否 | 样式对象。 |

## SpanStyle对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 否 | 匹配属性字符串样式的开始位置。 |
| length | number | 否 | 否 | 匹配属性字符串样式的长度。 |
| styledKey | [StyledStringKey](ts-universal-styled-string.md#styledstringkey枚举说明) | 否 | 否 | 样式类型的枚举值。 |
| styledValue | [StyledStringValue](ts-universal-styled-string.md#styledstringvalue) | 否 | 否 | 样式对象。 |

## TextStyle

PhonePC/2in1TabletTVWearable

文本字体样式对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 是 | 是 | 获取属性字符串的文本颜色。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontFamily | string | 是 | 是 | 获取属性字符串的文本字体。  默认返回undefined。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontSize | number | 是 | 是 | 获取属性字符串的文本字体大小。  单位：[vp](ts-pixel-units.md)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontWeight | number | 是 | 是 | 获取属性字符串的文本字体粗细。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontStyle | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 是 | 获取属性字符串的文本字体样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| strokeWidth20+ | number | 是 | 是 | 获取属性字符串的文本描边宽度。  默认返回0，单位为[vp](ts-pixel-units.md)。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| strokeColor20+ | [ResourceColor](ts-types.md#resourcecolor) | 是 | 是 | 获取属性字符串的文本描边颜色。  默认返回字体颜色。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| superscript20+ | [SuperscriptStyle](ts-text-common.md#superscriptstyle20枚举说明) | 是 | 是 | 获取属性字符串的文本上下角标。  默认值：SuperscriptStyle.NORMAL。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

fontWeight参数与返回值的关系如下：

| 参数 | 返回值 |
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
| FontWeight.Bold (or 'bold') | 9 |
| FontWeight.Normal (or 'normal') | 10 |
| FontWeight.Bolder (or 'bolder') | 11 |
| FontWeight.Lighter (or 'lighter') | 12 |
| FontWeight.Medium (or 'medium') | 13 |
| FontWeight.Regular (or 'regular') | 14 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(value?: TextStyleInterface)

文本字体样式的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextStyleInterface](ts-universal-styled-string.md#textstyleinterface对象说明) | 否 | 字体样式设置项。 |

## TextStyleInterface对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 字体颜色。  默认为主题色。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontFamily | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 文本字体。  默认为主题字体。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontSize | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 字体大小。  默认字体大小为16fp。  如果LengthMetrics的unit值是percent，当前设置不生效，处理为16fp。  单位：[fp](ts-pixel-units.md)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontWeight | number| [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 是 | 字体粗细。  number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontStyle | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 是 | 字体样式。  默认值：FontStyle.Normal  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| strokeWidth20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 文本描边宽度。如果LengthMetrics的unit值是percent，当前设置不生效，处理为0。  设置值小于0时为实心字，大于0时为空心字。  默认值为0。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| strokeColor20+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本描边颜色。  默认值为字体颜色，设置异常值时取字体颜色。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| superscript20+ | [SuperscriptStyle](ts-text-common.md#superscriptstyle20枚举说明) | 否 | 是 | 文本上下角标。  默认值：SuperscriptStyle.NORMAL  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## GestureStyle

PhonePC/2in1TabletTVWearable

事件手势对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(value?: GestureStyleInterface)

事件手势的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GestureStyleInterface](ts-universal-styled-string.md#gesturestyleinterface对象说明) | 否 | 事件设置项。 |

## GestureStyleInterface对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onClick | Callback<[ClickEvent](ts-universal-events-click.md#clickevent)> | 否 | 是 | 设置点击事件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onLongPress | Callback<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 否 | 是 | 设置长按事件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onTouch20+ | Callback<[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)> | 否 | 是 | 设置触摸事件。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## DecorationOptions20+

PhonePC/2in1TabletTVWearable

文本装饰线样式的额外配置选项对象说明。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableMultiType | boolean | 否 | 是 | 是否开启多装饰线显示。  默认值：undefined。设置为true开启，设置为false/undefined关闭。  所有需要显示的装饰线都必须启用此选项，在这些装饰线的交集区域显示多装饰线效果，样式、颜色和粗细将采用最后设置的装饰线的效果。 |

## DecorationStyle

PhonePC/2in1TabletTVWearable

文本装饰线样式对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TextDecorationType](ts-appendix-enums.md#textdecorationtype) | 是 | 否 | 获取属性字符串的文本装饰线类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 是 | 获取属性字符串的文本装饰线颜色。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| style | [TextDecorationStyle](ts-appendix-enums.md#textdecorationstyle12) | 是 | 是 | 获取属性字符串的文本装饰线样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| thicknessScale20+ | number | 是 | 是 | 获取属性字符串的文本装饰线粗细缩放值。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| options20+ | [DecorationOptions](ts-universal-styled-string.md#decorationoptions20) | 是 | 是 | 获取属性字符串的文本装饰线样式的额外配置选项。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(value: DecorationStyleInterface)

文本装饰线样式的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DecorationStyleInterface](ts-universal-styled-string.md#decorationstyleinterface) | 是 | 文本装饰线设置项。  默认值：  {  type: TextDecorationType.None,  color: Color.Black,  style: TextDecorationStyle.SOLID  } |

### constructor20+

PhonePC/2in1TabletTVWearable

constructor(value: DecorationStyleInterface, options?: DecorationOptions)

文本装饰线样式的构造函数，包含额外配置选项。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DecorationStyleInterface](ts-universal-styled-string.md#decorationstyleinterface) | 是 | 文本装饰线设置项。  默认值：  {  type: TextDecorationType.None,  color: Color.Black,  style: TextDecorationStyle.SOLID,  thicknessScale: 1.0  } |
| options | [DecorationOptions](ts-universal-styled-string.md#decorationoptions20) | 否 | 文本装饰线额外配置选项。  默认值：  {  enableMultiType: undefined  } |

## DecorationStyleInterface

PhonePC/2in1TabletTVWearable

文本装饰线样式接口对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TextDecorationType](ts-appendix-enums.md#textdecorationtype) | 否 | 否 | 装饰线类型。  默认值：TextDecorationType.None  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 装饰线颜色。  默认值：Color.Black  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| style | [TextDecorationStyle](ts-appendix-enums.md#textdecorationstyle12) | 否 | 是 | 装饰线样式。  默认值：TextDecorationStyle.SOLID  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| thicknessScale20+ | number | 否 | 是 | 装饰线粗细缩放。  默认值：1.0  取值范围：[0, +∞)  **说明：** 负值按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

说明

当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。

当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

## BaselineOffsetStyle

PhonePC/2in1TabletTVWearable

文本基线偏移量对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baselineOffset | number | 是 | 否 | 获取属性字符串的文本基线偏移量。  单位：[vp](ts-pixel-units.md) |

### constructor

PhonePC/2in1TabletTVWearable

constructor(value: LengthMetrics)

文本基线偏移的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 文本基线偏移量设置项。如果LengthMetrics的unit值是percent，该设置不生效。 |

## LetterSpacingStyle

PhonePC/2in1TabletTVWearable

文本字符间距对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| letterSpacing | number | 是 | 否 | 获取属性字符串的文本字符间距。  单位：[vp](ts-pixel-units.md) |

### constructor

PhonePC/2in1TabletTVWearable

constructor(value: LengthMetrics)

文本字符间距的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 文本字符间距设置项。如果LengthMetrics的unit值是percent，该设置不生效。 |

## LineHeightStyle

PhonePC/2in1TabletTVWearable

文本行高对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lineHeight | number | 是 | 否 | 获取属性字符串的文本行高。  单位：[vp](ts-pixel-units.md) |

### constructor

PhonePC/2in1TabletTVWearable

constructor(lineHeight: LengthMetrics)

文本行高的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lineHeight | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 文本行高设置项。如果LengthMetrics的value值不大于0时，不限制文本行高，自适应字体大小。 |

## TextShadowStyle

PhonePC/2in1TabletTVWearable

文本阴影对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textShadow | Array<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明)> | 是 | 否 | 获取属性字符串的文本阴影。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(value: ShadowOptions | Array<ShadowOptions>)

文本阴影对象的构造函数。

ShadowOptions对象中不支持fill字段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | Array<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明)> | 是 | 文本阴影设置项。 |

## ImageAttachment

PhonePC/2in1TabletTVWearable

图片对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | 获取属性字符串的图片数据源。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| size | [SizeOptions](ts-types.md#sizeoptions) | 是 | 是 | 获取属性字符串的图片尺寸。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  返回number类型值的单位为px。 |
| sizeInVp21+ | [SizeOptions](ts-types.md#sizeoptions) | 是 | 是 | 获取属性字符串的图片尺寸。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。  返回number类型值的单位为vp。  当ImageAttachment尺寸设置为负数值或undefined时，返回为undefined。 |
| verticalAlign | [ImageSpanAlignment](ts-appendix-enums.md#imagespanalignment10) | 是 | 是 | 获取属性字符串的图片对齐方式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| objectFit | [ImageFit](ts-appendix-enums.md#imagefit) | 是 | 是 | 获取属性字符串的图片缩放类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| layoutStyle | [ImageAttachmentLayoutStyle](ts-universal-styled-string.md#imageattachmentlayoutstyle对象说明) | 是 | 是 | 获取属性字符串的图片布局。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| colorFilter15+ | [ColorFilterType](ts-universal-styled-string.md#colorfiltertype15) | 是 | 是 | 获取属性字符串的图片颜色滤镜效果。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| supportSvg222+ | boolean | 是 | 是 | 获取属性字符串是否开启[SVG标签解析能力增强功能](ts-image-svg2-capabilities.md)。  true：支持SVG解析新能力；false：保持原有SVG解析能力。  默认值：false  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(value: ImageAttachmentInterface)

图片对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageAttachmentInterface](ts-universal-styled-string.md#imageattachmentinterface对象说明) | 是 | 图片设置项。 |

### constructor15+

PhonePC/2in1TabletTVWearable

constructor(attachment: Optional<AttachmentType>)

图片对象的构造函数。与value类型入参构造函数相比，attachment参数增加了对undefined类型和[ResourceStr](ts-types.md#resourcestr)类型图片的支持。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attachment | Optional<[AttachmentType](ts-universal-styled-string.md#attachmenttype15)> | 是 | PixelMap类型或[ResourceStr](ts-types.md#resourcestr)类型图片设置项。 |

## AttachmentType15+

PhonePC/2in1TabletTVWearable

type AttachmentType = ImageAttachmentInterface | ResourceImageAttachmentOptions

图片设置项类型，用于设置属性字符串PixelMap类型或[ResourceStr](ts-types.md#resourcestr)类型图片。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ImageAttachmentInterface](ts-universal-styled-string.md#imageattachmentinterface对象说明) | PixelMap类型图片设置项。 |
| [ResourceImageAttachmentOptions](ts-universal-styled-string.md#resourceimageattachmentoptions15) | ResourceStr类型图片设置项。 |

## ColorFilterType15+

PhonePC/2in1TabletTVWearable

type ColorFilterType = ColorFilter | DrawingColorFilter

图片颜色滤镜设置项类型。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](ts-types.md#colorfilter9) | ColorFilter类型图片颜色滤镜设置项。 |
| [DrawingColorFilter](ts-basic-components-image.md#drawingcolorfilter12) | DrawingColorFilter类型图片颜色滤镜设置项。 |

## ImageAttachmentInterface对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 设置图片数据源。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| size | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | 设置图片大小，不支持百分比。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  size的默认值与objectFit的值有关，不同的objectFit的值对应size的默认值不同。比如当objectFit的值为Cover时，图片高度为组件高度减去组件上下的内边距，图片宽度为组件宽度减去组件左右的内边距。 |
| verticalAlign | [ImageSpanAlignment](ts-appendix-enums.md#imagespanalignment10) | 否 | 是 | 设置图片基于文本的对齐方式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  默认值：ImageSpanAlignment.BOTTOM |
| objectFit | [ImageFit](ts-appendix-enums.md#imagefit) | 否 | 是 | 设置图片的缩放类型，当前枚举类型不支持ImageFit.MATRIX。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  默认值：ImageFit.Cover |
| layoutStyle | [ImageAttachmentLayoutStyle](ts-universal-styled-string.md#imageattachmentlayoutstyle对象说明) | 否 | 是 | 设置图片布局。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| colorFilter15+ | [ColorFilterType](ts-universal-styled-string.md#colorfiltertype15) | 否 | 是 | 设置属性字符串的图片颜色滤镜效果。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## ImageAttachmentLayoutStyle对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| margin | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [Margin](ts-types.md#margin) | 否 | 是 | 设置图片外边距。  默认值：0  单位：[vp](ts-pixel-units.md) |
| padding | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [Padding](ts-types.md#padding) | 否 | 是 | 设置图片内边距。  默认值：0  单位：[vp](ts-pixel-units.md) |
| borderRadius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 设置圆角。  默认值：0  单位：[vp](ts-pixel-units.md) |

## ResourceImageAttachmentOptions15+

PhonePC/2in1TabletTVWearable

ResourceStr类型图片设置项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resourceValue | Optional<[ResourceStr](ts-types.md#resourcestr)> | 否 | 否 | 设置图片数据源。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| size | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | 设置图片大小。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| verticalAlign | [ImageSpanAlignment](ts-appendix-enums.md#imagespanalignment10) | 否 | 是 | 设置图片基于文本的对齐方式。  默认值：ImageSpanAlignment.BOTTOM  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| objectFit | [ImageFit](ts-appendix-enums.md#imagefit) | 否 | 是 | 设置图片的缩放类型，当前枚举类型不支持ImageFit.MATRIX。  默认值：ImageFit.Cover  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| layoutStyle | [ImageAttachmentLayoutStyle](ts-universal-styled-string.md#imageattachmentlayoutstyle对象说明) | 否 | 是 | 设置图片布局。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| colorFilter | [ColorFilterType](ts-universal-styled-string.md#colorfiltertype15) | 否 | 是 | 设置属性字符串的图片颜色滤镜效果。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| syncLoad | boolean | 否 | 是 | 是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。  true：同步加载；false：异步加载。  默认值：false  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| supportSvg222+ | boolean | 否 | 是 | 控制是否开启[SVG标签解析能力增强功能](ts-image-svg2-capabilities.md)。  true：支持SVG解析新能力；false：保持原有SVG解析能力。  默认值：false  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## CustomSpan

PhonePC/2in1TabletTVWearable

自定义绘制Span，仅提供基类，具体实现由开发者定义。

自定义绘制Span拖拽显示的缩略图为空白。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### onMeasure

PhonePC/2in1TabletTVWearable

abstract onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics

获取自定义绘制Span的尺寸大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| measureInfo | [CustomSpanMeasureInfo](ts-universal-styled-string.md#customspanmeasureinfo对象说明) | 是 | 文本的字体大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CustomSpanMetrics](ts-universal-styled-string.md#customspanmetrics对象说明) | 自定义绘制Span的尺寸信息。  **说明：**  最终的CustomSpan的高度是由当前Text组件的行高所决定的。当height不传值，则默认取Text组件的fontSize的值作为CustomSpan的高度；当height大于当前行的其他子组件的高度时，此时height即为Text组件的行高。 |

### onDraw

PhonePC/2in1TabletTVWearable

abstract onDraw(context: DrawContext, drawInfo: CustomSpanDrawInfo): void

绘制自定义绘制Span。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [DrawContext](js-apis-arkui-graphics.md#drawcontext) | 是 | 图形绘制上下文。  **说明：**  DrawContext的canvas方法获取的画布是Text组件的画布，绘制时不会超出Text组件的范围。 |
| drawInfo | [CustomSpanDrawInfo](ts-universal-styled-string.md#customspandrawinfo对象说明) | 是 | 自定义绘制Span的绘制信息。 |

### invalidate13+

PhonePC/2in1TabletTVWearable

invalidate(): void

主动刷新使用CustomSpan的Text组件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## CustomSpanMeasureInfo对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontSize | number | 否 | 否 | 设置文本字体大小。  单位：[fp](ts-pixel-units.md) |

## CustomSpanMetrics对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 自定义绘制Span的宽。  单位：[vp](ts-pixel-units.md) |
| height | number | 否 | 是 | 自定义绘制Span的高。  单位：[vp](ts-pixel-units.md) |

## CustomSpanDrawInfo对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 自定义绘制Span相对于挂载组件的偏移。  单位：[px](ts-pixel-units.md) |
| lineTop | number | 否 | 否 | 自定义绘制Span相对于Text组件的上边距。  单位：[px](ts-pixel-units.md) |
| lineBottom | number | 否 | 否 | 自定义绘制Span相对于Text组件的下边距。  单位：[px](ts-pixel-units.md) |
| baseline | number | 否 | 否 | 自定义绘制Span的所在行的基线偏移量。  单位：[px](ts-pixel-units.md) |

## ParagraphStyle

PhonePC/2in1TabletTVWearable

文本段落样式对象说明。

除首个段落外，后续段落按'\n'划分。

每个段落的段落样式按首个占位设置的段落样式生效，未设置时，段落按被绑定组件的段落样式生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textAlign | [TextAlign](ts-appendix-enums.md#textalign) | 是 | 是 | 获取属性字符串文本段落在水平方向的对齐方式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textIndent | number | 是 | 是 | 获取属性字符串文本段落的首行文本缩进。单位VP  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxLines | number | 是 | 是 | 获取属性字符串文本段落的最大行数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| overflow | [TextOverflow](ts-appendix-enums.md#textoverflow) | 是 | 是 | 获取属性字符串文本段落超长时的显示方式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| wordBreak | [WordBreak](ts-appendix-enums.md#wordbreak11) | 是 | 是 | 获取属性字符串文本段落的断行规则。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| leadingMargin | number | [LeadingMarginPlaceholder](ts-basic-components-richeditor.md#leadingmarginplaceholder11) | 是 | 是 | 获取属性字符串文本段落的缩进。  返回为number类型时，单位为vp。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| paragraphSpacing19+ | number | 是 | 是 | 获取属性字符串文本段落的段落间距。  单位：vp  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| textVerticalAlign20+ | [TextVerticalAlign](ts-text-common.md#textverticalalign20) | 是 | 是 | 获取属性字符串文本段落在垂直方向的对齐方式。  一个段落下使用同一字号必须同时设置行高[lineHeight](ts-basic-components-text.md#lineheight)或者同一个段落不同字号文本混排时才有效果差异，否则设置了该属性任意枚举值和未设置该属性都是一样的排版效果。属性字符串[TextStyle](ts-universal-styled-string.md#textstyle)中的SuperscriptStyle上下角标样式仅在[TextVerticalAlign](ts-text-common.md#textverticalalign20)属性值为TextVerticalAlign.BASELINE时生效，其余垂直对齐方式下上下角标文本和普通文本表现一致，无上下角标效果。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| leadingMarginSpan22+ | [LeadingMarginSpan](ts-universal-styled-string.md#leadingmarginspan22) | 是 | 是 | 获取属性字符串文本段落的自定义缩进信息。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| textDirection23+ | [TextDirection](ts-text-common.md#textdirection22) | 是 | 是 | 获取文本方向。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

说明

属性字符串的maxLines和overflow仅在Text中生效，建议在组件侧设置。

textAlign只能调整文本整体的布局，不影响字符的显示顺序。若需要调整字符的显示顺序，请参考[镜像状态字符对齐](../harmonyos-guides/arkts-internationalization.md#镜像状态字符对齐)。

### constructor

PhonePC/2in1TabletTVWearable

constructor(value?: ParagraphStyleInterface)

文本段落样式的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ParagraphStyleInterface](ts-universal-styled-string.md#paragraphstyleinterface对象说明) | 否 | 段落样式设置项。 |

## ParagraphStyleInterface对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textAlign | [TextAlign](ts-appendix-enums.md#textalign) | 否 | 是 | 设置文本段落在水平方向的对齐方式。  默认值：TextAlign.Start  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textIndent | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 设置文本段落的首行文本缩进。不支持百分比。  默认值：0  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxLines | number | 否 | 是 | 设置文本段落的最大行数，默认不限制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| overflow | [TextOverflow](ts-appendix-enums.md#textoverflow) | 否 | 是 | 设置文本段落超长时的显示方式。  默认值：TextOverflow.None  需配合maxLines使用，单独设置不生效。不支持TextOverflow.MARQUEE。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| wordBreak | [WordBreak](ts-appendix-enums.md#wordbreak11) | 否 | 是 | 设置文本段落的断行规则。  默认值：WordBreak.NORMAL  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| leadingMargin | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [LeadingMarginPlaceholder](ts-basic-components-richeditor.md#leadingmarginplaceholder11) | 否 | 是 | 设置文本段落的缩进。不支持百分比。  默认值：0  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| paragraphSpacing19+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 设置文本段落的段落间距。  段落间距默认大小为0。不支持百分比。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| textVerticalAlign20+ | [TextVerticalAlign](ts-text-common.md#textverticalalign20) | 否 | 是 | 设置文本段落在垂直方向的对齐方式。  默认值：TextVerticalAlign.BASELINE  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| leadingMarginSpan22+ | [LeadingMarginSpan](ts-universal-styled-string.md#leadingmarginspan22) | 否 | 是 | 设置文本段落的自定义缩进。不支持百分比。  默认值：0  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| textDirection23+ | [TextDirection](ts-text-common.md#textdirection22) | 否 | 是 | 设置文本方向。  默认值：TextDirection.DEFAULT  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## UserDataSpan

PhonePC/2in1TabletTVWearable

支持存储自定义扩展信息，用于存储和获取用户数据，仅提供基类，具体实现由开发者定义。

扩展信息不影响实际显示效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## LeadingMarginSpan22+

PhonePC/2in1TabletTVWearable

文本段落的自定义缩进，仅提供基类，具体实现由开发者定义。

### onDraw22+

PhonePC/2in1TabletTVWearable

abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void

绘制自定义图案。段落中的每一行文本都会触发一次onDraw。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [DrawContext](js-apis-arkui-graphics.md#drawcontext) | 是 | 图形绘制上下文。  DrawContext的canvas方法获取的是组件的画布，绘制时不会超出组件的范围。 |
| drawInfo | [LeadingMarginSpanDrawInfo](ts-universal-styled-string.md#leadingmarginspandrawinfo22对象说明) | 是 | 自定义绘制信息。 |

### getLeadingMargin22+

PhonePC/2in1TabletTVWearable

abstract getLeadingMargin(): LengthMetrics

返回文本段落的缩进距离。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 文本段落的缩进。不支持百分比。  默认值：0 |

## LeadingMarginSpanDrawInfo22+对象说明

PhonePC/2in1TabletTVWearable

自定义绘制信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 当前行相对于组件的水平偏移。direction为RTL时，返回当前行右侧与组件右边缘的距离。  单位：[px](ts-pixel-units.md)  取值范围：大于等于0。 |
| top | number | 否 | 否 | 行顶与组件上边缘的距离。  单位：[px](ts-pixel-units.md)  取值范围：大于等于0。 |
| bottom | number | 否 | 否 | 行底与组件上边缘的距离。  单位：[px](ts-pixel-units.md)  取值范围：大于等于0。 |
| baseline | number | 否 | 否 | 当前行的基线与组件上边缘的距离。  单位：[px](ts-pixel-units.md)  取值范围：大于等于0。 |
| direction | [TextDirection](ts-text-common.md#textdirection22) | 否 | 否 | 文本内容的方向。 |
| start | number | 否 | 否 | 当前行的起始索引。  取值范围：大于等于0。 |
| end | number | 否 | 否 | 当前行的结束索引。  取值范围：大于等于0。 |
| first | boolean | 否 | 否 | 当前行是否是段落的首行。  true：首行；false：非首行。 |

## StyledStringKey枚举说明

PhonePC/2in1TabletTVWearable

范围属性字符串样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FONT | 0 | 字体样式键。[TextStyle](ts-universal-styled-string.md#textstyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DECORATION | 1 | 文本装饰线样式键。[DecorationStyle](ts-universal-styled-string.md#decorationstyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BASELINE\_OFFSET | 2 | 文本基线偏移量样式键。[BaselineOffsetStyle](ts-universal-styled-string.md#baselineoffsetstyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LETTER\_SPACING | 3 | 文本字符间距样式键。[LetterSpacingStyle](ts-universal-styled-string.md#letterspacingstyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TEXT\_SHADOW | 4 | 文本阴影样式键。[TextShadowStyle](ts-universal-styled-string.md#textshadowstyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LINE\_HEIGHT | 5 | 文本行高样式键。[LineHeightStyle](ts-universal-styled-string.md#lineheightstyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BACKGROUND\_COLOR14+ | 6 | 文本背景色样式键。[BackgroundColorStyle](ts-universal-styled-string.md#backgroundcolorstyle14)所属键。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| URL14+ | 7 | 超链接样式键。[UrlStyle](ts-universal-styled-string.md#urlstyle14)所属键。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| GESTURE | 100 | 事件手势键。[GestureStyle](ts-universal-styled-string.md#gesturestyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PARAGRAPH\_STYLE | 200 | 段落样式键。[ParagraphStyle](ts-universal-styled-string.md#paragraphstyle)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| IMAGE | 300 | 图片键。[ImageAttachment](ts-universal-styled-string.md#imageattachment)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CUSTOM\_SPAN | 400 | 自定义绘制Span键。[CustomSpan](ts-universal-styled-string.md#customspan)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| USER\_DATA | 500 | UserDataSpan键。[UserDataSpan](ts-universal-styled-string.md#userdataspan)所属键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## BackgroundColorStyle14+

PhonePC/2in1TabletTVWearable

文本背景颜色对象说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textBackgroundStyle | [TextBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11对象说明) | 是 | 否 | 获取属性字符串的文本背景颜色。  默认值：  {  color: Color.Transparent,  radius: 0  } |

### constructor14+

PhonePC/2in1TabletTVWearable

constructor(textBackgroundStyle: TextBackgroundStyle)

文本背景颜色的构造函数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textBackgroundStyle | [TextBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11对象说明) | 是 | 文本背景色设置项。  默认值：  {  color: Color.Transparent,  radius: 0  } |

## UrlStyle14+

PhonePC/2in1TabletTVWearable

超链接对象说明。

默认颜色、字号、字重分别是'#ff0a59f7'、'16fp'、'FontWeight.Regular'，若属性字符串设置TextStyle，则TextStyle优先级更高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 否 | 获取属性字符串的超链接内容。 |

### constructor14+

PhonePC/2in1TabletTVWearable

constructor(url: string)

超链接对象的构造函数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 超链接设置项。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（属性字符串处理）

从API version 12开始，该示例通过[insertString](ts-universal-styled-string.md#insertstring)、[removeStyles](ts-universal-styled-string.md#removestyles)、[replaceStyle](ts-universal-styled-string.md#replacestyle)、[getStyles](ts-universal-styled-string.md#getstyles)接口实现属性字符串的插入、删除、替换、查看。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct styled_string_process_demo {
5. @State height1: number = 450;
6. @State fontSize1: number = 16;
7. @State fontWeight1: number = 400;
8. @State color1: Color = Color.Blue;
9. scroll: Scroller = new Scroller();
10. fontStyleAttr1: TextStyle = new TextStyle({ fontColor: Color.Blue });
11. fontStyleAttr2: TextStyle = new TextStyle({ fontColor: Color.Orange });
12. // 创建可读写属性字符串的对象mutableStyledString1
13. mutableStyledString1: MutableStyledString = new MutableStyledString("运动45分钟");
14. // 创建构造入参有字符串和样式的对象mutableStyledString2
15. mutableStyledString2: MutableStyledString = new MutableStyledString("test hello world", [{
16. start: 0,
17. length: 5,
18. styledKey: StyledStringKey.FONT,
19. styledValue: this.fontStyleAttr1
20. }]);
21. // 创建只读属性字符串对象styledString2
22. styledString2: StyledString = new StyledString("运动45分钟");
23. spanStyle1: SpanStyle = {
24. start: 0,
25. length: 5,
26. styledKey: StyledStringKey.FONT,
27. styledValue: new TextStyle({ fontColor: Color.Pink })
28. };
29. spanStyle2: SpanStyle = {
30. start: 0,
31. length: 2,
32. styledKey: StyledStringKey.FONT,
33. styledValue: new TextStyle({ fontColor: Color.Red })
34. };
35. @State string1: string = '';
36. @State fontColor1: ResourceColor = Color.Red;
37. controller1: TextController = new TextController();
38. controller2: TextController = new TextController();
39. controller3: TextController = new TextController();

41. async onPageShow() {
42. this.controller1.setStyledString(this.styledString2);
43. this.controller2.setStyledString(this.mutableStyledString1);
44. this.controller3.setStyledString(this.mutableStyledString2);
45. }

47. build() {
48. Column() {
49. Scroll(this.scroll) {
50. Column() {
51. // 显示属性字符串
52. Text(undefined, { controller: this.controller1 })
53. Text(undefined, { controller: this.controller3 }).key('mutableStyledString2')
54. Button('修改string1的值')
55. .onClick(() => {
56. let result = this.mutableStyledString1.equals(this.styledString2);
57. if (result) {
58. this.string1 = this.mutableStyledString1.getString();
59. console.info("mutableStyledString1 content:", this.mutableStyledString1.getString());
60. console.info("mutableStyledString1 length:", this.mutableStyledString1.length);
61. }
62. })

64. // 属性字符串与Span冲突时忽略Span,以及样式与Text组件属性未冲突部分生效Text设置的属性
65. Text(undefined, { controller: this.controller2 }) {
66. Span("span and styledString test")
67. .fontColor(Color.Yellow)
68. .decoration({ type: TextDecorationType.LineThrough })
69. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
70. ImageSpan($r('app.media.startIcon'))
71. }
72. .key('styledString2')
73. .fontColor(this.fontColor1)
74. .letterSpacing(10)
75. .fontSize(32)
76. .fontWeight(600)
77. .fontStyle(FontStyle.Italic)
78. .lineHeight(30)
79. .textShadow({
80. radius: 5,
81. color: Color.Blue,
82. offsetX: 5,
83. offsetY: 5
84. })
85. .textCase(TextCase.UpperCase)
86. .decoration({ type: TextDecorationType.LineThrough, color: Color.Yellow })
87. .baselineOffset(2)
88. .copyOption(CopyOptions.InApp)
89. .margin({ top: 10 })
90. .draggable(true)

92. // 以上冲突测试对照组
93. Text() {
94. Span(this.string1)
95. .fontColor(this.color1)
96. .decoration({ type: TextDecorationType.LineThrough })
97. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
98. ImageSpan($r('app.media.startIcon'))
99. .width(50).height(50)
100. }
101. .letterSpacing(10)
102. .fontSize(32)
103. .fontWeight(600)
104. .fontStyle(FontStyle.Italic)
105. .lineHeight(30)
106. .textShadow({
107. radius: 5,
108. color: Color.Blue,
109. offsetX: 5,
110. offsetY: 5
111. })
112. .textCase(TextCase.UpperCase)
113. .decoration({ type: TextDecorationType.LineThrough, color: Color.Yellow })
114. .baselineOffset(2)

116. Button('设置样式及替换文本')
117. .onClick(() => {
118. this.mutableStyledString1.replaceStyle({
119. start: 2,
120. length: 2,
121. styledKey: StyledStringKey.FONT,
122. styledValue: this.fontStyleAttr1
123. });
124. this.mutableStyledString1.insertString(0, "压力85偏高，");
125. this.mutableStyledString1.setStyle({
126. start: 2,
127. length: 2,
128. styledKey: StyledStringKey.FONT,
129. styledValue: this.fontStyleAttr2
130. });
131. this.controller2.setStyledString(this.mutableStyledString1);
132. })
133. .margin({ top: 10 })

135. Button('查询样式及清空样式')
136. .onClick(() => {
137. let styles = this.mutableStyledString1.getStyles(0, this.mutableStyledString1.length);
138. if (styles.length == 2) {
139. for (let i = 0; i < styles.length; i++) {
140. console.info('StyledString style object start:' + styles[i].start);
141. console.info('StyledString style object length:' + styles[i].length);
142. console.info('StyledString style object key:' + styles[i].styledKey);
143. if (styles[i].styledKey === 0) {
144. let fontAttr = styles[i].styledValue as TextStyle;
145. console.info('StyledString fontColor:' + fontAttr.fontColor);
146. }
147. }
148. }
149. if (styles[0] !== undefined) {
150. this.mutableStyledString2.setStyle(styles[0]);
151. this.controller3.setStyledString(this.mutableStyledString2);
152. }
153. this.mutableStyledString1.removeStyles(2, 3);
154. this.controller2.setStyledString(this.mutableStyledString1);
155. })
156. .margin({ top: 10 })
157. }.width('100%')

159. }
160. .expandSafeArea([SafeAreaType.KEYBOARD])
161. .scrollable(ScrollDirection.Vertical)
162. .scrollBar(BarState.On)
163. .scrollBarColor(Color.Gray)
164. .scrollBarWidth(10)
165. .edgeEffect(EdgeEffect.None)
166. }
167. .width('100%')
168. }
169. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/1BCK6D2-RViM_r2aENN6rA/zh-cn_image_0000002552959820.png?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=21D0C85C23D57ACB4793FC21362F5588B14B169B81BEC4B1DA795678F35DF386)

### 示例2（设置事件）

从API version 12开始，该示例通过[StyleOptions](ts-universal-styled-string.md#styleoptions对象说明)中的styledKey、styledValue接口实现属性字符串绑定事件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct styled_string_bind_events_demo {
5. scroll: Scroller = new Scroller();
6. fontStyleAttr1: TextStyle = new TextStyle({ fontColor: Color.Blue });
7. private uiContext: UIContext = this.getUIContext();
8. clickGestureAttr: GestureStyle = new GestureStyle({
9. onClick: () => {
10. this.uiContext.getPromptAction().showToast({ message: 'clickGestureAttr object trigger click event' });
11. this.backgroundColor1 = Color.Yellow;
12. }
13. })
14. gestureStyleAttr: GestureStyle = new GestureStyle({
15. onClick: () => {
16. this.uiContext.getPromptAction().showToast({ message: 'gestureStyleAttr object trigger click event' });
17. this.backgroundColor1 = Color.Green;
18. },
19. onLongPress: () => {
20. this.uiContext.getPromptAction().showToast({ message: 'gestureStyleAttr object trigger long press event' });
21. this.backgroundColor1 = Color.Orange;
22. },
23. onTouch: () => {
24. this.uiContext.getPromptAction().showToast({ message: 'gestureStyleAttr object trigger touch event' });
25. this.backgroundColor1 = Color.Red;
26. }
27. });
28. // 创建事件的对象mutableStyledString3
29. mutableStyledString3: MutableStyledString = new MutableStyledString("hello world", [{
30. start: 0,
31. length: 5,
32. styledKey: StyledStringKey.GESTURE,
33. styledValue: this.clickGestureAttr
34. },
35. {
36. start: 0,
37. length: 5,
38. styledKey: StyledStringKey.FONT,
39. styledValue: this.fontStyleAttr1
40. },
41. {
42. start: 6,
43. length: 5,
44. styledKey: StyledStringKey.GESTURE,
45. styledValue: this.gestureStyleAttr
46. },
47. {
48. start: 6,
49. length: 5,
50. styledKey: StyledStringKey.FONT,
51. styledValue: new TextStyle({ fontColor: Color.Pink })
52. }]);
53. @State backgroundColor1: ResourceColor | undefined = undefined;
54. controller3: TextController = new TextController();

56. async onPageShow() {
57. this.controller3.setStyledString(this.mutableStyledString3);
58. }

60. build() {
61. Column() {
62. Scroll(this.scroll) {
63. Column({ space: 30 }) {
64. Button("响应属性字符串事件改变背景色").backgroundColor(this.backgroundColor1).width('80%')
65. // 包含事件的属性字符串
66. Text(undefined, { controller: this.controller3 }).fontSize(30)
67. .copyOption(CopyOptions.InApp)
68. .draggable(true)
69. .clip(true)
70. }.width('100%')
71. }
72. .expandSafeArea([SafeAreaType.KEYBOARD])
73. .scrollable(ScrollDirection.Vertical)
74. .scrollBar(BarState.On)
75. .scrollBarColor(Color.Gray)
76. .scrollBarWidth(10)
77. .edgeEffect(EdgeEffect.None)
78. }
79. .width('100%')
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/IAl42cP2TiGBgb_H53IfXw/zh-cn_image_0000002583479821.png?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=7F9CE79E2D3F1C8BE6E3BA5B56EE227E2E28EE6A7FDC31CD9ED8A89B382B246F)

### 示例3（设置文本样式）

从API version 12开始，该示例通过[getStyles](ts-universal-styled-string.md#getstyles)、[setStyle](ts-universal-styled-string.md#setstyle)接口实现属性字符串查询和设置样式。

```
1. // xxx.ets
2. import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct styled_string_set_text_style_demo {
7. fontStyleAttr1: TextStyle = new TextStyle({ fontColor: Color.Blue });
8. fontStyleAttr2: TextStyle = new TextStyle({
9. fontColor: Color.Orange,
10. fontSize: LengthMetrics.vp(20),
11. fontWeight: FontWeight.Bolder,
12. fontStyle: FontStyle.Italic,
13. fontFamily: "Arial",
14. superscript: SuperscriptStyle.SUPERSCRIPT
15. });
16. fontStyleAttr3: TextStyle = new TextStyle({
17. fontColor: Color.Orange,
18. fontSize: LengthMetrics.vp(20),
19. fontWeight: FontWeight.Lighter,
20. fontStyle: FontStyle.Italic,
21. fontFamily: "Arial",
22. superscript: SuperscriptStyle.SUBSCRIPT
23. });
24. // 创建多重TextStyle样式的对象mutableStyledString1
25. mutableStyledString1: MutableStyledString = new MutableStyledString("运动45分钟", [{
26. start: 0,
27. length: 2,
28. styledKey: StyledStringKey.FONT,
29. styledValue: this.fontStyleAttr3
30. }, {
31. start: 2,
32. length: 2,
33. styledKey: StyledStringKey.FONT,
34. styledValue: this.fontStyleAttr2
35. }
36. ]);
37. // 创建有多种样式组合对象mutableStyledString2
38. mutableStyledString2: MutableStyledString = new MutableStyledString("test hello world", [{
39. start: 0,
40. length: 5,
41. styledKey: StyledStringKey.FONT,
42. styledValue: this.fontStyleAttr1
43. }, {
44. start: 0,
45. length: 5,
46. styledKey: StyledStringKey.DECORATION,
47. styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough, color: Color.Blue })
48. }, {
49. start: 0,
50. length: 5,
51. styledKey: StyledStringKey.TEXT_SHADOW,
52. styledValue: new TextShadowStyle({
53. radius: 5,
54. type: ShadowType.COLOR,
55. color: Color.Yellow,
56. offsetX: 10,
57. offsetY: -10
58. })
59. }, {
60. start: 0,
61. length: 5,
62. styledKey: StyledStringKey.BASELINE_OFFSET,
63. styledValue: new BaselineOffsetStyle(LengthMetrics.px(20))
64. }, {
65. start: 0,
66. length: 5,
67. styledKey: StyledStringKey.LETTER_SPACING,
68. styledValue: new LetterSpacingStyle(new LengthMetrics(10, LengthUnit.VP))
69. }, {
70. start: 6,
71. length: 5,
72. styledKey: StyledStringKey.BASELINE_OFFSET,
73. styledValue: new BaselineOffsetStyle(LengthMetrics.fp(10))
74. }
75. ]);
76. @State fontColor1: ResourceColor = Color.Red;
77. controller: TextController = new TextController();
78. options: TextOptions = { controller: this.controller };
79. controller2: TextController = new TextController();
80. spanStyle1: SpanStyle = {
81. start: 0,
82. length: 5,
83. styledKey: StyledStringKey.FONT,
84. styledValue: new TextStyle({ fontColor: Color.Pink })
85. };

87. async onPageShow() {
88. this.controller.setStyledString(this.mutableStyledString1);
89. this.controller2.setStyledString(this.mutableStyledString2);
90. }

92. build() {
93. Column() {
94. Column({ space: 10 }) {
95. // 显示配了字体各种样式的属性字符串，Text组件亦配置冲突部分生效属性字符串配置，未冲突区间生效Text组件属性设置值
96. Text(undefined, this.options)
97. .fontColor(this.fontColor1)
98. .font({ size: 20, weight: 500, style: FontStyle.Normal })
99. // 显示配置了文本阴影、划线、字符间距、基线偏移量的属性字符串，Text组件亦配置生效属性字符串配置
100. Text(undefined, { controller: this.controller2 })
101. .fontSize(30)
102. .copyOption(CopyOptions.InApp)
103. .draggable(true)
104. .decoration({ type: TextDecorationType.Overline, color: Color.Pink })
105. .textShadow({
106. radius: 10,
107. type: ShadowType.COLOR,
108. color: Color.Green,
109. offsetX: -10,
110. offsetY: 10
111. })
112. Button('查询字体样式')
113. .onClick(() => {
114. let styles = this.mutableStyledString1.getStyles(0, this.mutableStyledString1.length);
115. if (styles.length !== 0) {
116. for (let i = 0; i < styles.length; i++) {
117. console.info('mutableStyledString1 style object start:' + styles[i].start);
118. console.info('mutableStyledString1 style object length:' + styles[i].length);
119. console.info('mutableStyledString1 style object key:' + styles[i].styledKey);
120. if (styles[i].styledKey === 0) {
121. let fontAttr = styles[i].styledValue as TextStyle;
122. console.info('mutableStyledString1 fontColor:' + fontAttr.fontColor);
123. console.info('mutableStyledString1 fontSize:' + fontAttr.fontSize);
124. console.info('mutableStyledString1 fontWeight:' + fontAttr.fontWeight);
125. console.info('mutableStyledString1 fontStyle:' + fontAttr.fontStyle);
126. console.info('mutableStyledString1 fontFamily:' + fontAttr.fontFamily);
127. console.info('mutableStyledString1 superscript:' + fontAttr.superscript);
128. }
129. }
130. }
131. })
132. .margin({ top: 10 })
133. Button('查询其他文本样式')
134. .onClick(() => {
135. let styles = this.mutableStyledString2.getStyles(0, this.mutableStyledString2.length);
136. if (styles.length !== 0) {
137. for (let i = 0; i < styles.length; i++) {
138. console.info('mutableStyledString2 style object start:' + styles[i].start);
139. console.info('mutableStyledString2 style object length:' + styles[i].length);
140. console.info('mutableStyledString2 style object key:' + styles[i].styledKey);
141. if (styles[i].styledKey === 1) {
142. let decoAttr = styles[i].styledValue as DecorationStyle;
143. console.info('mutableStyledString2 decoration type:' + decoAttr.type);
144. console.info('mutableStyledString2 decoration color:' + decoAttr.color);
145. }
146. if (styles[i].styledKey === 2) {
147. let baselineAttr = styles[i].styledValue as BaselineOffsetStyle;
148. console.info('mutableStyledString2 baselineOffset:' + baselineAttr.baselineOffset);
149. }
150. if (styles[i].styledKey === 3) {
151. let letterAttr = styles[i].styledValue as LetterSpacingStyle;
152. console.info('mutableStyledString2 letterSpacing:' + letterAttr.letterSpacing);
153. }
154. if (styles[i].styledKey === 4) {
155. let textShadowAttr = styles[i].styledValue as TextShadowStyle;
156. let shadowValues = textShadowAttr.textShadow;
157. if (shadowValues.length > 0) {
158. for (let j = 0; j < shadowValues.length; j++) {
159. console.info('mutableStyledString2 textShadow type:' + shadowValues[j].type);
160. console.info('mutableStyledString2 textShadow radius:' + shadowValues[j].radius);
161. console.info('mutableStyledString2 textShadow color:' + shadowValues[j].color);
162. console.info('mutableStyledString2 textShadow offsetX:' + shadowValues[j].offsetX);
163. console.info('mutableStyledString2 textShadow offsetY:' + shadowValues[j].offsetY);
164. }
165. }
166. }
167. }
168. }
169. })
170. .margin({ top: 10 })
171. Button('更新mutableStyledString1样式')
172. .onClick(() => {
173. this.mutableStyledString1.setStyle(this.spanStyle1);
174. this.controller.setStyledString(this.mutableStyledString1);
175. })
176. .margin({ top: 10 })
177. }.width('100%')
178. }
179. .width('100%')
180. }
181. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/yjyktx9OR2ytsTCS3x5tAw/zh-cn_image_0000002552800172.png?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=2C2E518CB26ADB3FEC52AE8F1D2793E9BF9C7E396C13B2E7698799A5DF84F26B)

### 示例4（设置图片）

从API version 12开始，该示例通过[ImageAttachment](ts-universal-styled-string.md#imageattachmentinterface对象说明)接口实现属性字符串设置图片。

```
1. // xxx.ets
2. import { image } from '@kit.ImageKit';
3. import { LengthMetrics } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct styled_string_set_image_demo {
8. @State message: string = 'Hello World';
9. imagePixelMap: image.PixelMap | undefined = undefined;
10. @State imagePixelMap3: image.PixelMap | undefined = undefined;
11. mutableStr: MutableStyledString = new MutableStyledString('123');
12. controller: TextController = new TextController();
13. private uiContext: UIContext = this.getUIContext();
14. mutableStr2: MutableStyledString = new MutableStyledString('This is set decoration line style to the mutableStr2', [{
15. start: 0,
16. length: 15,
17. styledKey: StyledStringKey.DECORATION,
18. styledValue: new DecorationStyle({
19. type: TextDecorationType.Overline,
20. color: Color.Orange,
21. style: TextDecorationStyle.DOUBLE
22. })
23. }]);

25. async aboutToAppear() {
26. console.info("aboutToAppear initial imagePixelMap");
27. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
28. this.imagePixelMap =
29. await this.getPixmapFromMedia($r('app.media.startIcon'));
30. }

32. private async getPixmapFromMedia(resource: Resource) {
33. let unit8Array = await this.uiContext.getHostContext()?.resourceManager?.getMediaContent(resource.id);
34. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
35. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
36. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
37. });
38. await imageSource.release();
39. return createPixelMap;
40. }

42. build() {
43. Row() {
44. Column({ space: 5 }) {
45. Text(undefined, { controller: this.controller })
46. .copyOption(CopyOptions.InApp)
47. .draggable(true)
48. .fontSize(30)
49. Button('设置图片')
50. .onClick(() => {
51. if (this.imagePixelMap !== undefined) {
52. this.mutableStr = new MutableStyledString(new ImageAttachment({
53. value: this.imagePixelMap,
54. size: { width: 50, height: 50 },
55. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
56. verticalAlign: ImageSpanAlignment.BASELINE,
57. objectFit: ImageFit.Contain
58. }));
59. this.controller.setStyledString(this.mutableStr);
60. }
61. })
62. Button('设置资源类型图片')
63. .onClick(() => {
64. if (this.imagePixelMap !== undefined) {
65. this.mutableStr = new MutableStyledString(new ImageAttachment({
66. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
67. resourceValue: $r('app.media.sky'),
68. size: { width: 50, height: 50 },
69. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
70. verticalAlign: ImageSpanAlignment.BASELINE,
71. objectFit: ImageFit.Contain,
72. syncLoad: true
73. }));
74. this.controller.setStyledString(this.mutableStr);
75. }
76. })
77. Button('Image之Get')
78. .onClick(() => {
79. let imageArray = this.mutableStr.getStyles(0, 1, StyledStringKey.IMAGE);
80. for (let i = 0; i < imageArray.length; ++i) {
81. console.info('mutableStr start ' + imageArray[i].start + ' length ' + imageArray[i].length + ' type ' +
82. imageArray[i].styledKey);
83. if (imageArray[i].styledKey === 300) {
84. let attachment = imageArray[i].styledValue as ImageAttachment;
85. this.imagePixelMap3 = attachment.value;
86. console.info('mutableStr value ' + JSON.stringify(attachment.value));
87. if (attachment.size !== undefined) {
88. console.info('mutableStr size width ' + attachment.size.width + ' height ' + attachment.size.height);
89. }
90. console.info('mutableStr vertical ' + attachment.verticalAlign);
91. console.info('mutableStr fit ' + attachment.objectFit);
92. if (attachment.layoutStyle !== undefined) {
93. let radius = attachment.layoutStyle.borderRadius as BorderRadiuses;
94. console.info('mutableStr radius ' + JSON.stringify(radius));
95. }
96. }
97. }
98. })
99. Image(this.imagePixelMap3).width(50).height(50)
100. Button('Image之Append')
101. .onClick(() => {
102. let str = new StyledString('123');
103. this.mutableStr.appendStyledString(str);
104. this.controller.setStyledString(this.mutableStr);
105. })
106. Button('Image之Insert 前')
107. .onClick(() => {
108. this.mutableStr.insertString(0, '123');
109. this.controller.setStyledString(this.mutableStr);
110. })
111. Button('Image之Insert 后')
112. .onClick(() => {
113. this.mutableStr.insertString(1, '123');
114. this.controller.setStyledString(this.mutableStr);
115. })
116. Button('Image之replace')
117. .onClick(() => {
118. this.mutableStr.replaceString(2, 5, "789");
119. this.controller.setStyledString(this.mutableStr);
120. })
121. }
122. .width('100%')
123. }
124. .height('100%')
125. }
126. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/-Ug1YPvWTKS_7CZj9mvY0Q/zh-cn_image_0000002583439867.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=5801BEB8DB991683C8826A7806A030E28187EF693FFB2BF875F8C4411B782884)

### 示例5（设置文本行高和段落样式）

从API version 12开始，该示例通过[LineHeightStyle](ts-universal-styled-string.md#lineheightstyle)、[ParagraphStyle](ts-universal-styled-string.md#paragraphstyle)接口实现属性字符串设置文本行高和段落样式。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. const canvasWidth = 1000;
4. const canvasHeight = 100;

6. class LeadingMarginCreator {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private offscreenCanvas: OffscreenCanvas = new OffscreenCanvas(canvasWidth, canvasHeight);
9. private offContext: OffscreenCanvasRenderingContext2D = this.offscreenCanvas.getContext("2d", this.settings);
10. public static instance: LeadingMarginCreator = new LeadingMarginCreator();

12. public genSquareMark(fontSize: number): PixelMap {
13. this.offContext = this.offscreenCanvas.getContext("2d", this.settings);
14. this.clearCanvas();
15. const coordinate = fontSize * (1 - 1 / 1.5) / 2;
16. const sideLength = fontSize / 1.5;
17. this.offContext.fillRect(coordinate, coordinate, sideLength, sideLength);
18. return this.offContext.getPixelMap(0, 0, fontSize, fontSize);
19. }

21. private clearCanvas() {
22. this.offContext.clearRect(0, 0, canvasWidth, canvasHeight);
23. }
24. }

26. @Entry
27. @Component
28. struct styled_string_set_lineheight_paragraphstyle_demo {
29. private leadingMarkCreatorInstance = LeadingMarginCreator.instance;
30. leadingMarginPlaceholder1: LeadingMarginPlaceholder = {
31. pixelMap: this.leadingMarkCreatorInstance.genSquareMark(24),
32. size: [15, 15]
33. };
34. titleParagraphStyleAttr: ParagraphStyle =
35. new ParagraphStyle({ textAlign: TextAlign.Center, paragraphSpacing: LengthMetrics.px(10) });
36. // 第一段落首行缩进15vp
37. paragraphStyleAttr1: ParagraphStyle = new ParagraphStyle({ textIndent: LengthMetrics.vp(15) });
38. // 第二段落缩进15vp且首行有placeholder占位显示
39. paragraphStyleAttr2: ParagraphStyle =
40. new ParagraphStyle({ textAlign: TextAlign.Start, leadingMargin: this.leadingMarginPlaceholder1 });
41. // 第三段落不设置缩进配置最大行数及超长显示方式
42. paragraphStyleAttr3: ParagraphStyle = new ParagraphStyle({
43. textAlign: TextAlign.End,
44. textVerticalAlign: TextVerticalAlign.BASELINE,
45. maxLines: 1,
46. wordBreak: WordBreak.BREAK_ALL,
47. overflow: TextOverflow.Ellipsis
48. });
49. // 行高样式对象
50. lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));
51. // 创建含段落样式的对象paragraphStyledString1
52. paragraphStyledString1: StyledString =
53. new StyledString("段落标题\n正文第一段落开始0123456789正文第一段落结束\n正文第二段落开始hello world正文第二段落结束\n正文第三段落ABCDEFGHIJKLMNOPQRSTUVWXYZ。",
54. [
55. {
56. start: 0,
57. length: 4,
58. styledKey: StyledStringKey.PARAGRAPH_STYLE,
59. styledValue: this.titleParagraphStyleAttr
60. },
61. {
62. start: 0,
63. length: 4,
64. styledKey: StyledStringKey.LINE_HEIGHT,
65. styledValue: new LineHeightStyle(new LengthMetrics(50))
66. }, {
67. start: 0,
68. length: 4,
69. styledKey: StyledStringKey.FONT,
70. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
71. },
72. {
73. start: 5,
74. length: 3,
75. styledKey: StyledStringKey.PARAGRAPH_STYLE,
76. styledValue: this.paragraphStyleAttr1
77. },
78. {
79. start: 5,
80. length: 20,
81. styledKey: StyledStringKey.LINE_HEIGHT,
82. styledValue: this.lineHeightStyle1
83. },
84. {
85. start: 32,
86. length: 5,
87. styledKey: StyledStringKey.PARAGRAPH_STYLE,
88. styledValue: this.paragraphStyleAttr2
89. },
90. {
91. start: 32,
92. length: 20,
93. styledKey: StyledStringKey.LINE_HEIGHT,
94. styledValue: this.lineHeightStyle1
95. },
96. {
97. start: 60,
98. length: 5,
99. styledKey: StyledStringKey.PARAGRAPH_STYLE,
100. styledValue: this.paragraphStyleAttr3
101. },
102. {
103. start: 60,
104. length: 5,
105. styledKey: StyledStringKey.LINE_HEIGHT,
106. styledValue: this.lineHeightStyle1
107. }
108. ]);
109. controller: TextController = new TextController();

111. async onPageShow() {
112. this.controller.setStyledString(this.paragraphStyledString1);
113. }

115. build() {
116. Row() {
117. Column({ space: 5 }) {
118. Text(undefined, { controller: this.controller })
119. .width(240)
120. .borderWidth(1)
121. .copyOption(CopyOptions.InApp)
122. .draggable(true)

124. // 查询段落样式
125. Text()
126. .onClick(() => {
127. let styles = this.paragraphStyledString1.getStyles(0, this.paragraphStyledString1.length);
128. if (styles.length !== 0) {
129. for (let i = 0; i < styles.length; i++) {
130. console.info('paragraphStyledString1 style object start:' + styles[i].start);
131. console.info('paragraphStyledString1 style object length:' + styles[i].length);
132. console.info('paragraphStyledString1 style object key:' + styles[i].styledKey);
133. if (styles[i].styledKey === 200) {
134. let paraAttr = styles[i].styledValue as ParagraphStyle;
135. console.info('paragraphStyledString1 textAlign:' + paraAttr.textAlign);
136. console.info('paragraphStyledString1 textIndent:' + paraAttr.textIndent);
137. console.info('paragraphStyledString1 maxLines:' + paraAttr.maxLines);
138. console.info('paragraphStyledString1 wordBreak:' + paraAttr.wordBreak);
139. console.info('paragraphStyledString1 leadingMargin:' + paraAttr.leadingMargin);
140. console.info('paragraphStyledString1 overflow:' + paraAttr.overflow);
141. }
142. }
143. }
144. })
145. .margin({ top: 10 })
146. }
147. .width('100%')
148. }
149. .height('100%')
150. }
151. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/rnqbZnj8QLWE3c-lEJ8vYg/zh-cn_image_0000002552959822.png?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=F1170E4BE43F55A07CC6A490AD42F5A664689FD2B753FD83A8763DCD0C363CDF)

### 示例6（设置自定义绘制Span）

从API version 12开始，该示例通过[CustomSpan](ts-universal-styled-string.md#customspan)接口和[measureTextSize](arkts-apis-uicontext-measureutils.md#measuretextsize12)实现属性字符串设置自定义绘制Span。

```
1. // xxx.ets
2. import { drawing } from '@kit.ArkGraphics2D';
3. import { LengthMetrics } from '@kit.ArkUI';

5. let gUIContext: UIContext;

7. class MyCustomSpan extends CustomSpan {
8. constructor(word: string, width: number, height: number) {
9. super();
10. this.word = word;
11. this.width = width;
12. this.height = height;
13. }

15. onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics {
16. this.setPx(gUIContext.vp2px(2));
17. let textSize = gUIContext.getMeasureUtils().measureTextSize({ textContent: this.word, fontSize: this.wordFontSize })
18. this.width = textSize.width as number;
19. this.height = textSize.height as number;
20. return {
21. width: gUIContext.px2vp(this.width) + (this.paddingLeft + this.paddingRight) * 2,
22. height: gUIContext.px2vp(this.height) + this.paddingTop + this.paddingBottom
23. };
24. }

26. onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
27. let canvas = context.canvas;

29. const brush = new drawing.Brush();
30. brush.setColor({
31. alpha: 255,
32. red: 0,
33. green: 74,
34. blue: 175
35. });
36. const font = new drawing.Font();
37. font.setSize(gUIContext.vp2px(this.wordFontSize));
38. const textBlob = drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
39. canvas.attachBrush(brush);
40. canvas.drawRect({
41. // 绘制的矩形在Span占位大小的范围里居中
42. left: options.x + gUIContext.vp2px(this.paddingLeft),
43. right: options.x + this.width + 2 * gUIContext.vp2px(this.paddingLeft) + gUIContext.vp2px(this.paddingRight),
44. top: options.lineTop,
45. bottom: options.baseline
46. });

48. brush.setColor({
49. alpha: 255,
50. red: 23,
51. green: 169,
52. blue: 141
53. });
54. canvas.attachBrush(brush);
55. // 文字在绘制的矩形里居中
56. canvas.drawTextBlob(textBlob, options.x + 2 * gUIContext.vp2px(this.paddingLeft),
57. options.baseline - gUIContext.vp2px(this.paddingBottom));
58. canvas.detachBrush();
59. }

61. setWord(word: string) {
62. this.word = word;
63. }

65. setPx(px: number) {
66. this.paddingLeft = px;
67. this.paddingRight = px;
68. this.paddingTop = px;
69. this.paddingBottom = px;
70. }

72. width: number = 160;
73. word: string = "drawing";
74. height: number = 10;
75. paddingLeft: number = 0;
76. paddingRight: number = 0;
77. paddingTop: number = 0;
78. paddingBottom: number = 0;
79. wordFontSize: number = 20;
80. }

82. @Entry
83. @Component
84. struct styled_string_set_customspan_demo {
85. customSpan1: MyCustomSpan = new MyCustomSpan("Hello", 80, 10);
86. customSpan2: MyCustomSpan = new MyCustomSpan("World", 80, 40);
87. style: MutableStyledString = new MutableStyledString(this.customSpan1);
88. textController: TextController = new TextController();
89. isPageShow: boolean = true;

91. aboutToAppear() {
92. gUIContext = this.getUIContext();
93. }

95. async onPageShow() {
96. if (!this.isPageShow) {
97. return;
98. }
99. this.isPageShow = false;

101. this.style.appendStyledString(new MutableStyledString("文本绘制 示例代码 CustomSpan", [
102. {
103. start: 0,
104. length: 5,
105. styledKey: StyledStringKey.FONT,
106. styledValue: new TextStyle({ fontColor: Color.Pink })
107. }, {
108. start: 5,
109. length: 5,
110. styledKey: StyledStringKey.FONT,
111. styledValue: new TextStyle({ fontColor: Color.Orange, fontStyle: FontStyle.Italic })
112. }, {
113. start: 10,
114. length: 500,
115. styledKey: StyledStringKey.FONT,
116. styledValue: new TextStyle({ fontColor: Color.Green, fontWeight: FontWeight.Bold })
117. }
118. ]));
119. this.style.appendStyledString(new StyledString(this.customSpan2));
120. this.style.appendStyledString(new StyledString("自定义绘制", [{
121. start: 0,
122. length: 5,
123. styledKey: StyledStringKey.FONT,
124. styledValue: new TextStyle({ fontColor: Color.Green, fontSize: LengthMetrics.px(50) })
125. }]));
126. this.textController.setStyledString(this.style);
127. }

129. build() {
130. Row() {
131. Column() {
132. Text(undefined, { controller: this.textController })
133. .copyOption(CopyOptions.InApp)
134. .fontSize(30)

136. Button("invalidate").onClick(() => {
137. this.customSpan1.setWord("你好");
138. this.customSpan1.invalidate();
139. })
140. }
141. .width('100%')
142. }
143. .height('100%')
144. }
145. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/2_Pv_XuQQhyW5NORL8NT5Q/zh-cn_image_0000002583479823.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=5D49EB7F2CB4F920B81046FAE10E7C51BBF4E0C82E062432D7B6DB34DD6FFE9D)

### 示例7（支持存储自定义扩展信息）

从API version 12开始，该示例通过[UserDataSpan](ts-universal-styled-string.md#userdataspan)接口实现属性字符串支持存储自定义扩展信息的功能。

```
1. // xxx.ets
2. class MyUserDataSpan extends UserDataSpan {
3. constructor(name: string, age: number) {
4. super();
5. this.name = name;
6. this.age = age;
7. }

9. name: string;
10. age: number;
11. }

13. @Entry
14. @Component
15. struct styled_string_set_userdataspan_demo {
16. @State name: string = "world";
17. @State age: number = 10;
18. controller: TextController = new TextController();
19. styleString: MutableStyledString = new MutableStyledString("hello world", [{
20. start: 0,
21. length: 11,
22. styledKey: StyledStringKey.USER_DATA,
23. styledValue: new MyUserDataSpan("hello", 21)
24. }]);

26. onPageShow(): void {
27. this.controller.setStyledString(this.styleString);
28. }

30. build() {
31. Column() {
32. Text(undefined, { controller: this.controller })
33. Button("get user data").onClick(() => {
34. let arr = this.styleString.getStyles(0, this.styleString.length);
35. let userDataSpan = arr[0].styledValue as MyUserDataSpan;
36. this.name = userDataSpan.name;
37. this.age = userDataSpan.age;
38. })
39. Text("name:" + this.name + "  age: " + this.age)
40. }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/kyOQBXSwSLSziCjYRiruVg/zh-cn_image_0000002552800174.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=81B76F43E363E54E0A15B2637FA15E83BFAB1092F9A2A6E3A76F2C551E5783CA)

### 示例8（设置超链接）

从API version 14开始，该示例通过[UrlStyle](ts-universal-styled-string.md#urlstyle14)接口，实现了对属性字符串中超链接设置的支持。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct styled_string_set_urlstyle_demo {
5. urlString: UrlStyle = new UrlStyle("https://www.example.com");
6. mutableStyledString: MutableStyledString = new MutableStyledString("Hello World", [{
7. start: 0,
8. length: "Hello".length,
9. styledKey: StyledStringKey.URL,
10. styledValue: this.urlString
11. }]);
12. controller: TextController = new TextController();

14. async onPageShow() {
15. this.controller.setStyledString(this.mutableStyledString);
16. }

18. build() {
19. Column() {
20. Column() {
21. Text(undefined, { controller: this.controller }).key('mutableStyledString').fontSize(30)
22. }
23. }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/PqLIY30tRxGuZUxqeHSs5w/zh-cn_image_0000002583439869.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=177BA83F462BE5684472C62FE79B8C0B3AE775D06AEABDAC30B9B4F7A05F6900)

### 示例9 （给图片设置colorFilter）

从API version 15开始，该示例通过给[ImageAttachment](ts-universal-styled-string.md#imageattachmentinterface对象说明)设置colorFilter实现了给图像设置颜色滤镜效果。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. import { drawing, common2D } from '@kit.ArkGraphics2D';

5. @Entry
6. @Component
7. struct styled_string_set_image_colorfilter_demo {
8. @State message: string = 'Hello World';
9. mutableStr: MutableStyledString = new MutableStyledString('origin image:');
10. mutableStr2: MutableStyledString = new MutableStyledString('with filter:');
11. controller: TextController = new TextController();
12. controller2: TextController = new TextController();
13. private color: common2D.Color = {
14. alpha: 125,
15. red: 125,
16. green: 125,
17. blue: 255
18. };

20. build() {
21. Row() {
22. Column({ space: 5 }) {
23. Text(undefined, { controller: this.controller })
24. .copyOption(CopyOptions.InApp)
25. .draggable(true)
26. .fontSize(30)
27. .onAppear(() => {
28. this.mutableStr = new MutableStyledString(new ImageAttachment({
29. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
30. resourceValue: $r('app.media.startIcon'),
31. size: { width: 50, height: 50 },
32. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
33. verticalAlign: ImageSpanAlignment.BASELINE,
34. objectFit: ImageFit.Contain,
35. syncLoad: true
36. }));
37. this.controller.setStyledString(this.mutableStr);
38. })
39. Text(undefined, { controller: this.controller2 })
40. .copyOption(CopyOptions.InApp)
41. .draggable(true)
42. .fontSize(30)
43. Button('set image color filter')
44. .onClick(() => {
45. this.mutableStr2 = new MutableStyledString(new ImageAttachment({
46. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
47. resourceValue: $r('app.media.startIcon'),
48. size: { width: 50, height: 50 },
49. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
50. verticalAlign: ImageSpanAlignment.BASELINE,
51. objectFit: ImageFit.Contain,
52. colorFilter: drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN),
53. syncLoad: true
54. }));
55. this.controller2.setStyledString(this.mutableStr2);
56. })
57. }
58. .width('100%')
59. }
60. .height('100%')
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/TtzN4Pv2TsChas3wxq0WhA/zh-cn_image_0000002552959824.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=19BE272E448A6A2F6998FFBB6B0E9D41E31771B67AB9085D9A95CAC198D86241)

### 示例10（属性字符串的插入、删除、替换）

从API version 12开始，该示例通过[subStyledString](ts-universal-styled-string.md#substyledstring)、[removeString](ts-universal-styled-string.md#removestring)、[removeStyle](ts-universal-styled-string.md#removestyle)、[clearStyles](ts-universal-styled-string.md#clearstyles)、[replaceStyledString](ts-universal-styled-string.md#replacestyledstring)、[insertStyledString](ts-universal-styled-string.md#insertstyledstring)接口实现属性字符串的插入、删除、替换。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct styled_string_modify_demo {
5. @State message: string = 'Hello World';
6. mutableStr: MutableStyledString = new MutableStyledString('123456', [{
7. start: 0,
8. length: 2,
9. styledKey: StyledStringKey.FONT,
10. styledValue: new TextStyle({ fontColor: Color.Red })
11. }, {
12. start: 0,
13. length: 3,
14. styledKey: StyledStringKey.DECORATION,
15. styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough })
16. }]);
17. mutableStr2: MutableStyledString = new MutableStyledString('with filter:');
18. controller: TextController = new TextController();
19. controller2: TextController = new TextController();

21. build() {
22. Row() {
23. Column({ space: 5 }) {
24. Text(undefined, { controller: this.controller })
25. .copyOption(CopyOptions.InApp)
26. .draggable(true)
27. .fontSize(30)
28. .onAppear(() => {
29. this.controller.setStyledString(this.mutableStr);
30. })
31. Text(undefined, { controller: this.controller2 })
32. .copyOption(CopyOptions.InApp)
33. .draggable(true)
34. .fontSize(30)
35. Button('GetSubStyledString (0,3)').onClick(() => {
36. this.controller2.setStyledString(this.mutableStr.subStyledString(0, 3));
37. })
38. Button('RemoveStyle (0,1,Decoration)').onClick(() => {
39. this.mutableStr.removeStyle(0, 1, StyledStringKey.DECORATION);
40. this.controller.setStyledString(this.mutableStr);
41. })
42. Button('RemoveString (5,1)').onClick(() => {
43. this.mutableStr.removeString(5, 1);
44. this.controller.setStyledString(this.mutableStr);
45. })
46. Button('ClearStyles').onClick(() => {
47. this.mutableStr.clearStyles();
48. this.controller.setStyledString(this.mutableStr);
49. })
50. Button('replaceStyledString').onClick(() => {
51. this.mutableStr.replaceStyledString(3, 1, new StyledString("abc", [{
52. start: 0,
53. length: 3,
54. styledKey: StyledStringKey.FONT,
55. styledValue: new TextStyle({ fontColor: Color.Blue })
56. }]));
57. this.controller.setStyledString(this.mutableStr);
58. })
59. Button('insertStyledString').onClick(() => {
60. this.mutableStr.insertStyledString(4, new StyledString("A"));
61. this.controller.setStyledString(this.mutableStr);
62. })
63. }
64. .width('100%')
65. }
66. .height('100%')
67. }
68. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/VTVH4-ReRra_tYdq3e8paw/zh-cn_image_0000002583479825.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=5B89EF974ABF1377A8824E1EE311349ED17962FCBC20E2FECBB6A9EFC91EEFF2)

### 示例11（属性字符串的文本描边）

从API version 20开始，该示例通过[TextStyle](ts-universal-styled-string.md#textstyle)设置strokeWidth和strokeColor接口实现属性字符串的文本描边。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct styled_string_strokewidth_strokecolor_demo {
7. @State string1: string = "Hello";
8. spanStyle: SpanStyle = {
9. start: 0,
10. length: 5,
11. styledKey: StyledStringKey.FONT,
12. styledValue: new TextStyle({
13. fontColor: '#ff2787d9',
14. strokeWidth: LengthMetrics.px(-5),
15. strokeColor: Color.Black,
16. fontWeight: FontWeight.Bolder,
17. fontSize: LengthMetrics.px(100)
18. })
19. };
20. spanStyle1: SpanStyle = {
21. start: 0,
22. length: 5,
23. styledKey: StyledStringKey.FONT,
24. styledValue: new TextStyle({
25. fontColor: '#ff2787d9',
26. strokeWidth: LengthMetrics.px(5),
27. strokeColor: Color.Black,
28. fontWeight: FontWeight.Bolder,
29. fontSize: LengthMetrics.px(100)
30. })
31. };

33. mutableStyledString: MutableStyledString = new MutableStyledString(this.string1, []);
34. controller: TextController = new TextController();

36. mutableStyledString1: MutableStyledString = new MutableStyledString(this.string1, []);
37. controller1: TextController = new TextController();

39. async onPageShow() {
40. this.mutableStyledString.setStyle(this.spanStyle)
41. this.controller.setStyledString(this.mutableStyledString);

43. this.mutableStyledString1.setStyle(this.spanStyle1)
44. this.controller1.setStyledString(this.mutableStyledString1);
45. }

47. build() {
48. Column() {
49. // 实心字
50. Text(undefined, { controller: this.controller })
51. .margin({ top: 10, bottom: 50 })
52. .draggable(true)
53. .onDragStart(() => {
54. })
55. // 空心字
56. Text(undefined, { controller: this.controller1 })
57. .margin({ top: 10, bottom: 50 })
58. .draggable(true)
59. .onDragStart(() => {
60. })
61. }
62. .height('100%')
63. .width('100%')
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/rxPRSgrEStmuiAsu12800w/zh-cn_image_0000002552800176.png?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=ACD7B703A6A8B3BB0689FA016BEE72D430816983A9703361723C283C09E70E6B)

### 示例12（fromHtml和toHtml互相转换）

该示例通过[fromHtml](ts-universal-styled-string.md#fromhtml)（从API version 12开始）、[toHtml](ts-universal-styled-string.md#tohtml14)（从API version 14开始）接口，将HTML中strong、b20+、em20+、i20+、u20+、del20+、s20+、a20+、sub20+、sup20+标签及其style属性中的background-color转换为属性字符串并转回HTML。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct styled_string_html_convert_demo {
5. @State html: string = "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span style = \"foreground-color:blue\"> <a href='https://www.example.com'>www.example</a> </span> <span style=\"background-color: red;\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>"; // 从API version 20开始支持b、em、i、u、del、s、a、sup、sub标签
6. @State spanString: StyledString | undefined = undefined;
7. @State resultText: string = ""; // 保存结果文本的状态
8. controller: TextController = new TextController;

10. build() {
11. Column() {
12. // 显示转换后的spanString
13. Text(undefined, { controller: this.controller }).height(100)

15. // TextArea显示每个步骤的结果
16. TextArea({ text: this.html })
17. .width("100%")
18. .height(100)
19. .margin(5)

21. // 按钮1:将HTML转换为SpanString
22. Button("Convert HTML to SpanString").onClick(async () => {
23. this.spanString = await StyledString.fromHtml(this.html);
24. this.controller.setStyledString(this.spanString);
25. this.resultText = "Converted HTML to SpanString successfully.";
26. }).margin(5)

28. // 按钮2:将SpanString转换为HTML
29. Button("Convert SpanString to HTML").onClick(() => {
30. if (this.spanString) {
31. // 将spanString转换为HTML并替换当前的HTML状态
32. const newHtml = StyledString.toHtml(this.spanString);
33. if (newHtml !== this.html) { // 通过检查内容是否已经相同来防止重复
34. this.html = newHtml;
35. }
36. this.resultText = "Converted SpanString to HTML successfully.";
37. } else {
38. this.resultText = "SpanString is undefined.";
39. }
40. }).margin(5)

42. // 按钮3:将HTML转换回SpanString
43. Button("Convert HTML to SpanString").onClick(async () => {
44. this.spanString = await StyledString.fromHtml(this.html);
45. this.controller.setStyledString(this.spanString);
46. this.resultText = "Converted HTML back to SpanString successfully.";
47. }).margin(5)

49. // 重置：重置HTML和SpanString
50. Button("Reset").onClick(() => {
51. this.html = "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span style = \"foreground-color:blue\"> <a href='https://www.example.com'>www.example</a> </span> <span style=\"background-color: red;\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>";
52. this.spanString = undefined;
53. this.controller.setStyledString(new StyledString("")); // 使用空的StyledString实例
54. this.resultText = "Reset HTML and SpanString successfully.";
55. }).margin(5)
56. }.width("100%").padding(20)
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/SIGJNqJWRoaeBXCojY35hQ/zh-cn_image_0000002583439871.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=4ACC8F09221398F6196B95AFB564B780799F231B31C055A212ACDEC878C70839)

### 示例13（多装饰线与加粗装饰线）

从API version 20开始，该示例通过[DecorationStyle](ts-universal-styled-string.md#decorationstyle)中设置enableMultiType、thicknessScale接口，实现多装饰线显示与加粗装饰线的效果。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI'
3. @Entry
4. @Component
5. struct styled_string_set_decorationstyle_demo {
6. @State styledString : StyledString | undefined = undefined
7. controller : TextController = new TextController
8. thickness: number = 2.0
9. mutableStyledString1: MutableStyledString = new MutableStyledString("1234567890", [
10. {
11. start: 0,
12. length: 10,
13. styledKey: StyledStringKey.FONT,
14. styledValue: new TextStyle({ fontColor: Color.Orange, fontSize: LengthMetrics.vp(30) })
15. },
16. {
17. start: 0,
18. length: 4,
19. styledKey: StyledStringKey.DECORATION,
20. styledValue: new DecorationStyle({type: TextDecorationType.LineThrough, thicknessScale: this.thickness}, {enableMultiType: true})
21. },
22. {
23. start: 2,
24. length: 5,
25. styledKey: StyledStringKey.DECORATION,
26. styledValue: new DecorationStyle({type: TextDecorationType.Underline, thicknessScale: this.thickness}, {enableMultiType: true})
27. },
28. {
29. start: 0,
30. length: 4,
31. styledKey: StyledStringKey.DECORATION,
32. styledValue: new DecorationStyle({type: TextDecorationType.Overline, thicknessScale: this.thickness}, {enableMultiType: true})
33. },
34. {
35. start: 6,
36. length: 2,
37. styledKey: StyledStringKey.DECORATION,
38. styledValue: new DecorationStyle({type: TextDecorationType.LineThrough})
39. },
40. {
41. start: 7,
42. length: 2,
43. styledKey: StyledStringKey.DECORATION,
44. styledValue: new DecorationStyle({type: TextDecorationType.LineThrough, color: Color.Green}, {enableMultiType: true})
45. },
46. {
47. start: 8,
48. length: 2,
49. styledKey: StyledStringKey.DECORATION,
50. styledValue: new DecorationStyle({type: TextDecorationType.Overline, color: Color.Green}, {enableMultiType: true})
51. }
52. ]);
53. build() {
54. Column({ space:3 }) {
55. Text(undefined, { controller: this.controller })
56. .height(100)
57. .copyOption(CopyOptions.LocalDevice)
58. .onAppear(()=>{
59. this.styledString = this.mutableStyledString1
60. this.controller.setStyledString(this.mutableStyledString1)
61. })
62. }.width("100%")
63. }
64. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/HfDZHsVxSkSgC7tQKpJXpw/zh-cn_image_0000002552959826.png?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=9291641F30DA2BA1D40BE1302E6A69DCB29C50145E62E2ADA1FA0461D125719E)

### 示例14（获取以vp为单位的图片尺寸）

从API version 21开始，该示例通过[ImageAttachmentInterface](ts-universal-styled-string.md#imageattachmentinterface对象说明)实现属性字符串设置图片，并且获取该图片以vp为单位的尺寸。

```
1. // xxx.ets
2. import { image } from '@kit.ImageKit';
3. import { LengthMetrics } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct styled_string_demo4 {
8. @State message: string = "Image info: \n";
9. imagePixelMap: image.PixelMap | undefined = undefined;
10. @State mutableStr: MutableStyledString = new MutableStyledString("");
11. controller: TextController = new TextController();

13. async aboutToAppear() {
14. this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.startIcon'));
15. }

17. private async updateImageInfoStr() {
18. this.message = "Image info: \n";
19. let imageArray = this.mutableStr.getStyles(0, this.mutableStr.length, StyledStringKey.IMAGE);
20. for (let i = 0; i < imageArray.length; ++i) {
21. this.message += (' Image ' + i + ':\n');
22. if (imageArray[i].styledKey === StyledStringKey.IMAGE) {
23. let attachment = imageArray[i].styledValue as ImageAttachment;
24. if (attachment.size !== undefined) {
25. let w: number = attachment.size.width as number;
26. let h: number = attachment.size.height as number;
27. this.message += ('    px size  width = ' + w.toFixed(2) + ' \theight = ' + h.toFixed(2) + '\n');
28. }
29. if (attachment.sizeInVp !== undefined) {
30. let w: number = attachment.sizeInVp.width as number;
31. let h: number = attachment.sizeInVp.height as number;
32. this.message += ('    sizeInVp width = ' + w.toFixed(2) + ' \theight = ' + h.toFixed(2) + '\n\n');
33. }
34. }
35. }
36. }

38. private async getPixmapFromMedia(resource: Resource) {
39. let unit8Array =
40. await this.getUIContext()?.getHostContext()?.resourceManager?.getMediaContent(resource.id);
41. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
42. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
43. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
44. });
45. await imageSource.release();
46. return createPixelMap;
47. }

49. build() {
50. Row() {
51. Column({ space: 5 }) {
52. Text(undefined, { controller: this.controller })
53. .copyOption(CopyOptions.InApp)
54. .draggable(true)
55. .fontSize(30)
56. Button('设置图片 50vp x 50vp')
57. .onClick(() => {
58. if (this.imagePixelMap !== undefined) {
59. this.mutableStr.appendStyledString(new MutableStyledString(new ImageAttachment({
60. value: this.imagePixelMap,
61. size: { width: 50, height: 50 },
62. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
63. verticalAlign: ImageSpanAlignment.BASELINE,
64. objectFit: ImageFit.Contain
65. })));
66. this.controller.setStyledString(this.mutableStr);
67. this.updateImageInfoStr();
68. }
69. }).margin(10)
70. Button('设置图片 70vp x 70vp')
71. .onClick(() => {
72. if (this.imagePixelMap !== undefined) {
73. this.mutableStr.appendStyledString(new MutableStyledString(new ImageAttachment({
74. value: this.imagePixelMap,
75. size: { width: 70, height: 70 },
76. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
77. verticalAlign: ImageSpanAlignment.BASELINE,
78. objectFit: ImageFit.Contain
79. })));
80. this.controller.setStyledString(this.mutableStr);
81. this.updateImageInfoStr();
82. }
83. }).margin(10)
84. Text(this.message).width("80%").padding(30)
85. }
86. .width('100%')
87. }
88. .height('100%')
89. }
90. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/lqv7E3rbQv68vClqHFhvKw/zh-cn_image_0000002583479827.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=CB0E5E85263C05E5F57DEF86A595EDC97448FBF03F33E9C36A625A6D961EE879)

### 示例15（设置段落自定义缩进）

从API version 22开始，该示例通过[LeadingMarginSpan](ts-universal-styled-string.md#leadingmarginspan22)设置段落缩进，并且自定义缩进图案。

```
1. // xxx.ets
2. import { drawing } from '@kit.ArkGraphics2D';
3. import { LengthMetrics } from '@kit.ArkUI';

5. /**
6. * 实现LeadingMarginSpan
7. */
8. class MyLeadingMarginSpan extends LeadingMarginSpan {
9. text: string = ""

11. constructor(text: string) {
12. super()
13. this.text = text
14. }

16. getText() {
17. return this.text;
18. }

20. // 返回缩进距离
21. getLeadingMargin(): LengthMetrics {
22. console.info("getLeadingMargin")
23. return LengthMetrics.vp(10)
24. }

26. // 回调给开发者行信息，用于canvas绘制
27. onDraw(context: DrawContext, options: LeadingMarginSpanDrawInfo) {
28. console.info("x = " + options.x + options.direction + ", top = " + options.top
29. + ", bottom = " + options.bottom + ", baseline = " + options.baseline
30. + ", direction = " + ", start = " + options.start + ", end = " + options.end + ", first = " + options.first)
31. let canvas = context.canvas;
32. if (!options.first) {
33. return
34. }

36. // 绘制文本符号
37. const font = new drawing.Font();
38. font.setSize(20);
39. const textBlob = drawing.TextBlob.makeFromString(this.text, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
40. canvas.drawTextBlob(textBlob, options.x - 30, options.top + (options.bottom - options.top) / 2);
41. }
42. }

44. @Entry
45. @Component
46. struct leadingMarginSpanDemo {
47. controller: RichEditorStyledStringController = new RichEditorStyledStringController();
48. options: RichEditorStyledStringOptions = { controller: this.controller };
49. textController: TextController = new TextController();
50. leadingMarginSpan: LeadingMarginSpan = new MyLeadingMarginSpan("●");
51. paragraphStyleAttr2: ParagraphStyle =
52. new ParagraphStyle({ leadingMarginSpan: this.leadingMarginSpan });
53. style: StyledString = new StyledString("段落标题\n段落内容101234567890123456789012345678901234567890123456789",
54. [
55. {
56. start: 0,
57. length: 10,
58. styledKey: StyledStringKey.PARAGRAPH_STYLE,
59. styledValue: this.paragraphStyleAttr2
60. }
61. ]
62. );

64. build() {
65. Column() {
66. Text(undefined, { controller: this.textController })
67. .width("90%")
68. .height("20%")
69. .margin({ top: 10 })
70. .borderWidth(1)
71. .copyOption(CopyOptions.InApp)
72. .draggable(true)

74. RichEditor(this.options)
75. .width("90%")
76. .height("20%")
77. .margin({ top: 10 })
78. .borderWidth(1)
79. Column() {
80. Button('setStyledString')
81. .onClick(() => {
82. this.textController.setStyledString(this.style);
83. this.controller.setStyledString(this.style);
84. }).margin({ top: 10 })
85. // 查询段落样式
86. Button("getStyles")
87. .onClick(() => {
88. let styles = this.style.getStyles(0, this.style.length);
89. if (styles.length == 0) {
90. return
91. }
92. for (let i = 0; i < styles.length; i++) {
93. console.info('getStyles style object start:' + styles[i].start);
94. console.info('getStyles style object length:' + styles[i].length);
95. console.info('getStyles style object key:' + styles[i].styledKey);
96. if (styles[i].styledKey === 200) {
97. let paraAttr = styles[i].styledValue as ParagraphStyle;
98. console.info('getStyles leadingMarginSpan:' + paraAttr.leadingMarginSpan);
99. let leadingMarginSpanClass = paraAttr.leadingMarginSpan as MyLeadingMarginSpan
100. if (leadingMarginSpanClass != null) {
101. console.info('getStyles leadingMarginSpan getText: ' + leadingMarginSpanClass.getText());
102. }
103. }
104. }
105. }).margin({ top: 10 })
106. }
107. }
108. .width('100%')
109. }
110. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/FIBfCmbwQR2SPu4TYdlagg/zh-cn_image_0000002552800178.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=5042CDC047731290B0C5D425E98A63D1C35D57528AFED09AD4A0947E77B5CD02)

### 示例16（使用supportSvg2属性时，SVG图片的显示效果）

从API version 22开始，该示例通过给[ResourceImageAttachmentOptions](ts-universal-styled-string.md#resourceimageattachmentoptions15)设置supportSvg2属性，使[SVG标签解析能力增强功能](ts-image-svg2-capabilities.md#svg易用性提升)的SVG易用性提升能力生效。

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. import { LengthMetrics } from '@kit.ArkUI';
3. @Entry
4. @Component
5. struct styled_string_process_demo {
6. controller: TextController = new TextController();
7. controller1: TextController = new TextController();
8. imageAttachment: ImageAttachment = new ImageAttachment({
9. // $r("app.media.ice")需要替换为开发者所需的图像资源文件。
10. resourceValue: $r("app.media.ice"),
11. size: { width: 50, height: 50 },
12. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
13. verticalAlign: ImageSpanAlignment.BASELINE,
14. objectFit: ImageFit.Contain,
15. syncLoad: true,
16. supportSvg2: true,
17. colorFilter: drawing.ColorFilter.createBlendModeColorFilter(
18. drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN)
19. })
20. imageAttachment1: ImageAttachment = new ImageAttachment({
21. // $r("app.media.ice")需要替换为开发者所需的图像资源文件。
22. resourceValue: $r("app.media.ice"),
23. size: { width: 50, height: 50 },
24. layoutStyle: { borderRadius: LengthMetrics.vp(10) },
25. verticalAlign: ImageSpanAlignment.BASELINE,
26. objectFit: ImageFit.Contain,
27. syncLoad: true,
28. supportSvg2: false,
29. colorFilter: drawing.ColorFilter.createBlendModeColorFilter(
30. drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN)
31. })
32. scroller: Scroller = new Scroller();
33. mutableStr: MutableStyledString = new MutableStyledString('');
34. mutableStr1: MutableStyledString = new MutableStyledString('');
35. aboutToAppear() {
36. this.mutableStr = new MutableStyledString(this.imageAttachment);
37. this.controller.setStyledString(this.mutableStr);
38. this.mutableStr1 = new MutableStyledString(this.imageAttachment1);
39. this.controller1.setStyledString(this.mutableStr1);
40. }

42. build() {
43. Column() {
44. Scroll(this.scroller) {
45. Column() {
46. Text('属性字符串不支持svg2')
47. Text(undefined, { controller: this.controller1 })
48. .draggable(true)
49. .fontSize(30)
50. Text('属性字符串支持svg2')
51. Text(undefined, { controller: this.controller })
52. .draggable(true)
53. .fontSize(30)
54. }.width('100%')
55. }
56. }
57. .width('100%')
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/nKQONGAyQ02YERO0j-t_LA/zh-cn_image_0000002583479815.png?HW-CC-KV=V1&HW-CC-Date=20260428T000153Z&HW-CC-Expire=86400&HW-CC-Sign=4FD630D3E64EF4020BDCBACEDEBF852C33708B5B88E2071ABE37EAC566564479)
