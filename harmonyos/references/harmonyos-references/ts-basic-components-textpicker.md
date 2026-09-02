---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker
title: TextPicker
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > TextPicker
category: harmonyos-references
scraped_at: 2026-09-02T15:01:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4d8985cdda681e65466c8988d328379777db585afe3a5ad7c222da2e761c398f
---

滑动选择文本、图片或图文混排内容的组件，用户可以按需创建单列数据选择器、多列非联动数据选择器和多列联动数据选择器，适用于需要用户从预设选项中选择数据的场景，如日期选择、地区选择、配置项设置等。组件支持循环滚动、自定义文本样式、分割线样式、渐隐效果、选择项高度调整、触控反馈、表冠灵敏度设置等特性，提供流畅的滑动交互体验和灵活的数据展示方式。

**说明** 

* 该组件从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该组件不建议开发者在动效过程中修改属性数据。
* 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。
* 多列非联动数据选择器和多列联动数据选择器在下文中统称为多列数据选择器。

## 子组件

该组件为基础组件，不建议包含子组件。

## 接口

TextPicker(options?: TextPickerOptions)

根据指定的数据列表创建文本选择器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明) | 否 | 配置文本选择器的参数。当需要自定义选择器的数据源、选中项、列宽等配置时传入此参数。参数缺省时组件无法显示。 |

## TextPickerOptions对象说明

文本选择器的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| range | string[] | string[][]10+ | [Resource](ts-types.md#resource) | [TextPickerRangeContent](ts-basic-components-textpicker.md#textpickerrangecontent10对象说明)[]10+ | [TextCascadePickerRangeContent](ts-basic-components-textpicker.md#textcascadepickerrangecontent10对象说明)[]10+ | 否 | 否 | 选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。  **说明**：  1. 单列数据选择器使用string[]，[Resource](ts-types.md#resource)，[TextPickerRangeContent](ts-basic-components-textpicker.md#textpickerrangecontent10对象说明)[]类型。  2. 多列非联动数据选择器使用string[][]类型。  3. 多列联动数据选择器使用[TextCascadePickerRangeContent](ts-basic-components-textpicker.md#textcascadepickerrangecontent10对象说明)[]类型。  4. Resource类型只支持[strarray.json](../harmonyos-guides/resource-categories-and-access.md#资源组目录)。  5. range的类型及列数不可以动态修改。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selected | number | number[]10+ | 否 | 是 | 设置选中项在数据选择列表中的索引值，索引从0开始。  默认值：0  **说明**：  1. 单列数据选择器使用number类型。  2. 多列非联动数据选择器使用number[]类型，数组长度与列数一致。  3. 多列联动数据选择器使用number[]类型，数组长度与层级数一致。  4. 从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  5. 未设置该属性或设置的值无效时，使用默认值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| value | [ResourceStr](ts-types.md#resourcestr) | [ResourceStr](ts-types.md#resourcestr)[] | 否 | 是 | 设置选中项的值，优先级低于selected。  默认值：数据选择列表中第一个元素的值。  **说明**：  1. 从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  2. 从API version 20开始，支持[Resource](ts-types.md#resource)类型。  3. 只有显示文本列表时该值有效。显示图片或图文混排的列表时，该值无效。  4. 单列数据选择器使用[ResourceStr](ts-types.md#resourcestr)类型。  5. 多列非联动数据选择器使用[ResourceStr](ts-types.md#resourcestr)[]类型，数组长度与列数一致。  6. 多列联动数据选择器使用[ResourceStr](ts-types.md#resourcestr)[]类型，数组长度与层级数一致。  7. 当selected和value均未设置，或selected值无效时，使用默认值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| columnWidths18+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)[] | 否 | 是 | 设置每一列的列宽。  默认值：每一列的列宽相等，为组件宽度除以列数。  **说明**：  1. 当文本长度大于列宽时，文本被截断。  2. 当设置为异常值时，使用默认值。  3. 支持设置为Undefined和Null，不支持Undefined[]和Null[]。  4. 当columnWidths数组长度与实际列数不匹配时，超出列数的列宽值将被忽略；未指定列宽的列将均分组件剩余可用宽度（组件宽度减去已指定列宽之和）。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## TextPickerRangeContent10+对象说明

单列数据选择器的数据选项内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | string | [Resource](ts-types.md#resource) | 否 | 否 | 图片资源。当icon为string类型时，表示图片存放的路径，例如"/common/hello.png"；当icon为Resource类型时，表示资源引用。 |
| text | string | [Resource](ts-types.md#resource) | 否 | 是 | 文本信息。  默认值：空字符串  **说明**：  1. 未设置该属性时，使用默认值。  2. 当文本长度大于列宽时，文本被截断。 |

## TextCascadePickerRangeContent10+对象说明

多列联动数据选择器的数据选项内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | [Resource](ts-types.md#resource) | 否 | 否 | 文本信息。  **说明**：当文本长度大于列宽时，文本被截断。 |
| children | [TextCascadePickerRangeContent](ts-basic-components-textpicker.md#textcascadepickerrangecontent10对象说明)[] | 否 | 是 | 联动数据。表示当前数据项的子选项数组，用于构建多列联动数据选择器的层级结构。数组的每个元素为[TextCascadePickerRangeContent](ts-basic-components-textpicker.md#textcascadepickerrangecontent10对象说明)类型，包含text和children属性，支持多级嵌套。当选择器支持多级联动时传入此参数；不传入时表示该选项没有子级数据。 |

## DividerOptions12+对象说明

分割线的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Dimension](ts-types.md#dimension10) | 否 | 是 | 分割线的线宽。  默认值：2.0px  单位：默认为vp，也可指定单位为px。  取值范围：[0, +∞)，strokeWidth小于0取默认值，最大不得超过列高的一半。不支持“百分比”类型。 |
| startMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | 分割线与TextPicker侧边起始端的距离。  默认值：0  单位：默认为vp，也可指定单位为px。  取值范围：[0, +∞)，startMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。  \*\*说明：\*\*当startMargin + endMargin超过组件宽度时，会被置0。 |
| endMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | 分割线与TextPicker侧边结束端的距离。  默认值：0  单位：默认为vp，也可指定单位为px。  取值范围：[0, +∞)，endMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。  \*\*说明：\*\*当startMargin + endMargin超过组件宽度时，会被置0。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线的颜色。  默认值：'#33000000' |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### defaultPickerItemHeight

defaultPickerItemHeight(value: number | string)

设置选择项的高度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 选择项的高度。  取值范围：  number类型：[0, +∞)，单位为vp。  string类型：仅支持number类型取值的字符串形式，例如"56"。  默认值：选中项56vp，非选中项36vp。  **说明：**  设置该参数后，选中项与非选中项的高度均为所设置的值。  当value的值为负数时，使用默认值。 |

### defaultPickerItemHeight18+

defaultPickerItemHeight(height: Optional<number | string>)

设置选择项的高度。与[defaultPickerItemHeight](ts-basic-components-textpicker.md#defaultpickeritemheight)相比，height参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | string> | 是 | 选择项的高度。  取值范围：  number类型：[0, +∞)，单位为vp。  string类型：仅支持number类型取值的字符串形式，例如"56"。  默认值：选中项56vp，非选中项36vp。  **说明：**  1. 设置该参数后，选中项与非选中项的高度均为所设置的值。  2. 当height的值为undefined时，维持上次取值。 |

### disappearTextStyle10+

disappearTextStyle(value: PickerTextStyle)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 边缘项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  **说明**：未调用该方法设置样式时，使用默认值。 |

**说明** 

若选中项向上或向下的可视项数低于两项则无对应边缘项。

### disappearTextStyle18+

disappearTextStyle(style: Optional<PickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。与[disappearTextStyle10+](ts-basic-components-textpicker.md#disappeartextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 边缘项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  当style的值为undefined时，使用默认值。 |

**说明** 

若选中项向上或向下的可视项数低于两项则无对应边缘项。

### disappearTextStyle20+

disappearTextStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[disappearTextStyle18+](ts-basic-components-textpicker.md#disappeartextstyle18)相比，style参数新增了对[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)|[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)> | 是 | 边缘项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.Clip  }  当style的值为undefined时，使用默认值。 |

**说明** 

若选中项向上或向下的可视项数低于两项则无对应边缘项。

### textStyle10+

textStyle(value: PickerTextStyle)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 待选项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  **说明**：未调用该方法设置样式时，使用默认值。 |

**说明** 

若选中项向上或向下可视项数低于一项则无对应待选项。

### textStyle18+

textStyle(style: Optional<PickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。与[textStyle10+](ts-basic-components-textpicker.md#textstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 待选项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  当style的值为undefined时，使用默认值。 |

**说明** 

若选中项向上或向下可视项数低于一项则无对应待选项。

### textStyle20+

textStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[textStyle18+](ts-basic-components-textpicker.md#textstyle18)相比，style参数新增了对[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)|[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)> | 是 | 待选项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.Clip  }  当style的值为undefined时，使用默认值。 |

**说明** 

若选中项向上或向下可视项数低于一项则无对应待选项。

### selectedTextStyle10+

selectedTextStyle(value: PickerTextStyle)

设置选中项的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  **说明**：未调用该方法设置样式时，使用默认值。 |

### selectedTextStyle18+

selectedTextStyle(style: Optional<PickerTextStyle>)

设置选中项的文本颜色、字号、字体粗细。与[selectedTextStyle10+](ts-basic-components-textpicker.md#selectedtextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  当style的值为undefined时，使用默认值。 |

### selectedTextStyle20+

selectedTextStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

设置选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[selectedTextStyle18+](ts-basic-components-textpicker.md#selectedtextstyle18)相比，style参数新增了对[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)|[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)> | 是 | 选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.Clip  }  当style的值为undefined时，使用默认值。 |

### selectedIndex10+

selectedIndex(value: number | number[])

设置选中项在数据选择列表中的索引值，优先级高于[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)中的"value"属性。单列数据选择器使用number类型。多列数据选择器使用number[]类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | number[] | 是 | 选中项在数据选择列表中的索引值，索引从0开始。  默认值：0  当value的值为负数或者超过数据选择列表的最大索引值时，使用默认值。 |

### selectedIndex18+

selectedIndex(index: Optional<number | number[]>)

设置选中项在数据选择列表中的索引值，优先级高于[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)中的"value"属性。单列数据选择器使用number类型，多列数据选择器使用number[]类型。与[selectedIndex10+](ts-basic-components-textpicker.md#selectedindex10)相比，index参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | number[]> | 是 | 选中项在数据选择列表中的索引值，索引从0开始。  默认值：0  当index的值为undefined时，使用[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)中的selected值。  当index的值为负数或者超过数据选择列表的最大索引值时，使用默认值。 |

### canLoop10+

canLoop(value: boolean)

设置是否可循环滚动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否可循环滚动。  - true：可循环。  - false：不可循环。  默认值：true |

### canLoop18+

canLoop(isLoop: Optional<boolean>)

设置是否可循环滚动。与[canLoop10+](ts-basic-components-textpicker.md#canloop10)相比，isLoop参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLoop | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否可循环滚动。  - true：可循环。  - false：不可循环。  默认值：true  当isLoop的值为undefined时，使用默认值。 |

### divider12+

divider(value: DividerOptions | null)

设置分割线样式，不设置该属性则按“默认值”展示分割线。

[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)中startMargin + endMargin 超过组件宽度后，startMargin和endMargin会被置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明) | null | 是 | 分割线样式。当需要自定义分割线的线宽、边距、颜色时传入DividerOptions对象；当需要隐藏分割线时传入null；不传入时使用默认样式。  默认值：  {  strokeWidth: '2px',  startMargin: 0,  endMargin: 0,  color: '#33000000'  }  1. 当value设置为有效的[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)时，按设置的样式显示分割线。  2. 当value设置为null时，不显示分割线。 |

### divider18+

divider(textDivider: Optional<DividerOptions | null>)

设置分割线样式，不设置该属性则按“默认值”展示分割线。与[divider12+](ts-basic-components-textpicker.md#divider12)相比，textDivider参数新增了对undefined类型的支持。

[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)中startMargin + endMargin 超过组件宽度后，startMargin和endMargin会被置0。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textDivider | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明) | null> | 是 | 默认值：  {  strokeWidth: '2px',  startMargin: 0,  endMargin: 0,  color: '#33000000'  }  1. 当textDivider的值为undefined时，使用默认值。  2. 当textDivider设置为有效的[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)时，按设置的样式显示分割线。  3. 当textDivider设置为null时，不显示分割线。 |

### gradientHeight12+

gradientHeight(value: Dimension)

设置渐隐效果的高度。若未设置该属性，则显示默认渐隐效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 内容区上下边缘的渐隐高度。  默认值：36vp  取值范围：[0, +∞)，支持百分比。  **说明：**  1. value设置为百分比时，100%为TextPicker高度的一半。  2. value设置为0时不显示渐隐效果。  3. value设置为数字且超过TextPicker高度的一半时，使用默认值。  4. 当value的值为负数时，使用默认值。 |

### gradientHeight18+

gradientHeight(height: Optional<Dimension>)

设置渐隐效果的高度。若未设置该属性，则显示默认渐隐效果。与[gradientHeight12+](ts-basic-components-textpicker.md#gradientheight12)相比，height参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Dimension](ts-types.md#dimension10)> | 是 | 内容区上下边缘的渐隐高度。  默认值：36vp  取值范围：[0, +∞)，支持百分比。  **说明：**  1. height设置为百分比时，100%为TextPicker高度的一半。  2. height设置为0时不显示渐隐效果。  3. height设置为数字且超过TextPicker高度的一半时，使用默认值。  4. 当height的值为undefined或负数时，使用默认值。 |

### disableTextStyleAnimation15+

disableTextStyleAnimation(disabled: boolean)

设置是否关闭滑动过程中文本样式变化的动效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disabled | boolean | 是 | 是否关闭滑动过程中文本样式变化的动效。  - true：关闭文本样式变化动效。  - false：不关闭文本样式变化动效。  默认值：false  **说明：**  设置为true时，滑动过程中无字号、字重、字体颜色等变化动效，且文本均显示为[defaultTextStyle](ts-basic-components-textpicker.md#defaulttextstyle15)属性设置的样式。如未设置[defaultTextStyle](ts-basic-components-textpicker.md#defaulttextstyle15)，则显示为[Text](ts-basic-components-text.md)组件默认样式。设置为false时，使用系统默认的滑动文本样式变化动效。 |

### defaultTextStyle15+

defaultTextStyle(style: TextPickerTextStyle)

设置关闭滑动过程中文本样式变化的动效时，各个选项的文本样式。仅当[disableTextStyleAnimation](ts-basic-components-textpicker.md#disabletextstyleanimation15)为true时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明) | 是 | 设置关闭滑动过程中文本样式变化的动效时，各个选项的文本样式。  默认值：与[Text](ts-basic-components-text.md)组件默认值相同。 |

### enableHapticFeedback18+

enableHapticFeedback(enable: Optional<boolean>)

设置是否开启触控反馈。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  设置为true后，其生效情况取决于系统的硬件是否支持。若硬件不支持触控反馈功能，开启该功能不会产生触控反馈效果，也不会抛出异常。 |

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```json
"requestPermissions": [
   {
      "name": "ohos.permission.VIBRATE"
   }
]
```

### digitalCrownSensitivity18+

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置表冠灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CrownSensitivity](ts-appendix-enums.md#crownsensitivity18)> | 是 | 表冠响应灵敏度。  默认值：CrownSensitivity.MEDIUM，响应速度适中。不同灵敏度值影响表冠滚动速度与选择项切换速度的对应关系，具体各枚举值的效果请参考[CrownSensitivity](ts-appendix-enums.md#crownsensitivity18)。 |

**说明** 

用于圆形屏幕的穿戴设备。组件响应[表冠事件](ts-universal-events-crown.md)，需要先获取焦点。

### selectedBackgroundStyle20+

selectedBackgroundStyle(style: Optional<PickerBackgroundStyle>)

设置选中项的背景样式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerBackgroundStyle](ts-basic-components-textpicker.md#pickerbackgroundstyle20)> | 是 | 选中项背景的颜色和边框圆角半径，多列模式时会同时设置所有列的选中项背景的颜色和圆角半径。  默认值：  {  color: $r('sys.color.comp\_background\_tertiary'),  borderRadius: $r('sys.float.corner\_radius\_level12')  } |

## 事件

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

onChange(callback: (value: string | string[], index: number | number[]) => void)

滑动TextPicker文本内容后，选项归位至选中项位置时，触发该回调。当用户滑动选择器导致选中项变化时触发，不能通过修改双向绑定的状态变量（如selected）来触发。当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[]10+ | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。  **说明：**  当显示文本或图片加文本列表时，value值为选中项中的文本值；当显示图片列表时，value值为空。 |
| index | number | number[]10+ | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

### onChange18+

onChange(callback: Optional<OnTextPickerChangeCallback>)

滑动TextPicker文本内容后，选项归位至选中项位置时，触发该回调。当用户滑动选择器导致选中项变化时触发，不能通过修改双向绑定的状态变量（如selected）来触发。当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。与[onChange](ts-basic-components-textpicker.md#onchange)相比，callback参数新增了对undefined类型的支持。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnTextPickerChangeCallback](ts-basic-components-textpicker.md#ontextpickerchangecallback18)> | 是 | 滑动选中TextPicker文本内容后，触发的回调。  当callback的值为undefined时，不使用回调函数。 |

### onScrollStop14+

onScrollStop(callback: TextPickerScrollStopCallback)

文本选择器的选项列滑动停止时触发该事件。

手指拖动选项列触发的滑动，手指离开屏幕且滑动停止时会触发该事件。

**说明** 

* 与[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)事件的差别在于，onScrollStop关注的是滚动行为完全停止，onEnterSelectedArea关注的是选项进入选中区域的逻辑状态。onEnterSelectedArea能更早响应索引变化，适合实时反馈场景，建议使用[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)；若需确认滚动行为完全停止，则使用onScrollStop。
* 从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TextPickerScrollStopCallback](ts-basic-components-textpicker.md#textpickerscrollstopcallback14) | 是 | 文本选择器的选项列滑动停止时触发该事件。回调签名：(value: string | string[], index: number | number[]) => void，其中value为当前选中项的文本，index为当前选中项的索引值（从0开始）。 |

### onScrollStop18+

onScrollStop(callback: Optional<TextPickerScrollStopCallback>)

文本选择器的选项列滑动停止时触发该事件。与[onScrollStop14+](ts-basic-components-textpicker.md#onscrollstop14)相比，callback参数新增了对undefined类型的支持。

手指拖动选项列触发的滑动，手指离开屏幕且滑动停止时会触发该事件。

**说明** 

* 与[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)事件的差别在于，onScrollStop关注的是滚动行为完全停止，onEnterSelectedArea关注的是选项进入选中区域的逻辑状态。onEnterSelectedArea能更早响应索引变化，适合实时反馈场景，建议使用[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)；若需确认滚动行为完全停止，则使用onScrollStop。
* 从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[TextPickerScrollStopCallback](ts-basic-components-textpicker.md#textpickerscrollstopcallback14)> | 是 | 文本选择器的选项列滑动停止时触发该事件。  当callback的值为undefined时，不使用回调函数。 |

### onEnterSelectedArea18+

onEnterSelectedArea(callback: TextPickerEnterSelectedAreaCallback)

滑动TextPicker过程中，选项进入分割线区域内（当前列的滑动距离超过选中项高度的一半）时，触发该回调。

**说明** 

* 与[onChange](ts-basic-components-textpicker.md#onchange)事件的差别在于，该事件的触发时机早于[onChange](ts-basic-components-textpicker.md#onchange)事件。onEnterSelectedArea在滑动过程中选项进入选中区域时触发，适合实时获取索引值变化，适用于需要快速响应用户滑动的场景；onChange在滑动结束且选中项归位后触发，适合获取最终确认的选中值，适用于需要获取用户最终选择的场景。
* 与[onScrollStop](ts-basic-components-textpicker.md#onscrollstop14)事件的差别在于，onEnterSelectedArea关注的是选项进入选中区域的逻辑状态，onScrollStop关注的是滚动行为完全停止。需要更早响应索引变化时使用onEnterSelectedArea，需要确认滚动完全停止时使用[onScrollStop](ts-basic-components-textpicker.md#onscrollstop14)。
* 在多列联动场景中，不建议使用该回调。该回调标识的是滑动过程中选项进入分割线区域内的节点；跟随变化的选项并不涉及滑动，因此回调返回值中仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TextPickerEnterSelectedAreaCallback](ts-basic-components-textpicker.md#textpickerenterselectedareacallback18) | 是 | 滑动TextPicker过程中，选项进入分割线区域时触发的回调。回调签名：(value: string | string[], index: number | number[]) => void，其中value为当前选中项的文本，index为当前选中项的索引值（从0开始）。 |

### onAccept(deprecated)

onAccept(callback: (value: string, index: number) => void)

点击弹窗中的“确定”按钮时触发该回调。该事件仅在[文本滑动选择器弹窗](ts-methods-textpicker-dialog.md)中生效。

**说明** 

从API version 8开始支持，从API version 10开始废弃。此接口已完全移除，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前选中项的文本。 |
| index | number | 是 | 当前选中项的索引值，索引从0开始。 |

### onCancel(deprecated)

onCancel(callback: () => void)

点击弹窗中的“取消”按钮时触发该回调。该事件仅在[文本滑动选择器弹窗](ts-methods-textpicker-dialog.md)中生效。

**说明** 

从API version 8开始支持，从API version 10开始废弃。此接口已完全移除，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 点击弹窗中的“取消”按钮时触发该回调。 |

## TextPickerTextStyle15+类型说明

文本样式选项，继承自[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minFontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本最小显示字号，与maxFontSize配合使用。当需要限制文本的最小显示尺寸以避免文本过小或需要实现字号自适应时传入此参数。  **说明**：当设置minFontSize和maxFontSize时，font中的size将不生效。默认最大行数为1，自适应高度方式为MIN\_FONT\_SIZE\_FIRST。详细规则请参考Text组件的[minFontSize](ts-basic-components-text.md#minfontsize)属性。 |
| maxFontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本最大显示字号，与minFontSize配合使用。当需要限制文本的最大显示尺寸以避免文本过大或需要实现字号自适应时传入此参数。  **说明**：当设置minFontSize和maxFontSize时，font中的size将不生效。详细规则请参考Text组件的[maxFontSize](ts-basic-components-text.md#maxfontsize)属性。 |
| overflow | [TextOverflow](ts-appendix-enums.md#textoverflow) | 否 | 是 | 文本截断方式。当设置为MARQUEE时，该属性不生效。详细规则请参考Text组件的[textOverflow](ts-basic-components-text.md#textoverflow)属性。 |

## OnTextPickerChangeCallback18+

type OnTextPickerChangeCallback = (selectItem: string | string[], index: number | number[]) => void

定义触发onChange事件的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectItem | string | string[]10+ | 是 | 当前选中项的文本。多列数据选择器的selectItem为数组类型。  **说明：**  当选择器内容为文本或图文混排时，selectItem值为选中项中的文本值；当选择器内容为图片时，selectItem值为空。 |
| index | number | number[]10+ | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

## TextPickerScrollStopCallback14+

type TextPickerScrollStopCallback = (value: string | string[], index: number | number[]) => void

定义触发onScrollStop事件的回调类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[] | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。  **说明：**  当选择器内容为文本或图文混排时，value值为选中项中的文本值；当选择器内容为图片时，value值为空。 |
| index | number | number[] | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

## TextPickerEnterSelectedAreaCallback18+

type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void

定义触发onEnterSelectedArea事件的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[] | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。  **说明：**  当选择器内容为文本或图文混排时，value值为选中项中的文本值；当选择器内容为图片时，value值为空。 |
| index | number | number[] | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

## PickerBackgroundStyle20+

选择器选中项的背景样式，包括选中项的背景颜色和边框圆角半径。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 选中项的背景颜色。  默认值：  'sys.color.comp\_background\_tertiary'  **说明**：未设置该属性时，使用默认值。 |
| borderRadius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 选中项的边框圆角半径。  默认值：{ value:24, unit:LengthUnit.VP }，即四个圆角半径均为24vp。  单位：默认为vp，可通过LengthMetrics或LocalizedBorderRadiuses类型指定单位。  **说明：**  1. [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)类型的value参数同时作用于四个圆角半径大小，unit参数用于设置单位。  2. [BorderRadiuses](ts-types.md#borderradiuses9)类型可以设置四个不同值的圆角半径，所有单位固定为vp。  3. [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12)类型可以设置四个不同值的圆角半径，并且可以单独设置每个圆角的单位。 |

## 示例

### 示例1（设置选择器列数）

该示例通过配置range实现单列数据选择器和多列数据选择器，并使用columnWidths调整每一列的宽度。

从API version 18开始，新增了[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)的columnWidths属性。

```ts
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private apfruits: string[] = ['apple1', 'apple2', 'apple3', 'apple4'];
  private orfruits: string[] = ['orange1', 'orange2', 'orange3', 'orange4'];
  private pefruits: string[] = ['peach1', 'peach2', 'peach3', 'peach4'];
  private multi: string[][] = [this.apfruits, this.orfruits, this.pefruits];
  private cascade: TextCascadePickerRangeContent[] = [
    {
      text: '辽宁省',
      children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },
        { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]
    },
    {
      text: '吉林省',
      children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },
        { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]
    },
    {
      text: '黑龙江省',
      children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },
        { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]
    }
  ];
  private singleColumnWidths: LengthMetrics[] = [
    LengthMetrics.percent(50)
  ];

  private multipleColumnWidths: LengthMetrics[] = [
    LengthMetrics.vp(100),
    LengthMetrics.vp(200),
    LengthMetrics.vp(100)
  ];

  private cascadeColumnWidths: LengthMetrics[] = [
    LengthMetrics.percent(20),
    LengthMetrics.percent(30),
    LengthMetrics.percent(50)
  ];
  build() {
    Column() {

      TextPicker({ range: this.apfruits, selected: this.select, columnWidths: this.singleColumnWidths })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        }).margin({ bottom: 50 })
        .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
          console.info('Picker item enter selected area, value: ' + value + ', index: ' + index);
        })

      TextPicker({ range: this.multi, columnWidths: this.multipleColumnWidths })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列:onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        }).margin({ bottom: 50 })
        .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列:onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })

      TextPicker({ range: this.cascade, columnWidths: this.cascadeColumnWidths })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列联动:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列联动:onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列联动:onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/R9TIwfvmTh-EY_xhRz2aYQ/zh-cn_image_0000002736314975.png)

### 示例2（设置文本样式）

该示例使用[disappearTextStyle](ts-basic-components-textpicker.md#disappeartextstyle10)、[textStyle](ts-basic-components-textpicker.md#textstyle10)、[selectedTextStyle](ts-basic-components-textpicker.md#selectedtextstyle10)设置文本选择器中的文本样式。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 0;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({ color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } })
        .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
        .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
        .defaultPickerItemHeight(50)
        .canLoop(false)
        .selectedIndex(2)
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/g_0GRc85ROa_gur44akG-A/zh-cn_image_0000002706675932.gif)

### 示例3（设置无分割线样式）

该示例通过配置[divider](ts-basic-components-textpicker.md#divider12)为null实现无分割线样式的文本选择器。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 0;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({ color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } })
        .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
        .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
        .divider(null)
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8L6nlek7Qq2hhWWoUCRKWQ/zh-cn_image_0000002736435019.gif)

### 示例4（设置分割线样式）

该示例通过配置divider的DividerOptions设置文本选择器的分割线样式。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({ color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } })
        .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
        .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
        .divider({
          strokeWidth: 10,
          color: Color.Red,
          startMargin: 10,
          endMargin: 20
        } as DividerOptions)
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/r5RZGuoVQ5ys4hTPeP0KfQ/zh-cn_image_0000002706835872.gif)

### 示例5（设置渐隐效果）

该示例通过配置[gradientHeight](ts-basic-components-textpicker.md#gradientheight12)设置文本选择器的渐隐效果高度。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({ color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } })
        .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
        .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
        .gradientHeight(100)
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/TFXlHgn9TsCTPEkH1L1baw/zh-cn_image_0000002736314977.gif)

### 示例6（设置选择项高度）

该示例通过配置[defaultPickerItemHeight](ts-basic-components-textpicker.md#defaultpickeritemheight)设置选择项的高度。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .defaultPickerItemHeight(60)
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/LuWepY7XSza-hrh-rDtoWA/zh-cn_image_0000002706675934.png)

### 示例7（设置循环滚动）

该示例通过配置[canLoop](ts-basic-components-textpicker.md#canloop10)设置文本选择器是否循环滚动。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  @State isLoop: boolean = false;
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .canLoop(this.isLoop)

      Row() {
        Text('循环滚动').fontSize(20)

        Toggle({ type: ToggleType.Switch, isOn: false })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })

    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/TATz9GoARbigDLXyKxKlyA/zh-cn_image_0000002736435021.gif)

### 示例8（设置选中项索引值）

该示例通过配置[selectedIndex](ts-basic-components-textpicker.md#selectedindex10)设置默认选中项的索引值。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: 1 })
        .selectedIndex(2)
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/0QqkO3xPRWSqVGG54xHT3Q/zh-cn_image_0000002706835874.png)

### 示例9（设置关闭文本样式变化动效与对应文本样式）

该示例通过配置[disableTextStyleAnimation](ts-basic-components-textpicker.md#disabletextstyleanimation15)、[defaultTextStyle](ts-basic-components-textpicker.md#defaulttextstyle15)实现关闭文本选择器文本样式变化的动效，并设置文本样式。

从API version 15开始，新增disableTextStyleAnimation、defaultTextStyle接口。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        .disableTextStyleAnimation(true)
        .margin({ bottom: 30 })
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        .disableTextStyleAnimation(true)
        .defaultTextStyle({ minFontSize: 18, maxFontSize: 28, overflow: TextOverflow.Ellipsis })
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/C3NUQohsRX28xCtFSlRtyg/zh-cn_image_0000002736314979.jpeg)

### 示例10（设置选中项背景样式）

该示例通过配置[selectedBackgroundStyle](ts-basic-components-textpicker.md#selectedbackgroundstyle20)实现文本选择器选中项的背景样式。

```ts
import { LengthUnit } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private showText1: string [] =
    ['Text1', 'Text1', 'Text1', 'Text1']
  private showText2: string[] [] =
    [
      ['Text2', 'Text2', 'Text2', 'Text2'],
      ['Text3', 'Text3', 'Text3', 'Text3']
  ]

  build() {
    Column() {
      Row() {
        TextPicker({ range: this.showText1 })
          .selectedBackgroundStyle({
            color: '#FFD5D5D5',
            borderRadius: { value: 0, unit: LengthUnit.VP }
          })
        Column()
          .width('10%')
        TextPicker({ range: this.showText1 })
          .selectedBackgroundStyle({
            color: '#FFE3F8F9',
            borderRadius: {
              topStart: { value: 5, unit: LengthUnit.VP },
              topEnd: { value: 10, unit: LengthUnit.VP },
              bottomStart: { value: 15, unit: LengthUnit.VP },
              bottomEnd: { value: 20, unit: LengthUnit.VP }
            }
          })
      }

      Row()
        .height('10%')
      Row() {
        TextPicker({ range: this.showText2 })
          .selectedBackgroundStyle({
            borderRadius: {
              topLeft: 8,
              topRight: 8,
              bottomLeft: 8,
              bottomRight: 8
            },
            color: '#FFFFEEF6'
          })
      }
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/pWoJABLYRSONuIC4EG2qew/zh-cn_image_0000002706675936.gif)

### 示例11（设置文本的最大字号、最小字号、超长文本截断方式）

该示例通过配置[disappearTextStyle](ts-basic-components-textpicker.md#disappeartextstyle20)、[textStyle](ts-basic-components-textpicker.md#textstyle20)和[selectedTextStyle](ts-basic-components-textpicker.md#selectedtextstyle20)，设置文本的颜色、最大字号、最小字号、超长文本截断方式。

从API version 20开始，新增disappearTextStyle、textStyle和selectedTextStyle接口。

```ts
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private rangeValue: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEEEEEEEEEEEEEE'];

  build() {
    RelativeContainer() {
      TextPicker({
        range: this.rangeValue
      })
        .disappearTextStyle({
          color: '#fff52769',
          // 设置minFontSize与maxFontSize时，font中的size属性将被忽略。
          font: { size: 50 },
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.Ellipsis
        })
        .textStyle({
          color: Color.Orange,
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.MARQUEE
        })
        .selectedTextStyle({
          color: '#ff9eea48',
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.Clip
        })
        .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/rtLwyMecTuiQUPoiNe87GQ/zh-cn_image_0000002736435023.gif)
