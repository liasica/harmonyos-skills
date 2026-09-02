---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common
title: 文本组件公共接口
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > 文本组件公共接口
category: harmonyos-references
scraped_at: 2026-09-02T15:01:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:47a62c80868a37d9f0accfd243a71bd6d97034b3e4f8b8e2cff2c80bf2ba9cf9
---

**说明** 

* 本模块首批接口从API version 10开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 文本类组件公共接口提供了文本处理的基础能力，包括光标样式设置、布局管理、文本选择控制、菜单项定制等功能。该模块适用于需要对文本组件进行精细控制的场景，例如文本编辑器、富文本应用、输入表单等。通过这些接口，开发者可以自定义光标样式、获取文本布局信息、处理文本选择、定制编辑菜单等，提升应用的文本交互体验。

## CaretStyle10+

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | [Length](ts-types.md#length) | 否 | 是 | 光标尺寸，不支持百分比。  默认值：'2vp' |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 光标颜色。  默认值：'#ff007dff'，表示蓝色。 |

## LayoutManager12+

布局管理器对象。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的布局信息。

### 导入对象

以Text组件为例，完整示例请参考Text组件的[示例10（获取文本信息）](ts-basic-components-text.md#示例10获取文本信息)。

```ts
controller: TextController = new TextController();
let layoutManager: LayoutManager = this.controller.getLayoutManager();
```

### getLineCount12+

getLineCount(): number

获取组件内容的总行数。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的总行数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 组件内容的总行数。当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，返回0。 |

### getGlyphPositionAtCoordinate12+

getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity

获取较为接近给定坐标的字符位置信息。

**说明** 

* 本接口实际获取的是UTF-16字符偏移量，而非字形偏移量。
* 文本内容变更后，需等待布局完成才可获取到最新的位置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 相对于组件的横坐标。  单位：[px](ts-pixel-units.md#基本像素单位) |
| y | number | 是 | 相对于组件的纵坐标。  单位：[px](ts-pixel-units.md#基本像素单位) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PositionWithAffinity](ts-text-common.md#positionwithaffinity12) | 字符位置信息。当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，返回无效值。 |

### getCharacterPositionAtCoordinate24+

getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined

获取距离指定坐标最近的字符的位置信息。

**说明** 

* 文本内容变更后，需等待布局完成才可获取到最新的位置信息。
* 本接口返回的字符位置为UTF-8编码偏移量。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 相对于组件的横坐标。  单位：[px](ts-pixel-units.md#基本像素单位) |
| y | number | 是 | 相对于组件的纵坐标。  单位：[px](ts-pixel-units.md#基本像素单位) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PositionWithAffinity](ts-text-common.md#positionwithaffinity12) | undefined | 字符的位置信息。当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，该接口会返回undefined。 |

### getCharacterPositionAtCoordinate

getCharacterPositionAtCoordinate(x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined

根据指定编码类型，获取距离指定坐标最近的字符位置信息。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的位置信息。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 相对于组件的横坐标。  单位：[px](ts-pixel-units.md#基本像素单位) |
| y | number | 是 | 相对于组件的纵坐标。  单位：[px](ts-pixel-units.md#基本像素单位) |
| encoding | [TextEncoding](ts-text-common.md#textencoding) | 否 | 字符位置使用的编码类型。UTF-8编码时，字符位置以字节为单位；UTF-16编码时，字符位置以UTF-16码元为单位。  默认值：TextEncoding.TEXT\_ENCODING\_UTF8 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PositionWithAffinity](ts-text-common.md#positionwithaffinity12) | undefined | 字符的位置信息。当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，该接口会返回undefined。 |

### getGlyphRangeForCharacterRange24+

getGlyphRangeForCharacterRange(charRange: [TextRange](ts-text-common.md#textrange12)): Array<[TextRange](ts-text-common.md#textrange12)> | undefined

根据给定的文本字符范围来获取范围内的字形范围，以及实际的字符范围。本接口的字符偏移量为UTF-8编码。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的字形范围信息。

以文本“世界Hello”为例，UTF-8编码下其字形索引与字符索引的对应关系如下：

| 文本 | 世 | 界 | H | e | l | l | o |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 字形索引范围 | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |
| 字符索引范围（UTF-8） | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] | [10, 11] |

其中文本“世”的字形索引范围为[0, 1]，一个汉字占3个字节，所以其对应的字符索引范围为[0, 3]。如果指定的字符索引范围是[0, 1]，但无法解析出三分之一个汉字，所以实际的字符索引范围是[0, 3]。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| charRange | [TextRange](ts-text-common.md#textrange12) | 是 | 文本的字符范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextRange](ts-text-common.md#textrange12)> | undefined | 数组中含有两个元素，第一个元素是字形范围，第二个元素是实际的字符范围。  当返回的范围是异常值时，范围内元素为-1。  当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，该接口会返回undefined。 |

### getGlyphRangeForCharacterRange

getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined

根据指定编码类型和文本字符范围，获取字形范围以及实际的字符范围。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的字形范围信息。

以文本“世界Hello”为例，不同编码类型下其字形索引与字符索引的对应关系如下：

| 文本 | 世 | 界 | H | e | l | l | o |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 字形索引范围 | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |
| 字符索引范围（UTF-8） | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] | [10, 11] |
| 字符索引范围（UTF-16） | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |

UTF-8编码时，一个汉字占3个字节，“世”的字形索引范围为[0, 1]，其对应的字符索引范围为[0, 3]。如果指定的字符索引范围是[0, 1]，但无法解析出三分之一个汉字，所以实际的字符索引范围是[0, 3]。

UTF-16编码时，字符索引以UTF-16码元为单位，BMP字符（如“世”）占1个码元（2个字节），补充平面字符（如emoji）占2个码元（4字节代理对）。“世”的字形索引范围为[0, 1]，其对应的字符索引范围为[0, 1]。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| charRange | [TextRange](ts-text-common.md#textrange12) | 是 | 文本的字符范围。 |
| encoding | [TextEncoding](ts-text-common.md#textencoding) | 否 | 字符范围使用的编码类型。UTF-8编码时，字符索引以字节为单位；UTF-16编码时，字符索引以UTF-16码元为单位。  默认值：TextEncoding.TEXT\_ENCODING\_UTF8 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextRange](ts-text-common.md#textrange12)> | undefined | 数组中含有两个元素，第一个元素是字形范围，第二个元素是实际的字符范围。  当返回的范围是异常值时，范围内元素为-1。  当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，该接口会返回undefined。 |

### getCharacterRangeForGlyphRange24+

getCharacterRangeForGlyphRange(glyphRange: [TextRange](ts-text-common.md#textrange12)): Array<[TextRange](ts-text-common.md#textrange12)> | undefined

根据给定的文本字形范围来获取范围内的字符范围，以及实际的字形范围。本接口的字符偏移量为UTF-8编码。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的字符范围信息。

以文本“世界Hello”为例，UTF-8编码下其字形索引与字符索引的对应关系如下：

| 文本 | 世 | 界 | H | e | l | l | o |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 字形索引范围 | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |
| 字符索引范围（UTF-8） | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] | [10, 11] |

其字形索引范围为[0, 7]，一个汉字占3个字节，所以其对应的字符索引范围为[0, 11]。如果指定的字形索引范围是[0, 11]，但字形一共只有7个，所以实际的字形索引范围是[0, 7]。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| glyphRange | [TextRange](ts-text-common.md#textrange12) | 是 | 文本的字形范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextRange](ts-text-common.md#textrange12)> | undefined | 数组中含有两个元素，第一个元素是字符范围，第二个元素是实际的字形范围。  当返回的范围是异常值时，范围内元素为-1。  当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，该接口会返回undefined。 |

### getCharacterRangeForGlyphRange

getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined

根据指定编码类型和文本字形范围，获取字符范围以及实际的字形范围。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的字符范围信息。

以文本“世界Hello”为例，不同编码类型下其字形索引与字符索引的对应关系如下：

| 文本 | 世 | 界 | H | e | l | l | o |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 字形索引范围 | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |
| 字符索引范围（UTF-8） | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] | [10, 11] |
| 字符索引范围（UTF-16） | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |

UTF-8编码时，其字形索引范围为[0, 7]，一个汉字占3个字节，对应的字符索引范围为[0, 11]。如果指定的字形索引范围超出实际字形数量（如[0, 11]），由于字形一共只有7个，返回的实际字形索引范围为[0, 7]。

UTF-16编码时，字符索引以UTF-16码元为单位，BMP字符（如“世”）占1个码元（2个字节），补充平面字符（如emoji）占2个码元（4字节代理对）。其字形索引范围为[0, 7]，对应的字符索引范围为[0, 7]。如果指定的字形索引范围超出实际字形数量（如[0, 10]），由于字形一共只有7个，返回的实际字形索引范围为[0, 7]。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| glyphRange | [TextRange](ts-text-common.md#textrange12) | 是 | 文本的字形范围。 |
| encoding | [TextEncoding](ts-text-common.md#textencoding) | 否 | 字符范围使用的编码类型。UTF-8编码时，字符索引以字节为单位；UTF-16编码时，字符索引以UTF-16码元为单位。  默认值：TextEncoding.TEXT\_ENCODING\_UTF8 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextRange](ts-text-common.md#textrange12)> | undefined | 数组中含有两个元素，第一个元素是字符范围，第二个元素是实际的字形范围。  当返回的范围是异常值时，范围内元素为-1。  当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，该接口会返回undefined。 |

### getLineMetrics12+

getLineMetrics(lineNumber: number): LineMetrics

获取指定行的行信息、文本样式信息、以及字体属性信息。

**说明** 

文本内容变更后，需等待布局完成才可获取到最新的行信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lineNumber | number | 是 | 行号，取值范围[0, 实际行数-1]，从0开始。当行号小于0或超出实际行数时，返回无效值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LineMetrics](ts-text-common.md#linemetrics12) | 行信息、文本样式信息、以及字体属性信息。  当行号小于0或超出实际行数，返回无效值。当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，返回无效值。 |

### getRectsForRange14+

getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>

根据给定的矩形区域宽度样式和高度样式，获取文本中任意区间范围内的字符或占位符所占的绘制区域信息。

**说明** 

* 文本内容变更后，需等待布局完成才可获取到最新的绘制区域信息。
* 参数range的[TextRange](ts-text-common.md#textrange12)为UTF-16字符偏移量。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [TextRange](ts-text-common.md#textrange12) | 是 | 需要获取的区域的文本区间。 |
| widthStyle | [RectWidthStyle](ts-text-common.md#rectwidthstyle14) | 是 | 返回的矩形区域的宽度规格，用于控制返回矩形的宽度计算方式，不同规格值会影响矩形的宽度边界。 |
| heightStyle | [RectHeightStyle](ts-text-common.md#rectheightstyle14) | 是 | 返回的矩形区域的高度规格，用于控制返回矩形的高度计算方式，不同规格值会影响矩形的高度边界。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextBox](ts-text-common.md#textbox14)> | 矩形区域数组。当[LayoutManager](ts-text-common.md#layoutmanager12)没有和组件绑定时，返回空数组。 |

## PositionWithAffinity12+

位置以及亲和度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | number | 否 | 否 | 字形或字符相对于组件内容的索引，整数。 |
| affinity | [Affinity](ts-text-common.md#affinity12) | 否 | 否 | 位置亲和度，表示光标位置在字形边界处的倾向性，具体取值请参见Affinity枚举。 |

## TextMenuItemId12+

自定义菜单项的Id值。用于识别菜单选项，内置菜单项Id值见下列属性表格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| CUT | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 默认剪切，为一级菜单项。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COPY | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 默认复制，为一级菜单项。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PASTE | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 默认粘贴，为一级菜单项。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SELECT\_ALL | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 默认全选，为一级菜单项。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COLLABORATION\_SERVICE | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 互通服务，为一级菜单项。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CAMERA\_INPUT | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 拍摄输入，为一级菜单项。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| AI\_WRITER13+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 小艺帮写。可对选中的文本进行润色、摘要提取、排版等，为一级菜单项。该菜单项依赖大模型能力，否则不生效。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| TRANSLATE15+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 翻译，为一级菜单项。对选中的文本提供翻译服务。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| SHARE18+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 分享，为一级菜单项。对选中的文本提供分享服务，拉起分享窗口分享选中文本内容。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| SEARCH18+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 搜索，为一级菜单项。对选中的文本提供搜索服务，拉起浏览器搜索选中文本内容。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| url20+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 打开链接，为一级菜单项。对选中的URL提供跳转服务，拉起浏览器搜索或者应用页面。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| email20+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 新建邮件，为一级菜单项。对选中的邮箱地址提供跳转服务，拉起邮箱应用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| phoneNumber20+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 呼叫，为一级菜单项。对选中的电话号码提供跳转服务，拉起电话拨号页面。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| address20+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 导航前往，为一级菜单项。对选中的地址提供跳转服务，拉起地图应用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| dateTime20+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 新建日程，为一级菜单项。对选中的日期和时间提供跳转服务，拉起新建日程页面。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| askAI20+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 问问小艺。对选中的文本提供AI问询能力，为一级菜单项。该菜单项依赖大模型能力，否则不生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| autoFill23+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 自动填充，为一级菜单项。点击后会展开二级菜单项“密码保险箱”，仅支持[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)或[RichEditor](ts-basic-components-richeditor.md)。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| passwordVault23+ | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 否 | 密码保险箱，为二级菜单项。点击该菜单项后会拉起密码保险箱应用，该应用提供自动填充账号密码能力，仅支持[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)或[RichEditor](ts-basic-components-richeditor.md)。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

### of

static of(id: ResourceStr): TextMenuItemId

根据id创建TextMenuItemId。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | [ResourceStr](ts-types.md#resourcestr) | 是 | 菜单项标识，用于创建TextMenuItemId对象以识别菜单选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 根据传入id创建的菜单项标识对象，用于识别菜单选项。 |

### equals

equals(id: TextMenuItemId): boolean

判断TextMenuItemId是否相等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 是 | 需要比较的TextMenuItemId对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 两个TextMenuItemId是否相等。  true表示相等，false表示不相等。 |

## TextMenuItem12+对象说明

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 菜单名称。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 菜单图标。  不支持网络图片。  默认值：undefined，不显示菜单图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| id | [TextMenuItemId](ts-text-common.md#textmenuitemid12) | 否 | 否 | 菜单id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| labelInfo15+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 快捷键提示。  该字段仅2in1设备支持。  默认值：undefined，不显示快捷键提示。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## EditMenuOptions

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onPrepareMenu20+ | [OnPrepareMenuCallback](ts-text-common.md#onpreparemenucallback20) | 否 | 是 | 当文本选择区域变化后显示菜单之前触发该回调，可在该回调中进行菜单数据设置。  与[onCreateMenu](ts-text-common.md#oncreatemenu12)功能相似但触发时机不同：onCreateMenu在菜单创建时触发，适用于初始化菜单项；本接口在每次选择区域变化后、菜单显示前触发，适用于根据选择内容动态调整菜单。两者可同时使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

### onCreateMenu12+

onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem>

在菜单创建时触发该回调，可在该回调中进行菜单数据设置。入参和返回值只包含一级菜单项，不包含二级菜单项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menuItems | Array<[TextMenuItem](ts-text-common.md#textmenuitem12对象说明)> | 是 | 将要显示的菜单项。  **说明：**  对默认菜单项的名称、图标、快捷键提示修改不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextMenuItem](ts-text-common.md#textmenuitem12对象说明)> | 处理后的菜单项。 |

### onMenuItemClick12+

onMenuItemClick(menuItem: TextMenuItem, range: TextRange): boolean

在菜单项被点击时触发该回调，用于处理菜单项的点击行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menuItem | [TextMenuItem](ts-text-common.md#textmenuitem12对象说明) | 是 | 菜单项。  **说明：**  从API version 23开始，对于具备可展开二级菜单能力的一级菜单项，例如自动填充，仅执行系统默认逻辑，不会执行用户自定义逻辑。 |
| range | [TextRange](ts-text-common.md#textrange12) | 是 | 选中的文本信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 菜单项的执行逻辑。  返回为true，拦截系统默认逻辑，仅执行自定义逻辑。  返回为false，先执行自定义逻辑，再执行系统逻辑。 |

## OnPrepareMenuCallback20+

type OnPrepareMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>

当文本选择区域变化后显示菜单之前触发该回调，可在该回调中进行菜单数据设置。入参和返回值只包含一级菜单项，不包含二级菜单项。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menuItems | Array<[TextMenuItem](ts-text-common.md#textmenuitem12对象说明)> | 是 | 将要显示的菜单项。  **说明：**  对默认菜单项的名称、图标、快捷键提示修改不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextMenuItem](ts-text-common.md#textmenuitem12对象说明)> | 处理后的菜单项。 |

## TextRange12+

文本范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 起始索引，从0开始。 |
| end | number | 否 | 是 | 结束索引，从0开始。 |

## EditableTextOnChangeCallback12+

type EditableTextOnChangeCallback = (value: string, previewText?: PreviewText, options?: TextChangeOptions) => void

输入内容发生变化时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 文本框内正式上屏的文本内容。 |
| previewText | [PreviewText](ts-text-common.md#previewtext12) | 否 | 预上屏文本信息，包含预上屏起始位置和文本内容。 |
| options15+ | [TextChangeOptions](ts-text-common.md#textchangeoptions15对象说明) | 否 | 文本内容变化信息，包含文本的选中区范围、文本框内正式上屏的文本内容、预上屏文本内容。 |

## TextDataDetectorType11+枚举说明

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHONE\_NUMBER | 0 | 电话号码 |
| URL | 1 | 链接 |
| EMAIL | 2 | 邮箱 |
| ADDRESS | 3 | 地址 |
| DATE\_TIME12+ | 4 | 日期时间 |

## TextDeleteDirection12+枚举说明

定义删除文本方向。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKWARD | 0 | 向后删除。 |
| FORWARD | 1 | 向前删除。 |

## SuperscriptStyle20+枚举说明

定义文本上下角标样式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通文本样式。 |
| SUPERSCRIPT | 1 | 上标文本样式。 |
| SUBSCRIPT | 2 | 下标文本样式。 |

## MenuType13+枚举说明

菜单类型。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECTION\_MENU | 0 | 文本选择菜单。 |
| PREVIEW\_MENU | 1 | 图片预览菜单。 |

## KeyboardAppearance15+枚举说明

键盘外观。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE\_IMMERSIVE | 0 | 默认外观模式，不采用沉浸式风格。 |
| IMMERSIVE | 1 | 沉浸式模式，跟随系统。 |
| LIGHT\_IMMERSIVE | 2 | 浅色沉浸式风格。 |
| DARK\_IMMERSIVE | 3 | 深色沉浸式风格。 |

## IncrementalUpdatePolicy

文本渲染的增量更新策略。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不启用增量更新，采用全量布局渲染。 |
| PARAGRAPH\_CACHE | 1 | 启用增量更新，使用段落级缓存。该策略生效的前提是文本绑定的属性字符串对象保持不变，若属性字符串对象发生变化则无法命中缓存。 |

## InsertValue12+对象说明

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| insertOffset | number | 否 | 否 | 插入的值的位置索引，从0开始。 |
| insertValue | string | 否 | 否 | 插入的值。 |

## DeleteValue12+对象说明

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deleteOffset | number | 否 | 否 | 删除的值的位置索引，从0开始。 |
| direction | [TextDeleteDirection](ts-text-common.md#textdeletedirection12枚举说明) | 否 | 否 | 删除值的方向。 |
| deleteValue | string | 否 | 否 | 删除的值。 |

## TextDataDetectorConfig11+对象说明

该配置只支持[Text](ts-basic-components-text.md)组件和[RichEditor](ts-basic-components-richeditor.md)组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| types | [TextDataDetectorType](ts-text-common.md#textdatadetectortype11枚举说明)[] | 否 | 否 | 设置文本识别的实体类型。设置types为null或者[]时，识别所有类型的实体，否则只识别指定类型的实体。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDetectResultUpdate | Callback<string> | 否 | 是 | 文本识别成功后，触发onDetectResultUpdate回调。  默认值：undefined，不触发回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| color12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置文本识别成功后的实体颜色。  默认值：'#ff0a59f7'，表示蓝色（不透明度为100%）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| decoration12+ | [DecorationStyleInterface](ts-universal-styled-string.md#decorationstyleinterface) | 否 | 是 | 设置文本识别成功后的实体装饰线样式。  默认值：  {  type: TextDecorationType.Underline,  color: 与实体颜色一致,  style: TextDecorationStyle.SOLID  }  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enablePreviewMenu20+ | boolean | 否 | 是 | 设置是否开启文本识别长按显示预览菜单。true表示开启，false表示未开启。  默认值：false  当[copyOptions](ts-basic-components-richeditor.md#copyoptions)设置为None时，若enablePreviewMenu设置为true，长按AI实体也不能显示预览菜单。  **设备行为差异：** 本接口实际支持的设备类型范围（Phone、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、TV、Car、Wearable）。因硬件形态限制，该接口在PC/2in1、TV、Car、Wearable设备中调用功能不生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## PreviewText12+

预上屏信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 否 | 预上屏内容的起始位置索引，从0开始。 |
| value | string | 否 | 否 | 预上屏的内容。 |

## FontSettingOptions12+对象说明

字体配置项。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableVariableFontWeight | boolean | 否 | 是 | 是否启用可变字重调节。字体配置项作为[fontWeight](ts-basic-components-text.md#fontweight12)接口的入参，fontWeight接口中weight取值为[100, 900]内非整百数值时，enableVariableFontWeight用于设置weight的值是否生效。  默认值：false  true：启用可变字重调节。此时如果weight取值为[100, 900]范围内任意整数，字重取值为weight，否则取默认值400。  false：禁用可变字重调节。此时如果weight取值为[100, 900]范围内的整百数值，字重取值为weight；weight是非整百数值时，字重取默认值400。 |

## FontConfigs24+对象说明

字体配置项。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontWeightConfigs | [FontWeightConfigs](ts-text-common.md#fontweightconfigs24对象说明) | 否 | 是 | 字体粗细配置。默认值继承[FontWeightConfigs](ts-text-common.md#fontweightconfigs24对象说明)。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## FontWeightConfigs24+对象说明

字体粗细配置项。当传入该配置对象时（包括空对象{}），未显式设置的属性将使用默认值。当传入null或undefined时，不应用默认值，字体粗细行为与父组件文本保持一致。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableVariableFontWeight | boolean | 否 | 是 | 是否启用可变字重调节。当设置字体粗细的值weight为[100, 900]内非整百数值时，enableVariableFontWeight用于设置weight的值是否生效。  默认值：false  true：启用可变字重调节。此时如果weight取值为[100, 900]范围内任意整数，字重取值为weight，否则取默认值400。  false：禁用可变字重调节。此时如果weight取值为[100, 900]范围内的整百数值，字重取值为weight；weight是非整百数值时，字重取默认值400。 |
| enableDeviceFontWeightCategory | boolean | 否 | 是 | 是否随设备的字体粗细级别自动更新字重。  默认值：true  true：当设备的字体粗细级别发生变化时，字重会自动更新。  false：当设备的字体粗细级别发生变化时，字重不会自动更新。 |

## OnDidChangeCallback12+

type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void

文本变化后回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rangeBefore | [TextRange](ts-text-common.md#textrange12) | 是 | 文本变化前将要被替换的文本范围。 |
| rangeAfter | [TextRange](ts-text-common.md#textrange12) | 是 | 文本变化后新增内容的文本范围。 |

## StyledStringChangedListener12+

属性字符串的文本内容变化监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onWillChange | Callback<[StyledStringChangeValue](ts-text-common.md#styledstringchangevalue12), boolean> | 否 | 是 | 文本内容将要变化回调函数。  默认值：null，不触发回调。  返回true表示允许文本内容变更，返回false表示阻止文本内容变更。 |
| onDidChange | [OnDidChangeCallback](ts-text-common.md#ondidchangecallback12) | 否 | 是 | 文本内容完成变化回调函数。  默认值：null，不触发回调。 |

## StyledStringChangeValue12+

属性字符串的文本变化信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| range | [TextRange](ts-text-common.md#textrange12) | 否 | 否 | 即将被替换的属性字符串子串在原字符串中的范围。 |
| replacementString | [StyledString](ts-universal-styled-string.md#styledstring) | 否 | 否 | 用于替换的属性字符串。 |
| previewText | [StyledString](ts-universal-styled-string.md#styledstring) | 否 | 是 | 预览内容属性字符串。  默认值：null，表示无预览内容。  该属性用于表示语音输入、拍摄输入、输入法预上屏场景下的未提交上屏的临时输入内容。 |

## AutoCapitalizationMode20+枚举说明

自动大小写模式类型，只提供接口能力，具体实现由输入法应用决定。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 默认状态，不进行自动大小写处理。 |
| WORDS | 1 | 按单词自动大小写，即输入单词的首个字符大写，其他字符小写。 |
| SENTENCES | 2 | 按句子自动大小写，即输入句子的首个字符大写，其他字符小写。 |
| ALL\_CHARACTERS | 3 | 按全字符自动大小写。 |

## TextBaseController12+

文本选择控制器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setSelection12+

setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

支持设置组件内的内容选中，选中部分背板高亮。

selectionStart和selectionEnd均为-1时表示全选。

未获焦时调用该接口不产生选中效果。

从API version 12开始，在PC/2in1设备中，无论options取何值，调用setSelection接口都不会弹出菜单，此外，如果组件中已经存在菜单，调用setSelection接口会关闭菜单。

在非2in1设备中，options取值为MenuPolicy.DEFAULT时，遵循以下规则：

1. 组件内有手柄菜单时，接口调用后不关闭菜单，并且调整菜单位置。
2. 组件内有不带手柄的菜单时，接口调用后不关闭菜单，并且菜单位置不变。
3. 组件内无菜单时，接口调用后也无菜单显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 选中开始位置。  取值小于0时，按0处理。取值大于文本长度时，按当前文本长度处理。  特殊取值效果：当selectionStart和selectionEnd均为-1时，表示全选。 |
| selectionEnd | number | 是 | 选中结束位置。  取值小于0时，按0处理。取值大于文本长度时，按当前文本长度处理。  特殊取值效果：当selectionStart和selectionEnd均为-1时，表示全选。 |
| options | [SelectionOptions](ts-universal-attributes-text-style.md#selectionoptions12对象说明) | 否 | 选择项配置。 默认值继承[SelectionOptions](ts-universal-attributes-text-style.md#selectionoptions12对象说明)。 |

### closeSelectionMenu12+

closeSelectionMenu(): void

关闭自定义选择菜单或系统默认选择菜单。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getLayoutManager12+

getLayoutManager(): LayoutManager

获取布局管理器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LayoutManager](ts-text-common.md#layoutmanager12) | 布局管理器对象，用于获取文本布局信息，如行数、行度量、字形位置等。 |

## TextEditControllerEx12+

文本扩展编辑控制器。

继承自[TextBaseController](ts-text-common.md#textbasecontroller12)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### isEditing12+

isEditing(): boolean

获取当前富文本的编辑状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true为编辑态，false为非编辑态。 |

### stopEditing12+

stopEditing(): void

退出编辑态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getCaretOffset12+

getCaretOffset(): number

返回当前光标所在位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前光标所在位置。 |

### setCaretOffset12+

setCaretOffset(offset: number): boolean

设置光标偏移位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 光标偏移位置，取值范围[0, 文本长度]。超出所有内容范围时，设置失败。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 光标是否设置成功。  true表示光标设置成功，false表示设置失败。 |

### getPreviewText12+

getPreviewText?(): PreviewText

获取预上屏信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PreviewText](ts-text-common.md#previewtext12) | 预上屏信息，包含预上屏起始位置索引和预上屏文本内容。 |

## StyledStringController12+

定义StyledString控制器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setStyledString12+

setStyledString(styledString: StyledString): void

设置富文本组件显示的属性字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styledString | [StyledString](ts-universal-styled-string.md#styledstring) | 是 | 属性字符串。  **说明：**  StyledString的子类[MutableStyledString](ts-universal-styled-string.md#mutablestyledstring)也可以作为入参值。 |

### getStyledString12+

getStyledString(): MutableStyledString

获取富文本组件显示的属性字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MutableStyledString](ts-universal-styled-string.md#mutablestyledstring) | 富文本组件显示的属性字符串。 |

## DecorationStyleResult12+

后端返回的文本装饰线样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TextDecorationType](ts-appendix-enums.md#textdecorationtype) | 否 | 否 | 装饰线类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 装饰线颜色。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| style | [TextDecorationStyle](ts-appendix-enums.md#textdecorationstyle12) | 否 | 是 | 装饰线样式。  默认值：TextDecorationStyle.SOLID  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| thicknessScale20+ | number | 否 | 是 | 装饰线粗细缩放比例。  默认值：1.0  取值范围：[0, +∞)  **说明：** 负值按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## LineMetrics12+

type LineMetrics = import('../api/@ohos.graphics.text').default.LineMetrics

用于描述文本布局中单行文字的度量信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.graphics.text').default.[LineMetrics](js-apis-graphics-text.md#linemetrics) | 用于描述文本布局中单行文字的度量信息。 |

## Affinity12+

type Affinity = import('../api/@ohos.graphics.text').default.Affinity

位置亲和度枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.graphics.text').default.[Affinity](js-apis-graphics-text.md#affinity) | 位置亲和度枚举。 |

## TextBox14+

type TextBox = import('../api/@ohos.graphics.text').default.TextBox

文本矩形区域。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.graphics.text').default.[TextBox](js-apis-graphics-text.md#textbox) | 文本矩形区域。 |

## Paragraph20+

type Paragraph = import('../api/@ohos.graphics.text').default.Paragraph

保存文本内容及样式的载体，支持排版与绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.graphics.text').default.[Paragraph](js-apis-graphics-text.md#paragraph) | 保存文本内容及样式的载体，支持排版与绘制操作。 |

## RectHeightStyle14+

type RectHeightStyle = import('../api/@ohos.graphics.text').default.RectHeightStyle

矩形区域高度规格枚举。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.graphics.text').default.[RectHeightStyle](js-apis-graphics-text.md#rectheightstyle) | 矩形区域高度规格枚举。 |

## RectWidthStyle14+

type RectWidthStyle = import('../api/@ohos.graphics.text').default.RectWidthStyle

矩形区域宽度规格枚举。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.graphics.text').default.[RectWidthStyle](js-apis-graphics-text.md#rectwidthstyle) | 矩形区域宽度规格枚举。 |

## TextEncoding

文本布局查询接口支持的文本编码类型。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT\_ENCODING\_UTF8 | 0 | UTF-8编码。 |
| TEXT\_ENCODING\_UTF16 | 1 | UTF-16编码。 |

## TextChangeOptions15+对象说明

文本变化相关信息，包括变化前后的选区范围、变化前的文本内容等。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rangeBefore | [TextRange](ts-text-common.md#textrange12) | 否 | 否 | 变化前的选区范围。 |
| rangeAfter | [TextRange](ts-text-common.md#textrange12) | 否 | 否 | 变化后的选区范围。 |
| oldContent | string | 否 | 否 | 变化前的文本内容。 |
| oldPreviewText | [PreviewText](ts-text-common.md#previewtext12) | 否 | 否 | 变化前的预上屏信息。 |

## EditableTextChangeValue15+

文本变化的详细信息，包括预上屏。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | 否 | 否 | 当前的文本内容。 |
| previewText | [PreviewText](ts-text-common.md#previewtext12) | 否 | 是 | 预上屏的内容信息。  默认值：undefined，表示无预上屏内容。 |
| options | [TextChangeOptions](ts-text-common.md#textchangeoptions15对象说明) | 否 | 是 | 变化的文本内容信息。  默认值：undefined。 |

## TextMenuShowMode16+

菜单的显示模式。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 显示在当前窗口中。 |
| PREFER\_WINDOW | 1 | 优先显示在独立窗口中，若不支持独立窗口，则显示在当前窗口中。  **说明：**  除应用主窗口、应用子窗口、系统模态窗口及系统桌面类型的窗口外，其他类型的窗口不支持将文本选择菜单显示在独立窗口中。  在预览器中不支持将文本选择菜单显示在独立窗口中。  在[UIExtension](js-apis-arkui-uiextension.md)中不支持将文本选择菜单显示在独立窗口中。  当文本类组件已经显示在子窗类型的[Popup](ohos-arkui-advanced-popup.md)、[Dialog](ohos-arkui-advanced-dialog.md)、[Toast](../harmonyos-guides/arkts-create-toast.md)、[Menu](ts-basic-components-menu.md)中时，不支持将其对应的文本选择菜单显示在独立窗口中。  当TextInput、TextArea可支持拉起AutoFill时，不支持将其对应的文本选择菜单显示在独立窗口中。 |

## TextMenuOptions16+对象说明

菜单选项。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showMode | [TextMenuShowMode](ts-text-common.md#textmenushowmode16) | 否 | 是 | 菜单的显示模式。  默认值：TextMenuShowMode.DEFAULT |

## ShaderStyle20+

文本着色器效果基类。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## LinearGradientStyle20+

显示为线性渐变。LinearGradientStyle继承自[ShaderStyle](ts-text-common.md#shaderstyle20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [LinearGradientOptions](ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明) | 否 | 否 | 显示为线性渐变效果。 |

### constructor20+

constructor(options: LinearGradientOptions)

用于创建LinearGradientStyle对象的构造函数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LinearGradientOptions](ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明) | 是 | 显示为线性渐变效果。  [LinearGradientOptions](ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明)中的direction默认值按[GradientDirection](ts-appendix-enums.md#gradientdirection)中的NONE处理。 |

## RadialGradientStyle20+

显示为径向渐变。RadialGradientStyle继承自[ShaderStyle](ts-text-common.md#shaderstyle20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [RadialGradientOptions](ts-universal-attributes-gradient-color.md#radialgradientoptions18对象说明) | 否 | 否 | 显示为径向渐变效果。 |

### constructor20+

constructor(options: RadialGradientOptions)

用于创建RadialGradientStyle对象的构造函数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RadialGradientOptions](ts-universal-attributes-gradient-color.md#radialgradientoptions18对象说明) | 是 | 显示为径向渐变效果。 |

## ColorShaderStyle20+

显示为纯色。ColorShaderStyle继承自[ShaderStyle](ts-text-common.md#shaderstyle20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 显示为纯色效果。 |

### constructor20+

constructor(color: ResourceColor)

用于创建ColorShaderStyle对象的构造函数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 显示为纯色效果。 |

## IMEClient20+对象说明

输入控件绑定输入法客户端类型。

### 属性

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nodeId | number | 否 | 否 | 当前输入控件的组件UniqueId。取值范围大于等于0。 |

### setExtraConfig22+

setExtraConfig(config: InputMethodExtraConfig): void

设置输入法扩展信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [InputMethodExtraConfig](ts-text-common.md#inputmethodextraconfig22) | 是 | 输入法扩展信息。 |

## MaxLinesOptions20+对象说明

配置TextArea组件，文本超长时的显示效果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| overflowMode | [MaxLinesMode](ts-text-common.md#maxlinesmode20) | 否 | 是 | overflowMode可配置[TextArea](ts-basic-components-textarea.md)组件的非内联模式。当超出设置的maxLines最大行数时，会启用滚动效果。需同时配置[textOverflow](ts-basic-components-textarea.md#textoverflow12)，且仅当textOverflow为None或Clip时，MaxLinesMode才能生效。默认情况下，MaxLinesMode的值为Clip，超出maxLines后文本会被截断。 |

## MaxLinesMode20+

TextArea组件在文本超长时显示效果。默认值为CLIP，按最大行截断显示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLIP | 0 | 文本超长时按最大行截断显示。 |
| SCROLL | 1 | 文本超长时可滚动显示。 |

## LineSpacingOptions20+对象说明

设置文本的行间距，是否仅在行与行之间生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onlyBetweenLines | boolean | 否 | 是 | 文本的行间距是否仅在行与行之间生效。  当设置为true时，行间距仅适用于行与行之间，首行上方和尾行下方无额外的行间距。当设置为false时，首行上方和尾行下方均会存在行间距。  默认值：false |

## TextVerticalAlign20+

文本垂直对齐的方式。默认值BASELINE，沿基线对齐。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASELINE | 0 | 对齐文本基线。 |
| BOTTOM | 1 | 对齐文本底部。 |
| CENTER | 2 | 垂直居中对齐。 |
| TOP | 3 | 对齐文本顶部。 |

## ContentTransition20+

文本动效基类。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NumericTextTransition20+

数字翻牌动效。仅限正整数，不支持小数和负数。不支持渐变色和Text跑马灯模式。不支持选中，[copyOption](ts-basic-components-text.md#copyoption9)属性无效。当文本存在子组件时或通过属性字符串设置时，数字翻牌失效。

NumericTextTransition继承自[ContentTransition](ts-text-common.md#contenttransition20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| flipDirection | [FlipDirection](ts-text-common.md#flipdirection20) | 否 | 是 | 翻牌方向。  默认值：FlipDirection.DOWN |
| enableBlur | boolean | 否 | 是 | 是否开启翻牌模糊效果。  默认值：false  true：开启翻牌模糊效果。  false：不开启翻牌模糊效果。 |

### constructor20+

constructor(options?: NumericTextTransitionOptions)

用于创建NumericTextTransition对象的构造函数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NumericTextTransitionOptions](ts-text-common.md#numerictexttransitionoptions20对象说明) | 否 | 设置数字翻牌动效。 默认值继承[NumericTextTransitionOptions](ts-text-common.md#numerictexttransitionoptions20对象说明)。 |

## NumericTextTransitionOptions20+对象说明

数字翻牌的参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| flipDirection | [FlipDirection](ts-text-common.md#flipdirection20) | 否 | 是 | 翻牌方向。  默认值：FlipDirection.DOWN |
| enableBlur | boolean | 否 | 是 | 是否开启翻牌模糊效果。  默认值：false  true：开启翻牌模糊效果。  false：不开启翻牌模糊效果。 |

## FlipDirection20+

翻牌方向。默认值为DOWN。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOWN | 0 | 内容往下翻。 |
| UP | 1 | 内容往上翻。 |

## TextLayoutOptions对象说明20+

文本布局选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| constraintWidth | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 设置被计算文本布局宽度。若不设置则宽度为单行布局所占最大宽度值。 |

## SelectedDragPreviewStyle23+对象说明

文本拖拽时的背板样式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 用于设置文本拖拽时的背板颜色。  默认值：跟随主题。默认主题时，浅色模式显示白色，深色模式显示黑色。 |

## TextContentAlign21+

文本内容区垂直对齐方向。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 0 | 内容区顶部对齐。 |
| CENTER | 1 | 内容区中心对齐。 |
| BOTTOM | 2 | 内容区底部对齐。 |

## StrokeJoinStyle

定义线条拐角的样式，即在绘制折线时线段拐角处的画笔样式。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MITER\_JOIN | 0 | 拐角类型为锐角。 |
| ROUND\_JOIN | 1 | 拐角类型为圆角。 |
| BEVEL\_JOIN | 2 | 拐角类型为平角。 |

## TextDirection22+

文本排版方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LTR | 0 | 文本排版方向从左到右。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| RTL | 1 | 文本排版方向从右到左。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| DEFAULT23+ | 2 | 文本排版方向遵循组件布局方向。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| AUTO23+ | 3 | 遵循自身实际文本内容的排版方向，如果文本为 RTL（Right-to-Left）类语言（如藏文、维吾尔文），文本排版方向为从右到左。如果为 LTR（Left-to-Right）类语言（如中文、英文），文本排版方向为从左到右。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## InputMethodExtraConfig22+

type InputMethodExtraConfig = import('../api/@ohos.inputMethod.ExtraConfig').InputMethodExtraConfig

输入法扩展信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.inputMethod.ExtraConfig').[InputMethodExtraConfig](js-apis-inputmethod-extraconfig.md#inputmethodextraconfig) | 输入法扩展信息。 |

## AccessibilitySpanOptions23+对象说明

Span的无障碍朗读功能属性。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍文本属性。组件无文本属性时，屏幕朗读选中此组件不会播报。设置该属性后可为此类组件设置无障碍文本，屏幕朗读时将播报该文本，帮助使用者明确选中了什么组件。  默认值：''  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明属性。此描述用于向用户详细解释当前组件，开发人员应提供详尽的文本说明，以协助用户理解即将执行的操作及其后果，尤其当这些后果无法仅从组件的属性和无障碍文本中直接获取时。  默认值：''  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | 无障碍重要性。用于设置组件是否可被无障碍辅助服务识别。  支持取值如下：  "auto"：当前组件由无障碍辅助服务和ArkUI进行综合判断组件是否可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务识别。  "no"：当前组件不可被无障碍辅助服务识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **说明：**  当accessibilityLevel设置成"auto"时，组件是否可被无障碍辅助服务所识别取决于以下多方面因素：  1. 组件是否可被识别由无障碍辅助服务内部判断，自行选择。  2. 若组件的父组件accessibilityGroup属性中isGroup设置为true，无障碍服务将不再关注其子组件内容，组件不可被无障碍辅助服务所识别。  3. 若组件的父组件accessibilityLevel属性设置为"no-hide-descendants"，组件不可被无障碍辅助服务所识别。 |

## FontVariation

type FontVariation = import('../api/@ohos.graphics.text').default.FontVariation

可变字体的属性。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.graphics.text').default.[FontVariation](js-apis-graphics-text.md#fontvariation) | 可变字体的属性。 |

## OnCreateMenuCallback

type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>

菜单创建时触发。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menuItems | Array<[TextMenuItem](ts-text-common.md#textmenuitem12对象说明)> | 是 | 当前显示的菜单项。  **说明：**  对默认菜单项的名称、图标、快捷键提示修改不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextMenuItem](ts-text-common.md#textmenuitem12对象说明)> | 处理后的菜单项。 |
